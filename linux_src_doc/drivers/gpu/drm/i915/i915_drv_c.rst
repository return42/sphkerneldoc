.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_drv.c

.. _`i915_driver_init_early`:

i915_driver_init_early
======================

.. c:function:: int i915_driver_init_early(struct drm_i915_private *dev_priv)

    setup state not requiring device access

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

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

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

.. _`i915_driver_init_mmio`:

i915_driver_init_mmio
=====================

.. c:function:: int i915_driver_init_mmio(struct drm_i915_private *dev_priv)

    setup device MMIO

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

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

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

.. _`i915_driver_init_hw`:

i915_driver_init_hw
===================

.. c:function:: int i915_driver_init_hw(struct drm_i915_private *dev_priv)

    setup state requiring device access

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

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

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

.. _`i915_driver_register`:

i915_driver_register
====================

.. c:function:: void i915_driver_register(struct drm_i915_private *dev_priv)

    register the driver with the rest of the system

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

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

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

.. _`i915_driver_load`:

i915_driver_load
================

.. c:function:: int i915_driver_load(struct pci_dev *pdev, const struct pci_device_id *ent)

    setup chip and create an initial config

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param ent:
        matching PCI ID entry
    :type ent: const struct pci_device_id \*

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

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`i915_driver_lastclose.description`:

Description
-----------

Take care of cleaning up after all DRM clients have exited.  In the
mode setting case, we want to restore the kernel's initial mode (just
in case the last client left us in a bad state).

Additionally, in the non-mode setting case, we'll tear down the GTT
and DMA structures, since the kernel won't be using them, and clea
up any GEM state.

.. _`i915_reset`:

i915_reset
==========

.. c:function:: void i915_reset(struct drm_i915_private *i915, unsigned int stalled_mask, const char *reason)

    reset chip after a hang

    :param i915:
        #drm_i915_private to reset
    :type i915: struct drm_i915_private \*

    :param stalled_mask:
        mask of the stalled engines with the guilty requests
    :type stalled_mask: unsigned int

    :param reason:
        user error message for why we are resetting
    :type reason: const char \*

.. _`i915_reset.description`:

Description
-----------

Reset the chip.  Useful if a hang is detected. Marks the device as wedged
on failure.

Caller must hold the struct_mutex.

.. _`i915_reset.procedure-is-fairly-simple`:

Procedure is fairly simple
--------------------------

- reset the chip using the reset reg
- re-init context state
- re-init hardware status page
- re-init ring buffer
- re-init interrupt state
- re-init display

.. _`i915_reset_engine`:

i915_reset_engine
=================

.. c:function:: int i915_reset_engine(struct intel_engine_cs *engine, const char *msg)

    reset GPU engine to recover from a hang

    :param engine:
        engine to reset
    :type engine: struct intel_engine_cs \*

    :param msg:
        reason for GPU reset; or NULL for no \ :c:func:`dev_notice`\ 
    :type msg: const char \*

.. _`i915_reset_engine.description`:

Description
-----------

Reset a specific GPU engine. Useful if a hang is detected.
Returns zero on successful reset or otherwise an error code.

.. _`i915_reset_engine.procedure-is`:

Procedure is
------------

- identifies the request that caused the hang and it is dropped
- reset engine (which will force the engine to idle)
- re-init/configure engine

.. This file was automatic generated / don't edit.

