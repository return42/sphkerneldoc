.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/display.c

.. _`intel_gvt_check_vblank_emulation`:

intel_gvt_check_vblank_emulation
================================

.. c:function:: void intel_gvt_check_vblank_emulation(struct intel_gvt *gvt)

    check if vblank emulation timer should be turned on/off when a virtual pipe is enabled/disabled.

    :param struct intel_gvt \*gvt:
        a GVT device

.. _`intel_gvt_check_vblank_emulation.description`:

Description
-----------

This function is used to turn on/off vblank timer according to currently
enabled/disabled virtual pipes.

.. _`intel_gvt_emulate_vblank`:

intel_gvt_emulate_vblank
========================

.. c:function:: void intel_gvt_emulate_vblank(struct intel_gvt *gvt)

    trigger vblank events for vGPUs on GVT device

    :param struct intel_gvt \*gvt:
        a GVT device

.. _`intel_gvt_emulate_vblank.description`:

Description
-----------

This function is used to trigger vblank interrupts for vGPUs on GVT device

.. _`intel_vgpu_clean_display`:

intel_vgpu_clean_display
========================

.. c:function:: void intel_vgpu_clean_display(struct intel_vgpu *vgpu)

    clean vGPU virtual display emulation

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_clean_display.description`:

Description
-----------

This function is used to clean vGPU virtual display emulation stuffs

.. _`intel_vgpu_init_display`:

intel_vgpu_init_display
=======================

.. c:function:: int intel_vgpu_init_display(struct intel_vgpu *vgpu, u64 resolution)

    initialize vGPU virtual display emulation

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param u64 resolution:
        *undescribed*

.. _`intel_vgpu_init_display.description`:

Description
-----------

This function is used to initialize vGPU virtual display emulation stuffs

.. _`intel_vgpu_init_display.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_reset_display`:

intel_vgpu_reset_display
========================

.. c:function:: void intel_vgpu_reset_display(struct intel_vgpu *vgpu)

    reset vGPU virtual display emulation

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_reset_display.description`:

Description
-----------

This function is used to reset vGPU virtual display emulation stuffs

.. This file was automatic generated / don't edit.

