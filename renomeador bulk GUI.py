import os
import re

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self). __init__()
        self.filtroEdit = QStandardItemModel
        self.selecionarView = QStandardItemModel()
        self.listView = QStandardItemModel()
        self.listModel = QStandardItemModel()
        uic.loadUi('renomeador bulk.ui', self)
        self.show()


        self.directory = "."
        self.listModel = QStandardItemModel()
        self.selectModel = QStandardItemModel()
        self.selectedIndexes = QStandardItemModel()

        self.selecionarView.setModel(self.selectModel)
        self.selected = []

        self.actionAbrir.triggered.connect(self.load_directory)
        self.filtroButton.clicked.connect(self.filer_list)
        self.selecionarButton.clicked.connect(self.choose_selection)
        self.removerButton.clicked.connect(self.removeAction)
        self.aplicarButton.clicked.connect(self.rename_files)


    def load_directory(self):
        try:
            self.selected = []
            self.selectModel.clear()
            self.listModel.clear()
            self.directory = QFileDialog.getExistingDirectory(self, "Escolher Diretório")
            if self.directory:
                for file in os.listdir(self.directory):
                    if os.path.isfile(os.path.join(self.directory, file)):
                        self.listModel.appendRow(QStandardItem(file))
            for file in os.listdir(self.directory):
                 if os.path.isfile(os.path.join(self.directory, file)):
                     self.listModel.appendRow(QStandardItem(file))
            self.listView.setModel(self.listModel)


        except Exception as e:
            print(e)




    def rename_files(self):
        counter = 1
        for filename in self.selected:
            if self.addPrefixRadio.isChecked():
                os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, self.nameEdit.text() + filename))
            elif self.removePrefixRadio.isChecked():
                if filename.startswith(self.nameEdit.text()):
                    os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, self.filename[len(self.nameEdit.text()):]))
            elif self.addSufixoRadio.isChecked():
                filetype = filename.split('.')[-1]
                os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, filename[:-(len(filetype) +1)] + self.nameEdit.text() + "." + filetype))
            elif self.removeSufixoRadio.isChecked():
                filetype = filename.split('.')[-1]
                if filename.endswith(self.nameEdit.text() + "." + filetype):
                   os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, filename[:-len(self.nameEdit.text() + '.' + filetype)] + "." + filetype))
            elif self.novoNomeRadio.isChecked():
                filetype = filename.split('.')[-1]
                os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, self.nameEdit.text() + str(counter) + "." + filetype))
                counter += 1
            else:
                print("Selecione entre Prefixo, Sufixo ou Novo Nome")

            self.selected = []
            self.selectModel.clear()
            self.listModel.clear()

            for file in os.listdir(self.directory):
                if os.path.isfile(os.path.join(self.directory, file)):
                    self.listModel.appendRow(QStandardItem(file))
            self.listView.setModel(self.listModel)











    def choose_selection(self):
        try:
         if len(self.listView.selectedIndexes()) != 0:
                for index in self.listView.selectedIndexes():
                    if index.data() not in self.selected:
                        self.selected.append(index.data())
                        self.selectModel.appendRow(QStandardItem(index.data()))
        except Exception as e:
            print(e)

    def remove_selection(self):
        try:
            if len(self.selecionarView.selectedIndexes()) != 0:
                for index in reversed(sorted(self.selecionarView.selectedIndexes())):
                    self.selected.remove(index.data())
                    self.selectModel.removeRow(index.row())
        except Exception as e:
            print(e)

    def removeAction(self):
        self.remove_selection()

    def filer_list(self):
        self.selectModel.clear()
        self.selected = []
        for index in range(self.listModel.rowCount()):
            item = self.listModel.item(index)
            if re.match(self.filtroEdit().text(), item.text()):
                self.selectModel.appendRow(QStandardItem(item.text()))
                self.selected.append(item.text)




app = QApplication([])
window = MyGUI()
app.exec_()