# TDD Lab Reflection

**1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?**

I wrote 9 tests in Part A and [X] lines of production code. The test-to-code ratio was 9:[X]. These tests helped verify the required behaviors throughout development.

**2. When was your bar red for the longest time, and what made it last so long?**

The longest red bar was during [step]. I found it difficult because [explain the actual problem]. I solved it by making smaller changes and rerunning the tests.

**3. Find one place where you used Fake It, Triangulate, and Obvious Implementation.**

I used Fake It in A1 by returning 600 directly. I used Triangulation in A2 by adding a second multiplication test to develop a general formula. I used Obvious Implementation for the unit equality check in A5. I think these strategies were appropriate because they helped me make progress in small steps.

**4. Which items are still on your test list?**

I completed all seven original items, including the optional multiplication of a Sum. A possible next improvement is handling unsupported conversion rates more clearly. I would avoid adding features without a clear requirement.

**5. Would you have designed Quantity.reduce this way from the beginning?**

Probably not. I might have calculated everything directly inside Quantity. Writing the tests helped me discover that separating Quantity, Sum, and Converter made the design more flexible.

**6. How did Part 0 and Part A feel different?**

In Part 0, the code already existed, so I focused on checking its behavior and finding bugs. In Part A, writing tests first helped guide the implementation and design. The tests for immutable multiplication and mixed-unit addition had the biggest impact on the design.