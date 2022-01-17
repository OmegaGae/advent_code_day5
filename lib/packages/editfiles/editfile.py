#!/usr/bin/env python3

# from types import new_class
import os


class Editfile:
    
    def __init__(self,filename: str='gods.txt'):
        """
        This class allows you to read and write file with .txt or .yaml extension
        by default this program will read gods.txt file
        filename:  name of your file with his extension example: file.txt or file.yaml
        """
    
        self.filename = filename
        print(self.filename)
        self.data_dir = os.path.join(os.path.dirname(__file__),'files')
        self.data_path = os.path.join(self.data_dir,filename)
    
    def read(self):
        """
        You can read a any file by adding is filename. 
        By default this methode will open gods.txt file mentionned in the init.
        """
        
        if self.filename.split('.')[1] == 'txt':
            with open(self.data_path, "r") as txt_file:
                self.textfile_r = txt_file.readlines()
            return self.textfile_r
        
    def write(self, data_to_be_write: list)->None:
        """
        You can write on a TXT file by giving the data you want to write.
        By default this methode will write on gods.txt file mentionned in the init.
        """
    
        if self.filename.split('.')[1] == 'txt':
            with open(self.data_path, "w") as txt_writable:
                txt_writable.write(data_to_be_write)
            

