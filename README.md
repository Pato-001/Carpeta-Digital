# 📘 README.md — Trabajo Práctico Integrador: Gestión de Países

## 🧾 Descripción general
Este proyecto fue desarrollado como **Trabajo Práctico Integrador** para la materia **Programación I**.  
El objetivo es crear un programa en Python que lea datos de países desde un archivo CSV y permita:
- Buscar países por nombre  
- Filtrar por continente  
- Filtrar por población o superficie  
- Ordenar resultados  
- Calcular estadísticas generales


---

## 🗂️ Archivos incluidos
- **`tp_paises.py`** → código principal del programa.  
- **`paises.csv`** → archivo de datos con 15 países (nombre, población, superficie y continente).  
- **`README.md`** → este documento (instrucciones y descripción).

---

## ⚙️ Requisitos
- **Python 3.10 o superior** (funciona perfectamente en Python 3.13).  
- Ejecutar desde **VS Code** o desde **CMD**.  

---

## ▶️ Cómo ejecutar el programa desde VS Code

1. Abrí **VS Code** y cargá la carpeta del proyecto:  
   `C:\Users\DecibelesComputacion\Desktop\Integrador Programacion I`

2. Abrí el archivo `tp_paises.py`.

3. Presioná **F5** o hacé clic en ▶️ (Run) arriba para ejecutar el programa.

4. Cuando el programa te pida la ruta del CSV, escribí:
   ```
   C:\Users\DecibelesComputacion\Desktop\Integrador Programacion I\paises.csv
   ```

5. Si el archivo es correcto, vas a ver el mensaje:
   ```
   Se cargaron 15 países válidos.
   ```
   y aparecerá el menú principal con todas las opciones.

---

## 🧮 Opciones del menú
| Opción | Descripción |
|--------|--------------|
| **1** | Buscar país por nombre (coincidencia parcial) |
| **2** | Filtrar por continente |
| **3** | Filtrar por rango de población |
| **4** | Filtrar por rango de superficie |
| **5** | Ordenar países por nombre, población o superficie |
| **6** | Mostrar estadísticas generales |
| **7** | Mostrar todos los países |
| **0** | Salir del programa |

---

## 📊 Ejemplo de salida
```
País con mayor población: China (1411750000)
País con menor población: Uruguay (3423100)
Promedio de población: 251839225
Promedio de superficie: 621934.40
Cantidad de países por continente:
  América: 7
  Europa: 4
  Asia: 3
  Oceania: 1
```

---

## 🧩 Estructura interna del código
El código se divide en secciones bien organizadas:
1. **Helpers de validación** → controlan que los datos sean correctos.  
2. **Lectura de CSV** → valida cabecera y carga los países en una lista de diccionarios.  
3. **Búsquedas y filtros** → funciones para encontrar países según distintos criterios.  
4. **Ordenamientos** → usa `sorted()` con distintas claves.  
5. **Estadísticas** → cálculos de promedio, mayor, menor, etc.  
6. **Menú principal** → interfaz de texto para el usuario.  

---

## ⚠️ Posibles errores comunes
- **Archivo no encontrado:** revisar que la ruta escrita sea correcta y que el archivo tenga extensión `.csv`.  
- **Campos mal formados:** si hay líneas con datos faltantes o inválidos, el programa las ignora y las muestra en una lista de errores.

---

## 💡 Mejoras futuras
- Permitir exportar los resultados filtrados a un nuevo CSV.  
- Aceptar separadores de miles (1.000.000).   

---

## ✍️ Autores
**Nombres:** Patricio Gonzalez - Ramiro Gonzalez
**Materia:** Programación I   
**Entorno de desarrollo:** VS Code en Windows

---

## ✅ Estado final del proyecto
✔ Código funcional  
✔ Validaciones completas   
✔ Probado con CSV de ejemplo (15 países)  
✔ Informe y README entregados  

---

## 📅 Fecha de entrega
13/11/2025
