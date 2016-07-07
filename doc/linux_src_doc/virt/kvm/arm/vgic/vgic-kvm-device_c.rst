.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-kvm-device.c

.. _`kvm_vgic_addr`:

kvm_vgic_addr
=============

.. c:function:: int kvm_vgic_addr(struct kvm *kvm, unsigned long type, u64 *addr, bool write)

    set or get vgic VM base addresses

    :param struct kvm \*kvm:
        pointer to the vm struct

    :param unsigned long type:
        the VGIC addr type, one of KVM_VGIC_V[23]_ADDR_TYPE_XXX

    :param u64 \*addr:
        pointer to address value

    :param bool write:
        if true set the address in the VM address space, if false read the
        address

.. _`kvm_vgic_addr.description`:

Description
-----------

Set or get the vgic base addresses for the distributor and the virtual CPU
interface in the VM physical address space.  These addresses are properties
of the emulated core/SoC and therefore user space initially knows this
information.
Check them for sanity (alignment, double assignment). We can't check for
overlapping regions in case of a virtual GICv3 here, since we don't know
the number of VCPUs yet, so we defer this check to \ :c:func:`map_resources`\ .

.. This file was automatic generated / don't edit.

