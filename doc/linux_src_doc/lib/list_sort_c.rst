.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/list_sort.c

.. _`list_sort`:

list_sort
=========

.. c:function:: void list_sort(void *priv, struct list_head *head, int (*) cmp (void *priv, struct list_head *a, struct list_head *b)

    sort a list

    :param void \*priv:
        private data, opaque to \ :c:func:`list_sort`\ , passed to \ ``cmp``\ 

    :param struct list_head \*head:
        the list to sort

    :param (int (\*) cmp (void \*priv, struct list_head \*a, struct list_head \*b):
        the elements comparison function

.. _`list_sort.description`:

Description
-----------

This function implements "merge sort", which has O(nlog(n))
complexity.

The comparison function \ ``cmp``\  must return a negative value if \ ``a``\ 
should sort before \ ``b``\ , and a positive value if \ ``a``\  should sort after
\ ``b``\ . If \ ``a``\  and \ ``b``\  are equivalent, and their original relative
ordering is to be preserved, \ ``cmp``\  must return 0.

.. This file was automatic generated / don't edit.

