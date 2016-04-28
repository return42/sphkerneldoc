.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-get-undo-access:

============================
jbd2_journal_get_undo_access
============================

*man jbd2_journal_get_undo_access(9)*

*4.6.0-rc5*

Notify intent to modify metadata with non-rewindable consequences


Synopsis
========

.. c:function:: int jbd2_journal_get_undo_access( handle_t * handle, struct buffer_head * bh )

Arguments
=========

``handle``
    transaction

``bh``
    buffer to undo


Description
===========

Sometimes there is a need to distinguish between metadata which has been
committed to disk and that which has not. The ext3fs code uses this for
freeing and allocating space, we have to make sure that we do not reuse
freed space until the deallocation has been committed, since if we
overwrote that space we would make the delete un-rewindable in case of a
crash.

To deal with that, jbd2_journal_get_undo_access requests write
access to a buffer for parts of non-rewindable operations such as delete
operations on the bitmaps. The journaling code must keep a copy of the
buffer's contents prior to the undo_access call until such time as we
know that the buffer has definitely been committed to disk.

We never need to know which transaction the committed data is part of,
buffers touched here are guaranteed to be dirtied later and so will be
committed to a new transaction in due course, at which point we can
discard the old committed data pointer.

Returns error number or 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
