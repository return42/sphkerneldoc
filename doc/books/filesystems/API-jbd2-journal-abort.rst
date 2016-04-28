.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-abort:

==================
jbd2_journal_abort
==================

*man jbd2_journal_abort(9)*

*4.6.0-rc5*

Shutdown the journal immediately.


Synopsis
========

.. c:function:: void jbd2_journal_abort( journal_t * journal, int errno )

Arguments
=========

``journal``
    the journal to shutdown.

``errno``
    an error number to record in the journal indicating the reason for
    the shutdown.


Description
===========

Perform a complete, immediate shutdown of the ENTIRE journal (not of a
single transaction). This operation cannot be undone without closing and
reopening the journal.

The jbd2_journal_abort function is intended to support higher level
error recovery mechanisms such as the ext2/ext3 remount-readonly error
mode.

Journal abort has very specific semantics. Any existing dirty,
unjournaled buffers in the main filesystem will still be written to disk
by bdflush, but the journaling mechanism will be suspended immediately
and no further transaction commits will be honoured.

Any dirty, journaled buffers will be written back to disk without
hitting the journal. Atomicity cannot be guaranteed on an aborted
filesystem, but we _do_ attempt to leave as much data as possible
behind for fsck to use for cleanup.

Any attempt to get a new transaction handle on a journal which is in
ABORT state will just result in an -EROFS error return. A
jbd2_journal_stop on an existing handle will return -EIO if we have
entered abort state during the update.

Recursive transactions are not disturbed by journal abort until the
final jbd2_journal_stop, which will receive the -EIO error.

Finally, the jbd2_journal_abort call allows the caller to supply an
errno which will be recorded (if possible) in the journal superblock.
This allows a client to record failure conditions in the middle of a
transaction without having to complete the transaction to record the
failure to disk. ext3_error, for example, now uses this functionality.

Errors which originate from within the journaling layer will NOT supply
an errno; a null errno implies that absolutely no further writes are
done to the journal (unless there are any already in progress).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
