.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_main.c

.. _`pch_gbe_mac_read_mac_addr`:

pch_gbe_mac_read_mac_addr
=========================

.. c:function:: s32 pch_gbe_mac_read_mac_addr(struct pch_gbe_hw *hw)

    Read MAC address

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_mac_read_mac_addr.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_wait_clr_bit`:

pch_gbe_wait_clr_bit
====================

.. c:function:: void pch_gbe_wait_clr_bit(void *reg, u32 bit)

    Wait to clear a bit

    :param void \*reg:
        Pointer of register

    :param u32 bit:
        *undescribed*

.. _`pch_gbe_mac_mar_set`:

pch_gbe_mac_mar_set
===================

.. c:function:: void pch_gbe_mac_mar_set(struct pch_gbe_hw *hw, u8 *addr, u32 index)

    Set MAC address register

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u8 \*addr:
        Pointer to the MAC address

    :param u32 index:
        MAC address array register

.. _`pch_gbe_mac_reset_hw`:

pch_gbe_mac_reset_hw
====================

.. c:function:: void pch_gbe_mac_reset_hw(struct pch_gbe_hw *hw)

    Reset hardware

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_mac_init_rx_addrs`:

pch_gbe_mac_init_rx_addrs
=========================

.. c:function:: void pch_gbe_mac_init_rx_addrs(struct pch_gbe_hw *hw, u16 mar_count)

    Initialize receive address's

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u16 mar_count:
        Receive address registers

.. _`pch_gbe_mac_mc_addr_list_update`:

pch_gbe_mac_mc_addr_list_update
===============================

.. c:function:: void pch_gbe_mac_mc_addr_list_update(struct pch_gbe_hw *hw, u8 *mc_addr_list, u32 mc_addr_count, u32 mar_used_count, u32 mar_total_num)

    Update Multicast addresses

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u8 \*mc_addr_list:
        Array of multicast addresses to program

    :param u32 mc_addr_count:
        Number of multicast addresses to program

    :param u32 mar_used_count:
        The first MAC Address register free to program

    :param u32 mar_total_num:
        Total number of supported MAC Address Registers

.. _`pch_gbe_mac_force_mac_fc`:

pch_gbe_mac_force_mac_fc
========================

.. c:function:: s32 pch_gbe_mac_force_mac_fc(struct pch_gbe_hw *hw)

    Force the MAC's flow control settings

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

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

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u32 wu_evt:
        Wake up event

.. _`pch_gbe_mac_ctrl_miim`:

pch_gbe_mac_ctrl_miim
=====================

.. c:function:: u16 pch_gbe_mac_ctrl_miim(struct pch_gbe_hw *hw, u32 addr, u32 dir, u32 reg, u16 data)

    Control MIIM interface

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u32 addr:
        Address of PHY

    :param u32 dir:
        Operetion. (Write or Read)

    :param u32 reg:
        Access register of PHY

    :param u16 data:
        Write data.

.. _`pch_gbe_mac_ctrl_miim.return`:

Return
------

Read date.

.. _`pch_gbe_mac_set_pause_packet`:

pch_gbe_mac_set_pause_packet
============================

.. c:function:: void pch_gbe_mac_set_pause_packet(struct pch_gbe_hw *hw)

    Set pause packet

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_alloc_queues`:

pch_gbe_alloc_queues
====================

.. c:function:: int pch_gbe_alloc_queues(struct pch_gbe_adapter *adapter)

    Allocate memory for all rings

    :param struct pch_gbe_adapter \*adapter:
        Board private structure to initialize

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure to initialize

.. _`pch_gbe_init_phy`:

pch_gbe_init_phy
================

.. c:function:: int pch_gbe_init_phy(struct pch_gbe_adapter *adapter)

    Initialize PHY

    :param struct pch_gbe_adapter \*adapter:
        Board private structure to initialize

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

    :param struct net_device \*netdev:
        Network interface device structure

    :param int addr:
        Phy ID

    :param int reg:
        Access location

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

    :param struct net_device \*netdev:
        Network interface device structure

    :param int addr:
        Phy ID (not used)

    :param int reg:
        Access location

    :param int data:
        Write data

.. _`pch_gbe_reset_task`:

pch_gbe_reset_task
==================

.. c:function:: void pch_gbe_reset_task(struct work_struct *work)

    Reset processing at the time of transmission timeout

    :param struct work_struct \*work:
        Pointer of board private structure

.. _`pch_gbe_reinit_locked`:

pch_gbe_reinit_locked
=====================

.. c:function:: void pch_gbe_reinit_locked(struct pch_gbe_adapter *adapter)

    Re-initialization

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_reset`:

pch_gbe_reset
=============

.. c:function:: void pch_gbe_reset(struct pch_gbe_adapter *adapter)

    Reset GbE

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_free_irq`:

pch_gbe_free_irq
================

.. c:function:: void pch_gbe_free_irq(struct pch_gbe_adapter *adapter)

    Free an interrupt

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_irq_disable`:

pch_gbe_irq_disable
===================

.. c:function:: void pch_gbe_irq_disable(struct pch_gbe_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_irq_enable`:

pch_gbe_irq_enable
==================

.. c:function:: void pch_gbe_irq_enable(struct pch_gbe_adapter *adapter)

    Enable default interrupt generation settings

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_setup_tctl`:

pch_gbe_setup_tctl
==================

.. c:function:: void pch_gbe_setup_tctl(struct pch_gbe_adapter *adapter)

    configure the Transmit control registers

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_configure_tx`:

pch_gbe_configure_tx
====================

.. c:function:: void pch_gbe_configure_tx(struct pch_gbe_adapter *adapter)

    Configure Transmit Unit after Reset

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_setup_rctl`:

pch_gbe_setup_rctl
==================

.. c:function:: void pch_gbe_setup_rctl(struct pch_gbe_adapter *adapter)

    Configure the receive control registers

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_configure_rx`:

pch_gbe_configure_rx
====================

.. c:function:: void pch_gbe_configure_rx(struct pch_gbe_adapter *adapter)

    Configure Receive Unit after Reset

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_unmap_and_free_tx_resource`:

pch_gbe_unmap_and_free_tx_resource
==================================

.. c:function:: void pch_gbe_unmap_and_free_tx_resource(struct pch_gbe_adapter *adapter, struct pch_gbe_buffer *buffer_info)

    Unmap and free tx socket buffer

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_buffer \*buffer_info:
        Buffer information structure

.. _`pch_gbe_unmap_and_free_rx_resource`:

pch_gbe_unmap_and_free_rx_resource
==================================

.. c:function:: void pch_gbe_unmap_and_free_rx_resource(struct pch_gbe_adapter *adapter, struct pch_gbe_buffer *buffer_info)

    Unmap and free rx socket buffer

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_buffer \*buffer_info:
        Buffer information structure

.. _`pch_gbe_clean_tx_ring`:

pch_gbe_clean_tx_ring
=====================

.. c:function:: void pch_gbe_clean_tx_ring(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Free Tx Buffers

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_tx_ring \*tx_ring:
        Ring to be cleaned

.. _`pch_gbe_clean_rx_ring`:

pch_gbe_clean_rx_ring
=====================

.. c:function:: void pch_gbe_clean_rx_ring(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring)

    Free Rx Buffers

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_rx_ring \*rx_ring:
        Ring to free buffers from

.. _`pch_gbe_watchdog`:

pch_gbe_watchdog
================

.. c:function:: void pch_gbe_watchdog(unsigned long data)

    Watchdog process

    :param unsigned long data:
        Board private structure

.. _`pch_gbe_tx_queue`:

pch_gbe_tx_queue
================

.. c:function:: void pch_gbe_tx_queue(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring, struct sk_buff *skb)

    Carry out queuing of the transmission data

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_tx_ring \*tx_ring:
        Tx descriptor ring structure

    :param struct sk_buff \*skb:
        Sockt buffer structure

.. _`pch_gbe_update_stats`:

pch_gbe_update_stats
====================

.. c:function:: void pch_gbe_update_stats(struct pch_gbe_adapter *adapter)

    Update the board statistics counters

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_intr`:

pch_gbe_intr
============

.. c:function:: irqreturn_t pch_gbe_intr(int irq, void *data)

    Interrupt Handler

    :param int irq:
        Interrupt number

    :param void \*data:
        Pointer to a network interface device structure

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_rx_ring \*rx_ring:
        Rx descriptor ring

    :param int cleaned_count:
        Cleaned count

.. _`pch_gbe_alloc_tx_buffers`:

pch_gbe_alloc_tx_buffers
========================

.. c:function:: void pch_gbe_alloc_tx_buffers(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Allocate transmit buffers

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_tx_ring \*tx_ring:
        Tx descriptor ring

.. _`pch_gbe_clean_tx`:

pch_gbe_clean_tx
================

.. c:function:: bool pch_gbe_clean_tx(struct pch_gbe_adapter *adapter, struct pch_gbe_tx_ring *tx_ring)

    Reclaim resources after transmit completes

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_tx_ring \*tx_ring:
        Tx descriptor ring

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_rx_ring \*rx_ring:
        Rx descriptor ring

    :param int \*work_done:
        Completed count

    :param int work_to_do:
        Request count

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_tx_ring \*tx_ring:
        Tx descriptor ring (for a specific queue) to setup

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_rx_ring \*rx_ring:
        Rx descriptor ring (for a specific queue) to setup

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_tx_ring \*tx_ring:
        Tx descriptor ring for a specific queue

.. _`pch_gbe_free_rx_resources`:

pch_gbe_free_rx_resources
=========================

.. c:function:: void pch_gbe_free_rx_resources(struct pch_gbe_adapter *adapter, struct pch_gbe_rx_ring *rx_ring)

    Free Rx Resources

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

    :param struct pch_gbe_rx_ring \*rx_ring:
        Ring to clean the resources from

.. _`pch_gbe_request_irq`:

pch_gbe_request_irq
===================

.. c:function:: int pch_gbe_request_irq(struct pch_gbe_adapter *adapter)

    Allocate an interrupt line

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

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

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_sw_init`:

pch_gbe_sw_init
===============

.. c:function:: int pch_gbe_sw_init(struct pch_gbe_adapter *adapter)

    Initialize general software structures (struct pch_gbe_adapter)

    :param struct pch_gbe_adapter \*adapter:
        Board private structure to initialize

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

    :param struct net_device \*netdev:
        Network interface device structure

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

    :param struct net_device \*netdev:
        Network interface device structure

.. _`pch_gbe_stop.return`:

Return
------

0: Successfully

.. _`pch_gbe_xmit_frame`:

pch_gbe_xmit_frame
==================

.. c:function:: int pch_gbe_xmit_frame(struct sk_buff *skb, struct net_device *netdev)

    Packet transmitting start

    :param struct sk_buff \*skb:
        Socket buffer structure

    :param struct net_device \*netdev:
        Network interface device structure

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

    :param struct net_device \*netdev:
        Network interface device structure

.. _`pch_gbe_set_mac`:

pch_gbe_set_mac
===============

.. c:function:: int pch_gbe_set_mac(struct net_device *netdev, void *addr)

    Change the Ethernet Address of the NIC

    :param struct net_device \*netdev:
        Network interface device structure

    :param void \*addr:
        Pointer to an address structure

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

    :param struct net_device \*netdev:
        Network interface device structure

    :param int new_mtu:
        New value for maximum frame size

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

    :param struct net_device \*netdev:
        Network interface device structure

    :param netdev_features_t features:
        New features

.. _`pch_gbe_set_features.return`:

Return
------

0:              HW state updated successfully

.. _`pch_gbe_ioctl`:

pch_gbe_ioctl
=============

.. c:function:: int pch_gbe_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    Controls register through a MII interface

    :param struct net_device \*netdev:
        Network interface device structure

    :param struct ifreq \*ifr:
        Pointer to ifr structure

    :param int cmd:
        Control command

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

    :param struct net_device \*netdev:
        Network interface device structure

.. _`pch_gbe_napi_poll`:

pch_gbe_napi_poll
=================

.. c:function:: int pch_gbe_napi_poll(struct napi_struct *napi, int budget)

    NAPI receive and transfer polling callback

    :param struct napi_struct \*napi:
        Pointer of polling device struct

    :param int budget:
        The maximum number of a packet

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

    :param struct net_device \*netdev:
        Network interface device structure

.. This file was automatic generated / don't edit.

