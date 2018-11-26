.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/vce_v2_0.c

.. _`vce_v2_0_ring_get_rptr`:

vce_v2_0_ring_get_rptr
======================

.. c:function:: uint64_t vce_v2_0_ring_get_rptr(struct amdgpu_ring *ring)

    get read pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`vce_v2_0_ring_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer

.. _`vce_v2_0_ring_get_wptr`:

vce_v2_0_ring_get_wptr
======================

.. c:function:: uint64_t vce_v2_0_ring_get_wptr(struct amdgpu_ring *ring)

    get write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`vce_v2_0_ring_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer

.. _`vce_v2_0_ring_set_wptr`:

vce_v2_0_ring_set_wptr
======================

.. c:function:: void vce_v2_0_ring_set_wptr(struct amdgpu_ring *ring)

    set write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`vce_v2_0_ring_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware

.. _`vce_v2_0_start`:

vce_v2_0_start
==============

.. c:function:: int vce_v2_0_start(struct amdgpu_device *adev)

    start VCE block

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`vce_v2_0_start.description`:

Description
-----------

Setup and start the VCE block

.. This file was automatic generated / don't edit.

