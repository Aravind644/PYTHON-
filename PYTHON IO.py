# python15
python IO


1.Write a program to read text from .txt file using InputStream

file1 = open("myfile.txt","r+") 
  
print "Output of Read function is "
print file1.read()
print
file1.close()


2.Write a program to write text to .txt file using OutputStream

fileptr = open("file2.txt", "w")    
fileptr.write('''''Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language''')  
fileptr.close()  



3.Read text from a .txt file using BufferedInputStream

file = open("any_file_name.txt", "r")
all_the_data = []
for line in file:
    one_piece_of_data = line.split("#")[0]
    all_the_data.append(one_piece_of_data)



4.Write text to a .txt file using BufferedOutputStream

WriteTxtFile = open("write-demo.txt", "w")
WriteTxtFile.write ("This is new text for the \n demo of writing in text file.")
WriteTxtFile.close()
 

    
    
5.Write a program to read text from .txt file using FileReader

def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')



6. Write a program to write text to .txt file using FileWriter

WriteTxtFile = open("write-demo.txt", "w")
WriteTxtFile.write ("This is new text for the \n demo of writing in text file.")
WriteTxtFile.close()
 



7.Read text from a .txt file using BufferedReader

file_in = BufferedReader(FileReader("c:\\dat\\buf_File.txt")) Read in all tftse lines at once with throe method calls to readLine ().

 line1, line2, line3 = file_in.readLine(), file_in.readLine(), file_in.readLine()

Print all three lines rt once.

print line1; print line2; print line3 Line 1 Line 2




8.Write text to a .txt file using BufferedWriter

def get_or_init_buffered_writer(self, file):
        try:
            if self.buffered_writer is None or self.buffered_writer.closed:
                self.buffered_writer = BufferedWriter(FileIO(self.settings.get_data_folder_path() + file, 'a'))
            return self.buffered_writer
        except IOError as e:
            log.error("Failed to initialize buffered writer! Error: %s", e)
            raise RuntimeError("Failed to initialize buffered writer!", e) 
            
            

9.Write a program to read data from properties file.

from jproperties import Properties
  
configs = Properties()
with open('example.properties', 'rb') as read_prop:
    configs.load(read_prop)
      
prop_view = configs.items()
print(type(prop_view))
   
for item in prop_view:
    print(item)
    
    

10. Write a program to read data from excel

import xlrd
location = "C:\\Users\\   \\Documents\\demo.xlsx"
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0, 0))


11.Write a program to write data to excel

 import xlwt
from xlwt import Workbook
  
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(1, 0, 'ISBT DEHRADUN')
sheet1.write(2, 0, 'SHASTRADHARA')
sheet1.write(3, 0, 'CLEMEN TOWN')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 1, 'ISBT DEHRADUN')
sheet1.write(0, 2, 'SHASTRADHARA')
sheet1.write(0, 3, 'CLEMEN TOWN')
sheet1.write(0, 4, 'RAJPUR ROAD')
sheet1.write(0, 5, 'CLOCK TOWER')
  
wb.save('xlwt example.xls')
