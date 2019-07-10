import sys
filename = sys.argv[1] #pileup file
coverage_filename = sys.argv[2]

print(filename)
infile = open(filename,'r')

coverage_file = open(coverage_filename,'r')
single_cov = float(coverage_file.readline().strip())

tot_cov = 0
n=0
for line in infile:
    cols = line.split()
    pos = int(cols[1])
    depth = float(cols[3])
    if (pos > 600) & (pos < 1115):
        tot_cov += depth
        n += 1

avg_ITS_cov = tot_cov/n

copynum = avg_ITS_cov/single_cov

threshold = copynum/(tot_cov/n)
variance = [] #to save all ITS variance; will only print significant variance within ITS

outfile = open("variance.txt",'w')

outfile.writelines("estimated copy number: " + str(copynum)+'\n')
outfile.writelines("average coverage: " + str(tot_cov/n)+'\n')
outfile.writelines("***threshold for variance: " + str(threshold)+'\n')

tot_cov = 0
n = 0
infile = open(filename,'r')
for line in infile:
    cols = line.split()
    pos = int(cols[1])
    depth = float(cols[3])

    mismatch_count =0
    for ch in cols[4]:
        if ch in "ACGTNacgtn":
            mismatch_count += 1
    if depth != 0:
        var = mismatch_count/depth
        variance.append(var)
        if (pos > 600) & (pos < 1115):
            tot_cov += depth
            n+= 1
            if (var >= 0.01):
                print(str(pos) + " (" + str(depth) + "): " + str(var))
                if (var >= threshold):
                    outfile.writelines("***" + str(pos) + " (" + str(mismatch_count) + "/" + str(depth) + "): " + str(var) + '\n')
		else: 
		    outfile.writelines(str(pos) + " (" + str(mismatch_count) + "/" + str(depth) + "): " + str(var) + '\n')
    else:
        variance.append(0)



#print n
#print tot_cov/n




