from flask import Flask, render_template, request
import os
import joblib

app = Flask(__name__)
clf_rf = joblib.load('random_forest_model.pkl')  # Load your trained model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Fetch input values from the form
            checking_account = request.form['checking_account']
            duration = int(request.form['duration'])
            credit_history = request.form['credit_history']
            purpose = request.form['purpose']
            credit_amount = int(request.form['credit_amount'])
            savings_account_bonds = request.form['savings_account_bonds']
            employment = request.form['employment']
            installment_rate = int(request.form['installment_rate'])
            personal_status_and_sex = request.form['personal_status_and_sex']
            other_debtors = request.form['other_debtors']
            residence = int(request.form['residence'])
            property = request.form['property']
            age = int(request.form['age'])
            other_installment_plans = request.form['other_installment_plans']
            housing = request.form['housing']
            credits = int(request.form['credits'])
            job = request.form['job']
            people_liable = int(request.form['people_liable'])
            telephone = request.form['telephone']
            foreign_worker = request.form['foreign_worker']

            # Convert checking_account 
            if checking_account == 'A11 :      ... <    0 DM':
                checking_account_final = 0
            elif checking_account =='A12 : 0 <= ... <  200 DM':
                checking_account_final = 1
            elif checking_account == 'A13 :      ... >= 200 DM':
                checking_account_final = 2
            else:
                checking_account_final = 3

            # Convert credit_history
            if credit_history == 'A11 :      ... <    0A30 : no credits taken/ all credits paid back duly DM':
                credit_history_final = 0
            elif credit_history =='A31 : all credits at this bank paid back duly':
                credit_history_final = 1
            elif credit_history =='A32 : existing credits paid back duly till now':
                credit_history_final = 2
            elif credit_history == 'A33 : delay in paying off in the past':
                credit_history_final = 3
            else:
                credit_history_final = 4
            
            # Convert purpose
            if purpose == 'A40 : car (new)':
                purpose_final = 1
            elif purpose =='A41 : car (used)':
                purpose_final = 2
            elif purpose =='A42 : furniture/equipment':
                purpose_final = 3
            elif purpose == 'A43 : radio/television':
                purpose_final = 4
            elif purpose =='A44 : domestic appliances':
                purpose_final = 5
            elif purpose =='A45 : repairs':
                purpose_final = 6
            elif purpose == 'A46 : education':
                purpose_final = 7
            # elif purpose =='A47 : (vacation - does not exist?)':
            #     purpose_final = 7
            elif purpose =='A48 : retraining':
                purpose_final = 8
            elif purpose == 'A49 : business':
                purpose_final = 9
            else:
                purpose_final = 0

            # Convert savings_account_bonds
            if savings_account_bonds == 'A61 :          ... <  100 DM':
                savings_account_bonds_final = 0
            elif savings_account_bonds =='A62 :   100 <= ... <  500 DM':
                savings_account_bonds_final = 1
            elif savings_account_bonds =='A63 :   500 <= ... < 1000 DM':
                savings_account_bonds_final = 2
            elif savings_account_bonds == 'A64 :          .. >= 1000 DM':
                savings_account_bonds_final = 3
            else:
                savings_account_bonds_final = 4
            
            # Convert employment
            if employment == 'A71 : unemployed':
                employment_final = 0
            elif employment =='A72 :       ... < 1 year':
                employment_final = 1
            elif employment =='A73 : 1  <= ... < 4 years':
                employment_final = 2
            elif employment == 'A74 : 4  <= ... <br 7 years':
                employment_final = 3
            else:
                employment_final = 4
            
            # Convert personal_status_and_sex
            if personal_status_and_sex == 'A91 : male   : divorced/separated':
                personal_status_and_sex_final = 0
            elif personal_status_and_sex =='A92 : female : divorced/separated/married':
                personal_status_and_sex_final = 1
            elif personal_status_and_sex =='A93 : male   : single':
                personal_status_and_sex_final = 2
            elif personal_status_and_sex =='A94 : male   : married/widowed':
                personal_status_and_sex_final = 3
            else:
                personal_status_and_sex_final = 4

            # Convert other_debtors
            if other_debtors == 'A101 : none':
                other_debtors_final = 0
            elif other_debtors =='A102 : co-applicant':
                other_debtors_final = 1
            else:
                other_debtors_final = 2
            
            # Convert property
            if property == 'A121 : real estate':
                property_final = 0
            elif property =='A122 : if not A121 : building society savings agreement/life insurance':
                property_final = 1
            elif property =='A123 : if not A121/A122 : car or other, not in attribute 6':
                property_final = 2
            else:
                property_final = 3
            
            # Convert other_installment_plans
            if other_installment_plans == 'A141 : bank':
                other_installment_plans_final = 0
            elif other_installment_plans =='A142 : stores':
                other_installment_plans_final = 1
            else:
                other_installment_plans_final = 2
            
            # Convert housing
            if housing == 'A151 : rent':
                housing_final = 0
            elif housing =='A152 : own':
                housing_final = 1
            else:
                housing_final = 2
            
            # Convert job
            if job == 'A171 : unemployed/ unskilled  - non-resident':
                job_final = 0
            elif job =='A172 : unskilled - resident':
                job_final = 1
            elif job =='A173 : skilled employee / official':
                job_final = 2
            else:
                job_final = 3
            
            # Convert telephone
            if telephone == 'A191 : none':
                telephone_final = 0
            else:
                telephone_final = 1
            
            # Convert foreign_worker
            if foreign_worker == 'A201 : yes':
                foreign_worker_final = 0
            else:
                foreign_worker_final = 1

            # Create feature vector
            user_features = [[checking_account_final,duration,credit_history_final,purpose_final,credit_amount,savings_account_bonds_final,employment_final,installment_rate,personal_status_and_sex_final,other_debtors_final,residence,property_final,age,other_installment_plans_final,housing_final,credits,job_final,people_liable,telephone_final,foreign_worker_final]]

            # Predict using the trained model
            prediction = clf_rf.predict(user_features)

            # Return prediction result
            result = "Congratulations! Based on our analysis, you have a <b><i><u>Good Credit</u></i></b> status.</br> This indicates a strong financial profile and reliable creditworthiness." if prediction[0] == 1 else "Unfortunately, our analysis indicates a <b><i><u>Bad Credit</u></i></b> status. This suggests potential challenges in your financial profile and creditworthiness."
            return render_template('result.html', result=result)
        
    except Exception as e:
        error_message = f"An error occurred during prediction: {str(e)}"
        return render_template('result.html', result=error_message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
