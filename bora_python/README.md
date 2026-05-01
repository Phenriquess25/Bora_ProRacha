# Bora Pro Racha


## Instalação

1. Instale o Python 3.9 ou superior.
2. Crie e ative um ambiente virtual.
3. Instale as dependências com:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação com:

```bash
python main.py
```

5. Execute os testes com:

```bash
pytest
```

Frontend — Como rodar

Se quiser usar a interface do frontend localizada em `frontend/index.html` siga um destes métodos:

- Abrir diretamente no navegador:

	- Abra o arquivo `frontend/index.html` no seu navegador (Chrome/Firefox). Certifique-se de que a API esteja rodando em `http://127.0.0.1:5000` e que `API_BASE` em `frontend/index.html` aponte para esse endereço.

- Servir com um servidor HTTP simples (recomendado):

	- Navegue até a pasta `frontend` e rode um servidor HTTP leve (Python 3.x):

```bash
cd frontend
python -m http.server 8000
```

	- Abra `http://localhost:8000` no navegador. Isso evita problemas de CORS/arquivos locais.

Pré-requisitos para rodar o frontend

- Navegador moderno (Chrome, Firefox, Edge).
- Backend rodando em `http://127.0.0.1:5000` (ver `api/app.py`).
- Se usar o servidor estático, Python 3 instalado (para `python -m http.server`).

Observações

- O frontend é uma SPA estática em `frontend/index.html` e não precisa de build nem Node.js. Ele faz chamadas `fetch()` para a API; garanta que o `API_BASE` dentro do arquivo aponte para o servidor Flask.
- Para desenvolvimento local, ative o backend primeiro com:

```bash
python api/app.py
```




# Funcionalidades e Como Foram Implementadas

## 1. Sincronização de horários

Onde está:

* [services/sync_service.py](services/sync_service.py)
* [domain/timeslot.py](domain/timeslot.py)
* [domain/booking.py](domain/booking.py)
* [domain/space.py](domain/space.py)

Como foi implementado:
A sincronização é feita pelo `SyncService`, que percorre os espaços, os intervalos de tempo e as reservas existentes.

A reserva fica com o estado controlado por `Booking`, o espaço pode entrar em manutenção com `Space`, e o `TimeSlot` muda entre `DISPONIVEL`, `RESERVADO` e `BLOQUEADO`. Assim, o serviço mantém a disponibilidade coerente com o estado real do sistema.

Conceitos aplicados:

* Encapsulamento (cada entidade controla seu próprio estado)
* Modelagem por estados

---

## 2. Cadastro rápido

Onde está:

* `domain/user.py`

Como foi implementado:
A entidade `User` controla os dados do usuário e seu nível de completude (parcial ou completo). As validações são feitas através de propriedades (`@property` e setters).

Conceitos aplicados:

* Encapsulamento
* Abstração

---

## 3. Agendamento fácil

Onde está:

* `domain/booking.py`

Como foi implementado:
O fluxo de agendamento (selecionar horário, reservar e confirmar) é implementado através de métodos dentro da classe `Booking`, que controla as transições de estado da reserva.

Conceitos aplicados:

* Encapsulamento
* Modelagem de estados

---

## 4. Filtro dinâmico

Onde está:

* `domain/filtro.py`
* `services/filter_service.py`
* `domain/interfaces.py`

Como foi implementado:
Os filtros foram implementados como classes que seguem a interface `IFiltro`. Cada filtro possui sua própria lógica no método `aplicar()`.

O `FilterService` recebe qualquer filtro e executa sem conhecer sua implementação.

```python
filtro.aplicar(lista)
```

Conceitos aplicados:

* Polimorfismo
* Abstração
* Strategy Pattern

---

## 5. Espaços detalhados

Onde está:

* `domain/space.py`

Como foi implementado:
A classe `Space` centraliza todas as informações do espaço, como localização, preço e horários disponíveis.

Conceitos aplicados:

* Encapsulamento
* Modelagem de entidade

---

## 6. Cadastro de espaço dinâmico

Onde está:

* `domain/space.py`

Como foi implementado:
A própria entidade `Space` possui métodos responsáveis por alterar seu estado, como adicionar horários, bloquear disponibilidade e atualizar informações.

Conceitos aplicados:

* Encapsulamento
* Responsabilidade única

---

## 7. Lembrete interativo

Onde está:

* [services/reminder_service.py](services/reminder_service.py)
* [domain/notification.py](domain/notification.py)
* [domain/booking.py](domain/booking.py)

Como foi implementado:
O `ReminderService` cria uma `Notification` do tipo `REMINDER` para uma reserva e guarda os lembretes pendentes. Depois ele pode enviar, cancelar ou listar esses lembretes.

Conceitos aplicados:

* Separação de responsabilidades
* Encapsulamento
* Uso de entidades para notificação

---

## 8. Fuso horário dinâmico

Onde está:

* [services/timezone_service.py](services/timezone_service.py)
* [domain/space.py](domain/space.py)

Como foi implementado:
O `TimezoneService` valida fusos horários, ajusta o fuso de um espaço e também faz conversão simplificada entre horários. O campo `timezone` da classe `Space` guarda essa informação.

Conceitos aplicados:

* Abstração
* Validação de dados
* Organização da lógica de domínio

---

## 9. Cancelamentos

Onde está:

* `domain/booking.py`

Como foi implementado:
A classe `Booking` possui métodos que alteram o estado da reserva para cancelado, além de possíveis regras associadas (como taxa ou liberação do horário).

Conceitos aplicados:

* Encapsulamento
* Modelagem por estados

---

## 10. Confirmação de agendamento (check-in)

Onde está:

* [services/checkin_service.py](services/checkin_service.py)
* [domain/booking.py](domain/booking.py)

Como foi implementado:
O `CheckinService` gera um código QR, valida se a reserva está confirmada e então chama `Booking.realizar_checkin()`. A própria reserva controla a mudança de estado para `CHECKIN_REALIZADO`.

Conceitos aplicados:

* Máquina de estados
* Encapsulamento
* Polimorfismo de comportamento via serviço



Herança aparece principalmente em [domain/base.py](domain/base.py), [domain/user.py](domain/user.py), [domain/space.py](domain/space.py), [domain/booking.py](domain/booking.py) e [services/base.py](services/base.py).

Como funciona:
[BaseEntity](domain/base.py) centraliza o id, a comparação entre objetos e a representação textual. [EntityComStatus](domain/base.py) estende essa base para entidades que precisam de status. Em outro ponto, [BaseService](services/base.py) concentra logger e validações reutilizáveis para todos os serviços.

Motivo de existir:
isso evita repetição, padroniza regras comuns e facilita manutenção. Se a forma de tratar id, status ou logging mudar, a alteração fica concentrada na classe base.

## Polimorfismo no projeto

Polimorfismo aparece principalmente em [domain/interfaces.py](domain/interfaces.py), [domain/filtro.py](domain/filtro.py), [domain/estrategia_calculo.py](domain/estrategia_calculo.py) e [services/filter_service.py](services/filter_service.py).

Como funciona:
as interfaces definem contratos como aplicar() e calcular(). As classes concretas implementam esses métodos de formas diferentes, mas o serviço chama sempre a mesma assinatura. Por isso [FilterService](services/filter_service.py) consegue receber qualquer filtro que implemente [IFiltro](domain/interfaces.py), e cada filtro decide sua própria lógica de execução.

Motivo de existir:
isso permite trocar regras sem alterar o serviço principal. O sistema fica mais flexível para adicionar novos filtros, novas estratégias de cálculo ou novos comportamentos de notificação sem reescrever as partes já prontas.

## Arquivos principais

- [domain/base.py](domain/base.py)
- [domain/interfaces.py](domain/interfaces.py)
- [domain/filtro.py](domain/filtro.py)
- [domain/estrategia_calculo.py](domain/estrategia_calculo.py)
- [domain/user.py](domain/user.py)
- [domain/booking.py](domain/booking.py)
- [domain/space.py](domain/space.py)
- [services/base.py](services/base.py)
- [services/filter_service.py](services/filter_service.py)
