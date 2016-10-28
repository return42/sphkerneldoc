.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/vtbl.c

.. _`ubi_update_layout_vol`:

ubi_update_layout_vol
=====================

.. c:function:: int ubi_update_layout_vol(struct ubi_device *ubi)

    helper for updatting layout volumes on flash

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`ubi_change_vtbl_record`:

ubi_change_vtbl_record
======================

.. c:function:: int ubi_change_vtbl_record(struct ubi_device *ubi, int idx, struct ubi_vtbl_record *vtbl_rec)

    change volume table record.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int idx:
        table index to change

    :param struct ubi_vtbl_record \*vtbl_rec:
        new volume table record

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct list_head \*rename_list:
        list of \ :c:type:`struct ubi_rename_entry <ubi_rename_entry>`\  objects

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

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param const struct ubi_vtbl_record \*vtbl:
        volume table

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

    :param int copy:
        number of the volume table copy

    :param void \*vtbl:
        contents of the volume table

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

    :param struct ubi_ainf_volume \*av:
        layout volume attaching information

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param const struct ubi_attach_info \*ai:
        scanning information

    :param const struct ubi_vtbl_record \*vtbl:
        volume table

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

    :param const struct ubi_volume \*vol:
        UBI volume description object

    :param const struct ubi_ainf_volume \*av:
        volume attaching information

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

    :param const struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

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

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_attach_info \*ai:
        attaching information

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

    :param const struct ubi_device \*ubi:
        UBI device description object

.. This file was automatic generated / don't edit.

