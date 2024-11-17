import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from GameBoard import Board_generate

class ButtonTools(object):

    def pressed(self, btn,app,gameboard,goal_x,goal_y):
        """Изменение цвета при нажатии на кнопку, а также вызов диалогового окна при победе"""
        if btn.styleSheet() == ("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);"):
            btn.setStyleSheet("background-color: rgb(46, 55, 93);\n""color: rgb(255, 255, 255);")
        else: 
            btn.setStyleSheet("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);")
        self.sum_check()
        if self.win_checker():
            self.win_dialog(app)

    def click_checker(self,app,gameboard, goal_x, goal_y):
        """Отслеживать нажатие на кнопку"""
        self.Btn_00.clicked.connect(lambda:self.pressed(self.Btn_00, app,gameboard,goal_x,goal_y))
        self.Btn_01.clicked.connect(lambda:self.pressed(self.Btn_01, app,gameboard,goal_x,goal_y))
        self.Btn_02.clicked.connect(lambda:self.pressed(self.Btn_02, app,gameboard,goal_x,goal_y))
        self.Btn_03.clicked.connect(lambda:self.pressed(self.Btn_03, app,gameboard,goal_x,goal_y))
        self.Btn_04.clicked.connect(lambda:self.pressed(self.Btn_04, app,gameboard,goal_x,goal_y))
        self.Btn_10.clicked.connect(lambda:self.pressed(self.Btn_10, app,gameboard,goal_x,goal_y))
        self.Btn_11.clicked.connect(lambda:self.pressed(self.Btn_11, app,gameboard,goal_x,goal_y))
        self.Btn_12.clicked.connect(lambda:self.pressed(self.Btn_12, app,gameboard,goal_x,goal_y))
        self.Btn_13.clicked.connect(lambda:self.pressed(self.Btn_13, app,gameboard,goal_x,goal_y))
        self.Btn_14.clicked.connect(lambda:self.pressed(self.Btn_14, app,gameboard,goal_x,goal_y))
        self.Btn_20.clicked.connect(lambda:self.pressed(self.Btn_20, app,gameboard,goal_x,goal_y))
        self.Btn_21.clicked.connect(lambda:self.pressed(self.Btn_21, app,gameboard,goal_x,goal_y))
        self.Btn_22.clicked.connect(lambda:self.pressed(self.Btn_22, app,gameboard,goal_x,goal_y))
        self.Btn_23.clicked.connect(lambda:self.pressed(self.Btn_23, app,gameboard,goal_x,goal_y))
        self.Btn_24.clicked.connect(lambda:self.pressed(self.Btn_24, app,gameboard,goal_x,goal_y))
        self.Btn_30.clicked.connect(lambda:self.pressed(self.Btn_30, app,gameboard,goal_x,goal_y))
        self.Btn_31.clicked.connect(lambda:self.pressed(self.Btn_31, app,gameboard,goal_x,goal_y))
        self.Btn_32.clicked.connect(lambda:self.pressed(self.Btn_32, app,gameboard,goal_x,goal_y))
        self.Btn_33.clicked.connect(lambda:self.pressed(self.Btn_33, app,gameboard,goal_x,goal_y))
        self.Btn_34.clicked.connect(lambda:self.pressed(self.Btn_34, app,gameboard,goal_x,goal_y))
        self.Btn_40.clicked.connect(lambda:self.pressed(self.Btn_40, app,gameboard,goal_x,goal_y))
        self.Btn_41.clicked.connect(lambda:self.pressed(self.Btn_41, app,gameboard,goal_x,goal_y))
        self.Btn_42.clicked.connect(lambda:self.pressed(self.Btn_42, app,gameboard,goal_x,goal_y))
        self.Btn_43.clicked.connect(lambda:self.pressed(self.Btn_43, app,gameboard,goal_x,goal_y))
        self.Btn_44.clicked.connect(lambda:self.pressed(self.Btn_44, app,gameboard,goal_x,goal_y))
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

    def win_dialog(self,app):
        """Диалоговое окно, возникающее при победе"""
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("You win! Want to try again?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.show()
        reply = msgBox.exec_()

        if reply == QMessageBox.Yes:
            self.restart_game()
        else:
            self.close(app)
        
    def restart_game(self):
        """Если в диалоговом окне пользователь выбрал ДА"""
        _translate = QtCore.QCoreApplication.translate
        res = Board_generate()
        game_board = res[0]
        sum_x = res[1]
        sum_y = res[2]
        self.sum_x0l.setText(_translate("MainWindow", str(sum_y[0])))
        self.sum_x1l.setText(_translate("MainWindow", str(sum_y[1])))
        self.sum_x2l.setText(_translate("MainWindow", str(sum_y[2])))
        self.sum_x3l.setText(_translate("MainWindow", str(sum_y[3])))
        self.sum_x4l.setText(_translate("MainWindow", str(sum_y[4])))
        self.sum_x0r.setText(_translate("MainWindow", str(sum_y[0])))
        self.sum_x1r.setText(_translate("MainWindow", str(sum_y[1])))
        self.sum_x2r.setText(_translate("MainWindow", str(sum_y[2])))
        self.sum_x3r.setText(_translate("MainWindow", str(sum_y[3])))
        self.sum_x4r.setText(_translate("MainWindow", str(sum_y[4])))
        self.sum_y0t.setText(_translate("MainWindow", str(sum_x[0])))
        self.sum_y1t.setText(_translate("MainWindow", str(sum_x[1])))
        self.sum_y2t.setText(_translate("MainWindow", str(sum_x[2])))
        self.sum_y3t.setText(_translate("MainWindow", str(sum_x[3])))
        self.sum_y4t.setText(_translate("MainWindow", str(sum_x[4])))
        self.sum_y0b.setText(_translate("MainWindow", str(sum_x[0])))
        self.sum_y1b.setText(_translate("MainWindow", str(sum_x[1])))
        self.sum_y2b.setText(_translate("MainWindow", str(sum_x[2])))
        self.sum_y3b.setText(_translate("MainWindow", str(sum_x[3])))
        self.sum_y4b.setText(_translate("MainWindow", str(sum_x[4])))
        self.Btn_00.setText(_translate("MainWindow", str(game_board[0][0])))
        self.Btn_04.setText(_translate("MainWindow", str(game_board[0][4])))
        self.Btn_02.setText(_translate("MainWindow", str(game_board[0][2])))
        self.Btn_01.setText(_translate("MainWindow", str(game_board[0][1])))
        self.Btn_03.setText(_translate("MainWindow", str(game_board[0][3])))
        self.Btn_20.setText(_translate("MainWindow", str(game_board[2][0])))
        self.Btn_10.setText(_translate("MainWindow", str(game_board[1][0])))
        self.Btn_30.setText(_translate("MainWindow", str(game_board[3][0])))
        self.Btn_11.setText(_translate("MainWindow", str(game_board[1][1])))
        self.Btn_12.setText(_translate("MainWindow", str(game_board[1][2])))
        self.Btn_13.setText(_translate("MainWindow", str(game_board[1][3])))
        self.Btn_14.setText(_translate("MainWindow", str(game_board[1][4])))
        self.Btn_24.setText(_translate("MainWindow", str(game_board[2][4])))
        self.Btn_34.setText(_translate("MainWindow", str(game_board[3][4])))
        self.Btn_44.setText(_translate("MainWindow", str(game_board[4][4])))
        self.Btn_31.setText(_translate("MainWindow", str(game_board[3][1])))
        self.Btn_32.setText(_translate("MainWindow", str(game_board[3][2])))
        self.Btn_33.setText(_translate("MainWindow", str(game_board[3][3])))
        self.Btn_23.setText(_translate("MainWindow", str(game_board[2][3])))
        self.Btn_22.setText(_translate("MainWindow", str(game_board[2][2])))
        self.Btn_21.setText(_translate("MainWindow", str(game_board[2][1])))
        self.Btn_42.setText(_translate("MainWindow", str(game_board[4][2])))
        self.Btn_41.setText(_translate("MainWindow", str(game_board[4][1])))
        self.Btn_43.setText(_translate("MainWindow", str(game_board[4][3])))
        self.Btn_40.setText(_translate("MainWindow", str(game_board[4][0])))

        self.gameboard = [[self.Btn_00, self.Btn_01,self.Btn_02,self.Btn_03,self.Btn_04],
                [self.Btn_10, self.Btn_11,self.Btn_12,self.Btn_13,self.Btn_14],
                [self.Btn_20, self.Btn_21,self.Btn_22,self.Btn_23,self.Btn_24],
                [self.Btn_30, self.Btn_31,self.Btn_32,self.Btn_33,self.Btn_34],
                [self.Btn_40, self.Btn_41,self.Btn_42,self.Btn_43,self.Btn_44]]
        self.sum_goal_x = [[self.sum_y0t,self.sum_y1t,self.sum_y2t,self.sum_y3t,self.sum_y4t],[self.sum_y0b,self.sum_y1b,self.sum_y2b,self.sum_y3b,self.sum_y4b]]
        self.sum_goal_y = [[ self.sum_x0l, self.sum_x1l,self.sum_x2l,self.sum_x3l,self.sum_x4l ],[self.sum_x0r, self.sum_x1r,self.sum_x2r,self.sum_x3r,self.sum_x4r]]

        for btns in self.gameboard:
            for btn in btns:
                btn.setStyleSheet("background-color: rgb(19, 148, 23);\n""color: rgb(255, 255, 255);")
        self.sum_check()

    def close(self,app):
        """Если в диалоговом окне пользователь выбрал НЕТ"""
        app.quit()