import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

enroll_1 = pd.read_csv('api_data_aadhar_enrolment/api_data_aadhar_enrolment_0_500000.csv');
enroll_1.head();
enroll_1.shape;
enroll_1['state'].unique();

enroll_1['new_date'] = pd.to_datetime(enroll_1['date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d');

enroll_1['new_date'].isnull().sum();
print(enroll_1['new_date'].max());
print(enroll_1['new_date'].min());


enroll_2 = pd.read_csv('api_data_aadhar_enrolment_1000000_1006029.csv')
enroll_2.head()

df = pd.concat([enroll_1, enroll_2],axis=0, ignore_index=True)