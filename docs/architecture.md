# Architecture and Design

## Pattern
The prototype uses a lightweight layered, modular monolith. The HTTP handler routes requests and serializes responses; domain modules hold authentication, menu, and order operations; the browser client renders data and gathers user input. This keeps a classroom build simple to run while retaining boundaries that can later be moved behind a framework or database.

## Module diagram
```mermaid
flowchart LR
  U[Student or staff browser] -->|HTTP and JSON| API[Python HTTP API]
  API --> AUTH[Authentication module]
  API --> MENU[Menu module]
  API --> ORDER[Order module]
  API --> WEB[Static browser interface]
  AUTH --> MEM[(Process memory prototype)]
  MENU --> MEM
  ORDER --> MEM
```

## Class diagram
```mermaid
classDiagram
  class User {
    +name: str
    +email: str
    +student_id: str
    +password_hash: str
    +register()
    +login()
  }
  class Cafeteria {
    +name: str
    +get_menu()
  }
  class MenuItem {
    +id: str
    +name: str
    +price: decimal
    +category: str
  }
  class Order {
    +order_id: str
    +student_id: str
    +items: list
    +total_price: decimal
    +status: str
    +create()
    +update_status()
  }
  User "1" --> "0..*" Order : places
  Cafeteria "1" o-- "1..*" MenuItem : offers
  Order "1" --> "1..*" MenuItem : contains
```

## Sequence diagram for placing an order
```mermaid
sequenceDiagram
  actor User
  participant UI as Browser UI
  participant API as HTTP API
  participant Order as Order service
  User->>UI: Select items and enter campus ID
  UI->>API: POST /api/orders
  API->>Order: validate and create order
  Order->>Order: calculate total and assign ID
  Order-->>API: Order
  API-->>UI: 201 order ID, total, status
  UI-->>User: Show confirmation and tracking ID
```

## Component and package diagram
```mermaid
flowchart TB
  subgraph Presentation
    HTML[frontend/index.html]
    JS[frontend/app.js]
  end
  subgraph Application
    HTTP[backend/app.py HTTP routes]
  end
  subgraph Domain
    A[backend/auth.py]
    M[backend/menu.py]
    O[backend/order.py]
  end
  subgraph Quality
    T[tests/test_project.py]
    CI[GitHub Actions]
  end
  HTML --> JS --> HTTP
  HTTP --> A
  HTTP --> M
  HTTP --> O
  CI --> T
  T --> A
  T --> M
  T --> O
```

## Design pattern example
The application uses a small Factory Method through `Order.create(...)`: it validates input, computes totals, creates the ID, and stores the order while callers depend on the returned `Order` model. This centralizes construction rules. A later refactor could inject repositories and an event publisher rather than keep module-level memory stores.

## Security and limitations
The prototype's menu is static; order and account state is volatile. The API has no session, access control, authorization boundary, durable audit trail, or payment integration, so its demo status update endpoint is not safe for deployment. Prices must be retrieved by item ID on the server. A production design should add a database, secure identity/session handling, staff-only status updates, user-specific order authorization, payment-provider hosted checkout/tokenization, HTTPS, CSRF protection where applicable, request throttling, and audit logging. Real-time tracking would use polling or server-sent events after reliable state storage is introduced.