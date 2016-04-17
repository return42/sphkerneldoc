.. -*- coding: utf-8; mode: rst -*-

==========
omap_drv.c
==========


.. _`dev_load`:

dev_load
========

.. c:function:: int dev_load (struct drm_device *dev, unsigned long flags)

    setup chip and create an initial config

    :param struct drm_device \*dev:
        DRM device

    :param unsigned long flags:
        startup flags



.. _`dev_load.the-driver-load-routine-has-to-do-several-things`:

The driver load routine has to do several things
------------------------------------------------

- initialize the memory manager
- allocate initial config memory
- setup the DRM framebuffer with the allocated memory



.. _`dev_lastclose`:

dev_lastclose
=============

.. c:function:: void dev_lastclose (struct drm_device *dev)

    clean up after all DRM clients have exited

    :param struct drm_device \*dev:
        DRM device



.. _`dev_lastclose.description`:

Description
-----------

Take care of cleaning up after all DRM clients have exited.  In the
mode setting case, we want to restore the kernel's initial mode (just
in case the last client left us in a bad state).

