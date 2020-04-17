/*Now we're going to write  a program to find the roots of a quadratic equation*/
/*it takes in a, b, c*/

/**First you want to include a couple things */

#include <math.h>
#include <stdio.h>

int main () {
  /*In all C program we define all of the variable we will ever need in the beginning*/
  /*the data type double in c is like a float*/
  double a, b, c, discrim, root1, root2, real, imagine;
  /**First we need to prompt the user to enter in a , b ,c and then we will scan them*/
  printf("Enter in a, b, c");
  scanf("%lf" "%lf" "%lf", &a, &b, &c);

  /* now this is the important part, lets define the discriminant equation */
  discrim = b*b -4*a*c ;

  /*Now let's set up the if else statement*/

  if (discrim > 0){
    root1 = (-b + sqrt(b-(4*a*c)))* (1/(2*a));
    root2 = (-b - sqrt(b-(4*a*c)))* (1/(2*a));
    printf("root1 = %.2lf and root2 = %.2lf", root1, root2);
  }

  else if (discrim == 0){
    root1 = (-b* (1/(2*a)));
    printf("root1 = root2 = %.2lf", root1);
  }

/*Now we finally find the real and imaginary part of the roots!*/
  else {
    real = (-b* (1/(2*a)));
    imagine = (sqrt(b-(4*a*c)))* (1/2*a);
    printf("root1 = %.2lf - %.2lfi and root2 = %.2lf + %.2lfi", real, imagine, real, imagine);
  }
}
