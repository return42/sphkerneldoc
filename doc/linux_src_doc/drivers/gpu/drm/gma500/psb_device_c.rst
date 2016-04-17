.. -*- coding: utf-8; mode: rst -*-

============
psb_device.c
============


.. _`psb_save_display_registers`:

psb_save_display_registers
==========================

.. c:function:: int psb_save_display_registers (struct drm_device *dev)

    save registers lost on suspend

    :param struct drm_device \*dev:
        our DRM device



.. _`psb_save_display_registers.description`:

Description
-----------

Save the state we need in order to be able to restore the interface
upon resume from suspend



.. _`psb_restore_display_registers`:

psb_restore_display_registers
=============================

.. c:function:: int psb_restore_display_registers (struct drm_device *dev)

    restore lost register state

    :param struct drm_device \*dev:
        our DRM device



.. _`psb_restore_display_registers.description`:

Description
-----------

Restore register state that was lost during suspend and resume.

