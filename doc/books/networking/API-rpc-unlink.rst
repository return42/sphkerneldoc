
.. _API-rpc-unlink:

==========
rpc_unlink
==========

*man rpc_unlink(9)*

*4.6.0-rc1*

remove a pipe


Synopsis
========

.. c:function:: int rpc_unlink( struct dentry * dentry )

Arguments
=========

``dentry``
    dentry for the pipe, as returned from rpc_mkpipe


Description
===========

After this call, lookups will no longer find the pipe, and any attempts to read or write using preexisting opens of the pipe will return -EPIPE.
