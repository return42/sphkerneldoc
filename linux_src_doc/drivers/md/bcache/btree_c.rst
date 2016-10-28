.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/btree.c

.. _`btree`:

btree
=====

.. c:function::  btree( fn,  key,  b,  op,  ...)

    recurse down the btree on a specified key

    :param  fn:
        function to call, which will be passed the child node

    :param  key:
        key to recurse on

    :param  b:
        parent btree node

    :param  op:
        pointer to struct btree_op

    :param ... :
        variable arguments

.. _`btree_root`:

btree_root
==========

.. c:function::  btree_root( fn,  c,  op,  ...)

    call a function on the root of the btree

    :param  fn:
        function to call, which will be passed the child node

    :param  c:
        cache set

    :param  op:
        pointer to struct btree_op

    :param ... :
        variable arguments

.. _`bch_btree_node_get`:

bch_btree_node_get
==================

.. c:function:: struct btree *bch_btree_node_get(struct cache_set *c, struct btree_op *op, struct bkey *k, int level, bool write, struct btree *parent)

    find a btree node in the cache and lock it, reading it in from disk if necessary.

    :param struct cache_set \*c:
        *undescribed*

    :param struct btree_op \*op:
        *undescribed*

    :param struct bkey \*k:
        *undescribed*

    :param int level:
        *undescribed*

    :param bool write:
        *undescribed*

    :param struct btree \*parent:
        *undescribed*

.. _`bch_btree_node_get.description`:

Description
-----------

If IO is necessary and running under generic_make_request, returns -EAGAIN.

The btree node will have either a read or a write lock held, depending on
level and op->lock.

.. This file was automatic generated / don't edit.

