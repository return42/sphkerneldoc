.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/befs/datastream.c

.. _`befs_read_datastream`:

befs_read_datastream
====================

.. c:function:: struct buffer_head *befs_read_datastream(struct super_block *sb, const befs_data_stream *ds, befs_off_t pos, uint *off)

    get buffer_head containing data, starting from pos.

    :param struct super_block \*sb:
        Filesystem superblock

    :param const befs_data_stream \*ds:
        datastrem to find data with

    :param befs_off_t pos:
        start of data

    :param uint \*off:
        offset of data in buffer_head->b_data

.. _`befs_read_datastream.description`:

Description
-----------

Returns pointer to buffer_head containing data starting with offset \ ``off``\ ,
if you don't need to know offset just set \ ``off``\  = NULL.

.. _`befs_read_lsymlink`:

befs_read_lsymlink
==================

.. c:function:: size_t befs_read_lsymlink(struct super_block *sb, const befs_data_stream *ds, void *buff, befs_off_t len)

    read long symlink from datastream.

    :param struct super_block \*sb:
        Filesystem superblock

    :param const befs_data_stream \*ds:
        Datastrem to read from

    :param void \*buff:
        Buffer in which to place long symlink data

    :param befs_off_t len:
        Length of the long symlink in bytes

.. _`befs_read_lsymlink.description`:

Description
-----------

Returns the number of bytes read

.. _`befs_count_blocks`:

befs_count_blocks
=================

.. c:function:: befs_blocknr_t befs_count_blocks(struct super_block *sb, const befs_data_stream *ds)

    blocks used by a file

    :param struct super_block \*sb:
        Filesystem superblock

    :param const befs_data_stream \*ds:
        Datastream of the file

.. _`befs_count_blocks.description`:

Description
-----------

Counts the number of fs blocks that the file represented by
inode occupies on the filesystem, counting both regular file
data and filesystem metadata (and eventually attribute data
when we support attributes)

.. This file was automatic generated / don't edit.

