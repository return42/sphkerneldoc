.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-kvm-device.c

.. _`kvm_vgic_addr`:

kvm_vgic_addr
=============

.. c:function:: int kvm_vgic_addr(struct kvm *kvm, unsigned long type, u64 *addr, bool write)

    set or get vgic VM base addresses

    :param kvm:
        pointer to the vm struct
    :type kvm: struct kvm \*

    :param type:
        the VGIC addr type, one of KVM_VGIC_V[23]_ADDR_TYPE_XXX
    :type type: unsigned long

    :param addr:
        pointer to address value
    :type addr: u64 \*

    :param write:
        if true set the address in the VM address space, if false read the
        address
    :type write: bool

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

.. _`vgic_v2_attr_regs_access`:

vgic_v2_attr_regs_access
========================

.. c:function:: int vgic_v2_attr_regs_access(struct kvm_device *dev, struct kvm_device_attr *attr, u32 *reg, bool is_write)

    allows user space to access VGIC v2 state

    :param dev:
        kvm device handle
    :type dev: struct kvm_device \*

    :param attr:
        kvm device attribute
    :type attr: struct kvm_device_attr \*

    :param reg:
        address the value is read or written
    :type reg: u32 \*

    :param is_write:
        true if userspace is writing a register
    :type is_write: bool

.. This file was automatic generated / don't edit.

