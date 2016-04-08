
.. _API-rpc-init-pipe-dir-object:

========================
rpc_init_pipe_dir_object
========================

*man rpc_init_pipe_dir_object(9)*

*4.6.0-rc1*

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
