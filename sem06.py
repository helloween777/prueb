import streamlit as st

#título de la aplicación
st.title("Ejercicios con bucles básicos en python")

#Ejercicio 1: Imprimir 10 veces 'Hola mundo'
st.subheader("Ejercicio 1: imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")
#Ejercicio 2: Imprimir los primeros 10 números
st.subheader("Ejercicio 2: Imprimir los primeros 10 números")
if st.button("Ejecutar Ejercicio 2"):
    for i in range(1, 11):
        st.write(i)
#Ejercicio 3: tabla de multiplicar
st.subheader("Ejercicio 3: Imprimir la tabla de multiplicar del número ingresado")
num = st.number_input("Ingrese un número para ver su tabla de multuplicar del 1 al 12", min value=1)
if st.button("Ejecutar Ejercicio 3"):
    for in range(1, 13):
        st.write(f"{num} x {i} = {num * i}")
