Sales Prediction App

The Sales Prediction App is a web-based tool that predicts future sales based on various user-provided inputs. It leverages a trained machine learning model to provide accurate sales forecasts.

Project Structure

Here’s an overview of the key components:

-app.py: The main application script that runs the sales prediction app using Streamlit.
- model.ipynb: A Jupyter Notebook detailing the data analysis, model training, testing, and evaluation.
- encoders.pkl: A serialized file containing encoders for categorical features, used to prepare input data for prediction.
- scaler.pkl: A serialized scaler used to normalize numerical features for consistent and accurate model predictions.
- requirements.txt: Lists all Python dependencies required to run the application.
- .gitignore: Specifies files and directories (e.g., virtual environments) to be ignored by Git.


# Disclaimer#

Initially, the project requirements specified that the web application should be deployed on AWS. While I successfully built and deployed the Sales Prediction App on an AWS EC2 instance, recurring stability issues (such as frequent shutdowns and service interruptions) impacted the user experience.

To ensure a more reliable, accessible, and seamless experience, I chose to redeploy the app on Streamlit Cloud, a free, robust hosting platform for web applications. This switch allows the app to meet all project goals while maintaining smooth functionality in data processing and sales predictions.

All core features, including the Streamlit-based UI and predictive analytics, remain fully aligned with the original project objectives.

You can view the deployed application here:  

https://salespredictions.streamlit.app/
