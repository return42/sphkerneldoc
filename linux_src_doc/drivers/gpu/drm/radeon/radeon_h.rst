.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon.h

.. _`radeon_ring_write`:

radeon_ring_write
=================

.. c:function:: void radeon_ring_write(struct radeon_ring *ring, uint32_t v)

    write a value to the ring

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

    :param v:
        dword (dw) value to write
    :type v: uint32_t

.. _`radeon_ring_write.description`:

Description
-----------

Write a value to the requested ring buffer (all asics).

.. This file was automatic generated / don't edit.

