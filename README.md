# CPU tempeture semester project  

This program takes a list of cpu core temps and calculates a linear piecewise interpolation for each step as well as a global least squares approximation.  

The output files contain a linear approximation between each tempeture reading on each line. The last line of the file is a global least squares approximation.  

## Assignment page:   
[Semester Project - CPU Temps](https://www.cs.odu.edu/~tkennedy/cs417/f19/Assts/project-cpu-temps/index.html#input-format)  
  
## To run with no-labels files (those included):  
python3 cpuTempProject.py "file name" false  

## To run with labels files:  
python3 cpuTempProject.py "file name" true

---  
Written in python3 with pydoc3 documentaion

