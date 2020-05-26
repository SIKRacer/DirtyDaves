import sys
import Config
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove, rename, listdir, path
from os.path import exists
import re

class document_Parse():
    # config = Config()
    def search_File(self, item):
        file = open("InventoryFiles/Inventory.txt", "r")
        file_name = "InventoryFiles/Inventory.txt"
        i = 0
        # item = "123456"

        springs_From_File = file.readlines()

        with open( file_name) as e:
            for line in e:

                if line.__contains__(item):
                    inventory_after = line.split(",")
                    postion = inventory_after.index(item)
                    return inventory_after[postion + 1]
                    # print(pos for pos, char in enumerate(line) if char == item)

    def grab_InventoryLine(self):
        file = open("InventoryFiles/Inventory.txt", "r")
        file_name = "InventoryFiles/Inventory.txt"
        i = 0

        with open(file_name) as line:
            # print(line.readlines())
            length_of_File = len(line.readlines())
            print(length_of_File)
            # print("\n")
            for e in line:
                inventory = e.split(",")
                print(inventory)
                print("Hello")
            #
            #     print(line.readlines(i))
            #     print("\n")
            #     i+=1

            # print(line.readline())

    # def again_Lets_Get_Inventory(self):
    #     file = open("Inventory.txt", "r+")
    #     name = "file"
    #     i = 0
    #     folder = file.read().splitlines()
    #     print(folder)
    #     while i < len(folder):
    #         new_line = folder[i]
    #         print(self.split_line(new_line))
    #         print("When")
    #         i += 1
    #     file.close()
    #     return folder
    #
    # def split_line(self, split_this):
    #     # what_this_is = split_this.split(',')
    #     # print(what_this_is)
    #     # self.give_back_based_on_Row_Column("1", "1", what_this_is)
    #
    #     let_us_see = self.give_back_based_on_Row_Column(1)
    #     return let_us_see
    #
    # def give_back_based_on_Row_Column(self, Row):
    #     list_of_Items = self.again_Lets_Get_Inventory()
    #     list_of_Items.split(',')
    #     # list_of_Items[Row]
    #
    #     return list_of_Items[Row]

    def Row_and_Column(self, Row):
        row_now_Get_Line = self.open_File_Return_Line(Row)
        correct_Value = row_now_Get_Line.split(',')
        return correct_Value

    def get_item_return_quantity(self, item):
        # row_now_Get_Line = self.open_File_Return_Line(Row)
        # correct_Value = row_now_Get_Line.split(',')
        with open("InventoryFiles/Inventory.txt") as e:
            for line in e:

                if line.__contains__(item):
                    inventory_after = line.split(",")
                    postion = inventory_after.index(item)
                    # postion = inventory_after.__getattribute__(item)
                    return inventory_after[postion + 1]

    def replace_Quantity_In_File(self, old_Amount, new_Amount, item):
        # self.iterate_File_For_Backup()
        file_name = "InventoryFiles/Inventory.txt"
        new_File_Name = "InventoryFiles/Inventory.txt"
        fh, path = mkstemp()
        with fdopen(fh, 'w') as new_file:
            with open(file_name) as old_file:
                for line in old_file:
                    whatever = line.split(",")
                    if whatever.__contains__(item):
                        new_file.write(item + "," + new_Amount + "," + whatever[2])
                    else:
                        new_file.writelines(line)

                    # if line.__contains__(old_Amount):
                    #     print(line[1])
                    #     new_file.write(line.replace(old_Amount, old_Amount))
                    # if line[1] == old_Amount:
                    #     print(line[1])
                    #     new_file.write(line.replace(old_Amount, new_Amount))
        copymode(file_name, path)
        self.iterate_File_For_Backup()
        # self.rename_To_Backup_File(file_name, new_File_Name)
        move(path, file_name)

    def open_File_Return_Line(self, line_Row):
        try:
            file = open("InventoryFiles/Inventory.txt", "r")
            give_Line = file.read().splitlines()
            # print(give_Line[line_Row])
            #TODO: Catch error that is returned here when the file is empty
            return give_Line[line_Row]
        except:
            print("Your file might be Empty!")

    def find_Item_Quantity(self, items):
        return items[1]

    def find_Item_Name(self, name):
        return name[0]

    def find_Item_Description(self, destcription):
        return destcription[2]

    def how_many_lines(self):
        file = open("InventoryFiles/Inventory.txt", "r")
        count = file.readlines()
        file.close()
        return len(count)

    def rename_To_Backup_File(self, old_File, new_File):
        # print("Renaming File " + old_File)
        # files_in_Location = listdir("InventoryFiles/")
        # # print(files_in_Location)
        # for file in files_in_Location:
        # print(path.dirname("InventoryFiles"))
        # print(path.exists(old_File))
        if path.exists(old_File):
            print("File Renamed")
            print(old_File + " " + new_File)
            rename(old_File, new_File)
        else:
            return

    def remove_File(self, file_To_Remove):
        # print("removing File " + file_To_Remove)
        # files_in_Location = listdir("InventoryFiles/")
        # print(path.exists(file_To_Remove))
        # for file in files_in_Location:
        #     print(file)
        if path.exists(file_To_Remove):
            print("Removed File")
            remove(file_To_Remove)
        else:
            return
        # print(path.exists(file_To_Remove))

    def iterate_File_For_Backup(self):
        i = 10
        while i > 0:
            if i == 10:
                self.remove_File("InventoryFiles/Inventory10.txt")
            self.rename_To_Backup_File("InventoryFiles/Inventory" + str(i) + ".txt", "InventoryFiles/Inventory" + str(i + 1) + ".txt")
            i -= 1
        self.rename_To_Backup_File("InventoryFiles/Inventory.txt", "InventoryFiles/Inventory1.txt")
        # new_File_Name = "InventoryFiles/Inventory" + str(i) + ".txt"
        # return new_File_Name






run = document_Parse()
# run.search_File()
# run.grab_InventoryLine()
# run.again_Lets_Get_Inventory()
# run.give_back_based_on_Row_Column(1)
# run.Row_and_Column(1,1)