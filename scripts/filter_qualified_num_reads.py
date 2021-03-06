#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:chenxiao


import sys,os
import pandas as pd
import Bio
import argparse
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio.SeqIO.FastaIO import SimpleFastaParser
from pyfaidx import Fasta
from pyfaidx import Faidx

def reads_filter_num(file,reads_file,n,outdir):
  reads_file = reads_file
  num=n
  reads_sorted=list(reads_file.keys())
  name_list=set(reads_sorted[:num])
  #output_file=os.path.join(outdir,'head_{0}_reads.fasta'.format(num))
  output_file=os.path.join(outdir,'head_reads.fasta')
  with open(file) as in_handle:
    with open(output_file, "w") as out_handle:
      for title,seq in SimpleFastaParser(in_handle):
        title1=title.split(" ")[0]
        if title1 in name_list:
          out_handle.write(">%s\n%s\n" % (title,seq))    
  
def main():
  parser=argparse.ArgumentParser()
  parser.add_argument('-f1','--reads_file',help='reads file in FASTA format',dest='file',type=str,required=True)
  parser.add_argument('-o','--outdir',help='outdir',dest='outdir',type=str,required=True)
  parser.add_argument('-g','--genome_size',help='Genome size(bp)',dest='genome_size',type=int,required=True)
  parser.add_argument('-r','--reads_number',help='select the number of reads(default 1000)',dest='reads_number',default=1000,type=int,required=False)

  args=parser.parse_args()
  file=os.path.abspath(args.file)
  outdir=os.path.abspath(args.outdir)
  genome_size=args.genome_size
  reads_number=args.reads_number
  
  #read in and index 
  reads = Fasta(file)
  fasta_str = Faidx(file)

  #build length dictionary
  dict_length={}
  for key in fasta_str.index.keys():
    dict_length[key]=fasta_str.index[key].rlen

  #sort(rn)
  dict_length_sorted=sorted(dict_length.items(),key=lambda item:item[1],reverse=True)
  #list to dic
  dic_dict_length_sorted={k:v for k,v in dict_length_sorted}
  #if reads_number:
  reads_filter_num(file,dic_dict_length_sorted,reads_number,outdir)

if __name__ == '__main__':
  main()
