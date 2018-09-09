#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:55:59 2018

@author: sagar

"""
students = []
class Student:

    school_name="Paragon Public School"
    def __init__(self,name,student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student Name : "+ self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

