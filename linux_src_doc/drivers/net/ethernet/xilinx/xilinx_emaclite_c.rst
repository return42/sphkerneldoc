.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/xilinx/xilinx_emaclite.c

.. _`net_local`:

struct net_local
================

.. c:type:: struct net_local

    Our private per device data

.. _`net_local.definition`:

Definition
----------

.. code-block:: c

    struct net_local {
        struct net_device *ndev;
        bool tx_ping_pong;
        bool rx_ping_pong;
        u32 next_tx_buf_to_use;
        u32 next_rx_buf_to_use;
        void __iomem *base_addr;
        spinlock_t reset_lock;
        struct sk_buff *deferred_skb;
        struct phy_device *phy_dev;
        struct device_node *phy_node;
        struct mii_bus *mii_bus;
        int last_link;
        bool has_mdio;
    }

.. _`net_local.members`:

Members
-------

ndev
    instance of the network device

tx_ping_pong
    indicates whether Tx Pong buffer is configured in HW

rx_ping_pong
    indicates whether Rx Pong buffer is configured in HW

next_tx_buf_to_use
    next Tx buffer to write to

next_rx_buf_to_use
    next Rx buffer to read from

base_addr
    base address of the Emaclite device

reset_lock
    lock used for synchronization

deferred_skb
    holds an skb (for transmission at a later time) when the
    Tx buffer is not free

phy_dev
    pointer to the PHY device

phy_node
    pointer to the PHY device node

mii_bus
    pointer to the MII bus

last_link
    last link status

has_mdio
    indicates whether MDIO is included in the HW

.. _`xemaclite_enable_interrupts`:

xemaclite_enable_interrupts
===========================

.. c:function:: void xemaclite_enable_interrupts(struct net_local *drvdata)

    Enable the interrupts for the EmacLite device

    :param struct net_local \*drvdata:
        Pointer to the Emaclite device private data

.. _`xemaclite_enable_interrupts.description`:

Description
-----------

This function enables the Tx and Rx interrupts for the Emaclite device along
with the Global Interrupt Enable.

.. _`xemaclite_disable_interrupts`:

xemaclite_disable_interrupts
============================

.. c:function:: void xemaclite_disable_interrupts(struct net_local *drvdata)

    Disable the interrupts for the EmacLite device

    :param struct net_local \*drvdata:
        Pointer to the Emaclite device private data

.. _`xemaclite_disable_interrupts.description`:

Description
-----------

This function disables the Tx and Rx interrupts for the Emaclite device,
along with the Global Interrupt Enable.

.. _`xemaclite_aligned_write`:

xemaclite_aligned_write
=======================

.. c:function:: void xemaclite_aligned_write(void *src_ptr, u32 *dest_ptr, unsigned length)

    Write from 16-bit aligned to 32-bit aligned address

    :param void \*src_ptr:
        Void pointer to the 16-bit aligned source address

    :param u32 \*dest_ptr:
        Pointer to the 32-bit aligned destination address

    :param unsigned length:
        Number bytes to write from source to destination

.. _`xemaclite_aligned_write.description`:

Description
-----------

This function writes data from a 16-bit aligned buffer to a 32-bit aligned
address in the EmacLite device.

.. _`xemaclite_aligned_read`:

xemaclite_aligned_read
======================

.. c:function:: void xemaclite_aligned_read(u32 *src_ptr, u8 *dest_ptr, unsigned length)

    Read from 32-bit aligned to 16-bit aligned buffer

    :param u32 \*src_ptr:
        Pointer to the 32-bit aligned source address

    :param u8 \*dest_ptr:
        Pointer to the 16-bit aligned destination address

    :param unsigned length:
        Number bytes to read from source to destination

.. _`xemaclite_aligned_read.description`:

Description
-----------

This function reads data from a 32-bit aligned address in the EmacLite device
to a 16-bit aligned buffer.

.. _`xemaclite_send_data`:

xemaclite_send_data
===================

.. c:function:: int xemaclite_send_data(struct net_local *drvdata, u8 *data, unsigned int byte_count)

    Send an Ethernet frame

    :param struct net_local \*drvdata:
        Pointer to the Emaclite device private data

    :param u8 \*data:
        Pointer to the data to be sent

    :param unsigned int byte_count:
        Total frame size, including header

.. _`xemaclite_send_data.description`:

Description
-----------

This function checks if the Tx buffer of the Emaclite device is free to send
data. If so, it fills the Tx buffer with data for transmission. Otherwise, it
returns an error.

.. _`xemaclite_send_data.return`:

Return
------

0 upon success or -1 if the buffer(s) are full.

.. _`xemaclite_send_data.note`:

Note
----

The maximum Tx packet size can not be more than Ethernet header
(14 Bytes) + Maximum MTU (1500 bytes). This is excluding FCS.

.. _`xemaclite_recv_data`:

xemaclite_recv_data
===================

.. c:function:: u16 xemaclite_recv_data(struct net_local *drvdata, u8 *data)

    Receive a frame

    :param struct net_local \*drvdata:
        Pointer to the Emaclite device private data

    :param u8 \*data:
        Address where the data is to be received

.. _`xemaclite_recv_data.description`:

Description
-----------

This function is intended to be called from the interrupt context or
with a wrapper which waits for the receive frame to be available.

.. _`xemaclite_recv_data.return`:

Return
------

Total number of bytes received

.. _`xemaclite_update_address`:

xemaclite_update_address
========================

.. c:function:: void xemaclite_update_address(struct net_local *drvdata, u8 *address_ptr)

    Update the MAC address in the device

    :param struct net_local \*drvdata:
        Pointer to the Emaclite device private data

    :param u8 \*address_ptr:
        Pointer to the MAC address (MAC address is a 48-bit value)

.. _`xemaclite_update_address.description`:

Description
-----------

Tx must be idle and Rx should be idle for deterministic results.
It is recommended that this function should be called after the
initialization and before transmission of any packets from the device.
The MAC address can be programmed using any of the two transmit
buffers (if configured).

.. _`xemaclite_set_mac_address`:

xemaclite_set_mac_address
=========================

.. c:function:: int xemaclite_set_mac_address(struct net_device *dev, void *address)

    Set the MAC address for this device

    :param struct net_device \*dev:
        Pointer to the network device instance

    :param void \*address:
        *undescribed*

.. _`xemaclite_set_mac_address.description`:

Description
-----------

This function copies the HW address from the sockaddr strucutre to the
net_device structure and updates the address in HW.

.. _`xemaclite_set_mac_address.return`:

Return
------

Error if the net device is busy or 0 if the addr is set
successfully

.. _`xemaclite_tx_timeout`:

xemaclite_tx_timeout
====================

.. c:function:: void xemaclite_tx_timeout(struct net_device *dev)

    Callback for Tx Timeout

    :param struct net_device \*dev:
        Pointer to the network device

.. _`xemaclite_tx_timeout.description`:

Description
-----------

This function is called when Tx time out occurs for Emaclite device.

.. _`xemaclite_tx_handler`:

xemaclite_tx_handler
====================

.. c:function:: void xemaclite_tx_handler(struct net_device *dev)

    Interrupt handler for frames sent

    :param struct net_device \*dev:
        Pointer to the network device

.. _`xemaclite_tx_handler.description`:

Description
-----------

This function updates the number of packets transmitted and handles the
deferred skb, if there is one.

.. _`xemaclite_rx_handler`:

xemaclite_rx_handler
====================

.. c:function:: void xemaclite_rx_handler(struct net_device *dev)

    Interrupt handler for frames received

    :param struct net_device \*dev:
        Pointer to the network device

.. _`xemaclite_rx_handler.description`:

Description
-----------

This function allocates memory for a socket buffer, fills it with data
received and hands it over to the TCP/IP stack.

.. _`xemaclite_interrupt`:

xemaclite_interrupt
===================

.. c:function:: irqreturn_t xemaclite_interrupt(int irq, void *dev_id)

    Interrupt handler for this driver

    :param int irq:
        Irq of the Emaclite device

    :param void \*dev_id:
        Void pointer to the network device instance used as callback
        reference

.. _`xemaclite_interrupt.description`:

Description
-----------

This function handles the Tx and Rx interrupts of the EmacLite device.

.. _`xemaclite_mdio_wait`:

xemaclite_mdio_wait
===================

.. c:function:: int xemaclite_mdio_wait(struct net_local *lp)

    Wait for the MDIO to be ready to use

    :param struct net_local \*lp:
        Pointer to the Emaclite device private data

.. _`xemaclite_mdio_wait.description`:

Description
-----------

This function waits till the device is ready to accept a new MDIO
request.

.. _`xemaclite_mdio_wait.return`:

Return
------

0 for success or ETIMEDOUT for a timeout

.. _`xemaclite_mdio_read`:

xemaclite_mdio_read
===================

.. c:function:: int xemaclite_mdio_read(struct mii_bus *bus, int phy_id, int reg)

    Read from a given MII management register

    :param struct mii_bus \*bus:
        the mii_bus struct

    :param int phy_id:
        the phy address

    :param int reg:
        register number to read from

.. _`xemaclite_mdio_read.description`:

Description
-----------

This function waits till the device is ready to accept a new MDIO
request and then writes the phy address to the MDIO Address register
and reads data from MDIO Read Data register, when its available.

.. _`xemaclite_mdio_read.return`:

Return
------

Value read from the MII management register

.. _`xemaclite_mdio_write`:

xemaclite_mdio_write
====================

.. c:function:: int xemaclite_mdio_write(struct mii_bus *bus, int phy_id, int reg, u16 val)

    Write to a given MII management register

    :param struct mii_bus \*bus:
        the mii_bus struct

    :param int phy_id:
        the phy address

    :param int reg:
        register number to write to

    :param u16 val:
        value to write to the register number specified by reg

.. _`xemaclite_mdio_write.description`:

Description
-----------

This function waits till the device is ready to accept a new MDIO
request and then writes the val to the MDIO Write Data register.

.. _`xemaclite_mdio_setup`:

xemaclite_mdio_setup
====================

.. c:function:: int xemaclite_mdio_setup(struct net_local *lp, struct device *dev)

    Register mii_bus for the Emaclite device

    :param struct net_local \*lp:
        Pointer to the Emaclite device private data

    :param struct device \*dev:
        *undescribed*

.. _`xemaclite_mdio_setup.description`:

Description
-----------

This function enables MDIO bus in the Emaclite device and registers a
mii_bus.

.. _`xemaclite_mdio_setup.return`:

Return
------

0 upon success or a negative error upon failure

.. _`xemaclite_adjust_link`:

xemaclite_adjust_link
=====================

.. c:function:: void xemaclite_adjust_link(struct net_device *ndev)

    Link state callback for the Emaclite device

    :param struct net_device \*ndev:
        pointer to net_device struct

.. _`xemaclite_adjust_link.description`:

Description
-----------

There's nothing in the Emaclite device to be configured when the link
state changes. We just print the status.

.. _`xemaclite_open`:

xemaclite_open
==============

.. c:function:: int xemaclite_open(struct net_device *dev)

    Open the network device

    :param struct net_device \*dev:
        Pointer to the network device

.. _`xemaclite_open.description`:

Description
-----------

This function sets the MAC address, requests an IRQ and enables interrupts
for the Emaclite device and starts the Tx queue.
It also connects to the phy device, if MDIO is included in Emaclite device.

.. _`xemaclite_close`:

xemaclite_close
===============

.. c:function:: int xemaclite_close(struct net_device *dev)

    Close the network device

    :param struct net_device \*dev:
        Pointer to the network device

.. _`xemaclite_close.description`:

Description
-----------

This function stops the Tx queue, disables interrupts and frees the IRQ for
the Emaclite device.
It also disconnects the phy device associated with the Emaclite device.

.. _`xemaclite_send`:

xemaclite_send
==============

.. c:function:: int xemaclite_send(struct sk_buff *orig_skb, struct net_device *dev)

    Transmit a frame

    :param struct sk_buff \*orig_skb:
        Pointer to the socket buffer to be transmitted

    :param struct net_device \*dev:
        Pointer to the network device

.. _`xemaclite_send.description`:

Description
-----------

This function checks if the Tx buffer of the Emaclite device is free to send
data. If so, it fills the Tx buffer with data from socket buffer data,
updates the stats and frees the socket buffer. The Tx completion is signaled
by an interrupt. If the Tx buffer isn't free, then the socket buffer is
deferred and the Tx queue is stopped so that the deferred socket buffer can
be transmitted when the Emaclite device is free to transmit data.

.. _`xemaclite_send.return`:

Return
------

0, always.

.. _`xemaclite_remove_ndev`:

xemaclite_remove_ndev
=====================

.. c:function:: void xemaclite_remove_ndev(struct net_device *ndev)

    Free the network device

    :param struct net_device \*ndev:
        Pointer to the network device to be freed

.. _`xemaclite_remove_ndev.description`:

Description
-----------

This function un maps the IO region of the Emaclite device and frees the net
device.

.. _`get_bool`:

get_bool
========

.. c:function:: bool get_bool(struct platform_device *ofdev, const char *s)

    Get a parameter from the OF device

    :param struct platform_device \*ofdev:
        Pointer to OF device structure

    :param const char \*s:
        Property to be retrieved

.. _`get_bool.description`:

Description
-----------

This function looks for a property in the device node and returns the value
of the property if its found or 0 if the property is not found.

.. _`get_bool.return`:

Return
------

Value of the parameter if the parameter is found, or 0 otherwise

.. _`xemaclite_of_probe`:

xemaclite_of_probe
==================

.. c:function:: int xemaclite_of_probe(struct platform_device *ofdev)

    Probe method for the Emaclite device.

    :param struct platform_device \*ofdev:
        Pointer to OF device structure

.. _`xemaclite_of_probe.description`:

Description
-----------

This function probes for the Emaclite device in the device tree.
It initializes the driver data structure and the hardware, sets the MAC
address and registers the network device.
It also registers a mii_bus for the Emaclite device, if MDIO is included
in the device.

.. _`xemaclite_of_probe.return`:

Return
------

0, if the driver is bound to the Emaclite device, or
a negative error if there is failure.

.. _`xemaclite_of_remove`:

xemaclite_of_remove
===================

.. c:function:: int xemaclite_of_remove(struct platform_device *of_dev)

    Unbind the driver from the Emaclite device.

    :param struct platform_device \*of_dev:
        Pointer to OF device structure

.. _`xemaclite_of_remove.description`:

Description
-----------

This function is called if a device is physically removed from the system or
if the driver module is being unloaded. It frees any resources allocated to
the device.

.. _`xemaclite_of_remove.return`:

Return
------

0, always.

.. This file was automatic generated / don't edit.

