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
    
    st.write('### Transactions:')
    for txn in transactions:
        if txn['status'] == 'valid':
            if st.button(f'Generate Smart Contract for Transaction ID {txn["id"]}'):
                st.write(f'Smart contract generated for Transaction ID {txn["id"]}')
        else:
            st.write(f'Transaction ID {txn["id"]} is invalid. Reason: {txn["reason"]}')

def generate_random_transactions():
    transactions = []
    for i in range(10):
        status = random.choice(['valid', 'invalid'])
        reason = ''
        if status == 'invalid':
            reason = random.choice(['Inactive', 'Suspected fraudulent activity', 'Insufficient balance'])
        transactions.append({'id': i+1, 'status': status, 'reason': reason})
    return transactions

def create_random_accounts():
    st.title('Random Accounts Created')
    valid_accounts = []
    invalid_accounts = []

    # Create 5 valid accounts
    for i in range(5):
        account_number = ''.join(random.choices('0123456789', k=8))
        valid_accounts.append({'account_number': account_number, 'status': 'valid'})

    # Create 5 invalid accounts
    for i in range(5):
        account_number = ''.join(random.choices('0123456789', k=8))
        reason = random.choice(['Inactive', 'Suspected fraudulent activity', 'Insufficient balance'])
        invalid_accounts.append({'account_number': account_number, 'status': 'invalid', 'reason': reason})

    st.write('### Valid Accounts:')
    for account in valid_accounts:
        if account['status'] == 'valid':
            if st.button(f'Generate Smart Contract for Account Number {account["account_number"]}'):
                st.write(f'Smart contract generated for Account Number {account["account_number"]}')
        else:
            st.write(f'Account Number {account["account_number"]} is invalid. Reason: {account["reason"]}')

    st.write('### Invalid Accounts:')
    for account in invalid_accounts:
        st.write(f'Account Number {account["account_number"]} is invalid. Reason: {account["reason"]}')

if __name__ == '__main__':
    dashboard()
