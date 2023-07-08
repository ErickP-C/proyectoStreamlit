import streamlit as st
import pandas as pd

# Crear una lista vacía para almacenar los datos de los clientes
lista_clientes = []

st.title('Formulario de Registro de Clientes')
# Mostrar la imagen
url_imagen = 'https://img.freepik.com/vector-premium/actualizar-documentos-reclamo-registro-informacion-personal-informe-declaracion-impuestos-informacion-ingresos_566886-2161.jpg?w=1380'
st.image(url_imagen, use_column_width=True)

# Obtener los datos del cliente
nombre = st.text_input('Nombre')
edad = st.number_input('Edad', min_value=0, max_value=150, step=1)
email = st.text_input('Email')
telefono = st.text_input('Teléfono')

# Botón para enviar el formulario
if st.button('Registrar Cliente'):
    # Crear un diccionario con los datos del cliente
    nuevo_cliente = {'Nombre': nombre, 'Edad': edad, 'Email': email, 'Teléfono': telefono}
    # Agregar el cliente a la lista
    lista_clientes.append(nuevo_cliente)
    st.success('Cliente registrado exitosamente.')

# Botón para eliminar un registro
if st.button('Eliminar Registro'):
    if lista_clientes:
        # Mostrar los nombres de los clientes registrados para seleccionar cuál eliminar
        nombres_clientes = [cliente['Nombre'] for cliente in lista_clientes]
        cliente_a_eliminar = st.selectbox('Seleccione el cliente a eliminar', nombres_clientes)

        # Eliminar el cliente seleccionado de la lista de clientes
        lista_clientes = [cliente for cliente in lista_clientes if cliente['Nombre'] != cliente_a_eliminar]
        st.success('Cliente eliminado exitosamente.')

# Convertir la lista de clientes en un dataframe
df_clientes = pd.DataFrame(lista_clientes)

# Mostrar la tabla con los clientes registrados
st.header('Clientes Registrados')
st.dataframe(df_clientes)
