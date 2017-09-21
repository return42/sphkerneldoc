.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_v3d.c

.. _`vc4_allocate_bin_bo`:

vc4_allocate_bin_bo
===================

.. c:function:: int vc4_allocate_bin_bo(struct drm_device *drm)

    allocates the memory that will be used for tile binning.

    :param struct drm_device \*drm:
        *undescribed*

.. _`vc4_allocate_bin_bo.description`:

Description
-----------

The binner has a limitation that the addresses in the tile state
buffer that point into the tile alloc buffer or binner overflow
memory only have 28 bits (256MB), and the top 4 on the bus for
tile alloc references end up coming from the tile state buffer's
address.

To work around this, we allocate a single large buffer while V3D is
in use, make sure that it has the top 4 bits constant across its
entire extent, and then put the tile state, tile alloc, and binner
overflow memory inside that buffer.

This creates a limitation where we may not be able to execute a job
if it doesn't fit within the buffer that we allocated up front.
However, it turns out that 16MB is "enough for anybody", and
real-world applications run into allocation failures from the
overall CMA pool before they make scenes complicated enough to run
out of bin space.

.. This file was automatic generated / don't edit.

