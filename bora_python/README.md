# Bora Pro Racha

Aplicação para agendamento de quadras e gerenciamento de reservas (backend em Python + frontend estático). Este repositório contém código de exemplo, serviços e mocks usados para desenvolvimento e testes.

Principais pontos:
- Módulos: `domain/`, `services/`, `mock/`, `tests/`.
- Para rodar rápido: `python main.py` (requer dependências em `requirements.txt`).
- Testes: `pytest`.

Se precisar, posso publicar este conteúdo no repositório GitHub que você indicou e manter `mock/mock_data.py` como fonte de dados.
- Completação gradual de dados do usuário

### 3. **AGENDAMENTO FÁCIL** (EasyBookingService)
- Seleção rápida de horários
- Criação de reservas simplificada
- Confirmação de reservas

### 4. **FILTRO DINÂMICO** (FilterService)
- Filtro por localização
- Filtro por esporte
- Filtro por preço
- Filtro avançado combinado
- Ordenação por preço e avaliação

### 5. **ESPAÇOS DETALHADOS** (DetailedSpaceService)
- Informações completas de espaços
- Sistema de avaliações (1-5 estrelas)
- Comentários de usuários
- Relatórios de espaços

### 6. **CADASTRO DINÂMICO** (DynamicSpaceRegistrationService)
- Registro de novos espaços
- Atualização de espaços
- Relatório de registro
- Verificação de disponibilidade

### 7. **LEMBRETES INTERATIVOS** (ReminderService)
- Agendamento de lembretes
- Envio de notificações
- Histórico de lembretes
- Estatísticas de lembretes

### 8. **FUSO HORÁRIO DINÂMICO** (TimezoneService)
- Gerenciamento de timezones
- Conversão de horários
- Validação de timezones
- Relatório de distribuição

### 9. **CANCELAMENTOS** (CancellationService)
- Políticas de cancelamento
- Cálculo de taxas
- Reembolsos
- Histórico de cancelamentos

### 10. **CHECK-IN** (CheckinService)
- Geração de código QR
- Confirmação de check-in
- Recibos de check-in
- Relatório de check-ins

---

## 🏗️ Arquitetura e Padrões de Design

### Domain Layer
```
domain/
├── base.py                 # BaseEntity, EntityComStatus
├── interfaces.py           # ABC Interfaces (Polimorfismo)
├── user.py                 # User Entity
├── space.py                # Space Entity
├── booking.py              # Booking Entity
├── timeslot.py             # TimeSlot Entity
├── notification.py         # Notification Entity
├── filtro.py               # Strategy Pattern - Filtros
└── estrategia_calculo.py   # Strategy Pattern - Cálculos
```

### Services Layer
```
services/
├── base.py                              # BaseService
├── base_repository.py                   # Generic Repository Pattern
├── sync_service.py                      # Sincronização
├── quick_registration_service.py        # Cadastro Rápido
├── easy_booking_service.py              # Agendamento Fácil
├── filter_service.py                    # Filtros Dinâmicos
├── detailed_space_service.py            # Espaços Detalhados
├── dynamic_space_registration_service.py # Cadastro Dinâmico
├── reminder_service.py                  # Lembretes
├── timezone_service.py                  # Timezones
├── cancellation_service.py              # Cancelamentos
└── checkin_service.py                   # Check-in
```

### Padrões de Design Implementados

1. **Strategy Pattern**
   - `FiltroEspaco` (filtros intercambiáveis)
   - `EstrategiaCalculo` (cálculos intercambiáveis)

2. **Composite Pattern**
   - `FiltroCombinado` (múltiplos filtros)

3. **Repository Pattern**
   - `BaseRepository` (operações CRUD genéricas)

4. **Factory Pattern**
   - Geração de IDs únicos em serviços

5. **Encapsulation (Encapsulamento)**
   - Atributos privados com `@property`
   - Validação em setters

6. **Inheritance & Polymorphism**
   - Hierarquia de entities com `BaseEntity`
   - Interfaces abstratas (`ABC`)

---

## 📦 Instalação e Uso

### Pré-requisitos
- Python 3.9+
- pip ou conda

### Instalação

```bash
# Clone ou navegue para o diretório
cd bora_python

# Instale as dependências
pip install -r requirements.txt

# (Opcional) Instale em modo desenvolvimento
pip install -e .
```

### Executar a Aplicação Principal

```bash
python main.py
```

### Executar os Testes

```bash
# Todos os testes
pytest

# Com coverage
pytest --cov=domain --cov=services --cov-report=html

# Testes específicos
pytest tests/test_domain.py
pytest tests/test_services.py

# Modo verbose
pytest -v

# Parar no primeiro erro
pytest -x
```

---

## 📁 Estrutura de Diretórios

```
bora_python/
├── domain/                    # Domain Layer (Entities, Value Objects)
│   ├── __init__.py
│   ├── base.py               # Base classes
│   ├── interfaces.py         # Abstract interfaces
│   ├── user.py               # User entity
│   ├── space.py              # Space entity
│   ├── booking.py            # Booking entity
│   ├── timeslot.py           # TimeSlot entity
│   ├── notification.py       # Notification entity
│   ├── filtro.py             # Filter strategies
│   └── estrategia_calculo.py # Calculation strategies
│
├── services/                  # Application Layer (Business Logic)
│   ├── __init__.py
│   ├── base.py               # Base service
│   ├── base_repository.py    # Generic repository
│   ├── sync_service.py       # Feature 1
│   ├── quick_registration_service.py    # Feature 2
│   ├── easy_booking_service.py          # Feature 3
│   ├── filter_service.py                # Feature 4
│   ├── detailed_space_service.py        # Feature 5
│   ├── dynamic_space_registration_service.py  # Feature 6
│   ├── reminder_service.py              # Feature 7
│   ├── timezone_service.py              # Feature 8
│   ├── cancellation_service.py          # Feature 9
│   └── checkin_service.py               # Feature 10
│
├── mock/                      # Test Data Layer
│   ├── __init__.py
│   └── mock_data.py          # Sample data
│
├── tests/                     # Test Layer
│   ├── __init__.py
│   ├── conftest.py           # pytest configuration
│   ├── test_domain.py        # Entity tests
│   └── test_services.py      # Service tests
│
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── setup.py                   # Package configuration
├── pytest.ini                 # pytest configuration
└── README.md                  # This file
```

---

## 🔍 Exemplos de Uso

### Filtrar Espaços

```python
from services.filter_service import FilterService
from mock.mock_data import mock_spaces

filter_service = FilterService()

# Filtro simples
maceio_spaces = filter_service.filtrar_por_local(mock_spaces, "Maceió")
futebol_spaces = filter_service.filtrar_por_esporte(mock_spaces, "Futebol")
barato = filter_service.filtrar_por_preco(mock_spaces, 100)

# Filtro avançado (combinado)
resultado = filter_service.filtrar_avancado(
    mock_spaces,
    local="Maceió",
    esporte="Futebol",
    preco_maximo=150
)
```

### Criar e Confirmar Reserva

```python
from services.easy_booking_service import EasyBookingService
from domain.timeslot import TimeSlot
from datetime import datetime, timedelta

service = EasyBookingService()

# Selecionar horário
inicio = datetime.now()
fim = inicio + timedelta(hours=1)
slot = TimeSlot("t1", "s1", inicio, fim)
service.selecionar_horario(slot)

# Criar reserva
reserva = service.criar_reserva_rapida("u1", "s1", "t1", 100.0)
print(f"Reserva: {reserva.id}")

# Confirmar
reserva_confirmada = service.confirmar_reserva(reserva)
print(f"Status: {reserva_confirmada.status}")
```

### Gerenciar Avaliações

```python
from services.detailed_space_service import DetailedSpaceService
from mock.mock_data import mock_spaces

service = DetailedSpaceService()
space = mock_spaces[0]

# Adicionar avaliações
service.adicionar_avaliacao(space.id, 5)
service.adicionar_avaliacao(space.id, 4)
service.adicionar_avaliacao(space.id, 5)

# Obter média
media = service.obter_media_avaliacoes(space.id)
print(f"Avaliação média: {media:.1f} ⭐")

# Adicionar comentários
service.adicionar_comentario(space.id, "Excelente!")
comentarios = service.obter_comentarios(space.id)
```

---

## 🧪 Testes

### Cobertura de Testes

- **test_domain.py**: Testes das entities (User, Space, Booking, etc.)
  - ✓ 20+ testes unitários
  - Validação de criação
  - Transições de estado
  - Cálculos

- **test_services.py**: Testes dos serviços
  - ✓ 30+ testes unitários
  - Filtragem
  - Agendamento
  - Cancelamentos
  - Check-in

### Executar Cobertura

```bash
pytest --cov=domain --cov=services --cov-report=html
# Abra htmlcov/index.html no navegador
```

---

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` (opcional):

```env
DEBUG=true
LOG_LEVEL=INFO
```

### Logging

Logs são configurados automaticamente em `services/base.py`:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

---

## 🚀 Recursos Avançados

### 1. Encapsulamento com Properties

```python
class User(BaseEntity):
    def __init__(self, id, nome, email):
        super().__init__(id)
        self._nome = nome
        self._email = email
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor
```

### 2. Strategy Pattern

```python
# Diferentes estratégias de filtro
class FiltroPorLocal(FiltroEspaco):
    def aplicar(self, espacos):
        return [e for e in espacos if e.localizacao == self.local]

class FiltroPorPreco(FiltroEspaco):
    def aplicar(self, espacos):
        return [e for e in espacos if e.preco <= self.maximo]

# Usar combinado
filtro_combinado = FiltroCombinado([
    FiltroPorLocal("Maceió"),
    FiltroPorPreco(150)
])
```

### 3. Generic Types

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class IRepository(Generic[T]):
    def find_all(self) -> List[T]: pass
    def save(self, entity: T) -> T: pass
```

---

## 📚 Técnicas Python Utilizadas

- ✓ **Type Hints** - Anotações de tipo para melhor IDE support
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
