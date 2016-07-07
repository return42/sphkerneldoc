.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/nfc/nfc.h

.. _`void`:

void
====

.. c:function:: typedef void(*data_exchange_cb_t)

    Definition of nfc_data_exchange callback

    :param \*data_exchange_cb_t:
        *undescribed*

.. _`void.description`:

Description
-----------

When a rx or tx package is lost or corrupted or the target gets out
of the operating field, err is -EIO.

.. _`nfc_target`:

struct nfc_target
=================

.. c:type:: struct nfc_target

    NFC target descriptiom

.. _`nfc_target.definition`:

Definition
----------

.. code-block:: c

    struct nfc_target {
        u32 idx;
        u32 supported_protocols;
        u16 sens_res;
        u8 sel_res;
        u8 nfcid1_len;
        u8 nfcid1[NFC_NFCID1_MAXSIZE];
        u8 nfcid2_len;
        u8 nfcid2[NFC_NFCID2_MAXSIZE];
        u8 sensb_res_len;
        u8 sensb_res[NFC_SENSB_RES_MAXSIZE];
        u8 sensf_res_len;
        u8 sensf_res[NFC_SENSF_RES_MAXSIZE];
        u8 hci_reader_gate;
        u8 logical_idx;
        u8 is_iso15693;
        u8 iso15693_dsfid;
        u8 iso15693_uid[NFC_ISO15693_UID_MAXSIZE];
    }

.. _`nfc_target.members`:

Members
-------

idx
    *undescribed*

supported_protocols
    *undescribed*

sens_res
    2 bytes describing the target SENS_RES response, if the target
    is a type A one. The \ ``sens_res``\  most significant byte must be byte 2
    as described by the NFC Forum digital specification (i.e. the platform
    configuration one) while \ ``sens_res``\  least significant byte is byte 1.

sel_res
    *undescribed*

nfcid1_len
    *undescribed*

nfcid2_len
    *undescribed*

sensb_res_len
    *undescribed*

sensf_res_len
    *undescribed*

hci_reader_gate
    *undescribed*

logical_idx
    *undescribed*

is_iso15693
    *undescribed*

iso15693_dsfid
    *undescribed*

.. _`nfc_min_aid_length`:

NFC_MIN_AID_LENGTH
==================

.. c:function::  NFC_MIN_AID_LENGTH()

    A struct for NFC secure element event transaction.

.. _`nfc_free_device`:

nfc_free_device
===============

.. c:function:: void nfc_free_device(struct nfc_dev *dev)

    free nfc device

    :param struct nfc_dev \*dev:
        The nfc device to free

.. _`nfc_set_parent_dev`:

nfc_set_parent_dev
==================

.. c:function:: void nfc_set_parent_dev(struct nfc_dev *nfc_dev, struct device *dev)

    set the parent device

    :param struct nfc_dev \*nfc_dev:
        The nfc device whose parent is being set

    :param struct device \*dev:
        The parent device

.. _`nfc_set_drvdata`:

nfc_set_drvdata
===============

.. c:function:: void nfc_set_drvdata(struct nfc_dev *dev, void *data)

    set driver specifc data

    :param struct nfc_dev \*dev:
        The nfc device

    :param void \*data:
        Pointer to driver specifc data

.. _`nfc_get_drvdata`:

nfc_get_drvdata
===============

.. c:function:: void *nfc_get_drvdata(struct nfc_dev *dev)

    get driver specifc data

    :param struct nfc_dev \*dev:
        The nfc device

.. _`nfc_device_name`:

nfc_device_name
===============

.. c:function:: const char *nfc_device_name(struct nfc_dev *dev)

    get the nfc device name

    :param struct nfc_dev \*dev:
        The nfc device whose name to return

.. _`nfc_vendor_cmd_alloc_reply_skb`:

nfc_vendor_cmd_alloc_reply_skb
==============================

.. c:function:: struct sk_buff *nfc_vendor_cmd_alloc_reply_skb(struct nfc_dev *dev, u32 oui, u32 subcmd, int approxlen)

    allocate vendor command reply

    :param struct nfc_dev \*dev:
        nfc device

    :param u32 oui:
        vendor oui

    :param u32 subcmd:
        *undescribed*

    :param int approxlen:
        an upper bound of the length of the data that will
        be put into the skb

.. _`nfc_vendor_cmd_alloc_reply_skb.description`:

Description
-----------

This function allocates and pre-fills an skb for a reply to
a vendor command. Since it is intended for a reply, calling
it outside of a vendor command's \ :c:func:`doit`\  operation is invalid.

The returned skb is pre-filled with some identifying data in
a way that any data that is put into the skb (with \ :c:func:`skb_put`\ ,
\ :c:func:`nla_put`\  or similar) will end up being within the
\ ``NFC_ATTR_VENDOR_DATA``\  attribute, so all that needs to be done
with the skb is adding data for the corresponding userspace tool
which can then read that data out of the vendor data attribute.
You must not modify the skb in any other way.

When done, call \ :c:func:`nfc_vendor_cmd_reply`\  with the skb and return
its error code as the result of the \ :c:func:`doit`\  operation.

.. _`nfc_vendor_cmd_alloc_reply_skb.return`:

Return
------

An allocated and pre-filled skb. \ ``NULL``\  if any errors happen.

.. This file was automatic generated / don't edit.

