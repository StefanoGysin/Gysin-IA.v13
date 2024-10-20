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
    QPushButton, QScrollArea, QTimer, QMessageBox
)
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QFont, QTextCursor, QKeyEvent
from typing import Optional
from html import escape
from gui.language_utils import detect_language

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
    MAX_HISTORY = 100
    MAX_MESSAGE_LENGTH = 500  # Limite máximo de caracteres por mensagem

    # Sinal emitido quando uma mensagem é enviada
    message_sent = Signal(str)

    def __init__(self, parent: Optional[QWidget] = None):
        """Inicializa o widget de chat."""
        super().__init__(parent)
        self._message_history: list[str] = []
        self._history_index: int = -1
        self._init_ui()

    def _init_ui(self):
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
        """Envia a mensagem inserida pelo usuário e detecta o idioma."""
        message = self.user_input.text().strip()
        if message:
            if len(message) > self.MAX_MESSAGE_LENGTH:
                QMessageBox.warning(self, "Mensagem muito longa", 
                                    f"A mensagem não pode exceder {self.MAX_MESSAGE_LENGTH} caracteres.")
                return
            try:
                # Detectar o idioma da mensagem
                detected_language = detect_language(message)
                print(f"Idioma detectado: {detected_language}")

                self.add_message("Você", message)
                self.message_sent.emit(message)
                self.add_to_history(message)
                self.user_input.clear()
            except Exception as e:
                self.add_error_message(f"Erro ao enviar mensagem: {str(e)}")
        else:
            # Feedback visual para mensagens vazias
            self.user_input.setStyleSheet("border: 1px solid red;")
            QTimer.singleShot(1000, lambda: self.user_input.setStyleSheet(
                f"border: 1px solid {self.BORDER_COLOR};"
            ))
        self.user_input.setFocus()

    def add_message(self, sender: str, message: str, background_color: Optional[str] = None):
        """Adiciona uma mensagem à área de exibição do chat."""
        try:
            cursor = self.chat_display.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.chat_display.setTextCursor(cursor)

            if background_color:
                formatted_message = f'<p style="background-color: {background_color};"><strong>{escape(sender)}:</strong> {escape(message)}</p>'
            else:
                formatted_message = f"<p><strong>{escape(sender)}:</strong> {escape(message)}</p>"
            
            self.chat_display.insertHtml(formatted_message)
            
            # Rola para o final da área de chat
            self.chat_display.verticalScrollBar().setValue(
                self.chat_display.verticalScrollBar().maximum()
            )
        except Exception as e:
            print(f"Erro ao adicionar mensagem: {str(e)}")

    def add_ai_response(self, response: str):
        """Adiciona uma resposta da IA ao chat."""
        self.add_message("Gysin IA", response)

    def add_system_message(self, message: str):
        """Adiciona uma mensagem do sistema ao chat."""
        self.add_message("Sistema", message, "#FFE6E6")  # Cor de fundo para mensagens do sistema

    def add_error_message(self, message: str):
        """Adiciona uma mensagem de erro ao chat."""
        self.add_message("Erro", message, "#FFCCCB")  # Cor de fundo para mensagens de erro

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
    
    def keyPressEvent(self, event: QKeyEvent):
        """Gerencia eventos de tecla pressionada."""
        if event.key() == Qt.Key_Up:
            self.navigate_history('up')
        elif event.key() == Qt.Key_Down:
            self.navigate_history('down')
        else:
            super().keyPressEvent(event)

    def add_to_history(self, message: str):
        """Adiciona uma mensagem ao histórico."""
        self._message_history.append(message)
        if len(self._message_history) > self.MAX_HISTORY:
            self._message_history.pop(0)
        self._history_index = len(self._message_history)

    def navigate_history(self, direction: str):
        """Navega pelo histórico de mensagens."""
        if not self._message_history:
            return
        
        if direction == 'up':
            self._history_index = max(0, self._history_index - 1)
        elif direction == 'down':
            self._history_index = min(len(self._message_history), self._history_index + 1)
        
        if self._history_index < len(self._message_history):
            self.user_input.setText(self._message_history[self._history_index])
        else:
            self.user_input.clear()