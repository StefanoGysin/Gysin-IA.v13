# Gysin IA

## Visão Geral
Gysin IA é uma assistente virtual desenvolvida para oferecer interações humanizadas e personalizadas. Utilizando processamento de linguagem natural e síntese de voz, Gysin IA é capaz de entender e responder a consultas em múltiplos idiomas, aprimorando a experiência do usuário através de respostas em áudio.

## Estrutura do Projeto
O projeto está organizado da seguinte forma:
```
Gysin-IA.v13/
│
├── api/                   # Clientes e interfaces para APIs
│   ├── openai_client.py   # Cliente para a API OpenAI
│   └── init.py
│
├── googlecloud/           # Integração com Google Cloud
│   ├── text_to_speech.py  # Conversão de texto para fala
│   ├── credencial.json    # Credenciais de serviço Google
│   └── init.py
│
├── gui/                   # Interface gráfica do usuário
│   ├── chat_widget.py     # Widget de chat
│   ├── language_utils.py  # Utilitários de detecção de idioma
│   ├── main_window.py     # Janela principal da aplicação
│   └── init.py
│
├── tests/                 # Testes unitários
│   ├── test_language_detection.py
│   ├── test_text_to_speech.py
│   └── init.py
│
├── .env                   # Variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git
└── main.py                # Ponto de entrada da aplicação
```
## Requisitos
Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Google Cloud Platform Account
- OpenAI API Key

## Instalação
### Siga os passos abaixo para instalar e configurar o projeto:

| 1. **Clone o Repositório** |
|---|


   ```bash
   git clone https://github.com/seu-usuario/gysin-ia.git
   cd gysin-ia/Gysin-IA.v13


Crie um Ambiente Virtual
python -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate


Instale as Dependências
pip install -r requirements.txt


Configuração das Variáveis de Ambiente

Copie o arquivo .env.example para .env e insira suas chaves de API:OPENAI_API_KEY=your_openai_api_key
GOOGLE_APPLICATION_CREDENTIALS=googlecloud/credencial.json




Configuração do Google Cloud

Ative a API Text-to-Speech no Google Cloud Console.
Baixe as credenciais JSON e salve como googlecloud/credencial.json.


Execução da Aplicação
python main.py



Uso
Após a inicialização, a aplicação abrirá uma janela de chat onde você pode interagir com a assistente virtual Gysin IA. Use o campo de entrada de texto para enviar mensagens e receba respostas em texto ou áudio.
Características

Detecção Automática de Idioma: Identifica o idioma do texto de entrada e responde apropriadamente.
Respostas em Áudio: Converte respostas de texto em áudio utilizando Google Cloud Text-to-Speech.
Suporte Multilíngue: Responde em múltiplos idiomas, incluindo Português, Inglês, Alemão e Espanhol.

Desenvolvimento
Para contribuir com o projeto, siga as etapas de instalação e certifique-se de que todos os testes passem antes de enviar um pull request. Utilize os arquivos de teste na pasta tests/ para validar suas alterações.
Contato
Para mais informações ou suporte, entre em contato com Stefano Gysin em StefanoGysin@hotmail.com.
