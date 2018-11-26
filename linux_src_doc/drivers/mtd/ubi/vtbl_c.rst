.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/vtbl.c

.. _`ubi_update_layout_vol`:

ubi_update_layout_vol
=====================

.. c:function:: int ubi_update_layout_vol(struct ubi_device *ubi)

    helper for updatting layout volumes on flash

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

.. _`ubi_change_vtbl_record`:

ubi_change_vtbl_record
======================

.. c:function:: int ubi_change_vtbl_record(struct ubi_device *ubi, int idx, struct ubi_vtbl_record *vtbl_rec)

    change volume table record.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param idx:
        table index to change
    :type idx: int

    :param vtbl_rec:
        new volume table record
    :type vtbl_rec: struct ubi_vtbl_record \*

.. _`ubi_change_vtbl_record.description`:

Description
-----------

This function changes volume table record \ ``idx``\ . If \ ``vtbl_rec``\  is \ ``NULL``\ , empty
volume table record is written. The caller does not have to calculate CRC of
the record as it is done by this function. Returns zero in case of success
and a negative error code in case of failure.

.. _`ubi_vtbl_rename_volumes`:

ubi_vtbl_rename_volumes
=======================

.. c:function:: int ubi_vtbl_rename_volumes(struct ubi_device *ubi, struct list_head *rename_list)

    rename UBI volumes in the volume table.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param rename_list:
        list of \ :c:type:`struct ubi_rename_entry <ubi_rename_entry>`\  objects
    :type rename_list: struct list_head \*

.. _`ubi_vtbl_rename_volumes.description`:

Description
-----------

This function re-names multiple volumes specified in \ ``req``\  in the volume
table. Returns zero in case of success and a negative error code in case of
failure.

.. _`vtbl_check`:

vtbl_check
==========

.. c:function:: int vtbl_check(const struct ubi_device *ubi, const struct ubi_vtbl_record *vtbl)

    check if volume table is not corrupted and sensible.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param vtbl:
        volume table
    :type vtbl: const struct ubi_vtbl_record \*

.. _`vtbl_check.description`:

Description
-----------

This function returns zero if \ ``vtbl``\  is all right, \ ``1``\  if CRC is incorrect,
and \ ``-EINVAL``\  if it contains inconsistent data.

.. _`create_vtbl`:

create_vtbl
===========

.. c:function:: int create_vtbl(struct ubi_device *ubi, struct ubi_attach_info *ai, int copy, void *vtbl)

    create a copy of volume table.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        attaching information
    :type ai: struct ubi_attach_info \*

    :param copy:
        number of the volume table copy
    :type copy: int

    :param vtbl:
        contents of the volume table
    :type vtbl: void \*

.. _`create_vtbl.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`process_lvol`:

process_lvol
============

.. c:function:: struct ubi_vtbl_record *process_lvol(struct ubi_device *ubi, struct ubi_attach_info *ai, struct ubi_ainf_volume *av)

    process the layout volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        attaching information
    :type ai: struct ubi_attach_info \*

    :param av:
        layout volume attaching information
    :type av: struct ubi_ainf_volume \*

.. _`process_lvol.description`:

Description
-----------

This function is responsible for reading the layout volume, ensuring it is
not corrupted, and recovering from corruptions if needed. Returns volume
table in case of success and a negative error code in case of failure.

.. _`create_empty_lvol`:

create_empty_lvol
=================

.. c:function:: struct ubi_vtbl_record *create_empty_lvol(struct ubi_device *ubi, struct ubi_attach_info *ai)

    create empty layout volume.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        attaching information
    :type ai: struct ubi_attach_info \*

.. _`create_empty_lvol.description`:

Description
-----------

This function returns volume table contents in case of success and a
negative error code in case of failure.

.. _`init_volumes`:

init_volumes
============

.. c:function:: int init_volumes(struct ubi_device *ubi, const struct ubi_attach_info *ai, const struct ubi_vtbl_record *vtbl)

    initialize volume information for existing volumes.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        scanning information
    :type ai: const struct ubi_attach_info \*

    :param vtbl:
        volume table
    :type vtbl: const struct ubi_vtbl_record \*

.. _`init_volumes.description`:

Description
-----------

This function allocates volume description objects for existing volumes.
Returns zero in case of success and a negative error code in case of
failure.

.. _`check_av`:

check_av
========

.. c:function:: int check_av(const struct ubi_volume *vol, const struct ubi_ainf_volume *av)

    check volume attaching information.

    :param vol:
        UBI volume description object
    :type vol: const struct ubi_volume \*

    :param av:
        volume attaching information
    :type av: const struct ubi_ainf_volume \*

.. _`check_av.description`:

Description
-----------

This function returns zero if the volume attaching information is consistent
to the data read from the volume tabla, and \ ``-EINVAL``\  if not.

.. _`check_attaching_info`:

check_attaching_info
====================

.. c:function:: int check_attaching_info(const struct ubi_device *ubi, struct ubi_attach_info *ai)

    check that attaching information.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

    :param ai:
        attaching information
    :type ai: struct ubi_attach_info \*

.. _`check_attaching_info.description`:

Description
-----------

Even though we protect on-flash data by CRC checksums, we still don't trust
the media. This function ensures that attaching information is consistent to
the information read from the volume table. Returns zero if the attaching
information is OK and \ ``-EINVAL``\  if it is not.

.. _`ubi_read_volume_table`:

ubi_read_volume_table
=====================

.. c:function:: int ubi_read_volume_table(struct ubi_device *ubi, struct ubi_attach_info *ai)

    read the volume table.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param ai:
        attaching information
    :type ai: struct ubi_attach_info \*

.. _`ubi_read_volume_table.description`:

Description
-----------

This function reads volume table, checks it, recover from errors if needed,
or creates it if needed. Returns zero in case of success and a negative
error code in case of failure.

.. _`self_vtbl_check`:

self_vtbl_check
===============

.. c:function:: void self_vtbl_check(const struct ubi_device *ubi)

    check volume table.

    :param ubi:
        UBI device description object
    :type ubi: const struct ubi_device \*

.. This file was automatic generated / don't edit.

