.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-v3.c

.. _`vgic_v3_probe`:

vgic_v3_probe
=============

.. c:function:: int vgic_v3_probe(const struct gic_kvm_info *info)

    probe for a GICv3 compatible interrupt controller in DT

    :param const struct gic_kvm_info \*info:
        *undescribed*

.. _`vgic_v3_probe.description`:

Description
-----------

Returns 0 if a GICv3 has been found, returns an error code otherwise

.. This file was automatic generated / don't edit.

