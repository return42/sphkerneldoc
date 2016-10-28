.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i810/i810_dma.c

.. _`i810_driver_device_is_agp`:

i810_driver_device_is_agp
=========================

.. c:function:: int i810_driver_device_is_agp(struct drm_device *dev)

    :param struct drm_device \*dev:
        *undescribed*

.. _`i810_driver_device_is_agp.description`:

Description
-----------

All Intel graphics chipsets are treated as AGP, even if they are really
PCI-e.

\param dev   The device to be tested.

\returns
A value of 1 is always retured to indictate every i810 is AGP.

.. This file was automatic generated / don't edit.

