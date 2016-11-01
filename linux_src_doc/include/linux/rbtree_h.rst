.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rbtree.h

.. _`rbtree_postorder_for_each_entry_safe`:

rbtree_postorder_for_each_entry_safe
====================================

.. c:function::  rbtree_postorder_for_each_entry_safe( pos,  n,  root,  field)

    iterate in post-order over rb_root of given type allowing the backing memory of \ ``pos``\  to be invalidated

    :param  pos:
        the 'type \*' to use as a loop cursor.

    :param  n:
        another 'type \*' to use as temporary storage

    :param  root:
        'rb_root \*' of the rbtree.

    :param  field:
        the name of the rb_node field within 'type'.

.. _`rbtree_postorder_for_each_entry_safe.description`:

Description
-----------

rbtree_postorder_for_each_entry_safe() provides a similar guarantee as
\ :c:func:`list_for_each_entry_safe`\  and allows the iteration to continue independent
of changes to \ ``pos``\  by the body of the loop.

Note, however, that it cannot handle other modifications that re-order the
rbtree it is iterating over. This includes calling \ :c:func:`rb_erase`\  on \ ``pos``\ , as
\ :c:func:`rb_erase`\  may rebalance the tree, causing us to miss some nodes.

.. This file was automatic generated / don't edit.

