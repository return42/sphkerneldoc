.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_cs.c

.. _`amdgpu_cs_parser_fini`:

amdgpu_cs_parser_fini
=====================

.. c:function:: void amdgpu_cs_parser_fini(struct amdgpu_cs_parser *parser, int error, bool backoff)

    clean parser states

    :param struct amdgpu_cs_parser \*parser:
        parser structure holding parsing context.

    :param int error:
        error number

    :param bool backoff:
        *undescribed*

.. _`amdgpu_cs_parser_fini.description`:

Description
-----------

If error is set than unvalidate buffer, otherwise just free memory
used by parsing context.

.. _`amdgpu_cs_wait_ioctl`:

amdgpu_cs_wait_ioctl
====================

.. c:function:: int amdgpu_cs_wait_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

    wait for a command submission to finish

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        data from userspace

    :param struct drm_file \*filp:
        file private

.. _`amdgpu_cs_wait_ioctl.description`:

Description
-----------

Wait for the command submission identified by handle to finish.

.. _`amdgpu_cs_get_fence`:

amdgpu_cs_get_fence
===================

.. c:function:: struct dma_fence *amdgpu_cs_get_fence(struct amdgpu_device *adev, struct drm_file *filp, struct drm_amdgpu_fence *user)

    helper to get fence from drm_amdgpu_fence

    :param struct amdgpu_device \*adev:
        amdgpu device

    :param struct drm_file \*filp:
        file private

    :param struct drm_amdgpu_fence \*user:
        drm_amdgpu_fence copied from user space

.. _`amdgpu_cs_wait_all_fences`:

amdgpu_cs_wait_all_fences
=========================

.. c:function:: int amdgpu_cs_wait_all_fences(struct amdgpu_device *adev, struct drm_file *filp, union drm_amdgpu_wait_fences *wait, struct drm_amdgpu_fence *fences)

    wait on all fences to signal

    :param struct amdgpu_device \*adev:
        amdgpu device

    :param struct drm_file \*filp:
        file private

    :param union drm_amdgpu_wait_fences \*wait:
        wait parameters

    :param struct drm_amdgpu_fence \*fences:
        array of drm_amdgpu_fence

.. _`amdgpu_cs_wait_any_fence`:

amdgpu_cs_wait_any_fence
========================

.. c:function:: int amdgpu_cs_wait_any_fence(struct amdgpu_device *adev, struct drm_file *filp, union drm_amdgpu_wait_fences *wait, struct drm_amdgpu_fence *fences)

    wait on any fence to signal

    :param struct amdgpu_device \*adev:
        amdgpu device

    :param struct drm_file \*filp:
        file private

    :param union drm_amdgpu_wait_fences \*wait:
        wait parameters

    :param struct drm_amdgpu_fence \*fences:
        array of drm_amdgpu_fence

.. _`amdgpu_cs_wait_fences_ioctl`:

amdgpu_cs_wait_fences_ioctl
===========================

.. c:function:: int amdgpu_cs_wait_fences_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

    wait for multiple command submissions to finish

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        data from userspace

    :param struct drm_file \*filp:
        file private

.. _`amdgpu_cs_find_mapping`:

amdgpu_cs_find_mapping
======================

.. c:function:: int amdgpu_cs_find_mapping(struct amdgpu_cs_parser *parser, uint64_t addr, struct amdgpu_bo **bo, struct amdgpu_bo_va_mapping **map)

    find bo_va for VM address

    :param struct amdgpu_cs_parser \*parser:
        command submission parser context

    :param uint64_t addr:
        VM address

    :param struct amdgpu_bo \*\*bo:
        resulting BO of the mapping found

    :param struct amdgpu_bo_va_mapping \*\*map:
        *undescribed*

.. _`amdgpu_cs_find_mapping.description`:

Description
-----------

Search the buffer objects in the command submission context for a certain
virtual memory address. Returns allocation structure when found, NULL
otherwise.

.. This file was automatic generated / don't edit.

