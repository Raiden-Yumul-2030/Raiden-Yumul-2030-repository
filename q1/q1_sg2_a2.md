# Code Quality Assessment Worksheet

**Section:** *9-Arayat* **Score:** *-*

**C# / Name:** *-, Yumul, -* **Date:** *August 16, 2026*


## ***Instructions:***
### **The problem: Finding the highest (Maximum) number from a given list of numbers.**


**PseudoCode 1**
```
Algorithm FindMax1(numbers)
   max ← numbers[0]
   For i from 1 to length(numbers)-1
      If numbers[i] > max Then
         max ← numbers[i]
      EndIf
   EndFor
   Return max
EndAlgorithm
```

**PseudoCode 2**
```
Algorithm FindMax2(numbers)
   For i from 0 to length(numbers)-1bigger ← true
      For j from 0 to length(numbers)-1
         If numbers[j] > numbers[i] Then
            bigger ← false
         EndIf
      EndFor
      If bigger = true Then
         Return numbers[i]
      EndIf
   EndFor
EndAlgorithm
```

## Questions with Checklists
### **1. Efficiency**
**Which algorithm is faster when the list of numbers is very large? Why?**


**Checklist to guide your answer:**
*PseudoCode 1*
- Does the algorithm use one loop or two nested loops?
- Does the algorithm repeat work unnecessarily?
- Which algorithm finishes in fewer steps?

*PseudoCode 2*
- Does the algorithm use one loop or two nested loops?
- Does the algorithm repeat work unnecessarily?
- Which algorithm finishes in fewer steps?

### **2. Readability**
**Which algorithm is easier to understand at first glance? What makes it clearer?**


**Checklist to guide your answer:**
*PseudoCode 1*
- Are variable names meaningful (e.g., max vs. bigger)?
- Is the logic simple or complicated?
- Are there fewer lines of code?

*PseudoCode 2*
- Are variable names meaningful (e.g., max vs. bigger)?
- Is the logic simple or complicated?
- Are there fewer lines of code?

### **3. Maintainability**
**If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?**


**Checklist to guide your answer:**
*PseudoCode 1*
- Is the structure straightforward?
- Would adding new steps break the code easily?
- Is there less chance of errors when updating?

*PseudoCode 2*
- Is the structure straightforward?
- Would adding new steps break the code easily?
- Is there less chance of errors when updating?

### **4. Testability**
**Which algorithm is easier to test with different inputs? Why?**


**Checklist to guide your answer:**
*PseudoCode 1*
- Can you test with small lists easily?
- Does the algorithm have fewer conditions to check?
- Is the output predictable and clear?

*PseudoCode 2*
- Can you test with small lists easily?
- Does the algorithm have fewer conditions to check?
- Is the output predictable and clear?


### **5. Security**
**Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?**


**Checklist to guide your answer:**
*PseudoCode 1*
- Does the algorithm check if the list is empty?
- Does it handle invalid inputs (like letters instead of numbers)?
- Does it avoid crashing when inputs are unusual?

*PseudoCode 2*
- Does the algorithm check if the list is empty?
- Does it handle invalid inputs (like letters instead of numbers)?
- Does it avoid crashing when inputs are unusual?

### **6. Final Answer**
**Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
