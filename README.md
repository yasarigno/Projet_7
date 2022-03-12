---
### PROJET-7
### Home Credit Default Risk. 
---

We implement Machine Learning algorithms to predict whether a client of HOME CREDIT will be able to repay a loan or he/she will have repayment difficulties.

The company [Home Credit](https://www.homecredit.net) wants to implement a “credit scoring” tool to calculate the probability that a customer will repay their credit, then classify the request as granted or refused credit. Therefore, they wish to develop a classification algorithm based on various data sources (behavioral data, data from other financial institutions, etc.).

<p align="center">
<img align="center" src="support\home_credit_logo.jpeg" style="width: 300px" />
</p>

In addition, customer relationship managers have reported that customers are increasingly demanding transparency with respect to credit granting decisions. This customer demand for transparency is completely in line with the values that the company wants to embody. We therefore decide to develop an [interactive dashboard](https://projet-7-credit.herokuapp.com) so that customer relationship managers can both explain credit granting decisions as transparently as possible, but also allow their customers to access their personal information and explore them easily.

There are already work done by other Data Scientist on this problem. [Will Koehrsen](https://www.kaggle.com/willkoehrsen) has a series of notebooks which explain all steps of solving this problem in an exceptional way. We start by one of his [notebook](https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction/notebook) on Kaggle and modify it for our needs.

The dataset contains a binary variable called **TARGET** where **0** indicates that the customer has repaid the credit as **1** means that he had difficulties to repay the credit on time. 

---
### Data source:

https://www.kaggle.com/c/home-credit-default-risk/data

| application_train  |   |
|---|---|
|  number of lines |   307 511 |
|  number of columns |   122 |
| application_test  |   |
|  number of lines |   48 744 |
|  number of columns |   121 |

---

The notebook contains a standard pipeline of Machine Learning:

<p align="center">
<img align="center" src="support\MLOps.jpeg" style="width: 700px" />
</p>

---
We have tested the following Machine Learning algorithms in this project:
- Linear Regression
- KNN
- Gradient Boosting
- Random Forest
- XGBoost

https://projet-7-credit.herokuapp.com


_EDIT: The work here needs a modification. For some reasons I need to wait to change them._
