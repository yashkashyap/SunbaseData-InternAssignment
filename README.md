# Customer Churn Prediction

## Introduction
This project is to predict customer churn of a telecom company. The dataset contains 100000 rows and 9 columns. I have done EDA and Feature Engineering on the data and have been to predict the churn with 0.918 accuracy.

## Data
The data is extremely even, with no outliers. The data is also very clean, with no missing values. The data is also very balanced, with 50% of the data being churned customers and 50% of the data being non-churned customers. The churn value is extremely difficult to predict as for similar kind of samples the prediction values can vary. The plots in the notebooks show this scenario effectively.

## Approach
Initially, I tried creating new features and build a model on top of them but the performance was really poor. Later I used the oversampling technique (SMOTE) to generate new samples and somehow make the data more ready for prediction. This approach worked really well and I was able to achieve 0.90 accuracy on the test set. Thereafter, I selected features based on feature importance and correlation matrix and achieved an accuracy of 0.918 on the test set at last.

## Conclusion
The data is difficult to handle and understand but the oversampling helped me reach the final score.