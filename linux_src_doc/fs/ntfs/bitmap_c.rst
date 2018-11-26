.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/bitmap.c

.. _`__ntfs_bitmap_set_bits_in_run`:

\__ntfs_bitmap_set_bits_in_run
==============================

.. c:function:: int __ntfs_bitmap_set_bits_in_run(struct inode *vi, const s64 start_bit, const s64 count, const u8 value, const bool is_rollback)

    set a run of bits in a bitmap to a value

    :param vi:
        vfs inode describing the bitmap
    :type vi: struct inode \*

    :param start_bit:
        first bit to set
    :type start_bit: const s64

    :param count:
        number of bits to set
    :type count: const s64

    :param value:
        value to set the bits to (i.e. 0 or 1)
    :type value: const u8

    :param is_rollback:
        if 'true' this is a rollback operation
    :type is_rollback: const bool

.. _`__ntfs_bitmap_set_bits_in_run.description`:

Description
-----------

Set \ ``count``\  bits starting at bit \ ``start_bit``\  in the bitmap described by the
vfs inode \ ``vi``\  to \ ``value``\ , where \ ``value``\  is either 0 or 1.

\ ``is_rollback``\  should always be 'false', it is for internal use to rollback
errors.  You probably want to use \ :c:func:`ntfs_bitmap_set_bits_in_run`\  instead.

Return 0 on success and -errno on error.

.. This file was automatic generated / don't edit.

