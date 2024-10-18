# Gysin IA

Gysin IA é um assistente virtual inteligente desenvolvido por Stefano Gysin, utilizando a API da OpenAI GPT-4 e uma interface gráfica moderna construída com PySide6.

## Estrutura do Projeto
```
Gysin-IA.v13/
│
├── .env # Arquivo de configuração com chaves de API
├── main.py # Ponto de entrada da aplicação
├── README.md # Este arquivo
│
├── api/
│ ├── init.py
│ └── openai_client.py # Cliente para interação com a API da OpenAI
│
├── gui/
│ ├── init.py
│ ├── main_window.py # Janela principal da aplicação
│ └── chat_widget.py # Widget personalizado para o chat
│
└── resources/
└── icons/
└── cil-cursor.png # Ícone para o botão de enviar
```
## Requisitos

- Python 3.7+
- PySide6
- OpenAI Python Client
- python-dotenv

## Instalação

1. Clone o repositório:
git clone github.com
cd Gysin-IA.v13
2. Instale as dependências:
pip install -r requirements.txt
3. Configure o arquivo `.env` com sua chave de API da OpenAI:
OPENAI_API_KEY=sua_chave_api_aqui
## Uso

Execute o script principal para iniciar a aplicação:

python main.py
## Características

- Interface gráfica moderna e responsiva
- Integração com a API GPT-4 da OpenAI
- Chat em tempo real com o assistente virtual
- Indicador visual de "digitação" do assistente
- Tratamento de erros e feedback visual

## Desenvolvimento

### Passo 1: Configuração do Ambiente
- Configurar o ambiente virtual Python
- Instalar as dependências necessárias

### Passo 2: Estruturação do Projeto
- Criar a estrutura de diretórios do projeto
- Inicializar os arquivos principais e módulos

### Passo 3: Implementação da API Client
- Desenvolver o `openai_client.py` para interagir com a API da OpenAI
- Implementar métodos para obter respostas e gerar imagens

### Passo 4: Desenvolvimento da GUI
- Criar `main_window.py` para a janela principal
- Desenvolver `chat_widget.py` para o widget de chat personalizado

### Passo 5: Integração
- Conectar a GUI com o cliente da API
- Implementar a lógica de envio e recebimento de mensagens

### Passo 6: Testes e Refinamento
- Realizar testes de funcionalidade e usabilidade
- Refinar a interface do usuário e corrigir bugs

### Passo 7: Documentação
- Criar o README.md com instruções detalhadas
- Documentar o código-fonte

## Contribuindo

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de submeter pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Stefano Gysin - StefanoGysin@hotmail.com

Link do Projeto: [https://github.com/seu-usuario/Gysin-IA.v13](https://github.com/seu-usuario/Gysin-IA.v13)