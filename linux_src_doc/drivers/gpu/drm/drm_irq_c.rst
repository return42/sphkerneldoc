.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_irq.c

.. _`irq-helpers`:

irq helpers
===========

The DRM core provides very simple support helpers to enable IRQ handling on a
device through the \ :c:func:`drm_irq_install`\  and \ :c:func:`drm_irq_uninstall`\  functions. This
only supports devices with a single interrupt on the main device stored in
\ :c:type:`drm_device.dev <drm_device>`\  and set as the device paramter in \ :c:func:`drm_dev_alloc`\ .

These IRQ helpers are strictly optional. Drivers which roll their own only
need to set \ :c:type:`drm_device.irq_enabled <drm_device>`\  to signal the DRM core that vblank
interrupts are working. Since these helpers don't automatically clean up the
requested interrupt like e.g. \ :c:func:`devm_request_irq`\  they're not really
recommended.

.. _`drm_irq_install`:

drm_irq_install
===============

.. c:function:: int drm_irq_install(struct drm_device *dev, int irq)

    install IRQ handler

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param irq:
        IRQ number to install the handler for
    :type irq: int

.. _`drm_irq_install.description`:

Description
-----------

Initializes the IRQ related data. Installs the handler, calling the driver
\ :c:type:`drm_driver.irq_preinstall <drm_driver>`\  and \ :c:type:`drm_driver.irq_postinstall <drm_driver>`\  functions before
and after the installation.

This is the simplified helper interface provided for drivers with no special
needs. Drivers which need to install interrupt handlers for multiple
interrupts must instead set \ :c:type:`drm_device.irq_enabled <drm_device>`\  to signal the DRM core
that vblank interrupts are available.

\ ``irq``\  must match the interrupt number that would be passed to \ :c:func:`request_irq`\ ,
if called directly instead of using this helper function.

\ :c:type:`drm_driver.irq_handler <drm_driver>`\  is called to handle the registered interrupt.

.. _`drm_irq_install.return`:

Return
------

Zero on success or a negative error code on failure.

.. _`drm_irq_uninstall`:

drm_irq_uninstall
=================

.. c:function:: int drm_irq_uninstall(struct drm_device *dev)

    uninstall the IRQ handler

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_irq_uninstall.description`:

Description
-----------

Calls the driver's \ :c:type:`drm_driver.irq_uninstall <drm_driver>`\  function and unregisters the IRQ
handler.  This should only be called by drivers which used \ :c:func:`drm_irq_install`\ 
to set up their interrupt handler. Other drivers must only reset
\ :c:type:`drm_device.irq_enabled <drm_device>`\  to false.

Note that for kernel modesetting drivers it is a bug if this function fails.
The sanity checks are only to catch buggy user modesetting drivers which call
the same function through an ioctl.

.. _`drm_irq_uninstall.return`:

Return
------

Zero on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

