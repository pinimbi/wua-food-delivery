# WUA Cafeteria Express Project Proposal

## Problem
Students and staff at the Women’s University in Africa may need to visit or contact several campus food outlets to learn what is available, place an order, and find out whether it is ready. This fragmented process makes menu comparison and collection planning harder. WUA Cafeteria Express proposes a single campus web interface for cafeteria menus, ordering, and order progress.

## Objectives
1. Present menus from multiple campus cafeterias with clear item prices.
2. Let a campus user assemble and submit an order with a campus identifier.
3. Give the user an order ID and current order state.
4. Establish a maintainable foundation with modular code, version control, tests, and CI.

## Scope and key features
The prototype provides sample menus for two cafeterias, a responsive browser interface, an in-memory JSON API, order totals, status lookup, a registration/login module with salted password hashing, input checks, automated tests, and a GitHub Actions test workflow. The prototype does not integrate a payment provider, campus identity service, database, courier dispatch, or production-grade real-time tracking. Menu prices are illustrative and must be validated by WUA before use.

## Users and success criteria
Students and staff browse menus, place orders, and check progress. Cafeteria staff would update order states in a future authenticated staff interface. Initial acceptance is met when a user can browse at least five menu items, create a valid order with the correct total, retrieve it by ID, and see an updated status, while invalid inputs are rejected and the automated suite passes.

## Proposed implementation
A small modular Python HTTP API serves JSON and the browser interface. The interface communicates through fetch requests. In-memory storage keeps the setup lightweight for a classroom demonstration. A layered separation between HTTP handling, domain modules, and the presentation makes later migration to a database and framework possible.

## Delivery plan
Work is organized as one-week increments: repository and setup; backlog and scope; proposal and risk review; requirements and UML; detailed design; architecture; pattern refactoring; unit tests; CI; and final sprint tracking and presentation. See `gantt.csv` and `sprint_plan.md`.