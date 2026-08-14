"""
Challenge: Loan Validator

Validate loan eligibility based on various conditions, such as:
- Minimum age requirement
- Credit score threshold
- Income level
- Employment status
- Debt-to-income ratio

This module provides functions to determine whether an applicant qualifies
for a loan based on predefined business rules.

Minimum age (e.g., 18 years)
Minimum credit score (e.g., 600)
Minimum income (e.g., R$ 1,500)
Accepted employment statuses (e.g., "employed", "self-employed")
Maximum acceptable debt-to-income ratio (e.g., 40%)
"""

def loan_validator(minimum_age, credit_score, income_level, employment_status, debts) -> bool:
    if minimum_age < 0 | income_level < 0:
        print("Input valid data.")
        return False
    if minimum_age < 18:
        print("The minimum age requerid is 18y.")
        return False
    if credit_score < 600:
        print("The credit score is to low.")
        return False
    if income_level < 1500:
        print("The income level is to low.")
        return False
    if employment_status not in ["employed",  "self-employed"]:
        print("You need to be employed or sel-employed.")
        return False
    dti_ratio = debts/income_level
    if dti_ratio > 0.4:
        print(f"The debt to income ratio is to low: {dti_ratio*100}.")
        return False
    print("All information has been validated; the loan has been accepted.")
    return True    

# --- Basic Tests ---

# 1. Approved case (all valid data)
assert loan_validator(25, 700, 3000, "employed", 500) == True

# 2. Rejected: age below minimum
assert loan_validator(16, 700, 3000, "employed", 500) == False

# 3. Rejected: credit score too low
assert loan_validator(25, 500, 3000, "employed", 500) == False

# 4. Rejected: income too low
assert loan_validator(25, 700, 1000, "employed", 500) == False

# 5. Rejected: unemployed
assert loan_validator(25, 700, 3000, "unemployed", 500) == False

print("All tests passed!")
