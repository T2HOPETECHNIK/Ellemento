#
#
#  This app will filter out the log output from the Delta HMI history
#
#  Author: Vincent Lao
#  Date: 2021-02-03
#


import sys
import re

    
def processFile(inFile, outFile, colToExclude):

    print (inFile," being processed")
    # Using readlines()
    file1 = open(inFile, 'r')
    Lines = file1.readlines()
    file1.close()

    fo = open(outFile,"w+")
     
    # Strips the newline character
    for line in Lines:
        if line and line.strip():
            # remove null characters
            clean_line = line.replace('\00', '')
            encoded_string = clean_line.encode("ascii", "ignore")
            clean_line = encoded_string.decode()
            
            # split into an array
            r = re.compile(r'([^\t]*)\t*')
            colArray = r.findall(clean_line)[:-1]
            for i in range(0,len(colArray)-1):
                if i not in colToExclude:
                    #print (i,"=", colArray[i])
                    fo.write(colArray[i])
                    fo.write(",")

            fo.write('\n')
            
    fo.close()

    print (outFile, " created")


def processWaterTemp():
    # columns to include (probably those containing only zeroes
    # index starts at zero for first column
    excludeList = [3,5,7,9,11,13,15,17,18,19,20,21,23,25,27,29,31,33,35,33,35,37,38,39,40,41]
    processFile("H2OTemp.csv","H2OTemp_cleaned.csv",excludeList)

    
def main():
    processWaterTemp()


if __name__ == "__main__":
    print ("Processing...\n")
    main()
    
