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

import os
import csv
import pandas as pd
import numpy as np


def main():

    input_name = "global_variable_template.xlsx"
    global_var_table_name = "global_variable_table.csv"
    hmi_tag_table_name = "hmi_tag.csv"

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = os.path.join(curr_dir, input_name)

    # extract tables from excel
    constant_table = pd.read_excel(dir_name, sheet_name="Constants")
    shelf_table = pd.read_excel(dir_name, sheet_name="Shelf")
    sensor_list_table = pd.read_excel(dir_name, sheet_name="Sensor List")
    sensor_data_table = pd.read_excel(dir_name, sheet_name="Sensor Data")

    #####################

    # read data from tables
    constants = read_const_table(constant_table)
    shelf_base_addr, shelfs = read_shelf_table(shelf_table)
    sensor_base_addr, sensors = read_sensor_list_table(sensor_list_table)
    sensor_data = read_sensor_data_table(sensor_data_table)

    # define common properties
    shelf_no = constants['shelf_no']['init_value']
    shelf_reg_size = constants['shelf_reg_size']['init_value']

    # ensure user has defined shelf_no and shelf_reg_size
    assert("shelf_no" in constants) and ("shelf_reg_size" in constants) == True

    global_var_table = {}
    hmi_tag_table = {}

    # parse constants and write into global_var_table
    for var_name in constants:
        var_data = constants[var_name]
        addr = "D{}".format(var_data['addr'])
        write_rec_glob_var_table(global_var_table, var_name, addr, var_data['type'], var_data['init_value'])

    # parse shelfs and write into global_var_table
    for i in range(shelf_no):
        for var_name in shelfs:
            shelf_data = shelfs[var_name]
            name = "s{}_{}".format(i, var_name)
            offset = shelf_data['addr_offset']
            addr_offset = float(offset) if "BOOL" in shelf_data['type'] else int(offset)
            addr = "D{}".format((shelf_base_addr + addr_offset + i * shelf_reg_size))
            write_rec_glob_var_table(global_var_table, name, addr, shelf_data['type'], shelf_data['init_value'])

    # parse sensors, sensor_data and write into global_var_table
    addr_offset = 1
    for snsr_name in sensors['shelf_sensors']:
        for i in range(shelf_no):
            for j, var_name in enumerate(sensor_data):
                data = sensor_data[var_name]
                name = "snsr_s{}_{}_{}".format(i, snsr_name, var_name)
                addr = "D{}".format(sensor_base_addr + addr_offset)
                write_rec_glob_var_table(global_var_table, name, addr, data['type'], data['init_value'])
                addr_offset += 1

    for snsr_name in sensors['other_sensors']:
        for i, var_name in enumerate(sensor_data):
            data = sensor_data[var_name]
            name = "snsr_{}_{}".format(snsr_name, var_name)
            addr = "D{}".format(sensor_base_addr + addr_offset)
            write_rec_glob_var_table(global_var_table, name, addr, data['type'], data['init_value'])
            addr_offset += 1

    # parse shelfs and write into hmi_tag_table

    # parse sensors, sensor_data and write into hmi_tag_table

    # write global_var_table into global_variable_table.csv
    write_glob_var_table_to_csv(global_var_table_name, global_var_table)

    # write hmi_tag_table into hmi_tag_table.csv

    #####################

    
    """
    # extract data from "Constants" table
    const_vars = constant_table['variable_name'].tolist()
    const_addrs = constant_table['addr'].tolist()
    const_types = constant_table['type'].tolist()
    const_values = constant_table['init_value'].tolist()

    assert ("shelf_no" in const_vars) and ("shelf_reg_size" in const_vars) == True
    shelf_no = int(const_values[const_vars.index("shelf_no")])
    shelf_reg_size = int(const_values[const_vars.index("shelf_reg_size")])

    k_var = []
    k_addr = []
    k_type = []
    k_value = []

    for i in range(len(const_vars)):
        k_var.append(const_vars[i])
        k_addr.append("D{}".format(const_addrs[i]))
        k_type.append(const_types[i])
        k_value.append(const_values[i])

    # extract data from "Shelf" sheet
    base_addr = int(shelf_table['base_addr'].tolist()[0])
    var_name_list = shelf_table['variable_name'].tolist()
    addr_offset_list = shelf_table['addr_offset'].tolist()
    type_list = shelf_table['type'].tolist()
    init_value_list = shelf_table['init_value'].tolist()

    s_var = []
    s_addr = []
    s_type = []
    s_default = []

    for i in range(shelf_no):
        for var_name in var_name_list:
            s_var.append("s{}_{}".format(i, var_name))
        for j, offset in enumerate(addr_offset_list):
            offset = float(offset) if "BOOL" in type_list[j] else int(offset)
            s_addr.append("D{}".format(base_addr + offset + i * shelf_reg_size))
        for var_type in type_list:
            s_type.append(var_type)
        for var_default in init_value_list:
            s_default.append(var_default)

    # extract data from "Sensor Data" sheet
    snsr_data_list = sensor_data_table['variable_name'].tolist()
    snsr_data_type_list = sensor_data_table['type'].tolist()
    snsr_data_default_value_list = sensor_data_table['init_value'].tolist()

    # extract data from "Shelf Sensor" sheet
    snsr_data_base_addr = int(sensor_list_table['base_addr'].tolist()[0])
    shelf_sensor_list = [x for x in sensor_list_table['shelf_sensor'].tolist() if not pd.isna(x)]
    general_sensor_list = [x for x in sensor_list_table['general_sensor'].tolist() if not pd.isna(x)]

    snsr_var = ["snsr_base_addr"]
    snsr_addr = ["D{}".format(snsr_data_base_addr)]
    snsr_type = ["WORD"]
    snsr_default = [0]

    offset_addr = 1

    for snsr in shelf_sensor_list:
        for i in range(shelf_no):
            for j, data in enumerate(snsr_data_list):
                snsr_var.append("snsr_s{}_{}_{}".format(i, snsr, data))
                snsr_addr.append("D{}".format(snsr_data_base_addr + offset_addr))
                snsr_type.append(snsr_data_type_list[j])
                snsr_default.append(snsr_data_default_value_list[j])
                offset_addr += 1

    for snsr in general_sensor_list:
        for i, data in enumerate(snsr_data_list):
            snsr_var.append("snsr_{}_{}".format(snsr, data))
            snsr_addr.append("D{}".format(snsr_data_base_addr + offset_addr))
            snsr_type.append(snsr_data_type_list[i])
            snsr_default.append(snsr_data_default_value_list[i])
            offset_addr += 1


    # write parsed data to csv file
    header = ["Class", "Identifiers", "Address", "Type", "Initial Value", "Comment"]

    with open(os.path.join(curr_dir, global_var_table_name), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        # write constant variable
        for i in range(len(k_var)):
            writer.writerow(['VAR', k_var[i], k_addr[i], k_type[i], k_value[i]])

        # write variable / parameter
        for i in range(len(s_var)):
            writer.writerow(['VAR', s_var[i], s_addr[i], s_type[i], s_default[i]])

        # write sensors variable
        for i in range(len(snsr_var)):
            writer.writerow(['VAR', snsr_var[i], snsr_addr[i], snsr_type[i], snsr_default[i]])

    print("Global variable generation completed.")

    """


def read_const_table(c_table: dict) -> dict:
    c_dict = {}
    c_vars = c_table['variable_name'].tolist()
    c_addrs = c_table['addr'].tolist()
    c_types = c_table['type'].tolist()
    c_init_values = c_table['init_value'].tolist()
    
    for c_var, c_addr, c_type, c_init_value in zip(c_vars, c_addrs, c_types, c_init_values):
        c_dict[c_var] = {'addr': c_addr, 'type': c_type, 'init_value': c_init_value}

    return c_dict


def read_shelf_table(s_table: dict) -> dict:
    s_dict = {}
    s_base_addr = int(s_table['base_addr'].tolist()[0])
    s_names = s_table['variable_name'].tolist()
    s_addr_offsets = s_table['addr_offset'].tolist()
    s_types = s_table['type'].tolist()
    s_init_values = s_table['init_value'].tolist()

    # inject name, addr_offset, type, init_value
    for s_name, s_addr_offset, s_type, s_init_value \
        in zip (s_names, s_addr_offsets, s_types, s_init_values):

        s_dict[s_name] = {
            'addr_offset': s_addr_offset,
            'type': s_type,
            'init_value': s_init_value
            }

    return s_base_addr, s_dict


def read_sensor_data_table(sd_table: dict) -> dict:
    sd_dict = {}
    sd_names = sd_table['variable_name'].tolist()
    sd_types = sd_table['type'].tolist()
    sd_init_values = sd_table['init_value'].tolist()

    # inject name, type, init_value into dict
    for sd_name, sd_type, sd_init_value in zip(sd_names, sd_types, sd_init_values):
        sd_dict[sd_name] = {'type': sd_type, 'init_value': sd_init_value}

    return sd_dict


def read_sensor_list_table(sl_table: dict) -> dict:
    sl_dict = {}
    sl_base_addr = int(sl_table['base_addr'].tolist()[0])
    shelf_sensors = [x for x in sl_table['shelf_sensor'].tolist() if not pd.isna(x)]
    other_sensors = [x for x in sl_table['general_sensor'].tolist() if not pd.isna(x)]

    sl_dict['shelf_sensors'] = shelf_sensors
    sl_dict['other_sensors'] = other_sensors

    return sl_base_addr, sl_dict


def write_rec_glob_var_table(
    global_var_table: dict, var_name: str, var_addr: str, \
    var_type: str, var_init_value: str
) -> None:

    global_var_table[var_name] = {
        "addr": var_addr,
        "type": var_type,
        "init_value": var_init_value
    }

    return


def write_glob_var_table_to_csv(filename, global_var_table):
    header = ["Class", "Identifiers", "Address", "Type", "Initial Value", "Comment"]
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(curr_dir, filename), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        for var_name in global_var_table:
            var_data = global_var_table[var_name]
            writer.writerow(['VAR', var_name, var_data['addr'], var_data['type'], var_data['init_value']])

    print("completed: global_variable_table.csv")

if __name__ == "__main__":
    main()