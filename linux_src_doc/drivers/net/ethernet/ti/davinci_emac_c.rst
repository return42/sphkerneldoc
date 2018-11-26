.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ti/davinci_emac.c

.. _`emac_get_drvinfo`:

emac_get_drvinfo
================

.. c:function:: void emac_get_drvinfo(struct net_device *ndev, struct ethtool_drvinfo *info)

    Get EMAC driver information

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

    :param info:
        ethtool info structure containing name and version
    :type info: struct ethtool_drvinfo \*

.. _`emac_get_drvinfo.description`:

Description
-----------

Returns EMAC driver information (name and version)

.. _`emac_get_coalesce`:

emac_get_coalesce
=================

.. c:function:: int emac_get_coalesce(struct net_device *ndev, struct ethtool_coalesce *coal)

    Get interrupt coalesce settings for this device

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

    :param coal:
        ethtool coalesce settings structure
    :type coal: struct ethtool_coalesce \*

.. _`emac_get_coalesce.description`:

Description
-----------

Fetch the current interrupt coalesce settings

.. _`emac_set_coalesce`:

emac_set_coalesce
=================

.. c:function:: int emac_set_coalesce(struct net_device *ndev, struct ethtool_coalesce *coal)

    Set interrupt coalesce settings for this device

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

    :param coal:
        ethtool coalesce settings structure
    :type coal: struct ethtool_coalesce \*

.. _`emac_set_coalesce.description`:

Description
-----------

Set interrupt coalesce parameters

.. _`emac_update_phystatus`:

emac_update_phystatus
=====================

.. c:function:: void emac_update_phystatus(struct emac_priv *priv)

    Update Phy status

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

.. _`emac_update_phystatus.description`:

Description
-----------

Updates phy status and takes action for network queue if required
based upon link status

.. _`hash_get`:

hash_get
========

.. c:function:: u32 hash_get(u8 *addr)

    Calculate hash value from mac address

    :param addr:
        mac address to delete from hash table
    :type addr: u8 \*

.. _`hash_get.description`:

Description
-----------

Calculates hash value from mac address

.. _`emac_hash_add`:

emac_hash_add
=============

.. c:function:: int emac_hash_add(struct emac_priv *priv, u8 *mac_addr)

    Hash function to add mac addr from hash table

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param mac_addr:
        mac address to delete from hash table
    :type mac_addr: u8 \*

.. _`emac_hash_add.description`:

Description
-----------

Adds mac address to the internal hash table

.. _`emac_hash_del`:

emac_hash_del
=============

.. c:function:: int emac_hash_del(struct emac_priv *priv, u8 *mac_addr)

    Hash function to delete mac addr from hash table

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param mac_addr:
        mac address to delete from hash table
    :type mac_addr: u8 \*

.. _`emac_hash_del.description`:

Description
-----------

Removes mac address from the internal hash table

.. _`emac_add_mcast`:

emac_add_mcast
==============

.. c:function:: void emac_add_mcast(struct emac_priv *priv, u32 action, u8 *mac_addr)

    Set multicast address in the EMAC adapter (Internal)

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param action:
        multicast operation to perform
    :type action: u32

    :param mac_addr:
        *undescribed*
    :type mac_addr: u8 \*

.. _`emac_add_mcast.mac_addr`:

mac_addr
--------

mac address to set

Set multicast addresses in EMAC adapter - internal function

.. _`emac_dev_mcast_set`:

emac_dev_mcast_set
==================

.. c:function:: void emac_dev_mcast_set(struct net_device *ndev)

    Set multicast address in the EMAC adapter

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_dev_mcast_set.description`:

Description
-----------

Set multicast addresses in EMAC adapter

.. _`emac_int_disable`:

emac_int_disable
================

.. c:function:: void emac_int_disable(struct emac_priv *priv)

    Disable EMAC module interrupt (from adapter)

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

.. _`emac_int_disable.description`:

Description
-----------

Disable EMAC interrupt on the adapter

.. _`emac_int_enable`:

emac_int_enable
===============

.. c:function:: void emac_int_enable(struct emac_priv *priv)

    Enable EMAC module interrupt (from adapter)

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

.. _`emac_int_enable.description`:

Description
-----------

Enable EMAC interrupt on the adapter

.. _`emac_irq`:

emac_irq
========

.. c:function:: irqreturn_t emac_irq(int irq, void *dev_id)

    EMAC interrupt handler

    :param irq:
        interrupt number
    :type irq: int

    :param dev_id:
        EMAC network adapter data structure ptr
    :type dev_id: void \*

.. _`emac_irq.description`:

Description
-----------

EMAC Interrupt handler - we only schedule NAPI and not process any packets
here. EVen the interrupt status is checked (TX/RX/Err) in NAPI poll function

Returns interrupt handled condition

.. _`emac_dev_xmit`:

emac_dev_xmit
=============

.. c:function:: int emac_dev_xmit(struct sk_buff *skb, struct net_device *ndev)

    EMAC Transmit function

    :param skb:
        SKB pointer
    :type skb: struct sk_buff \*

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_dev_xmit.description`:

Description
-----------

Called by the system to transmit a packet  - we queue the packet in
EMAC hardware transmit queue

Returns success(NETDEV_TX_OK) or error code (typically out of desc's)

.. _`emac_dev_tx_timeout`:

emac_dev_tx_timeout
===================

.. c:function:: void emac_dev_tx_timeout(struct net_device *ndev)

    EMAC Transmit timeout function

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_dev_tx_timeout.description`:

Description
-----------

Called when system detects that a skb timeout period has expired
potentially due to a fault in the adapter in not being able to send
it out on the wire. We teardown the TX channel assuming a hardware
error and re-initialize the TX channel for hardware operation

.. _`emac_set_type0addr`:

emac_set_type0addr
==================

.. c:function:: void emac_set_type0addr(struct emac_priv *priv, u32 ch, char *mac_addr)

    Set EMAC Type0 mac address

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param ch:
        RX channel number
    :type ch: u32

    :param mac_addr:
        MAC address to set in device
    :type mac_addr: char \*

.. _`emac_set_type0addr.description`:

Description
-----------

Called internally to set Type0 mac address of the adapter (Device)

Returns success (0) or appropriate error code (none as of now)

.. _`emac_set_type1addr`:

emac_set_type1addr
==================

.. c:function:: void emac_set_type1addr(struct emac_priv *priv, u32 ch, char *mac_addr)

    Set EMAC Type1 mac address

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param ch:
        RX channel number
    :type ch: u32

    :param mac_addr:
        MAC address to set in device
    :type mac_addr: char \*

.. _`emac_set_type1addr.description`:

Description
-----------

Called internally to set Type1 mac address of the adapter (Device)

Returns success (0) or appropriate error code (none as of now)

.. _`emac_set_type2addr`:

emac_set_type2addr
==================

.. c:function:: void emac_set_type2addr(struct emac_priv *priv, u32 ch, char *mac_addr, int index, int match)

    Set EMAC Type2 mac address

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param ch:
        RX channel number
    :type ch: u32

    :param mac_addr:
        MAC address to set in device
    :type mac_addr: char \*

    :param index:
        index into RX address entries
    :type index: int

    :param match:
        match parameter for RX address matching logic
    :type match: int

.. _`emac_set_type2addr.description`:

Description
-----------

Called internally to set Type2 mac address of the adapter (Device)

Returns success (0) or appropriate error code (none as of now)

.. _`emac_setmac`:

emac_setmac
===========

.. c:function:: void emac_setmac(struct emac_priv *priv, u32 ch, char *mac_addr)

    Set mac address in the adapter (internal function)

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

    :param ch:
        RX channel number
    :type ch: u32

    :param mac_addr:
        MAC address to set in device
    :type mac_addr: char \*

.. _`emac_setmac.description`:

Description
-----------

Called internally to set the mac address of the adapter (Device)

Returns success (0) or appropriate error code (none as of now)

.. _`emac_dev_setmac_addr`:

emac_dev_setmac_addr
====================

.. c:function:: int emac_dev_setmac_addr(struct net_device *ndev, void *addr)

    Set mac address in the adapter

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

    :param addr:
        MAC address to set in device
    :type addr: void \*

.. _`emac_dev_setmac_addr.description`:

Description
-----------

Called by the system to set the mac address of the adapter (Device)

Returns success (0) or appropriate error code (none as of now)

.. _`emac_hw_enable`:

emac_hw_enable
==============

.. c:function:: int emac_hw_enable(struct emac_priv *priv)

    Enable EMAC hardware for packet transmission/reception

    :param priv:
        The DaVinci EMAC private adapter structure
    :type priv: struct emac_priv \*

.. _`emac_hw_enable.description`:

Description
-----------

Enables EMAC hardware for packet processing - enables PHY, enables RX
for packet reception and enables device interrupts and then NAPI

Returns success (0) or appropriate error code (none right now)

.. _`emac_poll`:

emac_poll
=========

.. c:function:: int emac_poll(struct napi_struct *napi, int budget)

    EMAC NAPI Poll function

    :param napi:
        *undescribed*
    :type napi: struct napi_struct \*

    :param budget:
        Number of receive packets to process (as told by NAPI layer)
    :type budget: int

.. _`emac_poll.description`:

Description
-----------

NAPI Poll function implemented to process packets as per budget. We check
the type of interrupt on the device and accordingly call the TX or RX
packet processing functions. We follow the budget for RX processing and
also put a cap on number of TX pkts processed through config param. The
NAPI schedule function is called if more packets pending.

Returns number of packets received (in most cases; else TX pkts - rarely)

.. _`emac_poll_controller`:

emac_poll_controller
====================

.. c:function:: void emac_poll_controller(struct net_device *ndev)

    EMAC Poll controller function

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_poll_controller.description`:

Description
-----------

Polled functionality used by netconsole and others in non interrupt mode

.. _`emac_devioctl`:

emac_devioctl
=============

.. c:function:: int emac_devioctl(struct net_device *ndev, struct ifreq *ifrq, int cmd)

    EMAC adapter ioctl

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

    :param ifrq:
        request parameter
    :type ifrq: struct ifreq \*

    :param cmd:
        command parameter
    :type cmd: int

.. _`emac_devioctl.description`:

Description
-----------

EMAC driver ioctl function

Returns success(0) or appropriate error code

.. _`emac_dev_open`:

emac_dev_open
=============

.. c:function:: int emac_dev_open(struct net_device *ndev)

    EMAC device open

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_dev_open.description`:

Description
-----------

Called when system wants to start the interface. We init TX/RX channels
and enable the hardware for packet reception/transmission and start the
network queue.

Returns 0 for a successful open, or appropriate error code

.. _`emac_dev_stop`:

emac_dev_stop
=============

.. c:function:: int emac_dev_stop(struct net_device *ndev)

    EMAC device stop

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_dev_stop.description`:

Description
-----------

Called when system wants to stop or down the interface. We stop the network
queue, disable interrupts and cleanup TX/RX channels.

We return the statistics in net_device_stats structure pulled from emac

.. _`emac_dev_getnetstats`:

emac_dev_getnetstats
====================

.. c:function:: struct net_device_stats *emac_dev_getnetstats(struct net_device *ndev)

    EMAC get statistics function

    :param ndev:
        The DaVinci EMAC network adapter
    :type ndev: struct net_device \*

.. _`emac_dev_getnetstats.description`:

Description
-----------

Called when system wants to get statistics from the device.

We return the statistics in net_device_stats structure pulled from emac

.. _`davinci_emac_probe`:

davinci_emac_probe
==================

.. c:function:: int davinci_emac_probe(struct platform_device *pdev)

    EMAC device probe

    :param pdev:
        The DaVinci EMAC device that we are removing
    :type pdev: struct platform_device \*

.. _`davinci_emac_probe.description`:

Description
-----------

Called when probing for emac devicesr. We get details of instances and
resource information from platform init and register a network device
and allocate resources necessary for driver to perform

.. _`davinci_emac_remove`:

davinci_emac_remove
===================

.. c:function:: int davinci_emac_remove(struct platform_device *pdev)

    EMAC device remove

    :param pdev:
        The DaVinci EMAC device that we are removing
    :type pdev: struct platform_device \*

.. _`davinci_emac_remove.description`:

Description
-----------

Called when removing the device driver. We disable clock usage and release
the resources taken up by the driver and unregister network device

.. _`davinci_emac_init`:

davinci_emac_init
=================

.. c:function:: int davinci_emac_init( void)

    EMAC driver module init

    :param void:
        no arguments
    :type void: 

.. _`davinci_emac_init.description`:

Description
-----------

Called when initializing the driver. We register the driver with
the platform.

.. _`davinci_emac_exit`:

davinci_emac_exit
=================

.. c:function:: void __exit davinci_emac_exit( void)

    EMAC driver module exit

    :param void:
        no arguments
    :type void: 

.. _`davinci_emac_exit.description`:

Description
-----------

Called when exiting the driver completely. We unregister the driver with
the platform and exit

.. This file was automatic generated / don't edit.

