import streamlit as st

def main():
    st.title("Curso de streamlit")
    #Selectbox
    opcion = st.selectbox(
        'Elige tu fruta favorita',
        ['Manzana','Naranja','Platano','Fresa']
    )
    st.write(f'Tu fruta favorota es: {opcion}')

    #Multiselect
    opciones = st.multiselect(
        'Elige tus colores favoritos',
        ['rojo','verde','azul','amarillo']
    )
    st.write('Tu color favorito es', opciones)

    #Slider

    edad=st.slider(
        'Selecciona tu edad',
        min_value=0,
        max_value=100,
        value=25,
        step=1
    )
    st.write('tu edad es:', edad)

    #Select Slider
    nivel=st.select_slider(
        'Selecciona tu nivel de satisfaccion',
        options=['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
        value='Medio'
    )
    st.write('tu nivel de satisfaccion es:', nivel)

    st.image("https://picsum.photos/800")

    nombre = st.text_input("Ingresa tu nombre")
    st.write(nombre)

    mensaje = st.text_area("Ingresa tu mensaje", height=100)
    st.write(mensaje)

    numero = st.number_input("Ingresa un numero", 1, 25, step=1)
    st.write(numero)

    cita = st.date_input("selecciona una fecha")
    st.write(cita)

    hora = st.time_input("selecciona una hora")
    st.write(hora)

    color = st.color_picker("selecciona un color")
    st.write(color)

if __name__ == '__main__':
    main()