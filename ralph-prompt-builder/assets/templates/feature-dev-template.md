# Feature Development Template for Ralph-Loop

Use this template when implementing a new feature in your application.

## Instructions

1. Replace all `[PLACEHOLDERS]` with your specific details
2. Break feature into logical phases if complex
3. Set max-iterations based on complexity (recommended: 40-75 for medium features)
4. Copy the final prompt and run the ralph-loop command

---

## Prompt Template

```
Implement [FEATURE_NAME] feature.

Feature Description:
[Describe the feature in 2-3 sentences, including what it does and why]

User Story (optional):
As a [user type], I want to [action] so that [benefit].

Requirements:
1. [Specific requirement 1]
2. [Specific requirement 2]
3. [Specific requirement 3]
[Add more as needed]

Implementation Phases:

Phase 1: [Core Functionality]
- [ ] [Specific task 1]
- [ ] [Specific task 2]
- [ ] [Specific task 3]
Verification: [How to verify Phase 1 is complete]

Phase 2: [Validation/Testing]
- [ ] [Specific task 1]
- [ ] [Specific task 2]
- [ ] [Specific task 3]
Verification: [How to verify Phase 2 is complete]

Phase 3: [Integration/Polish]
- [ ] [Specific task 1]
- [ ] [Specific task 2]
- [ ] [Specific task 3]
Verification: [How to verify Phase 3 is complete]

Completion Criteria:
- [ ] All requirements implemented
- [ ] [Specific automated verification 1]
- [ ] [Specific automated verification 2]
- [ ] All tests pass (existing + new)
- [ ] No breaking changes to existing features
- [ ] [Any additional criteria]

When ALL phases complete and all criteria are met, output <promise>FEATURE_COMPLETE</promise>
```

---

## Ralph-Loop Command

```bash
/ralph-loop "[YOUR_PROMPT_HERE]" \
  --completion-promise "FEATURE_COMPLETE" \
  --max-iterations [40-75]
```

---

## Example: Search Functionality

```
Implement search functionality for products page.

Feature Description:
Add real-time search capability that allows users to filter products by name or description as they type, with debounced input to optimize performance.

User Story:
As a user, I want to search for products by name or description so that I can quickly find what I'm looking for without scrolling through all products.

Requirements:
1. Search input field visible on products page header
2. Real-time filtering as user types (case-insensitive)
3. Search matches product name OR description
4. Debounce input by 300ms to reduce filtering frequency
5. Display result count ("Showing X of Y products")
6. Show "No results" message when no matches
7. Clear button to reset search

Implementation Phases:

Phase 1: Search UI Component
- [ ] Create SearchInput component
- [ ] Add search input to products page header
- [ ] Style search input (consistent with design system)
- [ ] Add clear button (X icon)
Verification: Search input visible and styled correctly

Phase 2: Search Logic
- [ ] Implement debounced search function (300ms delay)
- [ ] Create filter function (case-insensitive, matches name OR description)
- [ ] Update product list based on search term
- [ ] Handle empty search (show all products)
Verification: Typing filters products correctly with 300ms delay

Phase 3: Enhanced UX
- [ ] Display result count dynamically
- [ ] Show "No results found for '[term]'" when appropriate
- [ ] Clear button functionality (resets search and shows all products)
- [ ] Preserve search term in URL query param (optional)
Verification: Result count accurate, empty states work, clear button works

Phase 4: Testing
- [ ] Write tests for search filtering logic
- [ ] Write tests for debounce functionality
- [ ] Write tests for empty states
- [ ] Write tests for clear functionality
- [ ] E2E test for complete search flow
Verification: All tests pass

Completion Criteria:
- [ ] Search input visible on products page
- [ ] Typing filters products in real-time (case-insensitive)
- [ ] Debouncing works (verified: doesn't filter on every keystroke)
- [ ] Search matches both name AND description fields
- [ ] Result count displays correctly ("Showing X of Y products")
- [ ] Empty results shows "No results found for '[search term]'"
- [ ] Clear button resets search and shows all products
- [ ] 10+ tests covering all search scenarios
- [ ] All tests pass (npm test)
- [ ] No performance issues (search completes in < 100ms)
- [ ] No errors in console

When ALL phases complete and all criteria are met, output <promise>FEATURE_COMPLETE</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "FEATURE_COMPLETE" --max-iterations 50
```

---

## Example: File Upload

```
Implement file upload functionality for user profile avatars.

Feature Description:
Allow users to upload profile picture (avatar) from their profile page, with automatic resizing and validation to ensure appropriate file types and sizes.

Requirements:
1. Upload button on user profile page
2. Accept only: .jpg, .jpeg, .png files
3. Maximum file size: 5MB
4. Client-side image preview before upload
5. Server-side resize to 200x200px
6. Save to /uploads/avatars directory
7. Update user profile with avatar URL
8. Display upload progress indicator

Implementation Phases:

Phase 1: Frontend Upload UI
- [ ] Create file input component (styled as button)
- [ ] Add file type validation (.jpg, .jpeg, .png only)
- [ ] Add file size validation (max 5MB)
- [ ] Implement image preview functionality
- [ ] Create upload progress indicator component
Verification: Can select image, see preview, validation works

Phase 2: Backend Upload Processing
- [ ] Setup Multer middleware for file uploads
- [ ] Configure upload destination (/uploads/avatars)
- [ ] Implement image resizing (sharp library, 200x200px)
- [ ] Generate unique filename (user-id-timestamp.jpg)
- [ ] Save file to disk
- [ ] Return avatar URL in response
Verification: Backend receives file, resizes, saves, returns URL

Phase 3: Database & Integration
- [ ] Update user schema to include avatar_url field
- [ ] Create endpoint to update user avatar URL
- [ ] Connect frontend upload to backend endpoint
- [ ] Update profile page to display avatar
- [ ] Handle upload errors (show error messages)
Verification: Complete flow works end-to-end

Phase 4: Testing
- [ ] Test file type validation (reject .exe, .pdf, etc.)
- [ ] Test file size validation (reject > 5MB)
- [ ] Test successful upload flow
- [ ] Test image resize (verify output is 200x200px)
- [ ] Test error handling (network errors, invalid files)
Verification: All tests pass

Completion Criteria:
- [ ] Upload button visible on profile page
- [ ] File type validation works (only .jpg, .jpeg, .png accepted)
- [ ] File size validation works (reject > 5MB, show error)
- [ ] Image preview displays before upload
- [ ] Upload progress shows 0-100%
- [ ] Server resizes image to exactly 200x200px
- [ ] Image saved to /uploads/avatars/[unique-name].jpg
- [ ] User record updated with avatar URL
- [ ] Profile page displays uploaded avatar
- [ ] Error messages shown for invalid files
- [ ] 15+ tests covering all scenarios
- [ ] All tests pass
- [ ] No errors in console or server logs

When ALL phases complete and all criteria are met, output <promise>FEATURE_COMPLETE</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "FEATURE_COMPLETE" --max-iterations 60
```

---

## Tips for Feature Development Prompts

1. **Break into phases** - Complex features need logical breakdown
2. **Phase verification** - Specify how to verify each phase independently
3. **Include integration phase** - Don't forget to connect all the pieces
4. **Test phase** - Always include a dedicated testing phase
5. **Be specific about UI** - Describe exactly where components go
6. **Define success metrics** - How will you know the feature works?
7. **Consider edge cases** - What happens when things go wrong?
8. **No breaking changes** - Ensure existing features still work

## Common Feature Development Criteria

- [ ] All requirements from spec implemented
- [ ] Feature works as described in user story
- [ ] Tests cover main use cases and edge cases
- [ ] Feature integrated with existing code
- [ ] No breaking changes (all existing tests pass)
- [ ] Error states handled appropriately
- [ ] UI/UX matches design specifications
- [ ] Performance acceptable (< Xms for key operations)
- [ ] Accessibility requirements met (ARIA labels, keyboard nav)
- [ ] Documentation updated (README, API docs, etc.)
