#!/usr/bin/env python
#coding=utf-8

class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.print_msg()

    def print_msg(self):
        print 'name:%s, age:%d' %(self.name, self.age)


class SchoolTeacher(SchoolMember):
    def __init__(self, name, age, sex, id):
        SchoolMember.__init__(self, name, age)
        self.sex = sex
        self.id = id
        
    def print_msg(self):
        print 'name:%s, age:%d, sex:%s, id:%d' %(self.name, self.age, self.sex, self.id)


class SchoolStudent(SchoolMember):
    def __init__(self, name, age, addr):
        SchoolMember.__init__(self, name, age)
        self.addr = addr

    def print_msg(self):
        print 'name:%s, age:%d, addr:%s' %(self.name, self.age, self.addr)


class SchoolCommon(SchoolStudent, SchoolTeacher):
    def __init__(self, name, age, addr, sex, id):
        SchoolStudent.__init__(self, name, age, addr)
        SchoolTeacher.__init__(self, name, age, sex, id)

    def print_msg(self):
        print 'name:%s, age:%d, sex:%s, addr:%s, id:%d' %(self.name, self.age, self.sex, self.addr, self.id)


def read_conf_file(file):
    with open(file) as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            
            line2 = line.strip()  # skip the blank line
            if len(line2) == 0: continue

            if line2.startswith('#') or line2.startswith(';'): continue
            if '=' not in line2:
                print 'group: %s' %(line2)
            else:
                print 'key(%s) = value(%s)' % (tuple(line2.split('=')))
                
            
if __name__ == "__main__":
    s1 = SchoolMember('cheng1', 29)
    s2 = SchoolTeacher('wang1', 39, 'boy', 2202)
    s2.print_msg()
    s1.print_msg()
    s3 = SchoolStudent('liu1', 19, 'sc ms xx')
    s3.print_msg()
