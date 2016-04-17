.. -*- coding: utf-8; mode: rst -*-

==============
rbtree_latch.h
==============


.. _`latch_tree_insert`:

latch_tree_insert
=================

.. c:function:: void latch_tree_insert (struct latch_tree_node *node, struct latch_tree_root *root, const struct latch_tree_ops *ops)

    insert @node into the trees @root

    :param struct latch_tree_node \*node:
        nodes to insert

    :param struct latch_tree_root \*root:
        trees to insert ``node`` into

    :param const struct latch_tree_ops \*ops:
        operators defining the node order



.. _`latch_tree_insert.description`:

Description
-----------

It inserts ``node`` into ``root`` in an ordered fashion such that we can always
observe one complete tree. See the comment for :c:func:`raw_write_seqcount_latch`.

The inserts use :c:func:`rcu_assign_pointer` to publish the element such that the
tree structure is stored before we can observe the new ``node``\ .

All modifications (latch_tree_insert, latch_tree_remove) are assumed to be
serialized.



.. _`latch_tree_erase`:

latch_tree_erase
================

.. c:function:: void latch_tree_erase (struct latch_tree_node *node, struct latch_tree_root *root, const struct latch_tree_ops *ops)

    removes @node from the trees @root

    :param struct latch_tree_node \*node:
        nodes to remote

    :param struct latch_tree_root \*root:
        trees to remove ``node`` from

    :param const struct latch_tree_ops \*ops:
        operators defining the node order



.. _`latch_tree_erase.description`:

Description
-----------

Removes ``node`` from the trees ``root`` in an ordered fashion such that we can
always observe one complete tree. See the comment for
:c:func:`raw_write_seqcount_latch`.

It is assumed that ``node`` will observe one RCU quiescent state before being
reused of freed.

All modifications (latch_tree_insert, latch_tree_remove) are assumed to be
serialized.



.. _`latch_tree_find`:

latch_tree_find
===============

.. c:function:: struct latch_tree_node *latch_tree_find (void *key, struct latch_tree_root *root, const struct latch_tree_ops *ops)

    find the node matching @key in the trees @root

    :param void \*key:
        search key

    :param struct latch_tree_root \*root:
        trees to search for ``key``

    :param const struct latch_tree_ops \*ops:
        operators defining the node order



.. _`latch_tree_find.description`:

Description
-----------

Does a lockless lookup in the trees ``root`` for the node matching ``key``\ .

It is assumed that this is called while holding the appropriate RCU read
side lock.

If the operators define a partial order on the elements (there are multiple
elements which have the same key value) it is undefined which of these
elements will be found. Nor is it possible to iterate the tree to find
further elements with the same key value.



.. _`latch_tree_find.returns`:

Returns
-------

a pointer to the node matching ``key`` or NULL.

