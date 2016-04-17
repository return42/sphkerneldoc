.. -*- coding: utf-8; mode: rst -*-

==========
i915_dma.c
==========


.. _`i915_driver_load`:

i915_driver_load
================

.. c:function:: int i915_driver_load (struct drm_device *dev, unsigned long flags)

    setup chip and create an initial config

    :param struct drm_device \*dev:
        DRM device

    :param unsigned long flags:
        startup flags



.. _`i915_driver_load.the-driver-load-routine-has-to-do-several-things`:

The driver load routine has to do several things
------------------------------------------------

- drive output discovery via :c:func:`intel_modeset_init`
- initialize the memory manager
- allocate initial config memory
- setup the DRM framebuffer with the allocated memory



.. _`i915_driver_lastclose`:

i915_driver_lastclose
=====================

.. c:function:: void i915_driver_lastclose (struct drm_device *dev)

    clean up after all DRM clients have exited

    :param struct drm_device \*dev:
        DRM device



.. _`i915_driver_lastclose.description`:

Description
-----------

Take care of cleaning up after all DRM clients have exited.  In the
mode setting case, we want to restore the kernel's initial mode (just
in case the last client left us in a bad state).

Additionally, in the non-mode setting case, we'll tear down the GTT
and DMA structures, since the kernel won't be using them, and clea
up any GEM state.

