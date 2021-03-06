.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/vmt.c

.. _`ubi_create_volume`:

ubi_create_volume
=================

.. c:function:: int ubi_create_volume(struct ubi_device *ubi, struct ubi_mkvol_req *req)

    create volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param req:
        volume creation request
    :type req: struct ubi_mkvol_req \*

.. _`ubi_create_volume.description`:

Description
-----------

This function creates volume described by \ ``req``\ . If \ ``req->vol_id``\  id
\ ``UBI_VOL_NUM_AUTO``\ , this function automatically assign ID to the new volume
and saves it in \ ``req->vol_id``\ . Returns zero in case of success and a negative
error code in case of failure. Note, the caller has to have the
\ ``ubi->device_mutex``\  locked.

.. _`ubi_remove_volume`:

ubi_remove_volume
=================

.. c:function:: int ubi_remove_volume(struct ubi_volume_desc *desc, int no_vtbl)

    remove volume.

    :param desc:
        volume descriptor
    :type desc: struct ubi_volume_desc \*

    :param no_vtbl:
        do not change volume table if not zero
    :type no_vtbl: int

.. _`ubi_remove_volume.description`:

Description
-----------

This function removes volume described by \ ``desc``\ . The volume has to be opened
in "exclusive" mode. Returns zero in case of success and a negative error
code in case of failure. The caller has to have the \ ``ubi->device_mutex``\ 
locked.

.. _`ubi_resize_volume`:

ubi_resize_volume
=================

.. c:function:: int ubi_resize_volume(struct ubi_volume_desc *desc, int reserved_pebs)

    re-size volume.

    :param desc:
        volume descriptor
    :type desc: struct ubi_volume_desc \*

    :param reserved_pebs:
        new size in physical eraseblocks
    :type reserved_pebs: int

.. _`ubi_resize_volume.description`:

Description
-----------

This function re-sizes the volume and returns zero in case of success, and a
negative error code in case of failure. The caller has to have the
\ ``ubi->device_mutex``\  locked.

.. _`ubi_rename_volumes`:

ubi_rename_volumes
==================

.. c:function:: int ubi_rename_volumes(struct ubi_device *ubi, struct list_head *rename_list)

    re-name UBI volumes.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param rename_list:
        list of \ :c:type:`struct ubi_rename_entry <ubi_rename_entry>`\  objects
    :type rename_list: struct list_head \*

.. _`ubi_rename_volumes.description`:

Description
-----------

This function re-names or removes volumes specified in the re-name list.
Returns zero in case of success and a negative error code in case of
failure.

.. _`ubi_add_volume`:

ubi_add_volume
==============

.. c:function:: int ubi_add_volume(struct ubi_device *ubi, struct ubi_volume *vol)

    add volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

.. _`ubi_add_volume.description`:

Description
-----------

This function adds an existing volume and initializes all its data
structures. Returns zero in case of success and a negative error code in
case of failure.

.. _`ubi_free_volume`:

ubi_free_volume
===============

.. c:function:: void ubi_free_volume(struct ubi_device *ubi, struct ubi_volume *vol)

    free volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

.. _`ubi_free_volume.description`:

Description
-----------

This function frees all resources for volume \ ``vol``\  but does not remove it.
Used only when the UBI device is detached.

.. _`self_check_volume`:

self_check_volume
=================

.. c:function:: int self_check_volume(struct ubi_device *ubi, int vol_id)

    check volume information.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol_id:
        volume ID
    :type vol_id: int

.. _`self_check_volume.description`:

Description
-----------

Returns zero if volume is all right and a a negative error code if not.

.. _`self_check_volumes`:

self_check_volumes
==================

.. c:function:: int self_check_volumes(struct ubi_device *ubi)

    check information about all volumes.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`self_check_volumes.description`:

Description
-----------

Returns zero if volumes are all right and a a negative error code if not.

.. This file was automatic generated / don't edit.

