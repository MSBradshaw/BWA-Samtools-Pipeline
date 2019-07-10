#!/bin/bash
module load bwa
#echo "Enter the Reference Sequence, a .fasta file: "
#read ref
#echo "Enter the first read file, a .fastq file: "
#read read1
#echo "Enter the second read file, a .fastq file: "
#read read2
#echo "Enter the output file, it will be a pilup file: "
#read final_out_file
echo "#bwa index " $1
bwa index $1
echo "#bwa aln $1 $2 read1.sai"
bwa aln $1 $2 > read1.sai
echo "#bwa aln $1 $3 read2.sai"
bwa aln $1 $3 > read2.sai
echo "#bwa sampe $1 read1.sai read2.sai $2 $3 > sam.sam"
bwa sampe $1 read1.sai read2.sai $2 $3 > sam.sam
echo "#module swap comiler_gnu/5.4"
module swap compiler_gnu/5.4
echo "#module load xz/5"
module load xz/5
echo "#module load samtools/1.5"
module load samtools/1.5
echo "#samtools view -m1 -b -o bam.bam sam.sam"
samtools view -m1 -b -o bam.bam sam.sam
echo  "#samtools sort -o sorted.bam bam.bam"
samtools sort -o sorted.bam bam.bam
echo "#samtools mpileup -o $4 -f $1 sorted.bam"
samtools mpileup -o $4 -f $1 sorted.bam
chmod 777 *
chmod 777 ../*
chmod 777 ../its_refs/*
rm *.sai
rm *am
rm *fasta.*

