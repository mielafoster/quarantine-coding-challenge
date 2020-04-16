/* This program will be in C*/
/* In C a character holds a ASCII value, which is an integer, not the character itself*/
/* ASCII stands for American Standard Code for Information Interchange*/
/* This program will print the ASCII value of any char we prompt*/

/* In C remember to always include stdio.h. It tells the compiler to insert the contents of stdio at that particular place*/
/*In other words it takes what we type and outputs it on the screen*/
#include <stdio.h>

int main(){
  /*This tells us that the function the main function will return an integer*/
  char c;
  /**the only variable it takes in*/
  printf("Please enter a character: ");
  scanf("%c", &c);
  /*scanf is a function that allows you to accept input
  it will read  in the char*/
  /*Now we want to print the ASCII value*/
  printf("ASCII value of %c = %d", c, c);
  return 0;
}
