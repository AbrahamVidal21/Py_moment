import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QScrollArea, QGroupBox, QGridLayout, QMessageBox


class FluidoInput(QWidget):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText(f"Fluido{self.index + 1}")

        self.densidad = QLineEdit()
        self.densidad.setPlaceholderText("1000")

        self.altura = QLineEdit()
        self.altura.setPlaceholderText("2")

        layout.addRow(f"Nombre del fluido {self.index + 1}:", self.nombre)
        layout.addRow(f"Densidad (kg/m³):", self.densidad)
        layout.addRow(f"Altura (m):", self.altura)

        self.setLayout(layout)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simulación de Fluidos en Tanque')
        layout = QVBoxLayout()

        # Formulario para entrada de datos generales
        form_layout = QFormLayout()

        self.patm_entry = QLineEdit()
        self.patm_entry.setPlaceholderText("101325")
        form_layout.addRow("Presión atmosférica (Pascales):", self.patm_entry)

        self.g_entry = QLineEdit()
        self.g_entry.setPlaceholderText("9.81")
        form_layout.addRow("Gravedad (m/s^2):", self.g_entry)

        self.ancho_tanque_entry = QLineEdit()
        self.ancho_tanque_entry.setPlaceholderText("5")
        form_layout.addRow("Ancho del tanque (metros):",
                           self.ancho_tanque_entry)

        self.n_fluids_entry = QLineEdit()
        self.n_fluids_entry.setPlaceholderText("3")
        form_layout.addRow("Número de fluidos:", self.n_fluids_entry)

        self.calculate_btn = QPushButton('Calcular Resultados')
        self.calculate_btn.clicked.connect(self.calcular_resultados)

        layout.addLayout(form_layout)
        self.fluido_groupbox = QGroupBox("Entradas de Fluidos")
        self.fluido_layout = QGridLayout()
        self.fluido_groupbox.setLayout(self.fluido_layout)

        layout.addWidget(self.fluido_groupbox)
        layout.addWidget(self.calculate_btn)

        self.setLayout(layout)
        self.actualizar_entradas()

        self.n_fluids_entry.textChanged.connect(self.actualizar_entradas)

    def actualizar_entradas(self):
        n_fluids = int(self.obtener_valor(
            self.n_fluids_entry, 3))  # Convertir a int
        while self.fluido_layout.count():
            child = self.fluido_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.fluido_inputs = [FluidoInput(i) for i in range(n_fluids)]
        for i, fluido_input in enumerate(self.fluido_inputs):
            self.fluido_layout.addWidget(fluido_input, i, 0, 1, 2)

    def obtener_valor(self, entry, valor_predeterminado):
        try:
            valor = entry.text()
            return float(valor) if valor else valor_predeterminado
        except ValueError:
            return valor_predeterminado

    def calcular_resultados(self):
        try:
            Patm = self.obtener_valor(self.patm_entry, 101325)
            g = self.obtener_valor(self.g_entry, 9.81)
            ancho_tanque = self.obtener_valor(self.ancho_tanque_entry, 5)
            n_fluids = int(self.obtener_valor(
                self.n_fluids_entry, 3))  # Convertir a int

            fluidos = []
            for i in range(n_fluids):
                nombre = self.fluido_inputs[i].nombre.text() or f"Fluido{
                    i + 1}"
                densidad = self.obtener_valor(
                    self.fluido_inputs[i].densidad, 1000)
                altura = self.obtener_valor(self.fluido_inputs[i].altura, 2)
                fluidos.append(
                    {"nombre": nombre, "densidad": densidad, "altura": altura})

            presion_absoluta_total = Patm
            fuerza_total = 0
            momento_total = 0
            altura_acumulada = 0

            resultados_texto = ""

            for fluido in fluidos:
                densidad = fluido["densidad"]
                altura = fluido["altura"]
                nombre = fluido["nombre"]

                presion_fluido = densidad * g * altura
                presion_absoluta_total += presion_fluido

                area_fluido = altura * ancho_tanque
                presion_media_fluido = presion_fluido / 2
                fuerza_fluido = presion_media_fluido * area_fluido

                fuerza_total += fuerza_fluido

                altura_centro_presion_fluido = (
                    2 / 3) * altura + altura_acumulada
                momento_fluido = altura_centro_presion_fluido * fuerza_fluido
                momento_total += momento_fluido

                altura_acumulada += altura

                resultados_texto += (f'\nPresión absoluta {nombre}: {presion_fluido:.2f} Pascales\n'
                                     f'Fuerza ejercida por el {nombre}: {
                                         fuerza_fluido:.2f} N\n'
                                     f'Momento debido al {nombre}: {momento_fluido:.2f} N*m\n')

            altura_centro_presion_total = momento_total / fuerza_total
            resultados_texto += (f'\nPresión absoluta total en el fondo del tanque: {presion_absoluta_total:.2f} Pascales\n'
                                 f'Fuerza total en la cara frontal del tanque: {
                                     fuerza_total:.2f} N\n'
                                 f'La altura del centro de presión desde la base del tanque es: {altura_centro_presion_total:.2f} metros')

            QMessageBox.information(self, "Resultados", resultados_texto)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
