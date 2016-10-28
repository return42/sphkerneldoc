.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_usb.c

.. _`rsi_usb_card_write`:

rsi_usb_card_write
==================

.. c:function:: int rsi_usb_card_write(struct rsi_hw *adapter, void *buf, u16 len, u8 endpoint)

    :param struct rsi_hw \*adapter:
        *undescribed*

    :param void \*buf:
        *undescribed*

    :param u16 len:
        *undescribed*

    :param u8 endpoint:
        *undescribed*

.. _`rsi_usb_card_write.description`:

Description
-----------

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

.. _`rsi_write_multiple`:

rsi_write_multiple
==================

.. c:function:: int rsi_write_multiple(struct rsi_hw *adapter, u8 endpoint, u8 *data, u32 count)

    This function writes multiple bytes of information to the USB card.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u8 endpoint:
        *undescribed*

    :param u8 \*data:
        Pointer to the data that has to be written.

    :param u32 count:
        Number of multiple bytes to be written.

.. _`rsi_write_multiple.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_find_bulk_in_and_out_endpoints`:

rsi_find_bulk_in_and_out_endpoints
==================================

.. c:function:: int rsi_find_bulk_in_and_out_endpoints(struct usb_interface *interface, struct rsi_hw *adapter)

    This function initializes the bulk endpoints to the device.

    :param struct usb_interface \*interface:
        Pointer to the USB interface structure.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_find_bulk_in_and_out_endpoints.return`:

Return
------

ret_val: 0 on success, -ENOMEM on failure.

.. _`rsi_usb_reg_write`:

rsi_usb_reg_write
=================

.. c:function:: int rsi_usb_reg_write(struct usb_device *usbdev, u32 reg, u16 value, u16 len)

    This function writes the given data into the given register address.

    :param struct usb_device \*usbdev:
        Pointer to the usb_device structure.

    :param u32 reg:
        Address of the register.

    :param u16 value:
        Value to write.

    :param u16 len:
        Length of data to be written.

.. _`rsi_usb_reg_write.return`:

Return
------

status: 0 on success, a negative error code on failure.

.. _`rsi_rx_done_handler`:

rsi_rx_done_handler
===================

.. c:function:: void rsi_rx_done_handler(struct urb *urb)

    This function is called when a packet is received from USB stack. This is callback to recieve done.

    :param struct urb \*urb:
        Received URB.

.. _`rsi_rx_done_handler.return`:

Return
------

None.

.. _`rsi_rx_urb_submit`:

rsi_rx_urb_submit
=================

.. c:function:: int rsi_rx_urb_submit(struct rsi_hw *adapter)

    This function submits the given URB to the USB stack.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_rx_urb_submit.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_usb_write_register_multiple`:

rsi_usb_write_register_multiple
===============================

.. c:function:: int rsi_usb_write_register_multiple(struct rsi_hw *adapter, u32 addr, u8 *data, u32 count)

    This function writes multiple bytes of information to multiple registers.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u32 addr:
        Address of the register.

    :param u8 \*data:
        Pointer to the data that has to be written.

    :param u32 count:
        Number of multiple bytes to be written on to the registers.

.. _`rsi_usb_write_register_multiple.return`:

Return
------

status: 0 on success, a negative error code on failure.

.. _`rsi_usb_host_intf_write_pkt`:

rsi_usb_host_intf_write_pkt
===========================

.. c:function:: int rsi_usb_host_intf_write_pkt(struct rsi_hw *adapter, u8 *pkt, u32 len)

    This function writes the packet to the USB card.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u8 \*pkt:
        Pointer to the data to be written on to the card.

    :param u32 len:
        Length of the data to be written on to the card.

.. _`rsi_usb_host_intf_write_pkt.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_deinit_usb_interface`:

rsi_deinit_usb_interface
========================

.. c:function:: void rsi_deinit_usb_interface(struct rsi_hw *adapter)

    This function deinitializes the usb interface.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_deinit_usb_interface.return`:

Return
------

None.

.. _`rsi_init_usb_interface`:

rsi_init_usb_interface
======================

.. c:function:: int rsi_init_usb_interface(struct rsi_hw *adapter, struct usb_interface *pfunction)

    This function initializes the usb interface.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param struct usb_interface \*pfunction:
        Pointer to USB interface structure.

.. _`rsi_init_usb_interface.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_probe`:

rsi_probe
=========

.. c:function:: int rsi_probe(struct usb_interface *pfunction, const struct usb_device_id *id)

    This function is called by kernel when the driver provided Vendor and device IDs are matched. All the initialization work is done here.

    :param struct usb_interface \*pfunction:
        Pointer to the USB interface structure.

    :param const struct usb_device_id \*id:
        Pointer to the usb_device_id structure.

.. _`rsi_probe.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_disconnect`:

rsi_disconnect
==============

.. c:function:: void rsi_disconnect(struct usb_interface *pfunction)

    This function performs the reverse of the probe function, it deintialize the driver structure.

    :param struct usb_interface \*pfunction:
        Pointer to the USB interface structure.

.. _`rsi_disconnect.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

