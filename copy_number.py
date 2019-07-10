import sys
files = []
buffers = []
if len(sys.argv) < 4:
    print "Too few arguments"
    print "command should be copy_number.py input1.pileup input2.pileup input3.pileup buffer1 (optional) buffer2 (optional) buffer3 (optional)"
    print "default buffer is 370"
    quit()
elif len(sys.argv) > 7:
    print "Too many arugments"
    print "command should be copy_number.py input1.pileup input2.pileup input3.pileup buffer1 (optional) buffer2 (optional) buffer3 (optional)"
    print "default buffer is 370"
    quit()
elif len(sys.argv) == 4:
    files = sys.argv[1:4]
    buffers.append(370)
    buffers.append(370)
    buffers.append(370)
elif len(sys.argv) == 7:
    files = sys.argv[1:4]
    buffers = sys.argv[4:]
else:
    print "command should be copy_number.py input1.pileup input2.pileup input3.pileup buffer1 (optional) buffer2 (optional) buffer3 (optional)"
    print "you may either include 3 buffers or no buffers"
    print "default buffer is 370"
    quit()

print str(buffers)
print str(files)
def get_copy_number_average(file,number):
    print number
    print "^^ is the number"
    number = int(number)
    infile = open(file,'r')
    coverage_numbers = []
    line_number = 0;
    for line in infile:
        coverage_numbers.append(line.rstrip().split()[3])
        line_number = line_number + 1
    stop_number = line_number - number
    bp_number = 0
    coverage_sum = 0
    for i in range(number,stop_number):
        coverage_sum = coverage_sum + int(coverage_numbers[i])
        bp_number = bp_number + 1
    return coverage_sum / bp_number

coverage_numbers = []
coverage_numbers.append(get_copy_number_average(files[0],buffers[0]))
coverage_numbers.append(get_copy_number_average(files[1],buffers[1]))
coverage_numbers.append(get_copy_number_average(files[2],buffers[2]))

cover_file = open('cover_numbers.txt','w')
cover_file.write(str(coverage_numbers[0]))
cover_file.write('\n')
cover_file.write(str(coverage_numbers[1]))
cover_file.write('\n')
cover_file.write(str(coverage_numbers[2]))
cover_file.write('\n')
cover_file.close()
outfile = open('average_coverage.txt','w')
outfile.write(str((coverage_numbers[0] + coverage_numbers[1] + coverage_numbers[2]) / 3));
outfile.close()
print 'done with pyscript'
