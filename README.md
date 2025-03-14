# Programacao-em-Par-plus-TDD# Projeto: Função "Olá, Mundo!" em Diferentes Idiomas (com TDD)

Este projeto demonstra como aplicar **Test-Driven Development (TDD)** em um exemplo simples de uma função que retorna "Olá, Mundo!" em diferentes idiomas. O fluxo básico é:

1. **Escrever o teste primeiro** (arquivo de teste).
2. **Fazer o teste falhar** (não há implementação ou não atende às expectativas).
3. **Implementar o código mínimo** para o teste passar.
4. **Refatorar**, mantendo os testes sempre passando.

---

## Estrutura de Pastas e Arquivos

```
.
├── ola_mundo.py
├── test_ola_mundo.py
└── README.md  (este arquivo)
```

- **`ola_mundo.py`**: Contém a função `ola_mundo_idioma`, responsável por retornar as diferentes traduções de "Olá, Mundo!".
- **`test_ola_mundo.py`**: Arquivo de teste com a classe de testes que verifica se a função retorna o resultado esperado para diferentes idiomas.
- **`README.md`**: Documentação do projeto (você está lendo agora).

---

## Como Executar

1. **Instale o Python** (3.x ou superior).
2. Faça o download/clone deste repositório.
3. Navegue até a pasta do projeto e execute os testes usando:

   ```bash
   python -m unittest test_ola_mundo.py
   ```
   
   ou

   ```bash
   python -m unittest discover
   ```

Se tudo estiver correto, você verá algo como:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## Visão Geral do Código

### Arquivo `ola_mundo.py`

```python
def ola_mundo_idioma(idioma: str) -> str:
    traducoes = {
        'pt': 'Olá, Mundo!',
        'en': 'Hello, World!',
        'es': 'Hola, Mundo!',
        'fr': 'Bonjour, Monde!'
    }
    return traducoes.get(idioma, 'Olá, Mundo!')


if __name__ == '__main__':
    # Exemplo de uso
    for lang in ['pt', 'en', 'es', 'fr', 'xx']:
        print(f'Idioma: {lang} -> {ola_mundo_idioma(lang)}')
```

- **Objetivo**: Retornar a string correspondente ao idioma fornecido.
- **Fallback**: Caso o idioma não seja reconhecido, retorna `"Olá, Mundo!"`.

### Arquivo `test_ola_mundo.py`

```python
import unittest
from ola_mundo import ola_mundo_idioma

class TestOlaMundo(unittest.TestCase):
    def test_portugues(self):
        self.assertEqual(ola_mundo_idioma('pt'), 'Olá, Mundo!')

    def test_ingles(self):
        self.assertEqual(ola_mundo_idioma('en'), 'Hello, World!')

    def test_espanhol(self):
        self.assertEqual(ola_mundo_idioma('es'), 'Hola, Mundo!')

    def test_frances(self):
        self.assertEqual(ola_mundo_idioma('fr'), 'Bonjour, Monde!')

    def test_padrao(self):
        self.assertEqual(ola_mundo_idioma('xx'), 'Olá, Mundo!')

if __name__ == '__main__':
    unittest.main()
```

- **Testes**: Validam se a função `ola_mundo_idioma` está retornando corretamente as traduções para cada idioma previsto.
- **Caso Padrão**: Testa o comportamento com um idioma não suportado para garantir que retorne `"Olá, Mundo!"`.

---

## Colaboração e TDD

Este projeto foi desenvolvido em um contexto de **pair programming** e **TDD**, com dois estudantes alternando papéis:
- **Estudante A**: Criou o arquivo de teste definindo as expectativas.
- **Estudante B**: Implementou o código para que o teste fosse aprovado.
- **Refatoração**: Em seguida, revisaram o código e os testes juntos, assegurando que tudo continuasse passando.

---

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma nova branch para sua feature ou correção de bug.
3. Adicione ou ajuste testes antes de implementar mudanças.
4. Implemente a solução de forma que todos os testes passem.
5. Faça um pull request com sua contribuição.

---

## Licença

Este projeto é disponibilizado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para usar, modificar e distribuir conforme as necessidades do seu projeto.