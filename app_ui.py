from PyQt5 import QtCore, QtGui, QtWidgets
import weather_app
import os

class Ui_WeatherApp(object):
    def setupUi(self, WeatherApp):
        WeatherApp.setObjectName("WeatherApp")
        WeatherApp.resize(920, 517)
        WeatherApp.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #2196F3, stop:1 #64B5F6);
            }
            QLineEdit {
                padding: 10px;
                border-radius: 20px;
                background-color: rgba(255, 255, 255, 0.9);
                border: none;
            }
            QPushButton {
                background-color: #1565C0;
                border-radius: 20px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QLabel {
                color: white;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(WeatherApp)
        self.centralwidget.setObjectName("centralwidget")

        # Search container (top section)
        self.search_container = QtWidgets.QWidget(self.centralwidget)
        self.search_container.setGeometry(QtCore.QRect(0, 0, 920, 150))
        
        # Current Weather Label
        self.currweatherlabel = QtWidgets.QLabel(self.search_container)
        self.currweatherlabel.setGeometry(QtCore.QRect(200, 20, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.currweatherlabel.setFont(font)
        self.currweatherlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currweatherlabel.setObjectName("currweatherlabel")
        
        # Search Input
        self.location_input = QtWidgets.QLineEdit(self.search_container)
        self.location_input.setGeometry(QtCore.QRect(200, 80, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.location_input.setFont(font)
        self.location_input.setAlignment(QtCore.Qt.AlignCenter)
        self.location_input.setObjectName("location_input")
        
        # Search Button
        self.SearchButton = QtWidgets.QPushButton(self.search_container)
        self.SearchButton.setGeometry(QtCore.QRect(610, 80, 41, 41))
        self.SearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SearchButton.setIcon(QtGui.QIcon("images/search_icon.png"))
        self.SearchButton.setIconSize(QtCore.QSize(20, 20))
        self.SearchButton.clicked.connect(self.search)

        # Weather display container (middle section)
        self.weather_container = QtWidgets.QWidget(self.centralwidget)
        self.weather_container.setGeometry(QtCore.QRect(0, 150, 920, 300))
        
        # Weather Icon Label
        self.weather_icon = QtWidgets.QLabel(self.weather_container)
        self.weather_icon.setGeometry(QtCore.QRect(360, 20, 200, 200))
        self.weather_icon.setAlignment(QtCore.Qt.AlignCenter)
        
        # Temperature Label
        self.templabel = QtWidgets.QLabel(self.weather_container)
        self.templabel.setGeometry(QtCore.QRect(330, 180, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.templabel.setFont(font)
        self.templabel.setAlignment(QtCore.Qt.AlignCenter)
        
        # Feels Like Label
        self.feelslikelabel = QtWidgets.QLabel(self.weather_container)
        self.feelslikelabel.setGeometry(QtCore.QRect(325, 270, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.feelslikelabel.setFont(font)
        self.feelslikelabel.setAlignment(QtCore.Qt.AlignCenter)
        
        # Weather Description Label
        self.typelabel = QtWidgets.QLabel(self.centralwidget)
        self.typelabel.setGeometry(QtCore.QRect(134, 450, 651, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.typelabel.setFont(font)
        self.typelabel.setAlignment(QtCore.Qt.AlignCenter)

        WeatherApp.setCentralWidget(self.centralwidget)
        self.retranslateUi(WeatherApp)
        
        # Create weather icons dictionary
        self.weather_icons = {
            'clear sky': 'sunny.png',
            'few clouds': 'partly_cloudy.png',
            'scattered clouds': 'cloudy.png',
            'broken clouds': 'cloudy.png',
            'shower rain': 'rain.png',
            'rain': 'rain.png',
            'thunderstorm': 'thunderstorm.png',
            'snow': 'snow.png',
            'mist': 'mist.png'
        }

    def retranslateUi(self, WeatherApp):
        _translate = QtCore.QCoreApplication.translate
        WeatherApp.setWindowTitle(_translate("WeatherApp", "Weather App"))
        self.location_input.setPlaceholderText(_translate("WeatherApp", "Enter city name..."))
        self.currweatherlabel.setText(_translate("WeatherApp", "Weather Forecast"))
        self.SearchButton.setShortcut(_translate("WeatherApp", "Return"))

    def search(self):
        location = self.location_input.text().strip()
        if not location:
            self.show_error("Please enter a location!")
            return
            
        weather = weather_app.fetch_weather(location)
        if "error" in weather:
            self.show_error(f"Error: {weather['error']}")
            return
            
        # Update temperature and description
        self.templabel.setText(f"{round(weather['temp'])}°C")
        self.feelslikelabel.setText(f"Feels like: {round(weather['feels_like'])}°C")
        self.typelabel.setText(weather['description'].capitalize())
        
        # Update weather icon
        description = weather['description'].lower()
        icon_file = self.weather_icons.get(description, 'default.png')
        icon_path = os.path.join('images', icon_file)
        
        if os.path.exists(icon_path):
            pixmap = QtGui.QPixmap(icon_path)
            scaled_pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.weather_icon.setPixmap(scaled_pixmap)
        
    def show_error(self, message):
        self.typelabel.setText(message)
        self.templabel.clear()
        self.feelslikelabel.clear()
        self.weather_icon.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WeatherApp = QtWidgets.QMainWindow()
    ui = Ui_WeatherApp()
    ui.setupUi(WeatherApp)
    WeatherApp.show()
    sys.exit(app.exec_())