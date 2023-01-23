'''
This is a 4-way set associative cache of size 512 kilobytes
With variable block sizes of 1 Bytes, 4 Bytes, 8 Bytes, 16 Bytes
'''
import math
def myfunc(trace,byte):
	print("--------",trace,"--------")
	print("--------",byte,"bytes","------------")
	#------------------------------------------
	#Below few lines of code extracts the lines 
	#of the trace file and also convert the 
	#hexadecimal address to binary format.
	byte_offset = int(math.log2(byte))
	with open(trace) as f:
		content = f.readlines()
	l=[x.strip() for x in content]

	for i in range(0,len(l)):
		l[i]=l[i][4:12]
		int_value=int(l[i],base=16)
		l[i]=str(bin(int_value))[2:].zfill(32)
	#------------------------------------------
	
	d={} # CACHE

	#Initially, all the cache lines are empty
	for i in range(0,len(l)):
		d[l[i][15:32-byte_offset]]=[]

	#hit and miss counts is initiallized to 0 at start
	hits=0
	misses=0

	# For every search in dictionary- 3 cases- Hit/Miss/Replace
	# i is for address 
	# j is for index access
	for i in range(0,len(l)):
		# 32 bit address is l[i] 
		found=0
		# initiallizing found=0 at start. If it is a cache hit,
		# we will change found=1 and increment hit count by 1 

		# If the valid bit = 0 (not implemented separately),
		# i.e., the cache line is empty
		if(len(d[l[i][15:32-byte_offset]])==0):
			d[l[i][15:32-byte_offset]].append(l[i][0:15])
			misses=misses+1
			continue

		# Otherwise, search in the cache line with index 
		# corresponding to the address.
		for j in range(0,len(d[l[i][15:32-byte_offset]])):
			if(d[l[i][15:32-byte_offset]][j]==l[i][0:15]):
				found=1
				hits=hits+1
				hitvalue=l[i][0:15]
				# Implementing LRU in the list. Least recently used is at 
				# 0th index, and the most recently used is at the last.
				# We shift the cache hit address and insert it at last
				# to indicate that it was most recently used.
				d[l[i][15:32-byte_offset]].pop(j)
				d[l[i][15:32-byte_offset]].append(hitvalue)
				break

		# If its cache miss, we will pop the LRU address from the cache line,
		# and insert the newly used address in the cache (extracted from memory)	
		if found==0:
			misses=misses+1
			if(len(d[l[i][15:int(32-byte_offset)]])==4):
				d[l[i][15:int(32-byte_offset)]].pop(0)
				d[l[i][15:int(32-byte_offset)]].append(l[i][0:15])
			else:
				d[l[i][15:int(32-byte_offset)]].append(l[i][0:15])

	print("hits:",hits)
	print("misses:",misses)
	print("hit percent:",hits*100/(misses+hits))
	print("miss percent:",misses*100/(misses+hits))
	print("---------------------------")

myfunc("gcc.trace",1)
myfunc("gcc.trace",4)
myfunc("gcc.trace",8)
myfunc("gcc.trace",16)
print("\n\n")
myfunc("gzip.trace",1)
myfunc("gzip.trace",4)
myfunc("gzip.trace",8)
myfunc("gzip.trace",16)
print("\n\n")
myfunc("mcf.trace",1)
myfunc("mcf.trace",4)
myfunc("mcf.trace",8)
myfunc("mcf.trace",16)
print("\n\n")
myfunc("swim.trace",1)
myfunc("swim.trace",4)
myfunc("swim.trace",8)
myfunc("swim.trace",16)
print("\n\n")
myfunc("twolf.trace",1)
myfunc("twolf.trace",4)
myfunc("twolf.trace",8)
myfunc("twolf.trace",16)