.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/mga/mga_drv.c

.. _`mga_driver_device_is_agp`:

mga_driver_device_is_agp
========================

.. c:function:: int mga_driver_device_is_agp(struct drm_device *dev)

    :param struct drm_device \*dev:
        *undescribed*

.. _`mga_driver_device_is_agp.description`:

Description
-----------

In addition to the usual tests performed by \c drm_device_is_agp, this
function detects PCI G450 cards that appear to the system exactly like
AGP G450 cards.

\param dev   The device to be tested.

\returns
If the device is a PCI G450, zero is returned.  Otherwise 2 is returned.

.. This file was automatic generated / don't edit.

