.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ih.c

.. _`amdgpu_ih_ring_alloc`:

amdgpu_ih_ring_alloc
====================

.. c:function:: int amdgpu_ih_ring_alloc(struct amdgpu_device *adev)

    allocate memory for the IH ring

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_ih_ring_alloc.description`:

Description
-----------

Allocate a ring buffer for the interrupt controller.
Returns 0 for success, errors for failure.

.. _`amdgpu_ih_ring_init`:

amdgpu_ih_ring_init
===================

.. c:function:: int amdgpu_ih_ring_init(struct amdgpu_device *adev, unsigned ring_size, bool use_bus_addr)

    initialize the IH state

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param unsigned ring_size:
        *undescribed*

    :param bool use_bus_addr:
        *undescribed*

.. _`amdgpu_ih_ring_init.description`:

Description
-----------

Initializes the IH state and allocates a buffer
for the IH ring buffer.
Returns 0 for success, errors for failure.

.. _`amdgpu_ih_ring_fini`:

amdgpu_ih_ring_fini
===================

.. c:function:: void amdgpu_ih_ring_fini(struct amdgpu_device *adev)

    tear down the IH state

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_ih_ring_fini.description`:

Description
-----------

Tears down the IH state and frees buffer
used for the IH ring buffer.

.. _`amdgpu_ih_process`:

amdgpu_ih_process
=================

.. c:function:: int amdgpu_ih_process(struct amdgpu_device *adev)

    interrupt handler

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_ih_process.description`:

Description
-----------

Interrupt hander (VI), walk the IH ring.
Returns irq process return code.

.. _`amdgpu_ih_add_fault`:

amdgpu_ih_add_fault
===================

.. c:function:: int amdgpu_ih_add_fault(struct amdgpu_device *adev, u64 key)

    Add a page fault record

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param u64 key:
        64-bit encoding of PASID and address

.. _`amdgpu_ih_add_fault.description`:

Description
-----------

This should be called when a retry page fault interrupt is
received. If this is a new page fault, it will be added to a hash
table. The return value indicates whether this is a new fault, or
a fault that was already known and is already being handled.

If there are too many pending page faults, this will fail. Retry
interrupts should be ignored in this case until there is enough
free space.

Returns 0 if the fault was added, 1 if the fault was already known,
-ENOSPC if there are too many pending faults.

.. _`amdgpu_ih_clear_fault`:

amdgpu_ih_clear_fault
=====================

.. c:function:: void amdgpu_ih_clear_fault(struct amdgpu_device *adev, u64 key)

    Remove a page fault record

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param u64 key:
        64-bit encoding of PASID and address

.. _`amdgpu_ih_clear_fault.description`:

Description
-----------

This should be called when a page fault has been handled. Any
future interrupt with this key will be processed as a new
page fault.

.. This file was automatic generated / don't edit.

