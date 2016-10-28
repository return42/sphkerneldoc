.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/si.c

.. _`si_get_allowed_info_register`:

si_get_allowed_info_register
============================

.. c:function:: int si_get_allowed_info_register(struct radeon_device *rdev, u32 reg, u32 *val)

    fetch the register for the info ioctl

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 reg:
        register offset in bytes

    :param u32 \*val:
        register value

.. _`si_get_allowed_info_register.description`:

Description
-----------

Returns 0 for success or -EINVAL for an invalid register

.. _`si_get_xclk`:

si_get_xclk
===========

.. c:function:: u32 si_get_xclk(struct radeon_device *rdev)

    get the xclk

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`si_get_xclk.description`:

Description
-----------

Returns the reference clock used by the gfx engine
(SI).

.. _`si_gfx_is_lockup`:

si_gfx_is_lockup
================

.. c:function:: bool si_gfx_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the GFX engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`si_gfx_is_lockup.description`:

Description
-----------

Check if the GFX engine is locked up.
Returns true if the engine appears to be locked up, false if not.

.. _`si_vm_decode_fault`:

si_vm_decode_fault
==================

.. c:function:: void si_vm_decode_fault(struct radeon_device *rdev, u32 status, u32 addr)

    print human readable fault info

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 status:
        VM_CONTEXT1_PROTECTION_FAULT_STATUS register value

    :param u32 addr:
        VM_CONTEXT1_PROTECTION_FAULT_ADDR register value

.. _`si_vm_decode_fault.description`:

Description
-----------

Print human readable fault information (SI).

.. _`si_get_gpu_clock_counter`:

si_get_gpu_clock_counter
========================

.. c:function:: uint64_t si_get_gpu_clock_counter(struct radeon_device *rdev)

    return GPU clock counter snapshot

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`si_get_gpu_clock_counter.description`:

Description
-----------

Fetches a GPU clock counter snapshot (SI).
Returns the 64 bit clock counter snapshot.

.. This file was automatic generated / don't edit.

