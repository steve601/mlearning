import sklearn
import joblib
import streamlit as st
import requests
from streamlit_lottie import st_lottie

with open('rfc_model.pkl','rb') as model:
    classifier = joblib.load(model)

def predictor(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness):
    global classifier
    prediction = classifier.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])
    if prediction == 1:
        return 'Malignant(Cancerous)'
    else:
        return 'Benign(Non-cancerous)'

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code  != 200:
        return None
    return r.json()

lottie_health = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_izvmskti.json")
def main():
    st.set_page_config(page_title="My health webapp",page_icon=":tada:",layout="wide")
    st.subheader("Hi :wave:,am Steven,a second year student from Kenyatta University pursuing BSC in Mathematics and Computer science.")
    st.title("BREAST CANCER DIAGNOSIS APP")
    st.write("Breast Cancer is the most common cancer amongst women in the world and it accounts for 25 % of all cancer cases.")
    st.write("It starts when the cells in the Breast begin to grow out of control and they form tumors which can be seen via X-ray.")
    st.write("The key challenge of this app against its detection is how to classify tumors into 'Malignant(Cancerous)' or 'Benign(Non-cancerous)'.")
    st.subheader("Following are the inputs to be used;")
    st.write("Radius mean >> mean of radius of Lobes")
    st.write("Texture mean >> mean of surface texture")
    st.write("Perimeter mean >> mean of perimeter of Lobes")
    st.write("Area mean >> mean area of Lobes")
    st.write("Smoothness mean >> mean of the surface smoothness")

    st_lottie(lottie_health,height=300)

    mean_radius = st.number_input('Radius mean')
    mean_texture = st.number_input('Texture mean')
    mean_perimeter = st.number_input('Perimeter mean')
    mean_area = st.number_input('Area mean')
    mean_smoothness = st.number_input('Smoothness mean')



    if st.button('DETECT'):
        prediction = predictor(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness)
        if prediction == 1:
            st.success("Kindly go for a medical check up!!!,PAMOJA TUANGAMIZE SARATANI")
        else:
            st.success("You are in good health condition,PAMOJA TUANGAMIZE SARATANI")




if __name__ == '__main__':
    main()
    
