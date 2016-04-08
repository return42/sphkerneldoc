
.. _API-rpc-mkpipe-dentry:

=================
rpc_mkpipe_dentry
=================

*man rpc_mkpipe_dentry(9)*

*4.6.0-rc1*

make an rpc_pipefs file for kernel<->userspace communication


Synopsis
========

.. c:function:: struct dentry ⋆ rpc_mkpipe_dentry( struct dentry * parent, const char * name, void * private, struct rpc_pipe * pipe )

Arguments
=========

``parent``
    dentry of directory to create new “pipe” in

``name``
    name of pipe

``private``
    private data to associate with the pipe, for the caller's use

``pipe``
    ``rpc_pipe`` containing input parameters


Description
===========

Data is made available for userspace to read by calls to ``rpc_queue_upcall``. The actual reads will result in calls to ``ops``->upcall, which will be called with the file pointer,
message, and userspace buffer to copy to.

Writes can come at any time, and do not necessarily have to be responses to upcalls. They will result in calls to ``msg``->downcall.

The ``private`` argument passed here will be available to all these methods from the file pointer, via RPC_I(file_inode(file))->private.
