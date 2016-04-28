.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-forget:

===================
jbd2_journal_forget
===================

*man jbd2_journal_forget(9)*

*4.6.0-rc5*

``bforget`` for potentially-journaled buffers.


Synopsis
========

.. c:function:: int jbd2_journal_forget( handle_t * handle, struct buffer_head * bh )

Arguments
=========

``handle``
    transaction handle

``bh``
    bh to 'forget'


Description
===========

We can only do the bforget if there are no commits pending against the
buffer. If the buffer is dirty in the current running transaction we can
safely unlink it.

bh may not be a journalled buffer at all - it may be a non-JBD buffer
which came off the hashtable. Check for this.

Decrements bh->b_count by one.

Allow this call even if the handle has aborted --- it may be part of the
caller's cleanup after an abort.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
