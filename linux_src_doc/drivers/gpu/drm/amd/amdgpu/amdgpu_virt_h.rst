.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_virt.h

.. _`amdgpu_virt_ops`:

struct amdgpu_virt_ops
======================

.. c:type:: struct amdgpu_virt_ops

    amdgpu device virt operations

.. _`amdgpu_virt_ops.definition`:

Definition
----------

.. code-block:: c

    struct amdgpu_virt_ops {
        int (*req_full_gpu)(struct amdgpu_device *adev, bool init);
        int (*rel_full_gpu)(struct amdgpu_device *adev, bool init);
        int (*reset_gpu)(struct amdgpu_device *adev);
        int (*wait_reset)(struct amdgpu_device *adev);
        void (*trans_msg)(struct amdgpu_device *adev, u32 req, u32 data1, u32 data2, u32 data3);
    }

.. _`amdgpu_virt_ops.members`:

Members
-------

req_full_gpu
    *undescribed*

rel_full_gpu
    *undescribed*

reset_gpu
    *undescribed*

wait_reset
    *undescribed*

trans_msg
    *undescribed*

.. This file was automatic generated / don't edit.

