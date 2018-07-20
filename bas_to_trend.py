# -*- coding: utf-8 -*-

import csv
"""
Spyder Editor

This is a temporary script file.
"""
point = ["35B.AHU01.CHV",
				"35B.AHU01.DAT",
				"35B.AHU01.SAF",
				"35B.AHU02.CHV",
				"35B.AHU02.DAT",
				"35B.AHU02.RAT",
				"35B.AHU02.SAF",
				"35B.AHU03.CHV",
				"35B.AHU03.DAT",
				"35B.AHU03.SAF",
				"35B.AHU04.CHV",
				"35B.AHU04.DAT",
				"35B.AHU04.RAT",
				"35B.AHU04.SAF",
				"35B.AHU05.DAT",
				"35B.AHU05.HTV",
				"35B.AHU05.RAT",
				"35B.AHU05.SAF",
				"35B.AHU06.CHV",
				"35B.AHU06.DAT",
				"35B.AHU06.RAT",
				"35B.AHU06.SAF",
				"35B.PENT.AHU1.RAT",
				"35B.PENT.AHU1.SAF",
				"35B.PENT.AHU1.SAT",
				"35B.PH.AHU1.CCV.A",
				"35B.PH.AHU1.CCV.B",
				"35B.PH.OAT",
				"35BROAD.FLR04.SSAC01.SAF",
				"35BROAD.FLR04.SSAC01.SAT",
				"35BROAD.FLR04.VAV.TMP.AVG",
				"COB.BSMT.CHW.SWT",
				"COB.BSMT.CT01.F1E",
				"COB.BSMT.CT01.F2E",
				"COB.BSMT.CW.SWT",
				"TBR1EN",
				"GC.BSMT.PLANT.TONNAGE"]

data = []

outFile = open('trend_data.csv', 'w')

with open('bas_data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter= '\t')
    for row in csvReader:
        for index in range(2, len(row)) :
            outFile.write((row[0] 
                + " " 
                + row[1] 
                + "," 
                + point[index - 2] 
                + "," + row[index]))
            
outFile.close()
    
    
    
