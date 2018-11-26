.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_virt.c

.. _`amdgpu_virt_request_full_gpu`:

amdgpu_virt_request_full_gpu
============================

.. c:function:: int amdgpu_virt_request_full_gpu(struct amdgpu_device *adev, bool init)

    request full gpu access

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

    :param init:
        is driver init time.
        When start to init/fini driver, first need to request full gpu access.
    :type init: bool

.. _`amdgpu_virt_request_full_gpu.return`:

Return
------

Zero if request success, otherwise will return error.

.. _`amdgpu_virt_release_full_gpu`:

amdgpu_virt_release_full_gpu
============================

.. c:function:: int amdgpu_virt_release_full_gpu(struct amdgpu_device *adev, bool init)

    release full gpu access

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

    :param init:
        is driver init time.
        When finishing driver init/fini, need to release full gpu access.
    :type init: bool

.. _`amdgpu_virt_release_full_gpu.return`:

Return
------

Zero if release success, otherwise will returen error.

.. _`amdgpu_virt_reset_gpu`:

amdgpu_virt_reset_gpu
=====================

.. c:function:: int amdgpu_virt_reset_gpu(struct amdgpu_device *adev)

    reset gpu

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. _`amdgpu_virt_reset_gpu.return`:

Return
------

Zero if reset success, otherwise will return error.

.. _`amdgpu_virt_wait_reset`:

amdgpu_virt_wait_reset
======================

.. c:function:: int amdgpu_virt_wait_reset(struct amdgpu_device *adev)

    wait for reset gpu completed

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. _`amdgpu_virt_wait_reset.return`:

Return
------

Zero if reset success, otherwise will return error.

.. _`amdgpu_virt_alloc_mm_table`:

amdgpu_virt_alloc_mm_table
==========================

.. c:function:: int amdgpu_virt_alloc_mm_table(struct amdgpu_device *adev)

    alloc memory for mm table

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. _`amdgpu_virt_alloc_mm_table.return`:

Return
------

Zero if allocate success.

.. _`amdgpu_virt_free_mm_table`:

amdgpu_virt_free_mm_table
=========================

.. c:function:: void amdgpu_virt_free_mm_table(struct amdgpu_device *adev)

    free mm table memory

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. This file was automatic generated / don't edit.

