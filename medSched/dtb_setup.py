# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 08:26:10 2017

@author: ladislav.zednik
"""

import sqlite3

dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#c.execute('DROP TABLE outZipDT')
c.execute('DROP TABLE schedule')


c.execute('''
    CREATE TABLE schedule(  cm_id INTEGER,
                            mbr_id INTEGER,
                            svc_date REAL,
                            svc_time INTEGER,
                            svc_len INTEGER
                      )
''')

#c.execute('''
#    CREATE TABLE mbrs(mbr_id INTEGER,
#                      product TEXT,
#                      addr1 TEXT,
#                      addr2 TEXT,
#                      city TEXT,
#                      state TEXT,
#                      zip TEXT,
#                      full_addr TEXT
#                      )
#''')

#c.execute('''
#    CREATE TABLE combs(comb_key INTEGER,
#                      zip TEXT,
#                      mbr1 INTEGER,
#                      mbr2 INTEGER
#                      )
#''')

#c.execute('''
#    CREATE TABLE inZipDT(   comb_key INTEGER,
#                            zip TEXT,
#                            dist TEXT,
#                            time TEXT
#                      )
#''')

#c.execute('''
#    CREATE TABLE outZipDT(  out_key INTEGER,
#                            zip1 TEXT,
#                            zip2 TEXT,
#                            dist TEXT,
#                            time TEXT
#                      )
#''')


conn.close()

print('done')
