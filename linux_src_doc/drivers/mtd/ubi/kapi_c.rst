.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/kapi.c

.. _`ubi_do_get_device_info`:

ubi_do_get_device_info
======================

.. c:function:: void ubi_do_get_device_info(struct ubi_device *ubi, struct ubi_device_info *di)

    get information about UBI device.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_device_info \*di:
        the information is stored here

.. _`ubi_do_get_device_info.description`:

Description
-----------

This function is the same as '\ :c:func:`ubi_get_device_info`\ ', but it assumes the UBI
device is locked and cannot disappear.

.. _`ubi_get_device_info`:

ubi_get_device_info
===================

.. c:function:: int ubi_get_device_info(int ubi_num, struct ubi_device_info *di)

    get information about UBI device.

    :param int ubi_num:
        UBI device number

    :param struct ubi_device_info \*di:
        the information is stored here

.. _`ubi_get_device_info.description`:

Description
-----------

This function returns \ ``0``\  in case of success, \ ``-EINVAL``\  if the UBI device
number is invalid, and \ ``-ENODEV``\  if there is no such UBI device.

.. _`ubi_do_get_volume_info`:

ubi_do_get_volume_info
======================

.. c:function:: void ubi_do_get_volume_info(struct ubi_device *ubi, struct ubi_volume *vol, struct ubi_volume_info *vi)

    get information about UBI volume.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_volume \*vol:
        volume description object

    :param struct ubi_volume_info \*vi:
        the information is stored here

.. _`ubi_get_volume_info`:

ubi_get_volume_info
===================

.. c:function:: void ubi_get_volume_info(struct ubi_volume_desc *desc, struct ubi_volume_info *vi)

    get information about UBI volume.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param struct ubi_volume_info \*vi:
        the information is stored here

.. _`ubi_open_volume`:

ubi_open_volume
===============

.. c:function:: struct ubi_volume_desc *ubi_open_volume(int ubi_num, int vol_id, int mode)

    open UBI volume.

    :param int ubi_num:
        UBI device number

    :param int vol_id:
        volume ID

    :param int mode:
        open mode

.. _`ubi_open_volume.description`:

Description
-----------

The \ ``mode``\  parameter specifies if the volume should be opened in read-only
mode, read-write mode, or exclusive mode. The exclusive mode guarantees that
nobody else will be able to open this volume. UBI allows to have many volume
readers and one writer at a time.

If a static volume is being opened for the first time since boot, it will be
checked by this function, which means it will be fully read and the CRC
checksum of each logical eraseblock will be checked.

This function returns volume descriptor in case of success and a negative
error code in case of failure.

.. _`ubi_open_volume_nm`:

ubi_open_volume_nm
==================

.. c:function:: struct ubi_volume_desc *ubi_open_volume_nm(int ubi_num, const char *name, int mode)

    open UBI volume by name.

    :param int ubi_num:
        UBI device number

    :param const char \*name:
        volume name

    :param int mode:
        open mode

.. _`ubi_open_volume_nm.description`:

Description
-----------

This function is similar to '\ :c:func:`ubi_open_volume`\ ', but opens a volume by name.

.. _`ubi_open_volume_path`:

ubi_open_volume_path
====================

.. c:function:: struct ubi_volume_desc *ubi_open_volume_path(const char *pathname, int mode)

    open UBI volume by its character device node path.

    :param const char \*pathname:
        volume character device node path

    :param int mode:
        open mode

.. _`ubi_open_volume_path.description`:

Description
-----------

This function is similar to '\ :c:func:`ubi_open_volume`\ ', but opens a volume the path
to its character device node.

.. _`ubi_close_volume`:

ubi_close_volume
================

.. c:function:: void ubi_close_volume(struct ubi_volume_desc *desc)

    close UBI volume.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

.. _`leb_read_sanity_check`:

leb_read_sanity_check
=====================

.. c:function:: int leb_read_sanity_check(struct ubi_volume_desc *desc, int lnum, int offset, int len)

    does sanity checks on read requests.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number to read from

    :param int offset:
        offset within the logical eraseblock to read from

    :param int len:
        how many bytes to read

.. _`leb_read_sanity_check.description`:

Description
-----------

This function is used by \ :c:func:`ubi_leb_read`\  and \ :c:func:`ubi_leb_read_sg`\ 
to perform sanity checks.

.. _`ubi_leb_read`:

ubi_leb_read
============

.. c:function:: int ubi_leb_read(struct ubi_volume_desc *desc, int lnum, char *buf, int offset, int len, int check)

    read data.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number to read from

    :param char \*buf:
        buffer where to store the read data

    :param int offset:
        offset within the logical eraseblock to read from

    :param int len:
        how many bytes to read

    :param int check:
        whether UBI has to check the read data's CRC or not.

.. _`ubi_leb_read.description`:

Description
-----------

This function reads data from offset \ ``offset``\  of logical eraseblock \ ``lnum``\  and
stores the data at \ ``buf``\ . When reading from static volumes, \ ``check``\  specifies
whether the data has to be checked or not. If yes, the whole logical
eraseblock will be read and its CRC checksum will be checked (i.e., the CRC
checksum is per-eraseblock). So checking may substantially slow down the
read speed. The \ ``check``\  argument is ignored for dynamic volumes.

In case of success, this function returns zero. In case of failure, this
function returns a negative error code.

\ ``-EBADMSG``\  error code is returned:
o for both static and dynamic volumes if MTD driver has detected a data
integrity problem (unrecoverable ECC checksum mismatch in case of NAND);
o for static volumes in case of data CRC mismatch.

If the volume is damaged because of an interrupted update this function just
returns immediately with \ ``-EBADF``\  error code.

.. _`ubi_leb_read_sg`:

ubi_leb_read_sg
===============

.. c:function:: int ubi_leb_read_sg(struct ubi_volume_desc *desc, int lnum, struct ubi_sgl *sgl, int offset, int len, int check)

    read data into a scatter gather list.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number to read from

    :param struct ubi_sgl \*sgl:
        *undescribed*

    :param int offset:
        offset within the logical eraseblock to read from

    :param int len:
        how many bytes to read

    :param int check:
        whether UBI has to check the read data's CRC or not.

.. _`ubi_leb_read_sg.description`:

Description
-----------

This function works exactly like \ :c:func:`ubi_leb_read_sg`\ . But instead of
storing the read data into a buffer it writes to an UBI scatter gather
list.

.. _`ubi_leb_write`:

ubi_leb_write
=============

.. c:function:: int ubi_leb_write(struct ubi_volume_desc *desc, int lnum, const void *buf, int offset, int len)

    write data.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number to write to

    :param const void \*buf:
        data to write

    :param int offset:
        offset within the logical eraseblock where to write

    :param int len:
        how many bytes to write

.. _`ubi_leb_write.description`:

Description
-----------

This function writes \ ``len``\  bytes of data from \ ``buf``\  to offset \ ``offset``\  of
logical eraseblock \ ``lnum``\ .

This function takes care of physical eraseblock write failures. If write to
the physical eraseblock write operation fails, the logical eraseblock is
re-mapped to another physical eraseblock, the data is recovered, and the
write finishes. UBI has a pool of reserved physical eraseblocks for this.

If all the data were successfully written, zero is returned. If an error
occurred and UBI has not been able to recover from it, this function returns
a negative error code. Note, in case of an error, it is possible that
something was still written to the flash media, but that may be some
garbage.

If the volume is damaged because of an interrupted update this function just
returns immediately with \ ``-EBADF``\  code.

.. _`ubi_leb_erase`:

ubi_leb_erase
=============

.. c:function:: int ubi_leb_erase(struct ubi_volume_desc *desc, int lnum)

    erase logical eraseblock.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number

.. _`ubi_leb_erase.description`:

Description
-----------

This function un-maps logical eraseblock \ ``lnum``\  and synchronously erases the
correspondent physical eraseblock. Returns zero in case of success and a
negative error code in case of failure.

If the volume is damaged because of an interrupted update this function just
returns immediately with \ ``-EBADF``\  code.

.. _`ubi_leb_unmap`:

ubi_leb_unmap
=============

.. c:function:: int ubi_leb_unmap(struct ubi_volume_desc *desc, int lnum)

    un-map logical eraseblock.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number

.. _`ubi_leb_unmap.description`:

Description
-----------

This function un-maps logical eraseblock \ ``lnum``\  and schedules the
corresponding physical eraseblock for erasure, so that it will eventually be
physically erased in background. This operation is much faster than the
erase operation.

Unlike erase, the un-map operation does not guarantee that the logical
eraseblock will contain all 0xFF bytes when UBI is initialized again. For
example, if several logical eraseblocks are un-mapped, and an unclean reboot
happens after this, the logical eraseblocks will not necessarily be
un-mapped again when this MTD device is attached. They may actually be
mapped to the same physical eraseblocks again. So, this function has to be
used with care.

In other words, when un-mapping a logical eraseblock, UBI does not store
any information about this on the flash media, it just marks the logical
eraseblock as "un-mapped" in RAM. If UBI is detached before the physical
eraseblock is physically erased, it will be mapped again to the same logical
eraseblock when the MTD device is attached again.

The main and obvious use-case of this function is when the contents of a
logical eraseblock has to be re-written. Then it is much more efficient to
first un-map it, then write new data, rather than first erase it, then write
new data. Note, once new data has been written to the logical eraseblock,
UBI guarantees that the old contents has gone forever. In other words, if an
unclean reboot happens after the logical eraseblock has been un-mapped and
then written to, it will contain the last written data.

This function returns zero in case of success and a negative error code in
case of failure. If the volume is damaged because of an interrupted update
this function just returns immediately with \ ``-EBADF``\  code.

.. _`ubi_leb_map`:

ubi_leb_map
===========

.. c:function:: int ubi_leb_map(struct ubi_volume_desc *desc, int lnum)

    map logical eraseblock to a physical eraseblock.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number

.. _`ubi_leb_map.description`:

Description
-----------

This function maps an un-mapped logical eraseblock \ ``lnum``\  to a physical
eraseblock. This means, that after a successful invocation of this
function the logical eraseblock \ ``lnum``\  will be empty (contain only \ ``0xFF``\ 
bytes) and be mapped to a physical eraseblock, even if an unclean reboot
happens.

This function returns zero in case of success, \ ``-EBADF``\  if the volume is
damaged because of an interrupted update, \ ``-EBADMSG``\  if the logical
eraseblock is already mapped, and other negative error codes in case of
other failures.

.. _`ubi_is_mapped`:

ubi_is_mapped
=============

.. c:function:: int ubi_is_mapped(struct ubi_volume_desc *desc, int lnum)

    check if logical eraseblock is mapped.

    :param struct ubi_volume_desc \*desc:
        volume descriptor

    :param int lnum:
        logical eraseblock number

.. _`ubi_is_mapped.description`:

Description
-----------

This function checks if logical eraseblock \ ``lnum``\  is mapped to a physical
eraseblock. If a logical eraseblock is un-mapped, this does not necessarily
mean it will still be un-mapped after the UBI device is re-attached. The
logical eraseblock may become mapped to the physical eraseblock it was last
mapped to.

This function returns \ ``1``\  if the LEB is mapped, \ ``0``\  if not, and a negative
error code in case of failure. If the volume is damaged because of an
interrupted update this function just returns immediately with \ ``-EBADF``\  error
code.

.. _`ubi_sync`:

ubi_sync
========

.. c:function:: int ubi_sync(int ubi_num)

    synchronize UBI device buffers.

    :param int ubi_num:
        UBI device to synchronize

.. _`ubi_sync.description`:

Description
-----------

The underlying MTD device may cache data in hardware or in software. This
function ensures the caches are flushed. Returns zero in case of success and
a negative error code in case of failure.

.. _`ubi_flush`:

ubi_flush
=========

.. c:function:: int ubi_flush(int ubi_num, int vol_id, int lnum)

    flush UBI work queue.

    :param int ubi_num:
        UBI device to flush work queue

    :param int vol_id:
        volume id to flush for

    :param int lnum:
        logical eraseblock number to flush for

.. _`ubi_flush.description`:

Description
-----------

This function executes all pending works for a particular volume id / logical
eraseblock number pair. If either value is set to \ ``UBI_ALL``\ , then it acts as
a wildcard for all of the corresponding volume numbers or logical
eraseblock numbers. It returns zero in case of success and a negative error
code in case of failure.

.. _`ubi_register_volume_notifier`:

ubi_register_volume_notifier
============================

.. c:function:: int ubi_register_volume_notifier(struct notifier_block *nb, int ignore_existing)

    register a volume notifier.

    :param struct notifier_block \*nb:
        the notifier description object

    :param int ignore_existing:
        if non-zero, do not send "added" notification for all
        already existing volumes

.. _`ubi_register_volume_notifier.description`:

Description
-----------

This function registers a volume notifier, which means that
'nb->\ :c:func:`notifier_call`\ ' will be invoked when an UBI  volume is created,
removed, re-sized, re-named, or updated. The first argument of the function
is the notification type. The second argument is pointer to a
\ :c:type:`struct ubi_notification <ubi_notification>`\  object which describes the notification event.
Using UBI API from the volume notifier is prohibited.

This function returns zero in case of success and a negative error code
in case of failure.

.. _`ubi_unregister_volume_notifier`:

ubi_unregister_volume_notifier
==============================

.. c:function:: int ubi_unregister_volume_notifier(struct notifier_block *nb)

    unregister the volume notifier.

    :param struct notifier_block \*nb:
        the notifier description object

.. _`ubi_unregister_volume_notifier.description`:

Description
-----------

This function unregisters volume notifier \ ``nm``\  and returns zero in case of
success and a negative error code in case of failure.

.. This file was automatic generated / don't edit.

