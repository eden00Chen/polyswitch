# polyswitch
## Introduction
Polyswitch is a program to evaluate switch errors in haplotype-resolved genome assemblies, including heterozygous diploid and polyploid genomes, based on ONT ultra long data. A number of ONT ultra-long reads were selected and subsequently split into 5-kb non-overlapping windows. The 5-kb windows were BLASTn against the haplotype-resolved genome assembly using default parameters, and only windows that meet the following criteria were considered as validate windows and thus kept for further analysis: 1) For each window, we allow the bit score in the best match should be 1.5 times larger than the secondary match; 2) the best bit score should be larger than 1000. In addition, we also restricted that these reads with at least 5 valid windows were retained for assessment of switch errors. We next used the majority rule to determine the original location of the ONT reads. For instance, if more than 50% of validated windows in one ultra-long read mapped to Chr01A, we considered this read was originally from Chr01A rather than other alternative haplotypes. Any validate window against the original location was considered as a switch error.
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
polyswitch -1 reads.fasta -2 genome.fasta -o outdir -g genome_size [-r reads_number]
-1  :               reads file in FASTA format
-2  :               genome file in FASTA format
-o  :               outdir
-g  :               genome size(bp)
-r  :               select the number of reads,default:1000
```
* output  
result.txt ：
```
#version is: 1.1.0
#reads_file  : /public/home/DATA/test_ONT_reads.fasta.gz
#genome_file : /public/home/DATA/test_hifiasam.fasta
genome_size  : 1500311513
reads_number : 4000
                  
  ***** Results: *****
                  
		switch_num : 4936
		total_window_num : 65070
		total_reads_length : 973.76
		swtich_error(switch_num/total_window_num) : 7.59%
		swtich_error(switch_num/total_reads_length) : 5.07 /MB
Dependencies and versions:
  seqkit : 2.1.0
  blast  : 2.3.0+
```
