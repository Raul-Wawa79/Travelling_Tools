from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
from PyQt6.QtCore import Qt
import requests

#Actual web page scrapped with Beautiful Soup. The function calculates the rate between 2 currencies and
# scraps the result
def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])

    #print(rate)
    return rate

#Function that uses the rate of previous function to create an output for our widget
def show_currency():
    input_text = float(text.text())
    in_curr = in_combo.currentText()
    to_curr = to_combo.currentText()
    rate = get_currency(in_curr, to_curr)
    output = input_text * rate
    message = f'{input_text} {in_curr} son {output} {to_curr}'
    output_label.setText(str(message))

#Instantiation of the app itself
app= QApplication([])
window = QWidget()
window.setWindowTitle('Conversor Moneda')

#Defining Main Layout and Layout 1
layout = QVBoxLayout()  #Main Layout, it is Vertical
layout1 = QHBoxLayout()
layout.addLayout(layout1)
#Adding Label
output_label = QLabel('')
layout.addWidget(output_label)
#Defining Layouts 2 & 3
layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)
#Input currency
in_combo = QComboBox()
currencies = ['USD', 'EUR', 'NPR']
in_combo.addItems(currencies)
layout2.addWidget(in_combo) #Adds the input currency combo widget

#Output currency
to_combo = QComboBox()
to_combo.addItems(currencies)
layout2.addWidget(to_combo) #Adds the input currency combo widget

#Adding text
text = QLineEdit()
layout3.addWidget(text)

#Adding a button
btn = QPushButton('Convertir')
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()
