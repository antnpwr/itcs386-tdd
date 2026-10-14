1. How many tests did you write in Part A, and how many lines of production code? What is the
ratio?
    * In part A, test_kitchen have 9 tests and total of around 40 lines. Ratio if around 1 test per 4-5 lines of code

2. When was your bar red for the longest time, and what made it last so long?
    * The logest red bar for me is in A6, i find it hard to understand the instruction and i am a bit lost on how to fix them. 

3. Find one place where you used Fake It, one where you triangulated, and one where you used
Obvious Implementation. Looking back, was each choice right?
    * An example of Fake it is from A4 where we just fake it as true first then write the real one later, triangulate was in A2 using two tests with different data, the obvious implementation would be the one in A5 that I just type real code. I think all of them are good choice.

4. Which items are still on your test list? Which would you implement next, and which should you
delete because they were speculation?
    * All the test list item on the top of the test file is all done. 
    * Maybe we can implement a test to reduce grams to ounces, or other test for more units/rates and catching their error, such as cups
    * We could delete the more units since it is not much needed compare to other ideas.

5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have
written this method?
    * I dont think so, I would just use if to check unit and match them.

6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel
different, and which tests shaped your design?
    * I think writing test after code in part 0 helps with catching bugs but it doesnt lead the code design, while writing test before code makes it more like that the test is the one that design it, and the code just follow the design of the test.