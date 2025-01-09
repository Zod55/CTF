#include <stdio.h>
#include <string.h>

void vulnerable_function(char* user_input) {
    int secret_value = 123;  // Value to be overwritten by the attacker
    printf("Before user input: secret_value = %d\n", secret_value);

    // Vulnerable printf - directly using user-controlled input
    printf(user_input);

    printf("\nAfter user input: secret_value = %d\n", secret_value);
}

int main() {
    char input[100];

    // Get input from the user
    printf("Enter your input: ");
    fgets(input, sizeof(input), stdin);

    // Call vulnerable function with user input
    vulnerable_function(input);

    return 0;
}
