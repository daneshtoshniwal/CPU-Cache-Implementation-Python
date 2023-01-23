# CPU-Cache-Implementation-Python
An efficient python code to calculate and display the hit rates, miss rates of a user-defined cache (input memory trace files)

How to run the code:
Run each code separately. The output will be displayed directly on the console. 

Trace Files:
The trace file will specify all the memory accesses/addresses that occur in a certain program. 
Each line in the trace file will specify a new memory reference and has the following fields:
 • Access Type: A single character indicating whether the access is a load ('l') or a store ('s').
You can ignore this field. For reporting hit/miss, it does not matter whether it is a Load/Store
 • Address: A 32-bit integer (in unsigned hexadecimal format) specifying the memory address 
that is being accessed. This is the only field you need.
 • Instructions since last memory access: Indicates the number of instructions of any type that 
executed between since the last memory access (i.e. the one on the previous line in the trace).
For example, if the 5th and 10th instructions in the program's execution are loads, and there are 
no memory operations between them, then the trace line for with the second load has "4" for 
this field. You can safely ignore this field.

Output from the code:
Hit rates or miss rates for all the 5 traces for the 4 different experiments.
