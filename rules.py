# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 05:25:19 2018

@author: Cynthia Khan
"""
"""
SAT > RAT -2 + 3.6
|Valve Command - 1| <= 0.02 && SAT - SAT Setpoint >= 3.6
|Valve Command - 1| <= 0.02
SAT - SAT Setpoint >= 3.6

Where the variables in these equations are defined by the “Measurement” 
field in the BAS point codex as,

"""
import csv

#SAT, RAT, VALVE COMMAND, SETPOINT
point = [[4,5,26,3],
         [34,33,32,38],
         [28,31,26,27],
         [10,8,6,9],
         [15,13,11,14],
         [20,18,16,19],
         [25,23,21,24],
         [43,26,40,42],
         [47,26,44,46],
         [51,26,48,50],
         [56,26,53,55]]

rule1 = []
rule2 = []
rule3 = []
rule4 = []
header = ["Date", "Time", "Rule", "Unit1", "Unit2",
          "Unit3", "Unit4", "Unit5", "Unit6", "Unit7", 
          "Unit8", "Unit9", "Unit10", "Unit1A"]

with open('rules.csv', 'w') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(header)
    
    with open('test_coe.csv', 'r') as incsv:
        reader = csv.reader(incsv)
        #skip header
        next(reader)
        #for each time step
        for line in reader:
            #for each unit
            for i in range(0,11):
                sat = float(line[point[i][0]])
                rat = float(line[point[i][1]])
                vc = float(line[point[i][2]])
                ss = float(line[point[i][3]])
            #Rule 1
                if (sat > (rat -2 + 3.6)):
                    rule1.append(1)
                else:
                    rule1.append(0)
            #Rule2
                if ((abs(vc -1) <= 0.02) & ((sat - ss) >=3.6)):
                   rule2.append(1)
                else:
                   rule2.append(0)
                   
            #Rule3
                if(abs(vc - 1) <= 0.02):
                   rule3.append(1)
                else:
                   rule3.append(0)
                   
            #Rule4
                if ((sat - ss) >=3.6):
                   rule4.append(1)
                else:
                   rule4.append(0)
            
            writer.writerow([line[0],line[1],1] + rule1)
            writer.writerow([line[0],line[1],2] + rule2)
            writer.writerow([line[0],line[1],3] + rule3)
            writer.writerow([line[0],line[1],4] + rule4)
            
            del rule1[:]
            del rule2[:]
            del rule3[:]
            del rule4[:]

incsv.close()
outcsv.close()

                   
                  
                   
                   