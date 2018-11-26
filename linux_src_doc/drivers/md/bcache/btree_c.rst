.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/btree.c

.. _`btree`:

btree
=====

.. c:function::  btree( fn,  key,  b,  op,  ...)

    recurse down the btree on a specified key

    :param fn:
        function to call, which will be passed the child node
    :type fn: 

    :param key:
        key to recurse on
    :type key: 

    :param b:
        parent btree node
    :type b: 

    :param op:
        pointer to struct btree_op
    :type op: 

    :param ellipsis ellipsis:
        variable arguments

.. _`btree_root`:

btree_root
==========

.. c:function::  btree_root( fn,  c,  op,  ...)

    call a function on the root of the btree

    :param fn:
        function to call, which will be passed the child node
    :type fn: 

    :param c:
        cache set
    :type c: 

    :param op:
        pointer to struct btree_op
    :type op: 

    :param ellipsis ellipsis:
        variable arguments

.. This file was automatic generated / don't edit.

