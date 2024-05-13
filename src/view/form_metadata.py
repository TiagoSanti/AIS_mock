from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import QFormLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget, QLabel, QScrollArea, QApplication, QFileDialog

class Ui_dynamic_form_metadata(object):
    def setupUi(self, dynamic_form):
        if not dynamic_form.objectName():
            dynamic_form.setObjectName(u"dynamic_form")
        dynamic_form.resize(384, 312)
        dynamic_form.setStyleSheet(u"background-color: white;\n"
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
            "#btn_discard{\n"
            "	background-color: white;\n"
            "	color: #2c88d9;\n"
            "	border:1px solid #2c88d9;\n"
            "	\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "	color: black;\n"
            "	background-color: white;\n"
            "	margin: 4px 2px;\n"
            "	padding: 1px 5px;\n"
            "	border: 1px solid #c5ced6;\n"
            "	border-radius: 4px;	\n"
            "}\n"
            """
            QScrollBar:vertical {
                background-color: #cfd8e0;
                width: 10px;
                border-radius: 5px;
                padding: 2px;
            }
            QScrollBar:vertical:hover {
                padding:0px;
            }
            QScrollBar::handle:vertical {
                background-color: #4b5c6b;
                min-height: 20px;
                border-radius: 3px;
            }
            QScrollBar::add-line:vertical {
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background-color: none;
            }
            """
            "# se tirar, quebra{}")
        self.verticalLayout = QVBoxLayout(dynamic_form)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Create a scroll area
        scroll_area = QScrollArea(dynamic_form)
        scroll_area.setWidgetResizable(True)
        scroll_area_content = QWidget(scroll_area)
        scroll_area.setWidget(scroll_area_content)

        self.formLayout = QFormLayout(scroll_area_content)
        self.formLayout.setObjectName(u"formLayout")

        self.inputs = []
        self.edit_dict = {}
        self.inputs_metadata = []
        self.metada_values = []

        self.verticalLayout.addWidget(scroll_area)

        self.buttons_frame = QWidget(dynamic_form)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_discard = QPushButton(self.buttons_frame)
        self.btn_discard.setObjectName(u"btn_discard")
        self.btn_discard.clicked.connect(dynamic_form.close)

        self.horizontalLayout.addWidget(self.btn_discard)

        self.btn_save_changes = QPushButton(self.buttons_frame)
        self.btn_save_changes.setObjectName(u"btn_save_changes")
        self.btn_save_changes.clicked.connect(dynamic_form.close)

        self.btn_add_dynamic = QPushButton(self.buttons_frame)
        self.btn_add_dynamic.setObjectName(u"btn_add_dynamic")
        self.btn_add_dynamic.clicked.connect(self.add_editable_combobox_text)

        self.horizontalLayout.addWidget(self.btn_save_changes)
        self.horizontalLayout.addWidget(self.btn_add_dynamic)
        self.verticalLayout.addWidget(self.buttons_frame)

        self.retranslateUi(dynamic_form)

        QMetaObject.connectSlotsByName(dynamic_form)

    def retranslateUi(self, dynamic_form):
        dynamic_form.setWindowTitle(QCoreApplication.translate("dynamic_form", u"Dynamic Form", None))
        self.btn_discard.setText(QCoreApplication.translate("dynamic_form", u"Discard", None))
        self.btn_add_dynamic.setText(QCoreApplication.translate("dynamic_form", u"Add Dynamic Field", None))
        self.btn_save_changes.setText(QCoreApplication.translate("dynamic_form", u"Save Changes", None))

    def add_text_line_edit(self, label_text, current_value):
        label = QLabel(label_text)
        line_edit = QLineEdit()
        if not current_value:
            current_value = "Example String"
        line_edit.setText(current_value)
        self.formLayout.addRow(label, line_edit)
        self.inputs.append(line_edit)
        self.edit_dict[label_text] = line_edit

    def add_text_combobox(self, label_text, items):
        label = QLabel(label_text)
        combobox = QComboBox()
        combobox.addItems(items)
        self.formLayout.addRow(label, combobox)
        self.inputs.append(combobox)
        self.edit_dict[label_text] = combobox

    def add_file_dialog(self, label_text):
        label = QLabel(label_text)
        line_edit = QLineEdit()
        button = QPushButton("Select Location")
        button.clicked.connect(lambda: self.get_dir_path(line_edit))
        self.formLayout.addRow(label, line_edit)
        self.formLayout.addRow(button)
        self.inputs.append(line_edit)
        self.edit_dict[label_text] = line_edit

    def get_dir_path(self, line_edit):
        dir_path = QFileDialog.getExistingDirectory()
        line_edit.setText(dir_path)


    def add_static_label(self, label_text, current_value):
        label_text = label_text + " : "
        label = QLabel(label_text)
        line_edit = QLineEdit()
        line_edit.setText(current_value)
        line_edit.setReadOnly(True)
        self.formLayout.addRow(label, line_edit)
        self.inputs.append(line_edit)

    
    def add_editable_combobox_text(self):
        combobox = QComboBox()
        line_edit = QLineEdit()
        items = self.metadata_values
        combobox.addItems(items)
        combobox.setEditable(True)
        self.formLayout.addRow(combobox, line_edit)
        self.inputs_metadata.append(combobox)
        self.inputs_metadata.append(line_edit)
        self.edit_dict[combobox] = line_edit

    def set_metadata_values(self, metadata_values):
        self.metadata_values = metadata_values

    def get_input_values(self):
        values = []
        for input_widget in self.inputs:
            values.append(input_widget.currentText() if isinstance(input_widget, QComboBox) else input_widget.text())
        return values
    
    def get_input_values_metadata(self):
        values = []
        for input_widget in self.inputs_metadata:
            values.append(input_widget.currentText() if isinstance(input_widget, QComboBox) else input_widget.text())
        return values
    
    def get_edit_dict(self):
        for key, value in self.edit_dict.items():
            self.edit_dict[key] = value.currentText() if isinstance(value, QComboBox) else value.text()
        return self.edit_dict
    
    def transform_input_values_metadata_to_dict(self):
        values = self.get_input_values_metadata()
        return dict(zip(values[::2], values[1::2]))
    