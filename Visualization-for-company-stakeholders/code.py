# --------------
# --------------

#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================================================================

# Company has more 'loan approvals' or 'loan disapprovals'?
# Can one of the company's health factors be it's loan status distribution?

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot.bar()

# ============================================================================================================================

# Which is the region with the highest no. of loan approvals? lowest no. of loan approvals?
# Which is the region with the maximum difference between loan approvals and loan rejections?

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind = 'bar', stacked=False) 

plt.xlabel('Property Area')
plt.ylabel('Loan Status') 

plt.xticks(rotation=45) 

# ============================================================================================================================

# Overall which group has asked for higher loan services irrespective of the approval? Graduate or Non Graduate?
# Which group has had better approval to non approval ratio? Graduate or Non Graduate?

education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind = 'bar', stacked=True) 

plt.xlabel('Education Status')
plt.ylabel('Loan Status') 

plt.xticks(rotation=45) 

# ============================================================================================================================

# Do Graduate people get approved a higher amount than their Non Graduate counterparts?
# What's the average amount of loan approved for Graduate? for Non Graduate? Is there a huge difference between the two? 

graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate') 
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate') 

#For automatic legend display
plt.legend()

# ============================================================================================================================

# Is there a correlation between 'ApplicantIncome' and 'LoanAmount'?(One way to know that is look at the line formed when you connect the scatter plot dots?)
# Is the 'TotalIncome' better related to the 'LoanAmount' than 'ApplicantIncome'?

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1) 

ax_1.plot(data['ApplicantIncome'], data['LoanAmount']) 
ax_1.set_title('Applicant Income') 

ax_2.plot(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.plot(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income') 

# ============================================================================================================================


