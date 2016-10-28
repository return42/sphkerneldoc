.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic.c

.. _`vgic_reg_access`:

vgic_reg_access
===============

.. c:function:: void vgic_reg_access(struct kvm_exit_mmio *mmio, u32 *reg, phys_addr_t offset, int mode)

    access vgic register

    :param struct kvm_exit_mmio \*mmio:
        pointer to the data describing the mmio access

    :param u32 \*reg:
        pointer to the virtual backing of vgic distributor data

    :param phys_addr_t offset:
        least significant 2 bits used for word offset

    :param int mode:
        ACCESS\_ mode (see defines above)

.. _`vgic_reg_access.description`:

Description
-----------

Helper to make vgic register access easier using one of the access
modes defined for vgic register access
(read,raz,write-ignored,setbit,clearbit,write)

.. _`vgic_unqueue_irqs`:

vgic_unqueue_irqs
=================

.. c:function:: void vgic_unqueue_irqs(struct kvm_vcpu *vcpu)

    move pending/active IRQs from LRs to the distributor

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

.. _`vgic_unqueue_irqs.description`:

Description
-----------

Move any IRQs that have already been assigned to LRs back to the
emulated distributor state so that the complete emulated state can be read
from the main emulation structures without investigating the LRs.

.. _`vgic_handle_mmio_access`:

vgic_handle_mmio_access
=======================

.. c:function:: int vgic_handle_mmio_access(struct kvm_vcpu *vcpu, struct kvm_io_device *this, gpa_t addr, int len, void *val, bool is_write)

    handle an in-kernel MMIO access This is called by the read/write KVM IO device wrappers below.

    :param struct kvm_vcpu \*vcpu:
        pointer to the vcpu performing the access

    :param struct kvm_io_device \*this:
        pointer to the KVM IO device in charge

    :param gpa_t addr:
        guest physical address of the access

    :param int len:
        size of the access

    :param void \*val:
        pointer to the data region

    :param bool is_write:
        read or write access

.. _`vgic_handle_mmio_access.description`:

Description
-----------

returns true if the MMIO access could be performed

.. _`vgic_register_kvm_io_dev`:

vgic_register_kvm_io_dev
========================

.. c:function:: int vgic_register_kvm_io_dev(struct kvm *kvm, gpa_t base, int len, const struct vgic_io_range *ranges, int redist_vcpu_id, struct vgic_io_device *iodev)

    register VGIC register frame on the KVM I/O bus

    :param struct kvm \*kvm:
        The VM structure pointer

    :param gpa_t base:
        The (guest) base address for the register frame

    :param int len:
        Length of the register frame window

    :param const struct vgic_io_range \*ranges:
        Describing the handler functions for each register

    :param int redist_vcpu_id:
        The VCPU ID to pass on to the handlers on call

    :param struct vgic_io_device \*iodev:
        Points to memory to be passed on to the handler

.. _`vgic_register_kvm_io_dev.description`:

Description
-----------

\ ``iodev``\  stores the parameters of this function to be usable by the handler
respectively the dispatcher function (since the KVM I/O bus framework lacks
an opaque parameter). Initialization is done in this function, but the
reference should be valid and unique for the whole VGIC lifetime.
If the register frame is not mapped for a specific VCPU, pass -1 to
\ ``redist_vcpu_id``\ .

.. _`kvm_vgic_inject_irq`:

kvm_vgic_inject_irq
===================

.. c:function:: int kvm_vgic_inject_irq(struct kvm *kvm, int cpuid, unsigned int irq_num, bool level)

    Inject an IRQ from a device to the vgic

    :param struct kvm \*kvm:
        The VM structure pointer

    :param int cpuid:
        The CPU for PPIs

    :param unsigned int irq_num:
        The IRQ number that is assigned to the device. This IRQ
        must not be mapped to a HW interrupt.

    :param bool level:
        Edge-triggered:  true:  to trigger the interrupt
        false: to ignore the call
        Level-sensitive  true:  raise the input signal
        false: lower the input signal

.. _`kvm_vgic_inject_irq.description`:

Description
-----------

The GIC is not concerned with devices being active-LOW or active-HIGH for
level-sensitive interrupts.  You can think of the level parameter as 1
being HIGH and 0 being LOW and all devices being active-HIGH.

.. _`kvm_vgic_inject_mapped_irq`:

kvm_vgic_inject_mapped_irq
==========================

.. c:function:: int kvm_vgic_inject_mapped_irq(struct kvm *kvm, int cpuid, unsigned int virt_irq, bool level)

    Inject a physically mapped IRQ to the vgic

    :param struct kvm \*kvm:
        The VM structure pointer

    :param int cpuid:
        The CPU for PPIs

    :param unsigned int virt_irq:
        The virtual IRQ to be injected

    :param bool level:
        Edge-triggered:  true:  to trigger the interrupt
        false: to ignore the call
        Level-sensitive  true:  raise the input signal
        false: lower the input signal

.. _`kvm_vgic_inject_mapped_irq.description`:

Description
-----------

The GIC is not concerned with devices being active-LOW or active-HIGH for
level-sensitive interrupts.  You can think of the level parameter as 1
being HIGH and 0 being LOW and all devices being active-HIGH.

.. _`kvm_vgic_map_phys_irq`:

kvm_vgic_map_phys_irq
=====================

.. c:function:: int kvm_vgic_map_phys_irq(struct kvm_vcpu *vcpu, int virt_irq, int phys_irq)

    map a virtual IRQ to a physical IRQ

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

    :param int virt_irq:
        The virtual IRQ number for the guest

    :param int phys_irq:
        The hardware IRQ number of the host

.. _`kvm_vgic_map_phys_irq.description`:

Description
-----------

Establish a mapping between a guest visible irq (\ ``virt_irq``\ ) and a
hardware irq (\ ``phys_irq``\ ). On injection, \ ``virt_irq``\  will be associated with
the physical interrupt represented by \ ``phys_irq``\ . This mapping can be
established multiple times as long as the parameters are the same.

Returns 0 on success or an error value otherwise.

.. _`kvm_vgic_unmap_phys_irq`:

kvm_vgic_unmap_phys_irq
=======================

.. c:function:: int kvm_vgic_unmap_phys_irq(struct kvm_vcpu *vcpu, unsigned int virt_irq)

    Remove a virtual to physical IRQ mapping

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

    :param unsigned int virt_irq:
        The virtual IRQ number to be unmapped

.. _`kvm_vgic_unmap_phys_irq.description`:

Description
-----------

Remove an existing mapping between virtual and physical interrupts.

.. _`kvm_vgic_vcpu_early_init`:

kvm_vgic_vcpu_early_init
========================

.. c:function:: void kvm_vgic_vcpu_early_init(struct kvm_vcpu *vcpu)

    Earliest possible per-vcpu vgic init stage

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

.. _`kvm_vgic_vcpu_early_init.description`:

Description
-----------

No memory allocation should be performed here, only static init.

.. _`kvm_vgic_get_max_vcpus`:

kvm_vgic_get_max_vcpus
======================

.. c:function:: int kvm_vgic_get_max_vcpus( void)

    Get the maximum number of VCPUs allowed by HW

    :param  void:
        no arguments

.. _`kvm_vgic_get_max_vcpus.description`:

Description
-----------

The host's GIC naturally limits the maximum amount of VCPUs a guest
can use.

.. _`kvm_vgic_early_init`:

kvm_vgic_early_init
===================

.. c:function:: void kvm_vgic_early_init(struct kvm *kvm)

    Earliest possible vgic initialization stage

    :param struct kvm \*kvm:
        *undescribed*

.. _`kvm_vgic_early_init.description`:

Description
-----------

No memory allocation should be performed here, only static init.

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

.. This file was automatic generated / don't edit.

