# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:25:11 2021

@author: Anindita
"""



test_str =input("Enter the string: ")
block=[]
sub_block=[]
print("The original string is : " + str(test_str))
  
res = ''.join(format(ord(i), '08b') for i in test_str)
  
print("The string after binary conversion : " + str(res))

block = [(res[i:i+8]) for i in range(0, len(res), 8)]
sub_block=[(res[i:i+4]) for i in range(0, len(res), 4)]
print("Blocks are: ",*block)
print("Sub Blocks are: ",*sub_block)

block0=[]
block1=[]
block2=[]
block3=[]

block1_0=block[0]
block1_1=block[1]
block1_2=block[2]
block1_3=block[3]

print("First Concatenation: ",sub_block[0]+" "+sub_block[1]+block1_0[0]+"|"+sub_block[2]+" "+sub_block[3]+block1_1[0]+"|"+sub_block[4]+" "+sub_block[5]+block1_2[0]+"|"+sub_block[6]+" "+sub_block[7]+block1_3[0])

print("Second Concatenation: ",block1_0[7]+sub_block[0]+" "+sub_block[1]+block1_0[0]+"|"+block1_1[7]+sub_block[2]+" "+sub_block[3]+block1_1[0]+"|"+block1_2[7]+sub_block[4]+" "+sub_block[5]+block1_2[0]+"|"+block1_3[7]+sub_block[6]+" "+sub_block[7]+block1_3[0])

print("Third Concatenation: ",block1_0[7]+sub_block[0]+block1_0[4]+" "+sub_block[1]+block1_0[0]+"|"+block1_1[7]+sub_block[2]+block1_1[4]+" "+sub_block[3]+block1_1[0]+"|"+block1_2[7]+sub_block[4]+block1_2[4]+" "+sub_block[5]+block1_2[0]+"|"+block1_3[7]+sub_block[6]+block1_3[4]+" "+sub_block[7]+block1_3[0])

print("Fourth Concatenation: ",block1_0[7]+sub_block[0]+block1_0[4]+" "+block1_0[3]+sub_block[1]+block1_0[0]+"|"+block1_1[7]+sub_block[2]+block1_1[4]+" "+block1_1[3]+sub_block[3]+block1_1[0]+"|"+block1_2[7]+sub_block[4]+block1_2[4]+" "+block1_2[3]+sub_block[5]+block1_2[0]+"|"+block1_3[7]+sub_block[6]+block1_3[4]+" "+block1_3[3]+sub_block[7]+block1_3[0])

