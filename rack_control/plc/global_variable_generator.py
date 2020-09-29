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

if __name__ == "__main__":

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    input_name = "global_variable_template.xlsx"
    output_name = "global_variable_table.csv"

    shelf_data = pd.read_excel(os.path.join(curr_dir, input_name), sheet_name="Shelf")
    constant_data = pd.read_excel(os.path.join(curr_dir, input_name), sheet_name="Constants")

    # extract data from "Constants" sheet
    const_list = constant_data['variable_name'].tolist()
    const_addr_list = constant_data['addr'].tolist()
    const_type_list = constant_data['type'].tolist()
    const_value_list = constant_data['init_value'].tolist()

    assert ("shelf_no" in const_list) and ("shelf_reg_size" in const_list) == True
    shelf_no = const_value_list[const_list.index("shelf_no")]
    shelf_reg_size = const_value_list[const_list.index("shelf_reg_size")]

    k_var = []
    k_addr = []
    k_type = []
    k_value = []

    for i in range(len(const_list)):
        k_var.append(const_list[i])
        k_addr.append("D{}".format(const_addr_list[i]))
        k_type.append(const_type_list[i])
        k_value.append(const_value_list[i])

    # extract data from "Shelf" sheet
    base_addr = int(shelf_data['base_addr'].tolist()[0])
    var_name_list = shelf_data['variable_name'].tolist()
    addr_offset_list = shelf_data['addr_offset'].tolist()
    type_list = shelf_data['type'].tolist()
    init_value_list = shelf_data['init_value'].tolist()

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


    # write parsed data to csv file
    header = ["Class", "Identifiers", "Address", "Type", "Initial Value", "Comment"]

    with open(os.path.join(curr_dir, output_name), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(header)

        # write constant variable
        for i in range(len(k_var)):
            writer.writerow(['VAR', k_var[i], k_addr[i], k_type[i], k_value[i]])

        # write variable / parameter
        for i in range(len(s_var)):
            writer.writerow(['VAR', s_var[i], s_addr[i], s_type[i], s_default[i]])

    print("Global variable generation completed.")