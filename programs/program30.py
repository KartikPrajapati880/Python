# Write a function to convert USD to INR

def usd_inr(inr):
    conver_rate = 83
    return inr * conver_rate

inr_rs = float(input("Enter the amount: "))
print("USD to INR: ", usd_inr(inr_rs))