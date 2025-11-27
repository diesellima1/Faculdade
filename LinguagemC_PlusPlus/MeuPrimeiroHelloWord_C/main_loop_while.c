/* MeuPrimeiroHelloWord_C/main_loop_while/main.c
tabuada de 2 usando loop while
*/

#include <stdio.h>// Include standard input-output library
int main() {                            // Main function
    int res, x = 1;                    // Initialize x to 1
   
    while (x <= 10){                  // Loop while x is less than or equal to 10
        res = 2 * x;                 //calculate 2 times x
        printf("%d\n", res);        // Print the result
        x = x + 1;                 // Increment x by 1
    }    
    return 0;                    // Return 0 to indicate successful execution
}