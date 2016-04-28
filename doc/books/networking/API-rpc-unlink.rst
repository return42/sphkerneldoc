.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-unlink:

==========
rpc_unlink
==========

*man rpc_unlink(9)*

*4.6.0-rc5*

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

After this call, lookups will no longer find the pipe, and any attempts
to read or write using preexisting opens of the pipe will return -EPIPE.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
