# Bora Pro Racha

Projeto para a disciplina de Projeto de Software: sistema de agendamento de quadras (Python backend + SPA frontend).

Rápido:
- Pré-requisitos: Python 3.9+
- Instalar: `pip install -r requirements.txt`
- Executar: `python main.py`
- Testes: `pytest`

Estrutura principal:
- `domain/`, `services/`, `mock/`, `frontend/index.html`, `tests/`

Uso educacional — não contém canal de suporte.

Se quiser, faço um push final para o repositório remoto (substituindo o conteúdo lá) ou adiciono um CHANGELOG curto. 
- ✓ **ABC (Abstract Base Classes)** - Interfaces abstratas
- ✓ **Properties** - Getters/Setters com validação
- ✓ **Decorators** - @property, @abstractmethod
- ✓ **Generics** - TypeVar, Generic para tipos genéricos
- ✓ **Context Managers** - Para gerenciamento de recursos
- ✓ **List Comprehensions** - Filtragem elegante de listas
- ✓ **F-strings** - Formatação moderna de strings
- ✓ **Dataclasses** - (Futuro) Para entities mais simples
- ✓ **Logging** - Sistema de logs estruturado

---

## 🤝 Comparação TypeScript vs Python

| Aspecto | TypeScript | Python |
|--------|-----------|--------|
| Encapsulamento | `private`/`public` | Convenção `_private` + properties |
| Interfaces | `interface` | ABC (Abstract Base Class) |
| Tipos | Type Annotations | Type Hints |
| Herança | `extends` | `super()` |
| Propriedades | Getters/Setters | `@property` |
| Genéricos | `<T>` | `TypeVar`, `Generic` |
| Testes | Jest | pytest |
| Empacotamento | npm | pip |

---

## 📝 Convenções de Código

### Nomenclatura

- **Classes**: `PascalCase` (ex: `UserService`)
- **Funções**: `snake_case` (ex: `obter_usuario`)
- **Constantes**: `UPPER_CASE` (ex: `MAX_RETRIES`)
- **Privado**: Prefixo `_` (ex: `_validar`)

### Docstrings

```python
def obter_usuario(user_id: str) -> User:
    """
    Retrieve user by ID
    
    Args:
        user_id: The user identifier
        
    Returns:
        User object or None if not found
        
    Raises:
        ValueError: If user_id is invalid
    """
    pass
```

---

## 🐛 Troubleshooting

### Erro de Import

```
ModuleNotFoundError: No module named 'domain'
```

**Solução**: Execute a partir do diretório `bora_python`:
```bash
cd bora_python
python main.py
```

### Testes não encontrados

```
no tests ran
```

**Solução**: Certifique-se que `pytest` está instalado:
```bash
pip install pytest pytest-cov
```

---

## 📦 Dependências

- **pytest** (7.4.3+) - Framework de testes
- **pytest-cov** (4.1.0+) - Cobertura de testes
- Python 3.9+

---

## 📄 Licença

MIT License - Sinta-se livre para usar em projetos pessoais e comerciais.

---

## 👨‍💻 Desenvolvimento

### Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no repositório
- Entre em contato com o time de desenvolvimento

---

**Versão**: 1.0.0  
**Data**: Abril 2026  
**Status**: ✓ Completo e Testado
