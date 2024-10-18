import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class OpenAIClient:
    def __init__(self):
        # Obtém a chave da API das variáveis de ambiente
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("A chave da API OpenAI não foi encontrada nas variáveis de ambiente.")
        
        # Inicializa o cliente OpenAI
        self.client = OpenAI(api_key=self.api_key)

    def get_response(self, prompt, max_tokens=150):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # Ou outro modelo disponível
                messages=[
                    {"role": "system", "content": "Você é uma assistente virtual chamada Gysin IA, desenvolvida para ser útil, criativa e amigável."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Erro ao obter resposta da API OpenAI: {e}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação."

    def generate_image(self, prompt):
        try:
            response = self.client.images.generate(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            return image_url
        except Exception as e:
            print(f"Erro ao gerar imagem com a API OpenAI: {e}")
            return None