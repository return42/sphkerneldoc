.. -*- coding: utf-8; mode: rst -*-

===============
radeon_object.c
===============


.. _`radeon_bo_fence`:

radeon_bo_fence
===============

.. c:function:: void radeon_bo_fence (struct radeon_bo *bo, struct radeon_fence *fence, bool shared)

    add fence to buffer object

    :param struct radeon_bo \*bo:
        buffer object in question

    :param struct radeon_fence \*fence:
        fence to add

    :param bool shared:
        true if fence should be added shared

