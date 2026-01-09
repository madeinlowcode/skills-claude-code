# Lisa Spec-Based Verification Examples

Exemplos reais de `specs/features.md` para diferentes tipos de projetos.

## Example 1: REST API com Autenticação
```markdown
# TODO API Specifications

## AUTH-1: User Registration

### Requirements
- [ ] POST /auth/register accepts { email, password, name }
- [ ] Password minimum 8 chars, 1 uppercase, 1 number, 1 special char
- [ ] Email validation (valid format, not already registered)
- [ ] Returns 201 with { user: { id, email, name }, token }
- [ ] Returns 400 for validation errors with error details
- [ ] Returns 409 if email already exists
- [ ] Password is hashed before storage
- [ ] Token is JWT with 7-day expiration

### Tests Required
- [ ] Test valid registration
- [ ] Test password too short
- [ ] Test missing uppercase in password
- [ ] Test duplicate email
- [ ] Test invalid email format
- [ ] Test token generation and format

---

## AUTH-2: User Login

### Requirements
- [ ] POST /auth/login accepts { email, password }
- [ ] Returns 200 with { user: { id, email, name }, token }
- [ ] Returns 401 for invalid credentials
- [ ] Returns 400 if email/password missing
- [ ] Token expiration set to 7 days

### Tests Required
- [ ] Test successful login
- [ ] Test wrong password
- [ ] Test non-existent email
- [ ] Test missing fields
- [ ] Test token validity

---

## CRUD-1: Create Todo

### Requirements
- [ ] POST /api/todos accepts { title, description }
- [ ] Title required, min 3 chars, max 100 chars
- [ ] Description optional, max 500 chars
- [ ] Returns 201 with created todo
- [ ] Returns 400 for validation errors
- [ ] Todo includes: id, title, description, createdAt, updatedAt, completed
- [ ] Default completed = false
- [ ] Todo belongs to authenticated user

### Tests Required
- [ ] Test valid todo creation
- [ ] Test missing title
- [ ] Test title too short
- [ ] Test title too long
- [ ] Test description too long
- [ ] Test authentication required

---

## CRUD-2: Read Todos

### Requirements
- [ ] GET /api/todos returns array of user's todos
- [ ] Results are sorted by createdAt descending
- [ ] GET /api/todos/:id returns single todo
- [ ] Returns 404 if todo not found
- [ ] User can only read own todos
- [ ] Returns empty array [] if no todos

### Tests Required
- [ ] Test read all todos
- [ ] Test read single todo
- [ ] Test todo not found
- [ ] Test authorization (own todos only)
- [ ] Test empty list

---

## CRUD-3: Update Todo

### Requirements
- [ ] PUT /api/todos/:id updates title and/or description
- [ ] Can update title, description, completed individually
- [ ] Returns 200 with updated todo
- [ ] Returns 400 for validation errors
- [ ] Returns 404 if todo not found
- [ ] User can only update own todos
- [ ] Updates createdAt but changes updatedAt

### Tests Required
- [ ] Test update title only
- [ ] Test update description only
- [ ] Test toggle completed
- [ ] Test validation on update
- [ ] Test todo not found
- [ ] Test authorization

---

## CRUD-4: Delete Todo

### Requirements
- [ ] DELETE /api/todos/:id removes todo
- [ ] Returns 204 on success
- [ ] Returns 404 if todo not found
- [ ] User can only delete own todos
- [ ] Deleted todos cannot be recovered

### Tests Required
- [ ] Test successful deletion
- [ ] Test todo not found
- [ ] Test authorization
- [ ] Test soft delete (if applicable)

---

## TEST-1: Code Coverage

### Requirements
- [ ] All endpoints have unit tests
- [ ] All validation logic has tests
- [ ] All error paths have tests
- [ ] Overall coverage >80%
- [ ] Critical paths (auth, CRUD) >90% coverage

### Tests Required
- [ ] Coverage report shows >80%
- [ ] No untested files (except config)
- [ ] Happy path tested
- [ ] Error paths tested
```

---

## Example 2: CLI Application
```markdown
# Project Scaffolder CLI Specs

## FEATURE-1: Project Creation

### Requirements
- [ ] Command: `scaffold create <project-name>`
- [ ] Creates directory with name
- [ ] Initializes git repository
- [ ] Copies template files
- [ ] Installs dependencies
- [ ] Returns success message with next steps

### Tests Required
- [ ] Directory created
- [ ] Git initialized
- [ ] Templates copied correctly
- [ ] Dependencies installed
- [ ] Error if directory exists

---

## FEATURE-2: Template Listing

### Requirements
- [ ] Command: `scaffold list`
- [ ] Shows all available templates
- [ ] Displays: name, description, version
- [ ] Shows locally installed templates
- [ ] Can filter by category (if applicable)

### Tests Required
- [ ] Lists all templates
- [ ] Format is readable
- [ ] Filters work correctly

---

## FEATURE-3: Customization

### Requirements
- [ ] Command: `scaffold create --template <name>`
- [ ] Supports flags for customization
- [ ] Flag: `--typescript` (default false)
- [ ] Flag: `--eslint` (default true)
- [ ] Flag: `--git` (default true)
- [ ] Flag: `--install` (default true)

### Tests Required
- [ ] Each flag works individually
- [ ] Flags can be combined
- [ ] Default values used if not provided
- [ ] Invalid flags show error
```

---

## Example 3: Data Processing Pipeline
```markdown
# CSV Import Pipeline Specs

## PIPELINE-1: CSV Parsing

### Requirements
- [ ] Parse CSV with headers in first row
- [ ] Handle quoted fields with commas
- [ ] Handle escaped quotes
- [ ] Detect encoding (UTF-8, ISO-8859-1)
- [ ] Returns array of objects
- [ ] Headers become object keys

### Tests Required
- [ ] Simple CSV parses correctly
- [ ] CSV with quotes parses correctly
- [ ] CSV with commas in quotes
- [ ] CSV with escaped quotes
- [ ] Different encodings detected
- [ ] Headers used as keys

---

## PIPELINE-2: Validation

### Requirements
- [ ] Validates data against schema
- [ ] Schema defines required fields
- [ ] Schema defines field types
- [ ] Returns validation errors
- [ ] Specifies row number and field
- [ ] Skips empty rows

### Tests Required
- [ ] Valid data passes
- [ ] Missing required field fails
- [ ] Wrong type fails with message
- [ ] Multiple errors reported
- [ ] Empty rows skipped

---

## PIPELINE-3: Transformation

### Requirements
- [ ] Transforms fields (trim, lowercase, etc.)
- [ ] Converts data types (string to number)
- [ ] Maps field names to database columns
- [ ] Handles null/empty values
- [ ] Logs transformation steps

### Tests Required
- [ ] Trim whitespace
- [ ] Case conversion
- [ ] Type conversion
- [ ] Field mapping
- [ ] Null handling
```

---

## Template Generation Script

Para gerar um spec template rapidamente:
```bash
# Create a new spec file
cat > specs/features.md << 'EOF'
# [Project Name] Specifications

## [FEATURE-1]: [Feature Name]

### Requirements
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

### Tests Required
- [ ] Test 1
- [ ] Test 2
- [ ] Test 3

---

## [FEATURE-2]: [Next Feature]

...

EOF
```
