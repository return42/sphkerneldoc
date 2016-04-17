.. -*- coding: utf-8; mode: rst -*-

===============
libcfs_string.c
===============


.. _`cfs_gettok`:

cfs_gettok
==========

.. c:function:: int cfs_gettok (struct cfs_lstr *next, char delim, struct cfs_lstr *res)

    :param struct cfs_lstr \*next:

        *undescribed*

    :param char delim:

        *undescribed*

    :param struct cfs_lstr \*res:

        *undescribed*



.. _`cfs_gettok.description`:

Description
-----------


Looks for \a delim in string \a next, sets \a res to point to
substring before the delimiter, sets \a next right after the found
delimiter.

\retval 1 if \a res points to a string of non-whitespace characters
\retval 0 otherwise



.. _`cfs_str2num_check`:

cfs_str2num_check
=================

.. c:function:: int cfs_str2num_check (char *str, int nob, unsigned *num, unsigned min, unsigned max)

    :param char \*str:

        *undescribed*

    :param int nob:

        *undescribed*

    :param unsigned \*num:

        *undescribed*

    :param unsigned min:

        *undescribed*

    :param unsigned max:

        *undescribed*



.. _`cfs_str2num_check.description`:

Description
-----------


Accepts decimal and hexadecimal number recordings.

\retval 1 if first \a nob chars of \a str convert to decimal or
hexadecimal integer in the range [\a min, \a max]
\retval 0 otherwise



.. _`cfs_range_expr_parse`:

cfs_range_expr_parse
====================

.. c:function:: int cfs_range_expr_parse (struct cfs_lstr *src, unsigned min, unsigned max, int bracketed, struct cfs_range_expr **expr)

    :param struct cfs_lstr \*src:

        *undescribed*

    :param unsigned min:

        *undescribed*

    :param unsigned max:

        *undescribed*

    :param int bracketed:

        *undescribed*

    :param struct cfs_range_expr \*\*expr:

        *undescribed*



.. _`cfs_range_expr_parse.description`:

Description
-----------

\a src should only have a single token which can be \<number\> or  \*

\retval pointer to allocated range_expr and initialized



.. _`cfs_range_expr_parse.range_expr`:

range_expr
----------

:re_lo, range_expr::re_hi and range_expr:re_stride if \a
src parses to
\<number\> |
\<number\> '-' \<number\> |
\<number\> '-' \<number\> '/' \<number\>
\retval 0 will be returned if it can be parsed, otherwise -EINVAL or
-ENOMEM will be returned.



.. _`cfs_range_expr_print`:

cfs_range_expr_print
====================

.. c:function:: int cfs_range_expr_print (char *buffer, int count, struct cfs_range_expr *expr, bool bracketed)

    :param char \*buffer:

        *undescribed*

    :param int count:

        *undescribed*

    :param struct cfs_range_expr \*expr:

        *undescribed*

    :param bool bracketed:

        *undescribed*



.. _`cfs_range_expr_print.description`:

Description
-----------

If \a bracketed is true, expression does not need additional
brackets.

\retval number of characters written



.. _`cfs_expr_list_print`:

cfs_expr_list_print
===================

.. c:function:: int cfs_expr_list_print (char *buffer, int count, struct cfs_expr_list *expr_list)

    :param char \*buffer:

        *undescribed*

    :param int count:

        *undescribed*

    :param struct cfs_expr_list \*expr_list:

        *undescribed*



.. _`cfs_expr_list_print.description`:

Description
-----------

If the list contains several expressions, separate them with comma
and surround the list with brackets.

\retval number of characters written



.. _`cfs_expr_list_match`:

cfs_expr_list_match
===================

.. c:function:: int cfs_expr_list_match (__u32 value, struct cfs_expr_list *expr_list)

    :param __u32 value:

        *undescribed*

    :param struct cfs_expr_list \*expr_list:

        *undescribed*



.. _`cfs_expr_list_match.description`:

Description
-----------


\retval 1 if \a value matches
\retval 0 otherwise



.. _`cfs_expr_list_values`:

cfs_expr_list_values
====================

.. c:function:: int cfs_expr_list_values (struct cfs_expr_list *expr_list, int max, __u32 **valpp)

    :param struct cfs_expr_list \*expr_list:

        *undescribed*

    :param int max:

        *undescribed*

    :param __u32 \*\*valpp:

        *undescribed*



.. _`cfs_expr_list_values.description`:

Description
-----------


\retval N N is total number of all matched values
\retval 0 if expression list is empty
\retval < 0 for failure



.. _`cfs_expr_list_free`:

cfs_expr_list_free
==================

.. c:function:: void cfs_expr_list_free (struct cfs_expr_list *expr_list)

    :param struct cfs_expr_list \*expr_list:

        *undescribed*



.. _`cfs_expr_list_free.description`:

Description
-----------


\retval none



.. _`cfs_expr_list_parse`:

cfs_expr_list_parse
===================

.. c:function:: int cfs_expr_list_parse (char *str, int len, unsigned min, unsigned max, struct cfs_expr_list **elpp)

    :param char \*str:

        *undescribed*

    :param int len:

        *undescribed*

    :param unsigned min:

        *undescribed*

    :param unsigned max:

        *undescribed*

    :param struct cfs_expr_list \*\*elpp:

        *undescribed*



.. _`cfs_expr_list_parse.description`:

Description
-----------


\retval 0 if \a str parses to \<number\> | \<expr_list\>
\retval -errno otherwise



.. _`cfs_expr_list_free_list`:

cfs_expr_list_free_list
=======================

.. c:function:: void cfs_expr_list_free_list (struct list_head *list)

    :param struct list_head \*list:

        *undescribed*



.. _`cfs_expr_list_free_list.description`:

Description
-----------


For each struct cfs_expr_list structure found on \a list it frees
range_expr list attached to it and frees the cfs_expr_list itself.

\retval none

