.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/befs/datastream.c

.. _`befs_read_datastream`:

befs_read_datastream
====================

.. c:function:: struct buffer_head *befs_read_datastream(struct super_block *sb, const befs_data_stream *ds, befs_off_t pos, uint *off)

    get buffer_head containing data, starting from pos.

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        datastream to find data with
    :type ds: const befs_data_stream \*

    :param pos:
        start of data
    :type pos: befs_off_t

    :param off:
        offset of data in buffer_head->b_data
    :type off: uint \*

.. _`befs_read_datastream.description`:

Description
-----------

Returns pointer to buffer_head containing data starting with offset \ ``off``\ ,
if you don't need to know offset just set \ ``off``\  = NULL.

.. _`befs_fblock2brun`:

befs_fblock2brun
================

.. c:function:: int befs_fblock2brun(struct super_block *sb, const befs_data_stream *data, befs_blocknr_t fblock, befs_block_run *run)

    give back block run for fblock

    :param sb:
        the superblock
    :type sb: struct super_block \*

    :param data:
        datastream to read from
    :type data: const befs_data_stream \*

    :param fblock:
        the blocknumber with the file position to find
    :type fblock: befs_blocknr_t

    :param run:
        The found run is passed back through this pointer
    :type run: befs_block_run \*

.. _`befs_fblock2brun.description`:

Description
-----------

Takes a file position and gives back a brun who's starting block
is block number fblock of the file.

Returns BEFS_OK or BEFS_ERR.

Calls specialized functions for each of the three possible
datastream regions.

.. _`befs_read_lsymlink`:

befs_read_lsymlink
==================

.. c:function:: size_t befs_read_lsymlink(struct super_block *sb, const befs_data_stream *ds, void *buff, befs_off_t len)

    read long symlink from datastream.

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream to read from
    :type ds: const befs_data_stream \*

    :param buff:
        Buffer in which to place long symlink data
    :type buff: void \*

    :param len:
        Length of the long symlink in bytes
    :type len: befs_off_t

.. _`befs_read_lsymlink.description`:

Description
-----------

Returns the number of bytes read

.. _`befs_count_blocks`:

befs_count_blocks
=================

.. c:function:: befs_blocknr_t befs_count_blocks(struct super_block *sb, const befs_data_stream *ds)

    blocks used by a file

    :param sb:
        Filesystem superblock
    :type sb: struct super_block \*

    :param ds:
        Datastream of the file
    :type ds: const befs_data_stream \*

.. _`befs_count_blocks.description`:

Description
-----------

Counts the number of fs blocks that the file represented by
inode occupies on the filesystem, counting both regular file
data and filesystem metadata (and eventually attribute data
when we support attributes)

.. _`befs_find_brun_direct`:

befs_find_brun_direct
=====================

.. c:function:: int befs_find_brun_direct(struct super_block *sb, const befs_data_stream *data, befs_blocknr_t blockno, befs_block_run *run)

    find a direct block run in the datastream

    :param sb:
        the superblock
    :type sb: struct super_block \*

    :param data:
        the datastream
    :type data: const befs_data_stream \*

    :param blockno:
        the blocknumber to find
    :type blockno: befs_blocknr_t

    :param run:
        The found run is passed back through this pointer
    :type run: befs_block_run \*

.. _`befs_find_brun_direct.description`:

Description
-----------

Finds the block run that starts at file block number blockno
in the file represented by the datastream data, if that
blockno is in the direct region of the datastream.

Return value is BEFS_OK if the blockrun is found, BEFS_ERR
otherwise.

.. _`befs_find_brun_direct.algorithm`:

Algorithm
---------

Linear search. Checks each element of array[] to see if it
contains the blockno-th filesystem block. This is necessary
because the block runs map variable amounts of data. Simply
keeps a count of the number of blocks searched so far (sum),
incrementing this by the length of each block run as we come
across it. Adds sum to \*count before returning (this is so
you can search multiple arrays that are logicaly one array,
as in the indirect region code).

When/if blockno is found, if blockno is inside of a block
run as stored on disk, we offset the start and length members
of the block run, so that blockno is the start and len is
still valid (the run ends in the same place).

.. _`befs_find_brun_indirect`:

befs_find_brun_indirect
=======================

.. c:function:: int befs_find_brun_indirect(struct super_block *sb, const befs_data_stream *data, befs_blocknr_t blockno, befs_block_run *run)

    find a block run in the datastream

    :param sb:
        the superblock
    :type sb: struct super_block \*

    :param data:
        the datastream
    :type data: const befs_data_stream \*

    :param blockno:
        the blocknumber to find
    :type blockno: befs_blocknr_t

    :param run:
        The found run is passed back through this pointer
    :type run: befs_block_run \*

.. _`befs_find_brun_indirect.description`:

Description
-----------

Finds the block run that starts at file block number blockno
in the file represented by the datastream data, if that
blockno is in the indirect region of the datastream.

Return value is BEFS_OK if the blockrun is found, BEFS_ERR
otherwise.

.. _`befs_find_brun_indirect.algorithm`:

Algorithm
---------

For each block in the indirect run of the datastream, read
it in and search through it for search_blk.

.. _`befs_find_brun_indirect.xxx`:

XXX
---

Really should check to make sure blockno is inside indirect
region.

.. _`befs_find_brun_dblindirect`:

befs_find_brun_dblindirect
==========================

.. c:function:: int befs_find_brun_dblindirect(struct super_block *sb, const befs_data_stream *data, befs_blocknr_t blockno, befs_block_run *run)

    find a block run in the datastream

    :param sb:
        the superblock
    :type sb: struct super_block \*

    :param data:
        the datastream
    :type data: const befs_data_stream \*

    :param blockno:
        the blocknumber to find
    :type blockno: befs_blocknr_t

    :param run:
        The found run is passed back through this pointer
    :type run: befs_block_run \*

.. _`befs_find_brun_dblindirect.description`:

Description
-----------

Finds the block run that starts at file block number blockno
in the file represented by the datastream data, if that
blockno is in the double-indirect region of the datastream.

Return value is BEFS_OK if the blockrun is found, BEFS_ERR
otherwise.

.. _`befs_find_brun_dblindirect.algorithm`:

Algorithm
---------

The block runs in the double-indirect region are different.
They are always allocated 4 fs blocks at a time, so each
block run maps a constant amount of file data. This means
that we can directly calculate how many block runs into the
double-indirect region we need to go to get to the one that
maps a particular filesystem block.

We do this in two stages. First we calculate which of the
inode addresses in the double-indirect block will point us
to the indirect block that contains the mapping for the data,
then we calculate which of the inode addresses in that
indirect block maps the data block we are after.

Oh, and once we've done that, we actually read in the blocks
that contain the inode addresses we calculated above. Even
though the double-indirect run may be several blocks long,
we can calculate which of those blocks will contain the index
we are after and only read that one. We then follow it to
the indirect block and perform a similar process to find
the actual block run that maps the data block we are interested
in.

Then we offset the run as in \ :c:func:`befs_find_brun_array`\  and we are
done.

.. This file was automatic generated / don't edit.

