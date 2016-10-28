.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/kvm/vgic/vgic.h

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

.. This file was automatic generated / don't edit.

