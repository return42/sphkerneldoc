.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic-v2.c

.. _`vgic_v2_probe`:

vgic_v2_probe
=============

.. c:function:: int vgic_v2_probe(const struct gic_kvm_info *gic_kvm_info, const struct vgic_ops **ops, const struct vgic_params **params)

    probe for a GICv2 compatible interrupt controller

    :param const struct gic_kvm_info \*gic_kvm_info:
        pointer to the GIC description

    :param const struct vgic_ops \*\*ops:
        address of a pointer to the GICv2 operations

    :param const struct vgic_params \*\*params:
        address of a pointer to HW-specific parameters

.. _`vgic_v2_probe.description`:

Description
-----------

Returns 0 if a GICv2 has been found, with the low level operations
in \*ops and the HW parameters in \*params. Returns an error code
otherwise.

.. This file was automatic generated / don't edit.

