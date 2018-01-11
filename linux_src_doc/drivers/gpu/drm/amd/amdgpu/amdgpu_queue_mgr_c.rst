.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_queue_mgr.c

.. _`amdgpu_queue_mgr_init`:

amdgpu_queue_mgr_init
=====================

.. c:function:: int amdgpu_queue_mgr_init(struct amdgpu_device *adev, struct amdgpu_queue_mgr *mgr)

    init an amdgpu_queue_mgr struct

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_queue_mgr \*mgr:
        amdgpu_queue_mgr structure holding queue information

.. _`amdgpu_queue_mgr_init.description`:

Description
-----------

Initialize the the selected \ ``mgr``\  (all asics).

Returns 0 on success, error on failure.

.. _`amdgpu_queue_mgr_fini`:

amdgpu_queue_mgr_fini
=====================

.. c:function:: int amdgpu_queue_mgr_fini(struct amdgpu_device *adev, struct amdgpu_queue_mgr *mgr)

    de-initialize an amdgpu_queue_mgr struct

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_queue_mgr \*mgr:
        amdgpu_queue_mgr structure holding queue information

.. _`amdgpu_queue_mgr_fini.description`:

Description
-----------

De-initialize the the selected \ ``mgr``\  (all asics).

Returns 0 on success, error on failure.

.. _`amdgpu_queue_mgr_map`:

amdgpu_queue_mgr_map
====================

.. c:function:: int amdgpu_queue_mgr_map(struct amdgpu_device *adev, struct amdgpu_queue_mgr *mgr, u32 hw_ip, u32 instance, u32 ring, struct amdgpu_ring **out_ring)

    Map a userspace ring id to an amdgpu_ring

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_queue_mgr \*mgr:
        amdgpu_queue_mgr structure holding queue information

    :param u32 hw_ip:
        HW IP enum

    :param u32 instance:
        HW instance

    :param u32 ring:
        user ring id

    :param struct amdgpu_ring \*\*out_ring:
        *undescribed*

.. _`amdgpu_queue_mgr_map.description`:

Description
-----------

Map a userspace ring id to an appropriate kernel ring. Different
policies are configurable at a HW IP level.

Returns 0 on success, error on failure.

.. This file was automatic generated / don't edit.

