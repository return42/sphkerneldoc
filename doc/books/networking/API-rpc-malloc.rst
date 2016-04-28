.. -*- coding: utf-8; mode: rst -*-

.. _API-rpc-malloc:

==========
rpc_malloc
==========

*man rpc_malloc(9)*

*4.6.0-rc5*

allocate an RPC buffer


Synopsis
========

.. c:function:: void * rpc_malloc( struct rpc_task * task, size_t size )

Arguments
=========

``task``
    RPC task that will use this buffer

``size``
    requested byte size


Description
===========

To prevent rpciod from hanging, this allocator never sleeps, returning
NULL and suppressing warning if the request cannot be serviced
immediately. The caller can arrange to sleep in a way that is safe for
rpciod.

Most requests are 'small' (under 2KiB) and can be serviced from a
mempool, ensuring that NFS reads and writes can always proceed, and that
there is good locality of reference for these buffers.

In order to avoid memory starvation triggering more writebacks of NFS
requests, we avoid using GFP_KERNEL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
