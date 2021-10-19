import sys
import pickle
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Best1 import Ui_MainWindow
from Create1 import Ui_FormCreateTask


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # подгрузим данные
        try:
            # из файла data.txt берем дату и задачи
            with open("data.txt", "rb") as f:
                self.data = pickle.load(f)
        except EOFError:
            self.data = []
        # соеденим нажатие на календарь с функцией
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        # кнопка создать
        self.pushButton.clicked.connect(self.create_task)

    def calendar_clicked(self, date):
        date = date.toPyDate()
        date_list_task = list(map(lambda x: f"{x[0]}: {x[1]}",
                                  filter(lambda t: t[0] == date, self.data)))
        print(date_list_task)
        self.listView.clear()
        self.listView.addItems(date_list_task)

    def create_task(self):
        # открываем окно для создания заданий
        self.wnd_create = CreateTaskWindow(self.data)
        self.wnd_create.show()


class CreateTaskWindow(QWidget, Ui_FormCreateTask):
    """создание задач"""
    def __init__(self, list_tasks):
        super().__init__()
        self.setupUi(self)
        self.data = list_tasks
        self.pushButton_2_create.clicked.connect(self.ok)
        self.pushButton_1_create.clicked.connect(lambda: self.hide())

    def ok(self):
        description = self.lineEdit_task_create.text()
        datetime = self.dateTimeEdit_create.date().toPyDate()
        self.data.append((datetime, description))
        with open("data.txt", "wb") as f:
            pickle.dump(self.data, f)
        self.hide()

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    wnd = TaskSystem()
    wnd.show()
    sys.exit(app.exec())


