# Requirements and Use Cases

## Functional requirements
- FR1: A visitor can view cafeterias and browse each menu with item names, categories, and prices.
- FR2: A campus user can register with name, valid email, student/staff ID, and a password of at least eight characters.
- FR3: A registered user can log in; password values are stored as salted PBKDF2-HMAC-SHA256 digests in the prototype process.
- FR4: A user can submit one or more menu items with quantities and receive a unique order ID and total.
- FR5: A user can retrieve an order by its ID and see its status.
- FR6: An authorized staff member will be able to update order status in the target system; the prototype API demonstrates the status update operation without production authorization.
- FR7: The system rejects malformed email, missing identity, empty orders, invalid quantities, unknown orders, and unrecognized statuses.
- FR8: The system exposes a health endpoint and runs tests in CI on pushes and pull requests.

## Non-functional requirements
- Security: hash passwords; validate inputs; avoid collecting payment credentials; production requires TLS, authorization, rate limits, secure sessions, secrets management, and a reviewed password/KDF policy.
- Reliability: invalid requests return clear errors; totals are computed server-side; automated tests cover core operations.
- Usability: responsive layout, readable labels, visible totals, and a clear order-status lookup.
- Maintainability: keep HTTP, authentication, menus, and orders in separate modules; document setup and scope.
- Performance: support a classroom demonstration with modest concurrent use. No production capacity claim is made.
- Privacy: the prototype uses memory-only records and should contain no real personal data.

## Use case UC1 Browse cafeteria menu
**Primary actor:** Student or staff member. **Preconditions:** The app is reachable. **Postconditions:** The selected menu is displayed; no order is changed.

1. User opens the menu page.
2. System lists cafeterias and selects the default.
3. User selects a cafeteria or refreshes its menu.
4. System displays available items, categories, and prices.

**Alternate flows:** If the cafeteria name is unknown, the system shows an empty menu. If the service is unavailable, the interface displays an error.

## Use case UC2 Place an order
**Primary actor:** Student or staff member. **Preconditions:** Menu is available; the user has selected one or more items. **Postconditions:** A new order is recorded with status `placed`, total, and order ID.

1. User adds menu items and adjusts quantities in the basket.
2. User enters a campus identifier and chooses Place order.
3. Interface sends item identifiers, quantities, prices, and campus identifier to the API.
4. System validates required fields, quantity, and price values and calculates the total on the server.
5. System stores the order and returns its ID, total, and initial status.
6. Interface displays the confirmation and makes the ID available for tracking.

**Alternate flows:** Missing ID or empty basket returns a validation error. Invalid quantity or negative price is rejected. A production implementation must look up prices server-side from a trusted catalog rather than trust client-submitted prices.

## Use case UC3 Track and update an order
**Primary actors:** Student/staff user; cafeteria staff (status update). **Preconditions:** Order exists. **Postconditions:** User sees current status; when staff updates, the new valid status is saved.

1. User enters an order ID and asks for its status.
2. System looks up the order.
3. System displays the current state.
4. Staff selects a valid next status in a future staff interface.
5. System checks authorization and allowed transition, saves it, and exposes it to the tracking view.

**Alternate flows:** Unknown ID returns not found. Invalid status is rejected. Production must enforce identity, ownership, staff authorization, and transition rules.