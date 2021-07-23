import os
import sys

import sys
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # 找出python所需要的路徑
    print(os.path)
    # 專案路徑
    print(os.getcwd())
    # 執行主檔
    print(sys.executable)
    print(3 + 5 * 6 / 4 * 2 - 8)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
