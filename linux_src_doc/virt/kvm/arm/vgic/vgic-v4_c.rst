.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-v4.c

.. _`vgic_v4_init`:

vgic_v4_init
============

.. c:function:: int vgic_v4_init(struct kvm *kvm)

    Initialize the GICv4 data structures

    :param struct kvm \*kvm:
        Pointer to the VM being initialized

.. _`vgic_v4_init.description`:

Description
-----------

We may be called each time a vITS is created, or when the
vgic is initialized. This relies on kvm->lock to be
held. In both cases, the number of vcpus should now be
fixed.

.. _`vgic_v4_teardown`:

vgic_v4_teardown
================

.. c:function:: void vgic_v4_teardown(struct kvm *kvm)

    Free the GICv4 data structures

    :param struct kvm \*kvm:
        Pointer to the VM being destroyed

.. _`vgic_v4_teardown.description`:

Description
-----------

Relies on kvm->lock to be held.

.. This file was automatic generated / don't edit.

