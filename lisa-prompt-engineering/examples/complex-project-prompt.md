# Complex Project Lisa Prompt Example

Exemplo para projeto grande e complexo com múltiplas fases.

## Cenário
Construir uma aplicação completa de E-commerce com:
- Backend (Node.js/Express)
- Database (PostgreSQL)
- Frontend (React)
- Tests
- Documentação

## Arquivos Necessários

### 1. PROMPT.md
```markdown
# Mission
Build a complete E-commerce application with user authentication, product catalog, shopping cart, orders, and payment integration.

# Overview
This is a multi-phase project. Each phase has specific deliverables. Progress is tracked in IMPLEMENTATION_PLAN.md.

# Phase Definition

## Phase 1: Project Setup & Database
Objective: Initialize all infrastructure and database schema

Tasks:
1. Backend project initialization
2. Database schema design
3. Migrations setup
4. Environment configuration

Completion: All tasks in Phase 1 marked [x] in IMPLEMENTATION_PLAN.md

## Phase 2: User Authentication
Objective: Implement complete auth system

Requirements:
- User registration
- User login
- JWT token management
- Password hashing
- Auth middleware

Completion: All endpoints tested and Phase 2 marked [x]

## Phase 3: Product Management
Objective: Build product catalog system

Requirements:
- Create product
- List products with filters
- Get single product
- Update product
- Delete product
- Product categories

Completion: All endpoints tested and Phase 3 marked [x]

## Phase 4: Shopping Cart
Objective: Implement cart functionality

Requirements:
- Add to cart
- Remove from cart
- Update quantity
- Get cart
- Clear cart

Completion: All endpoints tested and Phase 4 marked [x]

## Phase 5: Orders
Objective: Build order system

Requirements:
- Create order from cart
- Get user orders
- Get order details
- Cancel order
- Order status tracking

Completion: All endpoints tested and Phase 5 marked [x]

## Phase 6: Frontend
Objective: Build React application

Components:
- Landing page
- Product listing
- Product detail
- Cart page
- Checkout
- Order history

Completion: All pages functional and Phase 6 marked [x]

## Phase 7: Integration & Testing
Objective: End-to-end testing and optimization

Tasks:
- Full application walkthrough
- Performance testing
- Security audit
- Bug fixes

Completion: All tests pass and Phase 7 marked [x]

## Phase 8: Deployment & Documentation
Objective: Prepare for production

Tasks:
- API documentation
- Deployment guide
- README with setup instructions
- Code cleanup

Completion: All documentation complete and Phase 8 marked [x]

# Process Per Iteration

1. Read IMPLEMENTATION_PLAN.md to identify current phase
2. Find first unchecked [ ] task in current phase
3. Implement that specific component/feature
4. Write tests (if backend) or verify functionality (if frontend)
5. Run test suite to verify nothing broke
6. Mark [x] in IMPLEMENTATION_PLAN.md for completed task
7. Commit with message: "feat: implement [PHASE] - [task name]"
8. Loop continues to next iteration

# Mandatory Verification

Before moving to next phase:
1. Read IMPLEMENTATION_PLAN.md from disk
2. Verify all tasks in current phase are [x]
3. Run full test suite: `npm test`
4. Verify no breaking changes
5. If any [ ] remains: continue working on current phase

Before completing project:
1. Read IMPLEMENTATION_PLAN.md - verify all phases [x]
2. Run full backend test suite: `npm test`
3. Run full frontend test suite: `cd frontend && npm test`
4. Run application end-to-end:
   - Start backend
   - Start frontend
   - Test user registration
   - Test product browsing
   - Test adding to cart
   - Test checkout process
5. Verify documentation is complete
6. If ALL above pass: output completion promise

# Completion Criteria

When:
- IMPLEMENTATION_PLAN.md shows ALL phases [x]
- Backend: `npm test` passes 100% (all tests green)
- Frontend: `cd frontend && npm test` passes 100%
- End-to-end flow works: user can register → browse → add to cart → checkout
- API is documented and accessible
- README includes setup and deployment instructions
- Code coverage >80% for all critical paths
- No console errors or warnings

OUTPUT THIS PROMISE:
<promise>ECOMMERCE_APPLICATION_COMPLETE_AND_TESTED</promise>

# Constraints
- One task per iteration (atomic progress)
- Always run tests within the iteration (don't leave for later)
- Update IMPLEMENTATION_PLAN.md immediately when task completed
- Commit after EVERY completed task (not at end of phase)
- If test fails: fix in same iteration before moving on
- Read IMPLEMENTATION_PLAN.md from disk each iteration (don't trust memory)
- Frontend and backend must not have circular dependencies
- Database migrations must be reversible
- Environment variables documented in .env.example
- No hardcoded values (use config files)
```

### 2. IMPLEMENTATION_PLAN.md
```markdown
# E-Commerce Application Implementation Plan

## Phase 1: Project Setup & Database
- [ ] Create Node.js backend project directory
- [ ] Initialize npm and install core dependencies (express, cors, dotenv)
- [ ] Setup PostgreSQL database connection
- [ ] Design database schema (ERD diagram)
  - users table (id, email, password_hash, name, created_at)
  - products table (id, name, description, price, category, stock, created_at)
  - cart_items table (id, user_id, product_id, quantity, added_at)
  - orders table (id, user_id, total, status, created_at, updated_at)
  - order_items table (id, order_id, product_id, quantity, price)
- [ ] Create and run database migrations
- [ ] Setup .env.example with required variables
- [ ] Create basic Express server structure
- [ ] Setup error handling middleware
- [ ] Setup CORS configuration
- [ ] Create database connection pool

## Phase 2: User Authentication (Backend)
- [ ] Install bcrypt and jsonwebtoken packages
- [ ] Create User model/schema
- [ ] Implement POST /api/auth/register endpoint
  - Validate email format
  - Check email uniqueness
  - Validate password strength (min 8 chars, uppercase, number, special)
  - Hash password with bcrypt
  - Create user in database
  - Return JWT token
- [ ] Implement POST /api/auth/login endpoint
  - Validate email/password format
  - Check user exists
  - Verify password hash
  - Generate and return JWT token
- [ ] Create auth middleware for protected routes
- [ ] Implement token refresh mechanism
- [ ] Implement password reset flow (optional)
- [ ] Write comprehensive auth tests
- [ ] Test auth edge cases (wrong password, nonexistent user, etc.)
- [ ] Verify tokens work for subsequent requests

## Phase 3: Product Management (Backend)
- [ ] Create Product model/schema
- [ ] Implement GET /api/products endpoint
  - List all products paginated (20 per page)
  - Support filtering by category
  - Support search by name/description
  - Support sorting (price, name, newest)
  - Return product count and total pages
- [ ] Implement GET /api/products/:id endpoint
  - Return single product details
  - Return 404 if not found
- [ ] Implement POST /api/products endpoint (admin only)
  - Validate product data
  - Create product in database
  - Return created product with ID
- [ ] Implement PUT /api/products/:id endpoint (admin only)
  - Update product fields
  - Validate changes
  - Return updated product
- [ ] Implement DELETE /api/products/:id endpoint (admin only)
  - Mark product as deleted (soft delete)
  - Return 204 on success
- [ ] Create product seeding script (test data)
- [ ] Write product management tests
- [ ] Test filtering and search functionality
- [ ] Test pagination edge cases
- [ ] Test authorization (admin vs regular user)

## Phase 4: Shopping Cart (Backend)
- [ ] Create Cart model/schema (or use cart_items table)
- [ ] Implement GET /api/cart endpoint
  - Return user's current cart items
  - Include product details (name, price)
  - Calculate total price
  - Return cart with all items
- [ ] Implement POST /api/cart/add endpoint
  - Accept productId and quantity
  - Validate product exists
  - Validate quantity > 0
  - Check product stock availability
  - Add or merge item in cart
  - Return updated cart
- [ ] Implement PUT /api/cart/:itemId endpoint
  - Update quantity for cart item
  - Validate quantity > 0
  - Return updated cart
- [ ] Implement DELETE /api/cart/:itemId endpoint
  - Remove item from cart
  - Return updated cart
- [ ] Implement POST /api/cart/clear endpoint
  - Remove all items from user's cart
  - Return empty cart
- [ ] Implement cart validation (stock checks)
- [ ] Write cart tests for all operations
- [ ] Test edge cases (out of stock, invalid quantity)
- [ ] Test cart persistence across sessions

## Phase 5: Orders (Backend)
- [ ] Create Order model/schema
- [ ] Implement POST /api/orders endpoint
  - Convert cart items to order
  - Validate cart not empty
  - Calculate order total
  - Create order in database with status "pending"
  - Create order items in database
  - Clear user's cart
  - Return created order with ID
- [ ] Implement GET /api/orders endpoint
  - Return all orders for authenticated user
  - Include order items and products
  - Support filtering by status
  - Return paginated results
- [ ] Implement GET /api/orders/:id endpoint
  - Return single order with all items
  - Verify user owns this order
  - Return 404 if not found
- [ ] Implement PUT /api/orders/:id/cancel endpoint
  - Only cancel if status is "pending"
  - Change status to "cancelled"
  - Return updated order
- [ ] Implement order status tracking
  - Status options: pending, confirmed, shipped, delivered, cancelled
- [ ] Implement payment integration endpoint (stub)
- [ ] Write comprehensive order tests
- [ ] Test order creation and item persistence
- [ ] Test authorization (user can only see own orders)
- [ ] Test status transitions

## Phase 6: Frontend - React Setup
- [ ] Create React project with Create React App
- [ ] Setup React Router for page navigation
- [ ] Create component directory structure
- [ ] Install axios for API calls
- [ ] Setup authentication context/state management
- [ ] Create .env with API base URL
- [ ] Setup basic layout component (header, nav, footer)
- [ ] Create main App.js with routing

## Phase 6: Frontend - Pages & Components
- [ ] Create Landing Page component
  - Featured products section
  - Call-to-action buttons
  - Links to product catalog
- [ ] Create Product Listing Page
  - Display products in grid/list
  - Filter by category
  - Search functionality
  - Sorting options (price, newest, etc.)
  - Pagination controls
  - Add to cart button on each product
- [ ] Create Product Detail Page
  - Display full product info
  - Product images/gallery
  - Price and availability
  - Quantity selector
  - Add to cart button
  - Related products section
- [ ] Create Shopping Cart Page
  - List all cart items
  - Show quantity and price per item
  - Edit quantity inline
  - Remove item button
  - Cart total calculation
  - Proceed to checkout button
- [ ] Create Checkout Page
  - Review order summary
  - Shipping address form
  - Payment method selection
  - Place order button
  - Order confirmation
- [ ] Create Order History Page
  - List user's past orders
  - Show order date, total, status
  - Order detail link
  - Cancel order button
- [ ] Create User Profile Page
  - Display user info
  - Edit profile form
  - Logout button
- [ ] Create Login/Register Page
  - Registration form with validation
  - Login form
  - Password validation feedback
  - Link between login and register

## Phase 6: Frontend - Integration
- [ ] Connect Product Listing to backend API
  - Fetch products on page load
  - Test filtering and search
  - Test pagination
- [ ] Connect Product Detail to backend API
  - Fetch single product data
  - Fetch related products
- [ ] Connect Cart to backend API
  - Add to cart integration
  - Get cart integration
  - Update quantity integration
  - Remove item integration
- [ ] Connect Checkout to backend API
  - Create order integration
  - Handle payment response
- [ ] Connect Order History to backend API
  - Fetch user orders
  - Fetch order details
  - Cancel order integration
- [ ] Connect Authentication
  - Register new user
  - Login user
  - Store JWT token
  - Logout functionality
  - Protect private routes
- [ ] Add loading states and error handling
- [ ] Add user feedback (success/error messages)

## Phase 7: Integration & Testing
- [ ] End-to-end testing:
  - [ ] New user registration flow
  - [ ] User login flow
  - [ ] Browse products
  - [ ] Search and filter products
  - [ ] View product details
  - [ ] Add multiple products to cart
  - [ ] View and edit cart
  - [ ] Proceed to checkout
  - [ ] Complete order
  - [ ] View order history
- [ ] Performance testing:
  - [ ] Product list load time
  - [ ] Search performance
  - [ ] Cart operations speed
- [ ] Security audit:
  - [ ] Test CORS headers
  - [ ] Verify JWT token security
  - [ ] Test password hashing
  - [ ] Check for SQL injection vulnerabilities
  - [ ] Verify user authorization
- [ ] Bug fixes and cleanup:
  - [ ] Fix any found bugs
  - [ ] Remove console.log statements
  - [ ] Clean up unused code
  - [ ] Fix linting errors
  - [ ] Optimize bundle size

## Phase 8: Deployment & Documentation
- [ ] Write API Documentation
  - Document all endpoints
  - Include request/response examples
  - Document auth requirements
  - Document error responses
  - Include status codes
- [ ] Write Frontend Setup Guide
  - Installation steps
  - Environment variables needed
  - How to run development server
  - Build command
- [ ] Write Database Setup Guide
  - PostgreSQL version requirements
  - Database creation steps
  - Migration running steps
  - Seeding test data
- [ ] Write Deployment Guide
  - Production environment variables
  - Server setup (Heroku, AWS, etc.)
  - Database backup procedures
  - Security checklist
- [ ] Create comprehensive README.md
  - Project description
  - Tech stack used
  - Installation instructions
  - Running locally
  - Available scripts
  - Project structure
  - Contributing guidelines
  - License
- [ ] Prepare environment files
  - .env.example for backend
  - .env.example for frontend
  - Documentation for each variable
- [ ] Code cleanup and optimization
  - Remove unused imports
  - Optimize images
  - Minimize CSS/JS
  - Remove debug code
- [ ] Final security review
  - Check for exposed secrets
  - Verify input validation
  - Check authorization
  - Review error messages
```

### 3. specs/features.md (COMPLETO)
```markdown
# E-Commerce Feature Specifications

## AUTH-1: User Registration

### Requirements
- [ ] POST /api/auth/register endpoint exists
- [ ] Accepts JSON body with { email, password, name }
- [ ] Email validation: must be valid format
- [ ] Email uniqueness: returns 409 if email already registered
- [ ] Password strength: min 8 chars, 1 uppercase, 1 number, 1 special char
- [ ] Password returns 400 if doesn't meet requirements
- [ ] Password hashed with bcrypt before storage (never plain text)
- [ ] Returns 201 status on success
- [ ] Response includes: { user: { id, email, name }, token }
- [ ] JWT token generated with 7-day expiration
- [ ] Returns 400 for missing fields

### Tests Required
- [ ] Test valid registration succeeds
- [ ] Test duplicate email returns 409
- [ ] Test password too short returns 400
- [ ] Test password without uppercase returns 400
- [ ] Test password without number returns 400
- [ ] Test password without special char returns 400
- [ ] Test missing email returns 400
- [ ] Test missing password returns 400
- [ ] Test invalid email format returns 400
- [ ] Test JWT token is valid format
- [ ] Test user saved to database

---

## AUTH-2: User Login

### Requirements
- [ ] POST /api/auth/login endpoint exists
- [ ] Accepts JSON body with { email, password }
- [ ] Returns 401 for invalid credentials
- [ ] Returns 400 if email or password missing
- [ ] Verifies password against hashed password
- [ ] Returns 200 status on success
- [ ] Response includes: { user: { id, email, name }, token }
- [ ] JWT token generated with 7-day expiration
- [ ] Non-existent email returns 401

### Tests Required
- [ ] Test valid login succeeds
- [ ] Test wrong password returns 401
- [ ] Test non-existent email returns 401
- [ ] Test missing email returns 400
- [ ] Test missing password returns 400
- [ ] Test JWT token is valid
- [ ] Test token can be used for auth

---

## PRODUCT-1: Product Listing

### Requirements
- [ ] GET /api/products endpoint exists
- [ ] Returns array of all products
- [ ] Pagination: 20 items per page
- [ ] Supports page query param: ?page=1
- [ ] Returns { products: [...], total: N, pages: N }
- [ ] Supports category filter: ?category=electronics
- [ ] Supports search: ?search=laptop
- [ ] Supports sorting: ?sort=price OR name OR newest
- [ ] Sort ascending/descending: ?sort=price&order=asc
- [ ] Returns 200 status

### Tests Required
- [ ] Test list all products
- [ ] Test pagination (page 1, page 2, etc.)
- [ ] Test filter by category
- [ ] Test search by name
- [ ] Test search by description
- [ ] Test sort by price
- [ ] Test sort by name
- [ ] Test sort by newest
- [ ] Test empty search results
- [ ] Test invalid page returns empty

---

## PRODUCT-2: Single Product Details

### Requirements
- [ ] GET /api/products/:id endpoint exists
- [ ] Returns single product object
- [ ] Includes: id, name, description, price, category, stock, createdAt
- [ ] Returns 404 if product not found
- [ ] Returns 200 if found

### Tests Required
- [ ] Test get existing product
- [ ] Test get non-existent product returns 404
- [ ] Test response includes all fields
- [ ] Test correct product returned

---

## PRODUCT-3: Create Product (Admin)

### Requirements
- [ ] POST /api/products endpoint exists
- [ ] Requires authentication (401 if not logged in)
- [ ] Requires admin role (403 if not admin)
- [ ] Accepts JSON: { name, description, price, category, stock }
- [ ] Name required, min 3 chars, max 100 chars
- [ ] Description required, max 1000 chars
- [ ] Price required, must be number > 0
- [ ] Category required, must exist
- [ ] Stock required, must be number >= 0
- [ ] Returns 201 on success
- [ ] Returns created product with ID
- [ ] Returns 400 for validation errors

### Tests Required
- [ ] Test create with valid data
- [ ] Test missing auth returns 401
- [ ] Test non-admin user returns 403
- [ ] Test missing name returns 400
- [ ] Test name too short returns 400
- [ ] Test invalid price returns 400
- [ ] Test negative stock returns 400
- [ ] Test product saved to database
- [ ] Test ID auto-generated

---

## PRODUCT-4: Update Product (Admin)

### Requirements
- [ ] PUT /api/products/:id endpoint exists
- [ ] Requires authentication and admin role
- [ ] Can update: name, description, price, category, stock
- [ ] All fields optional (can update one or many)
- [ ] Validates same as create endpoint
- [ ] Returns 200 on success
- [ ] Returns 404 if product not found
- [ ] Returns updated product object

### Tests Required
- [ ] Test update name only
- [ ] Test update price only
- [ ] Test update multiple fields
- [ ] Test validation on update
- [ ] Test non-admin returns 403
- [ ] Test non-existent product returns 404
- [ ] Test product updated in database

---

## PRODUCT-5: Delete Product (Admin)

### Requirements
- [ ] DELETE /api/products/:id endpoint exists
- [ ] Requires authentication and admin role
- [ ] Returns 204 on success (soft delete)
- [ ] Returns 404 if product not found
- [ ] Deleted product no longer appears in listing

### Tests Required
- [ ] Test delete existing product
- [ ] Test non-admin returns 403
- [ ] Test non-existent returns 404
- [ ] Test product removed from listing
- [ ] Test cannot add deleted product to cart

---

## CART-1: Get Cart

### Requirements
- [ ] GET /api/cart endpoint exists
- [ ] Requires authentication (401 if not logged in)
- [ ] Returns user's current cart items
- [ ] Each item includes: productId, quantity, product details
- [ ] Calculates and returns: cartTotal (sum of all items)
- [ ] Returns empty array [] if cart empty
- [ ] Returns 200

### Tests Required
- [ ] Test get empty cart
- [ ] Test get cart with items
- [ ] Test cart includes product details
- [ ] Test cart total calculated correctly
- [ ] Test requires authentication

---

## CART-2: Add to Cart

### Requirements
- [ ] POST /api/cart/add endpoint exists
- [ ] Requires authentication
- [ ] Accepts JSON: { productId, quantity }
- [ ] Validates product exists (404 if not)
- [ ] Validates quantity > 0 (400 if not)
- [ ] Validates product in stock (400 if not enough)
- [ ] If item already in cart: increase quantity
- [ ] If item not in cart: add it
- [ ] Returns 200 and updated cart
- [ ] Cart total updated

### Tests Required
- [ ] Test add valid product
- [ ] Test add nonexistent product returns 404
- [ ] Test invalid quantity returns 400
- [ ] Test quantity > stock returns 400
- [ ] Test adding same product twice merges quantity
- [ ] Test cart total updates
- [ ] Test requires authentication

---

## CART-3: Update Cart Item

### Requirements
- [ ] PUT /api/cart/:itemId endpoint exists
- [ ] Updates quantity for cart item
- [ ] Accepts JSON: { quantity }
- [ ] Validates quantity > 0 (400 if not)
- [ ] Validates quantity <= product stock (400 if not)
- [ ] Returns 200 and updated cart
- [ ] Returns 404 if item not in cart

### Tests Required
- [ ] Test update quantity valid
- [ ] Test invalid quantity returns 400
- [ ] Test quantity > stock returns 400
- [ ] Test nonexistent item returns 404
- [ ] Test cart total updates

---

## CART-4: Remove from Cart

### Requirements
- [ ] DELETE /api/cart/:itemId endpoint exists
- [ ] Removes item from user's cart
- [ ] Returns 200 and updated cart
- [ ] Returns 404 if item not in cart

### Tests Required
- [ ] Test remove existing item
- [ ] Test nonexistent item returns 404
- [ ] Test item no longer in cart

---

## CART-5: Clear Cart

### Requirements
- [ ] POST /api/cart/clear endpoint exists
- [ ] Removes ALL items from user's cart
- [ ] Returns 200 and empty cart

### Tests Required
- [ ] Test clear cart
- [ ] Test cart is empty after clear
- [ ] Test can add new items after clear

---

## ORDER-1: Create Order

### Requirements
- [ ] POST /api/orders endpoint exists
- [ ] Requires authentication
- [ ] Converts user's cart to order
- [ ] Validates cart not empty (400 if empty)
- [ ] Calculates order total from cart items
- [ ] Creates order in database with status: "pending"
- [ ] Creates order_items for each cart item
- [ ] Clears user's cart after order created
- [ ] Returns 201 and created order
- [ ] Order includes: id, user_id, items[], total, status, createdAt

### Tests Required
- [ ] Test valid order creation
- [ ] Test empty cart returns 400
- [ ] Test order total correct
- [ ] Test order items match cart
- [ ] Test cart cleared after order
- [ ] Test status is "pending"
- [ ] Test requires authentication

---

## ORDER-2: Get User Orders

### Requirements
- [ ] GET /api/orders endpoint exists
- [ ] Requires authentication
- [ ] Returns all orders for authenticated user
- [ ] Includes order items and products
- [ ] Supports filtering by status: ?status=pending
- [ ] Paginated (20 per page)
- [ ] Sorted by newest first
- [ ] Returns 200 with orders array

### Tests Required
- [ ] Test get all orders
- [ ] Test filter by pending
- [ ] Test filter by delivered
- [ ] Test pagination works
- [ ] Test newest first
- [ ] Test requires authentication
- [ ] Test user only sees own orders

---

## ORDER-3: Get Order Details

### Requirements
- [ ] GET /api/orders/:id endpoint exists
- [ ] Returns single order with all details
- [ ] Includes order items with product info
- [ ] Verifies authenticated user owns this order
- [ ] Returns 404 if order not found
- [ ] Returns 403 if user doesn't own order
- [ ] Returns 200 if authorized

### Tests Required
- [ ] Test get own order
- [ ] Test user cannot access other user's order (403)
- [ ] Test nonexistent order returns 404
- [ ] Test includes all order items
- [ ] Test includes product details

---

## ORDER-4: Cancel Order

### Requirements
- [ ] PUT /api/orders/:id/cancel endpoint exists
- [ ] Requires authentication
- [ ] Only allows cancellation if status is "pending"
- [ ] Changes status to "cancelled"
- [ ] Returns 400 if already shipped/delivered
- [ ] Returns 404 if order not found
- [ ] Returns 403 if user doesn't own order
- [ ] Returns 200 with updated order

### Tests Required
- [ ] Test cancel pending order
- [ ] Test cannot cancel delivered order
- [ ] Test cannot cancel shipped order
- [ ] Test nonexistent returns 404
- [ ] Test unauthorized returns 403
- [ ] Test status changes to cancelled

---

## FRONTEND-1: User Registration Flow

### Requirements
- [ ] Registration page accessible
- [ ] Form accepts: email, password, name
- [ ] Shows password validation feedback (strength indicator)
- [ ] Form validation before submit
- [ ] Submit button disabled until valid
- [ ] Shows loading state during request
- [ ] Success: redirects to login or dashboard
- [ ] Error: displays error message
- [ ] Link to login page if already registered

### Tests Required
- [ ] Page renders correctly
- [ ] Validation works
- [ ] Can submit valid form
- [ ] Error message shown on failure
- [ ] Success redirects correctly

---

## FRONTEND-2: User Login Flow

### Requirements
- [ ] Login page accessible
- [ ] Form accepts: email, password
- [ ] Form validation
- [ ] Shows loading state during request
- [ ] Success: stores JWT token and redirects
- [ ] Error: displays error message
- [ ] Link to registration if no account
- [ ] Token persisted (localStorage or cookie)

### Tests Required
- [ ] Page renders correctly
- [ ] Can submit valid form
- [ ] Error message on failure
- [ ] Success redirects to dashboard
- [ ] Token stored correctly

---

## FRONTEND-3: Product Listing Page

### Requirements
- [ ] Displays products in grid or list
- [ ] Each product shows: name, price, image, "Add to Cart" button
- [ ] Category filter sidebar works
- [ ] Search bar works
- [ ] Sorting dropdown works (price, name, newest)
- [ ] Pagination controls present
- [ ] Product click navigates to detail page
- [ ] Loading state while fetching
- [ ] Error message if fetch fails

### Tests Required
- [ ] Page renders
- [ ] Products displayed
- [ ] Filter works
- [ ] Search works
- [ ] Sorting works
- [ ] Pagination works
- [ ] Can add to cart
- [ ] Can click product for details

---

## FRONTEND-4: Product Detail Page

### Requirements
- [ ] Displays product name, description, price, stock status
- [ ] Shows product image/gallery
- [ ] Quantity selector (spinner or input)
- [ ] "Add to Cart" button (disabled if out of stock)
- [ ] Shows "In Stock" or "Out of Stock"
- [ ] Back button or breadcrumb navigation
- [ ] Shows related products (optional)
- [ ] Loading state while fetching

### Tests Required
- [ ] Page renders with correct product
- [ ] Can change quantity
- [ ] Add to cart works
- [ ] Button disabled if out of stock
- [ ] Related products display

---

## FRONTEND-5: Shopping Cart Page

### Requirements
- [ ] Lists all cart items
- [ ] Each item shows: product name, price, quantity, subtotal
- [ ] Quantity can be edited inline (spinner or input)
- [ ] Remove item button present
- [ ] Shows cart total
- [ ] Empty cart message if no items
- [ ] "Continue Shopping" button
- [ ] "Checkout" button (disabled if empty)

### Tests Required
- [ ] Empty cart shows message
- [ ] Items displayed correctly
- [ ] Can update quantity
- [ ] Can remove item
- [ ] Cart total calculated correctly
- [ ] Can proceed to checkout

---

## FRONTEND-6: Checkout Page

### Requirements
- [ ] Displays order summary (items, subtotal, total)
- [ ] Shipping address form
- [ ] Payment method selection
- [ ] "Place Order" button
- [ ] Shows loading state during order creation
- [ ] Success: shows order confirmation
- [ ] Error: displays error message
- [ ] Confirmation includes order ID

### Tests Required
- [ ] Page renders
- [ ] Order summary correct
- [ ] Can submit order
- [ ] Confirmation displayed on success
- [ ] Error shown on failure

---

## FRONTEND-7: Order History Page

### Requirements
- [ ] Lists all user's past orders
- [ ] Each order shows: order ID, date, total, status
- [ ] Click order for details
- [ ] Cancel button if status is "pending"
- [ ] No orders message if empty
- [ ] Filter by status (optional)

### Tests Required
- [ ] Page renders
- [ ] Orders displayed
- [ ] Can click for details
- [ ] Can cancel pending order
- [ ] Filtered results correct

---

## TEST-1: Overall Code Coverage

### Requirements
- [ ] Backend code coverage >80%
- [ ] Critical paths >90% (auth, order, cart)
- [ ] All edge cases tested
- [ ] All error paths tested
- [ ] Frontend coverage >75%
- [ ] All components tested

### Tests Required
- [ ] Run coverage report
- [ ] All files covered
- [ ] Coverage meets thresholds
```

## Como Executar Este Projeto
```bash
# 1. Criar estrutura
mkdir ecommerce-app
cd ecommerce-app

# 2. Criar pastas do projeto
mkdir backend frontend
mkdir specs

# 3. Copiar os três arquivos:
# - Copiar PROMPT.md para raiz
# - Copiar IMPLEMENTATION_PLAN.md para raiz
# - Copiar specs/features.md para pasta specs/

# 4. Iniciar o loop
/lisa:loop PROMPT.md --max-iterations 200

# 5. Acompanhar progresso
/lisa:status
tail -f .claude/lisa-loop.log
```

## Estimativa de Tempo

- **Iterations:** 100-150 (depende da complexidade)
- **Tempo real:** 50-100 horas de execução
- **Resultado:** Aplicação e-commerce completa, testada e documentada

---

