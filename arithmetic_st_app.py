import streamlit as st
from PIL import Image

add_selectbox = st.sidebar.selectbox(
    'Yapmak istediğin işlemei seç',
    ('TOPLAMA', 'ÇIKARMA')
)

st.markdown('### ARITMETK ISLEMI')
st.write('iki','değişkenin',add_selectbox, 'islemleri yapıyoruz :)')
ilk_slider = st.sidebar.slider('Ilk değerini kaydırarak seç', 0.0, 10000.0, 0.0)

ikinci_slider = st.sidebar.slider( 'ikinci değerini kaydırarak seç',  0.0, 5000.0, 0.0)


st.write('Girdiğin ilk değeri: ', ilk_slider)
st.write(' Girdiğin ikinci değeri: ',ikinci_slider)
st.write(' Girdiğin ikinci değeri: ',add_selectbox)

#Buttonu basınca Toplama veya cıkarma isleminin yapması

if st.button('Hesaplama için tıkla'):
	if add_selectbox=='TOPLAMA':
		st.write( 'Girdiklerinin Toplamını = ',ilk_slider + ikinci_slider)
		toplama_resimi=Image.open('image/Toplam.png')
		st.image(toplama_resimi, use_column_width=False)

	else:
		st.write('Girdiklerinin çıkarımını = ', ilk_slider - ikinci_slider	)
		cikarma_resimi=Image.open('image/çıkarma.png')
		st.image(cikarma_resimi,use_column_width=False)