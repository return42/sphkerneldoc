.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/netdev.c

.. _`__ew32_prepare`:

\__ew32_prepare
===============

.. c:function:: s32 __ew32_prepare(struct e1000_hw *hw)

    prepare to write to MAC CSR register on certain parts

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`__ew32_prepare.description`:

Description
-----------

When updating the MAC CSR registers, the Manageability Engine (ME) could
be accessing the registers at the same time.  Normally, this is handled in
h/w by an arbiter but on some parts there is a bug that acknowledges Host
accesses later than it should which could result in the register to have
an incorrect value.  Workaround this by checking the FWSM register which
has bit 24 set while ME is accessing MAC CSR registers, wait if it is set
and try again a number of times.

.. _`e1000_regdump`:

e1000_regdump
=============

.. c:function:: void e1000_regdump(struct e1000_hw *hw, struct e1000_reg_info *reginfo)

    register printout routine

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param struct e1000_reg_info \*reginfo:
        pointer to the register info table

.. _`e1000e_dump`:

e1000e_dump
===========

.. c:function:: void e1000e_dump(struct e1000_adapter *adapter)

    Print registers, Tx-ring and Rx-ring

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_desc_unused`:

e1000_desc_unused
=================

.. c:function:: int e1000_desc_unused(struct e1000_ring *ring)

    calculate if we have unused descriptors

    :param struct e1000_ring \*ring:
        *undescribed*

.. _`e1000e_systim_to_hwtstamp`:

e1000e_systim_to_hwtstamp
=========================

.. c:function:: void e1000e_systim_to_hwtstamp(struct e1000_adapter *adapter, struct skb_shared_hwtstamps *hwtstamps, u64 systim)

    convert system time value to hw time stamp

    :param struct e1000_adapter \*adapter:
        board private structure

    :param struct skb_shared_hwtstamps \*hwtstamps:
        time stamp structure to update

    :param u64 systim:
        unsigned 64bit system time value.

.. _`e1000e_systim_to_hwtstamp.description`:

Description
-----------

Convert the system time value stored in the RX/TXSTMP registers into a
hwtstamp which can be used by the upper level time stamping functions.

The 'systim_lock' spinlock is used to protect the consistency of the
system time value. This is needed because reading the 64 bit time
value involves reading two 32 bit registers. The first read latches the
value.

.. _`e1000e_rx_hwtstamp`:

e1000e_rx_hwtstamp
==================

.. c:function:: void e1000e_rx_hwtstamp(struct e1000_adapter *adapter, u32 status, struct sk_buff *skb)

    utility function which checks for Rx time stamp

    :param struct e1000_adapter \*adapter:
        board private structure

    :param u32 status:
        descriptor extended error and status field

    :param struct sk_buff \*skb:
        particular skb to include time stamp

.. _`e1000e_rx_hwtstamp.description`:

Description
-----------

If the time stamp is valid, convert it into the timecounter ns value
and store that result into the shhwtstamps structure which is passed
up the network stack.

.. _`e1000_receive_skb`:

e1000_receive_skb
=================

.. c:function:: void e1000_receive_skb(struct e1000_adapter *adapter, struct net_device *netdev, struct sk_buff *skb, u32 staterr, __le16 vlan)

    helper function to handle Rx indications

    :param struct e1000_adapter \*adapter:
        board private structure

    :param struct net_device \*netdev:
        *undescribed*

    :param struct sk_buff \*skb:
        pointer to sk_buff to be indicated to stack

    :param u32 staterr:
        descriptor extended error and status field as written by hardware

    :param __le16 vlan:
        descriptor vlan field as written by hardware (no le/be conversion)

.. _`e1000_rx_checksum`:

e1000_rx_checksum
=================

.. c:function:: void e1000_rx_checksum(struct e1000_adapter *adapter, u32 status_err, struct sk_buff *skb)

    Receive Checksum Offload

    :param struct e1000_adapter \*adapter:
        board private structure

    :param u32 status_err:
        receive descriptor status and error fields

    :param struct sk_buff \*skb:
        *undescribed*

.. _`e1000_alloc_rx_buffers`:

e1000_alloc_rx_buffers
======================

.. c:function:: void e1000_alloc_rx_buffers(struct e1000_ring *rx_ring, int cleaned_count, gfp_t gfp)

    Replace used receive buffers

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

    :param int cleaned_count:
        *undescribed*

    :param gfp_t gfp:
        *undescribed*

.. _`e1000_alloc_rx_buffers_ps`:

e1000_alloc_rx_buffers_ps
=========================

.. c:function:: void e1000_alloc_rx_buffers_ps(struct e1000_ring *rx_ring, int cleaned_count, gfp_t gfp)

    Replace used receive buffers; packet split

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

    :param int cleaned_count:
        *undescribed*

    :param gfp_t gfp:
        *undescribed*

.. _`e1000_alloc_jumbo_rx_buffers`:

e1000_alloc_jumbo_rx_buffers
============================

.. c:function:: void e1000_alloc_jumbo_rx_buffers(struct e1000_ring *rx_ring, int cleaned_count, gfp_t gfp)

    Replace used jumbo receive buffers

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

    :param int cleaned_count:
        number of buffers to allocate this pass

    :param gfp_t gfp:
        *undescribed*

.. _`e1000_clean_rx_irq`:

e1000_clean_rx_irq
==================

.. c:function:: bool e1000_clean_rx_irq(struct e1000_ring *rx_ring, int *work_done, int work_to_do)

    Send received data up the network stack

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

    :param int \*work_done:
        *undescribed*

    :param int work_to_do:
        *undescribed*

.. _`e1000_clean_rx_irq.description`:

Description
-----------

the return value indicates whether actual cleaning was done, there
is no guarantee that everything was cleaned

.. _`e1000e_tx_hwtstamp_work`:

e1000e_tx_hwtstamp_work
=======================

.. c:function:: void e1000e_tx_hwtstamp_work(struct work_struct *work)

    check for Tx time stamp

    :param struct work_struct \*work:
        pointer to work struct

.. _`e1000e_tx_hwtstamp_work.description`:

Description
-----------

This work function polls the TSYNCTXCTL valid bit to determine when a
timestamp has been taken for the current stored skb.  The timestamp must
be for this skb because only one such packet is allowed in the queue.

.. _`e1000_clean_tx_irq`:

e1000_clean_tx_irq
==================

.. c:function:: bool e1000_clean_tx_irq(struct e1000_ring *tx_ring)

    Reclaim resources after transmit completes

    :param struct e1000_ring \*tx_ring:
        Tx descriptor ring

.. _`e1000_clean_tx_irq.description`:

Description
-----------

the return value indicates whether actual cleaning was done, there
is no guarantee that everything was cleaned

.. _`e1000_clean_rx_irq_ps`:

e1000_clean_rx_irq_ps
=====================

.. c:function:: bool e1000_clean_rx_irq_ps(struct e1000_ring *rx_ring, int *work_done, int work_to_do)

    Send received data up the network stack; packet split

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

    :param int \*work_done:
        *undescribed*

    :param int work_to_do:
        *undescribed*

.. _`e1000_clean_rx_irq_ps.description`:

Description
-----------

the return value indicates whether actual cleaning was done, there
is no guarantee that everything was cleaned

.. _`e1000_consume_page`:

e1000_consume_page
==================

.. c:function:: void e1000_consume_page(struct e1000_buffer *bi, struct sk_buff *skb, u16 length)

    helper function

    :param struct e1000_buffer \*bi:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param u16 length:
        *undescribed*

.. _`e1000_clean_jumbo_rx_irq`:

e1000_clean_jumbo_rx_irq
========================

.. c:function:: bool e1000_clean_jumbo_rx_irq(struct e1000_ring *rx_ring, int *work_done, int work_to_do)

    Send received data up the network stack; legacy

    :param struct e1000_ring \*rx_ring:
        *undescribed*

    :param int \*work_done:
        *undescribed*

    :param int work_to_do:
        *undescribed*

.. _`e1000_clean_jumbo_rx_irq.description`:

Description
-----------

the return value indicates whether actual cleaning was done, there
is no guarantee that everything was cleaned

.. _`e1000_clean_rx_ring`:

e1000_clean_rx_ring
===================

.. c:function:: void e1000_clean_rx_ring(struct e1000_ring *rx_ring)

    Free Rx Buffers per Queue

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

.. _`e1000_intr_msi`:

e1000_intr_msi
==============

.. c:function:: irqreturn_t e1000_intr_msi(int __always_unused irq, void *data)

    Interrupt Handler

    :param int __always_unused irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`e1000_intr`:

e1000_intr
==========

.. c:function:: irqreturn_t e1000_intr(int __always_unused irq, void *data)

    Interrupt Handler

    :param int __always_unused irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`e1000_configure_msix`:

e1000_configure_msix
====================

.. c:function:: void e1000_configure_msix(struct e1000_adapter *adapter)

    Configure MSI-X hardware

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_configure_msix.description`:

Description
-----------

e1000_configure_msix sets up the hardware to properly
generate MSI-X interrupts.

.. _`e1000e_set_interrupt_capability`:

e1000e_set_interrupt_capability
===============================

.. c:function:: void e1000e_set_interrupt_capability(struct e1000_adapter *adapter)

    set MSI or MSI-X if supported

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000e_set_interrupt_capability.description`:

Description
-----------

Attempt to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`e1000_request_msix`:

e1000_request_msix
==================

.. c:function:: int e1000_request_msix(struct e1000_adapter *adapter)

    Initialize MSI-X interrupts

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_request_msix.description`:

Description
-----------

e1000_request_msix allocates MSI-X vectors and requests interrupts from the
kernel.

.. _`e1000_request_irq`:

e1000_request_irq
=================

.. c:function:: int e1000_request_irq(struct e1000_adapter *adapter)

    initialize interrupts

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`e1000_irq_disable`:

e1000_irq_disable
=================

.. c:function:: void e1000_irq_disable(struct e1000_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_irq_enable`:

e1000_irq_enable
================

.. c:function:: void e1000_irq_enable(struct e1000_adapter *adapter)

    Enable default interrupt generation settings

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000e_get_hw_control`:

e1000e_get_hw_control
=====================

.. c:function:: void e1000e_get_hw_control(struct e1000_adapter *adapter)

    get control of the h/w from f/w

    :param struct e1000_adapter \*adapter:
        address of board private structure

.. _`e1000e_get_hw_control.description`:

Description
-----------

e1000e_get_hw_control sets {CTRL_EXT\|SWSM}:DRV_LOAD bit.
For ASF and Pass Through versions of f/w this means that
the driver is loaded. For AMT version (only with 82573)
of the f/w this means that the network i/f is open.

.. _`e1000e_release_hw_control`:

e1000e_release_hw_control
=========================

.. c:function:: void e1000e_release_hw_control(struct e1000_adapter *adapter)

    release control of the h/w to f/w

    :param struct e1000_adapter \*adapter:
        address of board private structure

.. _`e1000e_release_hw_control.description`:

Description
-----------

e1000e_release_hw_control resets {CTRL_EXT\|SWSM}:DRV_LOAD bit.
For ASF and Pass Through versions of f/w this means that the
driver is no longer loaded. For AMT version (only with 82573) i
of the f/w this means that the network i/f is closed.

.. _`e1000_alloc_ring_dma`:

e1000_alloc_ring_dma
====================

.. c:function:: int e1000_alloc_ring_dma(struct e1000_adapter *adapter, struct e1000_ring *ring)

    allocate memory for a ring structure

    :param struct e1000_adapter \*adapter:
        *undescribed*

    :param struct e1000_ring \*ring:
        *undescribed*

.. _`e1000e_setup_tx_resources`:

e1000e_setup_tx_resources
=========================

.. c:function:: int e1000e_setup_tx_resources(struct e1000_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param struct e1000_ring \*tx_ring:
        Tx descriptor ring

.. _`e1000e_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`e1000e_setup_rx_resources`:

e1000e_setup_rx_resources
=========================

.. c:function:: int e1000e_setup_rx_resources(struct e1000_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

.. _`e1000e_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`e1000_clean_tx_ring`:

e1000_clean_tx_ring
===================

.. c:function:: void e1000_clean_tx_ring(struct e1000_ring *tx_ring)

    Free Tx Buffers

    :param struct e1000_ring \*tx_ring:
        Tx descriptor ring

.. _`e1000e_free_tx_resources`:

e1000e_free_tx_resources
========================

.. c:function:: void e1000e_free_tx_resources(struct e1000_ring *tx_ring)

    Free Tx Resources per Queue

    :param struct e1000_ring \*tx_ring:
        Tx descriptor ring

.. _`e1000e_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`e1000e_free_rx_resources`:

e1000e_free_rx_resources
========================

.. c:function:: void e1000e_free_rx_resources(struct e1000_ring *rx_ring)

    Free Rx Resources

    :param struct e1000_ring \*rx_ring:
        Rx descriptor ring

.. _`e1000e_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`e1000_update_itr`:

e1000_update_itr
================

.. c:function:: unsigned int e1000_update_itr(u16 itr_setting, int packets, int bytes)

    update the dynamic ITR value based on statistics

    :param u16 itr_setting:
        current adapter->itr

    :param int packets:
        the number of packets during this measurement interval

    :param int bytes:
        the number of bytes during this measurement interval

.. _`e1000_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.  This functionality is controlled
by the InterruptThrottleRate module parameter.

.. _`e1000e_write_itr`:

e1000e_write_itr
================

.. c:function:: void e1000e_write_itr(struct e1000_adapter *adapter, u32 itr)

    write the ITR value to the appropriate registers

    :param struct e1000_adapter \*adapter:
        address of board private structure

    :param u32 itr:
        new ITR value to program

.. _`e1000e_write_itr.description`:

Description
-----------

e1000e_write_itr determines if the adapter is in MSI-X mode
and, if so, writes the EITR registers with the ITR value.
Otherwise, it writes the ITR value into the ITR register.

.. _`e1000_alloc_queues`:

e1000_alloc_queues
==================

.. c:function:: int e1000_alloc_queues(struct e1000_adapter *adapter)

    Allocate memory for all rings

    :param struct e1000_adapter \*adapter:
        board private structure to initialize

.. _`e1000e_poll`:

e1000e_poll
===========

.. c:function:: int e1000e_poll(struct napi_struct *napi, int weight)

    NAPI Rx polling callback

    :param struct napi_struct \*napi:
        struct associated with this polling callback

    :param int weight:
        number of packets driver is allowed to process this poll

.. _`e1000e_vlan_filter_disable`:

e1000e_vlan_filter_disable
==========================

.. c:function:: void e1000e_vlan_filter_disable(struct e1000_adapter *adapter)

    helper to disable hw VLAN filtering

    :param struct e1000_adapter \*adapter:
        board private structure to initialize

.. _`e1000e_vlan_filter_enable`:

e1000e_vlan_filter_enable
=========================

.. c:function:: void e1000e_vlan_filter_enable(struct e1000_adapter *adapter)

    helper to enable HW VLAN filtering

    :param struct e1000_adapter \*adapter:
        board private structure to initialize

.. _`e1000e_vlan_strip_disable`:

e1000e_vlan_strip_disable
=========================

.. c:function:: void e1000e_vlan_strip_disable(struct e1000_adapter *adapter)

    helper to disable HW VLAN stripping

    :param struct e1000_adapter \*adapter:
        board private structure to initialize

.. _`e1000e_vlan_strip_enable`:

e1000e_vlan_strip_enable
========================

.. c:function:: void e1000e_vlan_strip_enable(struct e1000_adapter *adapter)

    helper to enable HW VLAN stripping

    :param struct e1000_adapter \*adapter:
        board private structure to initialize

.. _`e1000_configure_tx`:

e1000_configure_tx
==================

.. c:function:: void e1000_configure_tx(struct e1000_adapter *adapter)

    Configure Transmit Unit after Reset

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`page_use_count`:

PAGE_USE_COUNT
==============

.. c:function::  PAGE_USE_COUNT( S)

    configure the receive control registers

    :param  S:
        *undescribed*

.. _`e1000_configure_rx`:

e1000_configure_rx
==================

.. c:function:: void e1000_configure_rx(struct e1000_adapter *adapter)

    Configure Receive Unit after Reset

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`e1000e_write_mc_addr_list`:

e1000e_write_mc_addr_list
=========================

.. c:function:: int e1000e_write_mc_addr_list(struct net_device *netdev)

    write multicast addresses to MTA

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000e_write_mc_addr_list.description`:

Description
-----------

Writes multicast address list to the MTA hash table.

.. _`e1000e_write_mc_addr_list.return`:

Return
------

-ENOMEM on failure
0 on no addresses written
X on writing X addresses to MTA

.. _`e1000e_write_uc_addr_list`:

e1000e_write_uc_addr_list
=========================

.. c:function:: int e1000e_write_uc_addr_list(struct net_device *netdev)

    write unicast addresses to RAR table

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000e_write_uc_addr_list.description`:

Description
-----------

Writes unicast address list to the RAR table.

.. _`e1000e_write_uc_addr_list.return`:

Return
------

-ENOMEM on failure/insufficient address space
0 on no addresses written
X on writing X addresses to the RAR table

.. _`e1000e_set_rx_mode`:

e1000e_set_rx_mode
==================

.. c:function:: void e1000e_set_rx_mode(struct net_device *netdev)

    secondary unicast, Multicast and Promiscuous mode set

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000e_set_rx_mode.description`:

Description
-----------

The ndo_set_rx_mode entry point is called whenever the unicast or multicast
address list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper unicast, multicast,
promiscuous mode, and all-multi behavior.

.. _`e1000e_get_base_timinca`:

e1000e_get_base_timinca
=======================

.. c:function:: s32 e1000e_get_base_timinca(struct e1000_adapter *adapter, u32 *timinca)

    get default SYSTIM time increment attributes

    :param struct e1000_adapter \*adapter:
        board private structure

    :param u32 \*timinca:
        pointer to returned time increment attributes

.. _`e1000e_get_base_timinca.description`:

Description
-----------

Get attributes for incrementing the System Time Register SYSTIML/H at
the default base frequency, and set the cyclecounter shift value.

.. _`e1000e_config_hwtstamp`:

e1000e_config_hwtstamp
======================

.. c:function:: int e1000e_config_hwtstamp(struct e1000_adapter *adapter, struct hwtstamp_config *config)

    configure the hwtstamp registers and enable/disable

    :param struct e1000_adapter \*adapter:
        board private structure

    :param struct hwtstamp_config \*config:
        *undescribed*

.. _`e1000e_config_hwtstamp.description`:

Description
-----------

Outgoing time stamping can be enabled and disabled. Play nice and
disable it when requested, although it shouldn't cause any overhead
when no packet needs it. At most one packet in the queue may be
marked for time stamping, otherwise it would be impossible to tell
for sure to which packet the hardware time stamp belongs.

Incoming time stamping has to be configured via the hardware filters.
Not all combinations are supported, in particular event type has to be
specified. Matching the kind of event packet is not supported, with the
exception of "all V2 events regardless of level 2 or 4".

.. _`e1000_configure`:

e1000_configure
===============

.. c:function:: void e1000_configure(struct e1000_adapter *adapter)

    configure the hardware for Rx and Tx

    :param struct e1000_adapter \*adapter:
        private board structure

.. _`e1000e_power_up_phy`:

e1000e_power_up_phy
===================

.. c:function:: void e1000e_power_up_phy(struct e1000_adapter *adapter)

    restore link in case the phy was powered down

    :param struct e1000_adapter \*adapter:
        address of board private structure

.. _`e1000e_power_up_phy.description`:

Description
-----------

The phy may be powered down to save power and turn off link when the
driver is unloaded and wake on lan is not enabled (among others)
\*\*\* this routine MUST be followed by a call to e1000e_reset \*\*\*

.. _`e1000_power_down_phy`:

e1000_power_down_phy
====================

.. c:function:: void e1000_power_down_phy(struct e1000_adapter *adapter)

    Power down the PHY

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_power_down_phy.description`:

Description
-----------

Power down the PHY so no link is implied when interface is down.
The PHY cannot be powered down if management or WoL is active.

.. _`e1000_flush_tx_ring`:

e1000_flush_tx_ring
===================

.. c:function:: void e1000_flush_tx_ring(struct e1000_adapter *adapter)

    remove all descriptors from the tx_ring

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_flush_tx_ring.description`:

Description
-----------

We want to clear all pending descriptors from the TX ring.
zeroing happens when the HW reads the regs. We  assign the ring itself as
the data of the next descriptor. We don't care about the data we are about
to reset the HW.

.. _`e1000_flush_rx_ring`:

e1000_flush_rx_ring
===================

.. c:function:: void e1000_flush_rx_ring(struct e1000_adapter *adapter)

    remove all descriptors from the rx_ring

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_flush_rx_ring.description`:

Description
-----------

Mark all descriptors in the RX ring as consumed and disable the rx ring

.. _`e1000_flush_desc_rings`:

e1000_flush_desc_rings
======================

.. c:function:: void e1000_flush_desc_rings(struct e1000_adapter *adapter)

    remove all descriptors from the descriptor rings

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000_flush_desc_rings.description`:

Description
-----------

In i219, the descriptor rings must be emptied before resetting the HW
or before changing the device state to D3 during runtime (runtime PM).

Failure to do this will cause the HW to enter a unit hang state which can
only be released by PCI reset on the device

.. _`e1000e_systim_reset`:

e1000e_systim_reset
===================

.. c:function:: void e1000e_systim_reset(struct e1000_adapter *adapter)

    reset the timesync registers after a hardware reset

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000e_systim_reset.description`:

Description
-----------

When the MAC is reset, all hardware bits for timesync will be reset to the
default values. This function will restore the settings last in place.
Since the clock SYSTIME registers are reset, we will simply restore the
cyclecounter to the kernel real clock time.

.. _`e1000e_reset`:

e1000e_reset
============

.. c:function:: void e1000e_reset(struct e1000_adapter *adapter)

    bring the hardware into a known good state

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000e_reset.description`:

Description
-----------

This function boots the hardware and enables some settings that
require a configuration cycle of the hardware - those cannot be
set/changed during runtime. After reset the device needs to be
properly configured for Rx, Tx etc.

.. _`e1000e_trigger_lsc`:

e1000e_trigger_lsc
==================

.. c:function:: void e1000e_trigger_lsc(struct e1000_adapter *adapter)

    trigger an LSC interrupt

    :param struct e1000_adapter \*adapter:
        *undescribed*

.. _`e1000e_trigger_lsc.description`:

Description
-----------

Fire a link status change interrupt to start the watchdog.

.. _`e1000e_down`:

e1000e_down
===========

.. c:function:: void e1000e_down(struct e1000_adapter *adapter, bool reset)

    quiesce the device and optionally reset the hardware

    :param struct e1000_adapter \*adapter:
        board private structure

    :param bool reset:
        boolean flag to reset the hardware or not

.. _`e1000e_sanitize_systim`:

e1000e_sanitize_systim
======================

.. c:function:: u64 e1000e_sanitize_systim(struct e1000_hw *hw, u64 systim)

    sanitize raw cycle counter reads

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u64 systim:
        time value read, sanitized and returned

.. _`e1000e_sanitize_systim.description`:

Description
-----------

Errata for 82574/82583 possible bad bits read from SYSTIMH/L:
check to see that the time is incrementing at a reasonable
rate and is a multiple of incvalue.

.. _`e1000e_cyclecounter_read`:

e1000e_cyclecounter_read
========================

.. c:function:: u64 e1000e_cyclecounter_read(const struct cyclecounter *cc)

    read raw cycle counter (used by time counter)

    :param const struct cyclecounter \*cc:
        cyclecounter structure

.. _`e1000_sw_init`:

e1000_sw_init
=============

.. c:function:: int e1000_sw_init(struct e1000_adapter *adapter)

    Initialize general software structures (struct e1000_adapter)

    :param struct e1000_adapter \*adapter:
        board private structure to initialize

.. _`e1000_sw_init.description`:

Description
-----------

e1000_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`e1000_intr_msi_test`:

e1000_intr_msi_test
===================

.. c:function:: irqreturn_t e1000_intr_msi_test(int __always_unused irq, void *data)

    Interrupt Handler

    :param int __always_unused irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`e1000_test_msi_interrupt`:

e1000_test_msi_interrupt
========================

.. c:function:: int e1000_test_msi_interrupt(struct e1000_adapter *adapter)

    Returns 0 for successful test

    :param struct e1000_adapter \*adapter:
        board private struct

.. _`e1000_test_msi_interrupt.description`:

Description
-----------

code flow taken from tg3.c

.. _`e1000_test_msi`:

e1000_test_msi
==============

.. c:function:: int e1000_test_msi(struct e1000_adapter *adapter)

    Returns 0 if MSI test succeeds or INTx mode is restored

    :param struct e1000_adapter \*adapter:
        board private struct

.. _`e1000_test_msi.description`:

Description
-----------

code flow taken from tg3.c, called with e1000 interrupts disabled.

.. _`e1000e_open`:

e1000e_open
===========

.. c:function:: int e1000e_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000e_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`e1000e_close`:

e1000e_close
============

.. c:function:: int e1000e_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000e_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`e1000_set_mac`:

e1000_set_mac
=============

.. c:function:: int e1000_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`e1000_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`e1000e_update_phy_task`:

e1000e_update_phy_task
======================

.. c:function:: void e1000e_update_phy_task(struct work_struct *work)

    work thread to update phy

    :param struct work_struct \*work:
        pointer to our work struct

.. _`e1000e_update_phy_task.description`:

Description
-----------

this worker thread exists because we must acquire a
semaphore to read the phy, which we could msleep while
waiting for it, and we can't msleep in a timer.

.. _`e1000_update_phy_info`:

e1000_update_phy_info
=====================

.. c:function:: void e1000_update_phy_info(struct timer_list *t)

    timre call-back to update PHY info

    :param struct timer_list \*t:
        *undescribed*

.. _`e1000_update_phy_info.description`:

Description
-----------

Need to wait a few seconds after link up to get diagnostic information from
the phy

.. _`e1000e_update_phy_stats`:

e1000e_update_phy_stats
=======================

.. c:function:: void e1000e_update_phy_stats(struct e1000_adapter *adapter)

    Update the PHY statistics counters

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000e_update_phy_stats.description`:

Description
-----------

Read/clear the upper 16-bit PHY registers and read/accumulate lower

.. _`e1000e_update_stats`:

e1000e_update_stats
===================

.. c:function:: void e1000e_update_stats(struct e1000_adapter *adapter)

    Update the board statistics counters

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_phy_read_status`:

e1000_phy_read_status
=====================

.. c:function:: void e1000_phy_read_status(struct e1000_adapter *adapter)

    Update the PHY register status snapshot

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_watchdog`:

e1000_watchdog
==============

.. c:function:: void e1000_watchdog(struct timer_list *t)

    Timer Call-back

    :param struct timer_list \*t:
        *undescribed*

.. _`e1000_tx_timeout`:

e1000_tx_timeout
================

.. c:function:: void e1000_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000e_get_stats64`:

e1000e_get_stats64
==================

.. c:function:: void e1000e_get_stats64(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    Get System Network Statistics

    :param struct net_device \*netdev:
        network interface device structure

    :param struct rtnl_link_stats64 \*stats:
        rtnl_link_stats64 pointer

.. _`e1000e_get_stats64.description`:

Description
-----------

Returns the address of the device statistics structure.

.. _`e1000_change_mtu`:

e1000_change_mtu
================

.. c:function:: int e1000_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`e1000_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`e1000e_hwtstamp_set`:

e1000e_hwtstamp_set
===================

.. c:function:: int e1000e_hwtstamp_set(struct net_device *netdev, struct ifreq *ifr)

    control hardware time stamping

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ifreq \*ifr:
        *undescribed*

.. _`e1000e_hwtstamp_set.description`:

Description
-----------

Outgoing time stamping can be enabled and disabled. Play nice and
disable it when requested, although it shouldn't cause any overhead
when no packet needs it. At most one packet in the queue may be
marked for time stamping, otherwise it would be impossible to tell
for sure to which packet the hardware time stamp belongs.

Incoming time stamping has to be configured via the hardware filters.
Not all combinations are supported, in particular event type has to be
specified. Matching the kind of event packet is not supported, with the
exception of "all V2 events regardless of level 2 or 4".

.. _`__e1000e_disable_aspm`:

\__e1000e_disable_aspm
======================

.. c:function:: void __e1000e_disable_aspm(struct pci_dev *pdev, u16 state, int locked)

    Disable ASPM states

    :param struct pci_dev \*pdev:
        pointer to PCI device struct

    :param u16 state:
        bit-mask of ASPM states to disable

    :param int locked:
        indication if this context holds pci_bus_sem locked.

.. _`__e1000e_disable_aspm.description`:

Description
-----------

Some devices \*must\* have certain ASPM states disabled per hardware errata.

.. _`e1000e_disable_aspm`:

e1000e_disable_aspm
===================

.. c:function:: void e1000e_disable_aspm(struct pci_dev *pdev, u16 state)

    Disable ASPM states.

    :param struct pci_dev \*pdev:
        pointer to PCI device struct

    :param u16 state:
        bit-mask of ASPM states to disable

.. _`e1000e_disable_aspm.description`:

Description
-----------

This function acquires the pci_bus_sem!
Some devices \*must\* have certain ASPM states disabled per hardware errata.

.. _`e1000e_disable_aspm_locked`:

e1000e_disable_aspm_locked
==========================

.. c:function:: void e1000e_disable_aspm_locked(struct pci_dev *pdev, u16 state)

    :param struct pci_dev \*pdev:
        pointer to PCI device struct

    :param u16 state:
        bit-mask of ASPM states to disable

.. _`e1000e_disable_aspm_locked.description`:

Description
-----------

This function must be called with pci_bus_sem acquired!
Some devices \*must\* have certain ASPM states disabled per hardware errata.

.. _`e1000_netpoll`:

e1000_netpoll
=============

.. c:function:: void e1000_netpoll(struct net_device *netdev)

    :param struct net_device \*netdev:
        network interface device structure

.. _`e1000_netpoll.description`:

Description
-----------

Polling 'interrupt' - used by things like netconsole to send skbs
without having to re-enable interrupts. It's not called while
the interrupt routine is executing.

.. _`e1000_io_error_detected`:

e1000_io_error_detected
=======================

.. c:function:: pci_ers_result_t e1000_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`e1000_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`e1000_io_slot_reset`:

e1000_io_slot_reset
===================

.. c:function:: pci_ers_result_t e1000_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`e1000_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot. Implementation
resembles the first-half of the e1000e_pm_resume routine.

.. _`e1000_io_resume`:

e1000_io_resume
===============

.. c:function:: void e1000_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`e1000_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation. Implementation resembles the
second-half of the e1000e_pm_resume routine.

.. _`e1000_probe`:

e1000_probe
===========

.. c:function:: int e1000_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in e1000_pci_tbl

.. _`e1000_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

e1000_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`e1000_remove`:

e1000_remove
============

.. c:function:: void e1000_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`e1000_remove.description`:

Description
-----------

e1000_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`e1000_init_module`:

e1000_init_module
=================

.. c:function:: int e1000_init_module( void)

    Driver Registration Routine

    :param  void:
        no arguments

.. _`e1000_init_module.description`:

Description
-----------

e1000_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`e1000_exit_module`:

e1000_exit_module
=================

.. c:function:: void __exit e1000_exit_module( void)

    Driver Exit Cleanup Routine

    :param  void:
        no arguments

.. _`e1000_exit_module.description`:

Description
-----------

e1000_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.

