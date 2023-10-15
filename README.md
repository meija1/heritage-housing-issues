# House Sale Price Predictor
This project aims to predict house prices in Aimes / Iowa and sale price for clients inherited houses using machine learning and data analysis.The main goal for this project is to help customer understand what house features correlates to house sale price and aid machine learning in making accurate predictions. The machine learning models used in this project are trained and tested on the dataset found in kaggle.com.
![responsive](https://github.com/meija1/heritage-housing-issues/assets/109754892/55a93126-8e9d-44bb-aa08-acd21c7b0d32)
## Table of Contents
* [Dataset Content](#dataset-content)
* [Business Requirements](#business-requirements)
* [CRISP-DM](#crisp-dm)
* [Hypothesis and validation](#hypothesis-and-validation)
* [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
* [ML Business Case](#ml-business-case)
* [Dashboard Design](#dashboard-design)
* [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment)
* [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|



## Business Requirements
A client who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, has requested to  help in maximising the sales price for the inherited properties.

Although client has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and has provided data for that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## CRISP-DM
Cross-industry standard process for data mining followed the base process:

1 - Buisness Understanding - Understanding the clients goals and what expectations from the model.

2 - Data Understanding - How the data works and meaning behind the variables.

3 - Data Preparation - Process the data using data cleaning and importing features to prepare the data for modeling.

4 - Modeling - Model the data for business needs using algorithms and spliting data into train and test sets.

5 - Evaluation - Evaluate the model if it meets the business standarts and evaluate it's performance. If it doesn't meet the requirements, start from step 1.

6 - Deployment - Deploy a finished project and app if the client is happy with the model.

## Hypothesis and validation
* 1: Sale Price for a house strongly correlates with the houses overall quality, meaning it could be the physical condition and/or social and physical environment.
  * How to validate: Data showed if the houses quality rating is higher, the house price is often high.
* 2: Ground living area square feet, Garage area, Total square feet of basement area are strong indicators for machine learning model that these features increase the sale price of the house.
  * How to validate: Our correlation study confirms that these features are one of the highest in correlation with the sale price.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
Business requirement 1:
* Collect data and inspect the data from kaggle.
* Study data using spearman and pearson methods to find correlation between the data.
* Visualize the data to understand the correlation.
Business requirement 2:
* Perform data cleaning to improve machine learning performance.
* Apply categorical or numerical encoders to transform the data.
* Find the best regressor model with best parameters to predict house sale price.
* Create a dashboard for client to visualize data and have an interface to predict house price
User Stories:
* As a user I can view variable features so that it's understood which correlates to the house sale price.
* As a user I can view project summary so that it's understood what and how the project works.
* As a user I can view project hypothesis so that I see if data has been validated.
* As a user I can select 4 house attribute so that I can view predicted price for all 4 inherited houses.
* As a user I can view model performance so that its known of how the model works and it's accuracy.

## ML Business Case
* We want ML model to predict sale price of a house and be able to visualize the data on a user friendly dashboard.
* Our ideal outcome is for the machine learning model to be able to predict house prices and clieants inherited property value as accurate as possible
* The model succsess metrics are:
  * At least a 0.7 R2 score on train and test set
* The model output is 0.8 on the R2 score that gives us a predictive value in dollaras of a house in Ames, Iowa.
* The training data was collected from public dataset on kaggle, it consists of nearly 1500 house records and their features.


## Dashboard Design
### Project Summary page
* Summarises project and tells about projects dataset. It includes projects Terms & Jargon and lists business requirements.
### Project Hypothesis
* Gives projects hypothesis and validation
### Predict House Price
* Includes Predict House Price Interface with 4 variables as input feature to predict any house price in Ames, Iowa
### Predict Inherited House Price
* Includes visible data of clients 4 inheted houses with the most important features for prediction. Underneath is a button to run the inherited house prediction.
### House Price Study
* Displays house price dataset in the first checkbox and variables that is most correlated with the sale price. Two checkboxes displaying spearman and pearson calculations on data correlation and short description. Sale price analysis checkbox shows correlation on these most correlated variables.
### Machine Learning Model
* Short description of the model and visualizing pipeline. Displayig 4 features the model was trained on and it's bar plot. Showing pipeline performance on train and test set incliding mean squared error, mean absolute error and r2 score


## Unfixed Bugs
No bugs recorded to my knowledge

## Deployment
### Heroku

* The App live link is: [House Price Predictor App](https://house-price-predict-1ae8b9e93921.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Codeanywhere - Used as development environment
* GitHub - For hosting the project
* Heroku - Deployment and hosting the app
* Jupyter Notebooks - Main software for data analysis and machine learning models using python
* Python - Was the main programming language used.
* Kaggle - Where the data for house prices was taken from
* Streamlit - Used to create dashboard interface for the client
* Pandas library - To read and inspect the data
* Feature Engine - Used for transformers and engineer data: Missing data imputation, Categorical encoding, Variable transformation
* scikit learn - Used for machine learning library like regression, classification, clustering, and statistical tools
* matplotlib - To display and visulize data in heatmaps and histograms

## Credits 
### Content 
- The project was heavily helped by Walkthrough Project 2-Churnometer by Code Institute, with their custom functions and features for the model and dashboard. [Churnometer](https://github.com/Code-Institute-Solutions/churnometer)
- A lot of common errors was fixed with the help of [Slack](https://app.slack.com/)
- Most errors and bugs were fixed by finding similar problems on [StackOverflow](https://stackoverflow.com/)

### Media
No media used in this project


## Acknowledgements
* Thanks to slack community for quick and helpfull responses
* This project would not be possible without Walkthrough Project 2-Churnometer guidence
* A big thanks to Code Institutes tutors and mentors for their support and help with the project

