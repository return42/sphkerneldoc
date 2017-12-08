.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_irq.h

.. _`amdgpu_dm_irq_init`:

amdgpu_dm_irq_init
==================

.. c:function:: int amdgpu_dm_irq_init(struct amdgpu_device *adev)

    Initialize internal structures of 'amdgpu_dm_irq'.

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_dm_irq_init.description`:

Description
-----------

This function should be called exactly once - during DM initialization.

.. _`amdgpu_dm_irq_init.return`:

Return
------

0 - success
non-zero - error

.. _`amdgpu_dm_irq_fini`:

amdgpu_dm_irq_fini
==================

.. c:function:: void amdgpu_dm_irq_fini(struct amdgpu_device *adev)

    deallocate internal structures of 'amdgpu_dm_irq'.

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_dm_irq_fini.description`:

Description
-----------

This function should be called exactly once - during DM destruction.

.. _`amdgpu_dm_irq_register_interrupt`:

amdgpu_dm_irq_register_interrupt
================================

.. c:function:: void *amdgpu_dm_irq_register_interrupt(struct amdgpu_device *adev, struct dc_interrupt_params *int_params, void (*ih)(void *), void *handler_args)

    register irq handler for Display block.

    :param struct amdgpu_device \*adev:
        AMD DRM device

    :param struct dc_interrupt_params \*int_params:
        parameters for the irq

    :param void (\*ih)(void \*):
        pointer to the irq hander function

    :param void \*handler_args:
        arguments which will be passed to ih

.. _`amdgpu_dm_irq_register_interrupt.return`:

Return
------

IRQ Handler Index on success.
NULL on failure.

Cannot be called from an interrupt handler.

.. _`amdgpu_dm_irq_unregister_interrupt`:

amdgpu_dm_irq_unregister_interrupt
==================================

.. c:function:: void amdgpu_dm_irq_unregister_interrupt(struct amdgpu_device *adev, enum dc_irq_source irq_source, void *ih_index)

    unregister handler which was registered by \ :c:func:`amdgpu_dm_irq_register_interrupt`\ .

    :param struct amdgpu_device \*adev:
        AMD DRM device.

    :param enum dc_irq_source irq_source:
        *undescribed*

    :param void \*ih_index:
        irq handler index which was returned by
        amdgpu_dm_irq_register_interrupt

.. _`amdgpu_dm_irq_suspend`:

amdgpu_dm_irq_suspend
=====================

.. c:function:: int amdgpu_dm_irq_suspend(struct amdgpu_device *adev)

    disable ASIC interrupt during suspend.

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_dm_irq_resume_early`:

amdgpu_dm_irq_resume_early
==========================

.. c:function:: int amdgpu_dm_irq_resume_early(struct amdgpu_device *adev)

    enable HPDRX ASIC interrupts during resume. amdgpu_dm_irq_resume - enable ASIC interrupt during resume.

    :param struct amdgpu_device \*adev:
        *undescribed*

.. This file was automatic generated / don't edit.

