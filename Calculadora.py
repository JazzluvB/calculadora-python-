import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(320, 420)
        self.setStyleSheet("background-color: #2C2C2E;")  # Fondo Gris Oxford

        # Layout
        layout = QGridLayout()
        self.setLayout(layout)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("SF Pro Display", 28))
        self.display.setStyleSheet("""
            background-color: #2C2C2E;
            color: white;
            border-radius: 15px;
            padding: 10px;
        """)
        layout.addWidget(self.display, 0, 0, 1, 4)

        # Botones
        botones = [
            ("AC", 1, 0, "#2C2C2E"), ("⌫", 1, 1, "#2C2C2E"), ("%", 1, 2, "#2C2C2E"), ("/", 1, 3, "#FF9F0A"),
            ("7", 2, 0, "#2C2C2E"), ("8", 2, 1, "#2C2C2E"), ("9", 2, 2, "#2C2C2E"), ("*", 2, 3, "#FF9F0A"),
            ("4", 3, 0, "#2C2C2E"), ("5", 3, 1, "#2C2C2E"), ("6", 3, 2, "#2C2C2E"), ("-", 3, 3, "#FF9F0A"),
            ("1", 4, 0, "#2C2C2E"), ("2", 4, 1, "#2C2C2E"), ("3", 4, 2, "#2C2C2E"), ("+", 4, 3, "#FF9F0A"),
            ("0", 5, 0, "#2C2C2E"), (".", 5, 1, "#2C2C2E"), ("=", 5, 2, "#FF9F0A"),
        ]

        for (texto, fila, columna, color) in botones:
            boton = QPushButton(texto)
            boton.setFont(QFont("SF Pro Display", 18, QFont.Bold))
            boton.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border-radius: 20px;
                    padding: 15px;
                    border: 2px solid #3A3A3E;
                }}
                QPushButton:pressed {{
                    background-color: #3C3C3E;
                }}
            """)
            boton.clicked.connect(lambda _, t=texto: self.on_click(t))
            if texto == "=":
                layout.addWidget(boton, fila, columna, 1, 2)
            else:
                layout.addWidget(boton, fila, columna)

    def on_click(self, texto):
        if texto == "=":
            try:
                resultado = str(eval(self.display.text()))
                self.display.setText(resultado)
            except:
                self.display.setText("Error")
        elif texto == "AC":
            self.display.clear()
        elif texto == "⌫":
            self.display.setText(self.display.text()[:-1])
        elif texto == "%":
            try:
                valor = float(self.display.text()) / 100
                self.display.setText(str(valor))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + texto)


# 🔹 Estructura de arranque
if __name__ == "__main__":
    app = QApplication(sys.argv)
    formulario = Formulario()
    formulario.show()
    sys.exit(app.exec())