.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gfx_v6_0.c

.. _`gfx_v6_0_ring_test_ib`:

gfx_v6_0_ring_test_ib
=====================

.. c:function:: int gfx_v6_0_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    basic ring IB test

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

    :param timeout:
        *undescribed*
    :type timeout: long

.. _`gfx_v6_0_ring_test_ib.description`:

Description
-----------

Allocate an IB and execute it on the gfx ring (SI).
Provides a basic gfx ring test to verify that IBs are working.
Returns 0 on success, error on failure.

.. This file was automatic generated / don't edit.

