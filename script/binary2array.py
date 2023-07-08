# Convert a binary file to C style array.

import os
from tkinter import filedialog

def selectFile():
    '''select file to convert to array
    returns filename as string
    '''
    filename = filedialog.askopenfilename()
    return filename

def binary_file_to_c_array(bianry_file_path):
    '''convert binary file to C style array
    returns array as string
    '''
    with open(bianry_file_path, 'rb') as f:
        data = f.read()
        return data

def write_array_to_file(array, c_filename='temp.h'):
    '''write array to file
    returns C head file path
    '''
    with open(c_filename, 'w') as f:
        array_size = len(array)
        f.write('uint8_t array' + '[' + str(array_size) + '] = {')
        for i in range(array_size - 1):
            # write 16 elements in one line, then insert an new line
            if i % 16 == 0:
                f.write('\n')
            # format x with 4 digits
            f.write(format_byte(array[i]) + ', ')
        # write the last element without comma
        f.write(format_byte(array[-1]))
        # write the end of the array
        f.write('\n};')
    return c_filename

def format_byte(byte):
    '''format x with 4 digits'''
    return '0x{:02X}'.format(byte)

def main():
    # 1.Choose a binary file in the system
    binary_file_path = selectFile()
    # 2.Convert the binary file to array
    array = binary_file_to_c_array(binary_file_path)
    # 3.New an temp file to store the array
    c_filename = write_array_to_file(array)
    # 4.Open c_filename to show the array
    os.system('start ' + c_filename)

if __name__ == '__main__':
    main()




    