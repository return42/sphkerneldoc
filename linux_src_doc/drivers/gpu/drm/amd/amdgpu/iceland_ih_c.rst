.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/iceland_ih.c

.. _`iceland_ih_enable_interrupts`:

iceland_ih_enable_interrupts
============================

.. c:function:: void iceland_ih_enable_interrupts(struct amdgpu_device *adev)

    Enable the interrupt ring buffer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`iceland_ih_enable_interrupts.description`:

Description
-----------

Enable the interrupt ring buffer (VI).

.. _`iceland_ih_disable_interrupts`:

iceland_ih_disable_interrupts
=============================

.. c:function:: void iceland_ih_disable_interrupts(struct amdgpu_device *adev)

    Disable the interrupt ring buffer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`iceland_ih_disable_interrupts.description`:

Description
-----------

Disable the interrupt ring buffer (VI).

.. _`iceland_ih_irq_init`:

iceland_ih_irq_init
===================

.. c:function:: int iceland_ih_irq_init(struct amdgpu_device *adev)

    init and enable the interrupt ring

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`iceland_ih_irq_init.description`:

Description
-----------

Allocate a ring buffer for the interrupt controller,
enable the RLC, disable interrupts, enable the IH
ring buffer and enable it (VI).
Called at device load and reume.
Returns 0 for success, errors for failure.

.. _`iceland_ih_irq_disable`:

iceland_ih_irq_disable
======================

.. c:function:: void iceland_ih_irq_disable(struct amdgpu_device *adev)

    disable interrupts

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`iceland_ih_irq_disable.description`:

Description
-----------

Disable interrupts on the hw (VI).

.. _`iceland_ih_get_wptr`:

iceland_ih_get_wptr
===================

.. c:function:: u32 iceland_ih_get_wptr(struct amdgpu_device *adev)

    get the IH ring buffer wptr

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`iceland_ih_get_wptr.description`:

Description
-----------

Get the IH ring buffer wptr from either the register
or the writeback memory buffer (VI).  Also check for
ring buffer overflow and deal with it.
Used by cz_irq_process(VI).
Returns the value of the wptr.

.. _`iceland_ih_decode_iv`:

iceland_ih_decode_iv
====================

.. c:function:: void iceland_ih_decode_iv(struct amdgpu_device *adev, struct amdgpu_iv_entry *entry)

    decode an interrupt vector

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_iv_entry \*entry:
        *undescribed*

.. _`iceland_ih_decode_iv.description`:

Description
-----------

Decodes the interrupt vector at the current rptr
position and also advance the position.

.. _`iceland_ih_set_rptr`:

iceland_ih_set_rptr
===================

.. c:function:: void iceland_ih_set_rptr(struct amdgpu_device *adev)

    set the IH ring buffer rptr

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`iceland_ih_set_rptr.description`:

Description
-----------

Set the IH ring buffer rptr.

.. This file was automatic generated / don't edit.

