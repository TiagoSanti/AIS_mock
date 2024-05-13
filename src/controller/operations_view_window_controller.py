import os
import cv2
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow, QFileSystemModel, QFileIconProvider
from PySide6.QtCore import QSize, QDir, QFileInfo, Qt, QFile
from PySide6.QtGui import QPixmap, QImage
from src.view.operation_views_window import Ui_MainWindow


class start_operation_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(start_operation_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Operations View")

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index("./operations"))

        # hiding unwanted columns in the tree
        self.treeView.setColumnHidden(1, True)
        self.treeView.setColumnHidden(2, True)
        self.treeView.setColumnHidden(3, True)

        self.list_model = QFileSystemModel()
        self.treeView.selectionModel().selectionChanged.connect(self.updateContentView)

    def updateContentView(self):
        self.updateListView()
        self.updateGridView()

    def updateListView(self):
        selected_index = self.treeView.currentIndex()
        selected_path = self.model.filePath(selected_index)

        self.list_model.setRootPath(selected_path)

        self.content_list_view.setModel(self.list_model)
        self.content_list_view.setRootIndex(
            self.list_model.index(selected_path))

    def updateGridView(self):
        selected_index = self.treeView.currentIndex()
        selected_path = self.model.filePath(selected_index)

        if selected_index:
            # cleaning up the layout
            for i in reversed(range(self.content_grid_layout.count())):
                widget = self.content_grid_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Listing directory items
            dir = QDir(selected_path)
            dir.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)
            items = dir.entryInfoList()

            # Creating QVBoxLayout in the grid for each item in the folder
            row = 0
            col = 0
            block_width = 150
            block_height = 150

            # Calcula o tamanho da célula no grid
            grid_item_width = block_width + self.content_grid_layout.horizontalSpacing()
            grid_item_height = block_height + self.content_grid_layout.verticalSpacing()

            # Define o tamanho fixo para cada widget no grid
            self.content_grid_layout.setColumnMinimumWidth(col, block_width)
            self.content_grid_layout.setRowMinimumHeight(row, block_height)

            for item_info in items:
                file_name = item_info.fileName()
                file_path = item_info.filePath()

                thumbnail_label = QLabel()
                thumbnail = self.generateThumbnail(file_path)
                if thumbnail:
                    thumbnail_label.setPixmap(thumbnail)
                    thumbnail_label.setScaledContents(True)
                    thumbnail_label.setMaximumSize(QSize(100, 100))

                    grid_item = QVBoxLayout()
                    grid_item.addWidget(
                        thumbnail_label, alignment=Qt.AlignCenter)

                    name_label = QLabel(file_name)
                    name_label.setAlignment(Qt.AlignHCenter)
                    grid_item.addWidget(name_label)

                    item_widget = QWidget()
                    item_widget.setLayout(grid_item)
                    item_widget.setMinimumSize(block_width, block_height)
                    item_widget.setMaximumSize(
                        block_width + grid_item_width, block_height + grid_item_height)

                    self.content_grid_layout.addWidget(item_widget, row, col)
                    col += 1
                    if col >= 3:
                        col = 0
                        row += 1

    def generateThumbnail(self, file_path):
        iconSize = 100
        image_extensions = ['png', 'jpg', 'jpeg', 'bmp', 'gif']
        video_extensions = ['mp4', 'avi', 'mkv', 'mov', 'wmv']

        file_extension = QFileInfo(file_path).suffix().lower()
        file_path = QDir.toNativeSeparators(file_path)

        if file_extension in image_extensions:
            if QFile.exists(file_path):
                pixmap = QPixmap(file_path)
                if not pixmap.isNull():
                    return pixmap.scaled(iconSize, iconSize)

        elif file_extension in video_extensions:
            # opening the video, reading the first frame
            cap = cv2.VideoCapture(file_path)
            ret, frame = cap.read()
            cap.release()

            # converting it to a pixelmap and returning it to use in the thumbnail
            if ret:
                height, width, _ = frame.shape
                qimg = QImage(frame.data, width, height, QImage.Format_BGR888)
                pixmap = QPixmap.fromImage(qimg)
                scaled_pixmap = pixmap.scaledToWidth(
                    iconSize, Qt.SmoothTransformation)
                return scaled_pixmap
            return None

        elif os.path.isdir(file_path):
            folder_icon = QFileIconProvider().icon(QFileIconProvider.Folder)
            pixmap = folder_icon.pixmap(iconSize, iconSize)
            return pixmap

        else:
            pixmap = QPixmap("./src/view/resources/images/pasta-aberta.png")
            if not pixmap.isNull():
                return pixmap.scaled(iconSize, iconSize, aspectMode=Qt.KeepAspectRatio)
