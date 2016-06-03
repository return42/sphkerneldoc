/* parse-markup: reST */

/* parse-SNIP: intro */
/**
 * DOC: kernel-doc intro
 *
 * This file / chapter includes all the refered examples of the kernel-doc-HOWTO
 * and additional tests.
 *
 * The content itself is nonsens / don’t look to close ;-)
 */
/* parse-SNAP: */


/* parse-SNIP: hello-world */
#include<stdio.h>
int main() {
  printf("Hello World\n");
  return 0;
}
/* parse-SNAP: */


/* parse-SNIP: my_struct */
/**
 * struct my_struct - short description
 * @a: first member
 * @b: second member
 *
 * Longer description
 */
struct my_struct {
    int a;
    int b;
/* private: */
    int c;
};
/* parse-SNAP: */


/* parse-SNIP: my_long_struct */
/**
 * struct my_struct - short description
 * @a: first member
 * @b: second member
 *
 * Longer description
 */
struct my_long_struct {
  int a;
  int b;
  /**
   * @c: This is longer description of C.
   *
   * You can use paragraphs to describe arguments
   * using this method.
   */
  int c;
};
/* parse-SNAP: */


/* parse-SNIP: theory-of-operation */
/**
 * DOC: Theory of Operation
 *
 * The whizbang foobar is a dilly of a gizmo.  It can do whatever you
 * want it to do, at any time.  It reads your mind.  Here's how it works.
 *
 * foo bar splat
 *
 * The only drawback to this gizmo is that is can sometimes damage
 * hardware, software, or its subject(s).
 */
/* parse-SNAP: */



/* parse-SNIP: user_function */
/**
 * user_function - function that can only be called in user context
 * @a: some argument
 * Context: !in_interrupt()
 *
 * This function makes no sense, it is only kernel-doc demonstration.
 *
 * ::
 *
 * Example:
 * x = user_function(22);
 *
 * Return:
 * Returns first argument
 */
int user_function(int a)
{
  return a;
}
/* parse-SNAP: */




/* parse-markup: kernel-doc */

/**
 * vintage - short description of this function
 * @parameter_a: first argument
 * @parameter_b: second argument
 * Context: in_gizmo_mode().
 *
 * Long description. This function has two integer arguments. The first is
 * @parameter_a and the second is @parameter_b.
 *
 * Example:
 * user_function(22);
 *
 * Return:
 * Sum of @parameter_a and @parameter_b.
 *
 * highlighting:
 *
 * - vintage()    : function
 * - @parameter_a : name of a parameter
 * - $ENVVAR      : environmental variable
 * - &my_struct   : name of a structure (up to two words including ``struct``)
 * - %CONST       : name of a constant.
 *
 * Parser Mode: *vintage* kernel-doc mode
 *
 * Within the *vintage kernel-doc mode* dogged ignores any whitespace or inline
 * markup.
 *
 * - Inline markup like *emphasis* or **emphasis strong**
 * - Literals and/or block indent:
 *
 *      a + b
 *
 * In kernel-doc *vintage* mode, there are no special block or inline markups
 * available. Markups like the one above result in ambiguous reST markup which
 * could produce error messages in the subsequently sphinx-build
 * process. Unexpected outputs are mostly the result.
 *
 * This is a link https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/
 * to the Linux kernel source tree
 *
 * colon markup: sectioning by colon markup in vintage mode is partial ugly. ;-)
 *
 */
int vintage(int parameter_a, char parameter_b)
{
  return a + b;
}


/* parse-markup: reST */

/**
 * rst_mode - short description of this function
 * @a: first argument
 * @b: second argument
 * Context: :c:func:`in_gizmo_mode`.
 *
 * Long description. This function has two integer arguments. The first is
 * ``parameter_a`` and the second is ``parameter_b``.
 *
 * As long as the reST / sphinx-doc toolchain uses `intersphinx
 * <http://www.sphinx-doc.org/en/stable/ext/intersphinx.html>`__ you can refer
 * definitions *outside* like :c:type:`struct media_device <media_device>`.  If
 * the description of ``media_device`` struct is found in any of the intersphinx
 * locations, a hyperref to this target is genarated a build time.
 *
 * Example:
 *
 * .. code-block:: c
 *
 *     user_function(22);
 *
 * Return:
 * Sum of ``parameter_a`` and the second is ``parameter_b``.
 *
 * highlighting:
 *
 * Because reST markup syntax conflicts with the highlighting markup from the
 * *vintage* mode, these *vintage* highlighting markup is not available in
 * reST-mode. reST brings it's own markup to refer and highlight function,
 * structs or whatever definition :
 *
 * - :c:func:`rst_mode` : function
 * - ``$ENVVAR``:  environmental variable
 * - :c:type:`my_struct` : name of a structure
 * - ``parameter_a`` : name of a parameter
 * - ``CONST`` : name of a constant.
 *
 * Parser Mode:
 *
 * This is an example with activated reST additions, in this section you will
 * find some common inline markups.
 *
 * Within the *reST mode* the kernel-doc parser pass through all markups to the
 * reST toolchain, except the *vintage highlighting* but including any
 * whitespace. With this, the full reST markup is available in the comments.
 *
 * This is a link to the `Linux kernel source tree
 * <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/>`_.
 *
 * This description is only to show some reST inline markups like *emphasise*
 * and **emphasis strong**. The follwing is a demo of a reST list markup:
 *
 * Definition list:
 * :def1: lorem
 * :def2: ipsum
 *
 * Ordered List:
 * - item one
 * - item two
 * - item three with
 *   a linebreak
 *
 * Literal blocks:
 * The next example shows a literal block::
 *
 *     +------+          +------+
 *     |\     |\        /|     /|
 *     | +----+-+      +-+----+ |
 *     | |    | |      | |    | |
 *     +-+----+ |      | +----+-+
 *      \|     \|      |/     |/
 *       +------+      +------+
 *
 * Highlighted code blocks:
 * The next example shows a code example, with highlighting C syntax in the
 * output.
 *
 * .. code-block:: c
 *
 *     // Hello World program
 *
 *     #include<stdio.h>
 *
 *     int main()
 *     {
 *         printf("Hello World");
 *     }
 *
 *
 * reST sectioning:
 *
 * colon markup: sectioning by colon markup in reST mode is less ugly. ;-)
 *
 * A kernel-doc section like *this* section is translated into a reST
 * *subsection*. This means, you can only use the follwing *sub-levels* within a
 * kernel-doc section.
 *
 * a subsubsection
 * ^^^^^^^^^^^^^^^
 *
 * lorem ipsum
 *
 * a paragraph
 * """""""""""
 *
 * lorem ipsum
 *
 */

int rst_mode(int a, char b)
{
  return a + b;
}

