.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_bo.c

.. _`v3d-gem-bo-management-support`:

V3D GEM BO management support
=============================

Compared to VC4 (V3D 2.x), V3D 3.3 introduces an MMU between the
GPU and the bus, allowing us to use shmem objects for our storage
instead of CMA.

Physically contiguous objects may still be imported to V3D, but the
driver doesn't allocate physically contiguous objects on its own.
Display engines requiring physically contiguous allocations should
look into Mesa's "renderonly" support (as used by the Mesa pl111
driver) for an example of how to integrate with V3D.

Long term, we should support evicting pages from the MMU when under
memory pressure (thus the \ :c:func:`v3d_bo_get_pages`\  refcounting), but
that's not a high priority since our systems tend to not have swap.

.. This file was automatic generated / don't edit.

