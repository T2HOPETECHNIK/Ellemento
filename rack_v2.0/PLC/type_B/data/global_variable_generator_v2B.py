"""
    Global Variable Generator:

    Function:
    - generate a csv file that contains all shelf-related global variable
      based on the inputs in global_variable_template.xlsx
    - csv file can be imported into Delta ISPSoft

    How to use:
    - configure parameter in global_variable_template.xlsx
    - run this script at the same directory as global_variable_template.xlsx
    - global_variable_table.csv will be generated upon script completion
"""

from typing import Union
import sys
import os
import csv
import pandas as pd
import numpy as np
import re
import struct

import json

ignore_SCADA_filter = True
SCADA_filter_names = ['pumpFillDrainMode0','pumpFillValue0']
server_filter_names = ['pumpFillDrainMode0','pumpFillValue0']
server_labels = ['PumpFillDrain', 'PumpFillValue']

def main():

    # parameter
    if len(sys.argv) == 2:
        input_name = sys.argv[1]
    else:
        input_name = "global_variable_template.xlsx"
    global_var_table_name = "global_variable_table.csv"
    plc2_global_var_table_name = "plc2_global_variable_table.csv"
    SCADA_var_table_name = "SCADA_import.csv"
    server_var_table_name = "server_import.csv"
    hmi_tag_table_name = "hmi_tag.csv"
    hmi_tag_plc_name = "{EtherLink1}1@"

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = os.path.join(curr_dir, input_name)

    # extract tables from excel
    constant_table = pd.read_excel(dir_name, sheet_name="Constants")
    shelf_table = pd.read_excel(dir_name, sheet_name="Shelf")
    sensor_list_table = pd.read_excel(dir_name, sheet_name="Sensor List")
    sensor_data_table = pd.read_excel(dir_name, sheet_name="Sensor Data")
    pump_data_table = pd.read_excel(dir_name, sheet_name="Pump")
    io_mapping_table = pd.read_excel(dir_name, sheet_name="IO Mapping")
    hmi_data_table = pd.read_excel(dir_name, sheet_name="HMI Internal")
    # for second PLC
    plc2_io_table = pd.read_excel(dir_name, sheet_name="PLC2 Global")

    # read data from tables
    constant_base_addr, constants = read_var_table(constant_table)
    shelf_base_addr, shelfs = read_var_table(shelf_table)
    sensor_base_addr, sensors = read_sensor_list_table(sensor_list_table)
    sensor_data = read_var_table(sensor_data_table)[1]
    pump_base_addr, pumps = read_var_table(pump_data_table)
    io_data = read_io_mapping_table(io_mapping_table)
    hmi_base_addr, hmi_internal = read_hmi_internal_table(hmi_data_table)
    # PLC 2
    plc2_io_data = read_plc2_mapping_table(plc2_io_table)

    # define common properties
    shelf_no = constants['shelf_no']['init_value']
    assert("shelf_no" in constants) == True

    global_var_table = {}
    hmi_tag_table = {}
    plc2_global_var_table = {}
    SCADA_tag_table = {}

    # parse constants and write into global_var_table
    constant_curr_addr = constant_base_addr
    for var_name in constants:
        var_data = constants[var_name]
		
        addr = "D{}".format(round(float(constant_curr_addr), 1) if "BOOL" in var_data['type'] else int (constant_curr_addr) )
        constant_curr_addr += int(var_data['addr_offset'])
        
        write_rec_glob_var_table(global_var_table, var_name, addr, var_data['type'], var_data['init_value'], var_data['comment'], var_data['retain'])

    # parse pump_data and write into global_var_table
    pump_curr_addr = pump_base_addr
    for var_name in pumps:
        pump_data = pumps[var_name]

        addr = "D{}".format( round(float(pump_curr_addr), 1) if "BOOL" in pump_data['type'] else int (pump_curr_addr) )
        pump_curr_addr += int(pump_data['addr_offset'])
        write_rec_glob_var_table(global_var_table, var_name, addr, pump_data['type'], pump_data['init_value'], pump_data['comment'], var_data['retain'])
        
    # parse shelfs and write into global_var_table
    shelf_curr_addr = shelf_base_addr
    for i in range(shelf_no):
        for var_name in shelfs:
            shelf_data = shelfs[var_name]
            name = "s{}_{}".format(i, var_name)

            addr = "D{}".format( round(float(shelf_curr_addr), 1) if "BOOL" in shelf_data['type'] else int (shelf_curr_addr))
            shelf_curr_addr += int(shelf_data['addr_offset'])

            write_rec_glob_var_table(global_var_table, name, addr, shelf_data['type'], shelf_data['init_value'], shelf_data['comment'], var_data['retain'])
    
    # parse constants and write into hmi_tag_table
    constant_curr_addr = constant_base_addr
    for var_name in constants:
        var_data = constants[var_name]
		
        # filter those that should go into hmi_tag
        if not var_data['hmi_tag']:
            constant_curr_addr += var_data['addr_offset']
            continue

        # check if variable is an array
        if "ARRAY" in var_data['type']:
            array_size = get_array_size(var_data['type'])
            array_type = get_array_type(var_data['type'])
            constant_arr_addr = constant_curr_addr

            int_addr = int(constant_arr_addr)

            for j in range(array_size):
                name = f"{var_name}{j}"

                addr_offset = calc_addr_offset_hmi_tag(is_array=True, var_type=array_type, 
                                                       offset=var_data['addr_offset'])

                var_type = translate_var_type_hmi_tag(var_type=array_type)

                # special case
                if "BOOL" in var_data['type']:
                    raw_addr = "D" + get_hmi_bit_address(offset=int_addr, size=array_size, index=j)
                    addr = hmi_tag_plc_name + raw_addr

                else:
                    addr = hmi_tag_plc_name + \
                        "D{}".format( round(float(constant_arr_addr), 1) if "BOOL" in var_data['type'] else int (constant_arr_addr) )

                    #raw_addr is without the "{EtherLink1}1@" in "{EtherLink1}1@D20020", just D20020
                    raw_addr = "D{}".format( round(float(constant_arr_addr), 1) if "BOOL" in var_data['type'] else int (constant_arr_addr) )

                constant_arr_addr += addr_offset
                write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, var_data['comment'])

            constant_curr_addr += var_data['addr_offset']

        # non-array variable
        else:
            name = f"{var_name}"
            addr_offset = calc_addr_offset_hmi_tag(is_array=False, var_type=var_data['type'], 
                                                offset=var_data['addr_offset'])
            var_type = translate_var_type_hmi_tag(var_type=var_data['type'])
            addr = hmi_tag_plc_name + \
                "D{}".format( round(float(constant_curr_addr), 1) if "BOOL" in var_data['type'] else int (constant_curr_addr))

            raw_addr = "D{}".format( round(float(constant_curr_addr), 1) if "BOOL" in var_data['type'] else int (constant_curr_addr) )
				
            write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, var_data['comment'])
            constant_curr_addr += addr_offset
    
    # parse pump_data and write into hmi_tag_table
    pump_curr_addr = pump_base_addr
    for var_name in pumps:
        pump_data = pumps[var_name]

        # filter those that should go into hmi_tag
        if not pump_data['hmi_tag']:
            pump_curr_addr += pump_data['addr_offset']
            continue

        # check if variable is an array
        if "ARRAY" in pump_data['type']:
            array_size = get_array_size(pump_data['type'])
            array_type = get_array_type(pump_data['type'])
            pump_arr_addr = pump_curr_addr

            for j in range(array_size):
                name = f"{var_name}{j}"
                addr_offset = calc_addr_offset_hmi_tag(is_array=True, var_type=array_type, 
                                                       offset=pump_data['addr_offset'])
                var_type = translate_var_type_hmi_tag(var_type=array_type)

                addr = hmi_tag_plc_name + \
                       "D{}".format( round(float(pump_arr_addr), 1) if "BOOL" in pump_data['type'] else int (pump_arr_addr) )

                raw_addr = "D{}".format( round(float(pump_arr_addr), 1) if "BOOL" in var_data['type'] else int (pump_arr_addr) )
                
                pump_arr_addr += addr_offset

                write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, pump_data['comment'])

            pump_curr_addr += pump_data['addr_offset']

        # non-array variable
        else:
            name = f"{var_name}"
            addr_offset = calc_addr_offset_hmi_tag(is_array=False, var_type=pump_data['type'], 
                                                   offset=pump_data['addr_offset'])
            var_type = translate_var_type_hmi_tag(var_type=pump_data['type'])

            addr = hmi_tag_plc_name + \
                   "D{}".format( round(float(pump_curr_addr), 1) if "BOOL" in shelf_data['type'] else int (pump_curr_addr))

            raw_addr = "D{}".format( round(float(pump_curr_addr), 1) if "BOOL" in shelf_data['type'] else int (pump_curr_addr))

            write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, pump_data['comment'])
			
            pump_curr_addr += addr_offset
        
    # parse shelfs and write into hmi_tag_table
    shelf_curr_addr = shelf_base_addr
    for i in range(shelf_no):
        for var_name in shelfs:
            shelf_data = shelfs[var_name]

            # filter those that should go into hmi_tag
            if not shelf_data['hmi_tag']:
                shelf_curr_addr += shelf_data['addr_offset']
                continue

            # check if variable is an array
            if "ARRAY" in shelf_data['type']:
                array_size = get_array_size(shelf_data['type'])
                array_type = get_array_type(shelf_data['type'])
                shelf_arr_addr = shelf_curr_addr

                for j in range(array_size):
                    name = f"s{i}_{var_name}{j}"

                    addr_offset = calc_addr_offset_hmi_tag(is_array=True, var_type=array_type,
                                                           offset=shelf_data['addr_offset'])
                    var_type = translate_var_type_hmi_tag(var_type=array_type)

                    addr = hmi_tag_plc_name + \
                           "D{}".format( round(float(shelf_arr_addr),1) if "BOOL" in shelf_data['type'] else int (shelf_arr_addr))

                    raw_addr = "D{}".format( round(float(shelf_arr_addr),1) if "BOOL" in shelf_data['type'] else int (shelf_arr_addr))
                    
                    shelf_arr_addr += addr_offset
                    write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, shelf_data['comment'])

                shelf_curr_addr += shelf_data['addr_offset']

            # non-array variable
            else:
                name = f"s{i}_{var_name}"

                addr_offset = calc_addr_offset_hmi_tag(is_array=False, var_type=array_type, offset=shelf_data['addr_offset'])
                var_type = translate_var_type_hmi_tag(var_type=shelf_data['type'])

                addr = hmi_tag_plc_name + \
                        "D{}".format( round(float(shelf_curr_addr), 1) if "BOOL" in shelf_data['type'] else int (shelf_curr_addr))

                raw_addr = "D{}".format( round(float(shelf_curr_addr), 1) if "BOOL" in shelf_data['type'] else int (shelf_curr_addr))

                write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, shelf_data['comment'])
				
                shelf_curr_addr += addr_offset

    # parse sensors, sensor_data and write into global_var_table
    # parse sensors, sensor_data and write into hmi_tag_table
    addr_offset = 1
    for i in range(shelf_no):
        for snsr_name in sensors['shelf_sensors']:
            for j, var_name in enumerate(sensor_data):
                data = sensor_data[var_name]
                name = "snsr_s{}_{}_{}".format(i, snsr_name, var_name)
                
                # for global_var_table
                addr = "D{}".format(sensor_base_addr + addr_offset)
                write_rec_glob_var_table(global_var_table, name, addr, data['type'], data['init_value'], data['comment'], data['retain'])

                # for hmi_tag_table
                addr = hmi_tag_plc_name + "D{}".format(sensor_base_addr + addr_offset)

                raw_addr = "D{}".format(sensor_base_addr + addr_offset)

                write_rec_hmi_tag_table(hmi_tag_table, name, data['type'], addr, raw_addr, data['comment'])

                addr_offset += 1

    for snsr_name in sensors['other_sensors']:
        for i, var_name in enumerate(sensor_data):
            data = sensor_data[var_name]
            name = "snsr_{}_{}".format(snsr_name, var_name)

            # for global_var_table
            addr = "D{}".format(sensor_base_addr + addr_offset)
            write_rec_glob_var_table(global_var_table, name, addr, data['type'], data['init_value'], data['comment'], data['retain'])
            
            # for hmi_tag_table
            addr = hmi_tag_plc_name + "D{}".format(sensor_base_addr + addr_offset)
            raw_addr = "D{}".format(sensor_base_addr + addr_offset)
            write_rec_hmi_tag_table(hmi_tag_table, name, data['type'], addr, raw_addr, data['comment'])
            
            addr_offset += 1

    
    # parse io_data and write into global_var_table & hmi_tag_table
    for io_name in io_data:
        io = io_data[io_name]
        write_rec_glob_var_table(global_var_table, io_name, io['addr'], io['type'], io['init_value'], io['comment'], io['retain'])

        if "ARRAY" in io['type']:
            array_size = get_array_size(io['type'])
            array_type = get_array_type(io['type'])
            constant_arr_addr = int(re.sub(r"\D", "", io['addr']))

            for j in range(array_size):
                name = f"{io_name}{j}"
                var_type = translate_var_type_hmi_tag(var_type=array_type)
                if array_type == "BOOL":
                    array_elem_size = 1
                elif array_type == "WORD":
                    array_elem_size = 1
                elif array_type == "DWORD":
                    array_elem_size = 2
                else:
                    array_elem_size = 1
                addr = hmi_tag_plc_name + 'D' + str(constant_arr_addr + (j * array_elem_size))

                raw_addr = 'D' + str(constant_arr_addr + (j * array_elem_size))

                write_rec_hmi_tag_table(hmi_tag_table, name, var_type, addr, raw_addr, io['comment'])

            
        else:
            if io['type'] == "BOOL":
                io_var_type = "BIT"
            else:
                io_var_type = io['type']

            if io['hmi_tag']:
                addr = hmi_tag_plc_name + io['addr']

                raw_addr = io['addr']
                write_rec_hmi_tag_table(hmi_tag_table, io_name, io_var_type, addr, raw_addr, io['comment'])
                #write_rec_hmi_tag_table(hmi_tag_table, io_name, io['type'], addr, io['comment'])


    # parse hmi_internal and write into hmi_tag_table
    hmi_curr_addr =  hmi_base_addr
    for var_name in hmi_internal:

        addr = "$"
        hmi_data = hmi_internal[var_name]
        if hmi_data['type'] == "BIT":
            addr += str(round(float(hmi_curr_addr), 1))
        elif hmi_data['type'] == "WORD" or hmi_data['type'] == "INT":
            addr += str(hmi_curr_addr)
        else:
            raise RuntimeError("Invalid type")

        raw_addr = str(hmi_curr_addr)

        write_rec_hmi_tag_table(hmi_tag_table, var_name, hmi_data['type'], addr, raw_addr, hmi_data['comment'])
		
        hmi_curr_addr += int(hmi_data['addr_offset'])

    # write global_var_table into global_variable_table.csv
    write_glob_var_table_to_csv(global_var_table_name, global_var_table)

    # write hmi_tag_table into hmi_tag_table.csv
    write_hmi_tag_table_to_csv(hmi_tag_table_name, hmi_tag_table)
	
    # write hmi_tag_table to SCADA file.csv (with extra filters of course)
    write_SCADA_tag_table_to_csv(SCADA_var_table_name, hmi_tag_table)

    # for server import
    write_server_tag_table_to_csv(server_var_table_name, hmi_tag_table)
    
    # parse io_data and write into global_var_table & hmi_tag_table
    for io_name in plc2_io_data:
        io = plc2_io_data[io_name]
        write_rec_glob_var_table(plc2_global_var_table, io_name, io['addr'], io['type'], io['init_value'], io['comment'], io['retain'])
		
    write_glob_var_table_to_csv(plc2_global_var_table_name, plc2_global_var_table)

# ============================================================================

# This function converts an array address to bit address
def get_hmi_bit_address(offset:int, size: int, index: int):
    
	new_offset = offset + (index // 16)
	addr = str(new_offset) + "." + str(index % 16)
	return addr



def read_var_table(s_table: dict) -> dict:
    s_dict = {}
    if s_table['base_addr'].tolist()[0] != "-":
        s_base_addr = int(s_table['base_addr'].tolist()[0])
    else:
        s_base_addr = None
    s_names = s_table['variable_name'].tolist()
    s_addr_offsets = s_table['addr_offset'].tolist()
    s_types = s_table['type'].tolist()
    s_init_values = s_table['init_value'].tolist()
    s_hmi_tags = s_table['hmi_tag'].tolist()
    s_comments = s_table['comment'].tolist()
    s_var_retain = s_table['retain'].tolist()

    # inject name, addr_offset, type, init_value
    for s_name, s_addr_offset, s_type, s_init_value, s_hmi_tag, s_comment, s_var_retain \
        in zip (s_names, s_addr_offsets, s_types, s_init_values, s_hmi_tags, s_comments, s_var_retain):

        s_dict[s_name] = {
            'addr_offset': s_addr_offset,
            'type': s_type,
            'init_value': s_init_value,
            'hmi_tag': True if not pd.isna(s_hmi_tag) else False,
            'retain': True if not pd.isna(s_var_retain) else False,
            'comment' : s_comment
            }

    return s_base_addr, s_dict

def read_sensor_list_table(sl_table: dict) -> dict:
    sl_dict = {}
    sl_base_addr = int(sl_table['base_addr'].tolist()[0])
    shelf_sensors = [x for x in sl_table['shelf_sensor'].tolist() if not pd.isna(x)]
    other_sensors = [x for x in sl_table['general_sensor'].tolist() if not pd.isna(x)]

    sl_dict['shelf_sensors'] = shelf_sensors
    sl_dict['other_sensors'] = other_sensors

    return sl_base_addr, sl_dict


def read_io_mapping_table(io_table: dict) -> dict:
    io_dict = {}
    var_names = io_table['variable_name'].tolist()
    var_addrs = io_table['addr'].tolist()
    var_types = io_table['type'].tolist()
    var_init_values = io_table['init_value'].tolist()
    var_hmi_tags = io_table['hmi_tag'].tolist()
    var_comments = io_table['comment'].tolist()
    var_retain = io_table['retain'].tolist()

    # inject name, addr_offset, type, init_value
    for io_name, io_addr, io_type, io_init_value, io_hmi_tag, io_comment, io_retain \
        in zip (var_names, var_addrs, var_types, var_init_values, var_hmi_tags, var_comments, var_retain):

        io_dict[io_name] = {
            'addr': io_addr,
            'type': io_type,
            'init_value': io_init_value,
            'hmi_tag': True if not pd.isna(io_hmi_tag) else False,
            'retain': True if not pd.isna(io_retain) else False,
            'comment': io_comment
            }

    return io_dict


def read_plc2_mapping_table(plc2_io_table: dict) -> dict:
    plc2_io_dict = {}
    plc2_var_names = plc2_io_table['variable_name'].tolist()
    plc2_var_addrs = plc2_io_table['addr'].tolist()
    plc2_var_types = plc2_io_table['type'].tolist()
    plc2_var_init_values = plc2_io_table['init_value'].tolist()
    plc2_var_comments = plc2_io_table['comment'].tolist()
    plc2_var_retain = plc2_io_table['retain'].tolist()

    # inject name, addr_offset, type, init_value
    for io_name, io_addr, io_type, io_init_value, io_comment, io_retain \
        in zip (plc2_var_names, plc2_var_addrs, plc2_var_types, plc2_var_init_values, plc2_var_comments, plc2_var_retain):

        plc2_io_dict[io_name] = {
            'addr': io_addr,
            'type': io_type,
            'init_value': io_init_value,
            'comment': io_comment,
            'retain' : True if not pd.isna(io_retain) else False
            }

    return plc2_io_dict



def read_hmi_internal_table(h_table: dict) -> dict:
    h_dict = {}
    h_base_addr = int(h_table['base_addr'].tolist()[0])
    h_names = h_table['var_name'].tolist()
    h_addr_offsets = h_table['addr_offset'].tolist()
    h_types = h_table['var_type'].tolist()
    h_comments = h_table['comment'].tolist()

    # inject name, addr_offset, type
    for h_name, h_addr_offset, h_type, h_comment in zip (h_names, h_addr_offsets, h_types, h_comments):
        h_dict[h_name] = {
            'addr_offset': h_addr_offset,
            'type': h_type,
            'comment': h_comment
        }

    return h_base_addr, h_dict


def write_rec_glob_var_table(
    global_var_table: dict, var_name: str, var_addr: str, \
    var_type: str, var_init_value: str, var_comment: str, var_retain: str) -> None:

    global_var_table[var_name] = {
        "addr": var_addr,
        "type": var_type,
        "init_value": var_init_value,
        "comment": var_comment,
        "retain": var_retain
    }
	
    #print("=> " + var_name + " " + var_addr)

    return


def write_glob_var_table_to_csv(filename, global_var_table):

    header = ["Class", "Identifiers", "Address", "Type", "Initial Value", "Comment"]
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(curr_dir, filename), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        for var_name in global_var_table:
            var_data = global_var_table[var_name]

            #var_retain = 'VAR'

            if var_data['retain'] is None:
                var_retain = 'VAR'
            else:
                if var_data['retain']: 
                    var_retain = 'VAR_RETAIN'
                else:
                    var_retain = 'VAR'

            if isinstance(var_data['comment'], str):
                writer.writerow([var_retain, var_name, var_data['addr'], var_data['type'], var_data['init_value'], var_data['comment']])
            else:
                writer.writerow([var_retain, var_name, var_data['addr'], var_data['type'], var_data['init_value']])

    print("completed: ", filename)
	
	
def Check_filter(varname, filter_array):
    accepted = False
    for varn in filter_array:
        if varname == varn:
            accepted = True
		
    return accepted




def write_rec_hmi_tag_table(
    table: dict, var_name: str, var_type: str, var_addr: str, var_raw_addr: str, var_comment: str) -> None:

    table[var_name] = {
        "type": var_type,
        "addr": var_addr,
        "raw_addr": var_raw_addr,
        "desc": var_comment
    }

    return


def write_hmi_tag_table_to_csv(filename, hmi_tag_table):
    header = ['Define Name', 'Type', 'Address', 'Description']
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(curr_dir, filename), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        for var_name in hmi_tag_table:
            var_data = hmi_tag_table[var_name]
            if isinstance(var_data['desc'], str):
                writer.writerow([var_name, var_data['type'], var_data['addr'], var_data['desc']])
            else:
                writer.writerow([var_name, var_data['type'], var_data['addr']])

    print("completed: ", filename)



def write_SCADA_tag_table_to_csv(filename, io_tag_table):
    header = ['Define Name', 'Type', 'Address', 'Description']
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(curr_dir, filename), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        for var_name in io_tag_table:
            var_data = io_tag_table[var_name]

            if Check_filter(var_name, SCADA_filter_names) == True or ignore_SCADA_filter == True:
                if var_data['type'] == "BOOL":
                    SCADA_type = "Digital"
                else:
                    SCADA_type = "Analog"

                SCADA_varname = "The Port\\\\The Driver\\\\" + var_name

                if isinstance(var_data['desc'], str):
                    #writer.writerow([var_name, var_data['type'], var_data['addr'], var_data['desc']])
                    writer.writerow([SCADA_varname, var_data['desc'], SCADA_type, var_data['raw_addr']])
                else:
                    #writer.writerow([var_name, var_data['type'], var_data['addr']])
                    writer.writerow([SCADA_varname, "", SCADA_type, var_data['raw_addr']])

    print("completed: ", filename)


'''
# write address definition as CSV file
def write_server_tag_table_to_csv(filename, io_tag_table):
    #header = ['Label', 'Define Name', 'Type', 'Address', 'Description']
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    index = 0

    with open(os.path.join(curr_dir, filename), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #writer.writerow(header)

        for var_name in io_tag_table:
            var_data = io_tag_table[var_name]

            if Check_filter(var_name, server_filter_names) == True:

                srv_label = server_labels[index]

                if isinstance(var_data['desc'], str):
                    writer.writerow([srv_label, var_name, var_data['type'], var_data['raw_addr'], var_data['desc']])
                else:
                    writer.writerow([srv_label, var_name, var_data['type'], var_data['raw_addr']])

                index = index + 1

    print("completed: ", filename)
'''

# write address definition as json file
def write_server_tag_table_to_csv(filename, io_tag_table):
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    index = 0
    json_decoded = {}
    json_decoded['addresses'] = []

    for var_name in io_tag_table:
        var_data = io_tag_table[var_name]

        if Check_filter(var_name, server_filter_names) == True:
            srv_label = server_labels[index]
            json_decoded['addresses'].append({
                    srv_label: var_data['raw_addr']
                    })

            index = index + 1

    with open(filename, 'w') as outfile:
        json.dump(json_decoded, outfile)

    print("completed: ", filename)


def calc_addr_offset_hmi_tag(is_array: bool, var_type: str, offset: str) -> Union[int, float]:
    if var_type == "BOOL":
        return (0.1) if is_array else float(offset)
    elif var_type == "WORD" or var_type == "INT":
        return (1) if is_array else int(offset)
    else:
        raise RuntimeError("Invalid type")


def translate_var_type_hmi_tag(var_type: str) -> str:
    if var_type == "BOOL" or var_type == "BIT":
        return "BIT"
    elif var_type == "WORD":
        return "WORD"
    elif var_type == "INT":
        return "INT"
    else:
        raise RuntimeError("Invalid type")


def get_array_size(data: str) -> int:
    tmp = data.split(' ')
    return int(tmp[1].replace('[', '').replace(']',''))


def get_array_type(data: str) -> int:
    return data.split(' ')[3]


if __name__ == "__main__":
    print(struct.calcsize("P") * 8, "- bit Python")
    main()
