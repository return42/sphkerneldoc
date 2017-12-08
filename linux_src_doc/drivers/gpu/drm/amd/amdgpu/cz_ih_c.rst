.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/cz_ih.c

.. _`cz_ih_enable_interrupts`:

cz_ih_enable_interrupts
=======================

.. c:function:: void cz_ih_enable_interrupts(struct amdgpu_device *adev)

    Enable the interrupt ring buffer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_enable_interrupts.description`:

Description
-----------

Enable the interrupt ring buffer (VI).

.. _`cz_ih_disable_interrupts`:

cz_ih_disable_interrupts
========================

.. c:function:: void cz_ih_disable_interrupts(struct amdgpu_device *adev)

    Disable the interrupt ring buffer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_disable_interrupts.description`:

Description
-----------

Disable the interrupt ring buffer (VI).

.. _`cz_ih_irq_init`:

cz_ih_irq_init
==============

.. c:function:: int cz_ih_irq_init(struct amdgpu_device *adev)

    init and enable the interrupt ring

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_irq_init.description`:

Description
-----------

Allocate a ring buffer for the interrupt controller,
enable the RLC, disable interrupts, enable the IH
ring buffer and enable it (VI).
Called at device load and reume.
Returns 0 for success, errors for failure.

.. _`cz_ih_irq_disable`:

cz_ih_irq_disable
=================

.. c:function:: void cz_ih_irq_disable(struct amdgpu_device *adev)

    disable interrupts

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_irq_disable.description`:

Description
-----------

Disable interrupts on the hw (VI).

.. _`cz_ih_get_wptr`:

cz_ih_get_wptr
==============

.. c:function:: u32 cz_ih_get_wptr(struct amdgpu_device *adev)

    get the IH ring buffer wptr

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_get_wptr.description`:

Description
-----------

Get the IH ring buffer wptr from either the register
or the writeback memory buffer (VI).  Also check for
ring buffer overflow and deal with it.
Used by cz_irq_process(VI).
Returns the value of the wptr.

.. _`cz_ih_prescreen_iv`:

cz_ih_prescreen_iv
==================

.. c:function:: bool cz_ih_prescreen_iv(struct amdgpu_device *adev)

    prescreen an interrupt vector

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_prescreen_iv.description`:

Description
-----------

Returns true if the interrupt vector should be further processed.

.. _`cz_ih_decode_iv`:

cz_ih_decode_iv
===============

.. c:function:: void cz_ih_decode_iv(struct amdgpu_device *adev, struct amdgpu_iv_entry *entry)

    decode an interrupt vector

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_iv_entry \*entry:
        *undescribed*

.. _`cz_ih_decode_iv.description`:

Description
-----------

Decodes the interrupt vector at the current rptr
position and also advance the position.

.. _`cz_ih_set_rptr`:

cz_ih_set_rptr
==============

.. c:function:: void cz_ih_set_rptr(struct amdgpu_device *adev)

    set the IH ring buffer rptr

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cz_ih_set_rptr.description`:

Description
-----------

Set the IH ring buffer rptr.

.. This file was automatic generated / don't edit.

