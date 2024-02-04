#include <stdio.h>

	int main() {
    	int a = 2;
    	int b = 2;
    	int c = a + b;

    	// Array of strings
    	char *users[] = {"User1", "User2", "User3"};

    	// Print the array using a FOR loop
    	for (int i = 0; i < sizeof(users) / sizeof(users[0]); i++)
	{
        	printf("User: %s\n", users[i]);
    	}

    	printf("C says: Hello, World!\n");
    	printf("%d + %d = %d\n", a, b, c);

    	return 0;
	}

