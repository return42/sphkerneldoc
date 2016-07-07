.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_drv.c

.. _`i915_reset`:

i915_reset
==========

.. c:function:: int i915_reset(struct drm_i915_private *dev_priv)

    reset chip after a hang

    :param struct drm_i915_private \*dev_priv:
        *undescribed*

.. _`i915_reset.description`:

Description
-----------

Reset the chip.  Useful if a hang is detected. Returns zero on successful
reset or otherwise an error code.

.. _`i915_reset.procedure-is-fairly-simple`:

Procedure is fairly simple
--------------------------

- reset the chip using the reset reg
- re-init context state
- re-init hardware status page
- re-init ring buffer
- re-init interrupt state
- re-init display

.. This file was automatic generated / don't edit.

