.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/volumes.c

.. _`alloc_profile_is_valid`:

alloc_profile_is_valid
======================

.. c:function:: int alloc_profile_is_valid(u64 flags, int extended)

    see if a given profile is valid and reduced

    :param flags:
        profile to validate
    :type flags: u64

    :param extended:
        if true \ ``flags``\  is treated as an extended profile
    :type extended: int

.. _`btrfs_alloc_device`:

btrfs_alloc_device
==================

.. c:function:: struct btrfs_device *btrfs_alloc_device(struct btrfs_fs_info *fs_info, const u64 *devid, const u8 *uuid)

    allocate struct btrfs_device

    :param fs_info:
        used only for generating a new devid, can be NULL if
        devid is provided (i.e. \ ``devid``\  != NULL).
    :type fs_info: struct btrfs_fs_info \*

    :param devid:
        a pointer to devid for this device.  If NULL a new devid
        is generated.
    :type devid: const u64 \*

    :param uuid:
        a pointer to UUID for this device.  If NULL a new UUID
        is generated.
    :type uuid: const u8 \*

.. _`btrfs_alloc_device.return`:

Return
------

a pointer to a new \ :c:type:`struct btrfs_device <btrfs_device>`\  on success; \ :c:func:`ERR_PTR`\ 
on error.  Returned struct is not linked onto any lists and must be
destroyed with btrfs_free_device.

.. This file was automatic generated / don't edit.

