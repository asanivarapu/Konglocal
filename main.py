# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import yaml


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    with open("C:\\Users\\asanivarapu\\Documents\\WORK\\Kong\\KongOS3.1.0.0\\deck_1.19.1_windows_amd64\\kong.yaml", 'r') as f:
        valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
    print(valuesYaml['services'][863])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
