// this test some kernel-doc stuff

/* parse-SNIP: hello-world */
#include<stdio.h>
int main() {
  printf("Hello World\n");
  return 0;
}
/* parse-SNAP: */

/* parse-SNIP: user_function */
/**
 * user_function - function that can only be called in user context
 * @a: some argument
 *
 * This function makes no sense, it's only a kernel-doc demonstration.
 *
 * Example:
 * x = user_function(22);
 *
 * Return:
 * Returns first argument
 */
int
user_function(int a)
{
  return a;
}
/* parse-SNAP: */

/* parse-SNIP: internal_function */
/**
 * internal_function - the answer
 *
 * Context: !sanity()
 *
 * Return:
 * The answer to the ultimate question of life, the universe and everything.
 */
int internal_function()
{
  return 42;
}
/* parse-SNAP: */

