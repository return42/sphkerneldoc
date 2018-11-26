.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rbtree_latch.h

.. _`latch_tree_insert`:

latch_tree_insert
=================

.. c:function:: void latch_tree_insert(struct latch_tree_node *node, struct latch_tree_root *root, const struct latch_tree_ops *ops)

    insert \ ``node``\  into the trees \ ``root``\ 

    :param node:
        nodes to insert
    :type node: struct latch_tree_node \*

    :param root:
        trees to insert \ ``node``\  into
    :type root: struct latch_tree_root \*

    :param ops:
        operators defining the node order
    :type ops: const struct latch_tree_ops \*

.. _`latch_tree_insert.description`:

Description
-----------

It inserts \ ``node``\  into \ ``root``\  in an ordered fashion such that we can always
observe one complete tree. See the comment for \ :c:func:`raw_write_seqcount_latch`\ .

The inserts use \ :c:func:`rcu_assign_pointer`\  to publish the element such that the
tree structure is stored before we can observe the new \ ``node``\ .

All modifications (latch_tree_insert, latch_tree_remove) are assumed to be
serialized.

.. _`latch_tree_erase`:

latch_tree_erase
================

.. c:function:: void latch_tree_erase(struct latch_tree_node *node, struct latch_tree_root *root, const struct latch_tree_ops *ops)

    removes \ ``node``\  from the trees \ ``root``\ 

    :param node:
        nodes to remote
    :type node: struct latch_tree_node \*

    :param root:
        trees to remove \ ``node``\  from
    :type root: struct latch_tree_root \*

    :param ops:
        operators defining the node order
    :type ops: const struct latch_tree_ops \*

.. _`latch_tree_erase.description`:

Description
-----------

Removes \ ``node``\  from the trees \ ``root``\  in an ordered fashion such that we can
always observe one complete tree. See the comment for
\ :c:func:`raw_write_seqcount_latch`\ .

It is assumed that \ ``node``\  will observe one RCU quiescent state before being
reused of freed.

All modifications (latch_tree_insert, latch_tree_remove) are assumed to be
serialized.

.. _`latch_tree_find`:

latch_tree_find
===============

.. c:function:: struct latch_tree_node *latch_tree_find(void *key, struct latch_tree_root *root, const struct latch_tree_ops *ops)

    find the node matching \ ``key``\  in the trees \ ``root``\ 

    :param key:
        search key
    :type key: void \*

    :param root:
        trees to search for \ ``key``\ 
    :type root: struct latch_tree_root \*

    :param ops:
        operators defining the node order
    :type ops: const struct latch_tree_ops \*

.. _`latch_tree_find.description`:

Description
-----------

Does a lockless lookup in the trees \ ``root``\  for the node matching \ ``key``\ .

It is assumed that this is called while holding the appropriate RCU read
side lock.

If the operators define a partial order on the elements (there are multiple
elements which have the same key value) it is undefined which of these
elements will be found. Nor is it possible to iterate the tree to find
further elements with the same key value.

.. _`latch_tree_find.return`:

Return
------

a pointer to the node matching \ ``key``\  or NULL.

.. This file was automatic generated / don't edit.

