
.. _API-rpc-remove-pipe-dir-object:

==========================
rpc_remove_pipe_dir_object
==========================

*man rpc_remove_pipe_dir_object(9)*

*4.6.0-rc1*

remove a rpc_pipe_dir_object from a directory


Synopsis
========

.. c:function:: void rpc_remove_pipe_dir_object( struct net * net, struct rpc_pipe_dir_head * pdh, struct rpc_pipe_dir_object * pdo )

Arguments
=========

``net``
    pointer to struct net

``pdh``
    pointer to struct rpc_pipe_dir_head

``pdo``
    pointer to struct rpc_pipe_dir_object
