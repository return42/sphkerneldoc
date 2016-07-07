.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/nci/core.c

.. _`nci_allocate_device`:

nci_allocate_device
===================

.. c:function:: struct nci_dev *nci_allocate_device(struct nci_ops *ops, __u32 supported_protocols, int tx_headroom, int tx_tailroom)

    allocate a new nci device

    :param struct nci_ops \*ops:
        device operations

    :param __u32 supported_protocols:
        NFC protocols supported by the device

    :param int tx_headroom:
        *undescribed*

    :param int tx_tailroom:
        *undescribed*

.. _`nci_free_device`:

nci_free_device
===============

.. c:function:: void nci_free_device(struct nci_dev *ndev)

    deallocate nci device

    :param struct nci_dev \*ndev:
        The nci device to deallocate

.. _`nci_register_device`:

nci_register_device
===================

.. c:function:: int nci_register_device(struct nci_dev *ndev)

    register a nci device in the nfc subsystem

    :param struct nci_dev \*ndev:
        *undescribed*

.. _`nci_unregister_device`:

nci_unregister_device
=====================

.. c:function:: void nci_unregister_device(struct nci_dev *ndev)

    unregister a nci device in the nfc subsystem

    :param struct nci_dev \*ndev:
        *undescribed*

.. _`nci_recv_frame`:

nci_recv_frame
==============

.. c:function:: int nci_recv_frame(struct nci_dev *ndev, struct sk_buff *skb)

    receive frame from NCI drivers

    :param struct nci_dev \*ndev:
        The nci device

    :param struct sk_buff \*skb:
        The sk_buff to receive

.. This file was automatic generated / don't edit.

