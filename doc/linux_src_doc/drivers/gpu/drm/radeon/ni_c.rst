.. -*- coding: utf-8; mode: rst -*-

====
ni.c
====


.. _`cayman_get_allowed_info_register`:

cayman_get_allowed_info_register
================================

.. c:function:: int cayman_get_allowed_info_register (struct radeon_device *rdev, u32 reg, u32 *val)

    fetch the register for the info ioctl

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 reg:
        register offset in bytes

    :param u32 \*val:
        register value



.. _`cayman_get_allowed_info_register.description`:

Description
-----------

Returns 0 for success or -EINVAL for an invalid register



.. _`cayman_gfx_is_lockup`:

cayman_gfx_is_lockup
====================

.. c:function:: bool cayman_gfx_is_lockup (struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the GFX engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information



.. _`cayman_gfx_is_lockup.description`:

Description
-----------

Check if the GFX engine is locked up.
Returns true if the engine appears to be locked up, false if not.



.. _`cayman_vm_decode_fault`:

cayman_vm_decode_fault
======================

.. c:function:: void cayman_vm_decode_fault (struct radeon_device *rdev, u32 status, u32 addr)

    print human readable fault info

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 status:
        VM_CONTEXT1_PROTECTION_FAULT_STATUS register value

    :param u32 addr:
        VM_CONTEXT1_PROTECTION_FAULT_ADDR register value



.. _`cayman_vm_decode_fault.description`:

Description
-----------

Print human readable fault information (cayman/TN).



.. _`cayman_vm_flush`:

cayman_vm_flush
===============

.. c:function:: void cayman_vm_flush (struct radeon_device *rdev, struct radeon_ring *ring, unsigned vm_id, uint64_t pd_addr)

    vm flush using the CP

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:

        *undescribed*

    :param unsigned vm_id:

        *undescribed*

    :param uint64_t pd_addr:

        *undescribed*



.. _`cayman_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using the CP (cayman-si).

