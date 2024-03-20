import streamlit as st
import random

# Minimalistic theme with light background and dark text
st.set_page_config(page_title="FINDataX Admin", page_config={"layout": "wide"})

# Placeholder user data (replace with your authentication method)
users = [
    {"name": "John Doe", "pin": 1234, "industry": "Banking", "designation": "Manager"},
    # Add more users with pin, name, industry and designation
]

def login_page():
  """
  Function to display the login page and handle authentication
  """
  name = st.text_input("Name")
  pin = st.text_input("PIN", type="password")  # Mask pin input
  industry = st.selectbox("Financial Industry", ["Banking", "Insurance", "Investment", "Other"])
  designation = st.text_input("Designation")
  login_button = st.button("Login")

  if login_button:
    # Validate user input with placeholder data
    for user in users:
      if user["name"] == name and user["pin"] == int(pin) and user["industry"] == industry and user["designation"] == designation:
        st.session_state["logged_in"] = True  # Set session state for login status
        st.session_state["user_data"] = user  # Store user data in session state
        return  # Exit function if valid credentials found
    st.error("Incorrect credentials")

def dashboard():
  """
  Function to display the administrator dashboard
  """
  user_data = st.session_state["user_data"]
  st.title(f'FINDATAX ADMINISTRATOR DASHBOARD - Welcome {user_data["name"]}')

  st.write('## Navigation')
  menu_options = ['Transactions', 'Accounts']
  selected_option = st.selectbox('', menu_options, format_func=lambda x: x.title())  # Concise option display

  if selected_option == 'Transactions':
      if st.button('Show Transactions'):
          display_transactions()
  elif selected_option == 'Accounts':
      if st.button('Create Accounts'):
          create_random_accounts()

def display_transactions():
    st.title('Todays Transactions')
    
    transactions = generate_random_transactions()
    
    st.write('### Transactions:')
    for txn in transactions:
        status_color = 'green' if txn['status'] == 'valid' else 'red'  # Apply color based on status
        status_text = txn['status'].title()  # Capitalize status
        col1, col2 = st.columns(2)  # Split columns for transaction details and button
        with col1:
            st.write(f'**ID:** {txn["id"]}')
            st.write(f'**Status:** <span style="color:{status_color}">{status_text}</span>', unsafe_allow_html=True)  # Colored status display
            if txn['status'] == 'invalid':
                st.write(f'**Reason:** {txn["reason"]}')
        with col2:
            if txn['status'] == 'valid':
                if st.button(f'Generate Smart Contract'):
                    generate_smart_contract(txn)

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
    st.title('Accounts Created')
    valid_accounts = []
    invalid_accounts = []

    # Create 5 valid accounts
    for i in range(5):
        account_number = ''.join(random.choices('0123456789', k=8))
        valid_accounts.append({'account_number': account_number, 'status': 'valid'})

    # Create 5 invalid accounts
    for i in range(5):
        account_number = ''.join(random.choices('0123456789', k=8))
        reason = random.choice
