# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operation_views_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QListView, QMainWindow, QScrollArea,
    QSizePolicy, QTabWidget, QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1168, 547)
        MainWindow.setStyleSheet(u"	background-color: white;\n"
"	color: black;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color: #cfd8e0;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"QScrollBar:vertical:hover {\n"
"	padding:0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4b5c6b;\n"
"    min-height: 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"	QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background-color: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	background-color: #cfd8e0;\n"
"	height: 10px;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"QScrollBar:horizontal:hover {\n"
"	padding:0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #4b5c6b;\n"
"	min-width: 20px;\n"
"	border-r"
                        "adius: 3px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background-color: none;\n"
"}\n"
"\n"
"# se tirar isso quebra")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filters_tab = QTabWidget(self.centralwidget)
        self.filters_tab.setObjectName(u"filters_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters_tab.sizePolicy().hasHeightForWidth())
        self.filters_tab.setSizePolicy(sizePolicy)
        self.filters_tab.setMinimumSize(QSize(320, 0))
        self.filters_tab.setMaximumSize(QSize(400, 16777215))
        self.filters_tab.setStyleSheet(u"")
        self.filters_tab.setTabPosition(QTabWidget.South)
        self.filters_tab.setTabShape(QTabWidget.Rounded)
        self.Filter = QWidget()
        self.Filter.setObjectName(u"Filter")
        self.filters_tab.addTab(self.Filter, "")
        self.Search = QWidget()
        self.Search.setObjectName(u"Search")
        self.filters_tab.addTab(self.Search, "")
        self.Bookmarks = QWidget()
        self.Bookmarks.setObjectName(u"Bookmarks")
        self.filters_tab.addTab(self.Bookmarks, "")
        self.Deployments = QWidget()
        self.Deployments.setObjectName(u"Deployments")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Deployments.sizePolicy().hasHeightForWidth())
        self.Deployments.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.Deployments)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(self.Deployments)
        self.treeView.setObjectName(u"treeView")
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QSize(300, 0))

        self.horizontalLayout.addWidget(self.treeView)

        self.filters_tab.addTab(self.Deployments, "")

        self.horizontalLayout_2.addWidget(self.filters_tab)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(550, 0))
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.grid_tab = QWidget()
        self.grid_tab.setObjectName(u"grid_tab")
        self.grid_tab.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.grid_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.grid_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 524, 484))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.content_grid_layout = QGridLayout()
        self.content_grid_layout.setObjectName(u"content_grid_layout")

        self.gridLayout_3.addLayout(self.content_grid_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.grid_tab, "")
        self.list_tab = QWidget()
        self.list_tab.setObjectName(u"list_tab")
        self.gridLayout_4 = QGridLayout(self.list_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.content_list_view = QListView(self.list_tab)
        self.content_list_view.setObjectName(u"content_list_view")

        self.gridLayout_4.addWidget(self.content_list_view, 0, 0, 2, 2)

        self.tabWidget.addTab(self.list_tab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.metadata_frame = QFrame(self.centralwidget)
        self.metadata_frame.setObjectName(u"metadata_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.metadata_frame.sizePolicy().hasHeightForWidth())
        self.metadata_frame.setSizePolicy(sizePolicy3)
        self.metadata_frame.setMinimumSize(QSize(250, 0))
        self.metadata_frame.setMaximumSize(QSize(300, 16777215))
        self.metadata_frame.setStyleSheet(u"")
        self.metadata_frame.setFrameShape(QFrame.StyledPanel)
        self.metadata_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.metadata_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.filters_tab.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filters_tab.setTabText(self.filters_tab.indexOf(self.Filter), QCoreApplication.translate("MainWindow", u"Filter", None))
        self.filters_tab.setTabText(self.filters_tab.indexOf(self.Search), QCoreApplication.translate("MainWindow", u"Search", None))
        self.filters_tab.setTabText(self.filters_tab.indexOf(self.Bookmarks), QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        self.filters_tab.setTabText(self.filters_tab.indexOf(self.Deployments), QCoreApplication.translate("MainWindow", u"Deployments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.grid_tab), QCoreApplication.translate("MainWindow", u"Thumbnails", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.list_tab), QCoreApplication.translate("MainWindow", u"Grid", None))
    # retranslateUi

