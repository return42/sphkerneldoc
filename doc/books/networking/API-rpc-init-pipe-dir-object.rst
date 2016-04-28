.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-init-pipe-dir-object:

========================
rpc_init_pipe_dir_object
========================

*man rpc_init_pipe_dir_object(9)*

*4.6.0-rc5*

initialise a struct rpc_pipe_dir_object


Synopsis
========

.. c:function:: void rpc_init_pipe_dir_object( struct rpc_pipe_dir_object * pdo, const struct rpc_pipe_dir_object_ops * pdo_ops, void * pdo_data )

Arguments
=========

``pdo``
    pointer to struct rpc_pipe_dir_object

``pdo_ops``
    pointer to const struct rpc_pipe_dir_object_ops

``pdo_data``
    pointer to caller-defined data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
