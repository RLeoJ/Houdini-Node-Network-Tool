from PySide2 import QtWidgets, QtCore
from Qt import QtCompat
import hou

try:
    from pathlib import Path
except:
    from pathlib2 import Path

ui_path = Path(__file__).parent / 'qt' / 'window.ui'

# from UI import ui_path

class ToolWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)

        self.create_tree()

        self.fileButton.clicked.connect(self.set_path)
        self.generateButton.clicked.connect(self.set_generation)

    def create_tree(self):
        filter = ["*.abc"]

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))

        self.model.setNameFilters(filter)
        self.model.setNameFilterDisables(False)

        self.fileTree.setModel(self.model)

    def set_path(self):
        self.box = QtWidgets.QFileDialog
        self.select = self.box.getExistingDirectory()
        text = self.fileLine
        text.setText(self.select)
        self.fileTree.setRootIndex(self.model.index(self.select))

    def set_generation(self):
        # Get the paths of selected files
        items = self.fileTree.selectedIndexes()
        paths = [i.model().filePath(i) for i in items]

        node = hou.node('/obj')
        geo = node.createNode('geo')
        merge = geo.createNode('merge')

        # For each file selected, create a node, set path parameter and plug into merge node.
        for i in paths:
            alembic = geo.createNode('alembic')
            alembic.parm('fileName').set(i)
            alembic.setFirstInput(merge)
            alembic.moveToGoodPosition()





def run():
    app = QtWidgets.QApplication([])
    tw = ToolWindow()
    tw.show()
    app.exec_()


if __name__ == '__main__':
    run()
