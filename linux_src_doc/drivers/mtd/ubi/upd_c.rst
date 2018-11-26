.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/upd.c

.. _`set_update_marker`:

set_update_marker
=================

.. c:function:: int set_update_marker(struct ubi_device *ubi, struct ubi_volume *vol)

    set update marker.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

.. _`set_update_marker.description`:

Description
-----------

This function sets the update marker flag for volume \ ``vol``\ . Returns zero
in case of success and a negative error code in case of failure.

.. _`clear_update_marker`:

clear_update_marker
===================

.. c:function:: int clear_update_marker(struct ubi_device *ubi, struct ubi_volume *vol, long long bytes)

    clear update marker.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param bytes:
        new data size in bytes
    :type bytes: long long

.. _`clear_update_marker.description`:

Description
-----------

This function clears the update marker for volume \ ``vol``\ , sets new volume
data size and clears the "corrupted" flag (static volumes only). Returns
zero in case of success and a negative error code in case of failure.

.. _`ubi_start_update`:

ubi_start_update
================

.. c:function:: int ubi_start_update(struct ubi_device *ubi, struct ubi_volume *vol, long long bytes)

    start volume update.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param bytes:
        update bytes
    :type bytes: long long

.. _`ubi_start_update.description`:

Description
-----------

This function starts volume update operation. If \ ``bytes``\  is zero, the volume
is just wiped out. Returns zero in case of success and a negative error code
in case of failure.

.. _`ubi_start_leb_change`:

ubi_start_leb_change
====================

.. c:function:: int ubi_start_leb_change(struct ubi_device *ubi, struct ubi_volume *vol, const struct ubi_leb_change_req *req)

    start atomic LEB change.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param req:
        operation request
    :type req: const struct ubi_leb_change_req \*

.. _`ubi_start_leb_change.description`:

Description
-----------

This function starts atomic LEB change operation. Returns zero in case of
success and a negative error code in case of failure.

.. _`write_leb`:

write_leb
=========

.. c:function:: int write_leb(struct ubi_device *ubi, struct ubi_volume *vol, int lnum, void *buf, int len, int used_ebs)

    write update data.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param lnum:
        logical eraseblock number
    :type lnum: int

    :param buf:
        data to write
    :type buf: void \*

    :param len:
        data size
    :type len: int

    :param used_ebs:
        how many logical eraseblocks will this volume contain (static
        volumes only)
    :type used_ebs: int

.. _`write_leb.description`:

Description
-----------

This function writes update data to corresponding logical eraseblock. In
case of dynamic volume, this function checks if the data contains 0xFF bytes
at the end. If yes, the 0xFF bytes are cut and not written. So if the whole
buffer contains only 0xFF bytes, the LEB is left unmapped.

The reason why we skip the trailing 0xFF bytes in case of dynamic volume is
that we want to make sure that more data may be appended to the logical
eraseblock in future. Indeed, writing 0xFF bytes may have side effects and
this PEB won't be writable anymore. So if one writes the file-system image
to the UBI volume where 0xFFs mean free space - UBI makes sure this free
space is writable after the update.

We do not do this for static volumes because they are read-only. But this
also cannot be done because we have to store per-LEB CRC and the correct
data length.

This function returns zero in case of success and a negative error code in
case of failure.

.. _`ubi_more_update_data`:

ubi_more_update_data
====================

.. c:function:: int ubi_more_update_data(struct ubi_device *ubi, struct ubi_volume *vol, const void __user *buf, int count)

    write more update data.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param buf:
        write data (user-space memory buffer)
    :type buf: const void __user \*

    :param count:
        how much bytes to write
    :type count: int

.. _`ubi_more_update_data.description`:

Description
-----------

This function writes more data to the volume which is being updated. It may
be called arbitrary number of times until all the update data arriveis. This
function returns \ ``0``\  in case of success, number of bytes written during the
last call if the whole volume update has been successfully finished, and a
negative error code in case of failure.

.. _`ubi_more_leb_change_data`:

ubi_more_leb_change_data
========================

.. c:function:: int ubi_more_leb_change_data(struct ubi_device *ubi, struct ubi_volume *vol, const void __user *buf, int count)

    accept more data for atomic LEB change.

    :param ubi:
        UBI device description object
    :type ubi: struct ubi_device \*

    :param vol:
        volume description object
    :type vol: struct ubi_volume \*

    :param buf:
        write data (user-space memory buffer)
    :type buf: const void __user \*

    :param count:
        how much bytes to write
    :type count: int

.. _`ubi_more_leb_change_data.description`:

Description
-----------

This function accepts more data to the volume which is being under the
"atomic LEB change" operation. It may be called arbitrary number of times
until all data arrives. This function returns \ ``0``\  in case of success, number
of bytes written during the last call if the whole "atomic LEB change"
operation has been successfully finished, and a negative error code in case
of failure.

.. This file was automatic generated / don't edit.

