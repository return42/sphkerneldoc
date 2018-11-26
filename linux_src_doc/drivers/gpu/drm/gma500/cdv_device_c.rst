.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/cdv_device.c

.. _`cdv_save_display_registers`:

cdv_save_display_registers
==========================

.. c:function:: int cdv_save_display_registers(struct drm_device *dev)

    save registers lost on suspend

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

.. _`cdv_save_display_registers.description`:

Description
-----------

Save the state we need in order to be able to restore the interface
upon resume from suspend

.. _`cdv_restore_display_registers`:

cdv_restore_display_registers
=============================

.. c:function:: int cdv_restore_display_registers(struct drm_device *dev)

    restore lost register state

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

.. _`cdv_restore_display_registers.description`:

Description
-----------

Restore register state that was lost during suspend and resume.

.. _`cdv_restore_display_registers.fixme`:

FIXME
-----

review

.. This file was automatic generated / don't edit.

