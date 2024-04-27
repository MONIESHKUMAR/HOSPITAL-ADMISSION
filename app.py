import streamlit as st

def get_doctor_appointment_1():
    st.write("1. STHISH KUMAR (MBBS,MD)")
    st.write("2. UDAY KUAMR (MBBS,MD)")
    st.write("3. KUMARA MONIESH (MBBS)")
    st.write("4. Random Doctor")
    doctor_selection = st.selectbox("Select the doctor for appointment:", ["STHISH KUMAR", "UDAY KUAMR", "KUMARA MONIESH", "Random Doctor"])
        
    time_preference = st.text_input("Enter your preferred time:")
    
    if(doctor_selection == "2" or doctor_selection == "4"):
        st.write("The Doctor is appointed successfully at ", time_preference)
        st.write("You will receive further updates on WhatsApp.")
    else:
        st.write("The doctor isn't available at your time preference.")
        

def get_doctor_appointment_2():
    st.write("1. DHANUSH (MBBS)")
    st.write("2. SUNDAR DAYAL (MBBS,MD)")
    st.write("3. DURAI MANAGATI (MD MBBS)")
    st.write("4. Random Doctor")
    doctor_selection = st.selectbox("Select the doctor for appointment:", ["DHANUSH", "SUNDAR DAYAL", "DURAI MANAGATI", "Random Doctor"])
        
    time_preference = st.text_input("Enter your preferred time:")
    
    if(doctor_selection == "2" or doctor_selection == "4"):
        st.write("The Doctor is appointed successfully at ", time_preference)
        st.write("You will receive further updates on WhatsApp.")
    else:
        st.write("The doctor isn't available at your time preference.")
        

def get_doctor_appointment_3():
    st.write("1. AMMIT(MBBS,MD)")
    st.write("2. SUNNIL(MBBS,DNB)")
    st.write("3. NAREN(MBBS)")
    st.write("4. Random Doctor")
    doctor_selection = st.selectbox("Select the doctor for appointment:", ["AMMIT(MBBS,MD)", "SUNNIL(MBBS,DNB)", "NAREN(MBBS)", "Random Doctor"])
        
    time_preference = st.text_input("Enter your preferred time:")
    
    if(doctor_selection == "2" or doctor_selection == "4"):
        st.write("The Doctor is appointed successfully at ", time_preference)
        st.write("You will receive further updates on WhatsApp.")
    else:
        st.write("The doctor isn't available at your time preference.")
           

def get_doctor_appointment_4():
    st.write("1. MAHANDRA (MBBS,MD)")
    st.write("2. SHINGH(MBBS)")
    st.write("3. DHONI(MBBS,MD)")
    st.write("4. Random Doctor")
    doctor_selection = st.selectbox("Select the doctor for appointment:", ["MAHANDRA (MBBS,MD)", "SHINGH(MBBS)", "DHONI(MBBS,MD)", "Random Doctor"])
        
    time_preference = st.text_input("Enter your preferred time:")
    
    if(doctor_selection == "2" or doctor_selection == "4"):
        st.write("The Doctor is appointed successfully at ", time_preference)
        st.write("You will receive further updates on WhatsApp.")
    else:
        st.write("The doctor isn't available at your time preference.")
               

def get_doctor_appointment_5():
    st.write("1. VIRAT(MBBS,WELL IN EAR)")
    st.write("2. KOHLI(MBBS,WELL IN TEETH)")
    st.write("3. HARINI(MBBS,WELL NOSE)")
    st.write("4. Random Doctor")
    doctor_selection = st.selectbox("Select the doctor for appointment:", ["VIRAT(MBBS,WELL IN EAR)", "KOHLI(MBBS,WELL IN TEETH)", "HARINI(MBBS,WELL NOSE)", "Random Doctor"])
        
    time_preference = st.text_input("Enter your preferred time:")
    
    if(doctor_selection == "2" or doctor_selection == "4"):
        st.write("The Doctor is appointed successfully at ", time_preference)
        st.write("You will receive further updates on WhatsApp.")
    else:
        st.write("The doctor isn't available at your time preference.")
          

def get_doctor_appointment_6():
    print("1. VIJAY(MBBS)")
    print("2. SIRIYA(MBBS)")
    print("3. SURIYA(MBBS)")
    print("4. Random Doctor")
    doctor_selection = int(input("Enter the option doctor for appointment: "))
        
    time_preference = input("Enter your prefered time: ")
    
    if(doctor_selection == 2):
        print("The Doctor is appointed successfully at ", time_preference)
        print("You will receive the further updates on whatsapp ")
    elif(doctor_selection == 4):
        print("The Doctor is appointed successfully at ", time_preference) 
        print("You will receive the further updates on whatsapp ")
    else:
        print("The doctor ins't available  at your time preference")
        get_doctor_appointment_6()   

# Define other get_doctor_appointment functions similarly...

def display_doctor_field():
    st.write("1. General Practitioner")
    st.write("2. Pediatrician")
    st.write("3. Neurolgist")
    st.write("4. Cardiologist")
    st.write("5. E. N. T")
    st.write("6. Orthologist")
    
    user_option = st.selectbox("Which type of doctor do you need?", ["General Practitioner", "Pediatrician", "Neurolgist", "Cardiologist", "E. N. T",])
    
    if(user_option == "General Practitioner"):
        get_doctor_appointment_1()
    elif(user_option == "Pediatrician"):
        get_doctor_appointment_2()
    elif(user_option == "Neurolgist"):
        st.write("you selected neuro")
        get_doctor_appointment_3()
    elif(user_option == "Cardiologist"):
        get_doctor_appointment_4()
    elif(user_option == "E. N. T"):
        get_doctor_appointment_5()

def main():
    st.title("Doctor Appointment System")
    st.write("Please fill in the following details:")

    patient_name = st.text_input("Enter your name:")
    patient_age = st.text_input("Enter your age:")
    patient_phone = st.text_input("Enter your mobile number:")
    patient_alternate_mobile_number = st.text_input("Enter your alternate mobile number:")
    patient_dob = st.date_input("Enter your D O B:")
    patient_height = st.number_input("Enter your height in cm:")
    patient_weight = st.number_input("Enter your weight in kg:")
    if patient_height !=0 and patient_weight !=0:
        height_in_meter = patient_height / 100
        patient_bmi = patient_weight / (height_in_meter ** 2)

        st.write("Your BMI is:", patient_bmi)

        if(patient_bmi < 18.5):
            st.write("You are underweight")
        elif(patient_bmi >= 18.5 and patient_bmi < 24.9):
            st.write("You are in a healthy weight range")
        elif(patient_bmi >= 25 and patient_bmi <= 29.9):
            st.write("You are overweight")
        else:
            st.write("You are obese")

    patient_symptoms = st.text_area("What kind of symptoms are you facing?")

    st.write("Let's proceed to select the type of doctor you need.")
    display_doctor_field()

if __name__ == "__main__":
    main()
