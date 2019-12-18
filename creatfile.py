#! /usr/bin/env python3
'''

 This program is related to the writing the boiler plate of program
 that I use in my daily purposes

 '''
import os
'''
Defining the boiler plates


'''
boiler_code = {
'python':'''#!usr/bin/env python3

\'''
            

This program is related to the writing the boiler plate of program
that I use in my daily purposes

\'''
def function_name():

if __name__ == '__main__':

           ''',
'org_note':'''#+TITLE: Note
#+AUTHOR:Surendra Tamang.
'''


}
def build(file_name, file_extension,file_path):
    if file_path == '':
        pass
    else:
#        path = file_path.replace('\\','\\\'')
        os.chdir(file_path)
    if file_extension == 'python':
        with open(file_name+'.py','w+') as f:
            f.write(boiler_code['python'])
            f.close()
    
    if file_extension == 'org':
        with open(file_name+'.org','w+') as f:
            f.write(boiler_code['org_note'])
            f.close
    return "Done!!" 

if __name__ == '__main__':
    file_name = input('Enter the file_name you want to create ')
    file_extension = input('Select file extension python|html| ')
    file_path = input("Enter place to put the file.")
    build(file_name, file_extension, file_path)

