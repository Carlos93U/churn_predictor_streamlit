# CHURN_PREDICTOR | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" height=20> | <img src="https://i.postimg.cc/cHqB5VtL/scikit-learn-logo.png" height=20>| <img src="https://pandas.pydata.org/static/img/pandas_white.svg" height=20>  | <img src="https://i.postimg.cc/m2dwfTdm/numpy-logo.png" height=20> |  <img src="https://matplotlib.org/_static/logo_dark.svg" height=20> | <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" height=20> | <img src="https://assets.ydata.ai/oss/ydata-profiling_red.png" height=20> |[<img src="https://static-00.iconduck.com/assets.00/github-icon-2048x1988-jzvzcf2t.png" height=20> ](https://github.com/Carlos93U) | [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png" height=20>](https://www.linkedin.com/in/juan-carlos-huillcas/) |

## 1. Resume

The project focuses on a dataset from a telecommunications company to predict if customers will churn. It utilizes the scikit-learn library, specifically the binomial logistic regression model. The analysis involves exploring relevant variables and implementing the model to predict churn. The aim is to understand the factors influencing customer churn and provide a strategy to retain them using supervised learning techniques.


<center>

[![yprofile-online-video-cutter-com.gif](https://i.postimg.cc/L5632mwF/yprofile-online-video-cutter-com.gif)](https://postimg.cc/Pp9wMndS)


</center>


## 2. Data Set Characteristics

The churn_data contains the following features:


| Field              | Description                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
| `customerID`       | A unique ID that identifies each customer                                                                                 |
| `Gender`           | The customer's gender: Male, Female                                                                                       |
| `SeniorCitizen`    | Indicates if the customer is 65 or older: Yes, No                                                                        |
| `Partner`          | Indicates if the customer is married: Yes, No                                                                             |
| `Dependents`       | Indicates if the customer lives with any dependents: Yes, No. Dependents could be children, parents, grandparents, etc.  |
| `Tenure`           | Indicates the total amount of months that the customer has been with the company.                                          |
| `PhoneService`     | Indicates if the customer subscribes to home phone service with the company: Yes, No                                       |
| `MultipleLines`    | Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No                                |
| `InternetService`  | Indicates if the customer subscribes to Internet service with the company: No, DSL, Fiber Optic, Cable.                   |
| `OnlineSecurity`   | Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No            |
| `OnlineBackup`     | Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No             |
| `DeviceProtection` | Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No |
| `TechSupport`      | Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No |
| `StreamingTV`      | Indicates if the customer uses their Internet service to stream television programming from a third-party provider: Yes, No. The company does not charge an additional fee for this service. |
| `StreamingMovies`  | Indicates if the customer uses their Internet service to stream movies from a third-party provider: Yes, No. The company does not charge an additional fee for this service. |
| `Contract`         | Indicates the customer's current contract type: Month-to-Month, One Year, Two Year                                         |
| `PaperlessBilling` | Indicates if the customer has chosen paperless billing: Yes, No                                                           |
| `PaymentMethod`    | Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check                                     |
| `MonthlyCharge`    | Indicates the customer's current total monthly charge for all their services from the company.                              |
| `TotalCharges`     | Indicates the customer's total charges, calculated to the end of the quarter.                                              |
| `Churn`            | Yes = the customer left the company this quarter. No = the customer remained with the company                                |


## 3. Setting up

*Create a virtual enviroment with:*

```
python3 -m venv env

```
*Activate virtual enviroment:*

```
source env/bin/activate
```

*Install requirements*

```
pip install -r requirements.txt
```

## 4. Running

* *Open a churn predictor notebook*
* *Run All*
* *See outputs*

Correlation values about target variable:

[![out1.png](https://i.postimg.cc/4NNYZsbw/out1.png)](https://postimg.cc/9zKmY3kq)

Churn vs Gender

[![out2.png](https://i.postimg.cc/WzshdvRN/out2.png)](https://postimg.cc/CB6F29LX)

Top 10 variables that contrinute to churn

[![out3.png](https://i.postimg.cc/L5vhfbRz/out3.png)](https://postimg.cc/fStwQ5VL)

## 5. Conclutions:

* Approximately the same amount of men as women churn.
* Month-to-month contracts factor heavily into a user's decision to churn.
* Lack of online security and technical support greatly contribute to churn.
* High monthly charges and short tenure influence users to churn.
* Having a two-year contract is a good indicator that the user will not churn from the company.
* Variables contributing the most precision to the model can be selected progressively.


## 5. Libraries and documentation

* [Python](https://www.python.org/doc/)
* [sklearn](https://scikit-learn.org/stable/)
* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [seaborn](https://seaborn.pydata.org/index.html#)
* [ydata_profiling](https://docs.profiling.ydata.ai/latest/)

## 6. Sources
* [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)