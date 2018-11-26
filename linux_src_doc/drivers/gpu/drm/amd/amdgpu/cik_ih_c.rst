.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/cik_ih.c

.. _`cik_ih_enable_interrupts`:

cik_ih_enable_interrupts
========================

.. c:function:: void cik_ih_enable_interrupts(struct amdgpu_device *adev)

    Enable the interrupt ring buffer

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_enable_interrupts.description`:

Description
-----------

Enable the interrupt ring buffer (CIK).

.. _`cik_ih_disable_interrupts`:

cik_ih_disable_interrupts
=========================

.. c:function:: void cik_ih_disable_interrupts(struct amdgpu_device *adev)

    Disable the interrupt ring buffer

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_disable_interrupts.description`:

Description
-----------

Disable the interrupt ring buffer (CIK).

.. _`cik_ih_irq_init`:

cik_ih_irq_init
===============

.. c:function:: int cik_ih_irq_init(struct amdgpu_device *adev)

    init and enable the interrupt ring

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_irq_init.description`:

Description
-----------

Allocate a ring buffer for the interrupt controller,
enable the RLC, disable interrupts, enable the IH
ring buffer and enable it (CIK).
Called at device load and reume.
Returns 0 for success, errors for failure.

.. _`cik_ih_irq_disable`:

cik_ih_irq_disable
==================

.. c:function:: void cik_ih_irq_disable(struct amdgpu_device *adev)

    disable interrupts

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_irq_disable.description`:

Description
-----------

Disable interrupts on the hw (CIK).

.. _`cik_ih_get_wptr`:

cik_ih_get_wptr
===============

.. c:function:: u32 cik_ih_get_wptr(struct amdgpu_device *adev)

    get the IH ring buffer wptr

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_get_wptr.description`:

Description
-----------

Get the IH ring buffer wptr from either the register
or the writeback memory buffer (CIK).  Also check for
ring buffer overflow and deal with it.
Used by \ :c:func:`cik_irq_process`\ .
Returns the value of the wptr.

.. _`cik_ih_prescreen_iv`:

cik_ih_prescreen_iv
===================

.. c:function:: bool cik_ih_prescreen_iv(struct amdgpu_device *adev)

    prescreen an interrupt vector

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_prescreen_iv.description`:

Description
-----------

Returns true if the interrupt vector should be further processed.

.. _`cik_ih_set_rptr`:

cik_ih_set_rptr
===============

.. c:function:: void cik_ih_set_rptr(struct amdgpu_device *adev)

    set the IH ring buffer rptr

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`cik_ih_set_rptr.description`:

Description
-----------

Set the IH ring buffer rptr.

.. This file was automatic generated / don't edit.

