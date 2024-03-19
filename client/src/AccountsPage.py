import streamlit as st
from utils.blockchain import get_accounts, validate_account

def accounts_page():
    st.title('Accounts')

    # Fetch accounts from the blockchain
    accounts = get_accounts()

    # Display accounts in a list
    for account in accounts:
        st.write(account['name'])

        # Add a button to validate the account
        if st.button(f'Validate {account["name"]}'):
            if validate_account(account):
                st.success('Account is valid, executing smart contract')
            else:
                st.error('Invalid account')

if __name__ == '__main__':
    accounts_page()