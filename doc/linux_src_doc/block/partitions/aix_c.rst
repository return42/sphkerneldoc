.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/partitions/aix.c

.. _`last_lba`:

last_lba
========

.. c:function:: u64 last_lba(struct block_device *bdev)

    return number of last logical block of device

    :param struct block_device \*bdev:
        block device

.. _`last_lba.description`:

Description
-----------

Returns last LBA value on success, 0 on error.
This is stored (by sd and ide-geometry) in
the part[0] entry for this disk, and is the number of
physical sectors available on the disk.

.. _`read_lba`:

read_lba
========

.. c:function:: size_t read_lba(struct parsed_partitions *state, u64 lba, u8 *buffer, size_t count)

    Read bytes from disk, starting at given LBA \ ``state``\  \ ``lba``\  \ ``buffer``\  \ ``count``\ 

    :param struct parsed_partitions \*state:
        *undescribed*

    :param u64 lba:
        *undescribed*

    :param u8 \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`read_lba.description`:

Description
-----------

Reads \ ``count``\  bytes from \ ``state``\ ->bdev into \ ``buffer``\ .
Returns number of bytes read on success, 0 on error.

.. _`alloc_pvd`:

alloc_pvd
=========

.. c:function:: struct pvd *alloc_pvd(struct parsed_partitions *state, u32 lba)

    reads physical volume descriptor \ ``state``\  \ ``lba``\ 

    :param struct parsed_partitions \*state:
        *undescribed*

    :param u32 lba:
        *undescribed*

.. _`alloc_pvd.description`:

Description
-----------

Returns pvd on success,  NULL on error.
Allocates space for pvd and fill it with disk blocks at \ ``lba``\ 

.. _`alloc_pvd.notes`:

Notes
-----

remember to free pvd when you're done!

.. _`alloc_lvn`:

alloc_lvn
=========

.. c:function:: struct lvname *alloc_lvn(struct parsed_partitions *state, u32 lba)

    reads logical volume names \ ``state``\  \ ``lba``\ 

    :param struct parsed_partitions \*state:
        *undescribed*

    :param u32 lba:
        *undescribed*

.. _`alloc_lvn.description`:

Description
-----------

Returns lvn on success,  NULL on error.
Allocates space for lvn and fill it with disk blocks at \ ``lba``\ 

.. _`alloc_lvn.notes`:

Notes
-----

remember to free lvn when you're done!

.. This file was automatic generated / don't edit.

