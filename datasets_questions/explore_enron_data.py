#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "People in dictionary: ", len(enron_data)
print "Features in dictionary: ", len(enron_data["SKILLING JEFFREY K"])

totalLength = len(enron_data)
poiCount = sum(enron_data[key]["poi"] for key in enron_data)
withSalaryCount = sum(0 if enron_data[key]["salary"] == "NaN" else 1 for key in enron_data)
withEmailCount = sum(0 if enron_data[key]["email_address"] == "NaN" else 1 for key in enron_data)
withoutTotalPayments = float(sum(1 if enron_data[key]["total_payments"] == "NaN" else 0 for key in enron_data))
withoutTotalPaymentsPoi = float(sum(1 if (enron_data[key]["total_payments"] == "NaN" and enron_data[key]["poi"]) else 0 for key in enron_data))

print "Total people: ", totalLength
print "Persons of interest: ", poiCount
print "Persons with salary: ", withSalaryCount
print "Persons with email: ", withEmailCount
print "Persons without total paymenst: ", withoutTotalPayments, " , percentage", withoutTotalPayments/totalLength
print "POI without total paymenst: ", withoutTotalPaymentsPoi, " , percentage", withoutTotalPaymentsPoi/poiCount

print "Payments"
print "Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Kenneth Lay: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Andrew Fastow: ", enron_data["FASTOW ANDREW S"]["total_payments"]



