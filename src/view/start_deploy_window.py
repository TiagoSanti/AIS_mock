# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_deploy_window.ui'
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
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from . import images_rc

class Ui_start_deploy_window(object):
    def setupUi(self, start_deploy_window):
        if not start_deploy_window.objectName():
            start_deploy_window.setObjectName(u"start_deploy_window")
        start_deploy_window.resize(498, 700)
        start_deploy_window.setStyleSheet(u"	background-color: white;\n"
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
"	background-color: #4b5c6b;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	padding: 7px 9px;\n"
"	padding-bottom: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #c5ced6;\n"
"	color: black;\n"
"}\n"
"\n"
"#bnt_Start_Deploy {\n"
"	height: 40px;\n"
"}\n"
"\n"
"# image_label{\n"
"	margin-top: 4px;\n"
"	border-radius: 93%;\n"
"}")
        self.centralwidget = QWidget(start_deploy_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_middle = QFrame(self.centralwidget)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_middle)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_image = QFrame(self.frame_middle)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setMaximumSize(QSize(210, 300))
        self.frame_image.setAutoFillBackground(False)
        self.frame_image.setStyleSheet(u"")
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_image)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_label = QLabel(self.frame_image)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMaximumSize(QSize(200, 220))
        self.image_label.setStyleSheet(u"")
        self.image_label.setPixmap(QPixmap(u":/images/pf_logo.png"))
        self.image_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.image_label)


        self.horizontalLayout.addWidget(self.frame_image)


        self.verticalLayout.addWidget(self.frame_middle)

        self.frame_botton = QFrame(self.centralwidget)
        self.frame_botton.setObjectName(u"frame_botton")
        self.frame_botton.setFrameShape(QFrame.StyledPanel)
        self.frame_botton.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_botton)
        self.gridLayout.setObjectName(u"gridLayout")
        self.operation_drop = QComboBox(self.frame_botton)
        self.operation_drop.addItem("")
        self.operation_drop.setObjectName(u"operation_drop")
        self.operation_drop.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.operation_drop, 0, 0, 1, 1)

        self.operationPlus_btn = QPushButton(self.frame_botton)
        self.operationPlus_btn.setObjectName(u"operationPlus_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operationPlus_btn.sizePolicy().hasHeightForWidth())
        self.operationPlus_btn.setSizePolicy(sizePolicy)
        self.operationPlus_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.operationPlus_btn, 0, 1, 1, 1)

        self.operator_drop = QComboBox(self.frame_botton)
        self.operator_drop.addItem("")
        self.operator_drop.setObjectName(u"operator_drop")
        self.operator_drop.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.operator_drop, 1, 0, 1, 1)

        self.operatorPlus_btn = QPushButton(self.frame_botton)
        self.operatorPlus_btn.setObjectName(u"operatorPlus_btn")
        sizePolicy.setHeightForWidth(self.operatorPlus_btn.sizePolicy().hasHeightForWidth())
        self.operatorPlus_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.operatorPlus_btn, 1, 1, 1, 1)

        self.persona_drop = QComboBox(self.frame_botton)
        self.persona_drop.addItem("")
        self.persona_drop.setObjectName(u"persona_drop")
        self.persona_drop.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.persona_drop, 2, 0, 1, 1)

        self.personnaPlus_btn = QPushButton(self.frame_botton)
        self.personnaPlus_btn.setObjectName(u"personnaPlus_btn")
        sizePolicy.setHeightForWidth(self.personnaPlus_btn.sizePolicy().hasHeightForWidth())
        self.personnaPlus_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.personnaPlus_btn, 2, 1, 1, 1)

        self.profile_drop = QComboBox(self.frame_botton)
        self.profile_drop.addItem("")
        self.profile_drop.setObjectName(u"profile_drop")
        self.profile_drop.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.profile_drop, 3, 0, 1, 1)

        self.profilePlus_btn = QPushButton(self.frame_botton)
        self.profilePlus_btn.setObjectName(u"profilePlus_btn")
        sizePolicy.setHeightForWidth(self.profilePlus_btn.sizePolicy().hasHeightForWidth())
        self.profilePlus_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.profilePlus_btn, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_botton)

        self.bnt_Start_Deploy = QPushButton(self.centralwidget)
        self.bnt_Start_Deploy.setObjectName(u"bnt_Start_Deploy")
        self.bnt_Start_Deploy.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_Start_Deploy.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.bnt_Start_Deploy)

        start_deploy_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(start_deploy_window)

        QMetaObject.connectSlotsByName(start_deploy_window)
    # setupUi

    def retranslateUi(self, start_deploy_window):
        start_deploy_window.setWindowTitle(QCoreApplication.translate("start_deploy_window", u"MainWindow", None))
        self.image_label.setText("")
        self.operation_drop.setItemText(0, QCoreApplication.translate("start_deploy_window", u"Select Operation", None))

        self.operationPlus_btn.setText(QCoreApplication.translate("start_deploy_window", u"+", None))
        self.operator_drop.setItemText(0, QCoreApplication.translate("start_deploy_window", u"Select Operator", None))

        self.operatorPlus_btn.setText(QCoreApplication.translate("start_deploy_window", u"+", None))
        self.persona_drop.setItemText(0, QCoreApplication.translate("start_deploy_window", u"Select Persona", None))

        self.personnaPlus_btn.setText(QCoreApplication.translate("start_deploy_window", u"+", None))
        self.profile_drop.setItemText(0, QCoreApplication.translate("start_deploy_window", u"Select Profile", None))

        self.profilePlus_btn.setText(QCoreApplication.translate("start_deploy_window", u"+", None))
        self.bnt_Start_Deploy.setText(QCoreApplication.translate("start_deploy_window", u"Start Deploy", None))
    # retranslateUi

