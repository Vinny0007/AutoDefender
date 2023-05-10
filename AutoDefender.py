import sys
from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt



import time
import sqlite3

class CarDealership(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        self.setWindowTitle("AvtoDefender") # заголовок окна
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        

        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
    
    def initUI(self):
        
        self.setWindowTitle('Автосалон')
        
        #Завантажуємо картинку та створюємо напис
        pixmap = QPixmap('Picture/autodefender.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        
        self.show()
               
        # Створюємо кнопку "Замовити"
        self.order_button = QPushButton('Order car', self)
        
        # Створюємо кнопку "Traid in"
        self.trade_in_button = QPushButton('Traid in', self)
        
        # Створюємо кнопку "Записатись на детейлінг"
        self.detailing_button = QPushButton('Detailing', self)
        
        # Створюємо кнопку "Записатись на детейлінг"
        self.repair_button = QPushButton('Repair shop', self)
        
        #Задаємо розмір
        button_size = QSize(568, 216)
        self.order_button.setFixedSize(button_size)
        self.trade_in_button.setFixedSize(button_size)
        self.detailing_button.setFixedSize(button_size)
        self.repair_button.setFixedSize(button_size)

        #Задаємо стиль
        button_style = 'background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 65px;'
        self.order_button.setStyleSheet(button_style)
        self.trade_in_button.setStyleSheet(button_style)
        self.repair_button.setStyleSheet(button_style)
        self.detailing_button.setStyleSheet(button_style)

        # Створюємо лейаут та додаємо до нього елементи
        layout = QVBoxLayout()
        layout = QGridLayout()
        layout.setContentsMargins(0, 150, 0, 0)
        layout.addWidget(self.order_button, 0, 0)
        layout.addWidget(self.trade_in_button, 0, 1)
        layout.addWidget(self.detailing_button, 1, 0)
        layout.addWidget(self.repair_button, 1, 1)
        self.setLayout(layout)
   
        
        
        self.order_button.clicked.connect(self.handleButton)
        self.trade_in_button.clicked.connect(self.handleButton)
        self.detailing_button.clicked.connect(self.handleButton)
        self.repair_button.clicked.connect(self.handleButton)
        
        

    def handleButton(self):
        sender = self.sender()
        if sender.text() == "Order car":
            self.window2 = Order_window()
            self.window2.show()
            self.close()
                
        elif sender.text() == "Traid in":
            self.window3 = Traid_in_window()
            self.window3.show()
            self.close()
        elif sender.text() == "Detailing":
            self.window4 = Detailing_window()
            self.window4.show()
            self.close()
        elif sender.text() == "Repair shop":
            self.window5 = Repair_shop_window()
            self.window5.show()
            self.close()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    

class Order_window(QWidget):
    def __init__(self,):
        super().__init__()
        
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        
        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        
        
    def initUI(self):     
        self.setWindowTitle('Order')
              
        pixmap = QPixmap('Picture/ordermain.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        
        self.show()

        #Cтворення рекламної інсталяції
        pictures =  f'Advertising/1.png'
        self.picture = QLabel('', self)
        self.picture.setPixmap(QPixmap(pictures))


        #Створюємо кнопку "На головну"
        self.exit_button = QPushButton('На головну', self)
                
        #Створюємо кнопку "Сhoose car"
        self.choose_button = QPushButton('Choose car', self)
        
        #Створюємо кнопку "Order car"
        self.order_button = QPushButton('Order car', self)
                
        #Задаємо стиль
        button_style = 'background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;'
        self.exit_button.setStyleSheet(button_style)
        self.choose_button.setStyleSheet(button_style)
        self.order_button.setStyleSheet(button_style)

        #Задаємо розмір
        button_size = QSize(400,200)
        self.exit_button.setFixedSize(button_size)
        self.choose_button.setFixedSize(button_size)
        self.order_button.setFixedSize(button_size)

        layout = QGridLayout()

        layout.addWidget(self.picture, 0, 0, 1, 3)
        layout.addWidget(self.choose_button,1, 1, 1, 1)
        layout.addWidget(self.order_button,1, 0, 1, 1)
        layout.addWidget(self.exit_button,1, 2, 1, 1)
        

        layout.setContentsMargins(0, 200, 0, 0)
        self.setLayout(layout)

        self.exit_button.clicked.connect(self.closed)
        self.choose_button.clicked.connect(self.choose)
        self.order_button.clicked.connect(self.order)
    
    def order(self):
        self.window1 = Order_window_2()
        self.window1.show()

        self.close()

    def choose(self):
        self.window1 = Order_window_1(pic_numb = 0)
        self.window1.show()

        self.close()

    def closed(self):
        self.window1 = CarDealership()
        self.window1.show()

        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

class Order_window_1(QWidget):
    def __init__(self,pic_numb):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        self.pic_numb = pic_numb
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        
        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        
    def initUI(self):     
        self.setWindowTitle('Order')
                        
        pixmap = QPixmap('Picture/сhoice.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        
        
        self.show()
        
        #Створюємо кнопку "На головну"
        self.exit_button = QPushButton('На головну', self)
        self.exit_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.exit_button.setFixedSize(200,100)
        

        #Створюємо кнопку "Відправити"
        self.send_button = QPushButton('Відправити', self)
        self.send_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.send_button.setFixedSize(200,100)

        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT char FROM sale")
        
        char = cursor.fetchone()[0]

        #Вивід фото автомобіля
        pictures =  f'Saleauto/1.jpg'
        self.picture = QLabel('', self)
        self.picture.setPixmap(QPixmap(pictures))
        
        #Вивід характеристик
        self.characters = QLabel(char, self)
        self.characters.setFixedSize(QSize(16777215, 300))
        
        #Поля з іменем та номер телефону
        self.name = QLineEdit('')
        self.name.setFixedSize(QSize(200, 16777215))
        self.name.setPlaceholderText("Прізвище та ім\'я")
        
        self.number = QLineEdit('')
        self.number.setFixedSize(QSize(200, 16777215))
        self.number.setPlaceholderText("Номер телефону")
        
        #Кнопки з переходами
        self.right_button = QPushButton('>', self)
        self.right_button.setFixedSize(QSize(30, 200))
        
        self.left_button = QPushButton('<', self)
        self.left_button.setFixedSize(QSize(30, 200))
                
        #Кнопка фільтру
        # self.filter_button = QPushButton('Filter', self)
        # self.filter_button.setFixedSize(QSize(200, 100))
        # self.filter_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')

        #Створюєм стиль
        style = 'background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;'
        self.characters.setStyleSheet(style)
        self.right_button.setStyleSheet(style)
        self.left_button.setStyleSheet(style)
        self.name.setStyleSheet(style)
        self.number.setStyleSheet(style)

        self.exit_button.clicked.connect(self.closed)
        self.send_button.clicked.connect(self.add_to_database)
        self.right_button.clicked.connect(self.right)
        self.left_button.clicked.connect(self.left)
        # self.filter_button.clicked.connect(self.filter_button)

        layout = QGridLayout()
        layout.setGeometry(QRect(0, 0, 1536, 861))

        layout.addWidget(self.exit_button, 0, 2, 1, 1)
        layout.addWidget(self.send_button, 0, 3, 1, 1)
        layout.addWidget(self.picture, 1, 2, 5, 3)
        # layout.addWidget(self.filter_button, 2, 6, 1, 1)
        layout.addWidget(self.characters, 2, 5, 3, 1)
        layout.addWidget(self.name, 3, 6, 1, 1)
        layout.addWidget(self.number, 4, 6, 1, 1)
        layout.addWidget(self.right_button, 0, 7, 6, 1)
        layout.addWidget(self.left_button, 2, 0, 1, 1)

        layout.setContentsMargins(0, 90, 0, 0)
        self.setLayout(layout)
    
    # def filter(self):
    #     msg_box = QMessageBox()
    #     msg_box.setWindowIcon(QIcon('icon.bmp'))

    def closed(self):
        self.window1 = CarDealership()
        self.window1.show()
        self.close()
    
    def right(self):
        self.pic_numb += 1 

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # cursor.execute(f"SELECT picture FROM sale WHERE numb={self.pic_numb + 1}")    
        # pictures = cursor.fetchone()[0]
        # self.picture.setPixmap(QPixmap(pictures))
        
        
        try:
            cursor.execute(f"SELECT char FROM sale WHERE numb={self.pic_numb +1}")
            char = cursor.fetchone()[0]
            self.characters.setText(char)
            
            cursor.execute(f"SELECT picture FROM sale WHERE numb={self.pic_numb +1}")    
            pictures = cursor.fetchone()[0]
            self.picture.setPixmap(QPixmap(pictures))
        except TypeError:
            # self.pic_numb -= 1
            cursor.execute(f"SELECT picture FROM sale WHERE numb={self.pic_numb}") 
            pictures = cursor.fetchone()[0]
            self.picture.setPixmap(QPixmap(pictures))
            
            cursor.execute(f"SELECT char FROM sale WHERE numb={self.pic_numb}")
            char = cursor.fetchone()[0]
            self.characters.setText(char)
    
    def left(self):
        self.pic_numb -= 1 
       
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        

        try:
            cursor.execute(f"SELECT char FROM sale WHERE numb={self.pic_numb}")
            char = cursor.fetchone()[0]
            self.characters.setText(char)

            cursor.execute(f"SELECT picture FROM sale WHERE numb={self.pic_numb}")    
            pictures = cursor.fetchone()[0]
            self.picture.setPixmap(QPixmap(pictures))
        except TypeError:
            self.pic_numb = 1
            
            cursor.execute(f"SELECT char FROM sale WHERE numb={self.pic_numb}")
            char = cursor.fetchone()[0]
            self.characters.setText(char)

            cursor.execute(f"SELECT picture FROM sale WHERE numb={self.pic_numb}")    
            pictures = cursor.fetchone()[0]
            self.picture.setPixmap(QPixmap(pictures))
    
    def add_to_database(self):
        name = self.name.text()
        number = self.number.text()
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Client_choice (Name, Number_phone, Сar_Number ) VALUES (?, ?, ?)", (name, number, self.pic_numb))
        conn.commit()
        conn.close()
        self.close()

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon('icon.bmp'))
        msg_box.setText("Дякуємо за ваше замовлення!")
        msg_box.setWindowTitle("Повідомлення")
        msg_box.exec()

        time.sleep(2)

        self.window1 = CarDealership()
        self.window1.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
class Order_window_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        

        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        
        
    def initUI(self):     
        self.setWindowTitle('Order')
                        
        pixmap = QPixmap('Picture/order.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        
        self.show()
        
        #Створюємо кнопку "На головну"
        self.exit_button = QPushButton('На головну', self)
        self.exit_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.exit_button.setFixedSize(300,100)
        
        #Створюємо кнопку "Відправити"
        self.send_button = QPushButton('Відправити', self)
        self.send_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.send_button.setFixedSize(300,100)

        #Створюємо надпис "Введіть  контактні дані"
        self.label = QLabel('Введіть  контактні дані')
        self.label.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Cтворюємо надпис "Надайте інформацію про автомобіль"
        self.label_2 = QLabel('Надайте інформацію про автомобіль')
        self.label_2.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Створюємо вибіркове поле 
        self.comboBox = QComboBox()
        self.comboBox.addItem("Нове авто")
        self.comboBox.addItem("Вживане авто")

        #Cтворюємо поле "Ім'я"
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ім'я")
        self.name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.name_input.setFixedSize(500,50)
        
        #Cтворюємо поле "Прізвище"
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Прізвище")
        self.last_name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.last_name_input.setFixedSize(500,50)

        #Cтворюємо поле "Номер телефону"
        self.number_phone_input = QLineEdit()
        self.number_phone_input.setPlaceholderText("Номер телефону")
        self.number_phone_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.number_phone_input.setFixedSize(500,50)

        #Створюємо поле "Марка авто"
        self.brand_input = QLineEdit()
        self.brand_input.setPlaceholderText("Марка авто")
        self.brand_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.brand_input.setFixedSize(500,50)

        #Створюємо поле "Модель авто"
        self.model_input = QLineEdit()
        self.model_input.setPlaceholderText("Модель авто")
        self.model_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.model_input.setFixedSize(500,50)

        #Створюємо поле "Об\'єм двигуна"
        self.engine_capacity_input = QLineEdit()
        self.engine_capacity_input.setPlaceholderText("Об'єм двигуна")        
        self.engine_capacity_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.engine_capacity_input.setFixedSize(500,50)

        #Створюємо поле "Колір"
        self.color_input = QLineEdit()
        self.color_input.setPlaceholderText("Колір")
        self.color_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.color_input.setFixedSize(300,50)

        #Створюємо поле "Рік випуску"
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Рік випуску")
        self.year_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.year_input.setFixedSize(300,50)

        #Cтворюємо поле "Бажана ціна"
        self.coments_input = QLineEdit()
        self.coments_input.setPlaceholderText("Бажана ціна")
        self.coments_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.coments_input.setFixedSize(300,50)

        self.send_button.clicked.connect(self.add_to_database)
        self.exit_button.clicked.connect(self.closed)

        layout = QGridLayout()
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.exit_button)
        h_layout.addWidget(self.send_button)
                
        layout.addLayout(h_layout, 1, 0, 1, 1)
        layout.addWidget(self.label, 2, 0, 1, 1)
        layout.addWidget(self.label_2, 2, 1, 1, 1)
        layout.addWidget(self.comboBox, 2, 2, 1, 1)
        layout.addWidget(self.name_input, 3, 0, 1, 1)
        layout.addWidget(self.last_name_input, 4, 0, 1, 1)
        layout.addWidget(self.number_phone_input, 5, 0, 1, 1)
        layout.addWidget(self.brand_input, 3, 1, 1, 1)
        layout.addWidget(self.model_input, 4, 1, 1, 1)
        layout.addWidget(self.engine_capacity_input, 5, 1, 1, 1)
        layout.addWidget(self.color_input, 3, 2, 1, 1)
        layout.addWidget(self.year_input, 4, 2, 1, 1)
        layout.addWidget(self.coments_input, 5, 2, 1, 1)
        
        self.setLayout(layout)
       
    def add_to_database(self):
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        number_phone = self.number_phone_input.text()
        brand = self.brand_input.text()
        model = self.model_input.text()
        engine = self.engine_capacity_input.text()
        color = self.color_input.text()
        year = self.year_input.text()
        coment = self.coments_input.text()
        new_used =  self.comboBox.currentText()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ORDERED (Name, Last_Name, Number_phone, Brand, Model, Engine_Capacity, Color, Year, Price, New_Used) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, last_name, number_phone, brand, model, engine, color, year, coment, new_used))
        conn.commit()
        conn.close()
        self.close()

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon('icon.bmp'))
        msg_box.setText("Дякуємо за ваше замовлення!")
        msg_box.setWindowTitle("Повідомлення")
        msg_box.exec()

        time.sleep(2)

        self.window1 = CarDealership()
        self.window1.show()
            
    def closed(self):
        self.window1 = CarDealership()
        self.window1.show()

        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

class Traid_in_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        self.setWindowTitle('Traid in')
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
       
        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
    
    def initUI(self):        
        pixmap = QPixmap('Picture/traid in.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        
        self.show()

        #Створюємо кнопку "На головну"
        self.exit_button = QPushButton('На головну', self)
        self.exit_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.exit_button.setFixedSize(200,100)
        
        #Створюємо кнопку "Відправити"
        self.send_button = QPushButton('Відправити', self)
        self.send_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.send_button.setFixedSize(200,100)

        #Створюємо надпис "Введіть  контактні дані"
        self.label = QLabel('Введіть  контактні дані')
        self.label.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Cтворюємо надпис "Надайте інформацію про автомобіль"
        self.label_2 = QLabel('Надайте інформацію про автомобіль')
        self.label_2.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Створюємо вибіркове поле 
        self.comboBox = QComboBox()
        self.comboBox.addItem("Нове авто")
        self.comboBox.addItem("Вживане авто")

        #Cтворюємо поле "Ім'я"
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ім'я")
        self.name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.name_input.setFixedSize(500,50)

        #Cтворюємо поле "Прізвище"
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Прізвище")
        self.last_name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.last_name_input.setFixedSize(500,50)

        #Cтворюємо поле "Номер телефону"
        self.number_phone_input = QLineEdit()
        self.number_phone_input.setPlaceholderText("Номер телефону")
        self.number_phone_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.number_phone_input.setFixedSize(500,50)

        #Створюємо поле "Марка авто"
        self.brand_input = QLineEdit()
        self.brand_input.setPlaceholderText("Марка авто")
        self.brand_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.brand_input.setFixedSize(500,50)

        #Створюємо поле "Модель авто"
        self.model_input = QLineEdit()
        self.model_input.setPlaceholderText("Модель авто")
        self.model_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.model_input.setFixedSize(500,50)

        #Створюємо поле "Об\'єм двигуна"
        self.engine_capacity_input = QLineEdit()
        self.engine_capacity_input.setPlaceholderText("Об'єм двигуна")        
        self.engine_capacity_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.engine_capacity_input.setFixedSize(500,50)

        #Створюємо поле "Колір"
        self.color_input = QLineEdit()
        self.color_input.setPlaceholderText("Колір")
        self.color_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.color_input.setFixedSize(400,50)

        #Створюємо поле "Рік випуску"
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Рік випуску")
        self.year_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.year_input.setFixedSize(400,50)
        #Cтворюємо поле "Бажана ціна"
        self.coments_input = QLineEdit()
        self.coments_input.setPlaceholderText("Бажана ціна")
        self.coments_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.coments_input.setFixedSize(400,50)

        self.send_button.clicked.connect(self.add_to_database)
        self.exit_button.clicked.connect(self.closed)

        layout = QGridLayout()
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.exit_button)
        h_layout.addWidget(self.send_button)
                
        layout.addLayout(h_layout, 1, 0, 1, 1)
        layout.addWidget(self.label, 2, 0, 1, 1)
        layout.addWidget(self.label_2, 2, 1, 1, 1)
        layout.addWidget(self.comboBox, 2, 2, 1, 1)
        layout.addWidget(self.name_input, 3, 0, 1, 1)
        layout.addWidget(self.last_name_input, 4, 0, 1, 1)
        layout.addWidget(self.number_phone_input, 5, 0, 1, 1)
        layout.addWidget(self.brand_input, 3, 1, 1, 1)
        layout.addWidget(self.model_input, 4, 1, 1, 1)
        layout.addWidget(self.engine_capacity_input, 5, 1, 1, 1)
        layout.addWidget(self.color_input, 3, 2, 1, 1)
        layout.addWidget(self.year_input, 4, 2, 1, 1)
        layout.addWidget(self.coments_input, 5, 2, 1, 1)
        
        self.setLayout(layout)

    def add_to_database(self):
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        number_phone = self.number_phone_input.text()
        brand = self.brand_input.text()
        model = self.model_input.text()
        engine = self.engine_capacity_input.text()
        color = self.color_input.text()
        year = self.year_input.text()
        coment = self.coments_input.text()
        new_used =  self.comboBox.currentText()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Traid_in (Name, Last_Name, Number_phone, Brand, Model, Engine_Capacity, Color, Year, Price, New_Used) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, last_name, number_phone, brand, model, engine, color, year, coment, new_used))
        conn.commit()
        conn.close()
        self.close()

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon('icon.bmp'))
        msg_box.setText("Дякуємо за ваше замовлення!")
        msg_box.setWindowTitle("Повідомлення")
        msg_box.exec()

        time.sleep(2)

        self.window1 = CarDealership()
        self.window1.show()
            
    def closed(self):
        self.window1 = CarDealership()
        self.window1.show()

        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
class Detailing_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        self.setWindowTitle('Detailing')
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        

        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0,0,screen_size.width(), screen_size.height())
    
    def initUI(self):        
        pixmap = QPixmap('Picture/detailing.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)

        self.show()

        #Створюємо кнопку "На головну"
        self.exit_button = QPushButton('На головну', self)
        self.exit_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.exit_button.setFixedSize(400,200)

        #Cтворюємо поле "Ім'я"
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ім'я")
        self.name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.name_input.setFixedSize(500,50)
    
        #Cтворюємо поле "Прізвище"
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Прізвище")
        self.last_name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.last_name_input.setFixedSize(500,50)

        #Cтворюємо поле "Номер телефону"
        self.number_phone_input = QLineEdit()
        self.number_phone_input.setPlaceholderText("Номер телефону")
        self.number_phone_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.number_phone_input.setFixedSize(500,50)

        #Створюємо поле "Тип авто"
        self.type_input = QLineEdit()
        self.type_input.setPlaceholderText("Тип автомобіля")
        self.type_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.type_input.setFixedSize(500,50)

        #Cтворюємо бронювання по даті
        self.dateEdit = QDateEdit()
        self.dateEdit.setToolTip('Виберіть бажану дату')
        self.dateEdit.setStyleSheet("background-color: #f0f0f0; color: #555555; border: 1px solid #cccccc;")
        self.dateEdit.setFixedSize(500,50)

        # #Cтворюємо надписи
        #Створюємо надпис "Введіть  контактні дані"
        self.label = QLabel('Введіть  контактні дані')
        self.label.setStyleSheet("font: 87 8pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Cтворюємо надпис "Надайте інформацію про автомобіль"
        self.label_2 = QLabel('Надайте інформацію про автомобіль')
        self.label_2.setStyleSheet("font: 87 8pt \"Arial Black\"; color: rgb(255, 255, 255);")
        
        #Cтворюємо надпис "Вкажіть дату"
        self.label_3 = QLabel('Вкажіть бажану дату')
        self.label_3.setStyleSheet("font: 87 8pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Cтворюємо поле "Додатковий коментар"
        self.coments_input = QLineEdit()
        self.coments_input.setPlaceholderText("Додатковий коментар")
        self.coments_input.setStyleSheet("font: 87 8pt \"Arial Black\";")

        #Cтворюємо кнопку 'Продовжити'
        self.continue_button = QPushButton('Продовжити запис', self)
        self.continue_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        
        self.exit_button.clicked.connect(self.closed)
        self.continue_button.clicked.connect(self.continued)

        layout = QGridLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.exit_button)
                      
        layout.addLayout(h_layout, 1, 0, 1, 1)
        layout.addWidget(self.name_input, 3, 0, 1, 1)
        layout.addWidget(self.last_name_input, 4, 0, 1, 1)
        layout.addWidget(self.number_phone_input, 5, 0, 1, 1)
        layout.addWidget(self.type_input, 3, 1, 1, 1)
        layout.addWidget(self.coments_input, 4, 2, 1, 1)
        layout.addWidget(self.continue_button, 5, 2, 1, 1)
        layout.addWidget(self.dateEdit, 3, 2, 1, 1)
        self.setLayout(layout)
    
    def continued(self):
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        number_phone = self.number_phone_input.text()
        type1 = self.type_input.text()
        coment = self.coments_input.text()
        selected_date = self.dateEdit.date().toString('yyyy-MM-dd')

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Detailing (Name, Last_Name, Number_phone, Type, Coments, Date) VALUES (?, ?, ?, ?, ?, ?)", (name, last_name, number_phone, type1, coment, selected_date))
        conn.commit()
        conn.close()
        self.close()
        self.window2 =  Detailing_window1()
        self.window2.show()

    def closed(self):
        self.window1 = CarDealership()
        self.window1.show()
        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

class Detailing_window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        self.setWindowTitle('Detailing')
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        
        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0,0,screen_size.width(), screen_size.height())
    
    def initUI(self):        
        pixmap = QPixmap('Picture/detailing.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)

        self.show()

        ##Створення надписів 
        #Створюємо надпис "Мийка і комплексні послуги"
        self.label1 = QLabel('Мийка і комплексні послуги')
        self.label1.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")
        
        #Створюємо надпис "Хімчистка салону та озонування"
        self.label2 = QLabel('Хімчистка салону та озонування')
        self.label2.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Створюємо надпис "Скло,диски, шини та двигун"
        self.label3 = QLabel('Скло,диски, шини та двигун')
        self.label3.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")
        
        #Створення кнопки продовження
        self.continue_button = QPushButton('Відправити', self)
        self.continue_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')

        #Створення check box для форми
        self.checkbox1 = QCheckBox('Безконтактне миття', self)
        self.checkbox2 = QCheckBox('2/3-х фазне миття', self)
        self.checkbox3 = QCheckBox('Кварцове миття', self)
        self.checkbox4 = QCheckBox('Хімчистка з розбиранням салону', self)
        self.checkbox5 = QCheckBox('Хімчистка без розбирання салону', self)
        self.checkbox6 = QCheckBox('Озонування', self)
        self.checkbox7 = QCheckBox('Чистка', self)
        self.checkbox8 = QCheckBox('Відновлення', self)
        self.checkbox9 = QCheckBox('Антидощ', self)

        style = """
                QCheckBox {
                    color: white;
                    spacing: 25px;
                }
                QCheckBox::indicator {
                    width: 50px;
                    height: 50px;
                }
                QCheckBox::indicator:unchecked {
                    border: 2px solid #ccc;
                }
                QCheckBox::indicator:checked {
                    background-color: #000000;
                    border: 2px solid #000000;
                }
                QCheckBox::indicator:unchecked:hover {
                    border: 2px solid #999;
                }
                QCheckBox::indicator:checked:hover {
                    background-color: #0c7bd0;
                    border: 2px solid #0c7bd0;
                }
            """

        self.checkbox1.setStyleSheet(style)
        self.checkbox2.setStyleSheet(style)
        self.checkbox3.setStyleSheet(style)
        self.checkbox4.setStyleSheet(style)
        self.checkbox5.setStyleSheet(style)
        self.checkbox6.setStyleSheet(style)
        self.checkbox7.setStyleSheet(style)
        self.checkbox8.setStyleSheet(style)
        self.checkbox9.setStyleSheet(style)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 50)
        layout.addWidget(self.label1, 2, 0, 1, 1)
        layout.addWidget(self.label2, 2, 1, 1, 1)
        layout.addWidget(self.label3, 2, 2, 1, 1)
        layout.addWidget(self.checkbox1, 3, 0, 1, 1)
        layout.addWidget(self.checkbox2, 4, 0, 1, 1)
        layout.addWidget(self.checkbox3, 5, 0, 1, 1)
        layout.addWidget(self.checkbox4, 3, 1, 1, 1)
        layout.addWidget(self.checkbox5, 4, 1, 1, 1)
        layout.addWidget(self.checkbox6, 5, 1, 1, 1)
        layout.addWidget(self.checkbox7, 3, 2, 1, 1)
        layout.addWidget(self.checkbox8, 4, 2, 1, 1)
        layout.addWidget(self.checkbox9, 5, 2, 1, 1)
        layout.addWidget(self.continue_button, 1, 0, 1, 1)
       
        self.setLayout(layout)
        
        self.continue_button.clicked.connect(self.send_data_to_sql)
    
    def send_data_to_sql(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        checkbox1_state = self.checkbox1.isChecked()
        checkbox2_state = self.checkbox2.isChecked()
        checkbox3_state = self.checkbox3.isChecked()
        checkbox4_state = self.checkbox4.isChecked()
        checkbox5_state = self.checkbox5.isChecked()
        checkbox6_state = self.checkbox6.isChecked()
        checkbox7_state = self.checkbox7.isChecked()
        checkbox8_state = self.checkbox8.isChecked()
        checkbox9_state = self.checkbox9.isChecked()
        
        cur.execute('INSERT INTO DETAILING (Contactless_washing, phase_washing, Quartz_washing, Dry_cleaning_witht , Dry_cleaning_without, Ozonation, Cleaning, Restoration, Anti_rain) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (checkbox1_state, checkbox2_state, checkbox3_state, checkbox4_state, checkbox5_state, checkbox6_state, checkbox7_state, checkbox8_state, checkbox9_state))
        conn.commit()
        conn.close()
        self.close()

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon('icon.bmp'))
        msg_box.setText("Ви успішно записані!")
        msg_box.setWindowTitle("Повідомлення")
        msg_box.exec()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

class Repair_shop_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.bmp'))
        self.setWindowTitle('Repair shop')
        # Отримуємо розмір екрану
        screen_size = QApplication.primaryScreen().geometry()
        

        # Задаємо розмір вікна як розмір екрану
        self.setGeometry(0,0,screen_size.width(), screen_size.height())
    
    def initUI(self):        
        pixmap = QPixmap('Picture/repair shop.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        
        self.show()

        #Створюємо кнопку "На головну"
        self.exit_button = QPushButton('На головну', self)
        self.exit_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.exit_button.setFixedSize(290,100)
        
        #Створюємо кнопку "Відправити"
        self.send_button = QPushButton('Відправити', self)
        self.send_button.setStyleSheet('background-color: #7d7c7c; color: white; bold; font-family: Impact,; font-size: 22px;')
        self.send_button.setFixedSize(290,100)

        #Створюємо надпис "Введіть  контактні дані"
        self.label = QLabel('Введіть  контактні дані')
        self.label.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Cтворюємо надпис "Надайте інформацію про автомобіль"
        self.label_2 = QLabel('Надайте інформацію про автомобіль')
        self.label_2.setStyleSheet("font: 87 20pt \"Arial Black\"; color: rgb(255, 255, 255);")

        #Створюємо вибіркове поле 
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Діагностика")
        self.comboBox.addItem("Поломка")
        self.comboBox.setFixedSize(500,50)

        #Cтворюємо поле "Ім'я"
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ім'я")
        self.name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.name_input.setFixedSize(500,50)
        
        #Cтворюємо поле "Прізвище"
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Прізвище")
        self.last_name_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.last_name_input.setFixedSize(500,50)

        #Cтворюємо поле "Номер телефону"
        self.number_phone_input = QLineEdit()
        self.number_phone_input.setPlaceholderText("Номер телефону")
        self.number_phone_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.number_phone_input.setFixedSize(500,50)

        #Створюємо поле "Марка авто"
        self.brand_input = QLineEdit()
        self.brand_input.setPlaceholderText("Марка авто")
        self.brand_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.brand_input.setFixedSize(500,50)

        #Створюємо поле "Модель авто"
        self.model_input = QLineEdit()
        self.model_input.setPlaceholderText("Модель авто")
        self.model_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.model_input.setFixedSize(500,50)

        #Створюємо поле "Модель двигуна"
        self.engine_capacity_input = QLineEdit()
        self.engine_capacity_input.setPlaceholderText("Модель двигуна")        
        self.engine_capacity_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.engine_capacity_input.setFixedSize(500,50)

        #Створюємо поле "Рік випуску"
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Рік випуску")
        self.year_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.year_input.setFixedSize(500,50)

        #Cтворюємо поле "Можлива причина поломки"
        self.coments_input = QLineEdit()
        self.coments_input.setPlaceholderText("Можлива причина поломки")
        self.coments_input.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.coments_input.setFixedSize(500,50)
        
        #cтворення checkBock
        self.checkbox1 = QCheckBox('Викликати евакуатор', self)
        self.checkbox1.setStyleSheet("""QCheckBox {color: white;spacing: 5px;}
                                        QCheckBox::indicator {width: 40px;height: 40px;}
                                        QCheckBox::indicator:unchecked {border: 2px solid #ccc;}
                                        QCheckBox::indicator:checked {background-color: #000000;border: 2px solid #000000;}
                                        QCheckBox::indicator:unchecked:hover {border: 2px solid #999;}
                                        QCheckBox::indicator:checked:hover {background-color: #0c7bd0;border: 2px solid #0c7bd0;}""")

        layout = QGridLayout()
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.exit_button)
        h_layout.addWidget(self.send_button)
                
        layout.addLayout(h_layout, 1, 0, 1, 1)
        layout.addWidget(self.label, 2, 0, 1, 1)
        layout.addWidget(self.label_2, 2, 1, 1, 1)
        layout.addWidget(self.checkbox1, 2, 2, 1, 1)
        layout.addWidget(self.name_input, 3, 0, 1, 1)
        layout.addWidget(self.last_name_input, 4, 0, 1, 1)
        layout.addWidget(self.number_phone_input, 5, 0, 1, 1)
        layout.addWidget(self.brand_input, 3, 1, 1, 1)
        layout.addWidget(self.model_input, 4, 1, 1, 1)
        layout.addWidget(self.engine_capacity_input, 5, 1, 1, 1)
        layout.addWidget(self.comboBox, 3, 2, 1, 1)
        layout.addWidget(self.year_input, 4, 2, 1, 1)
        layout.addWidget(self.coments_input, 5, 2, 1, 1)

        self.setLayout(layout)
        
        self.send_button.clicked.connect(self.add_to_database)
        self.exit_button.clicked.connect(self.closed)

    def closed(self):
        self.window1 = CarDealership()
        self.window1.show()

        self.close()

    def add_to_database(self):
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        number_phone = self.number_phone_input.text()
        brand = self.brand_input.text()
        model = self.model_input.text()
        engine = self.engine_capacity_input.text()
        year = self.year_input.text()
        coment = self.coments_input.text()
        diagnostic =  self.comboBox.currentText()
        checkbox1_state = self.checkbox1.isChecked()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Repair_shop (Name, Last_Name, Number_phone, Brand, Model, Engine, Year, Coments, Evacuation, Diagnostic) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, last_name, number_phone, brand, model, engine, year, coment, checkbox1_state, diagnostic))
        conn.commit()
        conn.close()
        self.close()

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon('icon.bmp'))
        msg_box.setText("Дякуємо за ваше замовлення!")
        msg_box.setWindowTitle("Повідомлення")
        msg_box.exec()

        time.sleep(2)

        self.window1 = CarDealership()
        self.window1.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CarDealership()
    sys.exit(app.exec())

