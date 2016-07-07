.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/bitmap.h

.. _`ntfs_bitmap_set_bits_in_run`:

ntfs_bitmap_set_bits_in_run
===========================

.. c:function:: int ntfs_bitmap_set_bits_in_run(struct inode *vi, const s64 start_bit, const s64 count, const u8 value)

    set a run of bits in a bitmap to a value

    :param struct inode \*vi:
        vfs inode describing the bitmap

    :param const s64 start_bit:
        first bit to set

    :param const s64 count:
        number of bits to set

    :param const u8 value:
        value to set the bits to (i.e. 0 or 1)

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

    :param struct inode \*vi:
        vfs inode describing the bitmap

    :param const s64 start_bit:
        first bit to set

    :param const s64 count:
        number of bits to set

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

    :param struct inode \*vi:
        vfs inode describing the bitmap

    :param const s64 start_bit:
        first bit to clear

    :param const s64 count:
        number of bits to clear

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

    :param struct inode \*vi:
        vfs inode describing the bitmap

    :param const s64 bit:
        bit to set

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

    :param struct inode \*vi:
        vfs inode describing the bitmap

    :param const s64 bit:
        bit to clear

.. _`ntfs_bitmap_clear_bit.description`:

Description
-----------

Clear bit \ ``bit``\  in the bitmap described by the vfs inode \ ``vi``\ .

Return 0 on success and -errno on error.

.. This file was automatic generated / don't edit.

