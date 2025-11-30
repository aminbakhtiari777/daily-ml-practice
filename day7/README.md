
This project uses the **Students Performance** dataset from Kaggle to build a simple machine learning model that predicts a student's **math score** based on demographic and academic features.

The goal is to practice a clean ML workflow:
data loading  
preprocessing  
encoding categorical features  
train/test split  
model training  
evaluation  
feature importance analysis  

---

## Dataset
Source: *Students Performance in Exams* (Kaggle)

Key columns:
- `gender`
- `race/ethnicity`
- `parental level of education`
- `lunch`
Ex_day7_week2

- `test preparation course`
- `math score`  
- `reading score`
- `writing score`

---

## Target Variable
math score

Reason:
It is a continuous numerical value.
Suitable for a **regression problem**.
Easy to interpret: *predict the math score based on the student’s profile and other exam scores.*

---

##  ML Workflow

### 1. Load Data
python
df = pd.read_csv("StudentsPerformance.csv")
