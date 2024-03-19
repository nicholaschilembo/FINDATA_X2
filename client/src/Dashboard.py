import streamlit as st

def dashboard():
    st.title('FINDataX Admin Dashboard')

    st.write('## Navigation')
    menu_options = ['Transactions', 'Accounts']
    selected_option = st.selectbox('Select a page', menu_options)

    if selected_option == 'Transactions':
        st.write('Display transactions page here...')
    elif selected_option == 'Accounts':
        st.write('Display accounts page here...')

if __name__ == '__main__':
    dashboard()
