.. -*- coding: utf-8; mode: rst -*-

===============
amdgpu_object.c
===============


.. _`amdgpu_bo_fence`:

amdgpu_bo_fence
===============

.. c:function:: void amdgpu_bo_fence (struct amdgpu_bo *bo, struct fence *fence, bool shared)

    add fence to buffer object

    :param struct amdgpu_bo \*bo:
        buffer object in question

    :param struct fence \*fence:
        fence to add

    :param bool shared:
        true if fence should be added shared

