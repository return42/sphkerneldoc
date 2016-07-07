.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_bitmap.c

.. _`drbd_bm_mark_for_writeout`:

drbd_bm_mark_for_writeout
=========================

.. c:function:: void drbd_bm_mark_for_writeout(struct drbd_device *device, int page_nr)

    mark a page with a "hint" to be considered for writeout

    :param struct drbd_device \*device:
        DRBD device.

    :param int page_nr:
        the bitmap page to mark with the "hint" flag

.. _`drbd_bm_mark_for_writeout.description`:

Description
-----------

From within an activity log transaction, we mark a few pages with these
hints, then call \ :c:func:`drbd_bm_write_hinted`\ , which will only write out changed
pages which are flagged with this mark.

.. _`drbd_bm_read`:

drbd_bm_read
============

.. c:function:: int drbd_bm_read(struct drbd_device *device)

    Read the whole bitmap from its on disk location.

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_bm_write`:

drbd_bm_write
=============

.. c:function:: int drbd_bm_write(struct drbd_device *device)

    Write the whole bitmap to its on disk location.

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_bm_write.description`:

Description
-----------

Will only write pages that have changed since last IO.

.. _`drbd_bm_write_all`:

drbd_bm_write_all
=================

.. c:function:: int drbd_bm_write_all(struct drbd_device *device)

    Write the whole bitmap to its on disk location.

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_bm_write_all.description`:

Description
-----------

Will write all pages.

.. _`drbd_bm_write_lazy`:

drbd_bm_write_lazy
==================

.. c:function:: int drbd_bm_write_lazy(struct drbd_device *device, unsigned upper_idx)

    Write bitmap pages 0 to \ ``upper_idx``\ -1, if they have changed.

    :param struct drbd_device \*device:
        DRBD device.

    :param unsigned upper_idx:
        0: write all changed pages; +ve: page index to stop scanning for changed pages

.. _`drbd_bm_write_copy_pages`:

drbd_bm_write_copy_pages
========================

.. c:function:: int drbd_bm_write_copy_pages(struct drbd_device *device)

    Write the whole bitmap to its on disk location.

    :param struct drbd_device \*device:
        DRBD device.

.. _`drbd_bm_write_copy_pages.description`:

Description
-----------

Will only write pages that have changed since last IO.
In contrast to \ :c:func:`drbd_bm_write`\ , this will copy the bitmap pages
to temporary writeout pages. It is intended to trigger a full write-out
while still allowing the bitmap to change, for example if a resync or online
verify is aborted due to a failed peer disk, while local IO continues, or
pending resync acks are still being processed.

.. _`drbd_bm_write_hinted`:

drbd_bm_write_hinted
====================

.. c:function:: int drbd_bm_write_hinted(struct drbd_device *device)

    Write bitmap pages with "hint" marks, if they have changed.

    :param struct drbd_device \*device:
        DRBD device.

.. This file was automatic generated / don't edit.

