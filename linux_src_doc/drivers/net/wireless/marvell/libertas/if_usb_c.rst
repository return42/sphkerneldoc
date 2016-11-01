.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/if_usb.c

.. _`if_usb_write_bulk_callback`:

if_usb_write_bulk_callback
==========================

.. c:function:: void if_usb_write_bulk_callback(struct urb *urb)

    callback function to handle the status of the URB

    :param struct urb \*urb:
        pointer to \ :c:type:`struct urb <urb>`\  structure

.. _`if_usb_write_bulk_callback.return`:

Return
------

N/A

.. _`if_usb_free`:

if_usb_free
===========

.. c:function:: void if_usb_free(struct if_usb_card *cardp)

    free tx/rx urb, skb and rx buffer

    :param struct if_usb_card \*cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 

.. _`if_usb_free.return`:

Return
------

N/A

.. _`if_usb_probe`:

if_usb_probe
============

.. c:function:: int if_usb_probe(struct usb_interface *intf, const struct usb_device_id *id)

    sets the configuration values

    :param struct usb_interface \*intf:
        &usb_interface pointer

    :param const struct usb_device_id \*id:
        pointer to usb_device_id

.. _`if_usb_probe.return`:

Return
------

0 on success, error code on failure

.. _`if_usb_disconnect`:

if_usb_disconnect
=================

.. c:function:: void if_usb_disconnect(struct usb_interface *intf)

    free resource and cleanup

    :param struct usb_interface \*intf:
        USB interface structure

.. _`if_usb_disconnect.return`:

Return
------

N/A

.. _`if_usb_send_fw_pkt`:

if_usb_send_fw_pkt
==================

.. c:function:: int if_usb_send_fw_pkt(struct if_usb_card *cardp)

    download FW

    :param struct if_usb_card \*cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 

.. _`if_usb_send_fw_pkt.return`:

Return
------

0

.. _`usb_tx_block`:

usb_tx_block
============

.. c:function:: int usb_tx_block(struct if_usb_card *cardp, uint8_t *payload, uint16_t nb)

    transfer the data to the device

    :param struct if_usb_card \*cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 

    :param uint8_t \*payload:
        pointer to payload data

    :param uint16_t nb:
        data length

.. _`usb_tx_block.return`:

Return
------

0 for success or negative error code

.. _`if_usb_receive`:

if_usb_receive
==============

.. c:function:: void if_usb_receive(struct urb *urb)

    read the packet into the upload buffer, wake up the main thread and initialise the Rx callack

    :param struct urb \*urb:
        pointer to \ :c:type:`struct urb <urb>`\ 

.. _`if_usb_receive.return`:

Return
------

N/A

.. _`if_usb_host_to_card`:

if_usb_host_to_card
===================

.. c:function:: int if_usb_host_to_card(struct lbs_private *priv, uint8_t type, uint8_t *payload, uint16_t nb)

    downloads data to FW

    :param struct lbs_private \*priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param uint8_t type:
        type of data

    :param uint8_t \*payload:
        pointer to data buffer

    :param uint16_t nb:
        number of bytes

.. _`if_usb_host_to_card.return`:

Return
------

0 for success or negative error code

.. _`if_usb_issue_boot_command`:

if_usb_issue_boot_command
=========================

.. c:function:: int if_usb_issue_boot_command(struct if_usb_card *cardp, int ivalue)

    issues Boot command to the Boot2 code

    :param struct if_usb_card \*cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 

    :param int ivalue:
        1:Boot from FW by USB-Download
        2:Boot from FW in EEPROM

.. _`if_usb_issue_boot_command.return`:

Return
------

0 for success or negative error code

.. _`check_fwfile_format`:

check_fwfile_format
===================

.. c:function:: int check_fwfile_format(const uint8_t *data, uint32_t totlen)

    check the validity of Boot2/FW image

    :param const uint8_t \*data:
        pointer to image

    :param uint32_t totlen:
        image length

.. _`check_fwfile_format.return`:

Return
------

0 (good) or 1 (failure)

.. This file was automatic generated / don't edit.

