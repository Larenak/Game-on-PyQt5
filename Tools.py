import sys
class ButtonTools(object):

    def pressed(self, btn):
        """Изменение цвета при нажатии на кнопку"""
        if btn.styleSheet() == ("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);"):
            btn.setStyleSheet("background-color: rgb(46, 55, 93);\n""color: rgb(255, 255, 255);")
        else: 
            btn.setStyleSheet("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);")
        self.sum_check()
        if self.win_checker():
            pass

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
    def sum_check(self):

        """Проверяет суммы чисел рядов и строк и если они совпадают с данными значениями, то обводит число суммы зеленым цветом"""
        for i in range(5):
            y_sum = 0
            x_sum = 0
            for j in range(5):
                if self.gameboard[i][j].styleSheet() == \
                ("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);"):
                    y_sum += int(self.gameboard[i][j].text())
                if self.gameboard[j][i].styleSheet() == \
                ("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);"):
                    x_sum += int(self.gameboard[j][i].text())   

            if int(self.sum_goal_x[0][i].text()) == x_sum:
                self.sum_goal_x[0][i].setStyleSheet("color: rgb(255, 255, 255);\
                                                    background-color: rgb(10, 25, 44);\
                                                    border :2px solid ;\
                                                    border-color : green; ")
                
                self.sum_goal_x[1][i].setStyleSheet("color: rgb(255, 255, 255);\
                                                    background-color: rgb(10, 25, 44);\
                                                    border :2px solid ;\
                                                    border-color : green; ")
            else: 
                self.sum_goal_x[0][i].setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(10, 25, 44);")
                self.sum_goal_x[1][i].setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(10, 25, 44);")
                
            if int(self.sum_goal_y[0][i].text()) == y_sum:
                self.sum_goal_y[0][i].setStyleSheet("color: rgb(255, 255, 255);\
                                                    background-color: rgb(10, 25, 44);\
                                                    border :2px solid ;\
                                                    border-color : green; ")
                
                self.sum_goal_y[1][i].setStyleSheet("color: rgb(255, 255, 255);\
                                                    background-color: rgb(10, 25, 44);\
                                                    border :2px solid ;\
                                                    border-color : green; ")
            else: 
                self.sum_goal_y[0][i].setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(10, 25, 44);")
                self.sum_goal_y[1][i].setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(10, 25, 44);")
    
    def win_checker(self):
        self.count_sum = 0
        for i in range(5):
            if self.sum_goal_y[0][i].styleSheet() == ("color: rgb(255, 255, 255);\
                                                    background-color: rgb(10, 25, 44);\
                                                    border :2px solid ;\
                                                    border-color : green; "):
                self.count_sum += 1
        for i in range(5):
            if self.sum_goal_x[0][i].styleSheet() == ("color: rgb(255, 255, 255);\
                                                    background-color: rgb(10, 25, 44);\
                                                    border :2px solid ;\
                                                    border-color : green; "):
                self.count_sum += 1
        if self.count_sum == 10:
            return True