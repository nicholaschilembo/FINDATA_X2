cimport streamlit as st
import random

def dashboard():
    st.title('Welcome MZANSI WEB3 to your FINDataX Adminstrator Dashboard')

    st.write('## Navigation')
    menu_options = ['Transactions', 'Accounts']
    selected_option = st.selectbox('Select a page', menu_options)

    if selected_option == 'Transactions':
        if st.button('Display Transactions'):
            display_transactions()
    elif selected_option == 'Accounts':
        if st.button('Display Accounts'):
            create_random_accounts()

def display_transactions():
    st.title('Transactions as of today')
    
    transactions = generate_random_transactions()
    
    st.write('### Transactions:')
    for txn in transactions:
        if txn['status'] == 'valid':
            if st.button(f'Generate Smart Contract for Transaction ID {txn["id"]}', key=f'txn_{txn["id"]}', help=f'Transaction ID {txn["id"]} is valid. Click to generate smart contract', class_='btn btn-success'):
                generate_smart_contract(txn)
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
    st.title('RAccounts as of today')
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
            if st.button(f'Generate Smart Contract for Account Number {account["account_number"]}', key=f'acc_{account["account_number"]}', help=f'Account Number {account["account_number"]} is valid. Click to generate smart contract', class_='btn btn-success'):
                generate_smart_contract(account)
        else:
            st.write(f'Account Number {account["account_number"]} is invalid. Reason: {account["reason"]}')

    st.write('### Invalid Accounts:')
    for account in invalid_accounts:
        st.write(f'Account Number {account["account_number"]} is invalid. Reason: {account["reason"]}')

def generate_smart_contract(data):
    # Here you would generate the immutable document with the provided data
    st.write(f'Generated Smart Contract for {data}')
    st.success('Smart contract generated successfully!')

if __name__ == '__main__':
    dashboard()
