.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nfc/fdp/fdp.c

.. _`fdp_nci_set_data_pkt_counter`:

fdp_nci_set_data_pkt_counter
============================

.. c:function:: void fdp_nci_set_data_pkt_counter(struct nci_dev *ndev, void (*cb)(struct nci_dev *ndev), int count)

    :param struct nci_dev \*ndev:
        *undescribed*

    :param void (\*cb)(struct nci_dev \*ndev):
        *undescribed*

    :param int count:
        *undescribed*

.. _`fdp_nci_set_data_pkt_counter.description`:

Description
-----------

We have no other way of knowing when all firmware packets were sent out
on the i2c bus. We need to know that in order to close the connection and
send the patch end message.

.. _`fdp_nci_send_patch`:

fdp_nci_send_patch
==================

.. c:function:: int fdp_nci_send_patch(struct nci_dev *ndev, u8 conn_id, u8 type)

    have the PBF flag set to 0x0 (last packet) even if the firmware file is segmented and there are multiple packets. If we give the whole firmware to nci_send_data it will segment it and it will set the PBF flag to 0x01 so we need to do the segmentation here.

    :param struct nci_dev \*ndev:
        *undescribed*

    :param u8 conn_id:
        *undescribed*

    :param u8 type:
        *undescribed*

.. _`fdp_nci_send_patch.description`:

Description
-----------

The firmware will be analyzed and applied when we send NCI_OP_PROP_PATCH_CMD
command with NCI_PATCH_TYPE_EOT parameter. The device will send a
NFCC_PATCH_NTF packaet and a NCI_OP_CORE_RESET_NTF packet.

.. This file was automatic generated / don't edit.

