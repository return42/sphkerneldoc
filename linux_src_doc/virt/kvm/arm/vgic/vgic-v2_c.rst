.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-v2.c

.. _`vgic_v2_probe`:

vgic_v2_probe
=============

.. c:function:: int vgic_v2_probe(const struct gic_kvm_info *info)

    probe for a GICv2 compatible interrupt controller in DT

    :param const struct gic_kvm_info \*info:
        *undescribed*

.. _`vgic_v2_probe.description`:

Description
-----------

Returns 0 if a GICv2 has been found, returns an error code otherwise

.. This file was automatic generated / don't edit.

