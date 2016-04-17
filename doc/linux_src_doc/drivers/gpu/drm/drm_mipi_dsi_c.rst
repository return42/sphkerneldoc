.. -*- coding: utf-8; mode: rst -*-

==============
drm_mipi_dsi.c
==============


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

.. c:function:: struct mipi_dsi_device *of_find_mipi_dsi_device_by_node (struct device_node *np)

    find the MIPI DSI device matching a device tree node

    :param struct device_node \*np:
        device tree node



.. _`of_find_mipi_dsi_device_by_node.return`:

Return
------

A pointer to the MIPI DSI device corresponding to ``np`` or NULL if no
such device exists (or has not been registered yet).



.. _`mipi_dsi_device_register_full`:

mipi_dsi_device_register_full
=============================

.. c:function:: struct mipi_dsi_device *mipi_dsi_device_register_full (struct mipi_dsi_host *host, const struct mipi_dsi_device_info *info)

    create a MIPI DSI device

    :param struct mipi_dsi_host \*host:
        DSI host to which this device is connected

    :param const struct mipi_dsi_device_info \*info:
        pointer to template containing DSI device information



.. _`mipi_dsi_device_register_full.description`:

Description
-----------

Create a MIPI DSI device by using the device information provided by
mipi_dsi_device_info template



.. _`mipi_dsi_device_register_full.returns`:

Returns
-------

A pointer to the newly created MIPI DSI device, or, a pointer encoded
with an error



.. _`mipi_dsi_device_unregister`:

mipi_dsi_device_unregister
==========================

.. c:function:: void mipi_dsi_device_unregister (struct mipi_dsi_device *dsi)

    unregister MIPI DSI device

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`of_find_mipi_dsi_host_by_node`:

of_find_mipi_dsi_host_by_node
=============================

.. c:function:: struct mipi_dsi_host *of_find_mipi_dsi_host_by_node (struct device_node *node)

    find the MIPI DSI host matching a device tree node

    :param struct device_node \*node:
        device tree node



.. _`of_find_mipi_dsi_host_by_node.returns`:

Returns
-------

A pointer to the MIPI DSI host corresponding to ``node`` or NULL if no
such device exists (or has not been registered yet).



.. _`mipi_dsi_attach`:

mipi_dsi_attach
===============

.. c:function:: int mipi_dsi_attach (struct mipi_dsi_device *dsi)

    attach a DSI device to its DSI host

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral



.. _`mipi_dsi_detach`:

mipi_dsi_detach
===============

.. c:function:: int mipi_dsi_detach (struct mipi_dsi_device *dsi)

    detach a DSI device from its DSI host

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral



.. _`mipi_dsi_packet_format_is_short`:

mipi_dsi_packet_format_is_short
===============================

.. c:function:: bool mipi_dsi_packet_format_is_short (u8 type)

    check if a packet is of the short format

    :param u8 type:
        MIPI DSI data type of the packet



.. _`mipi_dsi_packet_format_is_short.return`:

Return
------

true if the packet for the given data type is a short packet, false
otherwise.



.. _`mipi_dsi_packet_format_is_long`:

mipi_dsi_packet_format_is_long
==============================

.. c:function:: bool mipi_dsi_packet_format_is_long (u8 type)

    check if a packet is of the long format

    :param u8 type:
        MIPI DSI data type of the packet



.. _`mipi_dsi_packet_format_is_long.return`:

Return
------

true if the packet for the given data type is a long packet, false
otherwise.



.. _`mipi_dsi_create_packet`:

mipi_dsi_create_packet
======================

.. c:function:: int mipi_dsi_create_packet (struct mipi_dsi_packet *packet, const struct mipi_dsi_msg *msg)

    create a packet from a message according to the DSI protocol

    :param struct mipi_dsi_packet \*packet:
        pointer to a DSI packet structure

    :param const struct mipi_dsi_msg \*msg:
        message to translate into a packet



.. _`mipi_dsi_create_packet.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_shutdown_peripheral`:

mipi_dsi_shutdown_peripheral
============================

.. c:function:: int mipi_dsi_shutdown_peripheral (struct mipi_dsi_device *dsi)

    sends a Shutdown Peripheral command

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_shutdown_peripheral.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_turn_on_peripheral`:

mipi_dsi_turn_on_peripheral
===========================

.. c:function:: int mipi_dsi_turn_on_peripheral (struct mipi_dsi_device *dsi)

    sends a Turn On Peripheral command

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_turn_on_peripheral.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_generic_write`:

mipi_dsi_generic_write
======================

.. c:function:: ssize_t mipi_dsi_generic_write (struct mipi_dsi_device *dsi, const void *payload, size_t size)

    transmit data using a generic write packet

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param const void \*payload:
        buffer containing the payload

    :param size_t size:
        size of payload buffer



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

.. c:function:: ssize_t mipi_dsi_generic_read (struct mipi_dsi_device *dsi, const void *params, size_t num_params, void *data, size_t size)

    receive data using a generic read packet

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param const void \*params:
        buffer containing the request parameters

    :param size_t num_params:
        number of request parameters

    :param void \*data:
        buffer in which to return the received data

    :param size_t size:
        size of receive buffer



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

.. c:function:: ssize_t mipi_dsi_dcs_write_buffer (struct mipi_dsi_device *dsi, const void *data, size_t len)

    transmit a DCS command with payload

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param const void \*data:
        buffer containing data to be transmitted

    :param size_t len:
        size of transmission buffer



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

.. c:function:: ssize_t mipi_dsi_dcs_write (struct mipi_dsi_device *dsi, u8 cmd, const void *data, size_t len)

    send DCS write command

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u8 cmd:
        DCS command

    :param const void \*data:
        buffer containing the command payload

    :param size_t len:
        command payload length



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

.. c:function:: ssize_t mipi_dsi_dcs_read (struct mipi_dsi_device *dsi, u8 cmd, void *data, size_t len)

    send DCS read request command

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u8 cmd:
        DCS command

    :param void \*data:
        buffer in which to receive data

    :param size_t len:
        size of receive buffer



.. _`mipi_dsi_dcs_read.return`:

Return
------

The number of bytes read or a negative error code on failure.



.. _`mipi_dsi_dcs_nop`:

mipi_dsi_dcs_nop
================

.. c:function:: int mipi_dsi_dcs_nop (struct mipi_dsi_device *dsi)

    send DCS nop packet

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_nop.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_soft_reset`:

mipi_dsi_dcs_soft_reset
=======================

.. c:function:: int mipi_dsi_dcs_soft_reset (struct mipi_dsi_device *dsi)

    perform a software reset of the display module

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_soft_reset.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_get_power_mode`:

mipi_dsi_dcs_get_power_mode
===========================

.. c:function:: int mipi_dsi_dcs_get_power_mode (struct mipi_dsi_device *dsi, u8 *mode)

    query the display module's current power mode

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u8 \*mode:
        return location for the current power mode



.. _`mipi_dsi_dcs_get_power_mode.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_get_pixel_format`:

mipi_dsi_dcs_get_pixel_format
=============================

.. c:function:: int mipi_dsi_dcs_get_pixel_format (struct mipi_dsi_device *dsi, u8 *format)

    gets the pixel format for the RGB image data used by the interface

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u8 \*format:
        return location for the pixel format



.. _`mipi_dsi_dcs_get_pixel_format.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_enter_sleep_mode`:

mipi_dsi_dcs_enter_sleep_mode
=============================

.. c:function:: int mipi_dsi_dcs_enter_sleep_mode (struct mipi_dsi_device *dsi)

    disable all unnecessary blocks inside the display module except interface communication

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_enter_sleep_mode.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_exit_sleep_mode`:

mipi_dsi_dcs_exit_sleep_mode
============================

.. c:function:: int mipi_dsi_dcs_exit_sleep_mode (struct mipi_dsi_device *dsi)

    enable all blocks inside the display module

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_exit_sleep_mode.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_set_display_off`:

mipi_dsi_dcs_set_display_off
============================

.. c:function:: int mipi_dsi_dcs_set_display_off (struct mipi_dsi_device *dsi)

    stop displaying the image data on the display device

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_set_display_off.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_set_display_on`:

mipi_dsi_dcs_set_display_on
===========================

.. c:function:: int mipi_dsi_dcs_set_display_on (struct mipi_dsi_device *dsi)

    start displaying the image data on the display device

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_set_display_on.return`:

Return
------

0 on success or a negative error code on failure



.. _`mipi_dsi_dcs_set_column_address`:

mipi_dsi_dcs_set_column_address
===============================

.. c:function:: int mipi_dsi_dcs_set_column_address (struct mipi_dsi_device *dsi, u16 start, u16 end)

    define the column extent of the frame memory accessed by the host processor

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u16 start:
        first column of frame memory

    :param u16 end:
        last column of frame memory



.. _`mipi_dsi_dcs_set_column_address.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_set_page_address`:

mipi_dsi_dcs_set_page_address
=============================

.. c:function:: int mipi_dsi_dcs_set_page_address (struct mipi_dsi_device *dsi, u16 start, u16 end)

    define the page extent of the frame memory accessed by the host processor

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u16 start:
        first page of frame memory

    :param u16 end:
        last page of frame memory



.. _`mipi_dsi_dcs_set_page_address.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_dcs_set_tear_off`:

mipi_dsi_dcs_set_tear_off
=========================

.. c:function:: int mipi_dsi_dcs_set_tear_off (struct mipi_dsi_device *dsi)

    turn off the display module's Tearing Effect output signal on the TE signal line

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device



.. _`mipi_dsi_dcs_set_tear_off.return`:

Return
------

0 on success or a negative error code on failure



.. _`mipi_dsi_dcs_set_tear_on`:

mipi_dsi_dcs_set_tear_on
========================

.. c:function:: int mipi_dsi_dcs_set_tear_on (struct mipi_dsi_device *dsi, enum mipi_dsi_dcs_tear_mode mode)

    turn on the display module's Tearing Effect output signal on the TE signal line.

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param enum mipi_dsi_dcs_tear_mode mode:
        the Tearing Effect Output Line mode



.. _`mipi_dsi_dcs_set_tear_on.return`:

Return
------

0 on success or a negative error code on failure



.. _`mipi_dsi_dcs_set_pixel_format`:

mipi_dsi_dcs_set_pixel_format
=============================

.. c:function:: int mipi_dsi_dcs_set_pixel_format (struct mipi_dsi_device *dsi, u8 format)

    sets the pixel format for the RGB image data used by the interface

    :param struct mipi_dsi_device \*dsi:
        DSI peripheral device

    :param u8 format:
        pixel format



.. _`mipi_dsi_dcs_set_pixel_format.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_driver_register_full`:

mipi_dsi_driver_register_full
=============================

.. c:function:: int mipi_dsi_driver_register_full (struct mipi_dsi_driver *drv, struct module *owner)

    register a driver for DSI devices

    :param struct mipi_dsi_driver \*drv:
        DSI driver structure

    :param struct module \*owner:
        owner module



.. _`mipi_dsi_driver_register_full.return`:

Return
------

0 on success or a negative error code on failure.



.. _`mipi_dsi_driver_unregister`:

mipi_dsi_driver_unregister
==========================

.. c:function:: void mipi_dsi_driver_unregister (struct mipi_dsi_driver *drv)

    unregister a driver for DSI devices

    :param struct mipi_dsi_driver \*drv:
        DSI driver structure



.. _`mipi_dsi_driver_unregister.return`:

Return
------

0 on success or a negative error code on failure.

