import streamlit as st
import random

def dashboard():
    st.title('FINDataX Admin Dashboard')

    st.write('## Navigation')
    menu_options = ['Transactions', 'Accounts']
    selected_option = st.selectbox('Select a page', menu_options)

    if selected_option == 'Transactions':
        if st.button('Show Random Transactions'):
            display_transactions()
    elif selected_option == 'Accounts':
        if st.button('Create Random Accounts'):
            create_random_accounts()

def display_transactions():
    st.title('Random Transactions')
    
    transactions = generate_random_transactions()
    
    st.write('### Successful Transactions:')
    successful_transactions = [txn for txn in transactions if txn['status'] == 'successful']
    if successful_transactions:
        for txn in successful_transactions:
            st.write(f'- From: {txn["from_account"]} To: {txn["to_account"]} Amount: {txn["amount"]}')

    st.write('### Pending Transactions:')
    pending_transactions = [txn for txn in transactions if txn['status'] == 'pending']
    if pending_transactions:
        for txn in pending_transactions:
            st.write(f'- From: {txn["from_account"]} To: {txn["to_account"]} Amount: {txn["amount"]}')

    st.write('### Denied Transactions:')
    denied_transactions = [txn for txn in transactions if txn['status'] == 'denied']
    if denied_transactions:
        for txn in denied_transactions:
            st.write(f'- From: {txn["from_account"]} To: {txn["to_account"]} Amount: {txn["amount"]}')

def generate_random_transactions():
    transactions = []
    for _ in range(10):
        from_account = random.randint(10000000, 99999999)
        to_account = random.randint(10000000, 99999999)
        amount = random.randint(100, 1000)
        status = random.choice(['successful', 'pending', 'denied'])
        transactions.append({'from_account': from_account, 'to_account': to_account, 'amount': amount, 'status': status})
    return transactions

def create_random_accounts():
    st.title('Random Accounts Created')
    valid_accounts = []
    invalid_accounts = []

    # Create 5 valid accounts
    for i in range(5):
        account_number = ''.join(random.choices('0123456789', k=8))
        account_name = f'Valid_Account_{i}'
        account_balance = random.randint(500, 1000)
        valid_accounts.append((account_number, account_name, account_balance))

    # Create 5 invalid accounts
    for i in range(5):
        account_number = ''.join(random.choices('0123456789', k=8))
        account_name = f'Invalid_Account_{i}'
        account_balance = random.randint(0, 499)
        invalid_reason = random.choice(['Inactive', 'Suspected fraudulent activity', 'Insufficient balance'])
        invalid_accounts.append((account_number, account_name, account_balance, invalid_reason))

    # Display valid accounts
    st.write('### Valid Accounts:')
    for account_number, account_name, account_balance in valid_accounts:
        st.write(f'- Account Number: {account_number}, Name: {account_name}, Balance: {account_balance}')

    # Display invalid accounts
    st.write('### Invalid Accounts:')
    for account_number, account_name, account_balance, invalid_reason in invalid_accounts:
        st.write(f'- Account Number: {account_number}, Name: {account_name}, Balance: {account_balance}, Invalid Reason: {invalid_reason}')

if __name__ == '__main__':
    dashboard()
