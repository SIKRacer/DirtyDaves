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

    def Row_and_Column(self, Row):
        row_now_Get_Line = self.open_File_Return_Line(Row)
        correct_Value = row_now_Get_Line.split(',')
        return correct_Value

    def get_item_return_quantity(self, item):
        # row_now_Get_Line = self.open_File_Return_Line(Row)
        # correct_Value = row_now_Get_Line.split(',')
        with open("Spring.txt") as e:
            for line in e:

                if line.__contains__(item):
                    inventory_after = line.split(",")
                    postion = inventory_after.index(item)
                    # postion = inventory_after.__getattribute__(item)
                    return inventory_after[postion + 1]
        # return correct_Value[Column]

    def replace_Quantity_In_File(self, old_Amount, new_Amount, item):
        # with open("Spring.txt", 'w') as e:
        #     for line in e:
        #
        #         if line.__contains__(old_Amount):
        #             inventory_after = line.split(",")
        #             print(inventory_after)
        #             # postion = inventory_after.(item)
        #             # e.write(line.replace(old_Amount, new_Amount))
        filefound = open("Spring.txt", "r")
        book = filefound.readlines()
        for x in book:
            # print(x)
            if x.__contains__(item):
                for blah in x:
                    if blah.__contains__(item):
                        blah.replace(old_Amount, new_Amount)
        # print(book)

    def open_File_Return_Line(self, line_Row):
        try:
            file = open("Spring.txt", "r")
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
        file = open("Spring.txt", "r")
        count = file.readlines()
        return len(count)






run = document_Parse()
# run.search_File()
# run.grab_InventoryLine()
# run.again_Lets_Get_Inventory()
# run.give_back_based_on_Row_Column(1)
# run.Row_and_Column(1,1)