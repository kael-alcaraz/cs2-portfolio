# FINAL CODE: [score_checker.py](score_checker.py)
### Analysis
##### The input needs to be an integer, within the range 0 (the minimum value) and 100 (the maximum value.) It produces 5 different outcomes. The part that needs the boundaries is the invalid score decision, and what needs multiple decisions is the score checker itself.
### Flowchart:
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/df8d040e-ad74-4143-bdeb-b3e0470edd22" />
#### Pseudocode: function main()
    output "Put your score below: "
    input SCORE
    if SCORE < 0 OR SCORE > 100 then
        output "Oops! That is not a valid score."
    else
        if SCORE >= 90 then
            output "That is an outstanding score."
        else
            if SCORE >= 80 then
                output "That is a very satisfactory score."
            else
                if SCORE >= 75 then
                    output "That is a satisfactory score."
                else
                    output "That score needs some improvement."
                end If
            end If
        end If
    end If
end function
### Test
#### Test 1: -1 Expected output: Invalid score message Actual output: Invalid score message Result: Pass
#### Test 2: 0 Expected output: Needs improvement message Actual output: Needs improvement message Result: Pass
#### Test 3: 74 Expected output: Needs improvement message Actual output: Needs improvement message Result: Pass
#### Test 4: 75 Expected output: Satisfactory message Actual output: Satisfactory message Result: Pass
#### Test 5: 80 Expected output: Very satisfactory message Actual output: Very satisfactory message Result: Pass
#### Test 6: 90 Expected output: Outstanding message Actual output: Outstanding message Result: Pass
#### Test 7: 100 Expected output: Outstanding message Actual output: Outstanding message Result: Pass
#### Test 8: 101 Expected output: Invalid score message Actual output: Invalid score message Result: Pass
### Reflection
#### Testing Reflection: We test 0 and 100 for edge cases such as those. -1 and 101 are also important to make sure the boundaries hold. Tests 1, 2, 9, and 10 helped me understand the boundaries more. None of the tests failed.
#### Reflection: Selection structures made it more useful, as at its base is a sorting system hat needs selections. Proper comments help show the logic, and readable formatting shows how it works easily. It is more useful to plan it using a flowchart first, as that gives you a rough layout of the final code.
