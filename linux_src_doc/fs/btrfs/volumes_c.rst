.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/volumes.c

.. _`alloc_profile_is_valid`:

alloc_profile_is_valid
======================

.. c:function:: int alloc_profile_is_valid(u64 flags, int extended)

    see if a given profile is valid and reduced

    :param u64 flags:
        profile to validate

    :param int extended:
        if true \ ``flags``\  is treated as an extended profile

.. _`btrfs_alloc_device`:

btrfs_alloc_device
==================

.. c:function:: struct btrfs_device *btrfs_alloc_device(struct btrfs_fs_info *fs_info, const u64 *devid, const u8 *uuid)

    allocate struct btrfs_device

    :param struct btrfs_fs_info \*fs_info:
        used only for generating a new devid, can be NULL if
        devid is provided (i.e. \ ``devid``\  != NULL).

    :param const u64 \*devid:
        a pointer to devid for this device.  If NULL a new devid
        is generated.

    :param const u8 \*uuid:
        a pointer to UUID for this device.  If NULL a new UUID
        is generated.

.. _`btrfs_alloc_device.return`:

Return
------

a pointer to a new \ :c:type:`struct btrfs_device <btrfs_device>`\  on success; \ :c:func:`ERR_PTR`\ 
on error.  Returned struct is not linked onto any lists and can be
destroyed with \ :c:func:`kfree`\  right away.

.. This file was automatic generated / don't edit.

