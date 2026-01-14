# Bug Fix Template for Ralph-Loop

Use this template when fixing bugs in your application.

## Instructions

1. Replace all `[PLACEHOLDERS]` with your specific bug details
2. Include clear reproduction steps
3. Set max-iterations (recommended: 15-25 for most bug fixes)
4. Copy the final prompt and run the ralph-loop command

---

## Prompt Template

```
Fix bug: [BUG_TITLE/DESCRIPTION]

Bug Description:
[Describe what's happening vs what should happen]

Affected Component/File:
[Where the bug occurs, if known]

Reproduction Steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. Expected: [What should happen]
5. Actual: [What actually happens]

Error Message/Symptoms:
[Paste error message, stack trace, or describe symptoms]

Fix Workflow:
1. Create test that reproduces the bug
2. Run test - confirm it fails (bug exists)
3. Analyze root cause
4. Implement fix
5. Run test - if fails, refine fix
6. Run full test suite - ensure no regressions
7. Verify fix in application (manual test if needed)
8. When bug test passes AND all other tests pass, output <promise>BUG_FIXED</promise>

Completion Criteria:
- [ ] Bug no longer reproducible (follow reproduction steps - bug doesn't occur)
- [ ] Regression test added ([test file name])
- [ ] Regression test passes
- [ ] All [N] existing tests still pass
- [ ] No new errors in console/logs
- [ ] [Any additional verification specific to this bug]

When all criteria met, output <promise>BUG_FIXED</promise>
```

---

## Ralph-Loop Command

```bash
/ralph-loop "[YOUR_PROMPT_HERE]" \
  --completion-promise "BUG_FIXED" \
  --max-iterations [15-25]
```

---

## Example: Form Submission Crash

```
Fix bug: Form submission crashes when email field is empty

Bug Description:
The registration form crashes the entire application when users submit the form with an empty email field, instead of showing a validation error.

Affected Component/File:
src/components/RegistrationForm.tsx (likely the email validation logic)

Reproduction Steps:
1. Navigate to /register
2. Fill in username field with "testuser"
3. Leave email field completely empty
4. Fill in password field with "password123"
5. Click "Submit" button
6. Expected: Form shows validation error "Email is required"
7. Actual: App crashes with error "Cannot read property 'includes' of undefined"

Error Message/Symptoms:
```
TypeError: Cannot read property 'includes' of undefined
    at validateEmail (RegistrationForm.tsx:45)
    at handleSubmit (RegistrationForm.tsx:78)
```

Fix Workflow:
1. Create test that reproduces the bug (submit form with empty email)
2. Run test - confirm it fails (crashes as expected)
3. Analyze root cause (likely: no null check before calling .includes())
4. Implement fix (add null/undefined check in validateEmail function)
5. Run test - if fails, refine fix
6. Run full test suite - ensure no regressions (all 47 tests should still pass)
7. Manually test in browser (submit empty email, verify error shows)
8. When bug test passes AND all other tests pass, output <promise>BUG_FIXED</promise>

Completion Criteria:
- [ ] Bug no longer reproducible (empty email doesn't crash)
- [ ] Form displays validation error: "Email is required"
- [ ] Regression test added (tests/RegistrationForm.test.tsx: test_email_validation_empty)
- [ ] New test passes
- [ ] All 47 existing tests still pass
- [ ] No errors in console when submitting with empty email
- [ ] Form still works correctly with valid email (existing functionality not broken)

When all criteria met, output <promise>BUG_FIXED</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "BUG_FIXED" --max-iterations 15
```

---

## Example: Memory Leak

```
Fix bug: Memory leak in dashboard causing browser tab to become unresponsive

Bug Description:
When users keep the real-time dashboard open for more than 10 minutes, memory usage grows continuously from ~50MB to 500MB+, eventually making the browser tab unresponsive and requiring a page refresh.

Affected Component/File:
src/components/Dashboard.tsx (likely WebSocket connection not being cleaned up)

Reproduction Steps:
1. Navigate to /dashboard
2. Leave dashboard open
3. Monitor Chrome DevTools memory profiler
4. Wait 10 minutes
5. Expected: Memory usage stays relatively stable (< 100MB)
6. Actual: Memory usage grows to 500MB+ and tab becomes slow/unresponsive

Error Message/Symptoms:
- Memory grows continuously (heap snapshot shows increasing retained size)
- Browser tab lag/freeze
- Multiple WebSocket message listeners accumulating (evident in memory profiler)
- No console errors (silent leak)

Fix Workflow:
1. Use Chrome DevTools heap snapshot to identify leak source
2. Create test to monitor WebSocket connection cleanup
3. Identify root cause (likely: WebSocket not closed on component unmount, event listeners not removed)
4. Implement fix (cleanup in useEffect return or componentWillUnmount)
5. Test: Open dashboard, wait 2 minutes, monitor memory
6. Test: Navigate away from dashboard, verify memory is released
7. Run all component tests
8. When memory stable AND tests pass, output <promise>LEAK_FIXED</promise>

Completion Criteria:
- [ ] Memory usage stays below 100MB after 5 minutes on dashboard
- [ ] Memory is released when navigating away from dashboard (heap snapshot shows objects freed)
- [ ] WebSocket connection properly closes on unmount
- [ ] Event listeners properly removed on unmount
- [ ] All component tests pass (npm test)
- [ ] No console errors or warnings
- [ ] Dashboard real-time updates still work (fix doesn't break functionality)

When all criteria met, output <promise>LEAK_FIXED</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "LEAK_FIXED" --max-iterations 20
```

---

## Example: API 500 Error

```
Fix bug: POST /api/orders returns 500 error when product is out of stock

Bug Description:
When users attempt to create an order for a product that is out of stock (stock = 0), the API returns a 500 Internal Server Error instead of a 400 Bad Request with appropriate error message.

Affected Component/File:
src/controllers/orderController.ts (likely missing stock validation)

Reproduction Steps:
1. Ensure product with ID=123 has stock=0 in database
2. Send POST request to /api/orders with body: {"productId": 123, "quantity": 1}
3. Expected: 400 Bad Request with {"error": "Product out of stock"}
4. Actual: 500 Internal Server Error with generic error message

Error Message/Symptoms:
Server logs show:
```
TypeError: Cannot read property 'quantity' of null
    at createOrder (orderController.ts:34)
```

Fix Workflow:
1. Create test that reproduces the bug (create order with out-of-stock product)
2. Run test - confirm it returns 500 (bug exists)
3. Analyze root cause (likely: no stock validation before accessing product)
4. Implement fix (add stock check, return 400 if stock insufficient)
5. Run test - should now return 400 (not 500)
6. Run full API test suite - ensure no regressions
7. Test with various stock scenarios (stock=0, stock<quantity, stock>quantity)
8. When test passes AND all other tests pass, output <promise>BUG_FIXED</promise>

Completion Criteria:
- [ ] POST /api/orders with out-of-stock product returns 400 (not 500)
- [ ] Response body includes: {"error": "Product out of stock"}
- [ ] Regression test added (tests/orderController.test.ts: test_order_out_of_stock)
- [ ] Test covers stock=0 scenario
- [ ] Test covers stock<quantity scenario
- [ ] All 52 existing API tests still pass
- [ ] No 500 errors in server logs for this scenario
- [ ] Creating order with sufficient stock still works (existing functionality intact)

When all criteria met, output <promise>BUG_FIXED</promise>
```

**Command:**
```bash
/ralph-loop "[above prompt]" --completion-promise "BUG_FIXED" --max-iterations 18
```

---

## Tips for Bug Fix Prompts

1. **Precise reproduction** - The more detailed the steps, the better
2. **Include error messages** - Paste full stack traces
3. **Regression test first** - Always start by creating a failing test
4. **Test the fix** - Don't just make console errors go away, verify correct behavior
5. **Check for regressions** - Ensure existing tests still pass
6. **Root cause** - Fix the cause, not just the symptom
7. **Low max-iterations** - Most bugs fix in 10-20 iterations

## Common Bug Fix Criteria

- [ ] Bug no longer reproducible (follow exact reproduction steps)
- [ ] Regression test added and passing
- [ ] All existing tests still pass (no new bugs introduced)
- [ ] No errors in console/logs for this scenario
- [ ] Fix addresses root cause (not just symptom)
- [ ] Related functionality still works (no breaking changes)
- [ ] Error messages are clear and helpful (if applicable)
- [ ] Edge cases handled (null, undefined, empty, etc.)
