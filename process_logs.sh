#!/bin/bash

# Ensure log file exists
if [ ! -f logs.txt ]; then
    echo "Log file not found!"
    exit 1
fi

# Extract errors
grep "ERROR" logs.txt > errors.txt

# Count unique error codes
awk '{print $4}' errors.txt | sort | uniq -c > error_codes_for_viz.txt

# Display contents for verification
echo "Errors found:"
cat errors.txt

echo "Error code frequencies:"
cat error_codes_for_viz.txt
