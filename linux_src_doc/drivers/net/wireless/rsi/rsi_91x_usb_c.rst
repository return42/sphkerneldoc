.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_usb.c

.. _`rsi_usb_card_write`:

rsi_usb_card_write
==================

.. c:function:: int rsi_usb_card_write(struct rsi_hw *adapter, u8 *buf, u16 len, u8 endpoint)

    This function writes to the USB Card.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param buf:
        Pointer to the buffer from where the data has to be taken.
    :type buf: u8 \*

    :param len:
        Length to be written.
    :type len: u16

    :param endpoint:
        Type of endpoint.
    :type endpoint: u8

.. _`rsi_usb_card_write.return`:

Return
------

status: 0 on success, a negative error code on failure.

.. _`rsi_write_multiple`:

rsi_write_multiple
==================

.. c:function:: int rsi_write_multiple(struct rsi_hw *adapter, u8 endpoint, u8 *data, u32 count)

    This function writes multiple bytes of information to the USB card.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param endpoint:
        *undescribed*
    :type endpoint: u8

    :param data:
        Pointer to the data that has to be written.
    :type data: u8 \*

    :param count:
        Number of multiple bytes to be written.
    :type count: u32

.. _`rsi_write_multiple.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_find_bulk_in_and_out_endpoints`:

rsi_find_bulk_in_and_out_endpoints
==================================

.. c:function:: int rsi_find_bulk_in_and_out_endpoints(struct usb_interface *interface, struct rsi_hw *adapter)

    This function initializes the bulk endpoints to the device.

    :param interface:
        Pointer to the USB interface structure.
    :type interface: struct usb_interface \*

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_find_bulk_in_and_out_endpoints.return`:

Return
------

ret_val: 0 on success, -ENOMEM on failure.

.. _`rsi_usb_reg_write`:

rsi_usb_reg_write
=================

.. c:function:: int rsi_usb_reg_write(struct usb_device *usbdev, u32 reg, u16 value, u16 len)

    This function writes the given data into the given register address.

    :param usbdev:
        Pointer to the usb_device structure.
    :type usbdev: struct usb_device \*

    :param reg:
        Address of the register.
    :type reg: u32

    :param value:
        Value to write.
    :type value: u16

    :param len:
        Length of data to be written.
    :type len: u16

.. _`rsi_usb_reg_write.return`:

Return
------

status: 0 on success, a negative error code on failure.

.. _`rsi_rx_done_handler`:

rsi_rx_done_handler
===================

.. c:function:: void rsi_rx_done_handler(struct urb *urb)

    This function is called when a packet is received from USB stack. This is callback to recieve done.

    :param urb:
        Received URB.
    :type urb: struct urb \*

.. _`rsi_rx_done_handler.return`:

Return
------

None.

.. _`rsi_rx_urb_submit`:

rsi_rx_urb_submit
=================

.. c:function:: int rsi_rx_urb_submit(struct rsi_hw *adapter, u8 ep_num)

    This function submits the given URB to the USB stack.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param ep_num:
        *undescribed*
    :type ep_num: u8

.. _`rsi_rx_urb_submit.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_usb_write_register_multiple`:

rsi_usb_write_register_multiple
===============================

.. c:function:: int rsi_usb_write_register_multiple(struct rsi_hw *adapter, u32 addr, u8 *data, u16 count)

    This function writes multiple bytes of information to multiple registers.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param addr:
        Address of the register.
    :type addr: u32

    :param data:
        Pointer to the data that has to be written.
    :type data: u8 \*

    :param count:
        Number of multiple bytes to be written on to the registers.
    :type count: u16

.. _`rsi_usb_write_register_multiple.return`:

Return
------

status: 0 on success, a negative error code on failure.

.. _`rsi_usb_host_intf_write_pkt`:

rsi_usb_host_intf_write_pkt
===========================

.. c:function:: int rsi_usb_host_intf_write_pkt(struct rsi_hw *adapter, u8 *pkt, u32 len)

    This function writes the packet to the USB card.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param pkt:
        Pointer to the data to be written on to the card.
    :type pkt: u8 \*

    :param len:
        Length of the data to be written on to the card.
    :type len: u32

.. _`rsi_usb_host_intf_write_pkt.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_deinit_usb_interface`:

rsi_deinit_usb_interface
========================

.. c:function:: void rsi_deinit_usb_interface(struct rsi_hw *adapter)

    This function deinitializes the usb interface.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_deinit_usb_interface.return`:

Return
------

None.

.. _`rsi_init_usb_interface`:

rsi_init_usb_interface
======================

.. c:function:: int rsi_init_usb_interface(struct rsi_hw *adapter, struct usb_interface *pfunction)

    This function initializes the usb interface.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param pfunction:
        Pointer to USB interface structure.
    :type pfunction: struct usb_interface \*

.. _`rsi_init_usb_interface.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_probe`:

rsi_probe
=========

.. c:function:: int rsi_probe(struct usb_interface *pfunction, const struct usb_device_id *id)

    This function is called by kernel when the driver provided Vendor and device IDs are matched. All the initialization work is done here.

    :param pfunction:
        Pointer to the USB interface structure.
    :type pfunction: struct usb_interface \*

    :param id:
        Pointer to the usb_device_id structure.
    :type id: const struct usb_device_id \*

.. _`rsi_probe.return`:

Return
------

0 on success, a negative error code on failure.

.. _`rsi_disconnect`:

rsi_disconnect
==============

.. c:function:: void rsi_disconnect(struct usb_interface *pfunction)

    This function performs the reverse of the probe function, it deinitialize the driver structure.

    :param pfunction:
        Pointer to the USB interface structure.
    :type pfunction: struct usb_interface \*

.. _`rsi_disconnect.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

