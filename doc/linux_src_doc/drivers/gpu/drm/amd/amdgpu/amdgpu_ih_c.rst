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

.. This file was automatic generated / don't edit.

