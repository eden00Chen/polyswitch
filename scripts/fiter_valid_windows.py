#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:chenxiao
import os,sys
import pandas as pd
import numpy as np

def main():
  df_file=pd.read_table('BLAST_sort01.txt',sep='\t',header=None,names=['Query_id','Subject_id','%_identity','alignment_length ','mismatches','gap_openings','q.start','q.end','s.start','s.end','e-value','bit_score'])
  grouped_file=df_file.groupby('Query_id')
  for name,group in grouped_file:
    if(group.shape[0]>1):
      #line="{}\t{}|{}".format(name,group.iloc[0][1],group.iloc[0][11])
      #f0=open('/home/chenxiao/project/swtich_error_testtest/Script/test.txt','w')
      #f0.write(line)
      line_chrome1=group.iloc[0][1]
      line_bit_score1=group.iloc[0][11]
      line_chrome2=group.iloc[1][1]
      line_bit_score2=group.iloc[1][11]

      name0=name.split("_")[0]
      name1=name.split("_")[1]
      name2=name.split("_")[2]
      if (line_bit_score1==line_bit_score2 and line_chrome1==line_chrome2 and group.shape[0]>2):
        q=1
        while(line_bit_score1==line_bit_score2 and line_chrome1==line_chrome2 and q<group.shape[0]):
          line_bit_score2=group.iloc[q][11]
          line_chrome2=group.iloc[q][1]
          q=q+1
      ratio=line_bit_score1/line_bit_score2
      if(ratio >=1.5):
        line="{}\t{}\t{}\t{}\t{}|{}\t{}|{}\n".format(name0,name1,name2,line_chrome1,line_chrome1,line_bit_score1,line_chrome2,line_bit_score2)
        f0=open('valid_window.txt','a')
        f0.write(line)	
if __name__ == '__main__':
  main()
