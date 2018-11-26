.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/log.c

.. _`gfs2_struct2blk`:

gfs2_struct2blk
===============

.. c:function:: unsigned int gfs2_struct2blk(struct gfs2_sbd *sdp, unsigned int nstruct, unsigned int ssize)

    compute stuff

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param nstruct:
        the number of structures
    :type nstruct: unsigned int

    :param ssize:
        the size of the structures
    :type ssize: unsigned int

.. _`gfs2_struct2blk.description`:

Description
-----------

Compute the number of log descriptor blocks needed to hold a certain number
of structures of a certain size.

.. _`gfs2_struct2blk.return`:

Return
------

the number of blocks needed (minimum is always 1)

.. _`gfs2_remove_from_ail`:

gfs2_remove_from_ail
====================

.. c:function:: void gfs2_remove_from_ail(struct gfs2_bufdata *bd)

    Remove an entry from the ail lists, updating counters

    :param bd:
        The gfs2_bufdata to remove
    :type bd: struct gfs2_bufdata \*

.. _`gfs2_remove_from_ail.description`:

Description
-----------

The ail lock \_must\_ be held when calling this function

.. _`gfs2_ail1_start_one`:

gfs2_ail1_start_one
===================

.. c:function:: int gfs2_ail1_start_one(struct gfs2_sbd *sdp, struct writeback_control *wbc, struct gfs2_trans *tr, bool *withdraw)

    Start I/O on a part of the AIL

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param wbc:
        The writeback control structure
    :type wbc: struct writeback_control \*

    :param tr:
        *undescribed*
    :type tr: struct gfs2_trans \*

    :param withdraw:
        *undescribed*
    :type withdraw: bool \*

.. _`gfs2_ail1_flush`:

gfs2_ail1_flush
===============

.. c:function:: void gfs2_ail1_flush(struct gfs2_sbd *sdp, struct writeback_control *wbc)

    start writeback of some ail1 entries

    :param sdp:
        The super block
    :type sdp: struct gfs2_sbd \*

    :param wbc:
        The writeback control structure
    :type wbc: struct writeback_control \*

.. _`gfs2_ail1_flush.description`:

Description
-----------

Writes back some ail1 entries, according to the limits in the
writeback control structure

.. _`gfs2_ail1_start`:

gfs2_ail1_start
===============

.. c:function:: void gfs2_ail1_start(struct gfs2_sbd *sdp)

    start writeback of all ail1 entries

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_ail1_empty_one`:

gfs2_ail1_empty_one
===================

.. c:function:: void gfs2_ail1_empty_one(struct gfs2_sbd *sdp, struct gfs2_trans *tr, bool *withdraw)

    Check whether or not a trans in the AIL has been synced

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param tr:
        *undescribed*
    :type tr: struct gfs2_trans \*

    :param withdraw:
        *undescribed*
    :type withdraw: bool \*

.. _`gfs2_ail1_empty`:

gfs2_ail1_empty
===============

.. c:function:: int gfs2_ail1_empty(struct gfs2_sbd *sdp)

    Try to empty the ail1 lists

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_ail1_empty.description`:

Description
-----------

Tries to empty the ail1 lists, starting with the oldest first

.. _`gfs2_ail2_empty_one`:

gfs2_ail2_empty_one
===================

.. c:function:: void gfs2_ail2_empty_one(struct gfs2_sbd *sdp, struct gfs2_trans *tr)

    Check whether or not a trans in the AIL has been synced

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param tr:
        *undescribed*
    :type tr: struct gfs2_trans \*

.. _`gfs2_log_release`:

gfs2_log_release
================

.. c:function:: void gfs2_log_release(struct gfs2_sbd *sdp, unsigned int blks)

    Release a given number of log blocks

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

    :param blks:
        The number of blocks
    :type blks: unsigned int

.. _`gfs2_log_reserve`:

gfs2_log_reserve
================

.. c:function:: int gfs2_log_reserve(struct gfs2_sbd *sdp, unsigned int blks)

    Make a log reservation

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

    :param blks:
        The number of blocks to reserve
    :type blks: unsigned int

.. _`gfs2_log_reserve.description`:

Description
-----------

Note that we never give out the last few blocks of the journal. Thats
due to the fact that there is a small number of header blocks
associated with each log flush. The exact number can't be known until
flush time, so we ensure that we have just enough free blocks at all
times to avoid running out during a log flush.

We no longer flush the log here, instead we wake up logd to do that
for us. To avoid the thundering herd and to ensure that we deal fairly
with queued waiters, we use an exclusive wait. This means that when we
get woken with enough journal space to get our reservation, we need to
wake the next waiter on the list.

.. _`gfs2_log_reserve.return`:

Return
------

errno

.. _`log_distance`:

log_distance
============

.. c:function:: unsigned int log_distance(struct gfs2_sbd *sdp, unsigned int newer, unsigned int older)

    Compute distance between two journal blocks

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

    :param newer:
        The most recent journal block of the pair
    :type newer: unsigned int

    :param older:
        The older journal block of the pair
    :type older: unsigned int

.. _`log_distance.description`:

Description
-----------

Compute the distance (in the journal direction) between two
blocks in the journal

.. _`log_distance.return`:

Return
------

the distance in blocks

.. _`calc_reserved`:

calc_reserved
=============

.. c:function:: unsigned int calc_reserved(struct gfs2_sbd *sdp)

    Calculate the number of blocks to reserve when refunding a transaction's unused buffers.

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

.. _`calc_reserved.description`:

Description
-----------

This is complex.  We need to reserve room for all our currently used
metadata buffers (e.g. normal file I/O rewriting file time stamps) and
all our journaled data buffers for journaled files (e.g. files in the
meta_fs like rindex, or files for which chattr +j was done.)
If we don't reserve enough space, gfs2_log_refund and gfs2_log_flush
will count it as free space (sd_log_blks_free) and corruption will follow.

We can have metadata bufs and jdata bufs in the same journal.  So each
type gets its own log header, for which we need to reserve a block.
In fact, each type has the potential for needing more than one header
in cases where we have more buffers than will fit on a journal page.
Metadata journal entries take up half the space of journaled buffer entries.
Thus, metadata entries have buf_limit (502) and journaled buffers have
databuf_limit (251) before they cause a wrap around.

Also, we need to reserve blocks for revoke journal entries and one for an
overall header for the lot.

.. _`calc_reserved.return`:

Return
------

the number of blocks reserved

.. _`gfs2_write_log_header`:

gfs2_write_log_header
=====================

.. c:function:: void gfs2_write_log_header(struct gfs2_sbd *sdp, struct gfs2_jdesc *jd, u64 seq, u32 tail, u32 flags, int op_flags)

    Write a journal log header buffer at sd_log_flush_head

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

    :param jd:
        journal descriptor of the journal to which we are writing
    :type jd: struct gfs2_jdesc \*

    :param seq:
        sequence number
    :type seq: u64

    :param tail:
        tail of the log
    :type tail: u32

    :param flags:
        log header flags GFS2_LOG_HEAD\_\*
    :type flags: u32

    :param op_flags:
        flags to pass to the bio
    :type op_flags: int

.. _`gfs2_write_log_header.return`:

Return
------

the initialized log buffer descriptor

.. _`log_write_header`:

log_write_header
================

.. c:function:: void log_write_header(struct gfs2_sbd *sdp, u32 flags)

    Get and initialize a journal header buffer

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

    :param flags:
        The log header flags, including log header origin
    :type flags: u32

.. _`log_write_header.return`:

Return
------

the initialized log buffer descriptor

.. _`gfs2_log_flush`:

gfs2_log_flush
==============

.. c:function:: void gfs2_log_flush(struct gfs2_sbd *sdp, struct gfs2_glock *gl, u32 flags)

    flush incore transaction(s)

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param gl:
        The glock structure to flush.  If NULL, flush the whole incore log
    :type gl: struct gfs2_glock \*

    :param flags:
        The log header flags: GFS2_LOG_HEAD_FLUSH\_\* and debug flags
    :type flags: u32

.. _`gfs2_merge_trans`:

gfs2_merge_trans
================

.. c:function:: void gfs2_merge_trans(struct gfs2_trans *old, struct gfs2_trans *new)

    Merge a new transaction into a cached transaction

    :param old:
        Original transaction to be expanded
    :type old: struct gfs2_trans \*

    :param new:
        New transaction to be merged
    :type new: struct gfs2_trans \*

.. _`gfs2_log_commit`:

gfs2_log_commit
===============

.. c:function:: void gfs2_log_commit(struct gfs2_sbd *sdp, struct gfs2_trans *tr)

    Commit a transaction to the log

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param tr:
        the transaction
    :type tr: struct gfs2_trans \*

.. _`gfs2_log_commit.description`:

Description
-----------

We wake up gfs2_logd if the number of pinned blocks exceed thresh1
or the total number of used blocks (pinned blocks plus AIL blocks)
is greater than thresh2.

At mount time thresh1 is 1/3rd of journal size, thresh2 is 2/3rd of
journal size.

.. _`gfs2_log_commit.return`:

Return
------

errno

.. _`gfs2_log_shutdown`:

gfs2_log_shutdown
=================

.. c:function:: void gfs2_log_shutdown(struct gfs2_sbd *sdp)

    write a shutdown header into a journal

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_logd`:

gfs2_logd
=========

.. c:function:: int gfs2_logd(void *data)

    Update log tail as Active Items get flushed to in-place blocks

    :param data:
        *undescribed*
    :type data: void \*

.. _`gfs2_logd.description`:

Description
-----------

Also, periodically check to make sure that we're using the most recent
journal index.

.. This file was automatic generated / don't edit.

