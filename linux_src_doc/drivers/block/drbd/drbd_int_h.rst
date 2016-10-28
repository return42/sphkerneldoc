.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_int.h

.. _`expect`:

expect
======

.. c:function::  expect( exp)

    Make an assertion

    :param  exp:
        *undescribed*

.. _`expect.description`:

Description
-----------

Unlike the assert macro, this macro returns a boolean result.

.. _`drbd_chk_io_error`:

drbd_chk_io_error
=================

.. c:function::  drbd_chk_io_error( m,  e,  f)

    Handle the on_io_error setting, should be called from all io completion handlers

    :param  m:
        *undescribed*

    :param  e:
        *undescribed*

    :param  f:
        *undescribed*

.. _`drbd_chk_io_error.description`:

Description
-----------

See also drbd_main.c:\ :c:func:`after_state_ch`\  if (os.disk > D_FAILED && ns.disk == D_FAILED)

.. _`drbd_md_first_sector`:

drbd_md_first_sector
====================

.. c:function:: sector_t drbd_md_first_sector(struct drbd_backing_dev *bdev)

    Returns the first sector number of the meta data area

    :param struct drbd_backing_dev \*bdev:
        Meta data block device.

.. _`drbd_md_first_sector.description`:

Description
-----------

BTW, for internal meta data, this happens to be the maximum capacity
we could agree upon with our peer node.

.. _`drbd_md_last_sector`:

drbd_md_last_sector
===================

.. c:function:: sector_t drbd_md_last_sector(struct drbd_backing_dev *bdev)

    Return the last sector number of the meta data area

    :param struct drbd_backing_dev \*bdev:
        Meta data block device.

.. _`drbd_get_max_capacity`:

drbd_get_max_capacity
=====================

.. c:function:: sector_t drbd_get_max_capacity(struct drbd_backing_dev *bdev)

    Returns the capacity we announce to out peer

    :param struct drbd_backing_dev \*bdev:
        Meta data block device.

.. _`drbd_get_max_capacity.description`:

Description
-----------

returns the capacity we announce to out peer.  we clip ourselves at the
various MAX_SECTORS, because if we don't, current implementation will
oops sooner or later

.. _`drbd_md_ss`:

drbd_md_ss
==========

.. c:function:: sector_t drbd_md_ss(struct drbd_backing_dev *bdev)

    Return the sector number of our meta data super block

    :param struct drbd_backing_dev \*bdev:
        Meta data block device.

.. _`get_ldev_if_state`:

get_ldev_if_state
=================

.. c:function::  get_ldev_if_state( _device,  _min_state)

    Increase the ref count on device->ldev. Returns 0 if there is no ldev

    :param  _device:
        DRBD device.

    :param  _min_state:
        Minimum device state required for success.

.. _`get_ldev_if_state.description`:

Description
-----------

You have to call \ :c:func:`put_ldev`\  when finished working with device->ldev.

.. This file was automatic generated / don't edit.

