# Student Exam Risk Prediction System

## Project Description
This project predicts students' exam risk using their attendance, internal marks, assignment scores, and study hours. 
The system uses a Data Engineering pipeline to clean and structure the data, and a Logistic Regression machine learning model to predict Pass/Fail risk. Visualizations highlight key patterns for better understanding.

## Features
- Early identification of students at high risk of failing
- Data cleaning and preprocessing using Python and Pandas
- Machine Learning with Logistic Regression
- Visualizations for Attendance, Marks, and Risk Distribution
- Predictions saved in CSV for further analysis

## Folder Structure
student-exam-risk-prediction/
│
├── data/
│ ├── student_data.csv
│ ├── cleaned_student_data.csv
│ └── predictions.csv
├── notebooks/
│ ├── check_dataset.ipynb
│ ├── data_preprocessing.ipynb
│ ├── eda.ipynb
│ └── ml_model.ipynb
├── reports/
│ ├── attendance_vs_result.png
│ └── risk_distribution.png
└── README.md

## How to Run
1. Open the project folder in VS Code.
2. Install required libraries:
3. Open Jupyter Notebook and run:
   - `check_dataset.ipynb` → verify dataset
   - `data_preprocessing.ipynb` → clean data
   - `eda.ipynb` → explore data and generate graphs
   - `ml_model.ipynb` → train model and predict risk
4. Check `data/predictions.csv` for predicted risk
5. Check `reports/` folder for saved graphs

## Tools & Technologies
- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook / VS Code

## Future Scope
- Integrate real-time attendance system
- Use advanced ML models like Random Forest or XGBoost
- Provide personalized improvement suggestions for students
