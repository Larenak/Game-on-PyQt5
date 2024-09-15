from GameBoard import sum_x, sum_y
class ButtonTools(object):
    def pressed(self, btn):
        """Изменение цвета при нажатии на кнопку"""
        if btn.styleSheet() == ("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);"):
            btn.setStyleSheet("background-color: rgb(46, 55, 93);\n""color: rgb(255, 255, 255);")
        else: 
            btn.setStyleSheet("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);")
    def click_checker(self):
        """Отслеживать нажатие на кнопку"""
        self.Btn_00.clicked.connect(lambda:self.pressed(self.Btn_00))
        self.Btn_01.clicked.connect(lambda:self.pressed(self.Btn_01))
        self.Btn_02.clicked.connect(lambda:self.pressed(self.Btn_02))
        self.Btn_03.clicked.connect(lambda:self.pressed(self.Btn_03))
        self.Btn_04.clicked.connect(lambda:self.pressed(self.Btn_04))
        self.Btn_10.clicked.connect(lambda:self.pressed(self.Btn_10))
        self.Btn_11.clicked.connect(lambda:self.pressed(self.Btn_11))
        self.Btn_12.clicked.connect(lambda:self.pressed(self.Btn_12))
        self.Btn_13.clicked.connect(lambda:self.pressed(self.Btn_13))
        self.Btn_14.clicked.connect(lambda:self.pressed(self.Btn_14))
        self.Btn_20.clicked.connect(lambda:self.pressed(self.Btn_20))
        self.Btn_21.clicked.connect(lambda:self.pressed(self.Btn_21))
        self.Btn_22.clicked.connect(lambda:self.pressed(self.Btn_22))
        self.Btn_23.clicked.connect(lambda:self.pressed(self.Btn_23))
        self.Btn_24.clicked.connect(lambda:self.pressed(self.Btn_24))
        self.Btn_30.clicked.connect(lambda:self.pressed(self.Btn_30))
        self.Btn_31.clicked.connect(lambda:self.pressed(self.Btn_31))
        self.Btn_32.clicked.connect(lambda:self.pressed(self.Btn_32))
        self.Btn_33.clicked.connect(lambda:self.pressed(self.Btn_33))
        self.Btn_34.clicked.connect(lambda:self.pressed(self.Btn_34))
        self.Btn_40.clicked.connect(lambda:self.pressed(self.Btn_40))
        self.Btn_41.clicked.connect(lambda:self.pressed(self.Btn_41))
        self.Btn_42.clicked.connect(lambda:self.pressed(self.Btn_42))
        self.Btn_43.clicked.connect(lambda:self.pressed(self.Btn_43))
        self.Btn_44.clicked.connect(lambda:self.pressed(self.Btn_44))