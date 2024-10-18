# -*- coding: utf-8 -*-
"""
Módulo: ChatWidget

Este módulo implementa um widget de chat personalizado usando PySide6.
Ele fornece uma interface de usuário para exibir mensagens de chat,
enviar mensagens e receber respostas.

Autor: Stefano Gysin - StefanoGysin@hotmail.com
Data: 15/10/2024 13:11 (horário de Zurique)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit,
    QPushButton, QScrollArea, QTimer
)
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QFont, QTextCursor
from html import escape

class ChatWidget(QWidget):
    """
    Widget personalizado para interface de chat.

    Esta classe cria uma interface de usuário para um chat, incluindo
    uma área de exibição de mensagens, um campo de entrada e um botão de envio.
    """

    # Constantes de estilo
    BACKGROUND_COLOR = "#f0f0f0"
    BORDER_COLOR = "#ccc"
    FONT_SIZE = 12
    BUTTON_COLOR = "#4CAF50"

    # Sinal emitido quando uma mensagem é enviada
    message_sent = Signal(str)

    def __init__(self, parent=None):
        """Inicializa o widget de chat."""
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """Configura a interface do usuário do widget."""
        layout = QVBoxLayout(self)

        # Configuração da área de exibição do chat
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Arial", self.FONT_SIZE))
        self.chat_display.setStyleSheet(
            f"background-color: {self.BACKGROUND_COLOR}; "
            f"border: 1px solid {self.BORDER_COLOR}; border-radius: 5px;"
        )

        # Adição de uma área de rolagem para o chat
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.chat_display)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        # Layout para entrada de texto e botão de envio
        input_layout = QHBoxLayout()

        # Configuração do campo de entrada do usuário
        self.user_input = QLineEdit()
        self.user_input.setFont(QFont("Arial", self.FONT_SIZE))
        self.user_input.setPlaceholderText("Digite sua mensagem aqui...")
        self.user_input.setStyleSheet(
            f"border: 1px solid {self.BORDER_COLOR}; border-radius: 5px; padding: 5px;"
        )
        self.user_input.setAccessibleName("Campo de entrada de mensagem")
        input_layout.addWidget(self.user_input)

        # Configuração do botão de enviar
        self.send_button = QPushButton("Enviar")
        self.send_button.setStyleSheet(
            f"background-color: {self.BUTTON_COLOR}; color: white; "
            "border-radius: 5px; padding: 5px 10px;"
        )
        self.send_button.setAccessibleName("Enviar mensagem")
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)

        # Conexão de sinais
        self.send_button.clicked.connect(self.send_message)
        self.user_input.returnPressed.connect(self.send_message)

    @Slot()
    def send_message(self):
        """Envia a mensagem inserida pelo usuário."""
        message = self.user_input.text().strip()
        if message:
            self.add_message("Você", message)
            self.message_sent.emit(message)
            self.user_input.clear()
        else:
            # Feedback visual para mensagens vazias
            self.user_input.setStyleSheet("border: 1px solid red;")
            QTimer.singleShot(1000, lambda: self.user_input.setStyleSheet(
                f"border: 1px solid {self.BORDER_COLOR};"
            ))
        self.user_input.setFocus()

    def add_message(self, sender, message):
        """Adiciona uma mensagem à área de exibição do chat."""
        cursor = self.chat_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.chat_display.setTextCursor(cursor)
        
        formatted_message = f"<p><strong>{escape(sender)}:</strong> {escape(message)}</p>"
        self.chat_display.insertHtml(formatted_message)
        
        # Rola para o final da área de chat
        self.chat_display.verticalScrollBar().setValue(
            self.chat_display.verticalScrollBar().maximum()
        )

    def add_ai_response(self, response):
        """Adiciona uma resposta da IA ao chat."""
        self.add_message("Gysin IA", response)

    def clear_chat(self):
        """Limpa todas as mensagens do chat."""
        self.chat_display.clear()

    def disable_input(self):
        """Desabilita a entrada do usuário."""
        self.user_input.setEnabled(False)
        self.send_button.setEnabled(False)

    def enable_input(self):
        """Habilita a entrada do usuário."""
        self.user_input.setEnabled(True)
        self.send_button.setEnabled(True)