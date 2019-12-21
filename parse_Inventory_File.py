import sys
import Config

class document_Parse():
    # config = Config()
    def search_File(self, item):
        file = open("Spring.txt", "r")
        file_name = "Spring.txt"
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
        file = open("Spring.txt", "r")
        file_name = "Spring.txt"
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
    #     file = open("Spring.txt", "r+")
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

    def Row_and_Column(self, Row, Column):
        row_now_Get_Line = self.open_File_Return_Line(Row)
        correct_Value = row_now_Get_Line.split(',')
        return correct_Value[Column]

    def open_File_Return_Line(self, line_Row):
        file = open("Spring.txt", "r")
        give_Line = file.read().splitlines()
        # print(give_Line[line_Row])
        return give_Line[line_Row]





run = document_Parse()
# run.search_File()
# run.grab_InventoryLine()
# run.again_Lets_Get_Inventory()
# run.give_back_based_on_Row_Column(1)
run.Row_and_Column(1,1)