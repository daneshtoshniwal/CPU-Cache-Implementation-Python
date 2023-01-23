'''
This is a 4-way set associative cache of size 1024 kilobytes
Block size: 4 bytes.
'''
def myfunc(trace):
	print("--------",trace,"--------")
	#------------------------------------------
	#Below few lines of code extracts the lines 
	#of the trace file and also convert the 
	#hexadecimal address to binary format.
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
		d[l[i][13:30]]=[]

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
		if(len(d[l[i][13:30]])==0):
			d[l[i][13:30]].append(l[i][0:13])
			misses=misses+1
			continue
		
		# Otherwise, search in the cache line with index 
		# corresponding to the address.
		for j in range(0,len(d[l[i][13:30]])):
			if(d[l[i][13:30]][j]==l[i][0:13]):
				found=1
				hits=hits+1
				hitvalue=l[i][0:13]
				# Implementing LRU in the list. Least recently used is at 
				# 0th index, and the most recently used is at the last.
				# We shift the cache hit address and insert it at last
				# to indicate that it was most recently used.
				d[l[i][13:30]].pop(j)
				d[l[i][13:30]].append(hitvalue)
				break
		
		# If its cache miss, we will pop the LRU address from the cache line,
		# and insert the newly used address in the cache (extracted from memory)
		if found==0:
			misses=misses+1
			if(len(d[l[i][13:30]])==4):
				d[l[i][13:30]].pop(0)
				d[l[i][13:30]].append(l[i][0:13])
			else:
				d[l[i][13:30]].append(l[i][0:13])

	print("hits:",hits)
	print("misses:",misses)
	print("hit percent:",hits*100/(misses+hits))
	print("miss percent:",misses*100/(misses+hits))
	print("---------------------------")

myfunc("gcc.trace")
myfunc("gzip.trace")
myfunc("mcf.trace")
myfunc("swim.trace")
myfunc("twolf.trace")