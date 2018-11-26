.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/oaktrail_device.c

.. _`oaktrail_save_display_registers`:

oaktrail_save_display_registers
===============================

.. c:function:: int oaktrail_save_display_registers(struct drm_device *dev)

    save registers lost on suspend

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

.. _`oaktrail_save_display_registers.description`:

Description
-----------

Save the state we need in order to be able to restore the interface
upon resume from suspend

.. _`oaktrail_restore_display_registers`:

oaktrail_restore_display_registers
==================================

.. c:function:: int oaktrail_restore_display_registers(struct drm_device *dev)

    restore lost register state

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

.. _`oaktrail_restore_display_registers.description`:

Description
-----------

Restore register state that was lost during suspend and resume.

.. _`oaktrail_power_down`:

oaktrail_power_down
===================

.. c:function:: int oaktrail_power_down(struct drm_device *dev)

    power down the display island

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

.. _`oaktrail_power_down.description`:

Description
-----------

Power down the display interface of our device

.. This file was automatic generated / don't edit.

