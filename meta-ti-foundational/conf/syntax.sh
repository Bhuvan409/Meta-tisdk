#!/bin/bash

# This file contains intentional syntax errors for testing

echo "Starting test"

if [ -f "test.txt" ]; then
    echo "File exists"
# Missing 'fi' to close if statement

for i in 1 2 3; do
    echo $i
# Missing 'done' to close for loop

function test_func {
    echo "Test function"
# Missing closing brace
