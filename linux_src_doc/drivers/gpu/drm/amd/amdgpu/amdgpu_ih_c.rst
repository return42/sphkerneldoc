.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ih.c

.. _`amdgpu_ih_ring_init`:

amdgpu_ih_ring_init
===================

.. c:function:: int amdgpu_ih_ring_init(struct amdgpu_device *adev, struct amdgpu_ih_ring *ih, unsigned ring_size, bool use_bus_addr)

    initialize the IH state

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param ih:
        ih ring to initialize
    :type ih: struct amdgpu_ih_ring \*

    :param ring_size:
        ring size to allocate
    :type ring_size: unsigned

    :param use_bus_addr:
        true when we can use dma_alloc_coherent
    :type use_bus_addr: bool

.. _`amdgpu_ih_ring_init.description`:

Description
-----------

Initializes the IH state and allocates a buffer
for the IH ring buffer.
Returns 0 for success, errors for failure.

.. _`amdgpu_ih_ring_fini`:

amdgpu_ih_ring_fini
===================

.. c:function:: void amdgpu_ih_ring_fini(struct amdgpu_device *adev, struct amdgpu_ih_ring *ih)

    tear down the IH state

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param ih:
        ih ring to tear down
    :type ih: struct amdgpu_ih_ring \*

.. _`amdgpu_ih_ring_fini.description`:

Description
-----------

Tears down the IH state and frees buffer
used for the IH ring buffer.

.. _`amdgpu_ih_process`:

amdgpu_ih_process
=================

.. c:function:: int amdgpu_ih_process(struct amdgpu_device *adev, struct amdgpu_ih_ring *ih, void (*callback)(struct amdgpu_device *adev, struct amdgpu_ih_ring *ih))

    interrupt handler

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param ih:
        ih ring to process
    :type ih: struct amdgpu_ih_ring \*

    :param void (\*callback)(struct amdgpu_device \*adev, struct amdgpu_ih_ring \*ih):
        *undescribed*

.. _`amdgpu_ih_process.description`:

Description
-----------

Interrupt hander (VI), walk the IH ring.
Returns irq process return code.

.. This file was automatic generated / don't edit.

