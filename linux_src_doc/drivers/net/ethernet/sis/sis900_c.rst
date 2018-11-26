.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sis/sis900.c

.. _`sis900_get_mac_addr`:

sis900_get_mac_addr
===================

.. c:function:: int sis900_get_mac_addr(struct pci_dev *pci_dev, struct net_device *net_dev)

    Get MAC address for stand alone SiS900 model

    :param pci_dev:
        the sis900 pci device
    :type pci_dev: struct pci_dev \*

    :param net_dev:
        the net device to get address for
    :type net_dev: struct net_device \*

.. _`sis900_get_mac_addr.description`:

Description
-----------

Older SiS900 and friends, use EEPROM to store MAC address.
MAC address is read from \ :c:func:`read_eeprom`\  into \ ``net_dev->dev_addr``\ .

.. _`sis630e_get_mac_addr`:

sis630e_get_mac_addr
====================

.. c:function:: int sis630e_get_mac_addr(struct pci_dev *pci_dev, struct net_device *net_dev)

    Get MAC address for SiS630E model

    :param pci_dev:
        the sis900 pci device
    :type pci_dev: struct pci_dev \*

    :param net_dev:
        the net device to get address for
    :type net_dev: struct net_device \*

.. _`sis630e_get_mac_addr.description`:

Description
-----------

SiS630E model, use APC CMOS RAM to store MAC address.
APC CMOS RAM is accessed through ISA bridge.
MAC address is read into \ ``net_dev->dev_addr``\ .

.. _`sis635_get_mac_addr`:

sis635_get_mac_addr
===================

.. c:function:: int sis635_get_mac_addr(struct pci_dev *pci_dev, struct net_device *net_dev)

    Get MAC address for SIS635 model

    :param pci_dev:
        the sis900 pci device
    :type pci_dev: struct pci_dev \*

    :param net_dev:
        the net device to get address for
    :type net_dev: struct net_device \*

.. _`sis635_get_mac_addr.description`:

Description
-----------

SiS635 model, set MAC Reload Bit to load Mac address from APC
to rfdr. rfdr is accessed through rfcr. MAC address is read into
\ ``net_dev->dev_addr``\ .

.. _`sis96x_get_mac_addr`:

sis96x_get_mac_addr
===================

.. c:function:: int sis96x_get_mac_addr(struct pci_dev *pci_dev, struct net_device *net_dev)

    Get MAC address for SiS962 or SiS963 model

    :param pci_dev:
        the sis900 pci device
    :type pci_dev: struct pci_dev \*

    :param net_dev:
        the net device to get address for
    :type net_dev: struct net_device \*

.. _`sis96x_get_mac_addr.description`:

Description
-----------

SiS962 or SiS963 model, use EEPROM to store MAC address. And EEPROM
is shared by
LAN and 1394. When access EEPROM, send EEREQ signal to hardware first
and wait for EEGNT. If EEGNT is ON, EEPROM is permitted to be access
by LAN, otherwise is not. After MAC address is read from EEPROM, send
EEDONE signal to refuse EEPROM access by LAN.
The EEPROM map of SiS962 or SiS963 is different to SiS900.
The signature field in SiS962 or SiS963 spec is meaningless.
MAC address is read into \ ``net_dev->dev_addr``\ .

.. _`sis900_probe`:

sis900_probe
============

.. c:function:: int sis900_probe(struct pci_dev *pci_dev, const struct pci_device_id *pci_id)

    Probe for sis900 device

    :param pci_dev:
        the sis900 pci device
    :type pci_dev: struct pci_dev \*

    :param pci_id:
        the pci device ID
    :type pci_id: const struct pci_device_id \*

.. _`sis900_probe.description`:

Description
-----------

Check and probe sis900 net device for \ ``pci_dev``\ .
Get mac address according to the chip revision,
and assign SiS900-specific entries in the device structure.
ie: \ :c:func:`sis900_open`\ , \ :c:func:`sis900_start_xmit`\ , \ :c:func:`sis900_close`\ , etc.

.. _`sis900_mii_probe`:

sis900_mii_probe
================

.. c:function:: int sis900_mii_probe(struct net_device *net_dev)

    Probe MII PHY for sis900

    :param net_dev:
        the net device to probe for
    :type net_dev: struct net_device \*

.. _`sis900_mii_probe.description`:

Description
-----------

Search for total of 32 possible mii phy addresses.
Identify and set current phy if found one,
return error if it failed to found.

.. _`sis900_default_phy`:

sis900_default_phy
==================

.. c:function:: u16 sis900_default_phy(struct net_device *net_dev)

    Select default PHY for sis900 mac.

    :param net_dev:
        the net device to probe for
    :type net_dev: struct net_device \*

.. _`sis900_default_phy.description`:

Description
-----------

Select first detected PHY with link as default.
If no one is link on, select PHY whose types is HOME as default.
If HOME doesn't exist, select LAN.

.. _`sis900_set_capability`:

sis900_set_capability
=====================

.. c:function:: void sis900_set_capability(struct net_device *net_dev, struct mii_phy *phy)

    set the media capability of network adapter.

    :param net_dev:
        the net device to probe for
    :type net_dev: struct net_device \*

    :param phy:
        default PHY
    :type phy: struct mii_phy \*

.. _`sis900_set_capability.description`:

Description
-----------

Set the media capability of network adapter according to
mii status register. It's necessary before auto-negotiate.

.. _`read_eeprom`:

read_eeprom
===========

.. c:function:: u16 read_eeprom(void __iomem *ioaddr, int location)

    Read Serial EEPROM

    :param ioaddr:
        base i/o address
    :type ioaddr: void __iomem \*

    :param location:
        the EEPROM location to read
    :type location: int

.. _`read_eeprom.description`:

Description
-----------

Read Serial EEPROM through EEPROM Access Register.
Note that location is in word (16 bits) unit

.. _`mdio_read`:

mdio_read
=========

.. c:function:: int mdio_read(struct net_device *net_dev, int phy_id, int location)

    read MII PHY register

    :param net_dev:
        the net device to read
    :type net_dev: struct net_device \*

    :param phy_id:
        the phy address to read
    :type phy_id: int

    :param location:
        the phy regiester id to read
    :type location: int

.. _`mdio_read.description`:

Description
-----------

Read MII registers through MDIO and MDC
using MDIO management frame structure and protocol(defined by ISO/IEC).
Please see SiS7014 or ICS spec

.. _`mdio_write`:

mdio_write
==========

.. c:function:: void mdio_write(struct net_device *net_dev, int phy_id, int location, int value)

    write MII PHY register

    :param net_dev:
        the net device to write
    :type net_dev: struct net_device \*

    :param phy_id:
        the phy address to write
    :type phy_id: int

    :param location:
        the phy regiester id to write
    :type location: int

    :param value:
        the register value to write with
    :type value: int

.. _`mdio_write.description`:

Description
-----------

Write MII registers with \ ``value``\  through MDIO and MDC
using MDIO management frame structure and protocol(defined by ISO/IEC)
please see SiS7014 or ICS spec

.. _`sis900_reset_phy`:

sis900_reset_phy
================

.. c:function:: u16 sis900_reset_phy(struct net_device *net_dev, int phy_addr)

    reset sis900 mii phy.

    :param net_dev:
        the net device to write
    :type net_dev: struct net_device \*

    :param phy_addr:
        default phy address
    :type phy_addr: int

.. _`sis900_reset_phy.description`:

Description
-----------

Some specific phy can't work properly without reset.
This function will be called during initialization and
link status change from ON to DOWN.

.. _`sis900_open`:

sis900_open
===========

.. c:function:: int sis900_open(struct net_device *net_dev)

    open sis900 device

    :param net_dev:
        the net device to open
    :type net_dev: struct net_device \*

.. _`sis900_open.description`:

Description
-----------

Do some initialization and start net interface.
enable interrupts and set sis900 timer.

.. _`sis900_init_rxfilter`:

sis900_init_rxfilter
====================

.. c:function:: void sis900_init_rxfilter(struct net_device *net_dev)

    Initialize the Rx filter

    :param net_dev:
        the net device to initialize for
    :type net_dev: struct net_device \*

.. _`sis900_init_rxfilter.description`:

Description
-----------

Set receive filter address to our MAC address
and enable packet filtering.

.. _`sis900_init_tx_ring`:

sis900_init_tx_ring
===================

.. c:function:: void sis900_init_tx_ring(struct net_device *net_dev)

    Initialize the Tx descriptor ring

    :param net_dev:
        the net device to initialize for
    :type net_dev: struct net_device \*

.. _`sis900_init_tx_ring.description`:

Description
-----------

Initialize the Tx descriptor ring,

.. _`sis900_init_rx_ring`:

sis900_init_rx_ring
===================

.. c:function:: void sis900_init_rx_ring(struct net_device *net_dev)

    Initialize the Rx descriptor ring

    :param net_dev:
        the net device to initialize for
    :type net_dev: struct net_device \*

.. _`sis900_init_rx_ring.description`:

Description
-----------

Initialize the Rx descriptor ring,
and pre-allocate recevie buffers (socket buffer)

.. _`sis630_set_eq`:

sis630_set_eq
=============

.. c:function:: void sis630_set_eq(struct net_device *net_dev, u8 revision)

    set phy equalizer value for 630 LAN

    :param net_dev:
        the net device to set equalizer value
    :type net_dev: struct net_device \*

    :param revision:
        630 LAN revision number
    :type revision: u8

.. _`sis630_set_eq.description`:

Description
-----------

630E equalizer workaround rule(Cyrus Huang 08/15)
PHY register 14h(Test)

.. _`sis630_set_eq.bit-14`:

Bit 14
------

0 -- Automatically detect (default)
1 -- Manually set Equalizer filter

.. _`sis630_set_eq.bit-13`:

Bit 13
------

0 -- (Default)
1 -- Speed up convergence of equalizer setting
Bit 9 : 0 -- (Default)
1 -- Disable Baseline Wander
Bit 3~7   -- Equalizer filter setting

.. _`sis630_set_eq.link-on`:

Link ON
-------

Set Bit 9, 13 to 1, Bit 14 to 0
Then calculate equalizer value
Then set equalizer value, and set Bit 14 to 1, Bit 9 to 0
Link Off:Set Bit 13 to 1, Bit 14 to 0

.. _`sis630_set_eq.calculate-equalizer-value`:

Calculate Equalizer value
-------------------------

When Link is ON and Bit 14 is 0, SIS900PHY will auto-detect proper equalizer value.
When the equalizer is stable, this value is not a fixed value. It will be within
a small range(eg. 7~9). Then we get a minimum and a maximum value(eg. min=7, max=9)
0 <= max <= 4  --> set equalizer to max
5 <= max <= 14 --> set equalizer to max+1 or set equalizer to max+2 if max == min
max >= 15      --> set equalizer to max+5 or set equalizer to max+6 if max == min

.. _`sis900_timer`:

sis900_timer
============

.. c:function:: void sis900_timer(struct timer_list *t)

    sis900 timer routine

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`sis900_timer.description`:

Description
-----------

On each timer ticks we check two things,
link status (ON/OFF) and link mode (10/100/Full/Half)

.. _`sis900_check_mode`:

sis900_check_mode
=================

.. c:function:: void sis900_check_mode(struct net_device *net_dev, struct mii_phy *mii_phy)

    check the media mode for sis900

    :param net_dev:
        the net device to be checked
    :type net_dev: struct net_device \*

    :param mii_phy:
        the mii phy
    :type mii_phy: struct mii_phy \*

.. _`sis900_check_mode.description`:

Description
-----------

Older driver gets the media mode from mii status output
register. Now we set our media capability and auto-negotiate
to get the upper bound of speed and duplex between two ends.
If the types of mii phy is HOME, it doesn't need to auto-negotiate
and autong_complete should be set to 1.

.. _`sis900_set_mode`:

sis900_set_mode
===============

.. c:function:: void sis900_set_mode(struct sis900_private *sp, int speed, int duplex)

    Set the media mode of mac register.

    :param sp:
        the device private data
    :type sp: struct sis900_private \*

    :param speed:
        the transmit speed to be determined
    :type speed: int

    :param duplex:
        the duplex mode to be determined
    :type duplex: int

.. _`sis900_set_mode.description`:

Description
-----------

Set the media mode of mac register txcfg/rxcfg according to
speed and duplex of phy. Bit EDB_MASTER_EN indicates the EDB
bus is used instead of PCI bus. When this bit is set 1, the
Max DMA Burst Size for TX/RX DMA should be no larger than 16
double words.

.. _`sis900_auto_negotiate`:

sis900_auto_negotiate
=====================

.. c:function:: void sis900_auto_negotiate(struct net_device *net_dev, int phy_addr)

    Set the Auto-Negotiation Enable/Reset bit.

    :param net_dev:
        the net device to read mode for
    :type net_dev: struct net_device \*

    :param phy_addr:
        mii phy address
    :type phy_addr: int

.. _`sis900_auto_negotiate.description`:

Description
-----------

If the adapter is link-on, set the auto-negotiate enable/reset bit.
autong_complete should be set to 0 when starting auto-negotiation.
autong_complete should be set to 1 if we didn't start auto-negotiation.
sis900_timer will wait for link on again if autong_complete = 0.

.. _`sis900_read_mode`:

sis900_read_mode
================

.. c:function:: void sis900_read_mode(struct net_device *net_dev, int *speed, int *duplex)

    read media mode for sis900 internal phy

    :param net_dev:
        the net device to read mode for
    :type net_dev: struct net_device \*

    :param speed:
        the transmit speed to be determined
    :type speed: int \*

    :param duplex:
        the duplex mode to be determined
    :type duplex: int \*

.. _`sis900_read_mode.description`:

Description
-----------

The capability of remote end will be put in mii register autorec
after auto-negotiation. Use AND operation to get the upper bound
of speed and duplex between two ends.

.. _`sis900_tx_timeout`:

sis900_tx_timeout
=================

.. c:function:: void sis900_tx_timeout(struct net_device *net_dev)

    sis900 transmit timeout routine

    :param net_dev:
        the net device to transmit
    :type net_dev: struct net_device \*

.. _`sis900_tx_timeout.description`:

Description
-----------

print transmit timeout status
disable interrupts and do some tasks

.. _`sis900_start_xmit`:

sis900_start_xmit
=================

.. c:function:: netdev_tx_t sis900_start_xmit(struct sk_buff *skb, struct net_device *net_dev)

    sis900 start transmit routine

    :param skb:
        socket buffer pointer to put the data being transmitted
    :type skb: struct sk_buff \*

    :param net_dev:
        the net device to transmit with
    :type net_dev: struct net_device \*

.. _`sis900_start_xmit.description`:

Description
-----------

Set the transmit buffer descriptor,
and write TxENA to enable transmit state machine.
tell upper layer if the buffer is full

.. _`sis900_interrupt`:

sis900_interrupt
================

.. c:function:: irqreturn_t sis900_interrupt(int irq, void *dev_instance)

    sis900 interrupt handler

    :param irq:
        the irq number
    :type irq: int

    :param dev_instance:
        the client data object
    :type dev_instance: void \*

.. _`sis900_interrupt.description`:

Description
-----------

The interrupt handler does all of the Rx thread work,
and cleans up after the Tx thread

.. _`sis900_rx`:

sis900_rx
=========

.. c:function:: int sis900_rx(struct net_device *net_dev)

    sis900 receive routine

    :param net_dev:
        the net device which receives data
    :type net_dev: struct net_device \*

.. _`sis900_rx.description`:

Description
-----------

Process receive interrupt events,
put buffer to higher layer and refill buffer pool

.. _`sis900_rx.note`:

Note
----

This function is called by interrupt handler,
don't do "too much" work here

.. _`sis900_finish_xmit`:

sis900_finish_xmit
==================

.. c:function:: void sis900_finish_xmit(struct net_device *net_dev)

    finish up transmission of packets

    :param net_dev:
        the net device to be transmitted on
    :type net_dev: struct net_device \*

.. _`sis900_finish_xmit.description`:

Description
-----------

Check for error condition and free socket buffer etc
schedule for more transmission as needed

.. _`sis900_finish_xmit.note`:

Note
----

This function is called by interrupt handler,
don't do "too much" work here

.. _`sis900_close`:

sis900_close
============

.. c:function:: int sis900_close(struct net_device *net_dev)

    close sis900 device

    :param net_dev:
        the net device to be closed
    :type net_dev: struct net_device \*

.. _`sis900_close.description`:

Description
-----------

Disable interrupts, stop the Tx and Rx Status Machine
free Tx and RX socket buffer

.. _`sis900_get_drvinfo`:

sis900_get_drvinfo
==================

.. c:function:: void sis900_get_drvinfo(struct net_device *net_dev, struct ethtool_drvinfo *info)

    Return information about driver

    :param net_dev:
        the net device to probe
    :type net_dev: struct net_device \*

    :param info:
        container for info returned
    :type info: struct ethtool_drvinfo \*

.. _`sis900_get_drvinfo.description`:

Description
-----------

Process ethtool command such as "ehtool -i" to show information

.. _`sis900_set_wol`:

sis900_set_wol
==============

.. c:function:: int sis900_set_wol(struct net_device *net_dev, struct ethtool_wolinfo *wol)

    Set up Wake on Lan registers

    :param net_dev:
        the net device to probe
    :type net_dev: struct net_device \*

    :param wol:
        container for info passed to the driver
    :type wol: struct ethtool_wolinfo \*

.. _`sis900_set_wol.description`:

Description
-----------

Process ethtool command "wol" to setup wake on lan features.
SiS900 supports sending WoL events if a correct packet is received,
but there is no simple way to filter them to only a subset (broadcast,
multicast, unicast or arp).

.. _`mii_ioctl`:

mii_ioctl
=========

.. c:function:: int mii_ioctl(struct net_device *net_dev, struct ifreq *rq, int cmd)

    process MII i/o control command

    :param net_dev:
        the net device to command for
    :type net_dev: struct net_device \*

    :param rq:
        parameter for command
    :type rq: struct ifreq \*

    :param cmd:
        the i/o command
    :type cmd: int

.. _`mii_ioctl.description`:

Description
-----------

Process MII command like read/write MII register

.. _`sis900_set_config`:

sis900_set_config
=================

.. c:function:: int sis900_set_config(struct net_device *dev, struct ifmap *map)

    Set media type by net_device.set_config

    :param dev:
        the net device for media type change
    :type dev: struct net_device \*

    :param map:
        ifmap passed by ifconfig
    :type map: struct ifmap \*

.. _`sis900_set_config.description`:

Description
-----------

Set media type to 10baseT, 100baseT or 0(for auto) by ifconfig
we support only port changes. All other runtime configuration
changes will be ignored

.. _`sis900_mcast_bitnr`:

sis900_mcast_bitnr
==================

.. c:function:: u16 sis900_mcast_bitnr(u8 *addr, u8 revision)

    compute hashtable index

    :param addr:
        multicast address
    :type addr: u8 \*

    :param revision:
        revision id of chip
    :type revision: u8

.. _`sis900_mcast_bitnr.description`:

Description
-----------

SiS 900 uses the most sigificant 7 bits to index a 128 bits multicast
hash table, which makes this function a little bit different from other drivers
SiS 900 B0 & 635 M/B uses the most significat 8 bits to index 256 bits
multicast hash table.

.. _`set_rx_mode`:

set_rx_mode
===========

.. c:function:: void set_rx_mode(struct net_device *net_dev)

    Set SiS900 receive mode

    :param net_dev:
        the net device to be set
    :type net_dev: struct net_device \*

.. _`set_rx_mode.description`:

Description
-----------

Set SiS900 receive mode for promiscuous, multicast, or broadcast mode.
And set the appropriate multicast filter.
Multicast hash table changes from 128 to 256 bits for 635M/B & 900B0.

.. _`sis900_reset`:

sis900_reset
============

.. c:function:: void sis900_reset(struct net_device *net_dev)

    Reset sis900 MAC

    :param net_dev:
        the net device to reset
    :type net_dev: struct net_device \*

.. _`sis900_reset.description`:

Description
-----------

reset sis900 MAC and wait until finished
reset through command register
change backoff algorithm for 900B0 & 635 M/B

.. _`sis900_remove`:

sis900_remove
=============

.. c:function:: void sis900_remove(struct pci_dev *pci_dev)

    Remove sis900 device

    :param pci_dev:
        the pci device to be removed
    :type pci_dev: struct pci_dev \*

.. _`sis900_remove.description`:

Description
-----------

remove and release SiS900 net device

.. This file was automatic generated / don't edit.

