# 🏦 Banking System

A command-line based **Python Banking System** that allows users to manage basic banking operations such as creating accounts, depositing and withdrawing funds, checking balances, and transferring money between accounts — all while enforcing essential banking rules like minimum balance maintenance.

---

## 📋 Features

- ✅ **Create Bank Account** with proper validations (numeric, 5-digit, and minimum deposit).
- 💰 **Deposit Funds** into existing accounts.
- 🏧 **Withdraw Funds** while ensuring minimum balance of ₹1000 is maintained.
- 🔄 **Transfer Funds** between accounts with validation for sufficient funds and minimum balance enforcement.
- 📈 **Check Account Balance** of any valid account.
- 🚫 **Error Handling** for invalid inputs and business rule violations.

---

## 🛠️ Requirements

- **Python 3.x**

---

## 🚀 How to Run

1. Clone the repository or download the `BankingSystem.py` file.
2. Open a terminal or command prompt.
3. Run the script by typing:

```bash
python BankingSystem.py
```

---

## 📎 Business Rules
1. 🔢 Account numbers must be numeric and exactly 5 digits.
2. 💵 Initial balance when creating an account must be at least ₹1000.
3. 📉 After withdrawal or transfer, an account must not fall below ₹1000.
4. ➕ Only positive values are allowed for deposit, withdrawal, and transfer.
