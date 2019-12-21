import sys
import time


class create_Backup_Files():

    # def __init__(self):
    #     print("Hello World")

    def save_File(self, Amp):

        print("This is going to Save the " + Amp)
        backupFile = open("BackUp" + str(time.time()) + ".txt", 'w')
        backupFile.write(Amp)
        