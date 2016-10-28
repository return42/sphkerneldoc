.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic-v2-emul.c

.. _`vgic_v2_map_resources`:

vgic_v2_map_resources
=====================

.. c:function:: int vgic_v2_map_resources(struct kvm *kvm, const struct vgic_params *params)

    Configure global VGIC state before running any VCPUs

    :param struct kvm \*kvm:
        pointer to the kvm struct

    :param const struct vgic_params \*params:
        *undescribed*

.. _`vgic_v2_map_resources.description`:

Description
-----------

Map the virtual CPU interface into the VM before running any VCPUs.  We
can't do this at creation time, because user space must first set the
virtual CPU interface address in the guest physical address space.

.. This file was automatic generated / don't edit.

