.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fs-writeback.c

.. _`inode_io_list_move_locked`:

inode_io_list_move_locked
=========================

.. c:function:: bool inode_io_list_move_locked(struct inode *inode, struct bdi_writeback *wb, struct list_head *head)

    move an inode onto a bdi_writeback IO list

    :param struct inode \*inode:
        inode to be moved

    :param struct bdi_writeback \*wb:
        target bdi_writeback

    :param struct list_head \*head:
        one of \ ``wb``\ ->b_{dirty|io|more_io}

.. _`inode_io_list_move_locked.description`:

Description
-----------

Move \ ``inode``\ ->i_io_list to \ ``list``\  of \ ``wb``\  and set \ ``WB_has_dirty_io``\ .
Returns \ ``true``\  if \ ``inode``\  is the first occupant of the !dirty_time IO
lists; otherwise, \ ``false``\ .

.. _`inode_io_list_del_locked`:

inode_io_list_del_locked
========================

.. c:function:: void inode_io_list_del_locked(struct inode *inode, struct bdi_writeback *wb)

    remove an inode from its bdi_writeback IO list

    :param struct inode \*inode:
        inode to be removed

    :param struct bdi_writeback \*wb:
        bdi_writeback \ ``inode``\  is being removed from

.. _`inode_io_list_del_locked.description`:

Description
-----------

Remove \ ``inode``\  which may be on one of \ ``wb``\ ->b_{dirty|io|more_io} lists and
clear \ ``WB_has_dirty_io``\  if all are empty afterwards.

.. _`wb_wait_for_completion`:

wb_wait_for_completion
======================

.. c:function:: void wb_wait_for_completion(struct backing_dev_info *bdi, struct wb_completion *done)

    wait for completion of bdi_writeback_works

    :param struct backing_dev_info \*bdi:
        bdi work items were issued to

    :param struct wb_completion \*done:
        target wb_completion

.. _`wb_wait_for_completion.description`:

Description
-----------

Wait for one or more work items issued to \ ``bdi``\  with their ->done field
set to \ ``done``\ , which should have been defined with
\ :c:func:`DEFINE_WB_COMPLETION_ONSTACK`\ .  This function returns after all such
work items are completed.  Work items which are waited upon aren't freed
automatically on completion.

.. _`locked_inode_to_wb_and_lock_list`:

locked_inode_to_wb_and_lock_list
================================

.. c:function:: struct bdi_writeback *locked_inode_to_wb_and_lock_list(struct inode *inode)

    determine a locked inode's wb and lock it

    :param struct inode \*inode:
        inode of interest with i_lock held

.. _`locked_inode_to_wb_and_lock_list.description`:

Description
-----------

Returns \ ``inode``\ 's wb with its list_lock held.  \ ``inode``\ ->i_lock must be
held on entry and is released on return.  The returned wb is guaranteed
to stay \ ``inode``\ 's associated wb until its list_lock is released.

.. _`inode_to_wb_and_lock_list`:

inode_to_wb_and_lock_list
=========================

.. c:function:: struct bdi_writeback *inode_to_wb_and_lock_list(struct inode *inode)

    determine an inode's wb and lock it

    :param struct inode \*inode:
        inode of interest

.. _`inode_to_wb_and_lock_list.description`:

Description
-----------

Same as \ :c:func:`locked_inode_to_wb_and_lock_list`\  but \ ``inode``\ ->i_lock isn't held
on entry.

.. _`inode_switch_wbs`:

inode_switch_wbs
================

.. c:function:: void inode_switch_wbs(struct inode *inode, int new_wb_id)

    change the wb association of an inode

    :param struct inode \*inode:
        target inode

    :param int new_wb_id:
        ID of the new wb

.. _`inode_switch_wbs.description`:

Description
-----------

Switch \ ``inode``\ 's wb association to the wb identified by \ ``new_wb_id``\ .  The
switching is performed asynchronously and may fail silently.

.. _`wbc_attach_and_unlock_inode`:

wbc_attach_and_unlock_inode
===========================

.. c:function:: void wbc_attach_and_unlock_inode(struct writeback_control *wbc, struct inode *inode)

    associate wbc with target inode and unlock it

    :param struct writeback_control \*wbc:
        writeback_control of interest

    :param struct inode \*inode:
        target inode

.. _`wbc_attach_and_unlock_inode.description`:

Description
-----------

@inode is locked and about to be written back under the control of \ ``wbc``\ .
Record \ ``inode``\ 's writeback context into \ ``wbc``\  and unlock the i_lock.  On
writeback completion, \ :c:func:`wbc_detach_inode`\  should be called.  This is used
to track the cgroup writeback context.

.. _`wbc_detach_inode`:

wbc_detach_inode
================

.. c:function:: void wbc_detach_inode(struct writeback_control *wbc)

    disassociate wbc from inode and perform foreign detection

    :param struct writeback_control \*wbc:
        writeback_control of the just finished writeback

.. _`wbc_detach_inode.description`:

Description
-----------

To be called after a writeback attempt of an inode finishes and undoes
\ :c:func:`wbc_attach_and_unlock_inode`\ .  Can be called under any context.

As concurrent write sharing of an inode is expected to be very rare and
memcg only tracks page ownership on first-use basis severely confining
the usefulness of such sharing, cgroup writeback tracks ownership
per-inode.  While the support for concurrent write sharing of an inode
is deemed unnecessary, an inode being written to by different cgroups at
different points in time is a lot more common, and, more importantly,
charging only by first-use can too readily lead to grossly incorrect
behaviors (single foreign page can lead to gigabytes of writeback to be
incorrectly attributed).

To resolve this issue, cgroup writeback detects the majority dirtier of
an inode and transfers the ownership to it.  To avoid unnnecessary
oscillation, the detection mechanism keeps track of history and gives
out the switch verdict only if the foreign usage pattern is stable over
a certain amount of time and/or writeback attempts.

On each writeback attempt, \ ``wbc``\  tries to detect the majority writer
using Boyer-Moore majority vote algorithm.  In addition to the byte
count from the majority voting, it also counts the bytes written for the
current wb and the last round's winner wb (max of last round's current
wb, the winner from two rounds ago, and the last round's majority
candidate).  Keeping track of the historical winner helps the algorithm
to semi-reliably detect the most active writer even when it's not the
absolute majority.

Once the winner of the round is determined, whether the winner is
foreign or not and how much IO time the round consumed is recorded in
inode->i_wb_frn_history.  If the amount of recorded foreign IO time is
over a certain threshold, the switch verdict is given.

.. _`wbc_account_io`:

wbc_account_io
==============

.. c:function:: void wbc_account_io(struct writeback_control *wbc, struct page *page, size_t bytes)

    account IO issued during writeback

    :param struct writeback_control \*wbc:
        writeback_control of the writeback in progress

    :param struct page \*page:
        page being written out

    :param size_t bytes:
        number of bytes being written out

.. _`wbc_account_io.description`:

Description
-----------

@bytes from \ ``page``\  are about to written out during the writeback
controlled by \ ``wbc``\ .  Keep the book for foreign inode detection.  See
\ :c:func:`wbc_detach_inode`\ .

.. _`inode_congested`:

inode_congested
===============

.. c:function:: int inode_congested(struct inode *inode, int cong_bits)

    test whether an inode is congested

    :param struct inode \*inode:
        inode to test for congestion (may be NULL)

    :param int cong_bits:
        mask of WB_[a]sync_congested bits to test

.. _`inode_congested.description`:

Description
-----------

Tests whether \ ``inode``\  is congested.  \ ``cong_bits``\  is the mask of congestion
bits to test and the return value is the mask of set bits.

If cgroup writeback is enabled for \ ``inode``\ , the congestion state is
determined by whether the cgwb (cgroup bdi_writeback) for the blkcg
associated with \ ``inode``\  is congested; otherwise, the root wb's congestion
state is used.

\ ``inode``\  is allowed to be NULL as this function is often called on
mapping->host which is NULL for the swapper space.

.. _`wb_split_bdi_pages`:

wb_split_bdi_pages
==================

.. c:function:: long wb_split_bdi_pages(struct bdi_writeback *wb, long nr_pages)

    split nr_pages to write according to bandwidth

    :param struct bdi_writeback \*wb:
        target bdi_writeback to split \ ``nr_pages``\  to

    :param long nr_pages:
        number of pages to write for the whole bdi

.. _`wb_split_bdi_pages.description`:

Description
-----------

Split \ ``wb``\ 's portion of \ ``nr_pages``\  according to \ ``wb``\ 's write bandwidth in
relation to the total write bandwidth of all wb's w/ dirty inodes on
\ ``wb``\ ->bdi.

.. _`bdi_split_work_to_wbs`:

bdi_split_work_to_wbs
=====================

.. c:function:: void bdi_split_work_to_wbs(struct backing_dev_info *bdi, struct wb_writeback_work *base_work, bool skip_if_busy)

    split a wb_writeback_work to all wb's of a bdi

    :param struct backing_dev_info \*bdi:
        target backing_dev_info

    :param struct wb_writeback_work \*base_work:
        wb_writeback_work to issue

    :param bool skip_if_busy:
        skip wb's which already have writeback in progress

.. _`bdi_split_work_to_wbs.description`:

Description
-----------

Split and issue \ ``base_work``\  to all wb's (bdi_writeback's) of \ ``bdi``\  which
have dirty inodes.  If \ ``base_work``\ ->nr_page isn't \ ``LONG_MAX``\ , it's
distributed to the busy wbs according to each wb's proportion in the
total active write bandwidth of \ ``bdi``\ .

.. _`cgroup_writeback_umount`:

cgroup_writeback_umount
=======================

.. c:function:: void cgroup_writeback_umount( void)

    flush inode wb switches for umount

    :param  void:
        no arguments

.. _`cgroup_writeback_umount.description`:

Description
-----------

This function is called when a super_block is about to be destroyed and
flushes in-flight inode wb switches.  An inode wb switch goes through
RCU and then workqueue, so the two need to be flushed in order to ensure
that all previously scheduled switches are finished.  As wb switches are
rare occurrences and \ :c:func:`synchronize_rcu`\  can take a while, perform
flushing iff wb switches are in flight.

.. _`wb_start_background_writeback`:

wb_start_background_writeback
=============================

.. c:function:: void wb_start_background_writeback(struct bdi_writeback *wb)

    start background writeback

    :param struct bdi_writeback \*wb:
        bdi_writback to write from

.. _`wb_start_background_writeback.description`:

Description
-----------

  This makes sure WB_SYNC_NONE background writeback happens. When
  this function returns, it is only guaranteed that for given wb
  some IO is happening if we are over background dirty threshold.
  Caller need not hold sb s_umount semaphore.

.. _`__mark_inode_dirty`:

__mark_inode_dirty
==================

.. c:function:: void __mark_inode_dirty(struct inode *inode, int flags)

    internal function

    :param struct inode \*inode:
        inode to mark

    :param int flags:
        what kind of dirty (i.e. I_DIRTY_SYNC)

.. _`__mark_inode_dirty.description`:

Description
-----------

Mark an inode as dirty. Callers should use mark_inode_dirty or
mark_inode_dirty_sync.

Put the inode on the super block's dirty list.

CAREFUL! We mark it dirty unconditionally, but move it onto the
dirty list only if it is hashed or if it refers to a blockdev.
If it was not hashed, it will never be added to the dirty list
even if it is later hashed, as it will have been marked dirty already.

In short, make sure you hash any inodes _before_ you start marking
them dirty.

Note that for blockdevs, inode->dirtied_when represents the dirtying time of
the block-special inode (/dev/hda1) itself.  And the ->dirtied_when field of
the kernel-internal blockdev inode represents the dirtying time of the
blockdev's pages.  This is why for I_DIRTY_PAGES we always use
page->mapping->host, so the page-dirtying time is recorded in the internal
blockdev inode.

.. _`writeback_inodes_sb_nr`:

writeback_inodes_sb_nr
======================

.. c:function:: void writeback_inodes_sb_nr(struct super_block *sb, unsigned long nr, enum wb_reason reason)

    writeback dirty inodes from given super_block

    :param struct super_block \*sb:
        the superblock

    :param unsigned long nr:
        the number of pages to write

    :param enum wb_reason reason:
        reason why some writeback work initiated

.. _`writeback_inodes_sb_nr.description`:

Description
-----------

Start writeback on some inodes on this super_block. No guarantees are made
on how many (if any) will be written, and this function does not wait
for IO completion of submitted IO.

.. _`writeback_inodes_sb`:

writeback_inodes_sb
===================

.. c:function:: void writeback_inodes_sb(struct super_block *sb, enum wb_reason reason)

    writeback dirty inodes from given super_block

    :param struct super_block \*sb:
        the superblock

    :param enum wb_reason reason:
        reason why some writeback work was initiated

.. _`writeback_inodes_sb.description`:

Description
-----------

Start writeback on some inodes on this super_block. No guarantees are made
on how many (if any) will be written, and this function does not wait
for IO completion of submitted IO.

.. _`try_to_writeback_inodes_sb`:

try_to_writeback_inodes_sb
==========================

.. c:function:: void try_to_writeback_inodes_sb(struct super_block *sb, enum wb_reason reason)

    try to start writeback if none underway

    :param struct super_block \*sb:
        the superblock

    :param enum wb_reason reason:
        reason why some writeback work was initiated

.. _`try_to_writeback_inodes_sb.description`:

Description
-----------

Invoke __writeback_inodes_sb_nr if no writeback is currently underway.

.. _`sync_inodes_sb`:

sync_inodes_sb
==============

.. c:function:: void sync_inodes_sb(struct super_block *sb)

    sync sb inode pages

    :param struct super_block \*sb:
        the superblock

.. _`sync_inodes_sb.description`:

Description
-----------

This function writes and waits on any dirty inode belonging to this
super_block.

.. _`write_inode_now`:

write_inode_now
===============

.. c:function:: int write_inode_now(struct inode *inode, int sync)

    write an inode to disk

    :param struct inode \*inode:
        inode to write to disk

    :param int sync:
        whether the write should be synchronous or not

.. _`write_inode_now.description`:

Description
-----------

This function commits an inode to disk immediately if it is dirty. This is
primarily needed by knfsd.

The caller must either have a ref on the inode or must have set I_WILL_FREE.

.. _`sync_inode`:

sync_inode
==========

.. c:function:: int sync_inode(struct inode *inode, struct writeback_control *wbc)

    write an inode and its pages to disk.

    :param struct inode \*inode:
        the inode to sync

    :param struct writeback_control \*wbc:
        controls the writeback mode

.. _`sync_inode.description`:

Description
-----------

sync_inode() will write an inode and its pages to disk.  It will also
correctly update the inode on its superblock's dirty inode lists and will
update inode->i_state.

The caller must have a ref on the inode.

.. _`sync_inode_metadata`:

sync_inode_metadata
===================

.. c:function:: int sync_inode_metadata(struct inode *inode, int wait)

    write an inode to disk

    :param struct inode \*inode:
        the inode to sync

    :param int wait:
        wait for I/O to complete.

.. _`sync_inode_metadata.description`:

Description
-----------

Write an inode to disk and adjust its dirty state after completion.

.. _`sync_inode_metadata.note`:

Note
----

only writes the actual inode, no associated data or other metadata.

.. This file was automatic generated / don't edit.

