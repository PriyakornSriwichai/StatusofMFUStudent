import streamlit as st
import pandas as pd
import pickle 

st.image('./mfu1.jpg')
st.title(""" 

Status of MFU Student 

""")




st.sidebar.header('User Input') 
st.sidebar.subheader('Please enter your data:')

# -- Define function to display widgets and store data
def get_input():
    # Display widgets and store their values in variables
    v_Sex = st.sidebar.radio('Sex', ['Male','Female'])
    v_Years = st.sidebar.selectbox('Years', [2561,2562,2563,2564])
    v_TCAS = st.sidebar.selectbox('TCAS', [1,2,3,4,5])
    v_FacultyID = st.sidebar.selectbox('FacultyID', [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    v_School = st.sidebar.selectbox('School Of', ['Agro-industry','Cosmetic Science','Dentistry', 
    'Health Science', 'Information Technology', 'Integrative Medicine', 'Law', 'Liberal Arts', 
    'Management', 'Medicine','Nursing','Science','Sinology','Social Innovation'])
    v_GPA = st.sidebar.number_input('GPAX')
    v_StudentTH = st.sidebar.radio('Thai/International Student', ['Thai','International'])
    v_LevelID = st.sidebar.selectbox('LevelID', [1,2,3,4,5])
    v_EntryTypeID = st.sidebar.slider('EntryTypeID', min_value=0, max_value=100)
    v_HomeRegion = st.sidebar.selectbox('HomeRegion',['International', 'North','Central','South','East','West','Bankok','North East'])
    v_EntryTypeName = st.sidebar.selectbox('EntryTypeName',['FOREIGNER','QUOTA 17 NORTHERN PROVINCES','DIRECT ADMISSION BY SCHOOL','INTERNATIONAL SCHOOL','ADMISSIONS',
               'QUOTA BY SCHOOL','SPECIAL FOR GOOD STUDENT','GOOD BEHAVE STUDENTS','CHIANG RAI DEVELOPMENT SCHOLARSHIP','DIRECT ADMISSION',
               'RE-ID FIRST SEMESTER GPAX 2.00'])
    v_DepartmentCode = st.sidebar.number_input('DepartmentCode')


    # Change the value of sex to be {'M', 'F'} as stored in the trained dataset
    if v_Sex == 'Female':
        v_Sex = '1'
    elif v_Sex == 'Male':
        v_Sex = '2'


    if v_School == 'Agro-industry':
        v_School = 1
    elif v_School == 'Cosmetic Science':
        v_School = 2
    elif v_School == 'Dentistry':
        v_School = 3
    elif v_School == 'Health Science':
        v_School = 4
    elif v_School == 'Information Technology':
        v_School = 5
    elif v_School == 'Integrative Medicine':
        v_School = 6
    elif v_School == 'Law':
        v_School = 7
    elif v_School == 'Liberal Arts':
        v_School = 8
    elif v_School == 'Management':
        v_School = 9        
    elif v_School == 'Medicine':
        v_School = 10
    elif v_School == 'Nursing':
        v_School = 11
    elif v_School == 'Science':
        v_School = 12
    elif v_School == 'Sinology':
        v_School = 13
    elif v_School == 'Social Innovation':
        v_School = 14

    if v_StudentTH == 'Thai':
        v_StudentTH = 1
    if v_StudentTH == 'International':
        v_StudentTH = 2

    if v_HomeRegion == 'International':
        v_HomeRegion = 1
    elif v_HomeRegion == 'North':
        v_HomeRegion = 2
    elif v_HomeRegion == 'Central':
        v_HomeRegion = 3
    elif v_HomeRegion == 'South':
        v_HomeRegion = 4
    elif v_HomeRegion == 'East':
        v_HomeRegion = 5
    elif v_HomeRegion == 'West':
        v_HomeRegion = 6
    elif v_HomeRegion == 'Bankok':
        v_HomeRegion = 7
    elif v_HomeRegion == 'North East':
        v_HomeRegion = 8

    if v_EntryTypeName == 'FOREIGNER':
        v_EntryTypeName = 1
    elif v_EntryTypeName == 'QUOTA 17 NORTHERN PROVINCES':
        v_EntryTypeName = 2
    elif v_EntryTypeName == 'DIRECT ADMISSION BY SCHOOL':
        v_EntryTypeName = 3
    elif v_EntryTypeName == 'INTERNATIONAL SCHOOL':
        v_EntryTypeName = 4
    elif v_EntryTypeName == 'ADMISSIONS':
        v_EntryTypeName = 5
    elif v_EntryTypeName == 'QUOTA BY SCHOOL':
        v_EntryTypeName = 6
    elif v_EntryTypeName == 'SPECIAL FOR GOOD STUDENT':
        v_EntryTypeName = 7
    elif v_EntryTypeName == 'GOOD BEHAVE STUDENTS':
        v_EntryTypeName = 8
    elif v_EntryTypeName == 'CHIANG RAI DEVELOPMENT SCHOLARSHIP':
        v_EntryTypeName = 9
    elif v_EntryTypeName == 'DIRECT ADMISSION':
        v_EntryTypeName = 10
    elif v_EntryTypeName == 'RE-ID FIRST SEMESTER GPAX 2.00':
        v_EntryTypeName = 11
    


    # Store user input data in a dictionary
    data = {'Sex': v_Sex,
            'Years': v_Years,
            'TCAS': v_TCAS,
            'FacultyID': v_FacultyID,
            'School Of': v_School,
            'GPAX': v_GPA,
            'Thai/International Student': v_StudentTH,
            'LevelID': v_LevelID,
            'EntryTypeID': v_EntryTypeID,
            'HomeRegion': v_HomeRegion,
            'EntryTypeName': v_EntryTypeName,
            'DepartmentCode': v_DepartmentCode,}


    # Create a data frame from the above dictionary
    data_df = pd.DataFrame(data, index =[0])
    return data_df

# -- Call function to display widgets and get data from user
df = get_input()

st.header('Application of Status of MFU Student :')

# -- Display new data from user inputs:
st.subheader('User Input:')
st.write(df)

# -- Data Pre-processing for New Data:
# Combines user input data with sample dataset
# The sample data contains unique values for each nominal features
# This will be used for the One-hot encoding
data_sample = pd.read_csv('AI.csv')
df = pd.concat([df, data_sample],axis=0)

#One-hot encoding for nominal features
cat_data = pd.get_dummies(df[['School Of']])

#Combine all transformed features together
X = pd.concat([cat_data, df], axis=1)
X = X[:1] # Select only the first row (the user input data)

#Drop un-used feature
X = X.drop(columns=['Status','AcademicYear','StudentTH','FacultyName'])

# -- Display pre-processed new data:
st.subheader('Pre-Processed Input:')
st.write(X)

