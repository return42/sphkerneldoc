.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_sa.c

.. _`amdgpu_sa_event`:

amdgpu_sa_event
===============

.. c:function:: bool amdgpu_sa_event(struct amdgpu_sa_manager *sa_manager, unsigned size, unsigned align)

    Check if we can stop waiting

    :param sa_manager:
        pointer to the sa_manager
    :type sa_manager: struct amdgpu_sa_manager \*

    :param size:
        number of bytes we want to allocate
    :type size: unsigned

    :param align:
        alignment we need to match
    :type align: unsigned

.. _`amdgpu_sa_event.description`:

Description
-----------

Check if either there is a fence we can wait for or
enough free memory to satisfy the allocation directly

.. This file was automatic generated / don't edit.

