.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/jbd2/journal.c

.. _`jbd2_journal_force_commit_nested`:

jbd2_journal_force_commit_nested
================================

.. c:function:: int jbd2_journal_force_commit_nested(journal_t *journal)

    transaction.  This is used for forcing out undo-protected data which contains bitmaps, when the fs is running out of space.

    :param journal_t \*journal:
        journal to force
        Returns true if progress was made.

.. _`jbd2_journal_force_commit`:

jbd2_journal_force_commit
=========================

.. c:function:: int jbd2_journal_force_commit(journal_t *journal)

    force any uncommitted transactions

    :param journal_t \*journal:
        journal to force

.. _`jbd2_journal_force_commit.description`:

Description
-----------

Caller want unconditional commit. We can only force the running transaction
if we don't have an active handle, otherwise, we will deadlock.

.. _`jbd2_journal_init_dev`:

jbd2_journal_init_dev
=====================

.. c:function:: journal_t *jbd2_journal_init_dev(struct block_device *bdev, struct block_device *fs_dev, unsigned long long start, int len, int blocksize)

    creates and initialises a journal structure

    :param struct block_device \*bdev:
        Block device on which to create the journal

    :param struct block_device \*fs_dev:
        Device which hold journalled filesystem for this journal.

    :param unsigned long long start:
        Block nr Start of journal.

    :param int len:
        Length of the journal in blocks.

    :param int blocksize:
        blocksize of journalling device

.. _`jbd2_journal_init_dev.return`:

Return
------

a newly created journal_t *

 jbd2_journal_init_dev creates a journal which maps a fixed contiguous
 range of blocks on an arbitrary block device.

.. _`jbd2_journal_init_inode`:

jbd2_journal_init_inode
=======================

.. c:function:: journal_t *jbd2_journal_init_inode(struct inode *inode)

    creates a journal which maps to a inode.

    :param struct inode \*inode:
        An inode to create the journal in

.. _`jbd2_journal_init_inode.description`:

Description
-----------

jbd2_journal_init_inode creates a journal which maps an on-disk inode as
the journal.  The inode must exist already, must support \ :c:func:`bmap`\  and
must have all data blocks preallocated.

.. _`jbd2_journal_update_sb_log_tail`:

jbd2_journal_update_sb_log_tail
===============================

.. c:function:: int jbd2_journal_update_sb_log_tail(journal_t *journal, tid_t tail_tid, unsigned long tail_block, int write_op)

    Update log tail in journal sb on disk.

    :param journal_t \*journal:
        The journal to update.

    :param tid_t tail_tid:
        TID of the new transaction at the tail of the log

    :param unsigned long tail_block:
        The first block of the transaction at the tail of the log

    :param int write_op:
        With which operation should we write the journal sb

.. _`jbd2_journal_update_sb_log_tail.description`:

Description
-----------

Update a journal's superblock information about log tail and write it to
disk, waiting for the IO to complete.

.. _`jbd2_mark_journal_empty`:

jbd2_mark_journal_empty
=======================

.. c:function:: void jbd2_mark_journal_empty(journal_t *journal, int write_op)

    Mark on disk journal as empty.

    :param journal_t \*journal:
        The journal to update.

    :param int write_op:
        With which operation should we write the journal sb

.. _`jbd2_mark_journal_empty.description`:

Description
-----------

Update a journal's dynamic superblock fields to show that journal is empty.
Write updated superblock to disk waiting for IO to complete.

.. _`jbd2_journal_update_sb_errno`:

jbd2_journal_update_sb_errno
============================

.. c:function:: void jbd2_journal_update_sb_errno(journal_t *journal)

    Update error in the journal.

    :param journal_t \*journal:
        The journal to update.

.. _`jbd2_journal_update_sb_errno.description`:

Description
-----------

Update a journal's errno.  Write updated superblock to disk waiting for IO
to complete.

.. _`jbd2_journal_load`:

jbd2_journal_load
=================

.. c:function:: int jbd2_journal_load(journal_t *journal)

    Read journal from disk.

    :param journal_t \*journal:
        Journal to act on.

.. _`jbd2_journal_load.description`:

Description
-----------

Given a journal_t structure which tells us which disk blocks contain
a journal, read the journal from disk to initialise the in-memory
structures.

.. _`jbd2_journal_destroy`:

jbd2_journal_destroy
====================

.. c:function:: int jbd2_journal_destroy(journal_t *journal)

    Release a journal_t structure.

    :param journal_t \*journal:
        Journal to act on.

.. _`jbd2_journal_destroy.description`:

Description
-----------

Release a journal_t structure once it is no longer in use by the
journaled object.
Return <0 if we couldn't clean up the journal.

.. _`jbd2_journal_check_used_features`:

jbd2_journal_check_used_features
================================

.. c:function:: int jbd2_journal_check_used_features(journal_t *journal, unsigned long compat, unsigned long ro, unsigned long incompat)

    Check if features specified are used.

    :param journal_t \*journal:
        Journal to check.

    :param unsigned long compat:
        bitmask of compatible features

    :param unsigned long ro:
        bitmask of features that force read-only mount

    :param unsigned long incompat:
        bitmask of incompatible features

.. _`jbd2_journal_check_used_features.description`:

Description
-----------

Check whether the journal uses all of a given set of
features.  Return true (non-zero) if it does.

.. _`jbd2_journal_check_available_features`:

jbd2_journal_check_available_features
=====================================

.. c:function:: int jbd2_journal_check_available_features(journal_t *journal, unsigned long compat, unsigned long ro, unsigned long incompat)

    Check feature set in journalling layer

    :param journal_t \*journal:
        Journal to check.

    :param unsigned long compat:
        bitmask of compatible features

    :param unsigned long ro:
        bitmask of features that force read-only mount

    :param unsigned long incompat:
        bitmask of incompatible features

.. _`jbd2_journal_check_available_features.description`:

Description
-----------

Check whether the journaling code supports the use of
all of a given set of features on this journal.  Return true

.. _`jbd2_journal_set_features`:

jbd2_journal_set_features
=========================

.. c:function:: int jbd2_journal_set_features(journal_t *journal, unsigned long compat, unsigned long ro, unsigned long incompat)

    Mark a given journal feature in the superblock

    :param journal_t \*journal:
        Journal to act on.

    :param unsigned long compat:
        bitmask of compatible features

    :param unsigned long ro:
        bitmask of features that force read-only mount

    :param unsigned long incompat:
        bitmask of incompatible features

.. _`jbd2_journal_set_features.description`:

Description
-----------

Mark a given journal feature as present on the
superblock.  Returns true if the requested features could be set.

.. _`jbd2_journal_flush`:

jbd2_journal_flush
==================

.. c:function:: int jbd2_journal_flush(journal_t *journal)

    Flush journal

    :param journal_t \*journal:
        Journal to act on.

.. _`jbd2_journal_flush.description`:

Description
-----------

Flush all data for a given journal to disk and empty the journal.
Filesystems can use this when remounting readonly to ensure that
recovery does not need to happen on remount.

.. _`jbd2_journal_wipe`:

jbd2_journal_wipe
=================

.. c:function:: int jbd2_journal_wipe(journal_t *journal, int write)

    Wipe journal contents

    :param journal_t \*journal:
        Journal to act on.

    :param int write:
        flag (see below)

.. _`jbd2_journal_wipe.description`:

Description
-----------

Wipe out all of the contents of a journal, safely.  This will produce
a warning if the journal contains any valid recovery information.
Must be called between journal_init_*() and \ :c:func:`jbd2_journal_load`\ .

If 'write' is non-zero, then we wipe out the journal on disk; otherwise
we merely suppress recovery.

.. _`jbd2_journal_abort`:

jbd2_journal_abort
==================

.. c:function:: void jbd2_journal_abort(journal_t *journal, int errno)

    Shutdown the journal immediately.

    :param journal_t \*journal:
        the journal to shutdown.

    :param int errno:
        an error number to record in the journal indicating
        the reason for the shutdown.

.. _`jbd2_journal_abort.description`:

Description
-----------

Perform a complete, immediate shutdown of the ENTIRE
journal (not of a single transaction).  This operation cannot be
undone without closing and reopening the journal.

The jbd2_journal_abort function is intended to support higher level error
recovery mechanisms such as the ext2/ext3 remount-readonly error
mode.

Journal abort has very specific semantics.  Any existing dirty,
unjournaled buffers in the main filesystem will still be written to
disk by bdflush, but the journaling mechanism will be suspended
immediately and no further transaction commits will be honoured.

Any dirty, journaled buffers will be written back to disk without
hitting the journal.  Atomicity cannot be guaranteed on an aborted
filesystem, but we _do_ attempt to leave as much data as possible
behind for fsck to use for cleanup.

Any attempt to get a new transaction handle on a journal which is in
ABORT state will just result in an -EROFS error return.  A
jbd2_journal_stop on an existing handle will return -EIO if we have
entered abort state during the update.

Recursive transactions are not disturbed by journal abort until the
final jbd2_journal_stop, which will receive the -EIO error.

Finally, the jbd2_journal_abort call allows the caller to supply an errno
which will be recorded (if possible) in the journal superblock.  This
allows a client to record failure conditions in the middle of a
transaction without having to complete the transaction to record the
failure to disk.  ext3_error, for example, now uses this
functionality.

Errors which originate from within the journaling layer will NOT
supply an errno; a null errno implies that absolutely no further
writes are done to the journal (unless there are any already in
progress).

.. _`jbd2_journal_errno`:

jbd2_journal_errno
==================

.. c:function:: int jbd2_journal_errno(journal_t *journal)

    returns the journal's error state.

    :param journal_t \*journal:
        journal to examine.

.. _`jbd2_journal_errno.description`:

Description
-----------

This is the errno number set with \ :c:func:`jbd2_journal_abort`\ , the last
time the journal was mounted - if the journal was stopped
without calling abort this will be 0.

If the journal has been aborted on this mount time -EROFS will
be returned.

.. _`jbd2_journal_clear_err`:

jbd2_journal_clear_err
======================

.. c:function:: int jbd2_journal_clear_err(journal_t *journal)

    clears the journal's error state

    :param journal_t \*journal:
        journal to act on.

.. _`jbd2_journal_clear_err.description`:

Description
-----------

An error must be cleared or acked to take a FS out of readonly
mode.

.. _`jbd2_journal_ack_err`:

jbd2_journal_ack_err
====================

.. c:function:: void jbd2_journal_ack_err(journal_t *journal)

    Ack journal err.

    :param journal_t \*journal:
        journal to act on.

.. _`jbd2_journal_ack_err.description`:

Description
-----------

An error must be cleared or acked to take a FS out of readonly
mode.

.. This file was automatic generated / don't edit.

