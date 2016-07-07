.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/meta_io.c

.. _`gfs2_getbuf`:

gfs2_getbuf
===========

.. c:function:: struct buffer_head *gfs2_getbuf(struct gfs2_glock *gl, u64 blkno, int create)

    Get a buffer with a given address space

    :param struct gfs2_glock \*gl:
        the glock

    :param u64 blkno:
        the block number (filesystem scope)

    :param int create:
        1 if the buffer should be created

.. _`gfs2_getbuf.return`:

Return
------

the buffer

.. _`gfs2_meta_new`:

gfs2_meta_new
=============

.. c:function:: struct buffer_head *gfs2_meta_new(struct gfs2_glock *gl, u64 blkno)

    Get a block

    :param struct gfs2_glock \*gl:
        The glock associated with this block

    :param u64 blkno:
        The block number

.. _`gfs2_meta_new.return`:

Return
------

The buffer

.. _`gfs2_meta_read`:

gfs2_meta_read
==============

.. c:function:: int gfs2_meta_read(struct gfs2_glock *gl, u64 blkno, int flags, int rahead, struct buffer_head **bhp)

    Read a block from disk

    :param struct gfs2_glock \*gl:
        The glock covering the block

    :param u64 blkno:
        The block number

    :param int flags:
        flags

    :param int rahead:
        *undescribed*

    :param struct buffer_head \*\*bhp:
        the place where the buffer is returned (NULL on failure)

.. _`gfs2_meta_read.return`:

Return
------

errno

.. _`gfs2_meta_wait`:

gfs2_meta_wait
==============

.. c:function:: int gfs2_meta_wait(struct gfs2_sbd *sdp, struct buffer_head *bh)

    Reread a block from disk

    :param struct gfs2_sbd \*sdp:
        the filesystem

    :param struct buffer_head \*bh:
        The block to wait for

.. _`gfs2_meta_wait.return`:

Return
------

errno

.. _`gfs2_meta_wipe`:

gfs2_meta_wipe
==============

.. c:function:: void gfs2_meta_wipe(struct gfs2_inode *ip, u64 bstart, u32 blen)

    make inode's buffers so they aren't dirty/pinned anymore

    :param struct gfs2_inode \*ip:
        the inode who owns the buffers

    :param u64 bstart:
        the first buffer in the run

    :param u32 blen:
        the number of buffers in the run

.. _`gfs2_meta_indirect_buffer`:

gfs2_meta_indirect_buffer
=========================

.. c:function:: int gfs2_meta_indirect_buffer(struct gfs2_inode *ip, int height, u64 num, struct buffer_head **bhp)

    Get a metadata buffer

    :param struct gfs2_inode \*ip:
        The GFS2 inode

    :param int height:
        The level of this buf in the metadata (indir addr) tree (if any)

    :param u64 num:
        The block number (device relative) of the buffer

    :param struct buffer_head \*\*bhp:
        the buffer is returned here

.. _`gfs2_meta_indirect_buffer.return`:

Return
------

errno

.. _`gfs2_meta_ra`:

gfs2_meta_ra
============

.. c:function:: struct buffer_head *gfs2_meta_ra(struct gfs2_glock *gl, u64 dblock, u32 extlen)

    start readahead on an extent of a file

    :param struct gfs2_glock \*gl:
        the glock the blocks belong to

    :param u64 dblock:
        the starting disk block

    :param u32 extlen:
        the number of blocks in the extent

.. _`gfs2_meta_ra.return`:

Return
------

the first buffer in the extent

.. This file was automatic generated / don't edit.

