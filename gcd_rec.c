/*This program demonstrates recursion in C. It will find the GCD of two numbers*/
/*We could use a loop but it would be smarter to use recursion*/
#include <stdio.h>

/*First we need to do the recursive call */
int gcf(int num1, int num2);
/*We need to include this at the beginning because the main function doesnt know what gcf is because we havent defined it yet*/

int main (){
  int num1, num2;
  /*Define the two numbers as integers*/
  printf("Enter in two numbers: ");
  /*Prompt the player*/
  scanf("%d" "%d", &num1 , &num2);

  /*Now we will print the final statment and include the recursive call*/
  printf(" The GCD of %d and %d is %d", num1, num2, gcf(num1, num2));
  /*exit code*/
  return 0;
}
/*Now lets define the GCD function*/

int gcf(num1, num2) {
  /*We want to define the base case. The recursive call will take the seocnd number and the remainder to keep find the  GCF */
  if (num2 != 0)
    return gcf(num2, num1 % num2);
    /*It will keep going down to find the new GCF, if the number 2 isnt zero*/
  else
  /*This is the base case, once the second number is equal to zero we know we've found the GCF.*/
    return num1;
}
