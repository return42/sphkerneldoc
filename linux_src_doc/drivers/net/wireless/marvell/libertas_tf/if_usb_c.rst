.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas_tf/if_usb.c

.. _`if_usb_write_bulk_callback`:

if_usb_write_bulk_callback
==========================

.. c:function:: void if_usb_write_bulk_callback(struct urb *urb)

    call back to handle URB status

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`if_usb_write_bulk_callback.description`:

Description
-----------

\ ``param``\  urb          pointer to urb structure

.. _`if_usb_free`:

if_usb_free
===========

.. c:function:: void if_usb_free(struct if_usb_card *cardp)

    free tx/rx urb, skb and rx buffer

    :param cardp:
        *undescribed*
    :type cardp: struct if_usb_card \*

.. _`if_usb_free.description`:

Description
-----------

\ ``param``\  cardp        pointer if_usb_card

.. _`if_usb_probe`:

if_usb_probe
============

.. c:function:: int if_usb_probe(struct usb_interface *intf, const struct usb_device_id *id)

    sets the configuration values

    :param intf:
        *undescribed*
    :type intf: struct usb_interface \*

    :param id:
        *undescribed*
    :type id: const struct usb_device_id \*

.. _`if_usb_probe.description`:

Description
-----------

\ ``ifnum``\       interface number
\ ``id``\          pointer to usb_device_id

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
        *undescribed*
    :type intf: struct usb_interface \*

.. _`if_usb_disconnect.description`:

Description
-----------

\ ``intf``\        USB interface structure

.. _`if_usb_send_fw_pkt`:

if_usb_send_fw_pkt
==================

.. c:function:: int if_usb_send_fw_pkt(struct if_usb_card *cardp)

    This function downloads the FW

    :param cardp:
        *undescribed*
    :type cardp: struct if_usb_card \*

.. _`if_usb_send_fw_pkt.description`:

Description
-----------

\ ``priv``\        pointer to struct lbtf_private

.. _`if_usb_send_fw_pkt.return`:

Return
------

0

.. _`usb_tx_block`:

usb_tx_block
============

.. c:function:: int usb_tx_block(struct if_usb_card *cardp, uint8_t *payload, uint16_t nb, u8 data)

    transfer data to the device

    :param cardp:
        *undescribed*
    :type cardp: struct if_usb_card \*

    :param payload:
        *undescribed*
    :type payload: uint8_t \*

    :param nb:
        *undescribed*
    :type nb: uint16_t

    :param data:
        *undescribed*
    :type data: u8

.. _`usb_tx_block.description`:

Description
-----------

\ ``priv``\        pointer to struct lbtf_private
\ ``payload``\     pointer to payload data
\ ``nb``\          data length
\ ``data``\        non-zero for data, zero for commands

.. _`usb_tx_block.return`:

Return
------

0 on success, nonzero otherwise.

.. _`if_usb_receive`:

if_usb_receive
==============

.. c:function:: void if_usb_receive(struct urb *urb)

    read data received from the device.

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`if_usb_receive.description`:

Description
-----------

\ ``urb``\                 pointer to struct urb

.. _`if_usb_host_to_card`:

if_usb_host_to_card
===================

.. c:function:: int if_usb_host_to_card(struct lbtf_private *priv, uint8_t type, uint8_t *payload, uint16_t nb)

    Download data to the device

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

    :param type:
        *undescribed*
    :type type: uint8_t

    :param payload:
        *undescribed*
    :type payload: uint8_t \*

    :param nb:
        *undescribed*
    :type nb: uint16_t

.. _`if_usb_host_to_card.description`:

Description
-----------

\ ``priv``\                pointer to struct lbtf_private structure
\ ``type``\                type of data
\ ``buf``\                 pointer to data buffer
\ ``len``\                 number of bytes

.. _`if_usb_host_to_card.return`:

Return
------

0 on success, nonzero otherwise

.. _`if_usb_issue_boot_command`:

if_usb_issue_boot_command
=========================

.. c:function:: int if_usb_issue_boot_command(struct if_usb_card *cardp, int ivalue)

    Issue boot command to Boot2.

    :param cardp:
        *undescribed*
    :type cardp: struct if_usb_card \*

    :param ivalue:
        *undescribed*
    :type ivalue: int

.. _`if_usb_issue_boot_command.description`:

Description
-----------

\ ``ivalue``\    1 boots from FW by USB-Download, 2 boots from FW in EEPROM.

.. _`if_usb_issue_boot_command.return`:

Return
------

0

.. _`check_fwfile_format`:

check_fwfile_format
===================

.. c:function:: int check_fwfile_format(const u8 *data, u32 totlen)

    Check the validity of Boot2/FW image.

    :param data:
        *undescribed*
    :type data: const u8 \*

    :param totlen:
        *undescribed*
    :type totlen: u32

.. _`check_fwfile_format.description`:

Description
-----------

\ ``data``\        pointer to image
\ ``totlen``\      image length

.. _`check_fwfile_format.return`:

Return
------

0 if the image is valid, nonzero otherwise.

.. This file was automatic generated / don't edit.

