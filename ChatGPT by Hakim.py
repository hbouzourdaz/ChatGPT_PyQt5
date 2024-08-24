import sys
import openai
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QTextEdit, QWidget, QSpacerItem, QSizePolicy, QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap

# Set your OpenAI API key
openai.api_key = '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'

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("نظام تسجيل الدخول")
        self.setGeometry(100, 100, 400, 600)
        self.setWindowIcon(QIcon("login_icon.png"))

        # Disable maximize button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        # Center the window on the screen
        self.center_window()

        # Set font to Tajawal
        font = QFont("Tajawal", 12)
        self.setFont(font)

        # Set up style sheet with new colors and Tajawal font
        self.setStyleSheet("""
            QMainWindow {
                background-color: #e0f7fa;
            }
            QLabel, QLineEdit, QPushButton, QCheckBox {
                font-family: 'Tajawal';
            }
            QLabel {
                color: #00695c;
                font-size: 20px;
            }
            QLineEdit {
                border: 1px solid #004d40;
                border-radius: 5px;
                padding: 5px;
                font-size: 20px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #00796b;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #004d40;
            }
            QCheckBox {
                font-size: 20px;
                color: #004d40;
            }
            QPushButton#exit-button {
                background-color: #d32f2f;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton#exit-button:hover {
                background-color: #b71c1c;
            }
            QLabel#copyright {
                font-size: 16px;
                color: #004d40;
                margin-top: 20px;
                text-align: center;
                padding-top: 10px;
            }
        """)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout()
        form_layout = QVBoxLayout()

        # Add logo image
        self.logo_label = QLabel(self)
        self.logo_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("logo.png")
        self.logo_label.setPixmap(pixmap.scaled(QSize(150, 150), Qt.KeepAspectRatio))
        form_layout.addWidget(self.logo_label)

        # Username label and input
        self.label_username = QLabel("اسم المستخدم:")
        self.label_username.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(self.label_username)
        
        self.textbox_username = QLineEdit(self)
        self.textbox_username.setText("admin")
        self.textbox_username.setAlignment(Qt.AlignRight)
        self.textbox_username.setLayoutDirection(Qt.RightToLeft)
        form_layout.addWidget(self.textbox_username)

        # Password label and input
        self.label_password = QLabel("كلمة المرور:")
        self.label_password.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(self.label_password)
        
        self.textbox_password = QLineEdit(self)
        self.textbox_password.setEchoMode(QLineEdit.Password)
        self.textbox_password.setAlignment(Qt.AlignRight)
        self.textbox_password.setLayoutDirection(Qt.RightToLeft)
        form_layout.addWidget(self.textbox_password)

        # Remember Me checkbox
        self.checkbox_remember_me = QCheckBox("تذكرني", self)
        self.checkbox_remember_me.setLayoutDirection(Qt.RightToLeft)
        form_layout.addWidget(self.checkbox_remember_me)

        # Spacer item to add space between elements
        form_layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Login button
        self.button_login = QPushButton("تسجيل الدخول", self)
        self.button_login.clicked.connect(self.check_login)
        form_layout.addWidget(self.button_login)

        # Exit button with direct color setting and hover effect
        self.button_exit = QPushButton("خروج", self)
        self.button_exit.setObjectName("exit-button")
        self.button_exit.clicked.connect(self.close)
        form_layout.addWidget(self.button_exit)

        # Status message
        self.label_status = QLabel("", self)
        self.label_status.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(self.label_status)

        # Add form layout to main layout and center it
        main_layout.addStretch()
        main_layout.addLayout(form_layout)
        main_layout.addStretch()

        # Copyright text
        self.copyright_label = QLabel("© 2024 Hakim Bouzourdaz.", self)
        self.copyright_label.setObjectName("copyright")
        main_layout.addWidget(self.copyright_label)

        central_widget.setLayout(main_layout)

    def check_login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()

        if username == "admin" and password == "0000":
            self.label_status.setText("تم تسجيل الدخول بنجاح!")
            self.open_chatgpt_window()
        else:
            self.label_status.setText("اسم المستخدم أو كلمة المرور غير صحيحة.")

    def open_chatgpt_window(self):
        self.chatgpt_window = ChatGPTWindow()
        self.chatgpt_window.show()
        self.close()

    def center_window(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class ChatGPTWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("نافذة ChatGPT")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("openai.png"))

        # Center the window on the screen
        self.center_window()

        # Set font to Tajawal
        font = QFont("Tajawal", 12)
        self.setFont(font)

        # Set up style sheet for chat window
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;  /* White background */
            }
            QLabel, QTextEdit, QLineEdit, QPushButton {
                font-family: 'Tajawal';
            }
            QLabel {
                font-size: 20px;
                color: #00695c;
            }
            QTextEdit {
                border: 1px solid #004d40;
                border-radius: 5px;
                padding: 10px;
                font-size: 20px;
                background-color: #ffffff;
            }
            QLineEdit {
                border: 1px solid #004d40;
                border-radius: 5px;
                padding: 5px;
                font-size: 20px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #00796b;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #004d40;
            }
        """)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout()

        # Chat display area
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        main_layout.addWidget(self.chat_display)

        # User input area
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("أدخل رسالتك هنا...")
        main_layout.addWidget(self.user_input)

        # Send button
        self.button_send = QPushButton("إرسال", self)
        self.button_send.clicked.connect(self.send_message)
        main_layout.addWidget(self.button_send)

        central_widget.setLayout(main_layout)

    def send_message(self):
        user_message = self.user_input.text()
        if user_message:
            # Display the user's message in the chat area
            self.chat_display.append(f"أنت: {user_message}")
            # Clear the input field
            self.user_input.clear()

            # Call the OpenAI API with the newer model
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": user_message}
                    ]
                )
                # Display the ChatGPT response
                chatgpt_message = response.choices[0].message['content'].strip()
                self.chat_display.append(f"ChatGPT: {chatgpt_message}")
            except Exception as e:
                self.chat_display.append("حدث خطأ أثناء الاتصال بـ ChatGPT.")
                print(f"Error: {e}")

    def center_window(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
