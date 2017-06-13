.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/util.c

.. _`spu_sg_at_offset`:

spu_sg_at_offset
================

.. c:function:: int spu_sg_at_offset(struct scatterlist *sg, unsigned int skip, struct scatterlist **sge, unsigned int *sge_offset)

    Find the scatterlist entry at a given distance from the start of a scatterlist.

    :param struct scatterlist \*sg:
        [in]  Start of a scatterlist

    :param unsigned int skip:
        [in]  Distance from the start of the scatterlist, in bytes

    :param struct scatterlist \*\*sge:
        [out] Scatterlist entry at skip bytes from start

    :param unsigned int \*sge_offset:
        [out] Number of bytes from start of sge buffer to get to
        requested distance.

.. _`spu_sg_at_offset.return`:

Return
------

0 if entry found at requested distance
< 0 otherwise

.. _`spu_sg_count`:

spu_sg_count
============

.. c:function:: int spu_sg_count(struct scatterlist *sg_list, unsigned int skip, int nbytes)

    Determine number of elements in scatterlist to provide a specified number of bytes.

    :param struct scatterlist \*sg_list:
        scatterlist to examine

    :param unsigned int skip:
        index of starting point

    :param int nbytes:
        consider elements of scatterlist until reaching this number of
        bytes

.. _`spu_sg_count.return`:

Return
------

the number of sg entries contributing to nbytes of data

.. _`spu_msg_sg_add`:

spu_msg_sg_add
==============

.. c:function:: u32 spu_msg_sg_add(struct scatterlist **to_sg, struct scatterlist **from_sg, u32 *from_skip, u8 from_nents, u32 length)

    Copy scatterlist entries from one sg to another, up to a given length.

    :param struct scatterlist \*\*to_sg:
        scatterlist to copy to

    :param struct scatterlist \*\*from_sg:
        scatterlist to copy from

    :param u32 \*from_skip:
        number of bytes to skip in from_sg. Non-zero when previous
        request included part of the buffer in entry in from_sg.
        Assumes from_skip < from_sg->length.
        \ ``from_nents``\    number of entries in from_sg
        \ ``length``\        number of bytes to copy. may reach this limit before exhausting
        from_sg.

    :param u8 from_nents:
        *undescribed*

    :param u32 length:
        *undescribed*

.. _`spu_msg_sg_add.description`:

Description
-----------

Copies the entries themselves, not the data in the entries. Assumes to_sg has
enough entries. Does not limit the size of an individual buffer in to_sg.

to_sg, from_sg, skip are all updated to end of copy

.. _`spu_msg_sg_add.return`:

Return
------

Number of bytes copied

.. _`do_shash`:

do_shash
========

.. c:function:: int do_shash(unsigned char *name, unsigned char *result, const u8 *data1, unsigned int data1_len, const u8 *data2, unsigned int data2_len, const u8 *key, unsigned int key_len)

    Do a synchronous hash operation in software

    :param unsigned char \*name:
        The name of the hash algorithm

    :param unsigned char \*result:
        Buffer where digest is to be written

    :param const u8 \*data1:
        First part of data to hash. May be NULL.

    :param unsigned int data1_len:
        Length of data1, in bytes

    :param const u8 \*data2:
        Second part of data to hash. May be NULL.

    :param unsigned int data2_len:
        Length of data2, in bytes

    :param const u8 \*key:
        Key (if keyed hash)

    :param unsigned int key_len:
        Length of key, in bytes (or 0 if non-keyed hash)

.. _`do_shash.description`:

Description
-----------

Note that the crypto API will not select this driver's own transform because
this driver only registers asynchronous algos.

.. _`do_shash.return`:

Return
------

0 if hash successfully stored in result
< 0 otherwise

.. _`format_value_ccm`:

format_value_ccm
================

.. c:function:: void format_value_ccm(unsigned int val, u8 *buf, u8 len)

    Format a value into a buffer, using a specified number of bytes (i.e. maybe writing value X into a 4 byte buffer, or maybe into a 12 byte buffer), as per the SPU CCM spec.

    :param unsigned int val:
        value to write (up to max of unsigned int)

    :param u8 \*buf:
        (pointer to) buffer to write the value

    :param u8 len:
        number of bytes to use (0 to 255)

.. This file was automatic generated / don't edit.

