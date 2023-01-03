from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
from PyQt6.QtCore import Qt
import requests

#Actual function to scrap the weather data from a web page using an API key
def get_weather(city, units= 'metric', api_key= '822a0e14a3c380f8c63ef19eec3fb7c8'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}'
    r = requests.get(url)
    content = r.json()
    for item in content['list']:
        print(item['dt_txt'], item['main']['temp'], item['weather'][0]['description'])

   #returning content (the result of the scraping from the function above)
print(get_weather(city= 'barcelona'))

#Function to display the weather from previous function into the output message of our future widget
def show_weather():
    input_text = text.text()
    output_label.setText(input_text)
    city = text.currentText()
    weather = get_weather(city)
    output_label.setText(weather)


#Instantiation of the app itself
app= QApplication([])
window = QWidget()
window.setWindowTitle('Weather Check')

#Defining Main Layout and Layout 1
layout = QVBoxLayout()  #Main Layout, it is Vertical

#adding city/input box on where to check weather
text = QLineEdit()
layout.addWidget(text)

#Adding a button
btn = QPushButton('Check Weather')
layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_weather)

#Adding Label (Output message)
output_label = QLabel('')
layout.addWidget(output_label)

#App execution
window.setLayout(layout)
window.show()
app.exec()