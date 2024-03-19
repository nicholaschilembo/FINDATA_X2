import streamlit as st
import random

def dashboard():
    st.title('FINDataX Admin Dashboard')

    st.write('## Navigation')
    menu_options = ['Transactions', 'Accounts']
    selected_option = st.selectbox('Select a page', menu_options)

    if selected_option == 'Transactions':
        if st.button('Go to Transactions Page'):
            display_transactions()
    elif selected_option == 'Accounts':
        if st.button('Display Accounts'):
            create_random_accounts()

def display_transactions():
    st.title('Transactions Page')
    # Add code to display transactions here

def create_random_accounts():
    st.title('FINDataX registered accounts')
    valid_accounts = []
    invalid_accounts = []

    # Create 5 valid accounts
    for i in range(5):
        account_number = random.randint(10000000, 99999999)  # 8-digit account number
        account_name = f'Account_{account_number}'
        account_balance = random.randint(100, 1000)
        valid_accounts.append((account_name, account_balance, True))

    # Create 5 invalid accounts
    reasons = ['inactive', 'suspected fraudulent activity', 'insufficient balance']
    for i in range(5):
        account_number = random.randint(10000000, 99999999)  # 8-digit account number
        account_name = f'Account_{account_number}'
        account_balance = random.randint(100, 499)  # Insufficient balance for invalid accounts
        reason = random.choice(reasons)
        invalid_accounts.append((account_name, account_balance, False, reason))

    # Display valid accounts
    st.write('### Valid Accounts:')
    for account_name, account_balance, _, in valid_accounts:
        st.write(f'- {account_name}: Balance - {account_balance}')

    # Display invalid accounts
    st.write('### Invalid Accounts:')
    for account_name, account_balance, _, reason in invalid_accounts:
        st.write(f'- {account_name}: Balance - {account_balance} [Invalid: {reason}]')

if __name__ == '__main__':
    dashboard()
