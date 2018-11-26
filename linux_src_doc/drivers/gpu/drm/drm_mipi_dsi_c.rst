.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_mipi_dsi.c

.. _`dsi-helpers`:

dsi helpers
===========

These functions contain some common logic and helpers to deal with MIPI DSI
peripherals.

Helpers are provided for a number of standard MIPI DSI command as well as a
subset of the MIPI DCS command set.

.. _`of_find_mipi_dsi_device_by_node`:

of_find_mipi_dsi_device_by_node
===============================

.. c:function:: struct mipi_dsi_device *of_find_mipi_dsi_device_by_node(struct device_node *np)

    find the MIPI DSI device matching a device tree node

    :param np:
        device tree node
    :type np: struct device_node \*

.. _`of_find_mipi_dsi_device_by_node.return`:

Return
------

A pointer to the MIPI DSI device corresponding to \ ``np``\  or NULL if no
   such device exists (or has not been registered yet).

.. _`mipi_dsi_device_register_full`:

mipi_dsi_device_register_full
=============================

.. c:function:: struct mipi_dsi_device *mipi_dsi_device_register_full(struct mipi_dsi_host *host, const struct mipi_dsi_device_info *info)

    create a MIPI DSI device

    :param host:
        DSI host to which this device is connected
    :type host: struct mipi_dsi_host \*

    :param info:
        pointer to template containing DSI device information
    :type info: const struct mipi_dsi_device_info \*

.. _`mipi_dsi_device_register_full.description`:

Description
-----------

Create a MIPI DSI device by using the device information provided by
mipi_dsi_device_info template

.. _`mipi_dsi_device_register_full.return`:

Return
------

A pointer to the newly created MIPI DSI device, or, a pointer encoded
with an error

.. _`mipi_dsi_device_unregister`:

mipi_dsi_device_unregister
==========================

.. c:function:: void mipi_dsi_device_unregister(struct mipi_dsi_device *dsi)

    unregister MIPI DSI device

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`of_find_mipi_dsi_host_by_node`:

of_find_mipi_dsi_host_by_node
=============================

.. c:function:: struct mipi_dsi_host *of_find_mipi_dsi_host_by_node(struct device_node *node)

    find the MIPI DSI host matching a device tree node

    :param node:
        device tree node
    :type node: struct device_node \*

.. _`of_find_mipi_dsi_host_by_node.return`:

Return
------

A pointer to the MIPI DSI host corresponding to \ ``node``\  or NULL if no
such device exists (or has not been registered yet).

.. _`mipi_dsi_attach`:

mipi_dsi_attach
===============

.. c:function:: int mipi_dsi_attach(struct mipi_dsi_device *dsi)

    attach a DSI device to its DSI host

    :param dsi:
        DSI peripheral
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_detach`:

mipi_dsi_detach
===============

.. c:function:: int mipi_dsi_detach(struct mipi_dsi_device *dsi)

    detach a DSI device from its DSI host

    :param dsi:
        DSI peripheral
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_packet_format_is_short`:

mipi_dsi_packet_format_is_short
===============================

.. c:function:: bool mipi_dsi_packet_format_is_short(u8 type)

    check if a packet is of the short format

    :param type:
        MIPI DSI data type of the packet
    :type type: u8

.. _`mipi_dsi_packet_format_is_short.return`:

Return
------

true if the packet for the given data type is a short packet, false
otherwise.

.. _`mipi_dsi_packet_format_is_long`:

mipi_dsi_packet_format_is_long
==============================

.. c:function:: bool mipi_dsi_packet_format_is_long(u8 type)

    check if a packet is of the long format

    :param type:
        MIPI DSI data type of the packet
    :type type: u8

.. _`mipi_dsi_packet_format_is_long.return`:

Return
------

true if the packet for the given data type is a long packet, false
otherwise.

.. _`mipi_dsi_create_packet`:

mipi_dsi_create_packet
======================

.. c:function:: int mipi_dsi_create_packet(struct mipi_dsi_packet *packet, const struct mipi_dsi_msg *msg)

    create a packet from a message according to the DSI protocol

    :param packet:
        pointer to a DSI packet structure
    :type packet: struct mipi_dsi_packet \*

    :param msg:
        message to translate into a packet
    :type msg: const struct mipi_dsi_msg \*

.. _`mipi_dsi_create_packet.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_shutdown_peripheral`:

mipi_dsi_shutdown_peripheral
============================

.. c:function:: int mipi_dsi_shutdown_peripheral(struct mipi_dsi_device *dsi)

    sends a Shutdown Peripheral command

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_shutdown_peripheral.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_turn_on_peripheral`:

mipi_dsi_turn_on_peripheral
===========================

.. c:function:: int mipi_dsi_turn_on_peripheral(struct mipi_dsi_device *dsi)

    sends a Turn On Peripheral command

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_turn_on_peripheral.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_generic_write`:

mipi_dsi_generic_write
======================

.. c:function:: ssize_t mipi_dsi_generic_write(struct mipi_dsi_device *dsi, const void *payload, size_t size)

    transmit data using a generic write packet

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param payload:
        buffer containing the payload
    :type payload: const void \*

    :param size:
        size of payload buffer
    :type size: size_t

.. _`mipi_dsi_generic_write.description`:

Description
-----------

This function will automatically choose the right data type depending on
the payload length.

.. _`mipi_dsi_generic_write.return`:

Return
------

The number of bytes transmitted on success or a negative error code
on failure.

.. _`mipi_dsi_generic_read`:

mipi_dsi_generic_read
=====================

.. c:function:: ssize_t mipi_dsi_generic_read(struct mipi_dsi_device *dsi, const void *params, size_t num_params, void *data, size_t size)

    receive data using a generic read packet

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param params:
        buffer containing the request parameters
    :type params: const void \*

    :param num_params:
        number of request parameters
    :type num_params: size_t

    :param data:
        buffer in which to return the received data
    :type data: void \*

    :param size:
        size of receive buffer
    :type size: size_t

.. _`mipi_dsi_generic_read.description`:

Description
-----------

This function will automatically choose the right data type depending on
the number of parameters passed in.

.. _`mipi_dsi_generic_read.return`:

Return
------

The number of bytes successfully read or a negative error code on
failure.

.. _`mipi_dsi_dcs_write_buffer`:

mipi_dsi_dcs_write_buffer
=========================

.. c:function:: ssize_t mipi_dsi_dcs_write_buffer(struct mipi_dsi_device *dsi, const void *data, size_t len)

    transmit a DCS command with payload

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param data:
        buffer containing data to be transmitted
    :type data: const void \*

    :param len:
        size of transmission buffer
    :type len: size_t

.. _`mipi_dsi_dcs_write_buffer.description`:

Description
-----------

This function will automatically choose the right data type depending on
the command payload length.

.. _`mipi_dsi_dcs_write_buffer.return`:

Return
------

The number of bytes successfully transmitted or a negative error
code on failure.

.. _`mipi_dsi_dcs_write`:

mipi_dsi_dcs_write
==================

.. c:function:: ssize_t mipi_dsi_dcs_write(struct mipi_dsi_device *dsi, u8 cmd, const void *data, size_t len)

    send DCS write command

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param cmd:
        DCS command
    :type cmd: u8

    :param data:
        buffer containing the command payload
    :type data: const void \*

    :param len:
        command payload length
    :type len: size_t

.. _`mipi_dsi_dcs_write.description`:

Description
-----------

This function will automatically choose the right data type depending on
the command payload length.

.. _`mipi_dsi_dcs_write.return`:

Return
------

The number of bytes successfully transmitted or a negative error
code on failure.

.. _`mipi_dsi_dcs_read`:

mipi_dsi_dcs_read
=================

.. c:function:: ssize_t mipi_dsi_dcs_read(struct mipi_dsi_device *dsi, u8 cmd, void *data, size_t len)

    send DCS read request command

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param cmd:
        DCS command
    :type cmd: u8

    :param data:
        buffer in which to receive data
    :type data: void \*

    :param len:
        size of receive buffer
    :type len: size_t

.. _`mipi_dsi_dcs_read.return`:

Return
------

The number of bytes read or a negative error code on failure.

.. _`mipi_dsi_dcs_nop`:

mipi_dsi_dcs_nop
================

.. c:function:: int mipi_dsi_dcs_nop(struct mipi_dsi_device *dsi)

    send DCS nop packet

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_nop.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_soft_reset`:

mipi_dsi_dcs_soft_reset
=======================

.. c:function:: int mipi_dsi_dcs_soft_reset(struct mipi_dsi_device *dsi)

    perform a software reset of the display module

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_soft_reset.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_get_power_mode`:

mipi_dsi_dcs_get_power_mode
===========================

.. c:function:: int mipi_dsi_dcs_get_power_mode(struct mipi_dsi_device *dsi, u8 *mode)

    query the display module's current power mode

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param mode:
        return location for the current power mode
    :type mode: u8 \*

.. _`mipi_dsi_dcs_get_power_mode.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_get_pixel_format`:

mipi_dsi_dcs_get_pixel_format
=============================

.. c:function:: int mipi_dsi_dcs_get_pixel_format(struct mipi_dsi_device *dsi, u8 *format)

    gets the pixel format for the RGB image data used by the interface

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param format:
        return location for the pixel format
    :type format: u8 \*

.. _`mipi_dsi_dcs_get_pixel_format.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_enter_sleep_mode`:

mipi_dsi_dcs_enter_sleep_mode
=============================

.. c:function:: int mipi_dsi_dcs_enter_sleep_mode(struct mipi_dsi_device *dsi)

    disable all unnecessary blocks inside the display module except interface communication

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_enter_sleep_mode.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_exit_sleep_mode`:

mipi_dsi_dcs_exit_sleep_mode
============================

.. c:function:: int mipi_dsi_dcs_exit_sleep_mode(struct mipi_dsi_device *dsi)

    enable all blocks inside the display module

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_exit_sleep_mode.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_set_display_off`:

mipi_dsi_dcs_set_display_off
============================

.. c:function:: int mipi_dsi_dcs_set_display_off(struct mipi_dsi_device *dsi)

    stop displaying the image data on the display device

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_set_display_off.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_set_display_on`:

mipi_dsi_dcs_set_display_on
===========================

.. c:function:: int mipi_dsi_dcs_set_display_on(struct mipi_dsi_device *dsi)

    start displaying the image data on the display device

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_set_display_on.return`:

Return
------

0 on success or a negative error code on failure

.. _`mipi_dsi_dcs_set_column_address`:

mipi_dsi_dcs_set_column_address
===============================

.. c:function:: int mipi_dsi_dcs_set_column_address(struct mipi_dsi_device *dsi, u16 start, u16 end)

    define the column extent of the frame memory accessed by the host processor

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param start:
        first column of frame memory
    :type start: u16

    :param end:
        last column of frame memory
    :type end: u16

.. _`mipi_dsi_dcs_set_column_address.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_set_page_address`:

mipi_dsi_dcs_set_page_address
=============================

.. c:function:: int mipi_dsi_dcs_set_page_address(struct mipi_dsi_device *dsi, u16 start, u16 end)

    define the page extent of the frame memory accessed by the host processor

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param start:
        first page of frame memory
    :type start: u16

    :param end:
        last page of frame memory
    :type end: u16

.. _`mipi_dsi_dcs_set_page_address.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_set_tear_off`:

mipi_dsi_dcs_set_tear_off
=========================

.. c:function:: int mipi_dsi_dcs_set_tear_off(struct mipi_dsi_device *dsi)

    turn off the display module's Tearing Effect output signal on the TE signal line

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

.. _`mipi_dsi_dcs_set_tear_off.return`:

Return
------

0 on success or a negative error code on failure

.. _`mipi_dsi_dcs_set_tear_on`:

mipi_dsi_dcs_set_tear_on
========================

.. c:function:: int mipi_dsi_dcs_set_tear_on(struct mipi_dsi_device *dsi, enum mipi_dsi_dcs_tear_mode mode)

    turn on the display module's Tearing Effect output signal on the TE signal line.

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param mode:
        the Tearing Effect Output Line mode
    :type mode: enum mipi_dsi_dcs_tear_mode

.. _`mipi_dsi_dcs_set_tear_on.return`:

Return
------

0 on success or a negative error code on failure

.. _`mipi_dsi_dcs_set_pixel_format`:

mipi_dsi_dcs_set_pixel_format
=============================

.. c:function:: int mipi_dsi_dcs_set_pixel_format(struct mipi_dsi_device *dsi, u8 format)

    sets the pixel format for the RGB image data used by the interface

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param format:
        pixel format
    :type format: u8

.. _`mipi_dsi_dcs_set_pixel_format.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_set_tear_scanline`:

mipi_dsi_dcs_set_tear_scanline
==============================

.. c:function:: int mipi_dsi_dcs_set_tear_scanline(struct mipi_dsi_device *dsi, u16 scanline)

    set the scanline to use as trigger for the Tearing Effect output signal of the display module

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param scanline:
        scanline to use as trigger
    :type scanline: u16

.. _`mipi_dsi_dcs_set_tear_scanline.return`:

Return
------

0 on success or a negative error code on failure

.. _`mipi_dsi_dcs_set_display_brightness`:

mipi_dsi_dcs_set_display_brightness
===================================

.. c:function:: int mipi_dsi_dcs_set_display_brightness(struct mipi_dsi_device *dsi, u16 brightness)

    sets the brightness value of the display

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param brightness:
        brightness value
    :type brightness: u16

.. _`mipi_dsi_dcs_set_display_brightness.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_dcs_get_display_brightness`:

mipi_dsi_dcs_get_display_brightness
===================================

.. c:function:: int mipi_dsi_dcs_get_display_brightness(struct mipi_dsi_device *dsi, u16 *brightness)

    gets the current brightness value of the display

    :param dsi:
        DSI peripheral device
    :type dsi: struct mipi_dsi_device \*

    :param brightness:
        brightness value
    :type brightness: u16 \*

.. _`mipi_dsi_dcs_get_display_brightness.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_driver_register_full`:

mipi_dsi_driver_register_full
=============================

.. c:function:: int mipi_dsi_driver_register_full(struct mipi_dsi_driver *drv, struct module *owner)

    register a driver for DSI devices

    :param drv:
        DSI driver structure
    :type drv: struct mipi_dsi_driver \*

    :param owner:
        owner module
    :type owner: struct module \*

.. _`mipi_dsi_driver_register_full.return`:

Return
------

0 on success or a negative error code on failure.

.. _`mipi_dsi_driver_unregister`:

mipi_dsi_driver_unregister
==========================

.. c:function:: void mipi_dsi_driver_unregister(struct mipi_dsi_driver *drv)

    unregister a driver for DSI devices

    :param drv:
        DSI driver structure
    :type drv: struct mipi_dsi_driver \*

.. _`mipi_dsi_driver_unregister.return`:

Return
------

0 on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

