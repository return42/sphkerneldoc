.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/vega10_ih.c

.. _`vega10_ih_enable_interrupts`:

vega10_ih_enable_interrupts
===========================

.. c:function:: void vega10_ih_enable_interrupts(struct amdgpu_device *adev)

    Enable the interrupt ring buffer

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_enable_interrupts.description`:

Description
-----------

Enable the interrupt ring buffer (VEGA10).

.. _`vega10_ih_disable_interrupts`:

vega10_ih_disable_interrupts
============================

.. c:function:: void vega10_ih_disable_interrupts(struct amdgpu_device *adev)

    Disable the interrupt ring buffer

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_disable_interrupts.description`:

Description
-----------

Disable the interrupt ring buffer (VEGA10).

.. _`vega10_ih_irq_init`:

vega10_ih_irq_init
==================

.. c:function:: int vega10_ih_irq_init(struct amdgpu_device *adev)

    init and enable the interrupt ring

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_irq_init.description`:

Description
-----------

Allocate a ring buffer for the interrupt controller,
enable the RLC, disable interrupts, enable the IH
ring buffer and enable it (VI).
Called at device load and reume.
Returns 0 for success, errors for failure.

.. _`vega10_ih_irq_disable`:

vega10_ih_irq_disable
=====================

.. c:function:: void vega10_ih_irq_disable(struct amdgpu_device *adev)

    disable interrupts

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_irq_disable.description`:

Description
-----------

Disable interrupts on the hw (VEGA10).

.. _`vega10_ih_get_wptr`:

vega10_ih_get_wptr
==================

.. c:function:: u32 vega10_ih_get_wptr(struct amdgpu_device *adev)

    get the IH ring buffer wptr

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_get_wptr.description`:

Description
-----------

Get the IH ring buffer wptr from either the register
or the writeback memory buffer (VEGA10).  Also check for
ring buffer overflow and deal with it.
Returns the value of the wptr.

.. _`vega10_ih_prescreen_iv`:

vega10_ih_prescreen_iv
======================

.. c:function:: bool vega10_ih_prescreen_iv(struct amdgpu_device *adev)

    prescreen an interrupt vector

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_prescreen_iv.description`:

Description
-----------

Returns true if the interrupt vector should be further processed.

.. _`vega10_ih_decode_iv`:

vega10_ih_decode_iv
===================

.. c:function:: void vega10_ih_decode_iv(struct amdgpu_device *adev, struct amdgpu_iv_entry *entry)

    decode an interrupt vector

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param entry:
        *undescribed*
    :type entry: struct amdgpu_iv_entry \*

.. _`vega10_ih_decode_iv.description`:

Description
-----------

Decodes the interrupt vector at the current rptr
position and also advance the position.

.. _`vega10_ih_set_rptr`:

vega10_ih_set_rptr
==================

.. c:function:: void vega10_ih_set_rptr(struct amdgpu_device *adev)

    set the IH ring buffer rptr

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vega10_ih_set_rptr.description`:

Description
-----------

Set the IH ring buffer rptr.

.. This file was automatic generated / don't edit.

