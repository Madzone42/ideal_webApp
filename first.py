#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:37:08 2018

@author: sagar
"""
students=[]


def get_student_tittlecase():
    student_tittlecase=[]
    for student in students:
        student_tittlecase.append(student["name"].title())
    return student_tittlecase


def print_student_tittlecase():
    student_tittlecase = get_student_tittlecase()
    print(student_tittlecase)


def add_student(name,student_id):
    student={ "name" : name,"student_id":student_id}
    students.append(student)




def save_file(student):
    f=open("student.txt" , "a")
    try:
        f.write(student+ "\n")
        f.close()
    except Exception:
        print("Cannot save file! Lo Ciento :( ")

def read_file():
   try:
        f=open("student.txt","r")
        for student in f.readline():
            add_student(student)
        f.close()
   except Exception:
        print ( "Maaf Garideu Malai: :( ")
        

answer_me=input("Ready to Input Student Name?  'Y'/'N' : ")




def read_student(f):
    for line in f:
        yield line
        
        
    
read_file()
print_student_tittlecase()

while answer_me == "Y":
    student_name = input("Enter the name : ")
    student_id = input("Enter the ID : ")
    add_student(student_name,student_id)
    print_student_tittlecase()
    answer_me = input("Do you have more entries?  'Y'/'N' : ")
if answer_me=="N":
    print("Database uploaded! ")

add_student(student_name,student_id)
save_file(student_name)




