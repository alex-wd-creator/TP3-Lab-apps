# --- PROGRAMA: ASISTENTE DE MISIÓN ESPACIAL (TP3 - COLECCIONES) ---
def mostrar_menu():
    """Muestra las opciones del sistema de control."""
    print("\n--- SISTEMA DE PLAYLIST ---")
    print("1. Agregar canciones a la playlist (Listas)")
    print("2. [Pendiente] Calcular promedio de calificaciones")
    print("3. [Pendiente] Inventario de productos")
    print("4. Coordenadas y Desempaquetado (Tuplas)")
    print("5. Salir")

def ejecutar_asistente():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            # --- RESOLUCIÓN OPCIÓN 1: PLAYLIST DINÁMICA ---
            print(f"\n🎵 Generando lista de reproducción...")
            # 1. Creamos una lista vacía para almacenar las canciones
            playlist_mision = []
            # 2. Solicitamos al usuario la cantidad de elementos de forma dinámica
            try:
                cantidad = int(input("¿Cuántas canciones deseas agregar a la lista?: "))
                # 3. Usamos un ciclo for y la función range para la carga de datos
                for i in range(cantidad):
                    # Solicitamos el nombre de la canción.
                    # Sumamos 1 al índice solo para que sea informativo al usuario
                    cancion = input(f"Proporciona la canción {i + 1}: ")
                    # 4. Agregamos la canción a nuestra lista usando el método append
                    playlist_mision.append(cancion)

                # 5. Ordenamos la lista alfabéticamente antes de mostrarla
                playlist_mision.sort()

                # 6. Iteramos la lista final para mostrarla en consola
                print("\n📋 Lista de reproducción final (Orden Alfabético):")
                for cancion in playlist_mision:
                    print(f" - {cancion}")
            except ValueError:
                print("⚠️ Error: Por favor, ingresa un número entero válido para la cantidad.")
        elif opcion == "2":
            total_calificaciones = int(input("proporciona el numero de calificaciones a evaluar: "))
            calificaciones = []

            # iteramos las calificaciones
            for indice in range(total_calificaciones):
                calificacion = int(input(f"calificacion[{indice}] = "))
                calificaciones.append(calificacion) # Agregamos la calificacion a la lista

            # imprimimos las calificaciones proporcionadas
            print(f"\n las calificaciones proporcionadas son: {calificaciones}")

            # calculamos el promedio de las calificaciones
            suma_calificaciones = sum(calificaciones)
            promedio = suma_calificaciones/ total_calificaciones
            print(f"\n Promedio de las calificaciones: {promedio}")

        elif opcion == "3":
            print("*** Comvinacion listas y tuplas ***")
            # Definir una lista que almacena tuplas de producto
            productos = [
                ("p001", "camiseta", 20.00),
                ("p002", "jeans", 30.00),
                ("p003", "sudadera", 40.00)
            ]

            # imprimimos la informacion de cada producto
            # y calculamos el precio total
            precio_total = 0

            print(f"informacion de los productos: ")
            for producto in productos:
                #print(producto)
                id, descripcion, precio = producto # unpacking
                print(f"Producto: id = {id}, descripcion = {descripcion}, precio= {precio}")
                precio_total += precio # producto[2] para obtener el precio

            print(f"precio total de los productos: {precio_total}")

        elif opcion == "4":
            coordenadas = (3, 5)

            # acceder a los elementos de la tupla
            print(f"coordenada x: {coordenadas[0]}")
            print(f"coordenada y: {coordenadas[1]}")

        elif opcion == "5":
            print(f"️ Cerrando conexión. ¡Hasta luego!")
            continuar = False

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_asistente()
