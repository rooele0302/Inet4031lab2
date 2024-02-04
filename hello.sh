#!/bin/bash

	a=2
	b=2
	c=$((a + b))

	# Array of strings
	users=("User1" "User2" "User3")

	# Print the array using a FOR loop
	for user in "${users[@]}"; do
    	echo "User: $user"
	done

	echo "Bash says: Hello, World!"
	echo "$a + $b = $c"

