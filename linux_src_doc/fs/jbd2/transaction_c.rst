.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/jbd2/transaction.c

.. _`jbd2_journal_start`:

jbd2_journal_start
==================

.. c:function:: handle_t *jbd2_journal_start(journal_t *journal, int nblocks)

    Obtain a new handle.

    :param journal_t \*journal:
        Journal to start transaction on.

    :param int nblocks:
        number of block buffer we might modify

.. _`jbd2_journal_start.description`:

Description
-----------

We make sure that the transaction can guarantee at least nblocks of
modified buffers in the log.  We block until the log can guarantee
that much space. Additionally, if rsv_blocks > 0, we also create another
handle with rsv_blocks reserved blocks in the journal. This handle is
is stored in h_rsv_handle. It is not attached to any particular transaction
and thus doesn't block transaction commit. If the caller uses this reserved
handle, it has to set h_rsv_handle to NULL as otherwise \ :c:func:`jbd2_journal_stop`\ 
on the parent handle will dispose the reserved one. Reserved handle has to
be converted to a normal handle using \ :c:func:`jbd2_journal_start_reserved`\  before
it can be used.

Return a pointer to a newly allocated handle, or an \ :c:func:`ERR_PTR`\  value
on failure.

.. _`jbd2_journal_start_reserved`:

jbd2_journal_start_reserved
===========================

.. c:function:: int jbd2_journal_start_reserved(handle_t *handle, unsigned int type, unsigned int line_no)

    start reserved handle

    :param handle_t \*handle:
        handle to start

    :param unsigned int type:
        for handle statistics

    :param unsigned int line_no:
        for handle statistics

.. _`jbd2_journal_start_reserved.description`:

Description
-----------

Start handle that has been previously reserved with \ :c:func:`jbd2_journal_reserve`\ .
This attaches \ ``handle``\  to the running transaction (or creates one if there's
not transaction running). Unlike \ :c:func:`jbd2_journal_start`\  this function cannot
block on journal commit, checkpointing, or similar stuff. It can block on
memory allocation or frozen journal though.

Return 0 on success, non-zero on error - handle is freed in that case.

.. _`jbd2_journal_extend`:

jbd2_journal_extend
===================

.. c:function:: int jbd2_journal_extend(handle_t *handle, int nblocks)

    extend buffer credits.

    :param handle_t \*handle:
        handle to 'extend'

    :param int nblocks:
        nr blocks to try to extend by.

.. _`jbd2_journal_extend.description`:

Description
-----------

Some transactions, such as large extends and truncates, can be done
atomically all at once or in several stages.  The operation requests
a credit for a number of buffer modifications in advance, but can
extend its credit if it needs more.

jbd2_journal_extend tries to give the running handle more buffer credits.
It does not guarantee that allocation - this is a best-effort only.
The calling process MUST be able to deal cleanly with a failure to
extend here.

Return 0 on success, non-zero on failure.

return code < 0 implies an error
return code > 0 implies normal transaction-full status.

.. _`jbd2__journal_restart`:

jbd2__journal_restart
=====================

.. c:function:: int jbd2__journal_restart(handle_t *handle, int nblocks, gfp_t gfp_mask)

    restart a handle .

    :param handle_t \*handle:
        handle to restart

    :param int nblocks:
        nr credits requested

    :param gfp_t gfp_mask:
        memory allocation flags (for start_this_handle)

.. _`jbd2__journal_restart.description`:

Description
-----------

Restart a handle for a multi-transaction filesystem
operation.

If the \ :c:func:`jbd2_journal_extend`\  call above fails to grant new buffer credits
to a running handle, a call to jbd2_journal_restart will commit the
handle's transaction so far and reattach the handle to a new
transaction capable of guaranteeing the requested number of
credits. We preserve reserved handle if there's any attached to the
passed in handle.

.. _`jbd2_journal_lock_updates`:

jbd2_journal_lock_updates
=========================

.. c:function:: void jbd2_journal_lock_updates(journal_t *journal)

    establish a transaction barrier.

    :param journal_t \*journal:
        Journal to establish a barrier on.

.. _`jbd2_journal_lock_updates.description`:

Description
-----------

This locks out any further updates from being started, and blocks
until all existing updates have completed, returning only once the
journal is in a quiescent state with no updates running.

The journal lock should not be held on entry.

.. _`jbd2_journal_unlock_updates`:

jbd2_journal_unlock_updates
===========================

.. c:function:: void jbd2_journal_unlock_updates(journal_t *journal)

    release barrier

    :param journal_t \*journal:
        Journal to release the barrier on.

.. _`jbd2_journal_unlock_updates.description`:

Description
-----------

Release a transaction barrier obtained with \ :c:func:`jbd2_journal_lock_updates`\ .

Should be called without the journal lock held.

.. _`jbd2_journal_get_write_access`:

jbd2_journal_get_write_access
=============================

.. c:function:: int jbd2_journal_get_write_access(handle_t *handle, struct buffer_head *bh)

    notify intent to modify a buffer for metadata (not data) update.

    :param handle_t \*handle:
        transaction to add buffer modifications to

    :param struct buffer_head \*bh:
        bh to be used for metadata writes

.. _`jbd2_journal_get_write_access.return`:

Return
------

error code or 0 on success.

In full data journalling mode the buffer may be of type BJ_AsyncData,
because we're ``write()ing`` a buffer which is also part of a shared mapping.

.. _`jbd2_journal_get_create_access`:

jbd2_journal_get_create_access
==============================

.. c:function:: int jbd2_journal_get_create_access(handle_t *handle, struct buffer_head *bh)

    notify intent to use newly created bh

    :param handle_t \*handle:
        transaction to new buffer to

    :param struct buffer_head \*bh:
        new buffer.

.. _`jbd2_journal_get_create_access.description`:

Description
-----------

Call this if you create a new bh.

.. _`jbd2_journal_get_undo_access`:

jbd2_journal_get_undo_access
============================

.. c:function:: int jbd2_journal_get_undo_access(handle_t *handle, struct buffer_head *bh)

    Notify intent to modify metadata with non-rewindable consequences

    :param handle_t \*handle:
        transaction

    :param struct buffer_head \*bh:
        buffer to undo

.. _`jbd2_journal_get_undo_access.description`:

Description
-----------

Sometimes there is a need to distinguish between metadata which has
been committed to disk and that which has not.  The ext3fs code uses
this for freeing and allocating space, we have to make sure that we
do not reuse freed space until the deallocation has been committed,
since if we overwrote that space we would make the delete
un-rewindable in case of a crash.

To deal with that, jbd2_journal_get_undo_access requests write access to a
buffer for parts of non-rewindable operations such as delete
operations on the bitmaps.  The journaling code must keep a copy of
the buffer's contents prior to the undo_access call until such time
as we know that the buffer has definitely been committed to disk.

We never need to know which transaction the committed data is part
of, buffers touched here are guaranteed to be dirtied later and so
will be committed to a new transaction in due course, at which point
we can discard the old committed data pointer.

Returns error number or 0 on success.

.. _`jbd2_journal_set_triggers`:

jbd2_journal_set_triggers
=========================

.. c:function:: void jbd2_journal_set_triggers(struct buffer_head *bh, struct jbd2_buffer_trigger_type *type)

    Add triggers for commit writeout

    :param struct buffer_head \*bh:
        buffer to trigger on

    :param struct jbd2_buffer_trigger_type \*type:
        struct jbd2_buffer_trigger_type containing the trigger(s).

.. _`jbd2_journal_set_triggers.description`:

Description
-----------

Set any triggers on this journal_head.  This is always safe, because
triggers for a committing buffer will be saved off, and triggers for
a running transaction will match the buffer in that transaction.

Call with NULL to clear the triggers.

.. _`jbd2_journal_dirty_metadata`:

jbd2_journal_dirty_metadata
===========================

.. c:function:: int jbd2_journal_dirty_metadata(handle_t *handle, struct buffer_head *bh)

    mark a buffer as containing dirty metadata

    :param handle_t \*handle:
        transaction to add buffer to.

    :param struct buffer_head \*bh:
        buffer to mark

.. _`jbd2_journal_dirty_metadata.description`:

Description
-----------

mark dirty metadata which needs to be journaled as part of the current
transaction.

The buffer must have previously had \ :c:func:`jbd2_journal_get_write_access`\ 
called so that it has a valid journal_head attached to the buffer
head.

The buffer is placed on the transaction's metadata list and is marked
as belonging to the transaction.

Returns error number or 0 on success.

Special care needs to be taken if the buffer already belongs to the
current committing transaction (in which case we should have frozen
data present for that commit).  In that case, we don't relink the
buffer: that only gets done when the old transaction finally
completes its commit.

.. _`jbd2_journal_forget`:

jbd2_journal_forget
===================

.. c:function:: int jbd2_journal_forget(handle_t *handle, struct buffer_head *bh)

    \ :c:func:`bforget`\  for potentially-journaled buffers.

    :param handle_t \*handle:
        transaction handle

    :param struct buffer_head \*bh:
        bh to 'forget'

.. _`jbd2_journal_forget.description`:

Description
-----------

We can only do the bforget if there are no commits pending against the
buffer.  If the buffer is dirty in the current running transaction we
can safely unlink it.

bh may not be a journalled buffer at all - it may be a non-JBD
buffer which came off the hashtable.  Check for this.

Decrements bh->b_count by one.

Allow this call even if the handle has aborted --- it may be part of
the caller's cleanup after an abort.

.. _`jbd2_journal_stop`:

jbd2_journal_stop
=================

.. c:function:: int jbd2_journal_stop(handle_t *handle)

    complete a transaction

    :param handle_t \*handle:
        transaction to complete.

.. _`jbd2_journal_stop.description`:

Description
-----------

All done for a particular handle.

There is not much action needed here.  We just return any remaining
buffer credits to the transaction and remove the handle.  The only
complication is that we need to start a commit operation if the
filesystem is marked for synchronous update.

jbd2_journal_stop itself will not usually return an error, but it may
do so in unusual circumstances.  In particular, expect it to
return -EIO if a jbd2_journal_abort has been executed since the
transaction began.

.. _`jbd2_journal_try_to_free_buffers`:

jbd2_journal_try_to_free_buffers
================================

.. c:function:: int jbd2_journal_try_to_free_buffers(journal_t *journal, struct page *page, gfp_t gfp_mask)

    try to free page buffers.

    :param journal_t \*journal:
        journal for operation

    :param struct page \*page:
        to try and free

    :param gfp_t gfp_mask:
        we use the mask to detect how hard should we try to release
        buffers. If __GFP_DIRECT_RECLAIM and __GFP_FS is set, we wait for commit
        code to release the buffers.

.. _`jbd2_journal_try_to_free_buffers.description`:

Description
-----------


For all the buffers on this page,
if they are fully written out ordered data, move them onto BUF_CLEAN
so \ :c:func:`try_to_free_buffers`\  can reap them.

This function returns non-zero if we wish \ :c:func:`try_to_free_buffers`\ 
to be called. We do this if the page is releasable by \ :c:func:`try_to_free_buffers`\ .
We also do it if the page has locked or dirty buffers and the caller wants
us to perform sync or async writeout.

This complicates JBD locking somewhat.  We aren't protected by the
BKL here.  We wish to remove the buffer from its committing or
running transaction's ->t_datalist via __jbd2_journal_unfile_buffer.

This may *change* the value of transaction_t->t_datalist, so anyone
who looks at t_datalist needs to lock against this function.

Even worse, someone may be doing a jbd2_journal_dirty_data on this
buffer.  So we need to lock against that.  \ :c:func:`jbd2_journal_dirty_data`\ 
will come out of the lock with the buffer dirty, which makes it
ineligible for release here.

Who else is affected by this?  hmm...  Really the only contender
is \ :c:func:`do_get_write_access`\  - it could be looking at the buffer while
\ :c:func:`journal_try_to_free_buffer`\  is changing its state.  But that
cannot happen because we never reallocate freed data as metadata
while the data is part of a transaction.  Yes?

Return 0 on failure, 1 on success

.. _`jbd2_journal_invalidatepage`:

jbd2_journal_invalidatepage
===========================

.. c:function:: int jbd2_journal_invalidatepage(journal_t *journal, struct page *page, unsigned int offset, unsigned int length)

    :param journal_t \*journal:
        journal to use for flush...

    :param struct page \*page:
        page to flush

    :param unsigned int offset:
        start of the range to invalidate

    :param unsigned int length:
        length of the range to invalidate

.. _`jbd2_journal_invalidatepage.description`:

Description
-----------

Reap page buffers containing data after in the specified range in page.
Can return -EBUSY if buffers are part of the committing transaction and
the page is straddling i_size. Caller then has to wait for current commit
and try again.

.. This file was automatic generated / don't edit.

