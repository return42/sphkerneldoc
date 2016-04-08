
.. _API-rpc-add-pipe-dir-object:

=======================
rpc_add_pipe_dir_object
=======================

*man rpc_add_pipe_dir_object(9)*

*4.6.0-rc1*

associate a rpc_pipe_dir_object to a directory


Synopsis
========

.. c:function:: int rpc_add_pipe_dir_object( struct net * net, struct rpc_pipe_dir_head * pdh, struct rpc_pipe_dir_object * pdo )

Arguments
=========

``net``
    pointer to struct net

``pdh``
    pointer to struct rpc_pipe_dir_head

``pdo``
    pointer to struct rpc_pipe_dir_object
