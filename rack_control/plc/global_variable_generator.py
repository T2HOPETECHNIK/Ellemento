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

    excel_data = pd.read_excel(os.path.join(curr_dir, input_name), sheet_name="Sheet1")

    shelf_no = int(excel_data['shelf_no'].tolist()[0])
    base_addr = int(excel_data['base_addr'].tolist()[0])
    shelf_reg_size = int(excel_data['shelf_reg_size'].tolist()[0])

    var_name_list = excel_data['variable_name'].tolist()
    is_float_list = excel_data['is_float'].tolist()
    addr_offset_list = excel_data['addr_offset'].tolist()
    type_list = excel_data['type'].tolist()
    init_value_list = excel_data['init_value'].tolist()

    c_var = []
    c_addr = []
    c_type = []
    c_default = []

    for i in range(shelf_no):
        for var_name in var_name_list:
            c_var.append("s{}{}".format(i, var_name))
        for j, offset in enumerate(addr_offset_list):
            if is_float_list[j] == 'B':
                offset = float(offset)
            else:
                offset = int(offset)
            c_addr.append(base_addr + offset + i * shelf_reg_size)
        for var_type in type_list:
            c_type.append(var_type)
        for var_default in init_value_list:
            c_default.append(var_default)

    # write parsed data to csv file
    header = ["Class", "Identifiers", "Address", "Type", "Initial Value", "Comment"]

    with open(os.path.join(curr_dir, output_name), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(header)
        for i in range(len(c_var)):
            writer.writerow(['VAR', c_var[i], 'D{}'.format(c_addr[i]), c_type[i], c_default[i]])