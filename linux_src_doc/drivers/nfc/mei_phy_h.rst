.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nfc/mei_phy.h

.. _`nfc_mei_phy`:

struct nfc_mei_phy
==================

.. c:type:: struct nfc_mei_phy


.. _`nfc_mei_phy.definition`:

Definition
----------

.. code-block:: c

    struct nfc_mei_phy {
        struct mei_cl_device *cldev;
        struct nfc_hci_dev *hdev;
        wait_queue_head_t send_wq;
        u8 fw_ivn;
        u8 vendor_id;
        u8 radio_type;
        u8 reserved;
        u16 req_id;
        u16 recv_req_id;
        int powered;
        int hard_fault;
    }

.. _`nfc_mei_phy.members`:

Members
-------

cldev
    mei client device

hdev
    nfc hci device

send_wq
    send completion wait queue

fw_ivn
    NFC Interface Version Number

vendor_id
    NFC manufacturer ID

radio_type
    NFC radio type

reserved
    reserved for alignment

req_id
    message counter

recv_req_id
    reception message counter

powered
    the device is in powered state

hard_fault
    < 0 if hardware error occurred
    and prevents normal operation.

.. This file was automatic generated / don't edit.

