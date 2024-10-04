# -*- coding:utf-8 -*-

class Circle:
    def __init__(self):
        self.r = 1.0

    def set_r(self, r):
        self.r = r

    def print_menseki(self):
        r = self.r
        print "menseki=", r*r*3.14

