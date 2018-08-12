.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-mmio-v3.c

.. _`vgic_register_redist_iodev`:

vgic_register_redist_iodev
==========================

.. c:function:: int vgic_register_redist_iodev(struct kvm_vcpu *vcpu)

    register a single redist iodev

    :param struct kvm_vcpu \*vcpu:
        The VCPU to which the redistributor belongs

.. _`vgic_register_redist_iodev.description`:

Description
-----------

Register a KVM iodev for this VCPU's redistributor using the address
provided.

Return 0 on success, -ERRNO otherwise.

.. _`vgic_v3_insert_redist_region`:

vgic_v3_insert_redist_region
============================

.. c:function:: int vgic_v3_insert_redist_region(struct kvm *kvm, uint32_t index, gpa_t base, uint32_t count)

    Insert a new redistributor region

    :param struct kvm \*kvm:
        kvm handle

    :param uint32_t index:
        redist region index

    :param gpa_t base:
        base of the new rdist region

    :param uint32_t count:
        number of redistributors the region is made of (0 in the old style
        single region, whose size is induced from the number of vcpus)

.. _`vgic_v3_insert_redist_region.description`:

Description
-----------

Performs various checks before inserting the rdist region in the list.
Those tests depend on whether the size of the rdist region is known
(ie. count != 0). The list is sorted by rdist region index.

Return 0 on success, < 0 otherwise

.. _`vgic_v3_dispatch_sgi`:

vgic_v3_dispatch_sgi
====================

.. c:function:: void vgic_v3_dispatch_sgi(struct kvm_vcpu *vcpu, u64 reg)

    handle SGI requests from VCPUs

    :param struct kvm_vcpu \*vcpu:
        The VCPU requesting a SGI

    :param u64 reg:
        The value written into the ICC_SGI1R_EL1 register by that VCPU

.. _`vgic_v3_dispatch_sgi.description`:

Description
-----------

With GICv3 (and ARE=1) CPUs trigger SGIs by writing to a system register.
This will trap in sys_regs.c and call this function.
This ICC_SGI1R_EL1 register contains the upper three affinity levels of the
target processors as well as a bitmask of 16 Aff0 CPUs.
If the interrupt routing mode bit is not set, we iterate over all VCPUs to
check for matching ones. If this bit is set, we signal all, but not the
calling VCPU.

.. This file was automatic generated / don't edit.

