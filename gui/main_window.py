from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QApplication, QLabel
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QFont, QIcon, QTextCursor
from api.openai_client import OpenAIClient
from dotenv import load_dotenv
import os

load_dotenv()

class MainWindow(QMainWindow):
    # Constantes
    BACKGROUND_USER = "#E6F3FF"
    BACKGROUND_AI = "#F0FFF0"
    BACKGROUND_SYSTEM = "#444444"
    FONT_SIZE = 12

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gysin IA")
        self.setMinimumSize(1080, 720)

        self.setup_ui()
        self.openai_client = OpenAIClient()
        self.add_message("Sistema", "Bem-vindo ao Gysin IA! Como posso ajudar você hoje?", self.BACKGROUND_SYSTEM)

    def setup_ui(self):
        """Configura a interface do usuário."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Arial", self.FONT_SIZE))
        self.chat_display.setStyleSheet("background-color: #393737;")
        main_layout.addWidget(self.chat_display)

        self.typing_label = QLabel("Gysin IA está digitando...")
        self.typing_label.hide()
        main_layout.addWidget(self.typing_label)

        input_layout = QHBoxLayout()

        self.user_input = QLineEdit()
        self.user_input.setFont(QFont("Arial", self.FONT_SIZE))
        self.user_input.setPlaceholderText("Digite sua mensagem aqui...")
        input_layout.addWidget(self.user_input)

        self.send_button = QPushButton("Enviar")
        icon_path = "resources/icons/cil-cursor.png"
        if os.path.exists(icon_path):
            self.send_button.setIcon(QIcon(icon_path))
        input_layout.addWidget(self.send_button)

        main_layout.addLayout(input_layout)

        self.send_button.clicked.connect(self.send_message)
        self.user_input.returnPressed.connect(self.send_message)

    @Slot()
    def send_message(self):
        """Envia a mensagem do usuário e solicita resposta da IA."""
        user_text = self.user_input.text().strip()
        if not user_text:
            return  # Não envia mensagens vazias

        self.add_message("Você", user_text, self.BACKGROUND_USER)
        self.user_input.clear()
        self.user_input.setEnabled(False)
        self.send_button.setEnabled(False)
        self.typing_label.show()
        QApplication.setOverrideCursor(Qt.WaitCursor)

        QTimer.singleShot(100, lambda: self.get_ai_response(user_text))

    def get_ai_response(self, user_text):
        """Obtém a resposta da IA e a exibe."""
        try:
            response = self.openai_client.get_response(user_text)
            self.add_message("Gysin IA", response, self.BACKGROUND_AI)
        except Exception as e:
            self.add_message("Sistema", f"Erro: {str(e)}", self.BACKGROUND_SYSTEM)
        finally:
            self.user_input.setEnabled(True)
            self.send_button.setEnabled(True)
            self.typing_label.hide()
            QApplication.restoreOverrideCursor()

    def add_message(self, sender, message, background_color):
        """Adiciona uma mensagem à área de chat."""
        self.chat_display.append(f'<div style="background-color: {background_color}; padding: 5px; margin: 5px 0;">'
                                 f'<b>{sender}:</b> {message}</div>')
        self.chat_display.moveCursor(QTextCursor.End)
        self.chat_display.ensureCursorVisible()

    def closeEvent(self, event):
        """Manipula o evento de fechamento da janela."""
        # Adicione qualquer lógica de limpeza necessária aqui
        event.accept()