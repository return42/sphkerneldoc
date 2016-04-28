.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-init:

==========
fence_init
==========

*man fence_init(9)*

*4.6.0-rc5*

Initialize a custom fence.


Synopsis
========

.. c:function:: void fence_init( struct fence * fence, const struct fence_ops * ops, spinlock_t * lock, unsigned context, unsigned seqno )

Arguments
=========

``fence``
    [in] the fence to initialize

``ops``
    [in] the fence_ops for operations on this fence

``lock``
    [in] the irqsafe spinlock to use for locking this fence

``context``
    [in] the execution context this fence is run on

``seqno``
    [in] a linear increasing sequence number for this context


Description
===========

Initializes an allocated fence, the caller doesn't have to keep its
refcount after committing with this fence, but it will need to hold a
refcount again if fence_ops.enable_signaling gets called. This can be
used for other implementing other types of fence.

context and seqno are used for easy comparison between fences, allowing
to check which fence is later by simply using fence_later.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
