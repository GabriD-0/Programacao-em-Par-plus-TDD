
def ola_mundo_idioma(idioma:str) -> str:
    traducoes = {
        'pt': 'Ola Mundo',
        'en': 'Hello World',
        'es': 'Hola Mundo',
        'fr': 'Bonjour le monde',
        'it': 'Ciao Mondo',
        'de': 'Hallo Welt',
        'ja': 'こんにちは世界'
    }
    return traducoes.get(idioma, "Olá, Mundo!")


if __name__ == '__main__':
    for lang in ['pt', 'en', 'es', 'fr', 'it', 'de', 'ja']:
        print(f'Idioma: {lang}-> {ola_mundo_idioma(lang)}')	
