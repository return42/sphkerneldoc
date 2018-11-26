.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/nci/core.c

.. _`nci_allocate_device`:

nci_allocate_device
===================

.. c:function:: struct nci_dev *nci_allocate_device(struct nci_ops *ops, __u32 supported_protocols, int tx_headroom, int tx_tailroom)

    allocate a new nci device

    :param ops:
        device operations
    :type ops: struct nci_ops \*

    :param supported_protocols:
        NFC protocols supported by the device
    :type supported_protocols: __u32

    :param tx_headroom:
        *undescribed*
    :type tx_headroom: int

    :param tx_tailroom:
        *undescribed*
    :type tx_tailroom: int

.. _`nci_free_device`:

nci_free_device
===============

.. c:function:: void nci_free_device(struct nci_dev *ndev)

    deallocate nci device

    :param ndev:
        The nci device to deallocate
    :type ndev: struct nci_dev \*

.. _`nci_register_device`:

nci_register_device
===================

.. c:function:: int nci_register_device(struct nci_dev *ndev)

    register a nci device in the nfc subsystem

    :param ndev:
        *undescribed*
    :type ndev: struct nci_dev \*

.. _`nci_unregister_device`:

nci_unregister_device
=====================

.. c:function:: void nci_unregister_device(struct nci_dev *ndev)

    unregister a nci device in the nfc subsystem

    :param ndev:
        *undescribed*
    :type ndev: struct nci_dev \*

.. _`nci_recv_frame`:

nci_recv_frame
==============

.. c:function:: int nci_recv_frame(struct nci_dev *ndev, struct sk_buff *skb)

    receive frame from NCI drivers

    :param ndev:
        The nci device
    :type ndev: struct nci_dev \*

    :param skb:
        The sk_buff to receive
    :type skb: struct sk_buff \*

.. This file was automatic generated / don't edit.

