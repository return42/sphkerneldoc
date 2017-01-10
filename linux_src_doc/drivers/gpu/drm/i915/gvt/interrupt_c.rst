.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/interrupt.c

.. _`intel_vgpu_reg_imr_handler`:

intel_vgpu_reg_imr_handler
==========================

.. c:function:: int intel_vgpu_reg_imr_handler(struct intel_vgpu *vgpu, unsigned int reg, void *p_data, unsigned int bytes)

    Generic IMR register emulation write handler

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int reg:
        register offset written by guest

    :param void \*p_data:
        register data written by guest

    :param unsigned int bytes:
        register data length

.. _`intel_vgpu_reg_imr_handler.description`:

Description
-----------

This function is used to emulate the generic IMR register bit change
behavior.

.. _`intel_vgpu_reg_imr_handler.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_reg_master_irq_handler`:

intel_vgpu_reg_master_irq_handler
=================================

.. c:function:: int intel_vgpu_reg_master_irq_handler(struct intel_vgpu *vgpu, unsigned int reg, void *p_data, unsigned int bytes)

    master IRQ write emulation handler

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int reg:
        register offset written by guest

    :param void \*p_data:
        register data written by guest

    :param unsigned int bytes:
        register data length

.. _`intel_vgpu_reg_master_irq_handler.description`:

Description
-----------

This function is used to emulate the master IRQ register on gen8+.

.. _`intel_vgpu_reg_master_irq_handler.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_reg_ier_handler`:

intel_vgpu_reg_ier_handler
==========================

.. c:function:: int intel_vgpu_reg_ier_handler(struct intel_vgpu *vgpu, unsigned int reg, void *p_data, unsigned int bytes)

    Generic IER write emulation handler

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int reg:
        register offset written by guest

    :param void \*p_data:
        register data written by guest

    :param unsigned int bytes:
        register data length

.. _`intel_vgpu_reg_ier_handler.description`:

Description
-----------

This function is used to emulate the generic IER register behavior.

.. _`intel_vgpu_reg_ier_handler.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_reg_iir_handler`:

intel_vgpu_reg_iir_handler
==========================

.. c:function:: int intel_vgpu_reg_iir_handler(struct intel_vgpu *vgpu, unsigned int reg, void *p_data, unsigned int bytes)

    Generic IIR write emulation handler

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int reg:
        register offset written by guest

    :param void \*p_data:
        register data written by guest

    :param unsigned int bytes:
        register data length

.. _`intel_vgpu_reg_iir_handler.description`:

Description
-----------

This function is used to emulate the generic IIR register behavior.

.. _`intel_vgpu_reg_iir_handler.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_trigger_virtual_event`:

intel_vgpu_trigger_virtual_event
================================

.. c:function:: void intel_vgpu_trigger_virtual_event(struct intel_vgpu *vgpu, enum intel_gvt_event_type event)

    Trigger a virtual event for a vGPU

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param enum intel_gvt_event_type event:
        interrupt event

.. _`intel_vgpu_trigger_virtual_event.description`:

Description
-----------

This function is used to trigger a virtual interrupt event for vGPU.
The caller provides the event to be triggered, the framework itself
will emulate the IRQ register bit change.

.. _`intel_gvt_clean_irq`:

intel_gvt_clean_irq
===================

.. c:function:: void intel_gvt_clean_irq(struct intel_gvt *gvt)

    clean up GVT-g IRQ emulation subsystem

    :param struct intel_gvt \*gvt:
        a GVT device

.. _`intel_gvt_clean_irq.description`:

Description
-----------

This function is called at driver unloading stage, to clean up GVT-g IRQ
emulation subsystem.

.. _`intel_gvt_init_irq`:

intel_gvt_init_irq
==================

.. c:function:: int intel_gvt_init_irq(struct intel_gvt *gvt)

    initialize GVT-g IRQ emulation subsystem

    :param struct intel_gvt \*gvt:
        a GVT device

.. _`intel_gvt_init_irq.description`:

Description
-----------

This function is called at driver loading stage, to initialize the GVT-g IRQ
emulation subsystem.

.. _`intel_gvt_init_irq.return`:

Return
------

Zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

