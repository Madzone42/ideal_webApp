#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:37:54 2018

@author: sagar
"""
import student

class Highschool(Student):
    school_name="Paragon High School"

    def get_school_name(self):
        return "This is a high school"

    def get_name_capitalize(self):
        original_value=super().get_name_capitalize()
        return original_value + "-HS"
