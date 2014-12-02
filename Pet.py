#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: Pet
#   date: 2014-12-02
#   author: jdenisco
#   email: james.denisco@gmail.com
#
# Copyright © 2014 jdenisco <james.denisco@gmail.com>
#

"""
Description:
"""

import csv
import psycopg2


d = {}
inputfile = open('pets_to_add.csv', 'rt')
reader = csv.reader(inputfile)
header = reader.next()
header = [ str(h).lower() for h in header ]
try:
    conn = psycopg2.connect("dbname='pets' user='jdenisco' host='localhost'")
except (Exception) as e:
    print('Was not able to connect to database')

cursor = conn.cursor()
# c = cursor.execute('''SELECT * FROM person''')
#  print c

for row in reader:
    for i, x in enumerate(row):
        if len(x)< 1:
            x = row[i] = 'null'
    y = ','.join(str(x).lower() for x in row)
    z = y.split() 
    d=dict(zip(header, z))
    print d
#    write to database 
