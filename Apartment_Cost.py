import pickle
import streamlit as st

model = pickle.load(open('estimasi_apartment.sav', 'rb'))

st.title('Estimasi Harga Apartment di Azerbaijan')

#urutan inputan model : 
#area (m^2), jumlah kamar, 
# apakah bangunan baru?(1 yes, 0 no), 
# apakah sudah pernah diperbaiki?(1 yes, 0 no), 
# apakah ada akta pembelian??(1 yes, 0 no), 
# mortage(1 yes, 0 no), 
# apakah di lantai pertama?(1 yes, 0 no),
# apakah di lantai terakhir?(1 yes, 0 no), 
# location (0 = quarter, 1 = rayon, 2 = metro ).

area = st.number_input('Masukkan luas area (m^2)', min_value=0.0, step=0.1)
bedroom = st.number_input('Masukkan jumlah kamar', step=1, max_value=20, min_value=0)
new = st.selectbox('Apakah bangunan baru?', ['Yes', 'No'])

if new == 'Yes':
    new = 1
else:
    new = 0
repaired = st.selectbox('Apakah sudah pernah diperbaiki?', ['Yes', 'No'])
if repaired == 'Yes':
    repaired = 1
else:
    repaired = 0
deed = st.selectbox('Apakah ada akta pembelian?', ['Yes', 'No'])
if deed == 'Yes':
    deed = 1
else:
    deed = 0
mortage = st.selectbox('Apakah ada mortage?', ['Yes', 'No'])
if mortage == 'Yes':
    mortage = 1
else:
    mortage = 0
first_floor = st.selectbox('Apakah di lantai pertama?', ['Yes', 'No'])
if first_floor == 'Yes':
    first_floor = 1
else:
    first_floor = 0
last_floor = st.selectbox('Apakah di lantai terakhir?', ['Yes', 'No'])
if last_floor == 'Yes':
    last_floor = 1
else:
    last_floor = 0
location = st.selectbox('Lokasi', ['Quarter', 'Rayon', 'Metro'])
if location == 'Quarter':
    location = 0
elif location == 'Rayon':
    location = 1
else:
    location = 2

if st.button('Estimasi Harga'):
    if area == 0 or bedroom == 0:
        st.write('Masukkan luas area dan jumlah kamar terlebih dahulu')
        st.stop()
    else:
        result = model.predict([[area, bedroom, new, repaired, deed, mortage, first_floor, last_floor, location]])
        formatted_result_AZN = "{:,.2f}".format(round(result[0], 2))
        formatted_result_IDR = "{:,.2f}".format(round(result[0] * 9245.97, 2))
        st.write('Harga Apartment dalam AZN : ', formatted_result_AZN)
        st.write('Harga Apartment dalam IDR(Juta) : ', formatted_result_IDR)



