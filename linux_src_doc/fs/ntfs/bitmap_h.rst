.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/bitmap.h

.. _`ntfs_bitmap_set_bits_in_run`:

ntfs_bitmap_set_bits_in_run
===========================

.. c:function:: int ntfs_bitmap_set_bits_in_run(struct inode *vi, const s64 start_bit, const s64 count, const u8 value)

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

.. _`ntfs_bitmap_set_bits_in_run.description`:

Description
-----------

Set \ ``count``\  bits starting at bit \ ``start_bit``\  in the bitmap described by the
vfs inode \ ``vi``\  to \ ``value``\ , where \ ``value``\  is either 0 or 1.

Return 0 on success and -errno on error.

.. _`ntfs_bitmap_set_run`:

ntfs_bitmap_set_run
===================

.. c:function:: int ntfs_bitmap_set_run(struct inode *vi, const s64 start_bit, const s64 count)

    set a run of bits in a bitmap

    :param vi:
        vfs inode describing the bitmap
    :type vi: struct inode \*

    :param start_bit:
        first bit to set
    :type start_bit: const s64

    :param count:
        number of bits to set
    :type count: const s64

.. _`ntfs_bitmap_set_run.description`:

Description
-----------

Set \ ``count``\  bits starting at bit \ ``start_bit``\  in the bitmap described by the
vfs inode \ ``vi``\ .

Return 0 on success and -errno on error.

.. _`ntfs_bitmap_clear_run`:

ntfs_bitmap_clear_run
=====================

.. c:function:: int ntfs_bitmap_clear_run(struct inode *vi, const s64 start_bit, const s64 count)

    clear a run of bits in a bitmap

    :param vi:
        vfs inode describing the bitmap
    :type vi: struct inode \*

    :param start_bit:
        first bit to clear
    :type start_bit: const s64

    :param count:
        number of bits to clear
    :type count: const s64

.. _`ntfs_bitmap_clear_run.description`:

Description
-----------

Clear \ ``count``\  bits starting at bit \ ``start_bit``\  in the bitmap described by the
vfs inode \ ``vi``\ .

Return 0 on success and -errno on error.

.. _`ntfs_bitmap_set_bit`:

ntfs_bitmap_set_bit
===================

.. c:function:: int ntfs_bitmap_set_bit(struct inode *vi, const s64 bit)

    set a bit in a bitmap

    :param vi:
        vfs inode describing the bitmap
    :type vi: struct inode \*

    :param bit:
        bit to set
    :type bit: const s64

.. _`ntfs_bitmap_set_bit.description`:

Description
-----------

Set bit \ ``bit``\  in the bitmap described by the vfs inode \ ``vi``\ .

Return 0 on success and -errno on error.

.. _`ntfs_bitmap_clear_bit`:

ntfs_bitmap_clear_bit
=====================

.. c:function:: int ntfs_bitmap_clear_bit(struct inode *vi, const s64 bit)

    clear a bit in a bitmap

    :param vi:
        vfs inode describing the bitmap
    :type vi: struct inode \*

    :param bit:
        bit to clear
    :type bit: const s64

.. _`ntfs_bitmap_clear_bit.description`:

Description
-----------

Clear bit \ ``bit``\  in the bitmap described by the vfs inode \ ``vi``\ .

Return 0 on success and -errno on error.

.. This file was automatic generated / don't edit.

