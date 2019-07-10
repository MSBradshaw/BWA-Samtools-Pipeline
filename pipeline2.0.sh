##!/bin/bash
# $1 is the reference sequence
# $2 and $3 are the reads
# $4 is the output dirrectory
##estimate the copy number for using the 3 single repeat genes
./bwa_samtools_script.sh mcm7.fasta $2 $3 mcm7.pileup
./bwa_samtools_script.sh rpb1.fasta $2 $3 rpb1.pileup
./bwa_samtools_script.sh rpb2.fasta $2 $3 rpb2.pileup
python copy_number.py mcm7.pileup rpb1.pileup rpb2.pileup 397 376 374
./bwa_sam2.sh $1 $2 $3 pileup.pileup
python parse_variance.py pileup.pileup average_coverage.txt
mkdir ../final_dirs/$4
mv pileup.pileup ../final_dirs/$4
mv sorted.bam* ../final_dirs/$4
mv variance.txt ../final_dirs/$4
