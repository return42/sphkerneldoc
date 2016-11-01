.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/kvm/arm_vgic.h

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

.. _`kvm_vgic_setup_default_irq_routing`:

kvm_vgic_setup_default_irq_routing
==================================

.. c:function:: int kvm_vgic_setup_default_irq_routing(struct kvm *kvm)

    Setup a default flat gsi routing table mapping all SPIs

    :param struct kvm \*kvm:
        *undescribed*

.. This file was automatic generated / don't edit.

