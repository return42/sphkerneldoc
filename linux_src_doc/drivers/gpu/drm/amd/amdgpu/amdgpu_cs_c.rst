.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_cs.c

.. _`amdgpu_cs_parser_fini`:

amdgpu_cs_parser_fini
=====================

.. c:function:: void amdgpu_cs_parser_fini(struct amdgpu_cs_parser *parser, int error, bool backoff)

    clean parser states

    :param parser:
        parser structure holding parsing context.
    :type parser: struct amdgpu_cs_parser \*

    :param error:
        error number
    :type error: int

    :param backoff:
        *undescribed*
    :type backoff: bool

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

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param data:
        data from userspace
    :type data: void \*

    :param filp:
        file private
    :type filp: struct drm_file \*

.. _`amdgpu_cs_wait_ioctl.description`:

Description
-----------

Wait for the command submission identified by handle to finish.

.. _`amdgpu_cs_get_fence`:

amdgpu_cs_get_fence
===================

.. c:function:: struct dma_fence *amdgpu_cs_get_fence(struct amdgpu_device *adev, struct drm_file *filp, struct drm_amdgpu_fence *user)

    helper to get fence from drm_amdgpu_fence

    :param adev:
        amdgpu device
    :type adev: struct amdgpu_device \*

    :param filp:
        file private
    :type filp: struct drm_file \*

    :param user:
        drm_amdgpu_fence copied from user space
    :type user: struct drm_amdgpu_fence \*

.. _`amdgpu_cs_wait_all_fences`:

amdgpu_cs_wait_all_fences
=========================

.. c:function:: int amdgpu_cs_wait_all_fences(struct amdgpu_device *adev, struct drm_file *filp, union drm_amdgpu_wait_fences *wait, struct drm_amdgpu_fence *fences)

    wait on all fences to signal

    :param adev:
        amdgpu device
    :type adev: struct amdgpu_device \*

    :param filp:
        file private
    :type filp: struct drm_file \*

    :param wait:
        wait parameters
    :type wait: union drm_amdgpu_wait_fences \*

    :param fences:
        array of drm_amdgpu_fence
    :type fences: struct drm_amdgpu_fence \*

.. _`amdgpu_cs_wait_any_fence`:

amdgpu_cs_wait_any_fence
========================

.. c:function:: int amdgpu_cs_wait_any_fence(struct amdgpu_device *adev, struct drm_file *filp, union drm_amdgpu_wait_fences *wait, struct drm_amdgpu_fence *fences)

    wait on any fence to signal

    :param adev:
        amdgpu device
    :type adev: struct amdgpu_device \*

    :param filp:
        file private
    :type filp: struct drm_file \*

    :param wait:
        wait parameters
    :type wait: union drm_amdgpu_wait_fences \*

    :param fences:
        array of drm_amdgpu_fence
    :type fences: struct drm_amdgpu_fence \*

.. _`amdgpu_cs_wait_fences_ioctl`:

amdgpu_cs_wait_fences_ioctl
===========================

.. c:function:: int amdgpu_cs_wait_fences_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

    wait for multiple command submissions to finish

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param data:
        data from userspace
    :type data: void \*

    :param filp:
        file private
    :type filp: struct drm_file \*

.. _`amdgpu_cs_find_mapping`:

amdgpu_cs_find_mapping
======================

.. c:function:: int amdgpu_cs_find_mapping(struct amdgpu_cs_parser *parser, uint64_t addr, struct amdgpu_bo **bo, struct amdgpu_bo_va_mapping **map)

    find bo_va for VM address

    :param parser:
        command submission parser context
    :type parser: struct amdgpu_cs_parser \*

    :param addr:
        VM address
    :type addr: uint64_t

    :param bo:
        resulting BO of the mapping found
    :type bo: struct amdgpu_bo \*\*

    :param map:
        *undescribed*
    :type map: struct amdgpu_bo_va_mapping \*\*

.. _`amdgpu_cs_find_mapping.description`:

Description
-----------

Search the buffer objects in the command submission context for a certain
virtual memory address. Returns allocation structure when found, NULL
otherwise.

.. This file was automatic generated / don't edit.

