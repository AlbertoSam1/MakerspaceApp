# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_column.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_machine_shop_left_column = QFrame(self.menu_1)
        self.btn_machine_shop_left_column.setObjectName(u"btn_machine_shop_left_column")
        self.btn_machine_shop_left_column.setMinimumSize(QSize(0, 40))
        self.btn_machine_shop_left_column.setMaximumSize(QSize(16777215, 40))
        self.btn_machine_shop_left_column.setFrameShape(QFrame.NoFrame)
        self.btn_machine_shop_left_column.setFrameShadow(QFrame.Raised)
        self.btn_ms_leftcol_layout = QVBoxLayout(self.btn_machine_shop_left_column)
        self.btn_ms_leftcol_layout.setSpacing(0)
        self.btn_ms_leftcol_layout.setObjectName(u"btn_ms_leftcol_layout")
        self.btn_ms_leftcol_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_machine_shop_left_column)

        self.btn_safety_training_ms = QFrame(self.menu_1)
        self.btn_safety_training_ms.setObjectName(u"btn_safety_training_ms")
        self.btn_safety_training_ms.setMinimumSize(QSize(0, 40))
        self.btn_safety_training_ms.setMaximumSize(QSize(16777215, 40))
        self.btn_safety_training_ms.setFrameShape(QFrame.NoFrame)
        self.btn_safety_training_ms.setFrameShadow(QFrame.Raised)
        self.btn_safety_training_ms_layout = QVBoxLayout(self.btn_safety_training_ms)
        self.btn_safety_training_ms_layout.setSpacing(0)
        self.btn_safety_training_ms_layout.setObjectName(u"btn_safety_training_ms_layout")
        self.btn_safety_training_ms_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_safety_training_ms)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.menus.addWidget(self.menu_1)
        self.menu_2_inventory = QWidget()
        self.menu_2_inventory.setObjectName(u"menu_2_inventory")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2_inventory)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_inventory_overview_frame = QFrame(self.menu_2_inventory)
        self.btn_inventory_overview_frame.setObjectName(u"btn_inventory_overview_frame")
        self.btn_inventory_overview_frame.setMinimumSize(QSize(0, 40))
        self.btn_inventory_overview_frame.setFrameShape(QFrame.NoFrame)
        self.btn_inventory_overview_frame.setFrameShadow(QFrame.Raised)
        self.btn_inventory_overview_layout = QVBoxLayout(self.btn_inventory_overview_frame)
        self.btn_inventory_overview_layout.setSpacing(0)
        self.btn_inventory_overview_layout.setObjectName(u"btn_inventory_overview_layout")
        self.btn_inventory_overview_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_inventory_overview_frame)

        self.btn_inventory_search_frame = QFrame(self.menu_2_inventory)
        self.btn_inventory_search_frame.setObjectName(u"btn_inventory_search_frame")
        self.btn_inventory_search_frame.setMinimumSize(QSize(0, 40))
        self.btn_inventory_search_frame.setFrameShape(QFrame.NoFrame)
        self.btn_inventory_search_frame.setFrameShadow(QFrame.Raised)
        self.btn_inventory_search_layout = QHBoxLayout(self.btn_inventory_search_frame)
        self.btn_inventory_search_layout.setSpacing(0)
        self.btn_inventory_search_layout.setObjectName(u"btn_inventory_search_layout")
        self.btn_inventory_search_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_inventory_search_frame)

        self.btn_inventory_update_frame = QFrame(self.menu_2_inventory)
        self.btn_inventory_update_frame.setObjectName(u"btn_inventory_update_frame")
        self.btn_inventory_update_frame.setMinimumSize(QSize(0, 40))
        self.btn_inventory_update_frame.setFrameShape(QFrame.NoFrame)
        self.btn_inventory_update_frame.setFrameShadow(QFrame.Raised)
        self.btn_inventory_update_layout = QHBoxLayout(self.btn_inventory_update_frame)
        self.btn_inventory_update_layout.setSpacing(0)
        self.btn_inventory_update_layout.setObjectName(u"btn_inventory_update_layout")
        self.btn_inventory_update_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_inventory_update_frame)

        self.btn_inventory_append_frame = QFrame(self.menu_2_inventory)
        self.btn_inventory_append_frame.setObjectName(u"btn_inventory_append_frame")
        self.btn_inventory_append_frame.setMinimumSize(QSize(0, 40))
        self.btn_inventory_append_frame.setFrameShape(QFrame.NoFrame)
        self.btn_inventory_append_frame.setFrameShadow(QFrame.Raised)
        self.btn_inventory_append_layout = QHBoxLayout(self.btn_inventory_append_frame)
        self.btn_inventory_append_layout.setSpacing(0)
        self.btn_inventory_append_layout.setObjectName(u"btn_inventory_append_layout")
        self.btn_inventory_append_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_inventory_append_frame)

        self.btn_inventory_approve_frame = QFrame(self.menu_2_inventory)
        self.btn_inventory_approve_frame.setObjectName(u"btn_inventory_approve_frame")
        self.btn_inventory_approve_frame.setMinimumSize(QSize(0, 40))
        self.btn_inventory_approve_frame.setFrameShape(QFrame.NoFrame)
        self.btn_inventory_approve_frame.setFrameShadow(QFrame.Raised)
        self.btn_inventory_approve_layout = QHBoxLayout(self.btn_inventory_approve_frame)
        self.btn_inventory_approve_layout.setSpacing(0)
        self.btn_inventory_approve_layout.setObjectName(u"btn_inventory_approve_layout")
        self.btn_inventory_approve_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_inventory_approve_frame)

        self.btn_inventory_denied_frame = QFrame(self.menu_2_inventory)
        self.btn_inventory_denied_frame.setObjectName(u"btn_inventory_denied_frame")
        self.btn_inventory_denied_frame.setMinimumSize(QSize(0, 40))
        self.btn_inventory_denied_frame.setFrameShape(QFrame.NoFrame)
        self.btn_inventory_denied_frame.setFrameShadow(QFrame.Raised)
        self.btn_inventory_denied_layout = QHBoxLayout(self.btn_inventory_denied_frame)
        self.btn_inventory_denied_layout.setSpacing(0)
        self.btn_inventory_denied_layout.setObjectName(u"btn_inventory_denied_layout")
        self.btn_inventory_denied_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_inventory_denied_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.menus.addWidget(self.menu_2_inventory)
        self.menu_3_3dprinting = QWidget()
        self.menu_3_3dprinting.setObjectName(u"menu_3_3dprinting")
        self.verticalLayout_3 = QVBoxLayout(self.menu_3_3dprinting)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_printing_dashboard_frame = QFrame(self.menu_3_3dprinting)
        self.btn_printing_dashboard_frame.setObjectName(u"btn_printing_dashboard_frame")
        self.btn_printing_dashboard_frame.setMinimumSize(QSize(0, 40))
        self.btn_printing_dashboard_frame.setFrameShape(QFrame.NoFrame)
        self.btn_printing_dashboard_frame.setFrameShadow(QFrame.Raised)
        self.btn_printing_dashboard_layout = QVBoxLayout(self.btn_printing_dashboard_frame)
        self.btn_printing_dashboard_layout.setSpacing(0)
        self.btn_printing_dashboard_layout.setObjectName(u"btn_printing_dashboard_layout")
        self.btn_printing_dashboard_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.btn_printing_dashboard_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.menus.addWidget(self.menu_3_3dprinting)
        self.menu_4_monday = QWidget()
        self.menu_4_monday.setObjectName(u"menu_4_monday")
        self.verticalLayout_5 = QVBoxLayout(self.menu_4_monday)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.monday_column_frame = QFrame(self.menu_4_monday)
        self.monday_column_frame.setObjectName(u"monday_column_frame")
        self.monday_column_frame.setMinimumSize(QSize(0, 40))
        self.monday_column_frame.setFrameShape(QFrame.NoFrame)
        self.monday_column_frame.setFrameShadow(QFrame.Raised)
        self.monday_tab_layout = QHBoxLayout(self.monday_column_frame)
        self.monday_tab_layout.setSpacing(0)
        self.monday_tab_layout.setObjectName(u"monday_tab_layout")
        self.monday_tab_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.monday_column_frame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.menus.addWidget(self.menu_4_monday)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
    # retranslateUi

