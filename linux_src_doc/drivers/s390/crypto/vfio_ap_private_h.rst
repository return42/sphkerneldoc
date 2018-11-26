.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/vfio_ap_private.h

.. _`ap_matrix_mdev`:

struct ap_matrix_mdev
=====================

.. c:type:: struct ap_matrix_mdev

    the mediated matrix device structure

.. _`ap_matrix_mdev.definition`:

Definition
----------

.. code-block:: c

    struct ap_matrix_mdev {
        struct list_head node;
        struct ap_matrix matrix;
        struct notifier_block group_notifier;
        struct kvm *kvm;
    }

.. _`ap_matrix_mdev.members`:

Members
-------

node
    *undescribed*

matrix
    the adapters, usage domains and control domains assigned to the
    mediated matrix device.

group_notifier
    notifier block used for specifying callback function for
    handling the VFIO_GROUP_NOTIFY_SET_KVM event

kvm
    the struct holding guest's state

.. This file was automatic generated / don't edit.

