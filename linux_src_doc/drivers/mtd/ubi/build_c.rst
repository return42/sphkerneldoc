.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/build.c

.. _`mtd_dev_param`:

struct mtd_dev_param
====================

.. c:type:: struct mtd_dev_param

    MTD device parameter description data structure.

.. _`mtd_dev_param.definition`:

Definition
----------

.. code-block:: c

    struct mtd_dev_param {
        char name[MTD_PARAM_LEN_MAX];
        int ubi_num;
        int vid_hdr_offs;
        int max_beb_per1024;
    }

.. _`mtd_dev_param.members`:

Members
-------

name
    MTD character device node path, MTD device name, or MTD device number
    string

ubi_num
    *undescribed*

vid_hdr_offs
    VID header offset

max_beb_per1024
    maximum expected number of bad PEBs per 1024 PEBs

.. _`ubi_volume_notify`:

ubi_volume_notify
=================

.. c:function:: int ubi_volume_notify(struct ubi_device *ubi, struct ubi_volume *vol, int ntype)

    send a volume change notification.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param struct ubi_volume \*vol:
        volume description object of the changed volume

    :param int ntype:
        notification type to send (%UBI_VOLUME_ADDED, etc)

.. _`ubi_volume_notify.description`:

Description
-----------

This is a helper function which notifies all subscribers about a volume
change event (creation, removal, re-sizing, re-naming, updating). Returns
zero in case of success and a negative error code in case of failure.

.. _`ubi_notify_all`:

ubi_notify_all
==============

.. c:function:: int ubi_notify_all(struct ubi_device *ubi, int ntype, struct notifier_block *nb)

    send a notification to all volumes.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int ntype:
        notification type to send (%UBI_VOLUME_ADDED, etc)

    :param struct notifier_block \*nb:
        the notifier to call

.. _`ubi_notify_all.description`:

Description
-----------

This function walks all volumes of UBI device \ ``ubi``\  and sends the \ ``ntype``\ 
notification for each volume. If \ ``nb``\  is \ ``NULL``\ , then all registered notifiers
are called, otherwise only the \ ``nb``\  notifier is called. Returns the number of
sent notifications.

.. _`ubi_enumerate_volumes`:

ubi_enumerate_volumes
=====================

.. c:function:: int ubi_enumerate_volumes(struct notifier_block *nb)

    send "add" notification for all existing volumes.

    :param struct notifier_block \*nb:
        the notifier to call

.. _`ubi_enumerate_volumes.description`:

Description
-----------

This function walks all UBI devices and volumes and sends the
\ ``UBI_VOLUME_ADDED``\  notification for each volume. If \ ``nb``\  is \ ``NULL``\ , then all
registered notifiers are called, otherwise only the \ ``nb``\  notifier is called.
Returns the number of sent notifications.

.. _`ubi_get_device`:

ubi_get_device
==============

.. c:function:: struct ubi_device *ubi_get_device(int ubi_num)

    get UBI device.

    :param int ubi_num:
        UBI device number

.. _`ubi_get_device.description`:

Description
-----------

This function returns UBI device description object for UBI device number
\ ``ubi_num``\ , or \ ``NULL``\  if the device does not exist. This function increases the
device reference count to prevent removal of the device. In other words, the
device cannot be removed if its reference count is not zero.

.. _`ubi_put_device`:

ubi_put_device
==============

.. c:function:: void ubi_put_device(struct ubi_device *ubi)

    drop an UBI device reference.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`ubi_get_by_major`:

ubi_get_by_major
================

.. c:function:: struct ubi_device *ubi_get_by_major(int major)

    get UBI device by character device major number.

    :param int major:
        major number

.. _`ubi_get_by_major.description`:

Description
-----------

This function is similar to 'ubi_get_device()', but it searches the device
by its major number.

.. _`ubi_major2num`:

ubi_major2num
=============

.. c:function:: int ubi_major2num(int major)

    get UBI device number by character device major number.

    :param int major:
        major number

.. _`ubi_major2num.description`:

Description
-----------

This function searches UBI device number object by its major number. If UBI
device was not found, this function returns -ENODEV, otherwise the UBI device
number is returned.

.. _`kill_volumes`:

kill_volumes
============

.. c:function:: void kill_volumes(struct ubi_device *ubi)

    destroy all user volumes.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`uif_init`:

uif_init
========

.. c:function:: int uif_init(struct ubi_device *ubi)

    initialize user interfaces for an UBI device.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`uif_init.description`:

Description
-----------

This function initializes various user interfaces for an UBI device. If the
initialization fails at an early stage, this function frees all the
resources it allocated, returns an error.

This function returns zero in case of success and a negative error code in
case of failure.

.. _`uif_close`:

uif_close
=========

.. c:function:: void uif_close(struct ubi_device *ubi)

    close user interfaces for an UBI device.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`uif_close.description`:

Description
-----------

Note, since this function un-registers UBI volume device objects (@vol->dev),
the memory allocated voe the volumes is freed as well (in the release
function).

.. _`ubi_free_internal_volumes`:

ubi_free_internal_volumes
=========================

.. c:function:: void ubi_free_internal_volumes(struct ubi_device *ubi)

    free internal volumes.

    :param struct ubi_device \*ubi:
        UBI device description object

.. _`io_init`:

io_init
=======

.. c:function:: int io_init(struct ubi_device *ubi, int max_beb_per1024)

    initialize I/O sub-system for a given UBI device.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int max_beb_per1024:
        maximum expected number of bad PEB per 1024 PEBs

.. _`io_init.description`:

Description
-----------

If \ ``ubi``\ ->vid_hdr_offset or \ ``ubi``\ ->leb_start is zero, default offsets are

.. _`io_init.assumed`:

assumed
-------

o EC header is always at offset zero - this cannot be changed;
o VID header starts just after the EC header at the closest address
aligned to \ ``io``\ ->hdrs_min_io_size;
o data starts just after the VID header at the closest address aligned to
\ ``io``\ ->min_io_size

This function returns zero in case of success and a negative error code in
case of failure.

.. _`autoresize`:

autoresize
==========

.. c:function:: int autoresize(struct ubi_device *ubi, int vol_id)

    re-size the volume which has the "auto-resize" flag set.

    :param struct ubi_device \*ubi:
        UBI device description object

    :param int vol_id:
        ID of the volume to re-size

.. _`autoresize.description`:

Description
-----------

This function re-sizes the volume marked by the \ ``UBI_VTBL_AUTORESIZE_FLG``\  in
the volume table to the largest possible size. See comments in ubi-header.h
for more description of the flag. Returns zero in case of success and a
negative error code in case of failure.

.. _`ubi_attach_mtd_dev`:

ubi_attach_mtd_dev
==================

.. c:function:: int ubi_attach_mtd_dev(struct mtd_info *mtd, int ubi_num, int vid_hdr_offset, int max_beb_per1024)

    attach an MTD device.

    :param struct mtd_info \*mtd:
        MTD device description object

    :param int ubi_num:
        number to assign to the new UBI device

    :param int vid_hdr_offset:
        VID header offset

    :param int max_beb_per1024:
        maximum expected number of bad PEB per 1024 PEBs

.. _`ubi_attach_mtd_dev.description`:

Description
-----------

This function attaches MTD device \ ``mtd_dev``\  to UBI and assign \ ``ubi_num``\  number
to the newly created UBI device, unless \ ``ubi_num``\  is \ ``UBI_DEV_NUM_AUTO``\ , in
which case this function finds a vacant device number and assigns it
automatically. Returns the new UBI device number in case of success and a
negative error code in case of failure.

Note, the invocations of this function has to be serialized by the
\ ``ubi_devices_mutex``\ .

.. _`ubi_detach_mtd_dev`:

ubi_detach_mtd_dev
==================

.. c:function:: int ubi_detach_mtd_dev(int ubi_num, int anyway)

    detach an MTD device.

    :param int ubi_num:
        UBI device number to detach from

    :param int anyway:
        detach MTD even if device reference count is not zero

.. _`ubi_detach_mtd_dev.description`:

Description
-----------

This function destroys an UBI device number \ ``ubi_num``\  and detaches the
underlying MTD device. Returns zero in case of success and \ ``-EBUSY``\  if the
UBI device is busy and cannot be destroyed, and \ ``-EINVAL``\  if it does not
exist.

Note, the invocations of this function has to be serialized by the
\ ``ubi_devices_mutex``\ .

.. _`open_mtd_by_chdev`:

open_mtd_by_chdev
=================

.. c:function:: struct mtd_info *open_mtd_by_chdev(const char *mtd_dev)

    open an MTD device by its character device node path.

    :param const char \*mtd_dev:
        MTD character device node path

.. _`open_mtd_by_chdev.description`:

Description
-----------

This helper function opens an MTD device by its character node device path.
Returns MTD device description object in case of success and a negative
error code in case of failure.

.. _`open_mtd_device`:

open_mtd_device
===============

.. c:function:: struct mtd_info *open_mtd_device(const char *mtd_dev)

    open MTD device by name, character device path, or number.

    :param const char \*mtd_dev:
        name, character device node path, or MTD device device number

.. _`open_mtd_device.description`:

Description
-----------

This function tries to open and MTD device described by \ ``mtd_dev``\  string,
which is first treated as ASCII MTD device number, and if it is not true, it
is treated as MTD device name, and if that is also not true, it is treated
as MTD character device node path. Returns MTD device description object in
case of success and a negative error code in case of failure.

.. _`bytes_str_to_int`:

bytes_str_to_int
================

.. c:function:: int bytes_str_to_int(const char *str)

    convert a number of bytes string into an integer.

    :param const char \*str:
        the string to convert

.. _`bytes_str_to_int.description`:

Description
-----------

This function returns positive resulting integer in case of success and a
negative error code in case of failure.

.. _`ubi_mtd_param_parse`:

ubi_mtd_param_parse
===================

.. c:function:: int ubi_mtd_param_parse(const char *val, struct kernel_param *kp)

    parse the 'mtd=' UBI parameter.

    :param const char \*val:
        the parameter value to parse

    :param struct kernel_param \*kp:
        not used

.. _`ubi_mtd_param_parse.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of error.

.. This file was automatic generated / don't edit.

