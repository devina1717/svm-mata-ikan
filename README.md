# SupportVectorMachine Object Classification

Support Vector Machine             |  Streamlit
:-------------------------:|:-------------------------:
![SVM](https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_440,h_305/https://databasecamp.de/wp-content/uploads/svm-1024x709.png)  |  ![Streamlit](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/z3ahdkytzwi1jxlpazje)

## Demo
[![Demo](https://www.herokucdn.com/deploy/button.svg)](https://svmmataikan.herokuapp.com/)

## Library
- numpy
- pandas
- Pillow
- scikit_image
- streamlit
- streamlit_authenticator
- streamlit_cropper
- streamlit_option_menu
- scikit-learn

## Code

### Database
```python
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

```

### Auth
```python
choice = st.sidebar.selectbox('Login', ['Admin', 'User'])
```

### Predict Button
```python
                if st.button('PREDIKSI'):
                    CATEGORIES = ['busuk', 'kurang segar',
                                  'segar', 'tidak segar']
                    st.write('Hasil...')
                    flat_data = []
                    img = np.array(cropped_img)
                    img_resized = resize(img, (100, 100, 3))
                    flat_data.append(img_resized.flatten())
                    flat_data = np.array(flat_data)
                    y_out = model.predict(flat_data)
                    y_out = CATEGORIES[y_out[0]]
                    st.title(f' Prediksi: {y_out}')
                    q = model.predict_proba(flat_data)
                    for index, item in enumerate(CATEGORIES):
                        st.write(f'{item} : {q[0][index]*100}%')
```
