import streamlit as st
import pandas as pd

# Crear un dataframe vacío para almacenar los datos de los clientes
df_clientes = pd.DataFrame(columns=['Nombre', 'Edad', 'Email', 'Teléfono'])

st.title('Formulario de Registro de Clientes')

# Obtener los datos del cliente
nombre = st.text_input('Nombre')
edad = st.number_input('Edad', min_value=0, max_value=150, step=1)
email = st.text_input('Email')
telefono = st.text_input('Teléfono')

# Botón para enviar el formulario
if st.button('Registrar Cliente'):
    # Crear un diccionario con los datos del cliente
    nuevo_cliente = {'Nombre': nombre, 'Edad': edad, 'Email': email, 'Teléfono': telefono}
    # Agregar el cliente al dataframe
    df_clientes = df_clientes.append(nuevo_cliente, ignore_index=True)
    st.success('Cliente registrado exitosamente.')

# Mostrar la tabla con los clientes registrados
st.header('Clientes Registrados')
st.dataframe(df_clientes)
