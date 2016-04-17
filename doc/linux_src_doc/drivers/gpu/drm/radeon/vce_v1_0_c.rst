.. -*- coding: utf-8; mode: rst -*-

==========
vce_v1_0.c
==========


.. _`vce_v1_0_get_rptr`:

vce_v1_0_get_rptr
=================

.. c:function:: uint32_t vce_v1_0_get_rptr (struct radeon_device *rdev, struct radeon_ring *ring)

    get read pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`vce_v1_0_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer



.. _`vce_v1_0_get_wptr`:

vce_v1_0_get_wptr
=================

.. c:function:: uint32_t vce_v1_0_get_wptr (struct radeon_device *rdev, struct radeon_ring *ring)

    get write pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`vce_v1_0_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer



.. _`vce_v1_0_set_wptr`:

vce_v1_0_set_wptr
=================

.. c:function:: void vce_v1_0_set_wptr (struct radeon_device *rdev, struct radeon_ring *ring)

    set write pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`vce_v1_0_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware



.. _`vce_v1_0_start`:

vce_v1_0_start
==============

.. c:function:: int vce_v1_0_start (struct radeon_device *rdev)

    start VCE block

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`vce_v1_0_start.description`:

Description
-----------

Setup and start the VCE block

