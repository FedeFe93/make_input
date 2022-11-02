#!/usr/bin/env python

#example extract coordinates Molecule + create input for every frame in the current directory
# by Federica Ferraro, federica.ferraro@fau.de

import re,sys,os


molatoms=int(sys.argv[1])+2   #enter number of solute atoms
directory=os.getcwd()

i=-1
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".xyz"):
       i +=1
       f=open(filename)
       list=range(2,molatoms)
       newfile= open("Molecule"+str(i).zfill(4)+".xyz","w")   #extract coordinates and write in a new file
       newfile.write(str(molatoms-2)+"\n")
       newfile.write("\n")
       input1= open("Molecule"+str(i).zfill(4)+".com","w")  #write gaussian input
       input1.write("%Chk=Molecule"+str(i)+".chk\n")
       input1.write("#p PBEPBE/cc-pVTZ empiricaldispersion=gd3 \n")
       input1.write("\n")
       input1.write("title\n")
       input1.write("\n")
       input1.write("0 1\n")
       with open(filename,"r") as file:
           for k, line in enumerate(file):
               if k in list:
                   newfile.write(line)
                   input1.write(line)
                   input1.write(" ")
                   continue
                   newfile.close()
                   input1.close()
