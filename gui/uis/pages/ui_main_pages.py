# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(731, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: white; border-radius:20")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_frame = QFrame(self.frame_2)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMinimumSize(QSize(0, 160))
        self.logo_frame.setFrameShape(QFrame.NoFrame)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.logo_frame_layout = QVBoxLayout(self.logo_frame)
        self.logo_frame_layout.setSpacing(0)
        self.logo_frame_layout.setObjectName(u"logo_frame_layout")
        self.logo_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.logo_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.main_inputs_frame = QFrame(self.frame_2)
        self.main_inputs_frame.setObjectName(u"main_inputs_frame")
        self.main_inputs_frame.setMinimumSize(QSize(150, 50))
        self.main_inputs_frame.setFrameShape(QFrame.NoFrame)
        self.main_inputs_frame.setFrameShadow(QFrame.Raised)
        self.main_inputs_frame_layout = QVBoxLayout(self.main_inputs_frame)
        self.main_inputs_frame_layout.setSpacing(0)
        self.main_inputs_frame_layout.setObjectName(u"main_inputs_frame_layout")
        self.main_inputs_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.main_inputs_frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.log_in_btn_frame = QFrame(self.frame_2)
        self.log_in_btn_frame.setObjectName(u"log_in_btn_frame")
        self.log_in_btn_frame.setMinimumSize(QSize(150, 40))
        self.log_in_btn_frame.setFrameShape(QFrame.NoFrame)
        self.log_in_btn_frame.setFrameShadow(QFrame.Raised)
        self.login_frame_layout = QHBoxLayout(self.log_in_btn_frame)
        self.login_frame_layout.setSpacing(0)
        self.login_frame_layout.setObjectName(u"login_frame_layout")
        self.login_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.log_in_btn_frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.web_view_page_layout = QVBoxLayout(self.frame)
        self.web_view_page_layout.setSpacing(0)
        self.web_view_page_layout.setObjectName(u"web_view_page_layout")
        self.web_view_page_layout.setContentsMargins(0, 0, 0, 0)

        self.page_2_layout.addWidget(self.frame)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.MS_ST_add_student_label = QLabel(self.page_3)
        self.MS_ST_add_student_label.setObjectName(u"MS_ST_add_student_label")
        font1 = QFont()
        font1.setPointSize(14)
        self.MS_ST_add_student_label.setFont(font1)

        self.horizontalLayout_50.addWidget(self.MS_ST_add_student_label)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_45)


        self.verticalLayout_49.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.MS_ST_add_student_full_name = QLabel(self.page_3)
        self.MS_ST_add_student_full_name.setObjectName(u"MS_ST_add_student_full_name")

        self.horizontalLayout_51.addWidget(self.MS_ST_add_student_full_name)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_42)

        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(150, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.ms_st_full_name_entry_layout = QHBoxLayout(self.frame_3)
        self.ms_st_full_name_entry_layout.setSpacing(0)
        self.ms_st_full_name_entry_layout.setObjectName(u"ms_st_full_name_entry_layout")
        self.ms_st_full_name_entry_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_51.addWidget(self.frame_3)


        self.verticalLayout_49.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.MS_ST_add_student_abc = QLabel(self.page_3)
        self.MS_ST_add_student_abc.setObjectName(u"MS_ST_add_student_abc")

        self.horizontalLayout_52.addWidget(self.MS_ST_add_student_abc)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_41)

        self.MS_ST_add_student_abc_entry = QLineEdit(self.page_3)
        self.MS_ST_add_student_abc_entry.setObjectName(u"MS_ST_add_student_abc_entry")
        self.MS_ST_add_student_abc_entry.setMaxLength(6)

        self.horizontalLayout_52.addWidget(self.MS_ST_add_student_abc_entry)

        self.horizontalLayout_52.setStretch(1, 1)

        self.verticalLayout_49.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.MS_ST_add_student_yoc = QLabel(self.page_3)
        self.MS_ST_add_student_yoc.setObjectName(u"MS_ST_add_student_yoc")

        self.horizontalLayout_53.addWidget(self.MS_ST_add_student_yoc)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_43)

        self.MS_ST_add_student_yoc_entry = QLineEdit(self.page_3)
        self.MS_ST_add_student_yoc_entry.setObjectName(u"MS_ST_add_student_yoc_entry")
        self.MS_ST_add_student_yoc_entry.setMaxLength(4)

        self.horizontalLayout_53.addWidget(self.MS_ST_add_student_yoc_entry)


        self.verticalLayout_49.addLayout(self.horizontalLayout_53)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_23)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_44)

        self.MS_ST_add_student_button = QPushButton(self.page_3)
        self.MS_ST_add_student_button.setObjectName(u"MS_ST_add_student_button")

        self.horizontalLayout_54.addWidget(self.MS_ST_add_student_button)


        self.verticalLayout_49.addLayout(self.horizontalLayout_54)


        self.verticalLayout_51.addLayout(self.verticalLayout_49)

        self.line_3 = QFrame(self.page_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_51.addWidget(self.line_3)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.MS_ST_search_trainee_label = QLabel(self.page_3)
        self.MS_ST_search_trainee_label.setObjectName(u"MS_ST_search_trainee_label")
        self.MS_ST_search_trainee_label.setFont(font1)

        self.horizontalLayout_55.addWidget(self.MS_ST_search_trainee_label)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_46)


        self.verticalLayout_50.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.MS_ST_search_trainee_fname = QLabel(self.page_3)
        self.MS_ST_search_trainee_fname.setObjectName(u"MS_ST_search_trainee_fname")

        self.horizontalLayout_56.addWidget(self.MS_ST_search_trainee_fname)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_52)

        self.MS_ST_search_trainee_fname_entry = QLineEdit(self.page_3)
        self.MS_ST_search_trainee_fname_entry.setObjectName(u"MS_ST_search_trainee_fname_entry")
        self.MS_ST_search_trainee_fname_entry.setMaxLength(100)

        self.horizontalLayout_56.addWidget(self.MS_ST_search_trainee_fname_entry)


        self.verticalLayout_50.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_47)

        self.MS_ST_search_trainee_or1 = QLabel(self.page_3)
        self.MS_ST_search_trainee_or1.setObjectName(u"MS_ST_search_trainee_or1")

        self.horizontalLayout_57.addWidget(self.MS_ST_search_trainee_or1)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_48)


        self.verticalLayout_50.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.MS_ST_search_trainee_lname = QLabel(self.page_3)
        self.MS_ST_search_trainee_lname.setObjectName(u"MS_ST_search_trainee_lname")

        self.horizontalLayout_58.addWidget(self.MS_ST_search_trainee_lname)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_53)

        self.MS_ST_search_trainee_lname_entry = QLineEdit(self.page_3)
        self.MS_ST_search_trainee_lname_entry.setObjectName(u"MS_ST_search_trainee_lname_entry")
        self.MS_ST_search_trainee_lname_entry.setMaxLength(100)

        self.horizontalLayout_58.addWidget(self.MS_ST_search_trainee_lname_entry)


        self.verticalLayout_50.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_49)

        self.MS_ST_search_trainee_or2 = QLabel(self.page_3)
        self.MS_ST_search_trainee_or2.setObjectName(u"MS_ST_search_trainee_or2")

        self.horizontalLayout_59.addWidget(self.MS_ST_search_trainee_or2)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_50)


        self.verticalLayout_50.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.MS_ST_search_trainee_abc = QLabel(self.page_3)
        self.MS_ST_search_trainee_abc.setObjectName(u"MS_ST_search_trainee_abc")

        self.horizontalLayout_60.addWidget(self.MS_ST_search_trainee_abc)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_54)

        self.MS_ST_search_trainee_abc_entry = QLineEdit(self.page_3)
        self.MS_ST_search_trainee_abc_entry.setObjectName(u"MS_ST_search_trainee_abc_entry")
        self.MS_ST_search_trainee_abc_entry.setMaxLength(6)

        self.horizontalLayout_60.addWidget(self.MS_ST_search_trainee_abc_entry)

        self.horizontalLayout_60.setStretch(1, 1)

        self.verticalLayout_50.addLayout(self.horizontalLayout_60)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_50.addItem(self.verticalSpacer_27)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_57)

        self.MS_ST_search_trainee_button = QPushButton(self.page_3)
        self.MS_ST_search_trainee_button.setObjectName(u"MS_ST_search_trainee_button")

        self.horizontalLayout_61.addWidget(self.MS_ST_search_trainee_button)


        self.verticalLayout_50.addLayout(self.horizontalLayout_61)


        self.verticalLayout_51.addLayout(self.verticalLayout_50)


        self.horizontalLayout_62.addLayout(self.verticalLayout_51)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_55)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_29)

        self.MS_ST_search_trainee_textbrowser = QTextBrowser(self.page_3)
        self.MS_ST_search_trainee_textbrowser.setObjectName(u"MS_ST_search_trainee_textbrowser")
        self.MS_ST_search_trainee_textbrowser.setStyleSheet(u"")
        self.MS_ST_search_trainee_textbrowser.setFrameShadow(QFrame.Sunken)
        self.MS_ST_search_trainee_textbrowser.setLineWidth(2)

        self.verticalLayout_48.addWidget(self.MS_ST_search_trainee_textbrowser)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_56)

        self.MS_ST_search_trainee_override_entry = QLineEdit(self.page_3)
        self.MS_ST_search_trainee_override_entry.setObjectName(u"MS_ST_search_trainee_override_entry")

        self.horizontalLayout_49.addWidget(self.MS_ST_search_trainee_override_entry)

        self.MS_ST_search_trainee_renew = QPushButton(self.page_3)
        self.MS_ST_search_trainee_renew.setObjectName(u"MS_ST_search_trainee_renew")

        self.horizontalLayout_49.addWidget(self.MS_ST_search_trainee_renew)

        self.pushButton_12 = QPushButton(self.page_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_49.addWidget(self.pushButton_12)

        self.MS_ST_search_trainee_clear = QPushButton(self.page_3)
        self.MS_ST_search_trainee_clear.setObjectName(u"MS_ST_search_trainee_clear")

        self.horizontalLayout_49.addWidget(self.MS_ST_search_trainee_clear)


        self.verticalLayout_48.addLayout(self.horizontalLayout_49)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_28)

        self.verticalLayout_48.setStretch(1, 2)

        self.horizontalLayout_62.addLayout(self.verticalLayout_48)

        self.horizontalLayout_62.setStretch(0, 1)
        self.horizontalLayout_62.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_62)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_41 = QLabel(self.page_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)

        self.verticalLayout_28.addWidget(self.label_41)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_13)

        self.main_date_label = QLabel(self.page_4)
        self.main_date_label.setObjectName(u"main_date_label")

        self.verticalLayout_28.addWidget(self.main_date_label)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.cons_label = QLabel(self.page_4)
        self.cons_label.setObjectName(u"cons_label")

        self.verticalLayout_25.addWidget(self.cons_label)

        self.item_lost_label = QLabel(self.page_4)
        self.item_lost_label.setObjectName(u"item_lost_label")

        self.verticalLayout_25.addWidget(self.item_lost_label)

        self.material_cost_label = QLabel(self.page_4)
        self.material_cost_label.setObjectName(u"material_cost_label")

        self.verticalLayout_25.addWidget(self.material_cost_label)

        self.approvals_label = QLabel(self.page_4)
        self.approvals_label.setObjectName(u"approvals_label")

        self.verticalLayout_25.addWidget(self.approvals_label)

        self.rejections_label = QLabel(self.page_4)
        self.rejections_label.setObjectName(u"rejections_label")

        self.verticalLayout_25.addWidget(self.rejections_label)

        self.total_cost_label = QLabel(self.page_4)
        self.total_cost_label.setObjectName(u"total_cost_label")

        self.verticalLayout_25.addWidget(self.total_cost_label)


        self.horizontalLayout_22.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.cons_value = QLabel(self.page_4)
        self.cons_value.setObjectName(u"cons_value")
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.cons_value.setFont(font2)

        self.verticalLayout_26.addWidget(self.cons_value)

        self.item_lost_value = QLabel(self.page_4)
        self.item_lost_value.setObjectName(u"item_lost_value")
        self.item_lost_value.setFont(font2)

        self.verticalLayout_26.addWidget(self.item_lost_value)

        self.material_cost_value = QLabel(self.page_4)
        self.material_cost_value.setObjectName(u"material_cost_value")
        self.material_cost_value.setFont(font2)

        self.verticalLayout_26.addWidget(self.material_cost_value)

        self.approvals_value = QLabel(self.page_4)
        self.approvals_value.setObjectName(u"approvals_value")
        self.approvals_value.setFont(font2)

        self.verticalLayout_26.addWidget(self.approvals_value)

        self.rejections_value = QLabel(self.page_4)
        self.rejections_value.setObjectName(u"rejections_value")
        self.rejections_value.setFont(font2)

        self.verticalLayout_26.addWidget(self.rejections_value)

        self.total_cost_value = QLabel(self.page_4)
        self.total_cost_value.setObjectName(u"total_cost_value")
        self.total_cost_value.setFont(font2)

        self.verticalLayout_26.addWidget(self.total_cost_value)


        self.horizontalLayout_22.addLayout(self.verticalLayout_26)


        self.verticalLayout_28.addLayout(self.horizontalLayout_22)

        self.label_49 = QLabel(self.page_4)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_28.addWidget(self.label_49)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.n_of_items_label = QLabel(self.page_4)
        self.n_of_items_label.setObjectName(u"n_of_items_label")

        self.horizontalLayout_26.addWidget(self.n_of_items_label)

        self.current_n_of_items_value = QLabel(self.page_4)
        self.current_n_of_items_value.setObjectName(u"current_n_of_items_value")
        self.current_n_of_items_value.setFont(font2)
        self.current_n_of_items_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.current_n_of_items_value)


        self.verticalLayout_27.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.last_update_label = QLabel(self.page_4)
        self.last_update_label.setObjectName(u"last_update_label")

        self.horizontalLayout_25.addWidget(self.last_update_label)

        self.last_update_value = QLabel(self.page_4)
        self.last_update_value.setObjectName(u"last_update_value")
        self.last_update_value.setFont(font2)
        self.last_update_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.last_update_value)


        self.verticalLayout_27.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.current_staff_text_label = QLabel(self.page_4)
        self.current_staff_text_label.setObjectName(u"current_staff_text_label")

        self.horizontalLayout_23.addWidget(self.current_staff_text_label)

        self.current_staff_text_value = QLabel(self.page_4)
        self.current_staff_text_value.setObjectName(u"current_staff_text_value")
        self.current_staff_text_value.setFont(font2)
        self.current_staff_text_value.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_23.addWidget(self.current_staff_text_value)


        self.verticalLayout_27.addLayout(self.horizontalLayout_23)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_16)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_15)


        self.horizontalLayout_27.addLayout(self.verticalLayout_28)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_17)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.ms_info_label = QLabel(self.page_4)
        self.ms_info_label.setObjectName(u"ms_info_label")

        self.verticalLayout_31.addWidget(self.ms_info_label)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.cost_of_running_label = QLabel(self.page_4)
        self.cost_of_running_label.setObjectName(u"cost_of_running_label")

        self.verticalLayout_29.addWidget(self.cost_of_running_label)

        self.revenue_label = QLabel(self.page_4)
        self.revenue_label.setObjectName(u"revenue_label")

        self.verticalLayout_29.addWidget(self.revenue_label)

        self.num_staff_label = QLabel(self.page_4)
        self.num_staff_label.setObjectName(u"num_staff_label")

        self.verticalLayout_29.addWidget(self.num_staff_label)

        self.num_stud_workers_label = QLabel(self.page_4)
        self.num_stud_workers_label.setObjectName(u"num_stud_workers_label")

        self.verticalLayout_29.addWidget(self.num_stud_workers_label)

        self.num_volunteers_label = QLabel(self.page_4)
        self.num_volunteers_label.setObjectName(u"num_volunteers_label")

        self.verticalLayout_29.addWidget(self.num_volunteers_label)


        self.horizontalLayout_24.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.cost_of_running_value = QLabel(self.page_4)
        self.cost_of_running_value.setObjectName(u"cost_of_running_value")
        self.cost_of_running_value.setFont(font2)

        self.verticalLayout_30.addWidget(self.cost_of_running_value)

        self.revenue_value = QLabel(self.page_4)
        self.revenue_value.setObjectName(u"revenue_value")
        self.revenue_value.setFont(font2)

        self.verticalLayout_30.addWidget(self.revenue_value)

        self.num_staff_value = QLabel(self.page_4)
        self.num_staff_value.setObjectName(u"num_staff_value")
        self.num_staff_value.setFont(font2)

        self.verticalLayout_30.addWidget(self.num_staff_value)

        self.num_stud_workers_value = QLabel(self.page_4)
        self.num_stud_workers_value.setObjectName(u"num_stud_workers_value")
        self.num_stud_workers_value.setFont(font2)

        self.verticalLayout_30.addWidget(self.num_stud_workers_value)

        self.num_volunteers_value = QLabel(self.page_4)
        self.num_volunteers_value.setObjectName(u"num_volunteers_value")
        self.num_volunteers_value.setFont(font2)

        self.verticalLayout_30.addWidget(self.num_volunteers_value)


        self.horizontalLayout_24.addLayout(self.verticalLayout_30)


        self.verticalLayout_31.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.next_general_inv_label = QLabel(self.page_4)
        self.next_general_inv_label.setObjectName(u"next_general_inv_label")

        self.horizontalLayout_21.addWidget(self.next_general_inv_label)

        self.next_general_inv_value = QLabel(self.page_4)
        self.next_general_inv_value.setObjectName(u"next_general_inv_value")
        self.next_general_inv_value.setFont(font2)

        self.horizontalLayout_21.addWidget(self.next_general_inv_value)


        self.verticalLayout_31.addLayout(self.horizontalLayout_21)


        self.verticalLayout_33.addLayout(self.verticalLayout_31)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_14)


        self.horizontalLayout_27.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_20)

        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(300, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_27)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.search_inventory_title = QLabel(self.page_5)
        self.search_inventory_title.setObjectName(u"search_inventory_title")
        self.search_inventory_title.setFont(font1)

        self.verticalLayout_8.addWidget(self.search_inventory_title)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.search_inventory_type = QComboBox(self.page_5)
        self.search_inventory_type.setObjectName(u"search_inventory_type")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.search_inventory_type.setFont(font3)

        self.horizontalLayout_5.addWidget(self.search_inventory_type)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.search_checkbox_keyword_as = QCheckBox(self.page_5)
        self.search_checkbox_keyword_as.setObjectName(u"search_checkbox_keyword_as")
        self.search_checkbox_keyword_as.setFont(font2)
        self.search_checkbox_keyword_as.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.search_checkbox_keyword_as)

        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.search_as_user = QLabel(self.page_5)
        self.search_as_user.setObjectName(u"search_as_user")
        self.search_as_user.setFont(font2)

        self.horizontalLayout_5.addWidget(self.search_as_user)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(3, 2)
        self.horizontalLayout_5.setStretch(4, 1)
        self.horizontalLayout_5.setStretch(5, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.search_number_of_entries = QSpinBox(self.page_5)
        self.search_number_of_entries.setObjectName(u"search_number_of_entries")
        self.search_number_of_entries.setFont(font3)
        self.search_number_of_entries.setMinimum(1)
        self.search_number_of_entries.setMaximum(10)
        self.search_number_of_entries.setValue(5)

        self.horizontalLayout_6.addWidget(self.search_number_of_entries)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.search_checkbox_return_summary = QCheckBox(self.page_5)
        self.search_checkbox_return_summary.setObjectName(u"search_checkbox_return_summary")
        self.search_checkbox_return_summary.setFont(font2)
        self.search_checkbox_return_summary.setChecked(True)

        self.horizontalLayout_6.addWidget(self.search_checkbox_return_summary)

        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.search_access = QLabel(self.page_5)
        self.search_access.setObjectName(u"search_access")
        self.search_access.setFont(font2)

        self.horizontalLayout_6.addWidget(self.search_access)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(3, 2)
        self.horizontalLayout_6.setStretch(4, 1)
        self.horizontalLayout_6.setStretch(5, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.search_keyword = QLineEdit(self.page_5)
        self.search_keyword.setObjectName(u"search_keyword")
        self.search_keyword.setFont(font)

        self.horizontalLayout_7.addWidget(self.search_keyword)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.search_checkbox_best_fit = QCheckBox(self.page_5)
        self.search_checkbox_best_fit.setObjectName(u"search_checkbox_best_fit")
        self.search_checkbox_best_fit.setFont(font2)

        self.horizontalLayout_7.addWidget(self.search_checkbox_best_fit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.search_button = QPushButton(self.page_5)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setFont(font)

        self.verticalLayout_8.addWidget(self.search_button)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.search_display_table = QTableWidget(self.page_5)
        if (self.search_display_table.columnCount() < 6):
            self.search_display_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.search_display_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.search_display_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.search_display_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.search_display_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.search_display_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.search_display_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.search_display_table.setObjectName(u"search_display_table")
        font5 = QFont()
        font5.setFamily(u"Adobe Devanagari")
        font5.setPointSize(11)
        self.search_display_table.setFont(font5)
        self.search_display_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.search_display_table.setRowCount(0)

        self.verticalLayout_8.addWidget(self.search_display_table)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)
        self.verticalLayout_8.setStretch(3, 2)
        self.verticalLayout_8.setStretch(4, 1)
        self.verticalLayout_8.setStretch(5, 2)
        self.verticalLayout_8.setStretch(6, 1)
        self.verticalLayout_8.setStretch(7, 12)

        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_18 = QVBoxLayout(self.page_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.page_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.update_part_id = QLineEdit(self.page_6)
        self.update_part_id.setObjectName(u"update_part_id")
        self.update_part_id.setFont(font3)

        self.horizontalLayout_8.addWidget(self.update_part_id)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_11 = QLabel(self.page_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.update_resulting_part_name = QLabel(self.page_6)
        self.update_resulting_part_name.setObjectName(u"update_resulting_part_name")
        self.update_resulting_part_name.setFont(font2)

        self.horizontalLayout_8.addWidget(self.update_resulting_part_name)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.update_veriffy_button = QPushButton(self.page_6)
        self.update_veriffy_button.setObjectName(u"update_veriffy_button")
        self.update_veriffy_button.setFont(font3)

        self.horizontalLayout_9.addWidget(self.update_veriffy_button)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.update_show_entries_button = QPushButton(self.page_6)
        self.update_show_entries_button.setObjectName(u"update_show_entries_button")
        self.update_show_entries_button.setFont(font3)

        self.horizontalLayout_10.addWidget(self.update_show_entries_button)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_33 = QLabel(self.page_6)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_12.addWidget(self.label_33)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_34 = QLabel(self.page_6)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_12.addWidget(self.label_34)

        self.update_entry_override = QLineEdit(self.page_6)
        self.update_entry_override.setObjectName(u"update_entry_override")
        self.update_entry_override.setFont(font3)

        self.horizontalLayout_12.addWidget(self.update_entry_override)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.update_activate_button = QPushButton(self.page_6)
        self.update_activate_button.setObjectName(u"update_activate_button")
        self.update_activate_button.setFont(font)

        self.horizontalLayout_13.addWidget(self.update_activate_button)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.update_admin_label = QLabel(self.page_6)
        self.update_admin_label.setObjectName(u"update_admin_label")

        self.horizontalLayout_14.addWidget(self.update_admin_label)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_11.addLayout(self.verticalLayout_12)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_4 = QFrame(self.page_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.update_label_1 = QLabel(self.frame_4)
        self.update_label_1.setObjectName(u"update_label_1")
        self.update_label_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_1)

        self.update_label_2 = QLabel(self.frame_4)
        self.update_label_2.setObjectName(u"update_label_2")
        self.update_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_2)

        self.update_label_3 = QLabel(self.frame_4)
        self.update_label_3.setObjectName(u"update_label_3")
        self.update_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_3)

        self.update_label_4 = QLabel(self.frame_4)
        self.update_label_4.setObjectName(u"update_label_4")
        self.update_label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_4)

        self.update_label_5 = QLabel(self.frame_4)
        self.update_label_5.setObjectName(u"update_label_5")
        self.update_label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_5)

        self.update_label_6 = QLabel(self.frame_4)
        self.update_label_6.setObjectName(u"update_label_6")
        self.update_label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_6)

        self.update_label_7 = QLabel(self.frame_4)
        self.update_label_7.setObjectName(u"update_label_7")
        self.update_label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_7)

        self.update_label_8 = QLabel(self.frame_4)
        self.update_label_8.setObjectName(u"update_label_8")
        self.update_label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_8)

        self.update_label_9 = QLabel(self.frame_4)
        self.update_label_9.setObjectName(u"update_label_9")
        self.update_label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.update_label_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.update_entry_1 = QLineEdit(self.frame_4)
        self.update_entry_1.setObjectName(u"update_entry_1")
        self.update_entry_1.setFont(font2)
        self.update_entry_1.setLayoutDirection(Qt.LeftToRight)
        self.update_entry_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_1)

        self.update_entry_2 = QLineEdit(self.frame_4)
        self.update_entry_2.setObjectName(u"update_entry_2")
        self.update_entry_2.setFont(font2)
        self.update_entry_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_2)

        self.update_entry_3 = QLineEdit(self.frame_4)
        self.update_entry_3.setObjectName(u"update_entry_3")
        self.update_entry_3.setFont(font2)
        self.update_entry_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_3)

        self.update_entry_4 = QLineEdit(self.frame_4)
        self.update_entry_4.setObjectName(u"update_entry_4")
        self.update_entry_4.setFont(font2)
        self.update_entry_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_4)

        self.update_entry_5 = QLineEdit(self.frame_4)
        self.update_entry_5.setObjectName(u"update_entry_5")
        self.update_entry_5.setFont(font2)
        self.update_entry_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_5)

        self.update_entry_6 = QLineEdit(self.frame_4)
        self.update_entry_6.setObjectName(u"update_entry_6")
        self.update_entry_6.setFont(font2)
        self.update_entry_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_6)

        self.update_entry_7 = QLineEdit(self.frame_4)
        self.update_entry_7.setObjectName(u"update_entry_7")
        self.update_entry_7.setFont(font2)
        self.update_entry_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_7)

        self.update_entry_8 = QLineEdit(self.frame_4)
        self.update_entry_8.setObjectName(u"update_entry_8")
        self.update_entry_8.setFont(font2)
        self.update_entry_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_8)

        self.update_entry_9 = QLineEdit(self.frame_4)
        self.update_entry_9.setObjectName(u"update_entry_9")
        self.update_entry_9.setFont(font2)
        self.update_entry_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.update_entry_9)

        self.verticalSpacer_20 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_20)


        self.horizontalLayout_16.addLayout(self.verticalLayout_11)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.update_label_10 = QLabel(self.frame_4)
        self.update_label_10.setObjectName(u"update_label_10")
        self.update_label_10.setEnabled(True)
        self.update_label_10.setMinimumSize(QSize(0, 25))
        self.update_label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_10)

        self.update_label_11 = QLabel(self.frame_4)
        self.update_label_11.setObjectName(u"update_label_11")
        self.update_label_11.setMinimumSize(QSize(0, 25))
        self.update_label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_11)

        self.update_label_12 = QLabel(self.frame_4)
        self.update_label_12.setObjectName(u"update_label_12")
        self.update_label_12.setMinimumSize(QSize(0, 25))
        self.update_label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_12)

        self.update_label_13 = QLabel(self.frame_4)
        self.update_label_13.setObjectName(u"update_label_13")
        self.update_label_13.setMinimumSize(QSize(0, 25))
        self.update_label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_13)

        self.update_label_14 = QLabel(self.frame_4)
        self.update_label_14.setObjectName(u"update_label_14")
        self.update_label_14.setMinimumSize(QSize(0, 25))
        self.update_label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_14)

        self.update_label_15 = QLabel(self.frame_4)
        self.update_label_15.setObjectName(u"update_label_15")
        self.update_label_15.setEnabled(True)
        self.update_label_15.setMinimumSize(QSize(0, 25))
        self.update_label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_15)

        self.update_label_16 = QLabel(self.frame_4)
        self.update_label_16.setObjectName(u"update_label_16")
        self.update_label_16.setMinimumSize(QSize(0, 25))
        self.update_label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_16)

        self.update_label_17 = QLabel(self.frame_4)
        self.update_label_17.setObjectName(u"update_label_17")
        self.update_label_17.setMinimumSize(QSize(0, 25))
        self.update_label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_17)

        self.update_label_18 = QLabel(self.frame_4)
        self.update_label_18.setObjectName(u"update_label_18")
        self.update_label_18.setMinimumSize(QSize(0, 25))
        self.update_label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.update_label_18)

        self.verticalSpacer_19 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_19)


        self.horizontalLayout_16.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.update_entry_10 = QLineEdit(self.frame_4)
        self.update_entry_10.setObjectName(u"update_entry_10")
        self.update_entry_10.setFont(font2)
        self.update_entry_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_10)

        self.update_entry_11 = QLineEdit(self.frame_4)
        self.update_entry_11.setObjectName(u"update_entry_11")
        self.update_entry_11.setFont(font2)
        self.update_entry_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_11)

        self.update_entry_12 = QLineEdit(self.frame_4)
        self.update_entry_12.setObjectName(u"update_entry_12")
        self.update_entry_12.setFont(font2)
        self.update_entry_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_12)

        self.update_entry_13 = QLineEdit(self.frame_4)
        self.update_entry_13.setObjectName(u"update_entry_13")
        self.update_entry_13.setFont(font2)
        self.update_entry_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_13)

        self.update_entry_14 = QLineEdit(self.frame_4)
        self.update_entry_14.setObjectName(u"update_entry_14")
        self.update_entry_14.setFont(font2)
        self.update_entry_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_14)

        self.update_entry_15 = QLineEdit(self.frame_4)
        self.update_entry_15.setObjectName(u"update_entry_15")
        self.update_entry_15.setFont(font2)
        self.update_entry_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_15)

        self.update_entry_16 = QLineEdit(self.frame_4)
        self.update_entry_16.setObjectName(u"update_entry_16")
        self.update_entry_16.setFont(font2)
        self.update_entry_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_16)

        self.update_entry_17 = QLineEdit(self.frame_4)
        self.update_entry_17.setObjectName(u"update_entry_17")
        self.update_entry_17.setFont(font2)
        self.update_entry_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_17)

        self.update_entry_18 = QLineEdit(self.frame_4)
        self.update_entry_18.setObjectName(u"update_entry_18")
        self.update_entry_18.setFont(font2)
        self.update_entry_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.update_entry_18)

        self.verticalSpacer_18 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_18)


        self.horizontalLayout_16.addLayout(self.verticalLayout_17)

        self.update_send_button = QPushButton(self.frame_4)
        self.update_send_button.setObjectName(u"update_send_button")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.update_send_button.setFont(font6)

        self.horizontalLayout_16.addWidget(self.update_send_button)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_15.addWidget(self.frame_4)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)

        self.pages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_19 = QVBoxLayout(self.page_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(False)

        self.horizontalLayout_32.addWidget(self.label_13)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_25)


        self.verticalLayout_37.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_14 = QLabel(self.page_7)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_33.addWidget(self.label_14)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_26)

        self.choose_item_cat_inv = QComboBox(self.page_7)
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.addItem("")
        self.choose_item_cat_inv.setObjectName(u"choose_item_cat_inv")
        self.choose_item_cat_inv.setFont(font3)

        self.horizontalLayout_33.addWidget(self.choose_item_cat_inv)

        self.inventory_append_cs = QComboBox(self.page_7)
        self.inventory_append_cs.addItem("")
        self.inventory_append_cs.addItem("")
        self.inventory_append_cs.setObjectName(u"inventory_append_cs")
        self.inventory_append_cs.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_append_cs.sizePolicy().hasHeightForWidth())
        self.inventory_append_cs.setSizePolicy(sizePolicy)
        self.inventory_append_cs.setFont(font3)

        self.horizontalLayout_33.addWidget(self.inventory_append_cs)


        self.verticalLayout_37.addLayout(self.horizontalLayout_33)

        self.label_15 = QLabel(self.page_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(False)

        self.verticalLayout_37.addWidget(self.label_15)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_16 = QLabel(self.page_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(False)

        self.horizontalLayout_34.addWidget(self.label_16)

        self.lineEdit = QLineEdit(self.page_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setFont(font3)
        self.lineEdit.setMaxLength(2)

        self.horizontalLayout_34.addWidget(self.lineEdit)

        self.horizontalSpacer_28 = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_28)


        self.verticalLayout_37.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_29)

        self.see_custom_button_inv = QPushButton(self.page_7)
        self.see_custom_button_inv.setObjectName(u"see_custom_button_inv")
        self.see_custom_button_inv.setEnabled(False)
        self.see_custom_button_inv.setFont(font3)

        self.horizontalLayout_35.addWidget(self.see_custom_button_inv)


        self.verticalLayout_37.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_30)


        self.verticalLayout_37.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_31)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.pushButton_4 = QPushButton(self.page_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font3)

        self.verticalLayout_36.addWidget(self.pushButton_4)


        self.horizontalLayout_37.addLayout(self.verticalLayout_36)


        self.verticalLayout_37.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_32)

        self.pushButton_3 = QPushButton(self.page_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setFont(font3)

        self.horizontalLayout_38.addWidget(self.pushButton_3)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_40)

        self.pushButton_8 = QPushButton(self.page_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setFont(font3)

        self.horizontalLayout_38.addWidget(self.pushButton_8)

        self.horizontalLayout_38.setStretch(0, 1)

        self.verticalLayout_37.addLayout(self.horizontalLayout_38)


        self.horizontalLayout_47.addLayout(self.verticalLayout_37)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_38)


        self.verticalLayout_45.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_20 = QLabel(self.page_7)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_38.addWidget(self.label_20)

        self.label_21 = QLabel(self.page_7)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_38.addWidget(self.label_21)

        self.label_22 = QLabel(self.page_7)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_38.addWidget(self.label_22)

        self.label_23 = QLabel(self.page_7)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_38.addWidget(self.label_23)

        self.label_24 = QLabel(self.page_7)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_38.addWidget(self.label_24)

        self.label_25 = QLabel(self.page_7)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_38.addWidget(self.label_25)

        self.label_26 = QLabel(self.page_7)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_38.addWidget(self.label_26)


        self.horizontalLayout_39.addLayout(self.verticalLayout_38)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.lineEdit_9 = QLineEdit(self.page_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.page_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.page_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.page_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.page_7)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.page_7)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.page_7)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setEnabled(False)

        self.verticalLayout_41.addWidget(self.lineEdit_15)


        self.horizontalLayout_39.addLayout(self.verticalLayout_41)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_27 = QLabel(self.page_7)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_40.addWidget(self.label_27)

        self.label_28 = QLabel(self.page_7)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_40.addWidget(self.label_28)

        self.label_29 = QLabel(self.page_7)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_40.addWidget(self.label_29)

        self.label_30 = QLabel(self.page_7)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_40.addWidget(self.label_30)

        self.label_31 = QLabel(self.page_7)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_40.addWidget(self.label_31)

        self.label_32 = QLabel(self.page_7)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_40.addWidget(self.label_32)

        self.label_35 = QLabel(self.page_7)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_40.addWidget(self.label_35)


        self.horizontalLayout_39.addLayout(self.verticalLayout_40)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.lineEdit_2 = QLineEdit(self.page_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.page_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.page_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.page_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.page_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.page_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.page_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(False)

        self.verticalLayout_39.addWidget(self.lineEdit_8)


        self.horizontalLayout_39.addLayout(self.verticalLayout_39)


        self.horizontalLayout_46.addLayout(self.horizontalLayout_39)


        self.verticalLayout_45.addLayout(self.horizontalLayout_46)


        self.horizontalLayout_48.addLayout(self.verticalLayout_45)

        self.horizontalSpacer_39 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_39)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_17 = QLabel(self.page_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)

        self.verticalLayout_34.addWidget(self.label_17)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_21)

        self.check_last_inv_id = QPushButton(self.page_7)
        self.check_last_inv_id.setObjectName(u"check_last_inv_id")
        self.check_last_inv_id.setFont(font3)

        self.horizontalLayout_28.addWidget(self.check_last_inv_id)


        self.verticalLayout_34.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_30.addLayout(self.verticalLayout_34)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_22)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_21)

        self.last_inv_id_label = QLabel(self.page_7)
        self.last_inv_id_label.setObjectName(u"last_inv_id_label")
        self.last_inv_id_label.setFont(font3)

        self.verticalLayout_35.addWidget(self.last_inv_id_label)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_22)


        self.horizontalLayout_29.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_23)


        self.horizontalLayout_30.addLayout(self.horizontalLayout_29)


        self.verticalLayout_44.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_25 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_25)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_50 = QLabel(self.page_7)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_31.addWidget(self.label_50)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_24)

        self.label_51 = QLabel(self.page_7)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font3)

        self.horizontalLayout_31.addWidget(self.label_51)


        self.verticalLayout_44.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_26)

        self.frame_6 = QFrame(self.page_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_42.addWidget(self.label_19)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_36)

        self.label_52 = QLabel(self.frame_6)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_45.addWidget(self.label_52)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_37)


        self.verticalLayout_42.addLayout(self.horizontalLayout_45)

        self.verticalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_24)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_53 = QLabel(self.frame_6)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_43.addWidget(self.label_53)

        self.comboBox_2 = QComboBox(self.frame_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font3)

        self.horizontalLayout_43.addWidget(self.comboBox_2)


        self.verticalLayout_42.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_33)

        self.search_file_append_inv = QPushButton(self.frame_6)
        self.search_file_append_inv.setObjectName(u"search_file_append_inv")
        self.search_file_append_inv.setFont(font3)

        self.horizontalLayout_42.addWidget(self.search_file_append_inv)


        self.verticalLayout_42.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_54 = QLabel(self.frame_6)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_44.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_6)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)

        self.horizontalLayout_44.addWidget(self.label_55)


        self.verticalLayout_42.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_34)

        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font3)

        self.horizontalLayout_41.addWidget(self.pushButton_6)


        self.verticalLayout_42.addLayout(self.horizontalLayout_41)

        self.progressBar = QProgressBar(self.frame_6)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_42.addWidget(self.progressBar)

        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_42.addWidget(self.checkBox)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_35)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font3)

        self.horizontalLayout_40.addWidget(self.pushButton_7)


        self.verticalLayout_42.addLayout(self.horizontalLayout_40)

        self.verticalLayout_42.setStretch(9, 1)

        self.verticalLayout_43.addLayout(self.verticalLayout_42)


        self.verticalLayout_44.addWidget(self.frame_6)

        self.verticalLayout_44.setStretch(4, 1)

        self.horizontalLayout_48.addLayout(self.verticalLayout_44)


        self.verticalLayout_19.addLayout(self.horizontalLayout_48)

        self.pages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_23 = QVBoxLayout(self.page_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_36 = QLabel(self.page_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_36)

        self.approve_table = QTableWidget(self.page_8)
        if (self.approve_table.columnCount() < 5):
            self.approve_table.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.approve_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.approve_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.approve_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.approve_table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.approve_table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.approve_table.setObjectName(u"approve_table")
        self.approve_table.setFont(font5)
        self.approve_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.approve_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.approve_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.approve_table.setAutoScrollMargin(16)
        self.approve_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.approve_table.setWordWrap(False)
        self.approve_table.setRowCount(0)
        self.approve_table.setColumnCount(5)
        self.approve_table.horizontalHeader().setVisible(False)
        self.approve_table.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_21.addWidget(self.approve_table)

        self.refresh_approvals_inventory_button = QPushButton(self.page_8)
        self.refresh_approvals_inventory_button.setObjectName(u"refresh_approvals_inventory_button")
        self.refresh_approvals_inventory_button.setFont(font2)

        self.verticalLayout_21.addWidget(self.refresh_approvals_inventory_button)


        self.horizontalLayout_17.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_18 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_18)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_8)

        self.label_37 = QLabel(self.page_8)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_22.addWidget(self.label_37)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_38 = QLabel(self.page_8)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_18.addWidget(self.label_38)

        self.approve_entry_request_id = QLineEdit(self.page_8)
        self.approve_entry_request_id.setObjectName(u"approve_entry_request_id")
        self.approve_entry_request_id.setFont(font3)

        self.horizontalLayout_18.addWidget(self.approve_entry_request_id)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.approve_open_button = QPushButton(self.page_8)
        self.approve_open_button.setObjectName(u"approve_open_button")
        self.approve_open_button.setFont(font3)

        self.horizontalLayout_19.addWidget(self.approve_open_button)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_17.addLayout(self.verticalLayout_22)

        self.horizontalLayout_17.setStretch(0, 10)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_20.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_7)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_39 = QLabel(self.page_8)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_20.addWidget(self.label_39)

        self.label_40 = QLabel(self.page_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_40)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_27)

        self.approve_checkbox_confirm = QCheckBox(self.page_8)
        self.approve_checkbox_confirm.setObjectName(u"approve_checkbox_confirm")

        self.horizontalLayout_20.addWidget(self.approve_checkbox_confirm)

        self.approve_inventory_clear_button = QPushButton(self.page_8)
        self.approve_inventory_clear_button.setObjectName(u"approve_inventory_clear_button")
        self.approve_inventory_clear_button.setFont(font)

        self.horizontalLayout_20.addWidget(self.approve_inventory_clear_button)

        self.approve_confirm_button = QPushButton(self.page_8)
        self.approve_confirm_button.setObjectName(u"approve_confirm_button")
        self.approve_confirm_button.setFont(font)

        self.horizontalLayout_20.addWidget(self.approve_confirm_button)

        self.approve_deny_button = QPushButton(self.page_8)
        self.approve_deny_button.setObjectName(u"approve_deny_button")
        self.approve_deny_button.setFont(font3)

        self.horizontalLayout_20.addWidget(self.approve_deny_button)


        self.verticalLayout_20.addLayout(self.horizontalLayout_20)

        self.approve_text_display = QTextEdit(self.page_8)
        self.approve_text_display.setObjectName(u"approve_text_display")
        self.approve_text_display.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.approve_text_display)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(3, 1)

        self.verticalLayout_23.addLayout(self.verticalLayout_20)

        self.pages.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_47 = QVBoxLayout(self.page_9)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_69 = QLabel(self.page_9)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font1)

        self.verticalLayout_46.addWidget(self.label_69)

        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_9)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_76 = QLabel(self.page_9)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_64.addWidget(self.label_76)

        self.denied_choose_request_id = QComboBox(self.page_9)
        self.denied_choose_request_id.setObjectName(u"denied_choose_request_id")
        self.denied_choose_request_id.setFont(font3)

        self.horizontalLayout_64.addWidget(self.denied_choose_request_id)


        self.verticalLayout_46.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_51)

        self.denied_veiw_button = QPushButton(self.page_9)
        self.denied_veiw_button.setObjectName(u"denied_veiw_button")
        self.denied_veiw_button.setFont(font3)

        self.horizontalLayout_65.addWidget(self.denied_veiw_button)


        self.verticalLayout_46.addLayout(self.horizontalLayout_65)


        self.horizontalLayout_63.addLayout(self.verticalLayout_46)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_58)


        self.verticalLayout_32.addLayout(self.horizontalLayout_63)

        self.verticalSpacer_10 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_10)


        self.verticalLayout_24.addLayout(self.verticalLayout_32)

        self.denied_text_display_2 = QTextBrowser(self.page_9)
        self.denied_text_display_2.setObjectName(u"denied_text_display_2")

        self.verticalLayout_24.addWidget(self.denied_text_display_2)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_59)

        self.denied_delete_button = QPushButton(self.page_9)
        self.denied_delete_button.setObjectName(u"denied_delete_button")
        self.denied_delete_button.setFont(font)

        self.horizontalLayout_66.addWidget(self.denied_delete_button)


        self.verticalLayout_24.addLayout(self.horizontalLayout_66)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_11)


        self.verticalLayout_47.addLayout(self.verticalLayout_24)

        self.pages.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.welcome_image_logout_layout = QVBoxLayout(self.page_10)
        self.welcome_image_logout_layout.setSpacing(0)
        self.welcome_image_logout_layout.setObjectName(u"welcome_image_logout_layout")
        self.welcome_image_logout_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.page_10)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome to the Makerspace App!", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Password", None))
        self.MS_ST_add_student_label.setText(QCoreApplication.translate("MainPages", u"Add New Student", None))
        self.MS_ST_add_student_full_name.setText(QCoreApplication.translate("MainPages", u"Full Name", None))
        self.MS_ST_add_student_abc.setText(QCoreApplication.translate("MainPages", u"abc123", None))
        self.MS_ST_add_student_yoc.setText(QCoreApplication.translate("MainPages", u"Year of Conmpletion", None))
        self.MS_ST_add_student_button.setText(QCoreApplication.translate("MainPages", u"Add", None))
        self.MS_ST_search_trainee_label.setText(QCoreApplication.translate("MainPages", u"Search Trainee", None))
        self.MS_ST_search_trainee_fname.setText(QCoreApplication.translate("MainPages", u"First Name", None))
        self.MS_ST_search_trainee_or1.setText(QCoreApplication.translate("MainPages", u"or", None))
        self.MS_ST_search_trainee_lname.setText(QCoreApplication.translate("MainPages", u"Last Name", None))
        self.MS_ST_search_trainee_or2.setText(QCoreApplication.translate("MainPages", u"or", None))
        self.MS_ST_search_trainee_abc.setText(QCoreApplication.translate("MainPages", u"abc123", None))
        self.MS_ST_search_trainee_button.setText(QCoreApplication.translate("MainPages", u"Search", None))
        self.MS_ST_search_trainee_textbrowser.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">Machine Shop - Safety Training Record </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:60"
                        "0;\">For: __name__</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">With student ID: __abc123__</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">The sudent has (hasn't) been safety trained within</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">the last 2 years.</span></p>\n"
"<p style=\"-qt"
                        "-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">RowdyMaker: T/F</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">Maker Level:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">Write OXSDR and click renew to extend this student's</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">safety training record another year.</span></p></body></html>", None))
        self.MS_ST_search_trainee_renew.setText(QCoreApplication.translate("MainPages", u"Renew", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainPages", u"Edit Record", None))
        self.MS_ST_search_trainee_clear.setText(QCoreApplication.translate("MainPages", u"Clear", None))
        self.label_41.setText(QCoreApplication.translate("MainPages", u"Inventory Overview", None))
        self.main_date_label.setText(QCoreApplication.translate("MainPages", u"Week of November 16, 2020", None))
        self.cons_label.setText(QCoreApplication.translate("MainPages", u"Consumables Used:", None))
        self.item_lost_label.setText(QCoreApplication.translate("MainPages", u"Items Lost:", None))
        self.material_cost_label.setText(QCoreApplication.translate("MainPages", u"Material Cost:", None))
        self.approvals_label.setText(QCoreApplication.translate("MainPages", u"Approvals:", None))
        self.rejections_label.setText(QCoreApplication.translate("MainPages", u"Rejections:", None))
        self.total_cost_label.setText(QCoreApplication.translate("MainPages", u"Total Cost:", None))
        self.cons_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.item_lost_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.material_cost_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.approvals_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.rejections_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.total_cost_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_49.setText(QCoreApplication.translate("MainPages", u"Inventory Information", None))
        self.n_of_items_label.setText(QCoreApplication.translate("MainPages", u"Number of Items:", None))
#if QT_CONFIG(accessibility)
        self.current_n_of_items_value.setAccessibleDescription(QCoreApplication.translate("MainPages", u"0", None))
#endif // QT_CONFIG(accessibility)
        self.current_n_of_items_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.last_update_label.setText(QCoreApplication.translate("MainPages", u"Last Updated on:", None))
        self.last_update_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.current_staff_text_label.setText(QCoreApplication.translate("MainPages", u"Current Staff Admnistrators:", None))
        self.current_staff_text_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.ms_info_label.setText(QCoreApplication.translate("MainPages", u"Makerspace Information", None))
        self.cost_of_running_label.setText(QCoreApplication.translate("MainPages", u"Cost of running:", None))
        self.revenue_label.setText(QCoreApplication.translate("MainPages", u"Revenue:", None))
        self.num_staff_label.setText(QCoreApplication.translate("MainPages", u"Staff Members:", None))
        self.num_stud_workers_label.setText(QCoreApplication.translate("MainPages", u"Student Workers:", None))
        self.num_volunteers_label.setText(QCoreApplication.translate("MainPages", u"Volunteers:", None))
        self.cost_of_running_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.revenue_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.num_staff_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.num_stud_workers_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.num_volunteers_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.next_general_inv_label.setText(QCoreApplication.translate("MainPages", u"Next General Inventory:", None))
        self.next_general_inv_value.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.search_inventory_title.setText(QCoreApplication.translate("MainPages", u"Search Inventory", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Inventory Type", None))
        self.search_inventory_type.setCurrentText("")
        self.search_checkbox_keyword_as.setText(QCoreApplication.translate("MainPages", u"Keyword as Part ID", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Running Search as:", None))
        self.search_as_user.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Number of  Entries", None))
        self.search_checkbox_return_summary.setText(QCoreApplication.translate("MainPages", u"Return Summary Results", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Access Level", None))
        self.search_access.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Keyword", None))
        self.search_checkbox_best_fit.setText(QCoreApplication.translate("MainPages", u"Return Best Fit Item", None))
        self.search_button.setText(QCoreApplication.translate("MainPages", u"Search", None))
        ___qtablewidgetitem = self.search_display_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainPages", u"Part ID", None));
        ___qtablewidgetitem1 = self.search_display_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainPages", u"Name", None));
        ___qtablewidgetitem2 = self.search_display_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainPages", u"Location", None));
        ___qtablewidgetitem3 = self.search_display_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainPages", u"Quantity", None));
        ___qtablewidgetitem4 = self.search_display_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainPages", u"Available", None));
        ___qtablewidgetitem5 = self.search_display_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainPages", u"Who has it", None));
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Update Inventory Based on Part ID", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"Part ID", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"Part Name:", None))
        self.update_resulting_part_name.setText("")
        self.label_12.setText(QCoreApplication.translate("MainPages", u"Updating as:", None))
        self.update_veriffy_button.setText(QCoreApplication.translate("MainPages", u"Verify", None))
        self.update_show_entries_button.setText(QCoreApplication.translate("MainPages", u"Show Entries", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"Approve as Admin", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"Admin Override:", None))
        self.update_activate_button.setText(QCoreApplication.translate("MainPages", u"Activate", None))
        self.update_admin_label.setText(QCoreApplication.translate("MainPages", u"Updating as Admin", None))
        self.update_label_1.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_2.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_3.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_4.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_5.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_6.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_7.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_8.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_9.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_10.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_11.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_12.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_13.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_14.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_15.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_16.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_17.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_label_18.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.update_send_button.setText(QCoreApplication.translate("MainPages", u"Send Update", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"Select Part ID", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"Choose Part / Item Category", None))
        self.choose_item_cat_inv.setItemText(0, QCoreApplication.translate("MainPages", u"Power Tool", None))
        self.choose_item_cat_inv.setItemText(1, QCoreApplication.translate("MainPages", u"3D Printing", None))
        self.choose_item_cat_inv.setItemText(2, QCoreApplication.translate("MainPages", u"Hand Tool", None))
        self.choose_item_cat_inv.setItemText(3, QCoreApplication.translate("MainPages", u"Clamp Tool", None))
        self.choose_item_cat_inv.setItemText(4, QCoreApplication.translate("MainPages", u"Measuring Tool", None))
        self.choose_item_cat_inv.setItemText(5, QCoreApplication.translate("MainPages", u"Drill Bits", None))
        self.choose_item_cat_inv.setItemText(6, QCoreApplication.translate("MainPages", u"Tap and Die", None))
        self.choose_item_cat_inv.setItemText(7, QCoreApplication.translate("MainPages", u"Tool Cart", None))
        self.choose_item_cat_inv.setItemText(8, QCoreApplication.translate("MainPages", u"Soldering", None))
        self.choose_item_cat_inv.setItemText(9, QCoreApplication.translate("MainPages", u"Desktop Computer", None))
        self.choose_item_cat_inv.setItemText(10, QCoreApplication.translate("MainPages", u"Office Supply", None))
        self.choose_item_cat_inv.setItemText(11, QCoreApplication.translate("MainPages", u"Non Groupable Item", None))

        self.inventory_append_cs.setItemText(0, QCoreApplication.translate("MainPages", u"Stationary Item", None))
        self.inventory_append_cs.setItemText(1, QCoreApplication.translate("MainPages", u"Consumable", None))

        self.label_15.setText(QCoreApplication.translate("MainPages", u"If required - For Non Groupable Items set custom ID", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"\"AB\":", None))
        self.see_custom_button_inv.setText(QCoreApplication.translate("MainPages", u"See Current Custom ID's", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPages", u"Use", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPages", u"Set Entries", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainPages", u"Submit to Inventory", None))
        self.label_20.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_24.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_26.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_29.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_31.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"Unused", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u"Check Previous Part ID", None))
        self.check_last_inv_id.setText(QCoreApplication.translate("MainPages", u"Check", None))
        self.last_inv_id_label.setText(QCoreApplication.translate("MainPages", u"Part Id", None))
        self.label_50.setText(QCoreApplication.translate("MainPages", u"Part ID to be used:", None))
        self.label_51.setText(QCoreApplication.translate("MainPages", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainPages", u"Append multiple parts / items", None))
        self.label_52.setText(QCoreApplication.translate("MainPages", u"from file", None))
        self.label_53.setText(QCoreApplication.translate("MainPages", u"Type of file:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainPages", u"CSV", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainPages", u"Formated Excel", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainPages", u"Json", None))

        self.search_file_append_inv.setText(QCoreApplication.translate("MainPages", u"Search File", None))
        self.label_54.setText(QCoreApplication.translate("MainPages", u"File to use:", None))
        self.label_55.setText(QCoreApplication.translate("MainPages", u"Filename.csv", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainPages", u"Check File", None))
        self.checkBox.setText(QCoreApplication.translate("MainPages", u"File is ready to be submitted", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainPages", u"Submit to Inventory", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"Current Inventory Updates Submitted", None))
        ___qtablewidgetitem6 = self.approve_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainPages", u"Request ID", None));
        ___qtablewidgetitem7 = self.approve_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainPages", u"Date Submitted", None));
        ___qtablewidgetitem8 = self.approve_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainPages", u"Submitted By", None));
        ___qtablewidgetitem9 = self.approve_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainPages", u"Line Update Count", None));
        ___qtablewidgetitem10 = self.approve_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainPages", u"Reviewed", None));
        self.refresh_approvals_inventory_button.setText(QCoreApplication.translate("MainPages", u"Refresh", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"Review", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"Request ID", None))
        self.approve_open_button.setText(QCoreApplication.translate("MainPages", u"Open", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"Request ID:", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.approve_checkbox_confirm.setText(QCoreApplication.translate("MainPages", u"I have reviewed and confirmed the validity of this update", None))
        self.approve_inventory_clear_button.setText(QCoreApplication.translate("MainPages", u"Clear", None))
        self.approve_confirm_button.setText(QCoreApplication.translate("MainPages", u"Confirm Update", None))
        self.approve_deny_button.setText(QCoreApplication.translate("MainPages", u"Deny Update", None))
        self.approve_text_display.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:14pt; font-weight:600;\">Entrie Submitted for Approval</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainPages", u"Current Denied Updates", None))
        self.label_76.setText(QCoreApplication.translate("MainPages", u"Request ID:", None))
        self.denied_veiw_button.setText(QCoreApplication.translate("MainPages", u"View Request", None))
        self.denied_delete_button.setText(QCoreApplication.translate("MainPages", u"Delete", None))
    # retranslateUi

