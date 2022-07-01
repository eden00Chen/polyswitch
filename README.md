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
```
polyswitch -1 reads.fasta -2 genome.fasta -o outdir -g genome_size [-r reads_number]
-1  :               reads file in FASTA format
-2  :               genome file in FASTA format
-o  :               outdir
-g  :               genome size(bp)
-r  :               select the number of reads,default:1000,recommend:4000
```

## Test
* test_data location:(data szie:1.3G)
```
wget ftp://43.138.130.14/pub/test_data.tar.gz
```
* command line:
```
polyswitch -1 reads_absolute_path -2 genome_absolute_path -o out_dir -g 146298676 -r 1000 -t 20
```
* result:
```
#version is: 1.1.0
#reads_file  : sample_reads.fasta
#genome_file : sample_genome.fasta
genome_size  : 146298676
reads_number : 1000
                  
  ***** Results: *****
                  
		switch_num : 562
		total_window_num : 5088
		total_reads_length : 85.93
		swtich_error(switch_num/total_window_num) : 11.05%
		swtich_error(switch_num/total_reads_length) : 6.54 /MB
Dependencies and versions:
  seqkit : 2.1.0
  blast  : 2.3.0+
```
## Polyswitch note
* Only supports ONT ultra-long reads.
* Support the input of data in GZ format, but the file naming rule must be filename.gz
* The input path and output path of the file must be absolute                  
  not: reads.fasta
  
  ex: /public/home/polyswitch_project/Data/reads.fasta
