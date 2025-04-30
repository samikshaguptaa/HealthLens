import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os

#loading the saved models
diabetes_model = pickle.load(open('C:/Users/TTBSADMIN/OneDrive/Desktop/Health prediction/Diabetes_model.sav','rb'))
heart_model = pickle.load(open('C:/Users/TTBSADMIN/OneDrive/Desktop/Health prediction/Heart_model.sav','rb')) 
parkinson_model = pickle.load(open('C:/Users/TTBSADMIN/OneDrive/Desktop/Health prediction/parkinson_model.sav','rb'))


#sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           icons=['droplet', 'heart-pulse', 'activity'],
                            default_index=0,
                            orientation='vertical')
    
if selected == 'Diabetes Prediction':
    st.title('Diabetes Detective: Cracking the Sugar Case')
    st.markdown('-----')
    col1,col2,col3 = st.columns(3)
    
    with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       
    with col2:
       Glucose = st.text_input('Glucose')
       
    with col3:
       BloodPressure = st.text_input('BloodPressure')
       
    with col1:
       SkinThickness = st.text_input('SkinThickness')
       
    with col2:
       Insulin = st.text_input('Insulin')
       
    with col3:
       BMI = st.text_input('BMI')
       
    with col1:
       DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
       
    with col2:
       Age = st.text_input('Age')
       
    diab_diagnosis = '';
    
    if st.button('Diabetes Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        
        diab_prediction = diabetes_model.predict([user_input])
        
        if diab_prediction[0] == 0:
            diab_diagnosis = 'Not Diabetic'
        else:
            diab_diagnosis = 'Diabetic'
            
    st.success(diab_diagnosis)
    
if selected == 'Heart Disease Prediction':
    st.title('The Pulse Patrol 🚨')
    st.markdown('-----')
    col1, col2,col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest pain(cp)')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Cholesterol')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
        
    with col1:
        restecg = st.text_input('Heart Test')
        
    with col2:
        thalach = st.text_input('Max Heart Rate')
        
    with col3:
        exang = st.text_input('Exercise Pain')
        
    with col1:
        oldpeak = st.text_input('oldpeak')
    
    with col2:
        slope = st.text_input('slope')
        
    with col3:
        ca = st.text_input('Blocked Blood Pipes')
        
    with col1:
        thal = st.text_input('Heart Blood Issue')
        
    heart_pred = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        
        heart_prediction = heart_model.predict([user_input])
        
        if heart_prediction[0]==1:
            heart_pred = 'The person is having heart disease'
        else:
            heart_pred = 'The person does not have heart disease'
            
    st.success(heart_pred)
    
if selected == 'Parkinson Prediction':
    st.title('Stop the Shake Before It Takes')
    st.markdown('----')
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        MDVPFo_Hz = st.text_input('Average voice pitch')
    with col2:
        MDVP_Fhi_Hz = st.text_input('Highest pitch')
    with col3:
        MDVP_Flo_Hz = st.text_input('Lowest pitch')
    with col4:
        Jitter = st.text_input('Voice frequency instability')
    with col1:
        Jitter_Abs = st.text_input('Absolute pitch variation')
    with col2:
        RAP = st.text_input('Short-term pitch variation')
    with col3:
        PPQ = st.text_input('Pitch period consistency')
    with col4:
        DDP = st.text_input('Small-scale jitter fluctuation')
    with col1:
        Shimmer = st.text_input('Shimmer')
    with col2:
        Shimmer_dB = st.text_input('Loudness variation')
    with col3:
        Shimmer_APQ3 = st.text_input('Short-term amplitude variation')
    with col4:
        Shimmer_APQ5 = st.text_input('Amplitude perturbation measure')
    with col1:
        MDVP_APQ = st.text_input(' Overall amplitude consistency')
    with col2:
        Shimmer_DDA = st.text_input('Small-scale shimmer deviation')
    with col3:
        NHR = st.text_input('Noise in voice')
    with col4:
        HNR = st.text_input('Harmonics in voice')
    with col1:
        RPDE = st.text_input('Recurrence Period Density Entropy')
    with col2:
        DFA = st.text_input('Detrended Fluctuation Analysis')
    with col3:
        Spread1 = st.text_input('Frequency deviation')
    with col4:
        Spread2 = st.text_input('Pitch variability')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
        
    Parkinson_pred = ''
    if st.button('Parkinson Disease Test Result'):
        user_input = [MDVPFo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, Jitter, Jitter_Abs,RAP,PPQ,
                      DDP,Shimmer,Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,
                      HNR,NHR,RPDE,Spread1,Spread2,D2,PPE]
        
        user_input = [float(x) for x in user_input]
        
        Parkinson_prediction = parkinson_model.predict([user_input])
        
        if Parkinson_prediction[0]==1:
            Parkinson_pred = 'The person is having Parkinson disease'
        else:
            Parkinson_pred = 'The person does not have Parkinson disease'
            
    st.success(Parkinson_pred)