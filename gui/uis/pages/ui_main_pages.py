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
        MainPages.resize(969, 661)
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

        self.text_main_makerspace = QLabel(self.frame_2)
        self.text_main_makerspace.setObjectName(u"text_main_makerspace")
        font = QFont()
        font.setPointSize(10)
        self.text_main_makerspace.setFont(font)

        self.horizontalLayout.addWidget(self.text_main_makerspace)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_main_username = QLabel(self.frame_2)
        self.text_main_username.setObjectName(u"text_main_username")
        self.text_main_username.setMinimumSize(QSize(150, 0))
        self.text_main_username.setFont(font)
        self.text_main_username.setLayoutDirection(Qt.LeftToRight)
        self.text_main_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text_main_username)

        self.text_main_username_2 = QLabel(self.frame_2)
        self.text_main_username_2.setObjectName(u"text_main_username_2")
        self.text_main_username_2.setMinimumSize(QSize(150, 0))
        self.text_main_username_2.setFont(font)
        self.text_main_username_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text_main_username_2)


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

        self.ms_st_abc123_entry_layout = QHBoxLayout()
        self.ms_st_abc123_entry_layout.setObjectName(u"ms_st_abc123_entry_layout")
        self.MS_ST_add_student_abc = QLabel(self.page_3)
        self.MS_ST_add_student_abc.setObjectName(u"MS_ST_add_student_abc")

        self.ms_st_abc123_entry_layout.addWidget(self.MS_ST_add_student_abc)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ms_st_abc123_entry_layout.addItem(self.horizontalSpacer_41)

        self.frame_7 = QFrame(self.page_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.ms_st_abc123_entry = QHBoxLayout(self.frame_7)
        self.ms_st_abc123_entry.setSpacing(0)
        self.ms_st_abc123_entry.setObjectName(u"ms_st_abc123_entry")
        self.ms_st_abc123_entry.setContentsMargins(0, 0, 0, 0)

        self.ms_st_abc123_entry_layout.addWidget(self.frame_7)

        self.ms_st_abc123_entry_layout.setStretch(1, 1)

        self.verticalLayout_49.addLayout(self.ms_st_abc123_entry_layout)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.MS_ST_add_student_yoc = QLabel(self.page_3)
        self.MS_ST_add_student_yoc.setObjectName(u"MS_ST_add_student_yoc")

        self.horizontalLayout_53.addWidget(self.MS_ST_add_student_yoc)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_43)

        self.frame_8 = QFrame(self.page_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.ms_st_year_completed_entry = QHBoxLayout(self.frame_8)
        self.ms_st_year_completed_entry.setSpacing(0)
        self.ms_st_year_completed_entry.setObjectName(u"ms_st_year_completed_entry")
        self.ms_st_year_completed_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_53.addWidget(self.frame_8)


        self.verticalLayout_49.addLayout(self.horizontalLayout_53)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_23)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_44)

        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(100, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.ms_st_add_button = QHBoxLayout(self.frame_13)
        self.ms_st_add_button.setSpacing(0)
        self.ms_st_add_button.setObjectName(u"ms_st_add_button")
        self.ms_st_add_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_54.addWidget(self.frame_13)


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

        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(150, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.ms_st_search_fname_entry = QHBoxLayout(self.frame_9)
        self.ms_st_search_fname_entry.setSpacing(0)
        self.ms_st_search_fname_entry.setObjectName(u"ms_st_search_fname_entry")
        self.ms_st_search_fname_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_56.addWidget(self.frame_9)


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

        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(150, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.ms_st_search_lname_entry = QHBoxLayout(self.frame_10)
        self.ms_st_search_lname_entry.setSpacing(0)
        self.ms_st_search_lname_entry.setObjectName(u"ms_st_search_lname_entry")
        self.ms_st_search_lname_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_58.addWidget(self.frame_10)


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

        self.frame_11 = QFrame(self.page_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(150, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.ms_st_search_abc123_entry = QHBoxLayout(self.frame_11)
        self.ms_st_search_abc123_entry.setSpacing(0)
        self.ms_st_search_abc123_entry.setObjectName(u"ms_st_search_abc123_entry")
        self.ms_st_search_abc123_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_60.addWidget(self.frame_11)

        self.horizontalLayout_60.setStretch(1, 1)

        self.verticalLayout_50.addLayout(self.horizontalLayout_60)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_50.addItem(self.verticalSpacer_27)

        self.ms_st_search_button = QHBoxLayout()
        self.ms_st_search_button.setSpacing(0)
        self.ms_st_search_button.setObjectName(u"ms_st_search_button")
        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ms_st_search_button.addItem(self.horizontalSpacer_57)

        self.frame_14 = QFrame(self.page_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(100, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)

        self.ms_st_search_button.addWidget(self.frame_14)


        self.verticalLayout_50.addLayout(self.ms_st_search_button)


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

        self.frame_12 = QFrame(self.page_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.ms_st_renew_entry = QHBoxLayout(self.frame_12)
        self.ms_st_renew_entry.setSpacing(0)
        self.ms_st_renew_entry.setObjectName(u"ms_st_renew_entry")
        self.ms_st_renew_entry.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(150, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.ms_st_renew_edit_clear_buttons = QHBoxLayout(self.frame_15)
        self.ms_st_renew_edit_clear_buttons.setSpacing(0)
        self.ms_st_renew_edit_clear_buttons.setObjectName(u"ms_st_renew_edit_clear_buttons")
        self.ms_st_renew_edit_clear_buttons.setContentsMargins(0, 0, 0, 0)

        self.ms_st_renew_entry.addWidget(self.frame_15)


        self.horizontalLayout_49.addWidget(self.frame_12)


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

        self.frame_53 = QFrame(self.page_5)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(150, 0))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.ms_inv_invtype_dropdown = QHBoxLayout(self.frame_53)
        self.ms_inv_invtype_dropdown.setSpacing(0)
        self.ms_inv_invtype_dropdown.setObjectName(u"ms_inv_invtype_dropdown")
        self.ms_inv_invtype_dropdown.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_53)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.search_checkbox_keyword_as = QCheckBox(self.page_5)
        self.search_checkbox_keyword_as.setObjectName(u"search_checkbox_keyword_as")
        self.search_checkbox_keyword_as.setFont(font2)
        self.search_checkbox_keyword_as.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.search_checkbox_keyword_as)

        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.search_as_user = QLabel(self.page_5)
        self.search_as_user.setObjectName(u"search_as_user")
        self.search_as_user.setFont(font2)

        self.horizontalLayout_5.addWidget(self.search_as_user)

        self.horizontalLayout_5.setStretch(0, 1)
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

        self.frame_17 = QFrame(self.page_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(150, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.ms_inv_numberof_entry = QHBoxLayout(self.frame_17)
        self.ms_inv_numberof_entry.setSpacing(0)
        self.ms_inv_numberof_entry.setObjectName(u"ms_inv_numberof_entry")
        self.ms_inv_numberof_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.frame_17)

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

        self.frame_16 = QFrame(self.page_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(150, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.ms_inv_keyword_entry = QHBoxLayout(self.frame_16)
        self.ms_inv_keyword_entry.setSpacing(0)
        self.ms_inv_keyword_entry.setObjectName(u"ms_inv_keyword_entry")
        self.ms_inv_keyword_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.search_checkbox_best_fit = QCheckBox(self.page_5)
        self.search_checkbox_best_fit.setObjectName(u"search_checkbox_best_fit")
        self.search_checkbox_best_fit.setFont(font2)

        self.horizontalLayout_7.addWidget(self.search_checkbox_best_fit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.frame_54 = QFrame(self.page_5)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 30))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.ms_inv_search_button = QHBoxLayout(self.frame_54)
        self.ms_inv_search_button.setSpacing(0)
        self.ms_inv_search_button.setObjectName(u"ms_inv_search_button")
        self.ms_inv_search_button.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_54)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.frame_18 = QFrame(self.page_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 350))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.ms_inv_table_ = QVBoxLayout(self.frame_18)
        self.ms_inv_table_.setSpacing(0)
        self.ms_inv_table_.setObjectName(u"ms_inv_table_")
        self.ms_inv_table_.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_18)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)
        self.verticalLayout_8.setStretch(3, 2)
        self.verticalLayout_8.setStretch(4, 1)
        self.verticalLayout_8.setStretch(6, 1)

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

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.frame_23 = QFrame(self.page_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(150, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_partid_entry = QHBoxLayout(self.frame_23)
        self.ms_upd_inv_partid_entry.setSpacing(0)
        self.ms_upd_inv_partid_entry.setObjectName(u"ms_upd_inv_partid_entry")
        self.ms_upd_inv_partid_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_23)

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

        self.frame_19 = QFrame(self.page_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(150, 0))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_verify_buttton = QHBoxLayout(self.frame_19)
        self.ms_upd_inv_verify_buttton.setSpacing(0)
        self.ms_upd_inv_verify_buttton.setObjectName(u"ms_upd_inv_verify_buttton")
        self.ms_upd_inv_verify_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_19)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.frame_20 = QFrame(self.page_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(150, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_show_entries_buttton = QHBoxLayout(self.frame_20)
        self.ms_upd_inv_show_entries_buttton.setSpacing(0)
        self.ms_upd_inv_show_entries_buttton.setObjectName(u"ms_upd_inv_show_entries_buttton")
        self.ms_upd_inv_show_entries_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.frame_20)


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

        self.frame_24 = QFrame(self.page_6)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_adminovrr_entry = QHBoxLayout(self.frame_24)
        self.ms_upd_inv_adminovrr_entry.setSpacing(0)
        self.ms_upd_inv_adminovrr_entry.setObjectName(u"ms_upd_inv_adminovrr_entry")
        self.ms_upd_inv_adminovrr_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_12.addWidget(self.frame_24)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.frame_22 = QFrame(self.page_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(150, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_send_update_buttton = QHBoxLayout(self.frame_22)
        self.ms_upd_inv_send_update_buttton.setSpacing(0)
        self.ms_upd_inv_send_update_buttton.setObjectName(u"ms_upd_inv_send_update_buttton")
        self.ms_upd_inv_send_update_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_13.addWidget(self.frame_22)


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
        self.frame_25 = QFrame(self.frame_4)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(150, 20))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_textlabel_entry = QHBoxLayout(self.frame_25)
        self.ms_upd_inv_textlabel_entry.setSpacing(0)
        self.ms_upd_inv_textlabel_entry.setObjectName(u"ms_upd_inv_textlabel_entry")
        self.ms_upd_inv_textlabel_entry.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_25)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(150, 0))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_textlabel_entry_ = QHBoxLayout(self.frame_41)
        self.ms_upd_inv_textlabel_entry_.setSpacing(0)
        self.ms_upd_inv_textlabel_entry_.setObjectName(u"ms_upd_inv_textlabel_entry_")
        self.ms_upd_inv_textlabel_entry_.setContentsMargins(0, 0, 0, 0)

        self.ms_upd_inv_textlabel_entry.addWidget(self.frame_41)


        self.verticalLayout_11.addWidget(self.frame_25)


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

        self.horizontalLayout_16.addLayout(self.verticalLayout_17)

        self.frame_42 = QFrame(self.frame_4)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(150, 0))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_textlabel_entry__2 = QHBoxLayout(self.frame_42)
        self.ms_upd_inv_textlabel_entry__2.setSpacing(0)
        self.ms_upd_inv_textlabel_entry__2.setObjectName(u"ms_upd_inv_textlabel_entry__2")
        self.ms_upd_inv_textlabel_entry__2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_16.addWidget(self.frame_42)

        self.frame_21 = QFrame(self.frame_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(150, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.ms_upd_inv_activate_buttton = QHBoxLayout(self.frame_21)
        self.ms_upd_inv_activate_buttton.setSpacing(0)
        self.ms_upd_inv_activate_buttton.setObjectName(u"ms_upd_inv_activate_buttton")
        self.ms_upd_inv_activate_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_16.addWidget(self.frame_21)


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
        self.text_partid = QLabel(self.page_7)
        self.text_partid.setObjectName(u"text_partid")
        self.text_partid.setWordWrap(False)

        self.horizontalLayout_32.addWidget(self.text_partid)

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

        self.frame_26 = QFrame(self.page_7)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(150, 0))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.ms_partid_pwrtool_buttton = QHBoxLayout(self.frame_26)
        self.ms_partid_pwrtool_buttton.setSpacing(0)
        self.ms_partid_pwrtool_buttton.setObjectName(u"ms_partid_pwrtool_buttton")
        self.ms_partid_pwrtool_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_33.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.page_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(150, 0))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.ms_partid_stationaryitem_buttton = QHBoxLayout(self.frame_27)
        self.ms_partid_stationaryitem_buttton.setSpacing(0)
        self.ms_partid_stationaryitem_buttton.setObjectName(u"ms_partid_stationaryitem_buttton")
        self.ms_partid_stationaryitem_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_33.addWidget(self.frame_27)


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

        self.frame_28 = QFrame(self.page_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(150, 0))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.ms_partid_customid_entry = QHBoxLayout(self.frame_28)
        self.ms_partid_customid_entry.setSpacing(0)
        self.ms_partid_customid_entry.setObjectName(u"ms_partid_customid_entry")
        self.ms_partid_customid_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_34.addWidget(self.frame_28)

        self.horizontalSpacer_28 = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_28)


        self.verticalLayout_37.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_29)

        self.frame_29 = QFrame(self.page_7)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(150, 0))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.ms_partid_seecurrentcustomid_buttton = QHBoxLayout(self.frame_29)
        self.ms_partid_seecurrentcustomid_buttton.setSpacing(0)
        self.ms_partid_seecurrentcustomid_buttton.setObjectName(u"ms_partid_seecurrentcustomid_buttton")
        self.ms_partid_seecurrentcustomid_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_35.addWidget(self.frame_29)


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

        self.horizontalLayout_37.addLayout(self.verticalLayout_36)

        self.frame_30 = QFrame(self.page_7)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(150, 0))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.ms_partid_use_buttton = QHBoxLayout(self.frame_30)
        self.ms_partid_use_buttton.setSpacing(0)
        self.ms_partid_use_buttton.setObjectName(u"ms_partid_use_buttton")
        self.ms_partid_use_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_37.addWidget(self.frame_30)


        self.verticalLayout_37.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_32)

        self.frame_31 = QFrame(self.page_7)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(150, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.ms_partid_setentry_buttton = QHBoxLayout(self.frame_31)
        self.ms_partid_setentry_buttton.setSpacing(0)
        self.ms_partid_setentry_buttton.setObjectName(u"ms_partid_setentry_buttton")
        self.ms_partid_setentry_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_38.addWidget(self.frame_31)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_40)

        self.frame_32 = QFrame(self.page_7)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(150, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.ms_partid_submitinvertory_buttton = QHBoxLayout(self.frame_32)
        self.ms_partid_submitinvertory_buttton.setSpacing(0)
        self.ms_partid_submitinvertory_buttton.setObjectName(u"ms_partid_submitinvertory_buttton")
        self.ms_partid_submitinvertory_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_38.addWidget(self.frame_32)

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
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")

        self.horizontalLayout_39.addLayout(self.verticalLayout_41)

        self.frame_33 = QFrame(self.page_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(200, 0))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.ms_partid_unused_entry = QVBoxLayout(self.frame_33)
        self.ms_partid_unused_entry.setSpacing(0)
        self.ms_partid_unused_entry.setObjectName(u"ms_partid_unused_entry")
        self.ms_partid_unused_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_39.addWidget(self.frame_33)

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
        self.frame_34 = QFrame(self.page_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(200, 0))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.ms_partid_unused_entry_2 = QHBoxLayout(self.frame_34)
        self.ms_partid_unused_entry_2.setSpacing(0)
        self.ms_partid_unused_entry_2.setObjectName(u"ms_partid_unused_entry_2")
        self.ms_partid_unused_entry_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_39.addWidget(self.frame_34)


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
        self.text_checkprevpartid = QLabel(self.page_7)
        self.text_checkprevpartid.setObjectName(u"text_checkprevpartid")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.text_checkprevpartid.setFont(font4)

        self.verticalLayout_34.addWidget(self.text_checkprevpartid)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_21)

        self.frame_35 = QFrame(self.page_7)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(100, 0))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.ms_partid_check_buttton = QHBoxLayout(self.frame_35)
        self.ms_partid_check_buttton.setSpacing(0)
        self.ms_partid_check_buttton.setObjectName(u"ms_partid_check_buttton")
        self.ms_partid_check_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_28.addWidget(self.frame_35)


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

        self.text_partid_2 = QLabel(self.page_7)
        self.text_partid_2.setObjectName(u"text_partid_2")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.text_partid_2.setFont(font5)

        self.verticalLayout_35.addWidget(self.text_partid_2)

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
        self.text_partidtobeused = QLabel(self.page_7)
        self.text_partidtobeused.setObjectName(u"text_partidtobeused")

        self.horizontalLayout_31.addWidget(self.text_partidtobeused)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_24)

        self.label_51 = QLabel(self.page_7)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font5)

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

        self.frame_36 = QFrame(self.frame_6)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(100, 50))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.ms_partid_csv_buttton = QHBoxLayout(self.frame_36)
        self.ms_partid_csv_buttton.setSpacing(0)
        self.ms_partid_csv_buttton.setObjectName(u"ms_partid_csv_buttton")
        self.ms_partid_csv_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_43.addWidget(self.frame_36)


        self.verticalLayout_42.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_33)

        self.frame_37 = QFrame(self.frame_6)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(150, 0))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.ms_partid_searchfile_buttton = QHBoxLayout(self.frame_37)
        self.ms_partid_searchfile_buttton.setSpacing(0)
        self.ms_partid_searchfile_buttton.setObjectName(u"ms_partid_searchfile_buttton")
        self.ms_partid_searchfile_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_42.addWidget(self.frame_37)


        self.verticalLayout_42.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_54 = QLabel(self.frame_6)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_44.addWidget(self.label_54)

        self.text_filenamecsv = QLabel(self.frame_6)
        self.text_filenamecsv.setObjectName(u"text_filenamecsv")
        self.text_filenamecsv.setFont(font5)

        self.horizontalLayout_44.addWidget(self.text_filenamecsv)


        self.verticalLayout_42.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_34)

        self.frame_38 = QFrame(self.frame_6)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(150, 0))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.ms_partid_checkfile_buttton = QHBoxLayout(self.frame_38)
        self.ms_partid_checkfile_buttton.setSpacing(0)
        self.ms_partid_checkfile_buttton.setObjectName(u"ms_partid_checkfile_buttton")
        self.ms_partid_checkfile_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_41.addWidget(self.frame_38)


        self.verticalLayout_42.addLayout(self.horizontalLayout_41)

        self.frame_52 = QFrame(self.frame_6)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(150, 30))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.ms_partid_percentage = QHBoxLayout(self.frame_52)
        self.ms_partid_percentage.setSpacing(0)
        self.ms_partid_percentage.setObjectName(u"ms_partid_percentage")
        self.ms_partid_percentage.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_42.addWidget(self.frame_52)

        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_42.addWidget(self.checkBox)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_35)

        self.frame_39 = QFrame(self.frame_6)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(150, 0))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.ms_partid_submitinv_buttton = QHBoxLayout(self.frame_39)
        self.ms_partid_submitinv_buttton.setSpacing(0)
        self.ms_partid_submitinv_buttton.setObjectName(u"ms_partid_submitinv_buttton")
        self.ms_partid_submitinv_buttton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_40.addWidget(self.frame_39)


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
        self.text_currentinvupdatesubmissions = QLabel(self.page_8)
        self.text_currentinvupdatesubmissions.setObjectName(u"text_currentinvupdatesubmissions")
        self.text_currentinvupdatesubmissions.setFont(font1)

        self.verticalLayout_21.addWidget(self.text_currentinvupdatesubmissions)

        self.frame_48 = QFrame(self.page_8)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.ms_ciu_table1 = QHBoxLayout(self.frame_48)
        self.ms_ciu_table1.setSpacing(0)
        self.ms_ciu_table1.setObjectName(u"ms_ciu_table1")
        self.ms_ciu_table1.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_21.addWidget(self.frame_48)


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

        self.frame_40 = QFrame(self.page_8)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(100, 0))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.ms_currentinv_requestid_entry_ = QHBoxLayout(self.frame_40)
        self.ms_currentinv_requestid_entry_.setSpacing(0)
        self.ms_currentinv_requestid_entry_.setObjectName(u"ms_currentinv_requestid_entry_")
        self.ms_currentinv_requestid_entry_.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_18.addWidget(self.frame_40)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.frame_47 = QFrame(self.page_8)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(100, 0))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.ms_ciu_open_button = QHBoxLayout(self.frame_47)
        self.ms_ciu_open_button.setSpacing(0)
        self.ms_ciu_open_button.setObjectName(u"ms_ciu_open_button")
        self.ms_ciu_open_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_19.addWidget(self.frame_47)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_17.addLayout(self.verticalLayout_22)

        self.horizontalLayout_17.setStretch(0, 10)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_20.addLayout(self.horizontalLayout_17)

        self.frame_43 = QFrame(self.page_8)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(150, 20))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.ms_ciu_refresh_button = QHBoxLayout(self.frame_43)
        self.ms_ciu_refresh_button.setSpacing(0)
        self.ms_ciu_refresh_button.setObjectName(u"ms_ciu_refresh_button")
        self.ms_ciu_refresh_button.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_20.addWidget(self.frame_43)

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

        self.text_approve_checkbox_confirm = QCheckBox(self.page_8)
        self.text_approve_checkbox_confirm.setObjectName(u"text_approve_checkbox_confirm")

        self.horizontalLayout_20.addWidget(self.text_approve_checkbox_confirm)

        self.frame_44 = QFrame(self.page_8)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(100, 0))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.ms_ciu_clear_button = QHBoxLayout(self.frame_44)
        self.ms_ciu_clear_button.setSpacing(0)
        self.ms_ciu_clear_button.setObjectName(u"ms_ciu_clear_button")
        self.ms_ciu_clear_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_20.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.page_8)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(100, 0))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.ms_ciu_confirm_button = QHBoxLayout(self.frame_45)
        self.ms_ciu_confirm_button.setSpacing(0)
        self.ms_ciu_confirm_button.setObjectName(u"ms_ciu_confirm_button")
        self.ms_ciu_confirm_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_20.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.page_8)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(100, 0))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.ms_ciu_deny_button = QHBoxLayout(self.frame_46)
        self.ms_ciu_deny_button.setSpacing(0)
        self.ms_ciu_deny_button.setObjectName(u"ms_ciu_deny_button")
        self.ms_ciu_deny_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_20.addWidget(self.frame_46)


        self.verticalLayout_20.addLayout(self.horizontalLayout_20)

        self.approve_text_display = QTextEdit(self.page_8)
        self.approve_text_display.setObjectName(u"approve_text_display")
        self.approve_text_display.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.approve_text_display)

        self.verticalLayout_20.setStretch(0, 1)

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

        self.frame_49 = QFrame(self.page_9)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(150, 30))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.ms_currentdeny_requestid_entry = QHBoxLayout(self.frame_49)
        self.ms_currentdeny_requestid_entry.setSpacing(0)
        self.ms_currentdeny_requestid_entry.setObjectName(u"ms_currentdeny_requestid_entry")
        self.ms_currentdeny_requestid_entry.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_64.addWidget(self.frame_49)


        self.verticalLayout_46.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_51)

        self.frame_50 = QFrame(self.page_9)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(150, 0))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.ms_currentdeny_viewrequest_button = QHBoxLayout(self.frame_50)
        self.ms_currentdeny_viewrequest_button.setSpacing(0)
        self.ms_currentdeny_viewrequest_button.setObjectName(u"ms_currentdeny_viewrequest_button")
        self.ms_currentdeny_viewrequest_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_65.addWidget(self.frame_50)


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

        self.frame_51 = QFrame(self.page_9)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(150, 0))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.ms_currentdeny_delete_button = QHBoxLayout(self.frame_51)
        self.ms_currentdeny_delete_button.setSpacing(0)
        self.ms_currentdeny_delete_button.setObjectName(u"ms_currentdeny_delete_button")
        self.ms_currentdeny_delete_button.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_66.addWidget(self.frame_51)


        self.verticalLayout_24.addLayout(self.horizontalLayout_66)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_11)


        self.verticalLayout_47.addLayout(self.verticalLayout_24)

        self.pages.addWidget(self.page_9)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.text_main_makerspace.setText(QCoreApplication.translate("MainPages", u"Welcome to the Makerspace App!", None))
        self.text_main_username.setText(QCoreApplication.translate("MainPages", u"Username", None))
        self.text_main_username_2.setText(QCoreApplication.translate("MainPages", u"Password", None))
        self.MS_ST_add_student_label.setText(QCoreApplication.translate("MainPages", u"Add New Student", None))
        self.MS_ST_add_student_full_name.setText(QCoreApplication.translate("MainPages", u"Full Name", None))
        self.MS_ST_add_student_abc.setText(QCoreApplication.translate("MainPages", u"abc123", None))
        self.MS_ST_add_student_yoc.setText(QCoreApplication.translate("MainPages", u"Year of Conmpletion", None))
        self.MS_ST_search_trainee_label.setText(QCoreApplication.translate("MainPages", u"Search Trainee", None))
        self.MS_ST_search_trainee_fname.setText(QCoreApplication.translate("MainPages", u"First Name", None))
        self.MS_ST_search_trainee_or1.setText(QCoreApplication.translate("MainPages", u"or", None))
        self.MS_ST_search_trainee_lname.setText(QCoreApplication.translate("MainPages", u"Last Name", None))
        self.MS_ST_search_trainee_or2.setText(QCoreApplication.translate("MainPages", u"or", None))
        self.MS_ST_search_trainee_abc.setText(QCoreApplication.translate("MainPages", u"abc123", None))
        self.MS_ST_search_trainee_textbrowser.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">Machine Shop - Safety Training Record </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600"
                        ";\">For: __name__</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">With student ID: __abc123__</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">The sudent has (hasn't) been safety trained within</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">the last 2 years.</span></p>\n"
"<p style=\"-qt-"
                        "paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">RowdyMaker: T/F</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">Maker Level:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><s"
                        "pan style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">Write OXSDR and click renew to extend this student's</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:12pt; font-weight:600;\">safety training record another year.</span></p></body></html>", None))
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
        self.search_checkbox_keyword_as.setText(QCoreApplication.translate("MainPages", u"Keyword as Part ID", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Running Search as:", None))
        self.search_as_user.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Number of  Entries", None))
        self.search_checkbox_return_summary.setText(QCoreApplication.translate("MainPages", u"Return Summary Results", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Access Level", None))
        self.search_access.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Keyword", None))
        self.search_checkbox_best_fit.setText(QCoreApplication.translate("MainPages", u"Return Best Fit Item", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Update Inventory Based on Part ID", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"Part ID", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"Part Name:", None))
        self.update_resulting_part_name.setText("")
        self.label_12.setText(QCoreApplication.translate("MainPages", u"Updating as:", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"Approve as Admin", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"Admin Override:", None))
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
        self.text_partid.setText(QCoreApplication.translate("MainPages", u"Select Part ID", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"Choose Part / Item Category", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"If required - For Non Groupable Items set custom ID", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"\"AB\":", None))
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
        self.text_checkprevpartid.setText(QCoreApplication.translate("MainPages", u"Check Previous Part ID", None))
        self.text_partid_2.setText(QCoreApplication.translate("MainPages", u"Part Id", None))
        self.text_partidtobeused.setText(QCoreApplication.translate("MainPages", u"Part ID to be used:", None))
        self.label_51.setText(QCoreApplication.translate("MainPages", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainPages", u"Append multiple parts / items", None))
        self.label_52.setText(QCoreApplication.translate("MainPages", u"from file", None))
        self.label_53.setText(QCoreApplication.translate("MainPages", u"Type of file:", None))
        self.label_54.setText(QCoreApplication.translate("MainPages", u"File to use:", None))
        self.text_filenamecsv.setText(QCoreApplication.translate("MainPages", u"Filename.csv", None))
        self.checkBox.setText(QCoreApplication.translate("MainPages", u"File is ready to be submitted", None))
        self.text_currentinvupdatesubmissions.setText(QCoreApplication.translate("MainPages", u"Current Inventory Updates Submitted", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"Review", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"Request ID", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"Request ID:", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.text_approve_checkbox_confirm.setText(QCoreApplication.translate("MainPages", u"I have reviewed and confirmed the validity of this update", None))
        self.approve_text_display.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Devanagari'; font-size:14pt; font-weight:600;\">Entrie Submitted for Approval</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainPages", u"Current Denied Updates", None))
        self.label_76.setText(QCoreApplication.translate("MainPages", u"Request ID:", None))
    # retranslateUi

