# polyswitch
## Introduction
This is a software to evaluate polyploid typing based on ont ultra long data.
## Installation
```
$ git clone https://github.com/eden00Chen/polyswitch.git
$ cd polyswitch
$ chmod +x bin/*
$ chmod +x scripts/*
$ export PATH=/your/path/to/polyswitch/scripts/:/your/path/to/polyswitch/bin/:$PATH
```
*example : export PATH=/home/software/polyswitch/scripts/:/home/software/polyswitch/bin:$PATH*  
*check : ployswitch -h*
## Dependencies
Following is a list of thirty-party programs that will be used in polyswitch pipeline.
* seqkit v2.1.0 +
* blast v2.11.0 +
* python v3.9.5 + (Python Toolkit : pandas、numpy、pysam、pyfaidx、Bio)
## Usage
* input
```
polyswitch -1 reads.fasta -2 genome.fasta -o outdir -g genome.fasta [-r reads_number]
-1  :               reads file in FASTA format
-2  :               genome file in FASTA format
-o  :               outdir
-g  :               genome size(bp)
-r  :               select the number of reads,default:1000
```
* output  
result.txt ：
```
reads_file : head100.rn.fasta
genome_file : LW.p_utg.fasta
genome_size : 1500311513
reads_number : 99
switch_num : 153
total_window_num : 203
total_reads_length : 33.09
swtich_error(switch_num/total_window_num) : 7.52%
swtich_error(switch_num/total_reads_length) : 4.62 /MB
```
