.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/hfsplus/wrapper.c

.. _`hfsplus_submit_bio`:

hfsplus_submit_bio
==================

.. c:function:: int hfsplus_submit_bio(struct super_block *sb, sector_t sector, void *buf, void **data, int op, int op_flags)

    Perform block I/O

    :param sb:
        super block of volume for I/O
    :type sb: struct super_block \*

    :param sector:
        block to read or write, for blocks of HFSPLUS_SECTOR_SIZE bytes
    :type sector: sector_t

    :param buf:
        buffer for I/O
    :type buf: void \*

    :param data:
        output pointer for location of requested data
    :type data: void \*\*

    :param op:
        direction of I/O
    :type op: int

    :param op_flags:
        request op flags
    :type op_flags: int

.. _`hfsplus_submit_bio.description`:

Description
-----------

The unit of I/O is hfsplus_min_io_size(sb), which may be bigger than
HFSPLUS_SECTOR_SIZE, and \ ``buf``\  must be sized accordingly. On reads
\ ``data``\  will return a pointer to the start of the requested sector,
which may not be the same location as \ ``buf``\ .

If \ ``sector``\  is not aligned to the bdev logical block size it will
be rounded down. For writes this means that \ ``buf``\  should contain data
that starts at the rounded-down address. As long as the data was
read using \ :c:func:`hfsplus_submit_bio`\  and the same buffer is used things
will work correctly.

.. This file was automatic generated / don't edit.

