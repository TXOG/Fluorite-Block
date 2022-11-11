# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowdnfxCA.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -21, 801, 591))
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.tilte_label = QLabel(self.menu)
        self.tilte_label.setObjectName(u"tilte_label")
        self.tilte_label.setGeometry(QRect(0, 20, 801, 51))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(24)
        font.setBold(False)
        self.tilte_label.setFont(font)
        self.tilte_label.setCursor(QCursor(Qt.ArrowCursor))
        self.tilte_label.setTextFormat(Qt.AutoText)
        self.tilte_label.setScaledContents(False)
        self.tilte_label.setAlignment(Qt.AlignCenter)
        self.undo_btn = QPushButton(self.menu)
        self.undo_btn.setObjectName(u"undo_btn")
        self.undo_btn.setGeometry(QRect(270, 480, 261, 71))
        self.undo_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.redirect_btn = QPushButton(self.menu)
        self.redirect_btn.setObjectName(u"redirect_btn")
        self.redirect_btn.setGeometry(QRect(270, 320, 261, 71))
        self.redirect_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.apply_btn = QPushButton(self.menu)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setGeometry(QRect(270, 80, 261, 71))
        self.apply_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.whitelist_btn = QPushButton(self.menu)
        self.whitelist_btn.setObjectName(u"whitelist_btn")
        self.whitelist_btn.setGeometry(QRect(270, 160, 261, 71))
        self.whitelist_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.blacklist_btn = QPushButton(self.menu)
        self.blacklist_btn.setObjectName(u"blacklist_btn")
        self.blacklist_btn.setGeometry(QRect(270, 240, 261, 71))
        self.blacklist_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.cleanup_btn = QPushButton(self.menu)
        self.cleanup_btn.setObjectName(u"cleanup_btn")
        self.cleanup_btn.setGeometry(QRect(270, 400, 261, 71))
        self.cleanup_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.stackedWidget.addWidget(self.menu)
        self.custom_redirects = QWidget()
        self.custom_redirects.setObjectName(u"custom_redirects")
        self.stackedWidget.addWidget(self.custom_redirects)
        self.apply_blocklist = QWidget()
        self.apply_blocklist.setObjectName(u"apply_blocklist")
        self.oisd_full_frame = QFrame(self.apply_blocklist)
        self.oisd_full_frame.setObjectName(u"oisd_full_frame")
        self.oisd_full_frame.setGeometry(QRect(20, 80, 251, 91))
        self.oisd_full_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.oisd_full_frame.setFrameShape(QFrame.NoFrame)
        self.oisd_full_frame.setFrameShadow(QFrame.Raised)
        self.oisd_full_frame.setLineWidth(0)
        self.oisd_full_layout = QHBoxLayout(self.oisd_full_frame)
        self.oisd_full_layout.setSpacing(0)
        self.oisd_full_layout.setObjectName(u"oisd_full_layout")
        self.oisd_full_layout.setContentsMargins(0, 0, 0, 0)
        self.oisd_lightweight_frame = QFrame(self.apply_blocklist)
        self.oisd_lightweight_frame.setObjectName(u"oisd_lightweight_frame")
        self.oisd_lightweight_frame.setGeometry(QRect(20, 170, 251, 91))
        self.oisd_lightweight_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.oisd_lightweight_frame.setFrameShape(QFrame.NoFrame)
        self.oisd_lightweight_frame.setFrameShadow(QFrame.Raised)
        self.oisd_lightweight_frame.setLineWidth(0)
        self.oisd_lightweight_layout = QHBoxLayout(self.oisd_lightweight_frame)
        self.oisd_lightweight_layout.setSpacing(0)
        self.oisd_lightweight_layout.setObjectName(u"oisd_lightweight_layout")
        self.oisd_lightweight_layout.setContentsMargins(0, 0, 0, 0)
        self.ipgrabber_blocklist_frame = QFrame(self.apply_blocklist)
        self.ipgrabber_blocklist_frame.setObjectName(u"ipgrabber_blocklist_frame")
        self.ipgrabber_blocklist_frame.setGeometry(QRect(20, 260, 251, 91))
        self.ipgrabber_blocklist_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.ipgrabber_blocklist_frame.setStyleSheet(u"")
        self.ipgrabber_blocklist_frame.setFrameShape(QFrame.NoFrame)
        self.ipgrabber_blocklist_frame.setFrameShadow(QFrame.Raised)
        self.ipgrabber_blocklist_frame.setLineWidth(0)
        self.ipgrabber_blocklist_layout = QHBoxLayout(self.ipgrabber_blocklist_frame)
        self.ipgrabber_blocklist_layout.setSpacing(0)
        self.ipgrabber_blocklist_layout.setObjectName(u"ipgrabber_blocklist_layout")
        self.ipgrabber_blocklist_layout.setContentsMargins(0, 0, 0, 0)
        self.no_facebook_frame = QFrame(self.apply_blocklist)
        self.no_facebook_frame.setObjectName(u"no_facebook_frame")
        self.no_facebook_frame.setGeometry(QRect(20, 350, 251, 91))
        self.no_facebook_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.no_facebook_frame.setFrameShape(QFrame.NoFrame)
        self.no_facebook_frame.setFrameShadow(QFrame.Raised)
        self.no_facebook_frame.setLineWidth(0)
        self.no_facebook_layout = QHBoxLayout(self.no_facebook_frame)
        self.no_facebook_layout.setSpacing(0)
        self.no_facebook_layout.setObjectName(u"no_facebook_layout")
        self.no_facebook_layout.setContentsMargins(0, 0, 0, 0)
        self.tilte_label_2 = QLabel(self.apply_blocklist)
        self.tilte_label_2.setObjectName(u"tilte_label_2")
        self.tilte_label_2.setGeometry(QRect(0, 30, 801, 51))
        self.tilte_label_2.setFont(font)
        self.tilte_label_2.setCursor(QCursor(Qt.ArrowCursor))
        self.tilte_label_2.setTextFormat(Qt.AutoText)
        self.tilte_label_2.setScaledContents(False)
        self.tilte_label_2.setAlignment(Qt.AlignCenter)
        self.custom_blocklist_btn = QPushButton(self.apply_blocklist)
        self.custom_blocklist_btn.setObjectName(u"custom_blocklist_btn")
        self.custom_blocklist_btn.setGeometry(QRect(10, 460, 251, 71))
        self.custom_blocklist_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.apply_blocklist_btn = QPushButton(self.apply_blocklist)
        self.apply_blocklist_btn.setObjectName(u"apply_blocklist_btn")
        self.apply_blocklist_btn.setGeometry(QRect(520, 460, 261, 71))
        self.apply_blocklist_btn.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.oisd_full_label = QLabel(self.apply_blocklist)
        self.oisd_full_label.setObjectName(u"oisd_full_label")
        self.oisd_full_label.setGeometry(QRect(268, 79, 531, 91))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(12)
        self.oisd_full_label.setFont(font1)
        self.oisd_full_label.setTextFormat(Qt.RichText)
        self.oisd_full_label.setScaledContents(False)
        self.oisd_full_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.oisd_full_label.setWordWrap(True)
        self.oisd_lightweight_label_2 = QLabel(self.apply_blocklist)
        self.oisd_lightweight_label_2.setObjectName(u"oisd_lightweight_label_2")
        self.oisd_lightweight_label_2.setGeometry(QRect(270, 170, 531, 91))
        self.oisd_lightweight_label_2.setFont(font1)
        self.oisd_lightweight_label_2.setTextFormat(Qt.RichText)
        self.oisd_lightweight_label_2.setScaledContents(False)
        self.oisd_lightweight_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.oisd_lightweight_label_2.setWordWrap(True)
        self.ipgrabber_label = QLabel(self.apply_blocklist)
        self.ipgrabber_label.setObjectName(u"ipgrabber_label")
        self.ipgrabber_label.setGeometry(QRect(270, 260, 531, 91))
        self.ipgrabber_label.setFont(font1)
        self.ipgrabber_label.setTextFormat(Qt.RichText)
        self.ipgrabber_label.setScaledContents(False)
        self.ipgrabber_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ipgrabber_label.setWordWrap(True)
        self.no_facebook_label = QLabel(self.apply_blocklist)
        self.no_facebook_label.setObjectName(u"no_facebook_label")
        self.no_facebook_label.setGeometry(QRect(270, 350, 531, 91))
        self.no_facebook_label.setFont(font1)
        self.no_facebook_label.setTextFormat(Qt.RichText)
        self.no_facebook_label.setScaledContents(False)
        self.no_facebook_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.no_facebook_label.setWordWrap(True)
        self.stackedWidget.addWidget(self.apply_blocklist)
        self.cleanup_blocklists = QWidget()
        self.cleanup_blocklists.setObjectName(u"cleanup_blocklists")
        self.stackedWidget.addWidget(self.cleanup_blocklists)
        self.undo_all_changes = QWidget()
        self.undo_all_changes.setObjectName(u"undo_all_changes")
        self.stackedWidget.addWidget(self.undo_all_changes)
        self.blacklisting = QWidget()
        self.blacklisting.setObjectName(u"blacklisting")
        self.stackedWidget.addWidget(self.blacklisting)
        self.whitelisting = QWidget()
        self.whitelisting.setObjectName(u"whitelisting")
        self.stackedWidget.addWidget(self.whitelisting)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tilte_label.setText(QCoreApplication.translate("MainWindow", u"Sysblock GUI", None))
        self.undo_btn.setText(QCoreApplication.translate("MainWindow", u"UNDO", None))
        self.redirect_btn.setText(QCoreApplication.translate("MainWindow", u"Redirect", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.whitelist_btn.setText(QCoreApplication.translate("MainWindow", u"Whitelist", None))
        self.blacklist_btn.setText(QCoreApplication.translate("MainWindow", u"Blacklist", None))
        self.cleanup_btn.setText(QCoreApplication.translate("MainWindow", u"Cleanup", None))
        self.tilte_label_2.setText(QCoreApplication.translate("MainWindow", u"Apply Blocklist", None))
        self.custom_blocklist_btn.setText(QCoreApplication.translate("MainWindow", u"Custom URL", None))
        self.apply_blocklist_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.oisd_full_label.setText(QCoreApplication.translate("MainWindow", u"Main Blocklist. Recommended for higher spec devices. Note this can have a severe effect on startup time for weaker devices.", None))
        self.oisd_lightweight_label_2.setText(QCoreApplication.translate("MainWindow", u"Main Blocklist more friendly to low end devices. Recommended for laptops and weaker spec devices.", None))
        self.ipgrabber_label.setText(QCoreApplication.translate("MainWindow", u"Extra Blocklist. Blocks Ip Grabbers as they name suggests.", None))
        self.no_facebook_label.setText(QCoreApplication.translate("MainWindow", u"Blocks Facebook and Facebook related trackers entirely (no access).", None))
    # retranslateUi

