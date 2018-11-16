#! /usr/bin/env python3

# data preprocess for UC FYP 2018
import pandas as pd
import os
import numpy as np


df = pd.read_csv('data.csv')
df = df.dropna()
problems = list(df.columns)[1:]

l_factor = [1,2,3,4,8]
l_feeling = [6,7,8]

target_problem = problems[-1]
#target_classes = df[target_problem].unique()
target_classes = ['蜜月阶段：乐于接触，期待融入','沮丧阶段：发现差异，遇到障碍','内卷阶段：偏安一隅，拒绝融入','恢复调整：逐渐适应，积极接受','适应阶段：完全融入，适应文化']
target_mask = {}

for t_class in target_classes:
	yon = np.array(df[target_problem].apply(lambda x: 1 if x==t_class else 0))
	target_mask[t_class] = np.array(yon)


for problem in problems[:-1]:
	print(problem)
	df_problem = df[problem]
	answers = df_problem.unique()
	
	for answer in answers:
		print(answer)
		yon = np.array(df_problem.apply(lambda x: 1 if x==answer else 0))
		tot_in_answer = 0
		sub_dict = {}
		for t_class in target_classes:
			intersect = np.sum(yon * (target_mask[t_class]))
			tot_in_answer += intersect
			sub_dict[t_class] = intersect
		for t_class in target_classes:
			print(t_class,' number: ',sub_dict[t_class],' percentage in answer: ',round(sub_dict[t_class]/tot_in_answer,2),' percentage in class: ',round(sub_dict[t_class]/np.sum(target_mask[t_class]),2))

