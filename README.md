# Calculadora en Python 🧮

**Proyecto personal ejecutable desde VS Code**  
Calculadora desarrollada en Python 3.10.11 con PyQt5. Proyecto diseñado para practicar programación y desarrollo de interfaces gráficas, aplicando lo aprendido en clase y cursos, con soporte de AI para optimización de código y experiencia de aprendizaje.

---

## Características

- Operaciones básicas: suma, resta, multiplicación y división.
- Funciones adicionales:  
  - AC → limpiar pantalla  
  - ⌫ → borrar último carácter  
  - % → cálculo de porcentaje  
- Interfaz personalizable y moderna con colores, tipografías y efectos de botón (hover y pressed).  
- Layout organizado con `QGridLayout` para botones y display.  
- Proyecto **ejecutable desde VS Code**, sin necesidad de instalar aplicación independiente.

---

## Tecnologías y librerías usadas

- **Python 3.10.11** – lenguaje de programación principal.  
- **PyQt5** – framework para desarrollo de interfaces gráficas.  
  - `QApplication`, `QWidget`, `QGridLayout`, `QPushButton`, `QLineEdit`  
  - `Qt` (alineación de texto)  
  - `QFont` (tipografías personalizadas)  
- **sys** – para controlar la ejecución de la aplicación.  
- **Visual Studio Code** – entorno de desarrollo utilizado.  
- AI (opcional) – como apoyo para optimización y aprendizaje, no para reemplazar el trabajo personal.

---

## Cómo ejecutar

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/calculadora-python.git

2. Accede a la carpeta del proyecto
cd calculadora-python

3. Instala PyQt5 si no lo tienes
pip install pyqt5

4. Ejecuta la calculadora desde VS Code o terminal
python calculadora.py

