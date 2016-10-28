.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_nl.c

.. _`drbd_determine_dev_size`:

drbd_determine_dev_size
=======================

.. c:function:: enum determine_dev_size drbd_determine_dev_size(struct drbd_device *device, enum dds_flags flags, struct resize_parms *rs)

    Sets the right device size obeying all constraints

    :param struct drbd_device \*device:
        DRBD device.

    :param enum dds_flags flags:
        *undescribed*

    :param struct resize_parms \*rs:
        *undescribed*

.. _`drbd_determine_dev_size.description`:

Description
-----------

Returns 0 on success, negative return values indicate errors.
You should call \ :c:func:`drbd_md_sync`\  after calling this function.

.. _`drbd_check_al_size`:

drbd_check_al_size
==================

.. c:function:: int drbd_check_al_size(struct drbd_device *device, struct disk_conf *dc)

    Ensures that the AL is of the right size

    :param struct drbd_device \*device:
        DRBD device.

    :param struct disk_conf \*dc:
        *undescribed*

.. _`drbd_check_al_size.description`:

Description
-----------

Returns -EBUSY if current al lru is still used, -ENOMEM when allocation
failed, and 0 on success. You should call \ :c:func:`drbd_md_sync`\  after you called
this function.

.. This file was automatic generated / don't edit.

