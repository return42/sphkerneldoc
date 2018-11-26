.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_actlog.c

.. _`drbd_al_shrink`:

drbd_al_shrink
==============

.. c:function:: void drbd_al_shrink(struct drbd_device *device)

    Removes all active extents form the activity log

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_al_shrink.description`:

Description
-----------

Removes all active extents form the activity log, waiting until
the reference count of each entry dropped to 0 first, of course.

You need to lock device->act_log with \ :c:func:`lc_try_lock`\  / \ :c:func:`lc_unlock`\ 

.. _`drbd_rs_begin_io`:

drbd_rs_begin_io
================

.. c:function:: int drbd_rs_begin_io(struct drbd_device *device, sector_t sector)

    Gets an extent in the resync LRU cache and sets it to BME_LOCKED

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param sector:
        The sector number.
    :type sector: sector_t

.. _`drbd_rs_begin_io.description`:

Description
-----------

This functions sleeps on al_wait. Returns 0 on success, -EINTR if interrupted.

.. _`drbd_try_rs_begin_io`:

drbd_try_rs_begin_io
====================

.. c:function:: int drbd_try_rs_begin_io(struct drbd_device *device, sector_t sector)

    Gets an extent in the resync LRU cache, does not sleep

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param sector:
        The sector number.
    :type sector: sector_t

.. _`drbd_try_rs_begin_io.description`:

Description
-----------

Gets an extent in the resync LRU cache, sets it to BME_NO_WRITES, then
tries to set it to BME_LOCKED. Returns 0 upon success, and -EAGAIN
if there is still application IO going on in this area.

.. _`drbd_rs_cancel_all`:

drbd_rs_cancel_all
==================

.. c:function:: void drbd_rs_cancel_all(struct drbd_device *device)

    Removes all extents from the resync LRU (even BME_LOCKED)

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_rs_del_all`:

drbd_rs_del_all
===============

.. c:function:: int drbd_rs_del_all(struct drbd_device *device)

    Gracefully remove all extents from the resync LRU

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

.. _`drbd_rs_del_all.description`:

Description
-----------

Returns 0 upon success, -EAGAIN if at least one reference count was
not zero.

.. This file was automatic generated / don't edit.

