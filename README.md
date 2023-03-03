# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project is to utilize a machine learning model to predict if an applicant is likely to get a loan. This model will be deployed into a cloud where other users will be able to create a api post request to get results given they provide the necessary data. 

## Hypothesis
Applicants with a higher combined income will have a higher chance of obtaining a loan. This will be tested in the model with differing incomes and evaluate their predictions towards this hypothesis. 

Credit history will also have an impact on approving loans. This will be tested alongside with the other hypothesis but the change would be in the credit history to determine if this hypothesis is correct. 

## EDA 
Around 14% of people do not have a credit history. It is seen that there are large outliers in the applicant and coapplicant income causing a right skew of the data. Many of the data is from Males as they dominate 80% of the dataset. There is almost an equal amount of applicants living in all areas. Semi-Urban has the highest amount of applicants at 38% and rural at 29%. 65% of applicants are married which can be further investigated if they are going for a new home/car. At 87%, almost all of the applicants are not self-employed. The average loan amount is 146 thousand dollars which may be for a large purchase such as a house/land/business. On average, males have a higher income than females and having an education increases the overall income for both genders. 


## Process
1. Take a look at a general overview of the data
2. Create some visualizations to get an idea of some relationships between the data
3. Create pivot tables to understand how categorical features influences the numerical features
4. Cleaned the data by inputting missing values
5. Feature engineered total income from applicant and coapplicant income
6. Took the log of the incomes to get rid of extreme values
7. Create a logistic regression model by one hot encoding categorical features and scaling the numerical features
8. Performed gridsearch on baseline model to get the best hyperparameters
9. Create a pipeline to mainstream our model and test multiple models all at once
10. Chose the best model and exported to a pickle file
11. Create an api and deploy it to the cloud for anyone to utilize the model. 

## Results/Demo
The model performs with ~80% accuracy which is decent for a pre-screening method. The model has poor precision at ~39% for positive results but a good precision for negative results at 97%. An inperson talk with the applicant and more information would be required to ensure the application is actually approved for a loan but if they fail the screening with this model, it is likely they would not be eligble for the loan. 

## Challanges 
Getting the API to work and return results was a challenge as it involved a lot of debugging and getting it to the right format for Flask. Very hard to feature engineer as there were not enough columns to create new features. 

## Future Goals
I would like to get more information on the dataset such as age, country, city or year of application. This would be insightful information to have as features to build a better and more accurate model. There was a very high bias for males,marital status, education and employment type in the dataset which made the model bias for those features.