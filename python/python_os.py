#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
current_path = os.path.dirname(os.path.realpath(__file__))
example_path = os.path.dirname(current_path)
project_path=os.path.dirname(example_path)
print "current_path", current_path
print "example_path", example_path
print "project_path", project_path
print "/home/love/.config/xfce4/helps.rc's path:", os.path.dirname("/home/love/.config/xfce4/helps.rc")
print "/home/love/.config/xfce4/helps.rc's path's path:", os.path.dirname(os.path.dirname("/home/love/.config/xfce4/helps.rc"))
