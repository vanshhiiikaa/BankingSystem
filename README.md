# Banking System

A Python application that simulates core banking operations — account creation, deposits, withdrawals, balance inquiry, and transaction history — for multiple users.

## Features

- Create a new bank account (with account holder name, account number, initial deposit)
- Login/authenticate using account number and PIN
- Deposit and withdraw money
- Check account balance
- View transaction history
- Handles multiple accounts/users
- Input validation (invalid account, insufficient balance, negative amounts)

## Demo

```
--- Banking System ---
1. Create Account
2. Login
3. Exit

Select an option: 1
Enter your name: Vanshika
Set a 4-digit PIN: 1234
Enter initial deposit amount: 1000
Account created successfully! Your Account Number: 100001

Select an option: 2
Enter Account Number: 100001
Enter PIN: 1234
Login successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Logout

Select an option: 3
Enter amount to withdraw: 200
Withdrawal successful. New balance: ₹800
```

## How It Works

1. New users create an account with their details and an initial deposit
2. Each account is assigned a unique account number and secured with a PIN
3. Users log in using their account number and PIN
4. Once authenticated, users can deposit, withdraw, check balance, or view transaction history
5. All account data is stored (in-memory, a file, or a database — update based on your implementation)

## Getting Started

### Prerequisites
- Python 3.x
- (Add here if used: SQLite/MySQL for persistent account storage)

### Installation
```bash
git clone https://github.com/vanshhiiikaa/Banking-System.git
cd Banking-System
```

### Usage
```bash
python banking_system.py
```
Then follow the on-screen menu to create an account or log in.

## Tech Stack
- Python 3
- (Add: SQLite/MySQL if account data is stored in a database rather than in-memory)

## Possible Improvements
- [ ] Persist account data between sessions using a database (if not already done)
- [ ] Add fund transfer between accounts
- [ ] Lock account after repeated failed PIN attempts
- [ ] Add interest calculation for savings accounts
- [ ] Add a GUI or web interface
- [ ] Add unit tests

## Author
**Vanshika**
- GitHub: [@vanshhiiikaa](https://github.com/vanshhiiikaa)
- LinkedIn: [Vanshika Gupta](https://www.linkedin.com/in/vanshika-gupta-4a2002329)

## License
This project is open source and available under the [MIT License](LICENSE).
