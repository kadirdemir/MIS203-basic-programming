# Week 02 Lab and Quiz

The lab task and assessment checklist are in `lab_assignment.md` in this folder.

Use `week02/lab-quiz/` in your own repository for in-class lab and quiz work. Save `lab02_purchase_quote.py` here. Keep separate weekly homework in `week02/` outside this folder.

## Lab Completion Note

- Test run: used 2 × 50.00 and 1 × 80.00, with 20.00 TRY delivery and 10% tax. The program produced the expected final total of 218.00 TRY.
- Change after testing: improved the quote layout with separator lines, aligned columns, and two-decimal money formatting to make the output easier to read.
- Conversion note: `input()` returns text, so quantities must be converted with `int()` and money/tax values with `float()` before arithmetic can be performed correctly.
- Error-case test: entering letters for a quantity causes a `ValueError` because the text cannot be converted to an integer. A later version could use validation with `try`/`except` and ask the user to enter the value again.
