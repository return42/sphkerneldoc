.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/meta_io.c

.. _`gfs2_getbuf`:

gfs2_getbuf
===========

.. c:function:: struct buffer_head *gfs2_getbuf(struct gfs2_glock *gl, u64 blkno, int create)

    Get a buffer with a given address space

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

    :param blkno:
        the block number (filesystem scope)
    :type blkno: u64

    :param create:
        1 if the buffer should be created
    :type create: int

.. _`gfs2_getbuf.return`:

Return
------

the buffer

.. _`gfs2_meta_new`:

gfs2_meta_new
=============

.. c:function:: struct buffer_head *gfs2_meta_new(struct gfs2_glock *gl, u64 blkno)

    Get a block

    :param gl:
        The glock associated with this block
    :type gl: struct gfs2_glock \*

    :param blkno:
        The block number
    :type blkno: u64

.. _`gfs2_meta_new.return`:

Return
------

The buffer

.. _`gfs2_meta_read`:

gfs2_meta_read
==============

.. c:function:: int gfs2_meta_read(struct gfs2_glock *gl, u64 blkno, int flags, int rahead, struct buffer_head **bhp)

    Read a block from disk

    :param gl:
        The glock covering the block
    :type gl: struct gfs2_glock \*

    :param blkno:
        The block number
    :type blkno: u64

    :param flags:
        flags
    :type flags: int

    :param rahead:
        *undescribed*
    :type rahead: int

    :param bhp:
        the place where the buffer is returned (NULL on failure)
    :type bhp: struct buffer_head \*\*

.. _`gfs2_meta_read.return`:

Return
------

errno

.. _`gfs2_meta_wait`:

gfs2_meta_wait
==============

.. c:function:: int gfs2_meta_wait(struct gfs2_sbd *sdp, struct buffer_head *bh)

    Reread a block from disk

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param bh:
        The block to wait for
    :type bh: struct buffer_head \*

.. _`gfs2_meta_wait.return`:

Return
------

errno

.. _`gfs2_meta_wipe`:

gfs2_meta_wipe
==============

.. c:function:: void gfs2_meta_wipe(struct gfs2_inode *ip, u64 bstart, u32 blen)

    make inode's buffers so they aren't dirty/pinned anymore

    :param ip:
        the inode who owns the buffers
    :type ip: struct gfs2_inode \*

    :param bstart:
        the first buffer in the run
    :type bstart: u64

    :param blen:
        the number of buffers in the run
    :type blen: u32

.. _`gfs2_meta_indirect_buffer`:

gfs2_meta_indirect_buffer
=========================

.. c:function:: int gfs2_meta_indirect_buffer(struct gfs2_inode *ip, int height, u64 num, struct buffer_head **bhp)

    Get a metadata buffer

    :param ip:
        The GFS2 inode
    :type ip: struct gfs2_inode \*

    :param height:
        The level of this buf in the metadata (indir addr) tree (if any)
    :type height: int

    :param num:
        The block number (device relative) of the buffer
    :type num: u64

    :param bhp:
        the buffer is returned here
    :type bhp: struct buffer_head \*\*

.. _`gfs2_meta_indirect_buffer.return`:

Return
------

errno

.. _`gfs2_meta_ra`:

gfs2_meta_ra
============

.. c:function:: struct buffer_head *gfs2_meta_ra(struct gfs2_glock *gl, u64 dblock, u32 extlen)

    start readahead on an extent of a file

    :param gl:
        the glock the blocks belong to
    :type gl: struct gfs2_glock \*

    :param dblock:
        the starting disk block
    :type dblock: u64

    :param extlen:
        the number of blocks in the extent
    :type extlen: u32

.. _`gfs2_meta_ra.return`:

Return
------

the first buffer in the extent

.. This file was automatic generated / don't edit.

