#!/bin/bash
# This file contains intentional syntax errors for testing

echo "Starting test"

# Error 1: Missing 'fi' to close if statement
if [ -f "test.txt" ]; then
    echo "File exists"
# Missing 'fi' here

# Error 2: Missing 'done' to close for loop
for i in 1 2 3; do
    echo $i
# Missing 'done' here

# Error 3: Missing closing brace in function definition
function test_func {
    echo "Test function"
# Missing closing brace '}'

# Error 4: Unquoted variable that should be quoted
TEST_VAR="file with spaces.txt"
cat $TEST_VAR

# Error 5: Command substitution with deprecated backticks
files_count=`ls -1 | wc -l`

# Error 6: Using == in [ ] test (should be = for POSIX compatibility)
if [ "$VAR" == "value" ]; then
    echo "Matched"
fi

# Error 7: Incorrect indentation
if [ true ]; then
echo "Bad indentation"
fi

# Error 8: Unnecessary cat usage (useless use of cat)
cat file.txt | grep "pattern"

# Error 9: Missing shebang line (already has one, but for testing)

# Error 10: Using /bin/sh with bash-specific features
# (can't directly demonstrate, but the checker should look for this)
