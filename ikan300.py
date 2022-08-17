# library
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import random
from streamlit_option_menu import option_menu
from skimage.io import imread
from skimage.transform import resize
from PIL import Image
from datetime import datetime
from streamlit_cropper import st_cropper
import streamlit.components.v1 as html
from st_aggrid import AgGrid
import plotly.express as px
import io
import sqlite3
import cv2

import numpy as np
from PIL import Image as im

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(page_title="Devina SVM", page_icon="./favicon.ico", layout="centered", initial_sidebar_state="auto", menu_items={
    'Get Help': 'https://www.extremelycoolapp.com/help',
    'Report a bug': "https://www.extremelycoolapp.com/bug",
    'About': "# This is a header. This is an *extremely* cool app!"
})
# Configuration Key

conn = sqlite3.connect("data.db")
c = conn.cursor()


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO usertable(username, password) VALUES (?,?)',
              (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password =?',
              (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data

#path_logo_png = r"./Img/logo_pnl.png"
#imagefeed = Image.open(path_logo_png)
st.markdown(
            "<p style='text-align: left; color: white;'>Silahkan pilih metode login.</p>", unsafe_allow_html=True)
st.markdown(
            "<p style='text-align: left; color: white;'>Gulir kebawah, untuk mulai menggunakan aplikasi....</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3) 
with col1: st.write(' ') 
#with col2: st.image(imagefeed, caption='Politeknik Negeri Lhokseumawe') 
with col3: st.write(' ')
# st.image(imagefeed, caption='Politeknik Negeri Lhokseumawe')
st.markdown(
            "<h1 style='text-align: center; color: black;'>Rancang Bangun Sistem Identifikasi Kesegaran Ikan Berdasarkan Citra Mata Menggunakan SVM (Support Vector Machine)</h1>", unsafe_allow_html=True)
st.markdown(
            "<h2 style='text-align: center; color: black;'>Devina Humaira Putri (1857301065)</h1>", unsafe_allow_html=True)
st.sidebar.title("Silahkan Login")

# Authentication
choice = st.sidebar.selectbox('Login', ['Admin', 'User'])

# Path
path_grafik = r"./Img/graph.jpg"
path_ikan_jpg = r"./Img/ket_ikan.jpg"
path_model = r"./300px.p" #Edit / ganti file model


# App

# Login Block

if choice == 'Admin':
    # Obtain User Input for email and password
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.checkbox("Login"):
        create_usertable()
        result = login_user(username, password)
        if result:
            st.success("Masuk sebagai {}".format(username))
            choose = option_menu("Menu", ["Panduan", "Tentang", "Unggah", "Kamera", "Informasi", "Dataset"],
                                 icons=['house-door', 'info-circle', 'upload',
                                        'camera', 'info', 'file-arrow-up'],
                                 menu_icon="app-indicator",
                                 default_index=0,
                                 orientation="horizontal",
                                 styles={
                "container": {"padding": "5!important", "background-color": "#EFF2F9"}, 
                "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#008080"},
            }
            )


# Beranda PAGE
            if choose == 'Informasi':
                st.markdown(
                    "<h1 style='text-align: center; color: black;'>Informasi Dataset dan Model</h1>", unsafe_allow_html=True)
                st.markdown('Grafik dibawah ini menunjukkan jumlah dataset yang digunakan per kategori, untuk melakukan proses training')
                imagefeed = Image.open(path_grafik)
                col1, col2, col3 = st.columns(3) 
                with col1: st.write(' ') 
                with col2: st.image(imagefeed, caption='Grafik Dataset')
                with col3: st.write(' ')
                #st.image(imagefeed, caption='Grafik Dataset')
                # Model
                st.markdown("Pada link dibawah ini merupakan file Jupyter Notebook yang berisi informasi pelatihan dalam tahap pembuatan model")
                if st.button("Informasi Model"):
                    "[klik disini](https://drive.google.com/file/d/1Jhez2f4ni4dkB2O4GXWeUlBjtweoMkrq/view?usp=sharing)"
                #HSV
                # st.markdown('Pada penelitian ini feature extraction dilakukan dengan cara mengkonversi citra rgb menjadi hsv, perbandingan dari kedua gambar ditunjukkan dibawah ini.')
                # path_rgb_jpg = r"./Img/preview.jpg"
                # path_hsv_jpg = r"./Img/hsv.jpg"
                # col1, col2 = st.columns(2) 
                # with col1: st.image(path_rgb_jpg, caption='RGB') 
                # with col2: st.image(path_hsv_jpg, caption='HSV')

            elif choose == 'Panduan':
                st.markdown(
                    "<h1 style='text-align: center; color: black;'>Panduan Penggunaan Sistem</h1>", unsafe_allow_html=True)
                st.markdown('Halo! Terima kasih telah menggunakan aplikasi ini. Pada halaman ini kamu akan Devina pandu untuk mengetahui cara penggunaan aplikasi ini.')
                st.markdown('Menu navigasi: Bagian menu dijutukan untuk memudahkan Anda dalam bernavigasi pada sistem ini. Pada bagian Menu navigasi, menu yang tersedia adalah Panduan, Tentang, Unggah, Kamera dan Dataset. Dibawah ini akan dijelaskan peruntukan dan cara penggunaan masing-masing menu.')
                st.markdown('1.	Panduan')
                st.markdown('Pada menu ini  berisi tentang panduan penggunaan sistem. Bagian ini ditujukan untuk memudahkan Anda dalam menggunakan sistem ini.')
                st.markdown('2.	Tentang')
                st.markdown('Pada menu ini berisi tentang ciri-ciri ikan segar menurut SNI, Bagian ini ditujukan untuk mengedukasi pengguna tentang bagaimana cara memilih ikan yang segar. Pada bagian tersebut dijelaskan ciri ikan segar menggunakan poin-poin yang mudah dimengerti.')
                st.markdown('3.	Unggah')
                st.markdown('Menu ini bertujuan untuk mendeteksi tingkat kesegaran ikan berdasarkan citra mata yang diunggah melalui File dengan format JPG.')
                st.markdown('Langkah-langkah penggunaan:')
                st.markdown('a.	Siapkan citra mata ikan yang akan dideteksi tingkat kesegarannya.')
                st.markdown('b.	Pada bagian pilih gambar, Klik pada button Browse files untuk menginputkan citra yang akan dideteksi.')
                st.markdown('c.	Setelah citra diinputkan, selanjutnya akan muncul bagian crop gambar. Pada bagian ini silahkan crop gambar mata ikan tepat pada bagian matanya, seperti yang ditunjukkan pada gambar dibawah ini, untuk melakukan crop silahkan klik dan seret pada bagian kotak berwarna biru untuk memilih bagian yang akan dicrop, untuk mengatur besar kecilnya kotak silahkan klik pada salah satu ujung garis biru.')
                path_crop_jpg = r"./Img/crop.jpg"
                st.image(path_crop_jpg)
                st.markdown('d.	Setelah crop dilakukan, cek gambar yang telah dicrop melalui bagian Preview yang tersedia untuk mempermudah Anda melihat bagian yang telah Anda crop.')
                path_preview_jpg = r"./Img/preview.jpg"
                col1, col2, col3 = st.columns(3) 
                with col1: st.write(' ') 
                with col2: st.image(path_preview_jpg, caption='Hasil Crop Bagian Mata Ikan') 
                with col3: st.write(' ')
                #st.image(path_preview_jpg)
                st.markdown('e.	Setelah semuanya sesuai, silahkan klik button Predisi untuk melakukan prediksi tingkat kesegaran ikan.')
                st.markdown('f.	Selanjutnya pada bagian hasil, hasil prediksi akan tampil berupa teks : Segar, Kurang Segar, Tidak Segar, dan Busuk. Pada bagian ini juga akan menampilkan tingkat presentase prediksi per kategori tingkat kesegaran ikan.')
                st.markdown('4.	Kamera')
                st.markdown('Menu ini bertujuan untuk mendeteksi tingkat kesegaran ikan berdasarkan citra mata yang diunggah melalui kamera dengan format JPG.')
                st.markdown('Langkah-langkah penggunaan:')
                st.markdown('a.	Silahkan klik allow penggunaan kamera untuk dapat menggunakan fitur pada halaman ini')
                st.markdown('b.	Pada bagian Take a picture, Klik pada button Take Photo untuk menginputkan citra yang akan dideteksi. Pada pengguna mobile silahkan klik tombol pada pojok kanan atas untuk mengganti ke kamera bagian belakang. Jika terjadi error (bug) pada proses allow, ambil gambar sembarang terlebih dahulu menggunakan kamera depan, kemudian tekan button delete, lalu silahkan klik button di pojok kanan atas.')
                st.markdown('c.	Setelah citra diinputkan, selanjutnya akan muncul bagian crop gambar. Pada bagian ini silahkan crop gambar mata ikan tepat pada bagian matanya, seperti yang ditunjukkan pada gambar dibawah ini. Untuk melakukan crop silahkan klik dan seret pada bagian kotak berwarna biru untuk memilih bagian yang akan dicrop, untuk mengatur besar kecilnya kotak silahkan klik pada salah satu ujung garis biru.')
                path_crop_jpg = r"./Img/crop.jpg"
                st.image(path_crop_jpg)
                st.markdown('d.	Setelah crop dilakukan, cek gambar yang telah dicrop melalui bagian Preview yang tersedia untuk mempermudah Anda melihat bagian yang telah Anda crop.')
                path_preview_jpg = r"./Img/preview.jpg"
                col1, col2, col3 = st.columns(3) 
                with col1: st.write(' ') 
                with col2: st.image(path_preview_jpg, caption='Hasil Crop Bagian Mata Ikan') 
                with col3: st.write(' ')
                #st.image(path_preview_jpg)
                st.markdown('e.	Setelah semuanya sesuai, silahkan klik button Predisi untuk melakukan prediksi tingkat kesegaran ikan.')
                st.markdown('f.	Selanjutnya pada bagian hasil, hasil prediksi akan tampil berupa teks : Segar, Kurang Segar, Tidak Segar, dan Busuk. Pada bagian ini juga akan menampilkan tingkat presentase prediksi per kategori tingkat kesegaran ikan.')
                st.markdown('5.	Informasi')
                st.markdown('Pada bagian ini ditampilkan grafik jumlah dataset yang digunakan dari masing-masing kategori, pada bagian ini juga akan menampilkan hasil training dari model yang telah dibuat.')
                st.markdown('6.	Dataset')
                st.markdown('Pada bagian ini Admin dapat melihat dan mengupload dataset yang digunakan untuk membuat model pada sistem ini. Silahkan klik button Unggah untuk memunculkan link yang akan mengalihkan Admin ke Drive yang berisi dataset.')

            elif choose == 'Unggah':
                st.set_option('deprecation.showfileUploaderEncoding', False)
                st.text('Unggah Gambar')

                model = pickle.load(open(path_model, 'rb'))

                uploaded_file = st.file_uploader("Pilih gambar...", type='jpg')
                if uploaded_file is not None:
                    img = Image.open(uploaded_file)
                    realtime_update = st.sidebar.checkbox(
                        label="Update in Real Time", value=True)
                    box_color = st.sidebar.color_picker(
                        label="Box Color", value='#0000FF')
                    aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=[
                        "1:1", "16:9", "4:3", "2:3", "Free"])
                    aspect_dict = {
                        "1:1": (1, 1),
                        "16:9": (16, 9),
                        "4:3": (4, 3),
                        "2:3": (2, 3),
                        "Free": None
                    }
                    aspect_ratio = aspect_dict[aspect_choice]

                if uploaded_file:
                    img = Image.open(uploaded_file)
                    if not realtime_update:
                        st.write("Double click to save crop")
                    # Get a cropped image from the frontend
                    st.write("Crop gambar")
                    cropped_img = st_cropper(
                        img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

                    # Manipulate cropped image at will
                    st.write("Preview")
                    _ = cropped_img.thumbnail((150, 150))
                    st.image(cropped_img)

                if st.button('PREDIKSI'):
                    CATEGORIES = ['segar', 'kurang segar',
                                  'tidak segar', 'busuk']
                    st.write('Hasil...')
                    flat_data = []
                    img = np.array(cropped_img)
                    img_resized= resize(img, (300,300,3))#tanpa feature extraction
                    # hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #feature extraction hsv
                    # img_resized = resize(hsvImage, (100, 100, 3))
                    flat_data.append(img_resized.flatten())
                    flat_data = np.array(flat_data)
                    y_out = model.predict(flat_data)
                    y_out = CATEGORIES[y_out[0]]
                    st.title(f' Prediksi: {y_out}')
                    q = model.predict_proba(flat_data)
                    for index, item in enumerate(CATEGORIES):
                        st.write(f'{item} : {q[0][index]*100}%')

            elif choose == 'Kamera':
                st.set_option('deprecation.showfileUploaderEncoding', False)
                model = pickle.load(open(path_model, 'rb'))

                picture = st.camera_input("Take a picture")
                if picture is not None:
                    img = Image.open(picture)
                    realtime_update = st.sidebar.checkbox(
                        label="Update in Real Time", value=True)
                    box_color = st.sidebar.color_picker(
                        label="Box Color", value='#0000FF')
                    aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=[
                        "1:1", "16:9", "4:3", "2:3", "Free"])
                    aspect_dict = {
                        "1:1": (1, 1),
                        "16:9": (16, 9),
                        "4:3": (4, 3),
                        "2:3": (2, 3),
                        "Free": None
                    }
                    aspect_ratio = aspect_dict[aspect_choice]

                if picture:
                    img = Image.open(picture)
                    if not realtime_update:
                        st.write("Double click to save crop")
                    # Get a cropped image from the frontend
                    st.write("Crop gambar")
                    cropped_img = st_cropper(
                        img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

                    # Manipulate cropped image at will
                    st.write("Preview")
                    _ = cropped_img.thumbnail((150, 150))
                    st.image(cropped_img)

                if st.button('PREDIKSI'):
                    CATEGORIES = ['segar', 'kurang segar',
                                  'tidak segar', 'busuk']
                    st.write('Hasil...')
                    flat_data = []
                    img = np.array(cropped_img)
                    img_resized = resize(img, (300, 300, 3))# tanpa feature extraction
                    # hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#feature extraction hsv
                    # img_resized = resize(hsvImage, (100, 100, 3))
                    flat_data.append(img_resized.flatten())
                    flat_data = np.array(flat_data)
                    y_out = model.predict(flat_data)
                    y_out = CATEGORIES[y_out[0]]
                    st.title(f' Prediksi: {y_out}')
                    q = model.predict_proba(flat_data)
                    for index, item in enumerate(CATEGORIES):
                        st.write(f'{item} : {q[0][index]*100}%')

            # WORKPLACE FEED PAGE
            elif choose == 'Tentang':
                st.markdown(
                    "<h1 style='text-align: center; color: black;'>Kenali Ciri Ikan Segar menurut SNI</h1>", unsafe_allow_html=True)
                imagefeed = Image.open(path_ikan_jpg)
                st.image(imagefeed, caption='Ciri Ikan Segar menurut SNI')
                st.markdown('Ikan merupakan salah satu sumber protein yang popular dan terbukti baik bagi kesehatan tubuh. Selain memiliki kandungan protein yang tinggi dan rendah lemak, beberapa kandungan nutrisi daging ikan yang bermanfaat bagi tubuh, diantaranya adalah omega 3 yang bermanfaat bagi pertumbuhan otak, kalsium dan fosfor untuk pembentukan tulang dan gigi, serta vitamin d yang membuat tulang, gigi dan otot selalu dalam kondisi prima. Dibalik kandungan nutrisinya yang begitu banyak, ikan ternyata juga salah satu bahan makanan yang sangat mudah mengalami kerusakan. Ikan yang telah rusak tentunya akan mengalami penurunan nilai nutrisi yang dikandungnya, dan bahkan dapat menjadi berbahaya bagi konsumen apabila ikan sudah mengalami pembusukan. Maka dari itu, kita perlu mengetahui dan dapat membedakan ikan seperti apa yang termasuk ke dalam kategori baik untuk dikonsumsi. Pemerintah Indonesia sendiri telah menentukan standar ciri ikan segar yang dituangkan dalam SNI  2729:2013 tentang Ikan segar yang dikeluarkan oleh Badan Standarisasi Nasional (BSN)')
                st.markdown('1. Mata')
                st.markdown('Ikan yang segar memiliki bola mata yang cembung, kornea dan pupil jernih, mengkilap, dan memiliki warna yang spesifik sesuai dengan jenis ikan masing – masing. Sementara ikan yang tidak segar memiliki ciri berupa bola mata yang sangat cekung, kornea sangat keruh, pupil abu-abu dan tidak mengkilap')
                st.markdown('2. Insang')
                st.markdown('Ikan segar memiliki warna insang merah tua atau coklat kemerahan, cemerlang dengan sedikit sekali lapisan lendir transparan. Sementara ikan yang tidak segar memiliki warna insang abu- abu, atau coklat keabuabuan dengan lendir coklat bergumpal')
                st.markdown('3. Lendir Permukaan Badan')
                st.markdown('Ikan segar memiliki lapisan lendir jernih, transparan, mengkilap cerah di seluruh badannya, sementara ikan yang tidak segar memiliki lapiran lendir tebal menggumpal, dan telah berubah warna')
                st.markdown('4. Daging')
                st.markdown('Ikan yang segar memiliki sayatan daging sangat cemerlang, spesifik jenis, jaringan daging sangat kuat. Sementara ikan yang tidak segar memiliki sayatan daging sangat kusam, jaringan daging Rusak')
                st.markdown('5. Bau')
                st.markdown('Ikan yang segar memiliki bau yang sangat segar yang spesifik sesuai dengan jenis ikan masing – masing. Sementara ikan yang tidak segar memiliki  bau busuk yang kuat.')
                st.markdown('6. Tekstur')

                st.markdown('Ikan segar memiliki tekstur daging sangat padat, kompak, dan sangat elastis ketika disentuh. Sementara ikan tidak segar memiliki tekstur daging yang sangat lunak, dan bekas jari tidak hilang apabila ikan disentuh.')
            elif choose == 'Dataset':
                st.write(
                    "Unggah Dataset disini")
                if st.button("Unggah"):
                    "[klik disini](https://drive.google.com/drive/folders/1smK_ecrefcRLapbbLEy_49egn5HCtE2M?usp=sharing)"

if choice == 'User':
    choose2 = option_menu("Menu", ["Panduan", "Tentang", "Unggah", "Kamera", "Dataset"],
                          icons=['house-door', 'info-circle', 'upload',
                                 'camera', 'file-arrow-up'],
                          menu_icon="app-indicator", default_index=0, orientation="horizontal",
                          styles={
        "container": {"padding": "5!important", "background-color": "#EFF2F9"},
        "icon": {"color": "orange", "font-size": "15px"},
        "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#008080"},
    }
    )


# Beranda PAGE
    if choose2 == 'Unggah':
        model = pickle.load(open(path_model, 'rb'))

        uploaded_file = st.file_uploader("Pilih gambar...", type='jpg')
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            realtime_update = st.sidebar.checkbox(
                label="Update in Real Time", value=True)
            box_color = st.sidebar.color_picker(
                label="Box Color", value='#0000FF')
            aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=[
                                             "1:1", "16:9", "4:3", "2:3", "Free"])
            aspect_dict = {
                "1:1": (1, 1),
                "16:9": (16, 9),
                "4:3": (4, 3),
                "2:3": (2, 3),
                "Free": None
            }
            aspect_ratio = aspect_dict[aspect_choice]

        if uploaded_file:
            img = Image.open(uploaded_file)
            if not realtime_update:
                st.write("Double click to save crop")
            # Get a cropped image from the frontend
            st.write("Crop gambar")
            cropped_img = st_cropper(
                img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

            # Manipulate cropped image at will
            st.write("Preview")
            _ = cropped_img.thumbnail((150, 150))
            st.image(cropped_img)
            # Hapus tanda # untuk menampilkan nilai RGB
            # img_rgb = cropped_img.convert("RGB")
            # # rgb_pixel_value = img_rgb.getpixel((10, 10))
            # # st.write(f' Nilai RGB: {rgb_pixel_value}')
            # pix = img_rgb.load()
            # # For loop to extract and print all pixels
            # st.write(f'Nilai RGB:')
            # for x in range(img_rgb.width):
            #     for y in range(img_rgb.width):
            #         # getting pixel value using getpixel() method
            #         bb = (img_rgb.getpixel((x, y)))
            #         st.write(f'{bb}')

        if st.button('PREDIKSI'):
            CATEGORIES = ['segar', 'kurang segar',
                          'tidak segar', 'busuk']
            st.write('Hasil...')
            flat_data = []
            img = np.array(cropped_img)
            img_resized = resize(img, (300, 300, 3))
            # hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#feature extraction hsv
            # img_resized = resize(hsvImage, (100, 100, 3))
            # Hapus tanda # untuk menampilkan nilai HSV
            # data = im.fromarray(hsvImage)
            # pix = data.load()
            # st.write(f'Nilai HSV:')
            # for x in range(data.width):
            #     for y in range(data.width):
            #         # getting pixel value using getpixel() method
            #         bb = (data.getpixel((x, y)))
            #         st.write(f'{bb}')

            flat_data.append(img_resized.flatten())
            flat_data = np.array(flat_data)
            y_out = model.predict(flat_data)
            y_out = CATEGORIES[y_out[0]]
            st.title(f' Prediksi: {y_out}')
            q = model.predict_proba(flat_data)
            for index, item in enumerate(CATEGORIES):
                st.write(f'{item} : {q[0][index]*100}%')

    elif choose2 == 'Kamera':
        st.set_option('deprecation.showfileUploaderEncoding', False)
        model = pickle.load(open(path_model, 'rb'))

        picture = st.camera_input("Take a picture")
        if picture is not None:
            img = Image.open(picture)
            realtime_update = st.sidebar.checkbox(
                label="Update in Real Time", value=True)
            box_color = st.sidebar.color_picker(
                label="Box Color", value='#0000FF')
            aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=[
                "1:1", "16:9", "4:3", "2:3", "Free"])
            aspect_dict = {
                "1:1": (1, 1),
                "16:9": (16, 9),
                "4:3": (4, 3),
                "2:3": (2, 3),
                "Free": None
            }
            aspect_ratio = aspect_dict[aspect_choice]

        if picture:
            img = Image.open(picture)
            if not realtime_update:
                st.write("Double click to save crop")
            # Get a cropped image from the frontend
            st.write("Crop gambar")
            cropped_img = st_cropper(
                img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

            # Manipulate cropped image at will
            st.write("Preview")
            _ = cropped_img.thumbnail((150, 150))
            st.image(cropped_img)

        if st.button('PREDIKSI'):
            CATEGORIES = ['segar', 'kurang segar',
                          'tidak segar', 'busuk']
            st.write('Hasil...')
            flat_data = []
            img = np.array(cropped_img)
            img_resized = resize(img, (300, 300, 3))
            # hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#feature extraction hsv
            # img_resized = resize(hsvImage, (100, 100, 3))
            flat_data.append(img_resized.flatten())
            flat_data = np.array(flat_data)
            y_out = model.predict(flat_data)
            y_out = CATEGORIES[y_out[0]]
            st.title(f' Prediksi: {y_out}')
            q = model.predict_proba(flat_data)
            for index, item in enumerate(CATEGORIES):
                st.write(f'{item} : {q[0][index]*100}%')

# WORKPLACE FEED PAGE
    elif choose2 == 'Tentang':
        st.markdown(
            "<h1 style='text-align: center; color: black;'>Kenali Ciri Ikan Segar menurut SNI</h1>", unsafe_allow_html=True)
        imagefeed = Image.open(path_ikan_jpg)
        st.image(imagefeed, caption='Ciri Ikan Segar menurut SNI')
        st.markdown('Ikan merupakan salah satu sumber protein yang popular dan terbukti baik bagi kesehatan tubuh. Selain memiliki kandungan protein yang tinggi dan rendah lemak, beberapa kandungan nutrisi daging ikan yang bermanfaat bagi tubuh, diantaranya adalah omega 3 yang bermanfaat bagi pertumbuhan otak, kalsium dan fosfor untuk pembentukan tulang dan gigi, serta vitamin d yang membuat tulang, gigi dan otot selalu dalam kondisi prima. Dibalik kandungan nutrisinya yang begitu banyak, ikan ternyata juga salah satu bahan makanan yang sangat mudah mengalami kerusakan. Ikan yang telah rusak tentunya akan mengalami penurunan nilai nutrisi yang dikandungnya, dan bahkan dapat menjadi berbahaya bagi konsumen apabila ikan sudah mengalami pembusukan. Maka dari itu, kita perlu mengetahui dan dapat membedakan ikan seperti apa yang termasuk ke dalam kategori baik untuk dikonsumsi. Pemerintah Indonesia sendiri telah menentukan standar ciri ikan segar yang dituangkan dalam SNI  2729:2013 tentang Ikan segar yang dikeluarkan oleh Badan Standarisasi Nasional (BSN)')
        st.markdown('1. Mata')
        st.markdown('Ikan yang segar memiliki bola mata yang cembung, kornea dan pupil jernih, mengkilap, dan memiliki warna yang spesifik sesuai dengan jenis ikan masing – masing. Sementara ikan yang tidak segar memiliki ciri berupa bola mata yang sangat cekung, kornea sangat keruh, pupil abu-abu dan tidak mengkilap')
        st.markdown('2. Insang')
        st.markdown('Ikan segar memiliki warna insang merah tua atau coklat kemerahan, cemerlang dengan sedikit sekali lapisan lendir transparan. Sementara ikan yang tidak segar memiliki warna insang abu- abu, atau coklat keabuabuan dengan lendir coklat bergumpal')
        st.markdown('3. Lendir Permukaan Badan')
        st.markdown('Ikan segar memiliki lapisan lendir jernih, transparan, mengkilap cerah di seluruh badannya, sementara ikan yang tidak segar memiliki lapiran lendir tebal menggumpal, dan telah berubah warna')
        st.markdown('4. Daging')
        st.markdown('Ikan yang segar memiliki sayatan daging sangat cemerlang, spesifik jenis, jaringan daging sangat kuat. Sementara ikan yang tidak segar memiliki sayatan daging sangat kusam, jaringan daging Rusak')
        st.markdown('5. Bau')
        st.markdown('Ikan yang segar memiliki bau yang sangat segar yang spesifik sesuai dengan jenis ikan masing – masing. Sementara ikan yang tidak segar memiliki  bau busuk yang kuat.')
        st.markdown('6. Tekstur')

        st.markdown('Ikan segar memiliki tekstur daging sangat padat, kompak, dan sangat elastis ketika disentuh. Sementara ikan tidak segar memiliki tekstur daging yang sangat lunak, dan bekas jari tidak hilang apabila ikan disentuh.')
    elif choose2 == 'Dataset':
        st.write(
            "Lihat Dataset disini")
        if st.button("Lihat"):
            "[klik disini](https://drive.google.com/drive/folders/1smK_ecrefcRLapbbLEy_49egn5HCtE2M?usp=sharing)"

    elif choose2 == 'Panduan':
        st.markdown(
            "<h1 style='text-align: center; color: black;'>Panduan Penggunaan Sistem</h1>", unsafe_allow_html=True)
        st.markdown('Halo! Terima kasih telah menggunakan aplikasi ini. Pada halaman ini kamu akan Devina pandu untuk mengetahui cara penggunaan aplikasi ini.')
        st.markdown('Menu navigasi: Bagian menu dijutukan untuk memudahkan Anda dalam bernavigasi pada sistem ini. Pada bagian Menu navigasi, menu yang tersedia adalah Panduan, Tentang, Unggah, Kamera dan Dataset. Dibawah ini akan dijelaskan peruntukan dan cara penggunaan masing-masing menu.')
        st.markdown('1.	Panduan')
        st.markdown('Pada menu ini  berisi tentang panduan penggunaan sistem. Bagian ini ditujukan untuk memudahkan Anda dalam menggunakan sistem ini.')
        st.markdown('2.	Tentang')
        st.markdown('Pada menu ini berisi tentang ciri-ciri ikan segar menurut SNI, Bagian ini ditujukan untuk mengedukasi pengguna tentang bagaimana cara memilih ikan yang segar. Pada bagian tersebut dijelaskan ciri ikan segar menggunakan poin-poin yang mudah dimengerti.')
        st.markdown('3.	Unggah')
        st.markdown('Menu ini bertujuan untuk mendeteksi tingkat kesegaran ikan berdasarkan citra mata yang diunggah melalui File dengan format JPG.')
        st.markdown('Langkah-langkah penggunaan:')
        st.markdown('a.	Siapkan citra mata ikan yang akan dideteksi tingkat kesegarannya.')
        st.markdown('b.	Pada bagian pilih gambar, Klik pada button Browse files untuk menginputkan citra yang akan dideteksi.')
        st.markdown('c.	Setelah citra diinputkan, selanjutnya akan muncul bagian crop gambar. Pada bagian ini silahkan crop gambar mata ikan tepat pada bagian matanya, seperti yang ditunjukkan pada gambar dibawah ini, untuk melakukan crop silahkan klik dan seret pada bagian kotak berwarna biru untuk memilih bagian yang akan dicrop, untuk mengatur besar kecilnya kotak silahkan klik pada salah satu ujung garis biru.')
        path_crop_jpg = r"./Img/crop.jpg"
        st.image(path_crop_jpg)
        st.markdown('d.	Setelah crop dilakukan, cek gambar yang telah dicrop melalui bagian Preview yang tersedia untuk mempermudah Anda melihat bagian yang telah Anda crop.')
        path_preview_jpg = r"./Img/preview.jpg"
        col1, col2, col3 = st.columns(3) 
        with col1: st.write(' ') 
        with col2: st.image(path_preview_jpg, caption='Hasil Crop Bagian Mata Ikan') 
        with col3: st.write(' ')
        #st.image(path_preview_jpg)
        st.markdown('e.	Setelah semuanya sesuai, silahkan klik button Predisi untuk melakukan prediksi tingkat kesegaran ikan.')
        st.markdown('f.	Selanjutnya pada bagian hasil, hasil prediksi akan tampil berupa teks : Segar, Kurang Segar, Tidak Segar, dan Busuk. Pada bagian ini juga akan menampilkan tingkat presentase prediksi per kategori tingkat kesegaran ikan.')
        st.markdown('4.	Kamera')
        st.markdown('Menu ini bertujuan untuk mendeteksi tingkat kesegaran ikan berdasarkan citra mata yang diunggah melalui kamera dengan format JPG.')
        st.markdown('Langkah-langkah penggunaan:')
        st.markdown('a.	Silahkan klik allow penggunaan kamera untuk dapat menggunakan fitur pada halaman ini')
        st.markdown('b.	Pada bagian Take a picture, Klik pada button Take Photo untuk menginputkan citra yang akan dideteksi. Pada pengguna mobile silahkan klik tombol pada pojok kanan atas untuk mengganti ke kamera bagian belakang. Jika terjadi error (bug) pada proses allow, ambil gambar sembarang terlebih dahulu menggunakan kamera depan, kemudian tekan button delete, lalu silahkan klik button di pojok kanan atas.')
        st.markdown('c.	Setelah citra diinputkan, selanjutnya akan muncul bagian crop gambar. Pada bagian ini silahkan crop gambar mata ikan tepat pada bagian matanya, seperti yang ditunjukkan pada gambar dibawah ini. Untuk melakukan crop silahkan klik dan seret pada bagian kotak berwarna biru untuk memilih bagian yang akan dicrop, untuk mengatur besar kecilnya kotak silahkan klik pada salah satu ujung garis biru.')
        path_crop_jpg = r"./Img/crop.jpg"
        st.image(path_crop_jpg)
        st.markdown('d.	Setelah crop dilakukan, cek gambar yang telah dicrop melalui bagian Preview yang tersedia untuk mempermudah Anda melihat bagian yang telah Anda crop.')
        path_preview_jpg = r"./Img/preview.jpg"
        col1, col2, col3 = st.columns(3) 
        with col1: st.write(' ') 
        with col2: st.image(path_preview_jpg, caption='Hasil Crop Bagian Mata Ikan') 
        with col3: st.write(' ')
        #st.image(path_preview_jpg)
        st.markdown('e.	Setelah semuanya sesuai, silahkan klik button Predisi untuk melakukan prediksi tingkat kesegaran ikan.')
        st.markdown('f.	Selanjutnya pada bagian hasil, hasil prediksi akan tampil berupa teks : Segar, Kurang Segar, Tidak Segar, dan Busuk. Pada bagian ini juga akan menampilkan tingkat presentase prediksi per kategori tingkat kesegaran ikan.')
        st.markdown('5.	Dataset')
        st.markdown('Pada bagian ini pengguna dapat melihat dataset yang digunakan untuk membuat model pada sistem ini. Silahkan klik button Lihat untuk memunculkan link yang akan mengalihkan Anda ke Drive yang berisi dataset.')

