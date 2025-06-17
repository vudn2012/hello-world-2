import streamlit as st

st.title('Đăng ký tài khoản')
my_bar = st.progress(0)

# Danh sách các trường thông tin đăng ký
quiz = ['Tài khoản:', 'Mật khẩu:', 'Nhập lại mật khẩu:', 'Tên người dùng:', 'Email:']
answers = {}
len_quiz = len(quiz)

for field in quiz:
    answers[field] = st.text_input(field, '' if 'Mật khẩu' not in field else '', type='password' if 'Mật khẩu' in field else 'default')

if st.button('Xác nhận'):
    filled_fields = sum(1 for value in answers.values() if value.strip() != '')

    if filled_fields == len_quiz:
        my_bar.progress(100)
        st.success('Bạn đã hoàn thành đầy đủ thông tin!')
        st.balloons()
    else:
        my_bar.progress(int((filled_fields / len_quiz) * 100))
        st.warning('Bạn chưa hoàn thành đầy đủ thông tin!')

# Hiển thị thông tin đã nhập (không hiển thị mật khẩu)
st.subheader('Thông tin đã nhập:')
for key, value in answers.items():
    if 'Mật khẩu' not in key:
        st.write(f"{key} {value}")
