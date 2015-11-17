# Standard import for pandas, numpy and matplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
from dateutil.parser import parse

# Read in the csv file, parse the date
dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p')
complaints=pd.read_csv("311_Service_Requests_from_2010_to_Present.csv",parse_dates=['Created Date'],date_parser=dateparse) #maybe add 


#Q1: What fraction of complaints are associated with the 2nd most popular agency?
#question 1 - just get the 2nd most frequent value, divide by the column total (cast to float)

complaints = complaints.dropna(subset=['Agency']) #remove any null values from Agency
agency_counts = complaints['Agency'].value_counts() #make a new dataframe for Agency

print "Q1: The 2nd most popular agency is the", agency_counts.index.values[1]
print "and the fraction of complaints associated with it are", float(agency_counts[1]) / float(agency_counts.sum())


#Q2: What is the distance (in degrees) between the 90% and 10% percentiles of degrees latitude?
complaints = complaints.dropna(subset=['Latitude']) #remove any null values from Latitude
latitude_col = complaints['Latitude']

print "Q2: latitude 90% percentile is", latitude_col.quantile(0.9)
print "latitude 10% perecentile is", latitude_col.quantile(0.1)
print "and their difference is", latitude_col.quantile(0.9) - latitude_col.quantile(0.1)

#Q3: What is the difference between the expected number of calls received during 
#the most and least popular whole hours of the day? 

complaints = complaints.dropna(subset=['Created Date']) #remove any null values from Created Date
created_hours = complaints['Created Date'].dt.hour

print "Q3: most popular hour is", created_hours.value_counts().index.values[0], "with", created_hours.value_counts().max(), " calls"
print "the least popular hour is", created_hours.value_counts().idxmin(), "with", created_hours.value_counts().min(), "calls"
print "their difference is", (created_hours.value_counts().max() - created_hours.value_counts().min())

#Q4

complaints = complaints.dropna(subset=['Complaint Type']) #remove any null values from Created Date
boroComplaint = complaints[['Complaint Type','Borough']]
c_type = complaints['Complaint Type']

#print "complaints I MADE A LIST", c_type

#cond = boroComplaint.groupby('Borough').c_type.value_counts()

#/ boroComplaint.groupby('Complaint Type').b.count()
#print "cond is ", cond

#print "c_type counts ", (c_type.value_counts() / c_type.value_counts().sum())

#bCgroup = boroComplaint.groupby('Borough')
#print boroComplaint
#created_hours = pd.Datetimeindex(complaints['Created Date']).hour #use 'H' at some point


#Q5
#lat and long correspond to x, y
#mean of x, stddev of x, and y (max gives the height of the peak?) calculating cwd?



#Q6: What is the standard deviation in seconds of the time between consecutive calls?

created_seconds = complaints['Created Date'].dt.second + complaints['Created Date'].dt.minute * 60 + complaints['Created Date'].dt.hour * 3600 + complaints['Created Date'].dt.day * 24 * 3600
difference = abs(created_seconds - created_seconds.shift())

std = difference.std()

print "Q6: standard deviation between consecutive calls is", std



