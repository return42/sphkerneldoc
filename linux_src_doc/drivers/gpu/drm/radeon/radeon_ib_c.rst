.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_ib.c

.. _`radeon_ib_get`:

radeon_ib_get
=============

.. c:function:: int radeon_ib_get(struct radeon_device *rdev, int ring, struct radeon_ib *ib, struct radeon_vm *vm, unsigned size)

    request an IB (Indirect Buffer)

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        ring index the IB is associated with
    :type ring: int

    :param ib:
        IB object returned
    :type ib: struct radeon_ib \*

    :param vm:
        *undescribed*
    :type vm: struct radeon_vm \*

    :param size:
        requested IB size
    :type size: unsigned

.. _`radeon_ib_get.description`:

Description
-----------

Request an IB (all asics).  IBs are allocated using the
suballocator.
Returns 0 on success, error on failure.

.. _`radeon_ib_free`:

radeon_ib_free
==============

.. c:function:: void radeon_ib_free(struct radeon_device *rdev, struct radeon_ib *ib)

    free an IB (Indirect Buffer)

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        IB object to free
    :type ib: struct radeon_ib \*

.. _`radeon_ib_free.description`:

Description
-----------

Free an IB (all asics).

.. _`radeon_ib_schedule`:

radeon_ib_schedule
==================

.. c:function:: int radeon_ib_schedule(struct radeon_device *rdev, struct radeon_ib *ib, struct radeon_ib *const_ib, bool hdp_flush)

    schedule an IB (Indirect Buffer) on the ring

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        IB object to schedule
    :type ib: struct radeon_ib \*

    :param const_ib:
        Const IB to schedule (SI only)
    :type const_ib: struct radeon_ib \*

    :param hdp_flush:
        Whether or not to perform an HDP cache flush
    :type hdp_flush: bool

.. _`radeon_ib_schedule.description`:

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

.. _`radeon_ib_pool_init`:

radeon_ib_pool_init
===================

.. c:function:: int radeon_ib_pool_init(struct radeon_device *rdev)

    Init the IB (Indirect Buffer) pool

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_ib_pool_init.description`:

Description
-----------

Initialize the suballocator to manage a pool of memory
for use as IBs (all asics).
Returns 0 on success, error on failure.

.. _`radeon_ib_pool_fini`:

radeon_ib_pool_fini
===================

.. c:function:: void radeon_ib_pool_fini(struct radeon_device *rdev)

    Free the IB (Indirect Buffer) pool

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_ib_pool_fini.description`:

Description
-----------

Tear down the suballocator managing the pool of memory
for use as IBs (all asics).

.. _`radeon_ib_ring_tests`:

radeon_ib_ring_tests
====================

.. c:function:: int radeon_ib_ring_tests(struct radeon_device *rdev)

    test IBs on the rings

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_ib_ring_tests.description`:

Description
-----------

Test an IB (Indirect Buffer) on each ring.
If the test fails, disable the ring.
Returns 0 on success, error if the primary GFX ring
IB test fails.

.. This file was automatic generated / don't edit.

