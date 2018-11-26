.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ib.c

.. _`amdgpu_ib_get`:

amdgpu_ib_get
=============

.. c:function:: int amdgpu_ib_get(struct amdgpu_device *adev, struct amdgpu_vm *vm, unsigned size, struct amdgpu_ib *ib)

    request an IB (Indirect Buffer)

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

    :param vm:
        *undescribed*
    :type vm: struct amdgpu_vm \*

    :param size:
        requested IB size
    :type size: unsigned

    :param ib:
        IB object returned
    :type ib: struct amdgpu_ib \*

.. _`amdgpu_ib_get.description`:

Description
-----------

Request an IB (all asics).  IBs are allocated using the
suballocator.
Returns 0 on success, error on failure.

.. _`amdgpu_ib_free`:

amdgpu_ib_free
==============

.. c:function:: void amdgpu_ib_free(struct amdgpu_device *adev, struct amdgpu_ib *ib, struct dma_fence *f)

    free an IB (Indirect Buffer)

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param ib:
        IB object to free
    :type ib: struct amdgpu_ib \*

    :param f:
        the fence SA bo need wait on for the ib alloation
    :type f: struct dma_fence \*

.. _`amdgpu_ib_free.description`:

Description
-----------

Free an IB (all asics).

.. _`amdgpu_ib_schedule`:

amdgpu_ib_schedule
==================

.. c:function:: int amdgpu_ib_schedule(struct amdgpu_ring *ring, unsigned num_ibs, struct amdgpu_ib *ibs, struct amdgpu_job *job, struct dma_fence **f)

    schedule an IB (Indirect Buffer) on the ring

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

    :param num_ibs:
        number of IBs to schedule
    :type num_ibs: unsigned

    :param ibs:
        IB objects to schedule
    :type ibs: struct amdgpu_ib \*

    :param job:
        *undescribed*
    :type job: struct amdgpu_job \*

    :param f:
        fence created during this submission
    :type f: struct dma_fence \*\*

.. _`amdgpu_ib_schedule.description`:

Description
-----------

Schedule an IB on the associated ring (all asics).
Returns 0 on success, error on failure.

On SI, there are two parallel engines fed from the primary ring,
the CE (Constant Engine) and the DE (Drawing Engine).  Since
resource descriptors have moved to memory, the CE allows you to
prime the caches while the DE is updating register state so that
the resource descriptors will be already in cache when the draw is
processed.  To accomplish this, the userspace driver submits two
IBs, one for the CE and one for the DE.  If there is a CE IB (called
a CONST_IB), it will be put on the ring prior to the DE IB.  Prior
to SI there was just a DE IB.

.. _`amdgpu_ib_pool_init`:

amdgpu_ib_pool_init
===================

.. c:function:: int amdgpu_ib_pool_init(struct amdgpu_device *adev)

    Init the IB (Indirect Buffer) pool

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ib_pool_init.description`:

Description
-----------

Initialize the suballocator to manage a pool of memory
for use as IBs (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_ib_pool_fini`:

amdgpu_ib_pool_fini
===================

.. c:function:: void amdgpu_ib_pool_fini(struct amdgpu_device *adev)

    Free the IB (Indirect Buffer) pool

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ib_pool_fini.description`:

Description
-----------

Tear down the suballocator managing the pool of memory
for use as IBs (all asics).

.. _`amdgpu_ib_ring_tests`:

amdgpu_ib_ring_tests
====================

.. c:function:: int amdgpu_ib_ring_tests(struct amdgpu_device *adev)

    test IBs on the rings

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ib_ring_tests.description`:

Description
-----------

Test an IB (Indirect Buffer) on each ring.
If the test fails, disable the ring.
Returns 0 on success, error if the primary GFX ring
IB test fails.

.. This file was automatic generated / don't edit.

