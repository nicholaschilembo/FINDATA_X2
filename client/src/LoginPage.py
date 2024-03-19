import streamlit as st

def login_page():
    st.title('FINDataX Admin Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        # Validate credentials (e.g., against a smart contract or database)
        is_valid = validate_credentials(username, password)

        if is_valid:
            st.success('Login successful! Redirecting to admin dashboard...')
            # Redirect to admin dashboard - You can use st.experimental_set_query_params to pass parameters to the dashboard page
            st.experimental_rerun()
        else:
            st.error('Invalid credentials')

def validate_credentials(username, password):
    # Add your credential validation logic here
    # For example, you might check against a database or a smart contract
    # Replace this with your actual validation logic
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

if __name__ == '__main__':
    login_page()
