# tp_paises.py
# Trabajo Práctico Integrador - Programación I
import os

CSV_ENCODING = 'utf-8'

# ---------- Helpers de validación ----------
def es_entero_valido(s: str) -> bool:
    """
    Comprueba si s representa un entero no negativo válido.
    Acepta espacios alrededor, pero no signos ni separadores.
    """
    if s is None:
        return False
    s = s.strip()
    if s == '':
        return False
    return s.isdigit()

def convertir_a_entero_seguro(s: str) -> int:
    """
    Convierte s a entero después de validar con es_entero_valido.
    """
    s = s.strip()
    return int(s)

# ---------- Lectura CSV ----------
def cargar_paises_desde_csv(ruta_csv: str):
    """
    Lee el CSV y devuelve (lista_paises, lista_errores).
    Cada país es dict: {"nombre","poblacion","superficie","continente"}.
    Registros mal formados se ignoran y se agregan a lista_errores.
    """
    paises = []
    errores = []

    if not os.path.isfile(ruta_csv):
        errores.append(f"Archivo no encontrado: {ruta_csv}")
        return paises, errores

    with open(ruta_csv, 'r', encoding=CSV_ENCODING) as f:
        lineas = f.read().splitlines()

    if len(lineas) == 0:
        errores.append("Archivo CSV vacío.")
        return paises, errores

    # primera línea cabecera
    cabecera = lineas[0].strip().lower().split(',')

    # Validar manualmente que la cabecera tenga todos los campos esperados
    campos_requeridos = ['nombre', 'poblacion', 'superficie', 'continente']
    faltantes = [campo for campo in campos_requeridos if campo not in cabecera]

    if len(faltantes) > 0:
        errores.append(f"Cabecera CSV inválida. Faltan los siguientes campos: {', '.join(faltantes)}")
        return paises, errores

    # Si todos están, obtener los índices correspondientes
    idx_nombre = cabecera.index('nombre')
    idx_poblacion = cabecera.index('poblacion')
    idx_superficie = cabecera.index('superficie')
    idx_continente = cabecera.index('continente')

    for n_linea, linea in enumerate(lineas[1:], start=2):
        if linea.strip() == '':
            continue
        #salta la cabecera y empieza desde la segunda línea.
        
        partes = linea.split(',')
        if len(partes) < 4:
            errores.append(f"Línea {n_linea}: formato inválido (menos de 4 columnas).")
            continue

        nombre = partes[idx_nombre].strip()
        poblacion_s = partes[idx_poblacion].strip()
        superficie_s = partes[idx_superficie].strip()
        continente = partes[idx_continente].strip()

        if nombre == '':
            errores.append(f"Línea {n_linea}: nombre vacío.")
            continue
        if not es_entero_valido(poblacion_s):
            errores.append(f"Línea {n_linea}: población inválida -> '{poblacion_s}'.")
            continue
        if not es_entero_valido(superficie_s):
            errores.append(f"Línea {n_linea}: superficie inválida -> '{superficie_s}'.")
            continue
        if continente == '':
            errores.append(f"Línea {n_linea}: continente vacío.")
            continue

        poblacion = convertir_a_entero_seguro(poblacion_s)
        superficie = convertir_a_entero_seguro(superficie_s)

        pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(pais)

    return paises, errores

# ---------- Búsquedas y filtros ----------
def buscar_por_nombre(paises, consulta):
    q = consulta.strip().lower()
    if q == '':
        return []
    return [p for p in paises if q in p['nombre'].lower()]

def filtrar_por_continente(paises, continente):
    c = continente.strip().lower()
    if c == '':
        return []
    return [p for p in paises if p['continente'].lower() == c]

def filtrar_por_rango_poblacion(paises, min_pob, max_pob):
    if min_pob is None:
        min_pob = 0
    if max_pob is None:
        max_pob = 10**18
    if min_pob > max_pob:
        return []
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def filtrar_por_rango_superficie(paises, min_sup, max_sup):
    if min_sup is None:
        min_sup = 0
    if max_sup is None:
        max_sup = 10**18
    if min_sup > max_sup:
        return []
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]

# ---------- Ordenamientos ----------
def ordenar_paises(paises, clave, descendente=False):
    if clave not in {'nombre', 'poblacion', 'superficie'}:
        return list(paises)
    if clave == 'nombre':
        return sorted(paises, key=lambda x: x['nombre'].lower(), reverse=descendente)
    else:
        return sorted(paises, key=lambda x: x[clave], reverse=descendente)

# ---------- Estadísticas ----------
def pais_mayor_menor_poblacion(paises):
    if not paises:
        return None, None
    mayor = max(paises, key=lambda x: x['poblacion'])
    menor = min(paises, key=lambda x: x['poblacion'])
    return mayor, menor

def promedio_poblacion(paises):
    if not paises:
        return 0
    total = sum(p['poblacion'] for p in paises)
    return total // len(paises)

def promedio_superficie(paises):
    if not paises:
        return 0
    total = sum(p['superficie'] for p in paises)
    return total / len(paises)

def cantidad_por_continente(paises):
    conteo = {}
    for p in paises:
        cont = p['continente']
        conteo[cont] = conteo.get(cont, 0) + 1
    return conteo

# ---------- Mostrar resultados ----------
def mostrar_paises(paises):
    if not paises:
        print("No se encontraron países.")
        return
    for p in paises:
        print(f"{p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")

# ---------- Menú interactivo ----------
def menu_principal(paises):
    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar país por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por rango de población")
        print("4. Filtrar por rango de superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Mostrar todos")
        print("0. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == '1':
            q = input("Texto a buscar: ")
            mostrar_paises(buscar_por_nombre(paises, q))

        elif opcion == '2':
            cont = input("Nombre del continente: ")
            mostrar_paises(filtrar_por_continente(paises, cont))

        elif opcion == '3':
            min_pob = input("Población mínima (enter para 0): ").strip()
            max_pob = input("Población máxima (enter para sin tope): ").strip()

            if min_pob == '':
                min_pob = 0
            else:
                min_pob = int(min_pob)

            if max_pob == '':
                max_pob = 9999999999  # valor muy grande para “sin tope”
            else:
                max_pob = int(max_pob)

            paises_filtrados = filtrar_por_rango_poblacion(paises, min_pob, max_pob)

            if len(paises_filtrados) == 0:
                print("No se encontraron países en ese rango.")
            else:
                for p in paises_filtrados:
                    print(f"{p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")


        elif opcion == '4':
            min_s = input("Superficie mínima (enter para 0): ").strip()
            max_s = input("Superficie máxima (enter para sin tope): ").strip()
            min_sup = None
            max_sup = None
            if min_s != '':
                if es_entero_valido(min_s):
                    min_sup = convertir_a_entero_seguro(min_s)
                else:
                    print("Superficie mínima inválida.")
                    continue
            if max_s != '':
                if es_entero_valido(max_s):
                    max_sup = convertir_a_entero_seguro(max_s)
                else:
                    print("Superficie máxima inválida.")
                    continue
            mostrar_paises(filtrar_por_rango_superficie(paises, min_sup, max_sup))

        elif opcion == '5':
            print("Ordenar por: 1) nombre 2) poblacion 3) superficie")
            o = input("Elija (1/2/3): ").strip()
            sentido = input("Ascendente (a) o descendente (d)? [a/d]: ").strip().lower()
            descendente = sentido == 'd'
            if o == '1':
                clave = 'nombre'
            elif o == '2':
                clave = 'poblacion'
            elif o == '3':
                clave = 'superficie'
            else:
                print("Opción inválida.")
                continue
            mostrar_paises(ordenar_paises(paises, clave, descendente))

        elif opcion == '6':
            mayor, menor = pais_mayor_menor_poblacion(paises)
            if mayor is None:
                print("No hay datos para estadísticas.")
            else:
                print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
                print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
                print(f"Promedio de población: {promedio_poblacion(paises)}")
                print(f"Promedio de superficie: {promedio_superficie(paises):.2f}")
                print("Cantidad de países por continente:")
                for cont, cnt in cantidad_por_continente(paises).items():
                    print(f"  {cont}: {cnt}")

        elif opcion == '7':
            mostrar_paises(paises)

        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no reconocida. Intente de nuevo.")

# ---------- Programa principal ----------
if __name__ == '__main__':
    ruta = input("Ingrese la ruta del archivo CSV (ej: paises.csv): ").strip()
    paises, errores = cargar_paises_desde_csv(ruta)
    if errores:
        print("Se encontraron los siguientes errores al cargar el CSV:")
        for e in errores:
            print(" -", e)
    print(f"Se cargaron {len(paises)} países válidos.")
    menu_principal(paises)
