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

    :param ellipsis ellipsis:
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

    :param ellipsis ellipsis:
        variable arguments

.. This file was automatic generated / don't edit.

