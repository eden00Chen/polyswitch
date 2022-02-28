#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:chenxiao
import sys
import pysam

#with pysam.FastxFile('/home/chenxiao/project/swtich_error_V4/Data/heads_sliding.fasta') as fh:
with pysam.FastxFile(sys.argv[1]) as fh:
  for r in fh:
    name_1=r.name.split(':')[0].split('_')[0]
    name_2=r.name.split(':')[1].split('-')[0]
    name_3=r.name.split(':')[1].split('-')[1]
    new_name="{0}_{1}_{2}".format(name_1,name_2,name_3)
    print(">"+new_name)
    print(r.sequence)
 
#python rename_fasta.py test.fa > rename.fa
