
.. _API-jbd2-journal-try-to-free-buffers:

================================
jbd2_journal_try_to_free_buffers
================================

*man jbd2_journal_try_to_free_buffers(9)*

*4.6.0-rc1*

try to free page buffers.


Synopsis
========

.. c:function:: int jbd2_journal_try_to_free_buffers( journal_t * journal, struct page * page, gfp_t gfp_mask )

Arguments
=========

``journal``
    journal for operation

``page``
    to try and free

``gfp_mask``
    we use the mask to detect how hard should we try to release buffers. If __GFP_DIRECT_RECLAIM and __GFP_FS is set, we wait for commit code to release the buffers.


Description
===========

For all the buffers on this page, if they are fully written out ordered data, move them onto BUF_CLEAN so ``try_to_free_buffers`` can reap them.

This function returns non-zero if we wish ``try_to_free_buffers`` to be called. We do this if the page is releasable by ``try_to_free_buffers``. We also do it if the page has
locked or dirty buffers and the caller wants us to perform sync or async writeout.

This complicates JBD locking somewhat. We aren't protected by the BKL here. We wish to remove the buffer from its committing or running transaction's ->t_datalist via
__jbd2_journal_unfile_buffer.

This may ⋆change⋆ the value of transaction_t->t_datalist, so anyone who looks at t_datalist needs to lock against this function.

Even worse, someone may be doing a jbd2_journal_dirty_data on this buffer. So we need to lock against that. ``jbd2_journal_dirty_data`` will come out of the lock with the buffer
dirty, which makes it ineligible for release here.

Who else is affected by this? hmm... Really the only contender is ``do_get_write_access`` - it could be looking at the buffer while ``journal_try_to_free_buffer`` is changing its
state. But that cannot happen because we never reallocate freed data as metadata while the data is part of a transaction. Yes?

Return 0 on failure, 1 on success
