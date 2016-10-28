.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/reiserfs/do_balan.c

.. _`balance_leaf`:

balance_leaf
============

.. c:function:: int balance_leaf(struct tree_balance *tb, struct item_head *ih, const char *body, int flag, struct item_head *insert_key, struct buffer_head **insert_ptr)

    reiserfs tree balancing algorithm

    :param struct tree_balance \*tb:
        tree balance state

    :param struct item_head \*ih:
        item header of inserted item (little endian)

    :param const char \*body:
        body of inserted item or bytes to paste

    :param int flag:
        i - insert, d - delete, c - cut, p - paste (see do_balance)

    :param struct item_head \*insert_key:
        key to insert new nodes

    :param struct buffer_head \*\*insert_ptr:
        array of nodes to insert at the next level

.. _`balance_leaf.description`:

Description
-----------

In our processing of one level we sometimes determine what must be
inserted into the next higher level.  This insertion consists of a
key or two keys and their corresponding pointers.

.. This file was automatic generated / don't edit.

