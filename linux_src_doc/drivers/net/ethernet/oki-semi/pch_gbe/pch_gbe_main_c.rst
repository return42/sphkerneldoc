.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_main.c

.. _`pch_gbe_mac_read_mac_addr`:

pch_gbe_mac_read_mac_addr
=========================

.. c:function:: s32 pch_gbe_mac_read_mac_addr(struct pch_gbe_hw *hw)

    Read MAC address

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_mac_read_mac_addr.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_wait_clr_bit`:

pch_gbe_wait_clr_bit
====================

.. c:function:: void pch_gbe_wait_clr_bit(void *reg, u32 bit)

    Wait to clear a bit

    :param reg:
        Pointer of register
    :type reg: void \*

    :param bit:
        *undescribed*
    :type bit: u32

.. _`pch_gbe_mac_mar_set`:

pch_gbe_mac_mar_set
===================

.. c:function:: void pch_gbe_mac_mar_set(struct pch_gbe_hw *hw, u8 *addr, u32 index)

    Set MAC address register

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

    :param addr:
        Pointer to the MAC address
    :type addr: u8 \*

    :param index:
        MAC address array register
    :type index: u32

.. _`pch_gbe_mac_reset_hw`:

pch_gbe_mac_reset_hw
====================

.. c:function:: void pch_gbe_mac_reset_hw(struct pch_gbe_hw *hw)

    Reset hardware

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_mac_init_rx_addrs`:

pch_gbe_mac_init_rx_addrs
=========================

.. c:function:: void pch_gbe_mac_init_rx_addrs(struct pch_gbe_hw *hw, u16 mar_count)

    Initialize receive address's

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

    :param mar_count:
        Receive address registers
    :type mar_count: u16

.. _`pch_gbe_mac_force_mac_fc`:

pch_gbe_mac_force_mac_fc
========================

.. c:function:: s32 pch_gbe_mac_force_mac_fc(struct pch_gbe_hw *hw)

    Force the MAC's flow control settings

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_mac_force_mac_fc.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_mac_force_mac_fc.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_mac_set_wol_event`:

pch_gbe_mac_set_wol_event
=========================

.. c:function:: void pch_gbe_mac_set_wol_event(struct pch_gbe_hw *hw, u32 wu_evt)

    Set wake-on-lan event

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

    :param wu_evt:
        Wake up event
    :type wu_evt: u32

.. _`pch_gbe_mac_ctrl_miim`:

pch_gbe_mac_ctrl_miim
=====================

.. c:function:: u16 pch_gbe_mac_ctrl_miim(struct pch_gbe_hw *hw, u32 addr, u32 dir, u32 reg, u16 data)

    Control MIIM interface

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

    :param addr:
        Address of PHY
    :type addr: u32

    :param dir:
        Operetion. (Write or Read)
    :type dir: u32

    :param reg:
        Access register of PHY
    :type reg: u32

    :param data:
        Write data.
    :type data: u16

.. _`pch_gbe_mac_ctrl_miim.return`:

Return
------

Read date.

.. _`pch_gbe_mac_set_pause_packet`:

pch_gbe_mac_set_pause_packet
============================

.. c:function:: void pch_gbe_mac_set_pause_packet(struct pch_gbe_hw *hw)

    Set pause packet

    :param hw:
        Pointer to the HW structure
    :type hw: struct pch_gbe_hw \*

.. _`pch_gbe_alloc_queues`:

pch_gbe_alloc_queues
====================

.. c:function:: int pch_gbe_alloc_queues(struct pch_gbe_adapter *adapter)

    Allocate memory for all rings

    :param adapter:
        Board private structure to initialize
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_alloc_queues.return`:

Return
------

0:      Successfully

.. _`pch_gbe_alloc_queues.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_init_stats`:

pch_gbe_init_stats
==================

.. c:function:: void pch_gbe_init_stats(struct pch_gbe_adapter *adapter)

    Initialize status

    :param adapter:
        Board private structure to initialize
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_init_phy`:

pch_gbe_init_phy
================

.. c:function:: int pch_gbe_init_phy(struct pch_gbe_adapter *adapter)

    Initialize PHY

    :param adapter:
        Board private structure to initialize
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_init_phy.return`:

Return
------

0:      Successfully

.. _`pch_gbe_init_phy.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_mdio_read`:

pch_gbe_mdio_read
=================

.. c:function:: int pch_gbe_mdio_read(struct net_device *netdev, int addr, int reg)

    The read function for mii

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param addr:
        Phy ID
    :type addr: int

    :param reg:
        Access location
    :type reg: int

.. _`pch_gbe_mdio_read.return`:

Return
------

0:      Successfully

.. _`pch_gbe_mdio_read.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_mdio_write`:

pch_gbe_mdio_write
==================

.. c:function:: void pch_gbe_mdio_write(struct net_device *netdev, int addr, int reg, int data)

    The write function for mii

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param addr:
        Phy ID (not used)
    :type addr: int

    :param reg:
        Access location
    :type reg: int

    :param data:
        Write data
    :type data: int

.. _`pch_gbe_reset_task`:

pch_gbe_reset_task
==================

.. c:function:: void pch_gbe_reset_task(struct work_struct *work)

    Reset processing at the time of transmission timeout

    :param work:
        Pointer of board private structure
    :type work: struct work_struct \*

.. _`pch_gbe_reinit_locked`:

pch_gbe_reinit_locked
=====================

.. c:function:: void pch_gbe_reinit_locked(struct pch_gbe_adapter *adapter)

    Re-initialization

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_reset`:

pch_gbe_reset
=============

.. c:function:: void pch_gbe_reset(struct pch_gbe_adapter *adapter)

    Reset GbE

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_free_irq`:

pch_gbe_free_irq
================

.. c:function:: void pch_gbe_free_irq(struct pch_gbe_adapter *adapter)

    Free an interrupt

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_irq_disable`:

pch_gbe_irq_disable
===================

.. c:function:: void pch_gbe_irq_disable(struct pch_gbe_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_irq_enable`:

pch_gbe_irq_enable
==================

.. c:function:: void pch_gbe_irq_enable(struct pch_gbe_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_setup_tctl`:

pch_gbe_setup_tctl
==================

.. c:function:: void pch_gbe_setup_tctl(struct pch_gbe_adapter *adapter)

    configure the Transmit control registers

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_configure_tx`:

pch_gbe_configure_tx
====================

.. c:function:: void pch_gbe_configure_tx(struct pch_gbe_adapter *adapter)

    Configure Transmit Unit after Reset

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_setup_rctl`:

pch_gbe_setup_rctl
==================

.. c:function:: void pch_gbe_setup_rctl(struct pch_gbe_adapter *adapter)

    Configure the receive control registers

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_configure_rx`:

pch_gbe_configure_rx
====================

.. c:function:: void pch_gbe_configure_rx(struct pch_gbe_adapter *adapter)

    Configure Receive Unit after Reset

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_unmap_and_free_tx_resource`:

pch_gbe_unmap_and_free_tx_resource
==================================

.. c:function:: void pch_gbe_unmap_and_free_tx_resource(struct pch_gbe_adapter *adapter, struct pch_gbe_buffer *buffer_info)

    Unmap and free tx socket buffer

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param buffer_info:
        Buffer information structure
    :type buffer_info: struct pch_gbe_buffer \*

.. _`pch_gbe_unmap_and_free_rx_resource`:

pch_gbe_unmap_and_free_rx_resource
==================================

.. c:function:: void pch_gbe_unmap_and_free_rx_resource(struct pch_gbe_adapter *adapter, struct pch_gbe_buffer *buffer_info)

    Unmap and free rx socket buffer

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param buffer_info:
        Buffer information structure
    :type buffer_info: struct pch_gbe_buffer \*

.. _`pch_gbe_clean_tx_ring`:

pch_gbe_clean_tx_ring
=====================

.. c:function:: void pch_gbe_clean_tx_ring(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Free Tx Buffers

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param tx_ring:
        Ring to be cleaned
    :type tx_ring: struct pch_gbe_tx_ring \*

.. _`pch_gbe_clean_rx_ring`:

pch_gbe_clean_rx_ring
=====================

.. c:function:: void pch_gbe_clean_rx_ring(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring)

    Free Rx Buffers

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param rx_ring:
        Ring to free buffers from
    :type rx_ring: struct pch_gbe_rx_ring \*

.. _`pch_gbe_watchdog`:

pch_gbe_watchdog
================

.. c:function:: void pch_gbe_watchdog(struct timer_list *t)

    Watchdog process

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`pch_gbe_tx_queue`:

pch_gbe_tx_queue
================

.. c:function:: void pch_gbe_tx_queue(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring, struct sk_buff *skb)

    Carry out queuing of the transmission data

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param tx_ring:
        Tx descriptor ring structure
    :type tx_ring: struct pch_gbe_tx_ring \*

    :param skb:
        Sockt buffer structure
    :type skb: struct sk_buff \*

.. _`pch_gbe_update_stats`:

pch_gbe_update_stats
====================

.. c:function:: void pch_gbe_update_stats(struct pch_gbe_adapter *adapter)

    Update the board statistics counters

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_intr`:

pch_gbe_intr
============

.. c:function:: irqreturn_t pch_gbe_intr(int irq, void *data)

    Interrupt Handler

    :param irq:
        Interrupt number
    :type irq: int

    :param data:
        Pointer to a network interface device structure
    :type data: void \*

.. _`pch_gbe_intr.return`:

Return
------

- IRQ_HANDLED:  Our interrupt
- IRQ_NONE:     Not our interrupt

.. _`pch_gbe_alloc_rx_buffers`:

pch_gbe_alloc_rx_buffers
========================

.. c:function:: void pch_gbe_alloc_rx_buffers(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring, int cleaned_count)

    Replace used receive buffers; legacy & extended

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param rx_ring:
        Rx descriptor ring
    :type rx_ring: struct pch_gbe_rx_ring \*

    :param cleaned_count:
        Cleaned count
    :type cleaned_count: int

.. _`pch_gbe_alloc_tx_buffers`:

pch_gbe_alloc_tx_buffers
========================

.. c:function:: void pch_gbe_alloc_tx_buffers(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Allocate transmit buffers

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param tx_ring:
        Tx descriptor ring
    :type tx_ring: struct pch_gbe_tx_ring \*

.. _`pch_gbe_clean_tx`:

pch_gbe_clean_tx
================

.. c:function:: bool pch_gbe_clean_tx(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Reclaim resources after transmit completes

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param tx_ring:
        Tx descriptor ring
    :type tx_ring: struct pch_gbe_tx_ring \*

.. _`pch_gbe_clean_tx.true`:

true
----

Cleaned the descriptor

.. _`pch_gbe_clean_tx.false`:

false
-----

Not cleaned the descriptor

.. _`pch_gbe_clean_rx`:

pch_gbe_clean_rx
================

.. c:function:: bool pch_gbe_clean_rx(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring, int *work_done, int work_to_do)

    Send received data up the network stack; legacy

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param rx_ring:
        Rx descriptor ring
    :type rx_ring: struct pch_gbe_rx_ring \*

    :param work_done:
        Completed count
    :type work_done: int \*

    :param work_to_do:
        Request count
    :type work_to_do: int

.. _`pch_gbe_clean_rx.true`:

true
----

Cleaned the descriptor

.. _`pch_gbe_clean_rx.false`:

false
-----

Not cleaned the descriptor

.. _`pch_gbe_setup_tx_resources`:

pch_gbe_setup_tx_resources
==========================

.. c:function:: int pch_gbe_setup_tx_resources(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Allocate Tx resources (Descriptors)

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param tx_ring:
        Tx descriptor ring (for a specific queue) to setup
    :type tx_ring: struct pch_gbe_tx_ring \*

.. _`pch_gbe_setup_tx_resources.return`:

Return
------

0:              Successfully

.. _`pch_gbe_setup_tx_resources.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_setup_rx_resources`:

pch_gbe_setup_rx_resources
==========================

.. c:function:: int pch_gbe_setup_rx_resources(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring)

    Allocate Rx resources (Descriptors)

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param rx_ring:
        Rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct pch_gbe_rx_ring \*

.. _`pch_gbe_setup_rx_resources.return`:

Return
------

0:              Successfully

.. _`pch_gbe_setup_rx_resources.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_free_tx_resources`:

pch_gbe_free_tx_resources
=========================

.. c:function:: void pch_gbe_free_tx_resources(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Free Tx Resources

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct pch_gbe_tx_ring \*

.. _`pch_gbe_free_rx_resources`:

pch_gbe_free_rx_resources
=========================

.. c:function:: void pch_gbe_free_rx_resources(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring)

    Free Rx Resources

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

    :param rx_ring:
        Ring to clean the resources from
    :type rx_ring: struct pch_gbe_rx_ring \*

.. _`pch_gbe_request_irq`:

pch_gbe_request_irq
===================

.. c:function:: int pch_gbe_request_irq(struct pch_gbe_adapter *adapter)

    Allocate an interrupt line

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_request_irq.return`:

Return
------

0:              Successfully

.. _`pch_gbe_request_irq.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_up`:

pch_gbe_up
==========

.. c:function:: int pch_gbe_up(struct pch_gbe_adapter *adapter)

    Up GbE network device

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_up.return`:

Return
------

0:              Successfully

.. _`pch_gbe_up.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_down`:

pch_gbe_down
============

.. c:function:: void pch_gbe_down(struct pch_gbe_adapter *adapter)

    Down GbE network device

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_sw_init`:

pch_gbe_sw_init
===============

.. c:function:: int pch_gbe_sw_init(struct pch_gbe_adapter *adapter)

    Initialize general software structures (struct pch_gbe_adapter)

    :param adapter:
        Board private structure to initialize
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_sw_init.return`:

Return
------

0:              Successfully

.. _`pch_gbe_sw_init.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_open`:

pch_gbe_open
============

.. c:function:: int pch_gbe_open(struct net_device *netdev)

    Called when a network interface is made active

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_open.return`:

Return
------

0:              Successfully

.. _`pch_gbe_open.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_stop`:

pch_gbe_stop
============

.. c:function:: int pch_gbe_stop(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_stop.return`:

Return
------

0: Successfully

.. _`pch_gbe_xmit_frame`:

pch_gbe_xmit_frame
==================

.. c:function:: int pch_gbe_xmit_frame(struct sk_buff *skb, struct net_device *netdev)

    Packet transmitting start

    :param skb:
        Socket buffer structure
    :type skb: struct sk_buff \*

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_xmit_frame.return`:

Return
------

- NETDEV_TX_OK:   Normal end
- NETDEV_TX_BUSY: Error end

.. _`pch_gbe_set_multi`:

pch_gbe_set_multi
=================

.. c:function:: void pch_gbe_set_multi(struct net_device *netdev)

    Multicast and Promiscuous mode set

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_set_mac`:

pch_gbe_set_mac
===============

.. c:function:: int pch_gbe_set_mac(struct net_device *netdev, void *addr)

    Change the Ethernet Address of the NIC

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param addr:
        Pointer to an address structure
    :type addr: void \*

.. _`pch_gbe_set_mac.return`:

Return
------

0:              Successfully
-EADDRNOTAVAIL: Failed

.. _`pch_gbe_change_mtu`:

pch_gbe_change_mtu
==================

.. c:function:: int pch_gbe_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        New value for maximum frame size
    :type new_mtu: int

.. _`pch_gbe_change_mtu.return`:

Return
------

0:              Successfully
-EINVAL:        Failed

.. _`pch_gbe_set_features`:

pch_gbe_set_features
====================

.. c:function:: int pch_gbe_set_features(struct net_device *netdev, netdev_features_t features)

    Reset device after features changed

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param features:
        New features
    :type features: netdev_features_t

.. _`pch_gbe_set_features.return`:

Return
------

0:              HW state updated successfully

.. _`pch_gbe_ioctl`:

pch_gbe_ioctl
=============

.. c:function:: int pch_gbe_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    Controls register through a MII interface

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

    :param ifr:
        Pointer to ifr structure
    :type ifr: struct ifreq \*

    :param cmd:
        Control command
    :type cmd: int

.. _`pch_gbe_ioctl.return`:

Return
------

0:      Successfully

.. _`pch_gbe_ioctl.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_tx_timeout`:

pch_gbe_tx_timeout
==================

.. c:function:: void pch_gbe_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. _`pch_gbe_napi_poll`:

pch_gbe_napi_poll
=================

.. c:function:: int pch_gbe_napi_poll(struct napi_struct *napi, int budget)

    NAPI receive and transfer polling callback

    :param napi:
        Pointer of polling device struct
    :type napi: struct napi_struct \*

    :param budget:
        The maximum number of a packet
    :type budget: int

.. _`pch_gbe_napi_poll.false`:

false
-----

Exit the polling mode

.. _`pch_gbe_napi_poll.true`:

true
----

Continue the polling mode

.. _`pch_gbe_netpoll`:

pch_gbe_netpoll
===============

.. c:function:: void pch_gbe_netpoll(struct net_device *netdev)

    Used by things like netconsole to send skbs

    :param netdev:
        Network interface device structure
    :type netdev: struct net_device \*

.. This file was automatic generated / don't edit.

