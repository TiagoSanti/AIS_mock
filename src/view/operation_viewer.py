# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metadata_viewer_window_operation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_OperationMetadataViewer(object):
    def setupUi(self, OperationMetadataViewer):
        if not OperationMetadataViewer.objectName():
            OperationMetadataViewer.setObjectName(u"OperationMetadataViewer")
        OperationMetadataViewer.resize(699, 800)
        OperationMetadataViewer.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	border: 1px solid #c3cfd9;\n"
"}\n"
"\n"
"QComboBox {\n"
"	color: black;\n"
"	background-color: white;\n"
"	font-size: 16px;\n"
"	margin: 4px 2px;\n"
"	padding: 1px 5px;\n"
"	border: 1px solid #c5ced6;\n"
"	border-radius: 4px;	\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #c5ced6;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	background-color: #2c88d9;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #c5ced6;\n"
"	color: black;\n"
"}\n"
"\n"
"#edit_operationbtn{\n"
"	background-color: white;\n"
"	color: #2c88d9;\n"
"	border:1px solid #2c88d9;\n"
"	\n"
"}\n"
"\n"
"#btn_remove_dynamic {\n"
"	background-color: #d3455b;\n"
"}\n"
"\n"
"#delete_btn {\n"
"	background-color: #d3455b;\n"
"}\n"
"\n"
"#discard_changes_btn {\n"
"	background-color: white;\n"
"	color: #2c88d9;\n"
"	border:1px s"
                        "olid #2c88d9;\n"
"	\n"
"}\n"
"\n"
"# se tirar, quebra{}")
        self.centralwidget = QWidget(OperationMetadataViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image_frame = QFrame(self.centralwidget)
        self.image_frame.setObjectName(u"image_frame")
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.image_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.imagel_label = QLabel(self.image_frame)
        self.imagel_label.setObjectName(u"imagel_label")
        self.imagel_label.setPixmap(QPixmap(u"../../../../../../Downloads/WhatsApp Image 2024-04-22 at 16.11.44.jpeg"))
        self.imagel_label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.imagel_label, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.image_frame)

        self.static_frame = QFrame(self.centralwidget)
        self.static_frame.setObjectName(u"static_frame")
        self.static_frame.setMaximumSize(QSize(839, 308))
        self.static_frame.setFrameShape(QFrame.StyledPanel)
        self.static_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.static_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.static_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.static_label = QLabel(self.frame)
        self.static_label.setObjectName(u"static_label")

        self.verticalLayout_3.addWidget(self.static_label)

        self.static_table = QTableWidget(self.frame)
        self.static_table.setObjectName(u"static_table")

        self.verticalLayout_3.addWidget(self.static_table)


        self.gridLayout.addWidget(self.frame, 3, 0, 1, 6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.new_operationbtn = QPushButton(self.static_frame)
        self.new_operationbtn.setObjectName(u"new_operationbtn")

        self.gridLayout.addWidget(self.new_operationbtn, 1, 4, 1, 1)

        self.static_dropdown = QComboBox(self.static_frame)
        self.static_dropdown.setObjectName(u"static_dropdown")
        self.static_dropdown.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.static_dropdown.setIconSize(QSize(35, 35))
        self.static_dropdown.setDuplicatesEnabled(True)

        self.gridLayout.addWidget(self.static_dropdown, 1, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.static_frame)

        self.dynamic_frame = QFrame(self.centralwidget)
        self.dynamic_frame.setObjectName(u"dynamic_frame")
        self.dynamic_frame.setFrameShape(QFrame.StyledPanel)
        self.dynamic_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.dynamic_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.dynamic_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dynamic_label = QLabel(self.frame_2)
        self.dynamic_label.setObjectName(u"dynamic_label")

        self.verticalLayout_4.addWidget(self.dynamic_label)

        self.dynamic_table = QTableWidget(self.frame_2)
        self.dynamic_table.setObjectName(u"dynamic_table")

        self.verticalLayout_4.addWidget(self.dynamic_table)


        self.horizontalLayout.addWidget(self.frame_2)

        self.button_dynamic_frame = QFrame(self.dynamic_frame)
        self.button_dynamic_frame.setObjectName(u"button_dynamic_frame")
        self.button_dynamic_frame.setFrameShape(QFrame.StyledPanel)
        self.button_dynamic_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.button_dynamic_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.btn_add_dynamic = QPushButton(self.button_dynamic_frame)
        self.btn_add_dynamic.setObjectName(u"btn_add_dynamic")

        self.verticalLayout_2.addWidget(self.btn_add_dynamic)

        self.btn_remove_dynamic = QPushButton(self.button_dynamic_frame)
        self.btn_remove_dynamic.setObjectName(u"btn_remove_dynamic")

        self.verticalLayout_2.addWidget(self.btn_remove_dynamic)

        self.edit_operationbtn = QPushButton(self.button_dynamic_frame)
        self.edit_operationbtn.setObjectName(u"edit_operationbtn")

        self.verticalLayout_2.addWidget(self.edit_operationbtn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.button_dynamic_frame)


        self.verticalLayout.addWidget(self.dynamic_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.delete_btn = QPushButton(self.bottom_frame)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.discard_changes_btn = QPushButton(self.bottom_frame)
        self.discard_changes_btn.setObjectName(u"discard_changes_btn")

        self.horizontalLayout_3.addWidget(self.discard_changes_btn)

        self.savechanges_btn = QPushButton(self.bottom_frame)
        self.savechanges_btn.setObjectName(u"savechanges_btn")

        self.horizontalLayout_3.addWidget(self.savechanges_btn)


        self.verticalLayout.addWidget(self.bottom_frame)

        OperationMetadataViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(OperationMetadataViewer)

        QMetaObject.connectSlotsByName(OperationMetadataViewer)
    # setupUi

    def retranslateUi(self, OperationMetadataViewer):
        OperationMetadataViewer.setWindowTitle(QCoreApplication.translate("OperationMetadataViewer", u"MainWindow", None))
        self.imagel_label.setText("")
        self.static_label.setText(QCoreApplication.translate("OperationMetadataViewer", u"Static Proprieties", None))
        self.new_operationbtn.setText(QCoreApplication.translate("OperationMetadataViewer", u"New Operation", None))
        self.dynamic_label.setText(QCoreApplication.translate("OperationMetadataViewer", u"Dynamic Proprieties", None))
        self.btn_add_dynamic.setText(QCoreApplication.translate("OperationMetadataViewer", u"add", None))
        self.btn_remove_dynamic.setText(QCoreApplication.translate("OperationMetadataViewer", u"remove", None))
        self.edit_operationbtn.setText(QCoreApplication.translate("OperationMetadataViewer", u"Edit operation", None))
        self.delete_btn.setText(QCoreApplication.translate("OperationMetadataViewer", u"Delete Operation", None))
        self.discard_changes_btn.setText(QCoreApplication.translate("OperationMetadataViewer", u"Discard", None))
        self.savechanges_btn.setText(QCoreApplication.translate("OperationMetadataViewer", u"Save", None))
    # retranslateUi

