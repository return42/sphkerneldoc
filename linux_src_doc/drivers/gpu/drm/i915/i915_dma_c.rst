.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_dma.c

.. _`i915_driver_init_early`:

i915_driver_init_early
======================

.. c:function:: int i915_driver_init_early(struct drm_i915_private *dev_priv, struct drm_device *dev, struct intel_device_info *info)

    setup state not requiring device access

    :param struct drm_i915_private \*dev_priv:
        device private

    :param struct drm_device \*dev:
        *undescribed*

    :param struct intel_device_info \*info:
        *undescribed*

.. _`i915_driver_init_early.description`:

Description
-----------

Initialize everything that is a "SW-only" state, that is state not
requiring accessing the device or exposing the driver via kernel internal
or userspace interfaces. Example steps belonging here: lock initialization,
system memory allocation, setting up device specific attributes and
function hooks not requiring accessing the device.

.. _`i915_driver_cleanup_early`:

i915_driver_cleanup_early
=========================

.. c:function:: void i915_driver_cleanup_early(struct drm_i915_private *dev_priv)

    cleanup the setup done in \ :c:func:`i915_driver_init_early`\ 

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_init_mmio`:

i915_driver_init_mmio
=====================

.. c:function:: int i915_driver_init_mmio(struct drm_i915_private *dev_priv)

    setup device MMIO

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_init_mmio.description`:

Description
-----------

Setup minimal device state necessary for MMIO accesses later in the
initialization sequence. The setup here should avoid any other device-wide
side effects or exposing the driver via kernel internal or user space
interfaces.

.. _`i915_driver_cleanup_mmio`:

i915_driver_cleanup_mmio
========================

.. c:function:: void i915_driver_cleanup_mmio(struct drm_i915_private *dev_priv)

    cleanup the setup done in \ :c:func:`i915_driver_init_mmio`\ 

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_init_hw`:

i915_driver_init_hw
===================

.. c:function:: int i915_driver_init_hw(struct drm_i915_private *dev_priv)

    setup state requiring device access

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_init_hw.description`:

Description
-----------

Setup state that requires accessing the device, but doesn't require
exposing the driver via kernel internal or userspace interfaces.

.. _`i915_driver_cleanup_hw`:

i915_driver_cleanup_hw
======================

.. c:function:: void i915_driver_cleanup_hw(struct drm_i915_private *dev_priv)

    cleanup the setup done in \ :c:func:`i915_driver_init_hw`\ 

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_register`:

i915_driver_register
====================

.. c:function:: void i915_driver_register(struct drm_i915_private *dev_priv)

    register the driver with the rest of the system

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_register.description`:

Description
-----------

Perform any steps necessary to make the driver available via kernel
internal or userspace interfaces.

.. _`i915_driver_unregister`:

i915_driver_unregister
======================

.. c:function:: void i915_driver_unregister(struct drm_i915_private *dev_priv)

    cleanup the registration done in \ :c:func:`i915_driver_regiser`\ 

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_driver_load`:

i915_driver_load
================

.. c:function:: int i915_driver_load(struct drm_device *dev, unsigned long flags)

    setup chip and create an initial config

    :param struct drm_device \*dev:
        DRM device

    :param unsigned long flags:
        startup flags

.. _`i915_driver_load.the-driver-load-routine-has-to-do-several-things`:

The driver load routine has to do several things
------------------------------------------------

- drive output discovery via \ :c:func:`intel_modeset_init`\ 
- initialize the memory manager
- allocate initial config memory
- setup the DRM framebuffer with the allocated memory

.. _`i915_driver_lastclose`:

i915_driver_lastclose
=====================

.. c:function:: void i915_driver_lastclose(struct drm_device *dev)

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

.. This file was automatic generated / don't edit.

