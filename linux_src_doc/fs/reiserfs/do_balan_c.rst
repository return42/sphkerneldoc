.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/reiserfs/do_balan.c

.. _`balance_leaf`:

balance_leaf
============

.. c:function:: int balance_leaf(struct tree_balance *tb, struct item_head *ih, const char *body, int flag, struct item_head *insert_key, struct buffer_head **insert_ptr)

    reiserfs tree balancing algorithm

    :param tb:
        tree balance state
    :type tb: struct tree_balance \*

    :param ih:
        item header of inserted item (little endian)
    :type ih: struct item_head \*

    :param body:
        body of inserted item or bytes to paste
    :type body: const char \*

    :param flag:
        i - insert, d - delete, c - cut, p - paste (see do_balance)
    :type flag: int

    :param insert_key:
        key to insert new nodes
    :type insert_key: struct item_head \*

    :param insert_ptr:
        array of nodes to insert at the next level
    :type insert_ptr: struct buffer_head \*\*

.. _`balance_leaf.description`:

Description
-----------

In our processing of one level we sometimes determine what must be
inserted into the next higher level.  This insertion consists of a
key or two keys and their corresponding pointers.

.. This file was automatic generated / don't edit.

