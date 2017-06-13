.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_mipi_dsi.h

.. _`mipi_dsi_msg`:

struct mipi_dsi_msg
===================

.. c:type:: struct mipi_dsi_msg

    read/write DSI buffer

.. _`mipi_dsi_msg.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_msg {
        u8 channel;
        u8 type;
        u16 flags;
        size_t tx_len;
        const void *tx_buf;
        size_t rx_len;
        void *rx_buf;
    }

.. _`mipi_dsi_msg.members`:

Members
-------

channel
    virtual channel id

type
    payload data type

flags
    flags controlling this message transmission

tx_len
    length of \ ``tx_buf``\ 

tx_buf
    data to be written

rx_len
    length of \ ``rx_buf``\ 

rx_buf
    data to be read, or NULL

.. _`mipi_dsi_packet`:

struct mipi_dsi_packet
======================

.. c:type:: struct mipi_dsi_packet

    represents a MIPI DSI packet in protocol format

.. _`mipi_dsi_packet.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_packet {
        size_t size;
        u8 header;
        size_t payload_length;
        const u8 *payload;
    }

.. _`mipi_dsi_packet.members`:

Members
-------

size
    size (in bytes) of the packet

header
    the four bytes that make up the header (Data ID, Word Count or
    Packet Data, and ECC)

payload_length
    number of bytes in the payload

payload
    a pointer to a buffer containing the payload, if any

.. _`mipi_dsi_host_ops`:

struct mipi_dsi_host_ops
========================

.. c:type:: struct mipi_dsi_host_ops

    DSI bus operations

.. _`mipi_dsi_host_ops.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_host_ops {
        int (*attach)(struct mipi_dsi_host *host,struct mipi_dsi_device *dsi);
        int (*detach)(struct mipi_dsi_host *host,struct mipi_dsi_device *dsi);
        ssize_t (*transfer)(struct mipi_dsi_host *host,const struct mipi_dsi_msg *msg);
    }

.. _`mipi_dsi_host_ops.members`:

Members
-------

attach
    attach DSI device to DSI host

detach
    detach DSI device from DSI host

transfer
    transmit a DSI packet

.. _`mipi_dsi_host_ops.description`:

Description
-----------

DSI packets transmitted by .transfer() are passed in as mipi_dsi_msg
structures. This structure contains information about the type of packet
being transmitted as well as the transmit and receive buffers. When an
error is encountered during transmission, this function will return a
negative error code. On success it shall return the number of bytes
transmitted for write packets or the number of bytes received for read
packets.

Note that typically DSI packet transmission is atomic, so the .transfer()
function will seldomly return anything other than the number of bytes
contained in the transmit buffer on success.

.. _`mipi_dsi_host`:

struct mipi_dsi_host
====================

.. c:type:: struct mipi_dsi_host

    DSI host device

.. _`mipi_dsi_host.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_host {
        struct device *dev;
        const struct mipi_dsi_host_ops *ops;
        struct list_head list;
    }

.. _`mipi_dsi_host.members`:

Members
-------

dev
    driver model device node for this DSI host

ops
    DSI host operations

list
    list management

.. _`mipi_dsi_device_info`:

struct mipi_dsi_device_info
===========================

.. c:type:: struct mipi_dsi_device_info

    template for creating a mipi_dsi_device

.. _`mipi_dsi_device_info.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_device_info {
        char type;
        u32 channel;
        struct device_node *node;
    }

.. _`mipi_dsi_device_info.members`:

Members
-------

type
    DSI peripheral chip type

channel
    DSI virtual channel assigned to peripheral

node
    pointer to OF device node or NULL

.. _`mipi_dsi_device_info.description`:

Description
-----------

This is populated and passed to mipi_dsi_device_new to create a new
DSI device

.. _`mipi_dsi_device`:

struct mipi_dsi_device
======================

.. c:type:: struct mipi_dsi_device

    DSI peripheral device

.. _`mipi_dsi_device.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_device {
        struct mipi_dsi_host *host;
        struct device dev;
        char name;
        unsigned int channel;
        unsigned int lanes;
        enum mipi_dsi_pixel_format format;
        unsigned long mode_flags;
    }

.. _`mipi_dsi_device.members`:

Members
-------

host
    DSI host for this peripheral

dev
    driver model device node for this peripheral

name
    DSI peripheral chip type

channel
    virtual channel assigned to the peripheral

lanes
    number of active data lanes

format
    pixel format for video mode

mode_flags
    DSI operation mode related flags

.. _`mipi_dsi_pixel_format_to_bpp`:

mipi_dsi_pixel_format_to_bpp
============================

.. c:function:: int mipi_dsi_pixel_format_to_bpp(enum mipi_dsi_pixel_format fmt)

    obtain the number of bits per pixel for any given pixel format defined by the MIPI DSI specification

    :param enum mipi_dsi_pixel_format fmt:
        MIPI DSI pixel format

.. _`mipi_dsi_pixel_format_to_bpp.return`:

Return
------

The number of bits per pixel of the given pixel format.

.. _`mipi_dsi_dcs_tear_mode`:

enum mipi_dsi_dcs_tear_mode
===========================

.. c:type:: enum mipi_dsi_dcs_tear_mode

    Tearing Effect Output Line mode

.. _`mipi_dsi_dcs_tear_mode.definition`:

Definition
----------

.. code-block:: c

    enum mipi_dsi_dcs_tear_mode {
        MIPI_DSI_DCS_TEAR_MODE_VBLANK,
        MIPI_DSI_DCS_TEAR_MODE_VHBLANK
    };

.. _`mipi_dsi_dcs_tear_mode.constants`:

Constants
---------

MIPI_DSI_DCS_TEAR_MODE_VBLANK
    the TE output line consists of V-Blanking
    information only

MIPI_DSI_DCS_TEAR_MODE_VHBLANK
    the TE output line consists of both
    V-Blanking and H-Blanking information

.. _`mipi_dsi_driver`:

struct mipi_dsi_driver
======================

.. c:type:: struct mipi_dsi_driver

    DSI driver

.. _`mipi_dsi_driver.definition`:

Definition
----------

.. code-block:: c

    struct mipi_dsi_driver {
        struct device_driver driver;
        int(*probe)(struct mipi_dsi_device *dsi);
        int(*remove)(struct mipi_dsi_device *dsi);
        void (*shutdown)(struct mipi_dsi_device *dsi);
    }

.. _`mipi_dsi_driver.members`:

Members
-------

driver
    device driver model driver

probe
    callback for device binding

remove
    callback for device unbinding

shutdown
    called at shutdown time to quiesce the device

.. This file was automatic generated / don't edit.

