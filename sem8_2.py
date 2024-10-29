import streamlit as st

def calcular(iperación, num1, num2)
    """Realiza la operación especificada entre num1 y num2."""
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return

    if operacion == "Suma":
        return num1+num2
    elif operacion == "Resta":
        return num1-num2
    elif operacion == "Multiplicación":
        return num1*num2
    elif operacion == "División":
        if num2 == 0:
            return "Error: no se puede dividir entre 0"
        return num1/num2
    else:
        return "Operación no válida"

def main():
    st.title("Calculadora Básica")