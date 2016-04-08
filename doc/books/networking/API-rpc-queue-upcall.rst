
.. _API-rpc-queue-upcall:

================
rpc_queue_upcall
================

*man rpc_queue_upcall(9)*

*4.6.0-rc1*

queue an upcall message to userspace


Synopsis
========

.. c:function:: int rpc_queue_upcall( struct rpc_pipe * pipe, struct rpc_pipe_msg * msg )

Arguments
=========

``pipe``
    upcall pipe on which to queue given message

``msg``
    message to queue


Description
===========

Call with an ``inode`` created by ``rpc_mkpipe`` to queue an upcall. A userspace process may then later read the upcall by performing a read on an open file for this inode. It is
up to the caller to initialize the fields of ``msg`` (other than ``msg``->list) appropriately.
