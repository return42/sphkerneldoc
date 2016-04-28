.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-find-or-alloc-pipe-dir-object:

=================================
rpc_find_or_alloc_pipe_dir_object
=================================

*man rpc_find_or_alloc_pipe_dir_object(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: struct rpc_pipe_dir_object * rpc_find_or_alloc_pipe_dir_object( struct net * net, struct rpc_pipe_dir_head * pdh, int (*match) struct rpc_pipe_dir_object *, void *, struct rpc_pipe_dir_object *(*alloc) void *, void * data )

Arguments
=========

``net``
    pointer to struct net

``pdh``
    pointer to struct rpc_pipe_dir_head

``match``
    match struct rpc_pipe_dir_object to data

``alloc``
    allocate a new struct rpc_pipe_dir_object

``data``
    user defined data for ``match`` and ``alloc``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
