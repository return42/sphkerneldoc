/* parse-markup: reST */

/**
 * DOC: About Examples
 *
 * The file ``all-in-a-tumble.h`` includes all the referred examples of the
 * kernel-doc-HOWTO. It is also used as a test of the kernel-doc parser, to see
 * how kernel-doc content will be rendered and where the parser might fail.
 *
 * The content itself is nonsense / don’t look to close ;-)
 */


// The parse-SNIP/SNAP comments are used to include the C sorce code as snippets
// into a reST document. These are the examples of the kernel-doc-HOWTO book.

/* parse-SNIP: hello-world */
#include<stdio.h>
int main() {
  printf("Hello World\n");
  return 0;
}
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
 * struct my_long_struct - short description with &my_struct->a and &my_struct->b
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


/* parse-SNIP: my_union */
/**
 * union my_union - short description
 * @a: first member
 * @b: second member
 *
 * Longer description
 */
union my_union {
    int a;
    int b;
};
/* parse-SNAP: */


/* parse-SNIP: my_enum */
/**
 * enum my_enum - log level
 * @QUIET: logs nothing
 * @INFO: logs info messages
 * @WARN: logs warn and info messages
 * @DEBUG: logs debug, warn and info messages
 */

enum my_enum {
  QUIET,
  INFO,
  WARN,
  DEBUG
};
/* parse-SNAP: */


/* parse-SNIP: my_typedef */
/**
 * typedef my_typedef - useless typdef of int
 *
 */
typedef int my_typedef;
/* parse-SNAP: */



/* parse-SNIP: user_function */
/**
 * user_function - function that can only be called in user context
 * @a: some argument
 * Context: !in_interrupt()
 *
 * This function makes no sense, it is only kernel-doc demonstration.
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
 * locations, a hyperref to this target is generated a build time.
 *
 * Example:
 *   int main() {
 *     printf("Hello World\n");
 *     return 0;
 *   }
 *
 * Return:
 * Sum of ``parameter_a`` and the second is ``parameter_b``.
 *
 * highlighting:
 * The highlight pattern, are non regular reST markups. They are only available
 * within kernel-doc comments, helping C developers to write short and compact
 * documentation.
 *
 * - user_function() : function
 * - @a : name of a parameter
 * - &struct my_struct : name of a structure (including the word struct)
 * - &union my_union : name of a union
 * - &my_struct->a or &my_struct.b -  member of a struct or union.
 * - &enum my_enum : name of a enum
 * - &typedef my_typedef : name of a typedef
 * - %CONST : name of a constant.
 * - $ENVVAR : environmental variable
 *
 * The kernel-doc parser translates the pattern above to the corresponding reST
 * markups. You don't have to use the *highlight* pattern, if you prefer *pure*
 * reST, use the reST markup.
 *
 * - :c:func:`user_function` : function
 * - ``a`` : name of a parameter
 * - :c:type:`struct my_struct <my_struct>` : name of a structure (including the word struct)
 * - :c:type:`union my_union <my_union>` : name of a union
 * - :c:type:`my_struct->a <my_struct>` or :c:type:`my_struct.b <my_struct>` -  member of a struct or union.
 * - :c:type:`enum my_enum <my_enum>` : name of a enum
 * - :c:type:`typedef my_typedef <my_typedef>` : name of a typedef
 * - ``CONST`` : name of a constant.
 * - ``\$ENVVAR`` : environmental variable
 *
 * Since the prefixes ``$...``, ``&...`` and ``@...`` are used to markup the
 * highlight pattern, you have to escape them in other uses: $lorem, \&lorem
 * and \@lorem. To esacpe from function highlighting, use lorem\().
 *
 * Parser Mode:
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
 * and **emphasis strong**. The following is a demo of a reST list markup:
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
 *     #include<stdio.h>
 *     int main\()
 *     {
 *        printf("Hello World");
 *     }
 *
 *
 * reST sectioning:
 *
 * colon markup: sectioning by colon markup in reST mode is less ugly. ;-)
 *
 * A kernel-doc section like *this* section is translated into a reST
 * *subsection*. This means, you can only use the following *sub-levels* within a
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



/* parse-markup: kernel-doc */

/**
 * vintage - short description of this function
 * @parameter_a: first argument
 * @parameter_b: second argument
 * Context: in_gizmo_mode().
 *
 * This is a test of a typical markup from *vintage* kernel-doc.  Don't look to
 * close here, it is only for testing some kernel-doc parser stuff.
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
 * Within the *vintage kernel-doc mode* ignores any whitespace or inline
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

