.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/if_usb.c

.. _`if_usb_write_bulk_callback`:

if_usb_write_bulk_callback
==========================

.. c:function:: void if_usb_write_bulk_callback(struct urb *urb)

    callback function to handle the status of the URB

    :param urb:
        pointer to \ :c:type:`struct urb <urb>`\  structure
    :type urb: struct urb \*

.. _`if_usb_write_bulk_callback.return`:

Return
------

N/A

.. _`if_usb_free`:

if_usb_free
===========

.. c:function:: void if_usb_free(struct if_usb_card *cardp)

    free tx/rx urb, skb and rx buffer

    :param cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 
    :type cardp: struct if_usb_card \*

.. _`if_usb_free.return`:

Return
------

N/A

.. _`if_usb_probe`:

if_usb_probe
============

.. c:function:: int if_usb_probe(struct usb_interface *intf, const struct usb_device_id *id)

    sets the configuration values

    :param intf:
        \ :c:type:`struct usb_interface <usb_interface>`\  pointer
    :type intf: struct usb_interface \*

    :param id:
        pointer to usb_device_id
    :type id: const struct usb_device_id \*

.. _`if_usb_probe.return`:

Return
------

0 on success, error code on failure

.. _`if_usb_disconnect`:

if_usb_disconnect
=================

.. c:function:: void if_usb_disconnect(struct usb_interface *intf)

    free resource and cleanup

    :param intf:
        USB interface structure
    :type intf: struct usb_interface \*

.. _`if_usb_disconnect.return`:

Return
------

N/A

.. _`if_usb_send_fw_pkt`:

if_usb_send_fw_pkt
==================

.. c:function:: int if_usb_send_fw_pkt(struct if_usb_card *cardp)

    download FW

    :param cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 
    :type cardp: struct if_usb_card \*

.. _`if_usb_send_fw_pkt.return`:

Return
------

0

.. _`usb_tx_block`:

usb_tx_block
============

.. c:function:: int usb_tx_block(struct if_usb_card *cardp, uint8_t *payload, uint16_t nb)

    transfer the data to the device

    :param cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 
    :type cardp: struct if_usb_card \*

    :param payload:
        pointer to payload data
    :type payload: uint8_t \*

    :param nb:
        data length
    :type nb: uint16_t

.. _`usb_tx_block.return`:

Return
------

0 for success or negative error code

.. _`if_usb_receive`:

if_usb_receive
==============

.. c:function:: void if_usb_receive(struct urb *urb)

    read the packet into the upload buffer, wake up the main thread and initialise the Rx callack

    :param urb:
        pointer to \ :c:type:`struct urb <urb>`\ 
    :type urb: struct urb \*

.. _`if_usb_receive.return`:

Return
------

N/A

.. _`if_usb_host_to_card`:

if_usb_host_to_card
===================

.. c:function:: int if_usb_host_to_card(struct lbs_private *priv, uint8_t type, uint8_t *payload, uint16_t nb)

    downloads data to FW

    :param priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure
    :type priv: struct lbs_private \*

    :param type:
        type of data
    :type type: uint8_t

    :param payload:
        pointer to data buffer
    :type payload: uint8_t \*

    :param nb:
        number of bytes
    :type nb: uint16_t

.. _`if_usb_host_to_card.return`:

Return
------

0 for success or negative error code

.. _`if_usb_issue_boot_command`:

if_usb_issue_boot_command
=========================

.. c:function:: int if_usb_issue_boot_command(struct if_usb_card *cardp, int ivalue)

    issues Boot command to the Boot2 code

    :param cardp:
        pointer to \ :c:type:`struct if_usb_card <if_usb_card>`\ 
    :type cardp: struct if_usb_card \*

    :param ivalue:
        1:Boot from FW by USB-Download
        2:Boot from FW in EEPROM
    :type ivalue: int

.. _`if_usb_issue_boot_command.return`:

Return
------

0 for success or negative error code

.. _`check_fwfile_format`:

check_fwfile_format
===================

.. c:function:: int check_fwfile_format(const uint8_t *data, uint32_t totlen)

    check the validity of Boot2/FW image

    :param data:
        pointer to image
    :type data: const uint8_t \*

    :param totlen:
        image length
    :type totlen: uint32_t

.. _`check_fwfile_format.return`:

Return
------

0 (good) or 1 (failure)

.. This file was automatic generated / don't edit.

