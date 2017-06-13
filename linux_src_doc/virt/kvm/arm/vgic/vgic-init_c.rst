.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-init.c

.. _`kvm_vgic_early_init`:

kvm_vgic_early_init
===================

.. c:function:: void kvm_vgic_early_init(struct kvm *kvm)

    Initialize static VGIC VCPU data structures

    :param struct kvm \*kvm:
        The VM whose VGIC districutor should be initialized

.. _`kvm_vgic_early_init.description`:

Description
-----------

Only do initialization of static structures that don't require any
allocation or sizing information from userspace.  \ :c:func:`vgic_init`\  called
\ :c:func:`kvm_vgic_dist_init`\  which takes care of the rest.

.. _`kvm_vgic_vcpu_early_init`:

kvm_vgic_vcpu_early_init
========================

.. c:function:: void kvm_vgic_vcpu_early_init(struct kvm_vcpu *vcpu)

    Initialize static VGIC VCPU data structures

    :param struct kvm_vcpu \*vcpu:
        The VCPU whose VGIC data structures whould be initialized

.. _`kvm_vgic_vcpu_early_init.description`:

Description
-----------

Only do initialization, but do not actually enable the VGIC CPU interface
yet.

.. _`kvm_vgic_create`:

kvm_vgic_create
===============

.. c:function:: int kvm_vgic_create(struct kvm *kvm, u32 type)

    triggered by the instantiation of the VGIC device by user space, either through the legacy KVM_CREATE_IRQCHIP ioctl (v2 only) or through the generic KVM_CREATE_DEVICE API ioctl. \ :c:func:`irqchip_in_kernel`\  tells you if this function succeeded or not.

    :param struct kvm \*kvm:
        kvm struct pointer

    :param u32 type:
        KVM_DEV_TYPE_ARM_VGIC_V[23]

.. _`kvm_vgic_dist_init`:

kvm_vgic_dist_init
==================

.. c:function:: int kvm_vgic_dist_init(struct kvm *kvm, unsigned int nr_spis)

    initialize the dist data structures

    :param struct kvm \*kvm:
        kvm struct pointer

    :param unsigned int nr_spis:
        number of spis, frozen by caller

.. _`kvm_vgic_vcpu_init`:

kvm_vgic_vcpu_init
==================

.. c:function:: int kvm_vgic_vcpu_init(struct kvm_vcpu *vcpu)

    Register VCPU-specific KVM iodevs

    :param struct kvm_vcpu \*vcpu:
        pointer to the VCPU being created and initialized

.. _`vgic_lazy_init`:

vgic_lazy_init
==============

.. c:function:: int vgic_lazy_init(struct kvm *kvm)

    Lazy init is only allowed if the GIC exposed to the guest is a GICv2. A GICv3 must be explicitly initialized by the guest using the KVM_DEV_ARM_VGIC_GRP_CTRL KVM_DEVICE group.

    :param struct kvm \*kvm:
        kvm struct pointer

.. _`kvm_vgic_map_resources`:

kvm_vgic_map_resources
======================

.. c:function:: int kvm_vgic_map_resources(struct kvm *kvm)

    called on the first VCPU run. Also map the virtual CPU interface into the VM. v2/v3 derivatives call vgic_init if not already done. \ :c:func:`vgic_ready`\  returns true if this function has succeeded.

    :param struct kvm \*kvm:
        kvm struct pointer

.. _`kvm_vgic_init_cpu_hardware`:

kvm_vgic_init_cpu_hardware
==========================

.. c:function:: void kvm_vgic_init_cpu_hardware( void)

    initialize the GIC VE hardware

    :param  void:
        no arguments

.. _`kvm_vgic_init_cpu_hardware.description`:

Description
-----------

For a specific CPU, initialize the GIC VE hardware.

.. _`kvm_vgic_hyp_init`:

kvm_vgic_hyp_init
=================

.. c:function:: int kvm_vgic_hyp_init( void)

    populates the kvm_vgic_global_state variable according to the host GIC model. Accordingly calls either vgic_v2/v3_probe which registers the KVM_DEVICE that can be instantiated by a guest later on .

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

