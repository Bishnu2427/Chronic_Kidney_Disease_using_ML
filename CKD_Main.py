import pickle
import streamlit as st

# Loading the Random Forest Regressor Model
pickle_in = open("ckd_model.pkl", "rb")
rfr_model = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_water_intake(wc,bgr,bu,sc,pcv,al,hemo,su,htn,bp):
    data=[[wc,bgr,bu,sc,pcv,al,hemo,su,htn,bp]]

    # Make the prediction based on Random Forest Regressor
    prediction = rfr_model.predict(data)

    # Handle potential output format
    predicted_water_intake = prediction[0]

    return predicted_water_intake

def pred_main():
    html_temp = """
        <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Chronic Kidney Disease Prediction</h2>
        </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    

    wc = st.text_input("White Blood Cell Count", "Type Here")
    bgr = st.text_input("Blood Glucose Random", "Type Here")
    bu = st.text_input("Blood Urea", "Type Here")
    sc = st.text_input("Serum Creatinine", "Type Here")
    pcv = st.text_input("Packed Cell Volume", "Type Here")
    al = st.text_input("Ablumin", "Type Here")
    hemo = st.text_input("Haemoglobin", "Type Here")
    su = st.text_input("Suger", "Type Here")
    htn = st.text_input("Hypertension", "Type Here")
    bp = st.text_input("Blood Pressure", "Type Here")
    
    result = ""
    
    if st.button("Predict CKD"):
        result = predict_water_intake(wc,bgr,bu,sc,pcv,al,hemo,su,htn,bp)
        if result is not None:  # Check if prediction was successful
            st.success('You have CKD. Please consult a healthcare professional for personalized advice .......')
        else:
            st.success("You don't have CKD, you are safe .....")
            
if __name__ == '__main__':
    pred_main()
