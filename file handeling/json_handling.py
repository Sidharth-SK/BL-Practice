import json
file_path = 'BL Fellowship/file handeling/hdfc_loan_sample_20_rows.json'


with open(file_path, 'r') as f:
    dataset = json.load(f)
    for data in dataset:
        print(data['Loan_ID'])

approved: int = 0
rejected: int = 0
with open(file_path, 'r') as f:
    dataset = json.load(f)
    for data in dataset:
        if data['Loan_Status'] == 'Approved':
            approved += 1
        else:
            rejected += 1

print(f"Approved: {approved}")
print(f"Rejected: {rejected}")


with open(file_path, 'r') as f:
    dict_list:  dict[str, list[str | int]] = {}
    dataset = json.load(f)
    for data in dataset:
        dict_list[data['Loan_ID']] = [data['Customer_Name'], data['Loan_Amount'], data['Loan_Status']]
print(f"{dict_list}")


with open(file_path, 'r') as f:
    upper_limit_loan:  dict[str, list[str | int]] = {}
    dataset = json.load(f)
    for data in dataset:
        if data['Loan_Amount'] > 5000000:
            upper_limit_loan[data['Loan_ID']] = [data['Customer_Name'], data['Loan_Amount']]
print(f"{upper_limit_loan}")


approved_cibil: list[float] = []
rejected_cibil: list[float] = []
with open(file_path, 'r') as f:
    dataset = json.load(f)
    for data in dataset:
        if data['Loan_Status'] == 'Approved':
            approved_cibil.append(data['CIBIL_Score'])
        else:
            rejected_cibil.append(data['CIBIL_Score'])

approved_avg: float = sum(approved_cibil) / len(approved_cibil)
rejected_avg: float = sum(rejected_cibil) / len(rejected_cibil)

print(f"Approved CIBIL avg: {approved_avg}")
print(f"Rejected CIBIL avg: {rejected_avg}")


with open(file_path, 'r') as f:
    dataset = json.load(f)
    for data in dataset:
        if any(null in data.values() for null in [None, 'null', '']):
            print(f"Null found in: \t{data['Loan_ID']}")


#add a new key called EMI
interest_rates = {
    'Home': 8.5,
    'Auto': 9.5,
    'Business': 10.5,
    'Personal': 11.5,
    'Medical': 9.0,
    'Education': 9.5,
    'Default': 10.0  # Default rate if purpose not found
}
def calc_emi(loan_amount, loan_term_months, annual_rate):
    monthly_rate = annual_rate / 12
    emi = loan_amount * (monthly_rate / (1 - (1 + monthly_rate)**(-loan_term_months)))
    return emi

with open(file_path, 'r', encoding='utf-8') as f:
    dataset = json.load(f)
    for data in dataset:
        purpose = data['Purpose_of_Loan']
        rate = interest_rates.get(purpose, interest_rates['Default'])
        emi = calc_emi(data['Loan_Amount'], data['Loan_Term_Months'], rate)
        data['EMI'] = emi
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)