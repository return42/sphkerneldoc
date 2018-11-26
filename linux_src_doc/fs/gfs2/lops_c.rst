.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/lops.c

.. _`gfs2_pin`:

gfs2_pin
========

.. c:function:: void gfs2_pin(struct gfs2_sbd *sdp, struct buffer_head *bh)

    Pin a buffer in memory

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

    :param bh:
        The buffer to be pinned
    :type bh: struct buffer_head \*

.. _`gfs2_pin.description`:

Description
-----------

The log lock must be held when calling this function

.. _`gfs2_unpin`:

gfs2_unpin
==========

.. c:function:: void gfs2_unpin(struct gfs2_sbd *sdp, struct buffer_head *bh, struct gfs2_trans *tr)

    Unpin a buffer

    :param sdp:
        the filesystem the buffer belongs to
    :type sdp: struct gfs2_sbd \*

    :param bh:
        The buffer to unpin
    :type bh: struct buffer_head \*

    :param tr:
        *undescribed*
    :type tr: struct gfs2_trans \*

.. _`gfs2_end_log_write_bh`:

gfs2_end_log_write_bh
=====================

.. c:function:: void gfs2_end_log_write_bh(struct gfs2_sbd *sdp, struct bio_vec *bvec, blk_status_t error)

    end log write of pagecache data with buffers

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

    :param bvec:
        The bio_vec
    :type bvec: struct bio_vec \*

    :param error:
        The i/o status
    :type error: blk_status_t

.. _`gfs2_end_log_write_bh.description`:

Description
-----------

This finds the relevant buffers and unlocks them and sets the
error flag according to the status of the i/o request. This is
used when the log is writing data which has an in-place version
that is pinned in the pagecache.

.. _`gfs2_end_log_write`:

gfs2_end_log_write
==================

.. c:function:: void gfs2_end_log_write(struct bio *bio)

    end of i/o to the log

    :param bio:
        The bio
    :type bio: struct bio \*

.. _`gfs2_end_log_write.description`:

Description
-----------

Each bio_vec contains either data from the pagecache or data
relating to the log itself. Here we iterate over the bio_vec
array, processing both kinds of data.

.. _`gfs2_log_flush_bio`:

gfs2_log_flush_bio
==================

.. c:function:: void gfs2_log_flush_bio(struct gfs2_sbd *sdp, int op, int op_flags)

    Submit any pending log bio

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

    :param op:
        REQ_OP
    :type op: int

    :param op_flags:
        req_flag_bits
    :type op_flags: int

.. _`gfs2_log_flush_bio.description`:

Description
-----------

Submit any pending part-built or full bio to the block device. If
there is no pending bio, then this is a no-op.

.. _`gfs2_log_alloc_bio`:

gfs2_log_alloc_bio
==================

.. c:function:: struct bio *gfs2_log_alloc_bio(struct gfs2_sbd *sdp, u64 blkno)

    Allocate a new bio for log writing

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

    :param blkno:
        The next device block number we want to write to
    :type blkno: u64

.. _`gfs2_log_alloc_bio.description`:

Description
-----------

This should never be called when there is a cached bio in the
super block. When it returns, there will be a cached bio in the
super block which will have as many bio_vecs as the device is
happy to handle.

.. _`gfs2_log_alloc_bio.return`:

Return
------

Newly allocated bio

.. _`gfs2_log_get_bio`:

gfs2_log_get_bio
================

.. c:function:: struct bio *gfs2_log_get_bio(struct gfs2_sbd *sdp, u64 blkno)

    Get cached log bio, or allocate a new one

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

    :param blkno:
        The device block number we want to write to
    :type blkno: u64

.. _`gfs2_log_get_bio.description`:

Description
-----------

If there is a cached bio, then if the next block number is sequential
with the previous one, return it, otherwise flush the bio to the
device. If there is not a cached bio, or we just flushed it, then
allocate a new one.

.. _`gfs2_log_get_bio.return`:

Return
------

The bio to use for log writes

.. _`gfs2_log_write`:

gfs2_log_write
==============

.. c:function:: void gfs2_log_write(struct gfs2_sbd *sdp, struct page *page, unsigned size, unsigned offset, u64 blkno)

    write to log

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param page:
        the page to write
    :type page: struct page \*

    :param size:
        the size of the data to write
    :type size: unsigned

    :param offset:
        the offset within the page
    :type offset: unsigned

    :param blkno:
        block number of the log entry
    :type blkno: u64

.. _`gfs2_log_write.description`:

Description
-----------

Try and add the page segment to the current bio. If that fails,
submit the current bio to the device and create a new one, and
then add the page segment to that.

.. _`gfs2_log_write_bh`:

gfs2_log_write_bh
=================

.. c:function:: void gfs2_log_write_bh(struct gfs2_sbd *sdp, struct buffer_head *bh)

    write a buffer's content to the log

    :param sdp:
        The super block
    :type sdp: struct gfs2_sbd \*

    :param bh:
        The buffer pointing to the in-place location
    :type bh: struct buffer_head \*

.. _`gfs2_log_write_bh.description`:

Description
-----------

This writes the content of the buffer to the next available location
in the log. The buffer will be unlocked once the i/o to the log has
completed.

.. _`gfs2_log_write_page`:

gfs2_log_write_page
===================

.. c:function:: void gfs2_log_write_page(struct gfs2_sbd *sdp, struct page *page)

    write one block stored in a page, into the log

    :param sdp:
        The superblock
    :type sdp: struct gfs2_sbd \*

    :param page:
        The struct page
    :type page: struct page \*

.. _`gfs2_log_write_page.description`:

Description
-----------

This writes the first block-sized part of the page into the log. Note
that the page must have been allocated from the gfs2_page_pool mempool
and that after this has been called, ownership has been transferred and
the page may be freed at any time.

.. _`gfs2_meta_sync`:

gfs2_meta_sync
==============

.. c:function:: void gfs2_meta_sync(struct gfs2_glock *gl)

    Sync all buffers associated with a glock

    :param gl:
        The glock
    :type gl: struct gfs2_glock \*

.. _`databuf_lo_before_commit`:

databuf_lo_before_commit
========================

.. c:function:: void databuf_lo_before_commit(struct gfs2_sbd *sdp, struct gfs2_trans *tr)

    Scan the data buffers, writing as we go

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param tr:
        *undescribed*
    :type tr: struct gfs2_trans \*

.. This file was automatic generated / don't edit.

