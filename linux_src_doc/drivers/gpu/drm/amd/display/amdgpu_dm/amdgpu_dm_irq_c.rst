.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_irq.c

.. _`dm_irq_work_func`:

dm_irq_work_func
================

.. c:function:: void dm_irq_work_func(struct work_struct *work)

    Handle an IRQ outside of the interrupt handler proper.

    :param struct work_struct \*work:
        work struct

.. _`remove_irq_handler`:

remove_irq_handler
==================

.. c:function:: struct list_head *remove_irq_handler(struct amdgpu_device *adev, void *ih, const struct dc_interrupt_params *int_params)

    handler was removed.

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param void \*ih:
        *undescribed*

    :param const struct dc_interrupt_params \*int_params:
        *undescribed*

.. _`amdgpu_dm_irq_schedule_work`:

amdgpu_dm_irq_schedule_work
===========================

.. c:function:: void amdgpu_dm_irq_schedule_work(struct amdgpu_device *adev, enum dc_irq_source irq_source)

    schedule all work items registered for the "irq_source".

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param enum dc_irq_source irq_source:
        *undescribed*

.. _`amdgpu_dm_hpd_fini`:

amdgpu_dm_hpd_fini
==================

.. c:function:: void amdgpu_dm_hpd_fini(struct amdgpu_device *adev)

    hpd tear down callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_dm_hpd_fini.description`:

Description
-----------

Tear down the hpd pins used by the card (evergreen+).
Disable the hpd interrupts.

.. This file was automatic generated / don't edit.

