import streamlit as st

#Función principal para verificar automóviles
def verificar_automoviles():
    st.title("Centro de Verificación de Automóviles")

    #Lista para almacenar los puntos contaminantes
    if 'puntos_contaminantes' not in st.session_state:
        st.session_state.puntos_contaminantes = []

    #Input para los puntos contaminates del automóvil
    puntos = st.number_input("Ingrese los puntos contaminantes del automóvil", min_value=0.0, step=0.1)

    #Botón para registrar el automóvil
    if st.button("Registrar automóvil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.sucess(f"Automóvil registrado con {puntos} puntos contaminantes.")
    
    #Mostrar los datos registrados hasta el momento
    if len(st.session_state.puntos_contaminates) > 0 and sr.button("Calcular resultados"):
        promedio = sum(st.session_state.puntos_contaminates) / len(st.session_state.puntos_contaminantes)
        menos_contaminacion = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)

        #Mostrar los resultados
        st.write(f"Promedio de puntos contaminantes: {promedio:.2f}")
        st.write(f"El automóvil que menos contaminó tiene {menos_contaminación}")
        st.write(f"El automóvil que más contaminó tiene {mas_contaminacion}")

    #Opción para reiniciar los datos
    if st.button("Reiniciar datos"):
        st.session_state.puntos_contaminantes = []
        st.sucess("Datos reiniciados correctamente")

#Ejecutar la función
if __name__ == "__main__":
    verificar_automoviles()
