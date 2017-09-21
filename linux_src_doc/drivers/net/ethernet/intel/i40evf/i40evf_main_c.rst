.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40evf/i40evf_main.c

.. _`i40evf_allocate_dma_mem_d`:

i40evf_allocate_dma_mem_d
=========================

.. c:function:: i40e_status i40evf_allocate_dma_mem_d(struct i40e_hw *hw, struct i40e_dma_mem *mem, u64 size, u32 alignment)

    OS specific memory alloc for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_dma_mem \*mem:
        ptr to mem struct to fill out

    :param u64 size:
        size of memory requested

    :param u32 alignment:
        what to align the allocation to

.. _`i40evf_free_dma_mem_d`:

i40evf_free_dma_mem_d
=====================

.. c:function:: i40e_status i40evf_free_dma_mem_d(struct i40e_hw *hw, struct i40e_dma_mem *mem)

    OS specific memory free for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_dma_mem \*mem:
        ptr to mem struct to free

.. _`i40evf_allocate_virt_mem_d`:

i40evf_allocate_virt_mem_d
==========================

.. c:function:: i40e_status i40evf_allocate_virt_mem_d(struct i40e_hw *hw, struct i40e_virt_mem *mem, u32 size)

    OS specific memory alloc for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_virt_mem \*mem:
        ptr to mem struct to fill out

    :param u32 size:
        size of memory requested

.. _`i40evf_free_virt_mem_d`:

i40evf_free_virt_mem_d
======================

.. c:function:: i40e_status i40evf_free_virt_mem_d(struct i40e_hw *hw, struct i40e_virt_mem *mem)

    OS specific memory free for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_virt_mem \*mem:
        ptr to mem struct to free

.. _`i40evf_debug_d`:

i40evf_debug_d
==============

.. c:function:: void i40evf_debug_d(void *hw, u32 mask, char *fmt_str,  ...)

    OS dependent version of debug printing

    :param void \*hw:
        pointer to the HW structure

    :param u32 mask:
        debug level mask

    :param char \*fmt_str:
        printf-type format description

    :param ... :
        variable arguments

.. _`i40evf_schedule_reset`:

i40evf_schedule_reset
=====================

.. c:function:: void i40evf_schedule_reset(struct i40evf_adapter *adapter)

    Set the flags and schedule a reset event

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_tx_timeout`:

i40evf_tx_timeout
=================

.. c:function:: void i40evf_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_misc_irq_disable`:

i40evf_misc_irq_disable
=======================

.. c:function:: void i40evf_misc_irq_disable(struct i40evf_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_misc_irq_enable`:

i40evf_misc_irq_enable
======================

.. c:function:: void i40evf_misc_irq_enable(struct i40evf_adapter *adapter)

    Enable default interrupt generation settings

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_irq_disable`:

i40evf_irq_disable
==================

.. c:function:: void i40evf_irq_disable(struct i40evf_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_irq_enable_queues`:

i40evf_irq_enable_queues
========================

.. c:function:: void i40evf_irq_enable_queues(struct i40evf_adapter *adapter, u32 mask)

    Enable interrupt for specified queues

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u32 mask:
        bitmap of queues to enable

.. _`i40evf_fire_sw_int`:

i40evf_fire_sw_int
==================

.. c:function:: void i40evf_fire_sw_int(struct i40evf_adapter *adapter, u32 mask)

    Generate SW interrupt for specified vectors

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u32 mask:
        bitmap of vectors to trigger

.. _`i40evf_irq_enable`:

i40evf_irq_enable
=================

.. c:function:: void i40evf_irq_enable(struct i40evf_adapter *adapter, bool flush)

    Enable default interrupt generation settings

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param bool flush:
        boolean value whether to run \ :c:func:`rd32`\ 

.. _`i40evf_msix_aq`:

i40evf_msix_aq
==============

.. c:function:: irqreturn_t i40evf_msix_aq(int irq, void *data)

    Interrupt handler for vector 0

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to netdev

.. _`i40evf_msix_clean_rings`:

i40evf_msix_clean_rings
=======================

.. c:function:: irqreturn_t i40evf_msix_clean_rings(int irq, void *data)

    MSIX mode Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a q_vector

.. _`i40evf_map_vector_to_rxq`:

i40evf_map_vector_to_rxq
========================

.. c:function:: void i40evf_map_vector_to_rxq(struct i40evf_adapter *adapter, int v_idx, int r_idx)

    associate irqs with rx queues

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param int v_idx:
        interrupt number

    :param int r_idx:
        queue number

.. _`i40evf_map_vector_to_txq`:

i40evf_map_vector_to_txq
========================

.. c:function:: void i40evf_map_vector_to_txq(struct i40evf_adapter *adapter, int v_idx, int t_idx)

    associate irqs with tx queues

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param int v_idx:
        interrupt number

    :param int t_idx:
        queue number

.. _`i40evf_map_rings_to_vectors`:

i40evf_map_rings_to_vectors
===========================

.. c:function:: int i40evf_map_rings_to_vectors(struct i40evf_adapter *adapter)

    Maps descriptor rings to vectors

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_map_rings_to_vectors.description`:

Description
-----------

This function maps descriptor rings to the queue-specific vectors
we were allotted through the MSI-X enabling code.  Ideally, we'd have
one vector per ring/queue, but on a constrained vector budget, we
group the rings as "efficiently" as possible.  You would add new
mapping configurations in here.

.. _`i40evf_netpoll`:

i40evf_netpoll
==============

.. c:function:: void i40evf_netpoll(struct net_device *netdev)

    A Polling 'interrupt' handler

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_netpoll.description`:

Description
-----------

This is used by netconsole to send skbs without having to re-enable
interrupts.  It's not called while the normal interrupt routine is executing.

.. _`i40evf_irq_affinity_notify`:

i40evf_irq_affinity_notify
==========================

.. c:function:: void i40evf_irq_affinity_notify(struct irq_affinity_notify *notify, const cpumask_t *mask)

    Callback for affinity changes

    :param struct irq_affinity_notify \*notify:
        context as to what irq was changed

    :param const cpumask_t \*mask:
        the new affinity mask

.. _`i40evf_irq_affinity_notify.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
so that we may register to receive changes to the irq affinity masks.

.. _`i40evf_irq_affinity_release`:

i40evf_irq_affinity_release
===========================

.. c:function:: void i40evf_irq_affinity_release(struct kref *ref)

    Callback for affinity notifier release

    :param struct kref \*ref:
        internal core kernel usage

.. _`i40evf_irq_affinity_release.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
to inform the current notification subscriber that they will no longer
receive notifications.

.. _`i40evf_request_traffic_irqs`:

i40evf_request_traffic_irqs
===========================

.. c:function:: int i40evf_request_traffic_irqs(struct i40evf_adapter *adapter, char *basename)

    Initialize MSI-X interrupts

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param char \*basename:
        *undescribed*

.. _`i40evf_request_traffic_irqs.description`:

Description
-----------

Allocates MSI-X vectors for tx and rx handling, and requests
interrupts from the kernel.

.. _`i40evf_request_misc_irq`:

i40evf_request_misc_irq
=======================

.. c:function:: int i40evf_request_misc_irq(struct i40evf_adapter *adapter)

    Initialize MSI-X interrupts

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_request_misc_irq.description`:

Description
-----------

Allocates MSI-X vector 0 and requests interrupts from the kernel. This
vector is only for the admin queue, and stays active even when the netdev
is closed.

.. _`i40evf_free_traffic_irqs`:

i40evf_free_traffic_irqs
========================

.. c:function:: void i40evf_free_traffic_irqs(struct i40evf_adapter *adapter)

    Free MSI-X interrupts

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_free_traffic_irqs.description`:

Description
-----------

Frees all MSI-X vectors other than 0.

.. _`i40evf_free_misc_irq`:

i40evf_free_misc_irq
====================

.. c:function:: void i40evf_free_misc_irq(struct i40evf_adapter *adapter)

    Free MSI-X miscellaneous vector

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_free_misc_irq.description`:

Description
-----------

Frees MSI-X vector 0.

.. _`i40evf_configure_tx`:

i40evf_configure_tx
===================

.. c:function:: void i40evf_configure_tx(struct i40evf_adapter *adapter)

    Configure Transmit Unit after Reset

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`i40evf_configure_rx`:

i40evf_configure_rx
===================

.. c:function:: void i40evf_configure_rx(struct i40evf_adapter *adapter)

    Configure Receive Unit after Reset

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`i40evf_find_vlan`:

i40evf_find_vlan
================

.. c:function:: struct i40evf_vlan_filter *i40evf_find_vlan(struct i40evf_adapter *adapter, u16 vlan)

    Search filter list for specific vlan filter

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u16 vlan:
        vlan tag

.. _`i40evf_find_vlan.description`:

Description
-----------

Returns ptr to the filter object or NULL

.. _`i40evf_add_vlan`:

i40evf_add_vlan
===============

.. c:function:: struct i40evf_vlan_filter *i40evf_add_vlan(struct i40evf_adapter *adapter, u16 vlan)

    Add a vlan filter to the list

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u16 vlan:
        VLAN tag

.. _`i40evf_add_vlan.description`:

Description
-----------

Returns ptr to the filter object or NULL when no memory available.

.. _`i40evf_del_vlan`:

i40evf_del_vlan
===============

.. c:function:: void i40evf_del_vlan(struct i40evf_adapter *adapter, u16 vlan)

    Remove a vlan filter from the list

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u16 vlan:
        VLAN tag

.. _`i40evf_vlan_rx_add_vid`:

i40evf_vlan_rx_add_vid
======================

.. c:function:: int i40evf_vlan_rx_add_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Add a VLAN filter to a device

    :param struct net_device \*netdev:
        network device struct

    :param __always_unused __be16 proto:
        *undescribed*

    :param u16 vid:
        VLAN tag

.. _`i40evf_vlan_rx_kill_vid`:

i40evf_vlan_rx_kill_vid
=======================

.. c:function:: int i40evf_vlan_rx_kill_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Remove a VLAN filter from a device

    :param struct net_device \*netdev:
        network device struct

    :param __always_unused __be16 proto:
        *undescribed*

    :param u16 vid:
        VLAN tag

.. _`i40evf_find_filter`:

i40evf_find_filter
==================

.. c:function:: struct i40evf_mac_filter *i40evf_find_filter(struct i40evf_adapter *adapter, u8 *macaddr)

    Search filter list for specific mac filter

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u8 \*macaddr:
        the MAC address

.. _`i40evf_find_filter.description`:

Description
-----------

Returns ptr to the filter object or NULL

.. _`i40evf_add_filter`:

i40evf_add_filter
=================

.. c:function:: struct i40evf_mac_filter *i40evf_add_filter(struct i40evf_adapter *adapter, u8 *macaddr)

    Add a mac filter to the filter list

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param u8 \*macaddr:
        the MAC address

.. _`i40evf_add_filter.description`:

Description
-----------

Returns ptr to the filter object or NULL when no memory available.

.. _`i40evf_set_mac`:

i40evf_set_mac
==============

.. c:function:: int i40evf_set_mac(struct net_device *netdev, void *p)

    NDO callback to set port mac address

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`i40evf_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40evf_set_rx_mode`:

i40evf_set_rx_mode
==================

.. c:function:: void i40evf_set_rx_mode(struct net_device *netdev)

    NDO callback to set the netdev filters

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_napi_enable_all`:

i40evf_napi_enable_all
======================

.. c:function:: void i40evf_napi_enable_all(struct i40evf_adapter *adapter)

    enable NAPI on all queue vectors

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_napi_disable_all`:

i40evf_napi_disable_all
=======================

.. c:function:: void i40evf_napi_disable_all(struct i40evf_adapter *adapter)

    disable NAPI on all queue vectors

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_configure`:

i40evf_configure
================

.. c:function:: void i40evf_configure(struct i40evf_adapter *adapter)

    set up transmit and receive data structures

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_up_complete`:

i40evf_up_complete
==================

.. c:function:: void i40evf_up_complete(struct i40evf_adapter *adapter)

    Finish the last steps of bringing up a connection

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_down`:

i40evf_down
===========

.. c:function:: void i40evf_down(struct i40evf_adapter *adapter)

    Shutdown the connection processing

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_acquire_msix_vectors`:

i40evf_acquire_msix_vectors
===========================

.. c:function:: int i40evf_acquire_msix_vectors(struct i40evf_adapter *adapter, int vectors)

    Setup the MSIX capability

    :param struct i40evf_adapter \*adapter:
        board private structure

    :param int vectors:
        number of vectors to request

.. _`i40evf_acquire_msix_vectors.description`:

Description
-----------

Work with the OS to set up the MSIX vectors needed.

Returns 0 on success, negative on failure

.. _`i40evf_free_queues`:

i40evf_free_queues
==================

.. c:function:: void i40evf_free_queues(struct i40evf_adapter *adapter)

    Free memory for all rings

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_free_queues.description`:

Description
-----------

Free all of the memory associated with queue pairs.

.. _`i40evf_alloc_queues`:

i40evf_alloc_queues
===================

.. c:function:: int i40evf_alloc_queues(struct i40evf_adapter *adapter)

    Allocate memory for all rings

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_alloc_queues.description`:

Description
-----------

We allocate one ring per queue at run-time since we don't know the
number of queues at compile-time.  The polling_netdev array is
intended for Multiqueue, but should work fine with a single queue.

.. _`i40evf_set_interrupt_capability`:

i40evf_set_interrupt_capability
===============================

.. c:function:: int i40evf_set_interrupt_capability(struct i40evf_adapter *adapter)

    set MSI-X or FAIL if not supported

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_set_interrupt_capability.description`:

Description
-----------

Attempt to configure the interrupts using the best available
capabilities of the hardware and the kernel.

.. _`i40evf_config_rss_aq`:

i40evf_config_rss_aq
====================

.. c:function:: int i40evf_config_rss_aq(struct i40evf_adapter *adapter)

    Configure RSS keys and lut by using AQ commands

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_config_rss_aq.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`i40evf_config_rss_reg`:

i40evf_config_rss_reg
=====================

.. c:function:: int i40evf_config_rss_reg(struct i40evf_adapter *adapter)

    Configure RSS keys and lut by writing registers

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_config_rss_reg.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40evf_config_rss`:

i40evf_config_rss
=================

.. c:function:: int i40evf_config_rss(struct i40evf_adapter *adapter)

    Configure RSS keys and lut

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_config_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40evf_fill_rss_lut`:

i40evf_fill_rss_lut
===================

.. c:function:: void i40evf_fill_rss_lut(struct i40evf_adapter *adapter)

    Fill the lut with default values

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_init_rss`:

i40evf_init_rss
===============

.. c:function:: int i40evf_init_rss(struct i40evf_adapter *adapter)

    Prepare for RSS

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_init_rss.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`i40evf_alloc_q_vectors`:

i40evf_alloc_q_vectors
======================

.. c:function:: int i40evf_alloc_q_vectors(struct i40evf_adapter *adapter)

    Allocate memory for interrupt vectors

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`i40evf_free_q_vectors`:

i40evf_free_q_vectors
=====================

.. c:function:: void i40evf_free_q_vectors(struct i40evf_adapter *adapter)

    Free memory allocated for interrupt vectors

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`i40evf_reset_interrupt_capability`:

i40evf_reset_interrupt_capability
=================================

.. c:function:: void i40evf_reset_interrupt_capability(struct i40evf_adapter *adapter)

    Reset MSIX setup

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_init_interrupt_scheme`:

i40evf_init_interrupt_scheme
============================

.. c:function:: int i40evf_init_interrupt_scheme(struct i40evf_adapter *adapter)

    Determine if MSIX is supported and init

    :param struct i40evf_adapter \*adapter:
        board private structure to initialize

.. _`i40evf_free_rss`:

i40evf_free_rss
===============

.. c:function:: void i40evf_free_rss(struct i40evf_adapter *adapter)

    Free memory used by RSS structs

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_watchdog_timer`:

i40evf_watchdog_timer
=====================

.. c:function:: void i40evf_watchdog_timer(unsigned long data)

    Periodic call-back timer

    :param unsigned long data:
        pointer to adapter disguised as unsigned long

.. _`i40evf_watchdog_task`:

i40evf_watchdog_task
====================

.. c:function:: void i40evf_watchdog_task(struct work_struct *work)

    Periodic call-back task

    :param struct work_struct \*work:
        pointer to work_struct

.. _`i40evf_reset_task`:

i40evf_reset_task
=================

.. c:function:: void i40evf_reset_task(struct work_struct *work)

    Call-back task to handle hardware reset

    :param struct work_struct \*work:
        pointer to work_struct

.. _`i40evf_reset_task.description`:

Description
-----------

During reset we need to shut down and reinitialize the admin queue
before we can use it to communicate with the PF again. We also clear
and reinit the rings because that context is lost as well.

.. _`i40evf_adminq_task`:

i40evf_adminq_task
==================

.. c:function:: void i40evf_adminq_task(struct work_struct *work)

    worker thread to clean the admin queue

    :param struct work_struct \*work:
        pointer to work_struct containing our data

.. _`i40evf_client_task`:

i40evf_client_task
==================

.. c:function:: void i40evf_client_task(struct work_struct *work)

    worker thread to perform client work

    :param struct work_struct \*work:
        pointer to work_struct containing our data

.. _`i40evf_client_task.description`:

Description
-----------

This task handles client interactions. Because client calls can be
reentrant, we can't handle them in the watchdog.

.. _`i40evf_free_all_tx_resources`:

i40evf_free_all_tx_resources
============================

.. c:function:: void i40evf_free_all_tx_resources(struct i40evf_adapter *adapter)

    Free Tx Resources for All Queues

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`i40evf_setup_all_tx_resources`:

i40evf_setup_all_tx_resources
=============================

.. c:function:: int i40evf_setup_all_tx_resources(struct i40evf_adapter *adapter)

    allocate all queues Tx resources

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_setup_all_tx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`i40evf_setup_all_rx_resources`:

i40evf_setup_all_rx_resources
=============================

.. c:function:: int i40evf_setup_all_rx_resources(struct i40evf_adapter *adapter)

    allocate all queues Rx resources

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_setup_all_rx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`i40evf_free_all_rx_resources`:

i40evf_free_all_rx_resources
============================

.. c:function:: void i40evf_free_all_rx_resources(struct i40evf_adapter *adapter)

    Free Rx Resources for All Queues

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`i40evf_open`:

i40evf_open
===========

.. c:function:: int i40evf_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`i40evf_close`:

i40evf_close
============

.. c:function:: int i40evf_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40evf_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled. All IRQs except vector 0 (reserved for admin queue)
are freed, along with all transmit and receive resources.

.. _`i40evf_change_mtu`:

i40evf_change_mtu
=================

.. c:function:: int i40evf_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`i40evf_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40evf_set_features`:

i40evf_set_features
===================

.. c:function:: int i40evf_set_features(struct net_device *netdev, netdev_features_t features)

    set the netdev feature flags

    :param struct net_device \*netdev:
        ptr to the netdev being adjusted

    :param netdev_features_t features:
        the feature set that the stack is suggesting

.. _`i40evf_set_features.note`:

Note
----

expects to be called while under \ :c:func:`rtnl_lock`\ 

.. _`i40evf_features_check`:

i40evf_features_check
=====================

.. c:function:: netdev_features_t i40evf_features_check(struct sk_buff *skb, struct net_device *dev, netdev_features_t features)

    Validate encapsulated packet conforms to limits

    :param struct sk_buff \*skb:
        skb buff

    :param struct net_device \*dev:
        *undescribed*

    :param netdev_features_t features:
        Offload features that the stack believes apply

.. _`i40evf_fix_features`:

i40evf_fix_features
===================

.. c:function:: netdev_features_t i40evf_fix_features(struct net_device *netdev, netdev_features_t features)

    fix up the netdev feature bits

    :param struct net_device \*netdev:
        our net device

    :param netdev_features_t features:
        desired feature bits

.. _`i40evf_fix_features.description`:

Description
-----------

Returns fixed-up features bits

.. _`i40evf_check_reset_complete`:

i40evf_check_reset_complete
===========================

.. c:function:: int i40evf_check_reset_complete(struct i40e_hw *hw)

    check that VF reset is complete

    :param struct i40e_hw \*hw:
        pointer to hw struct

.. _`i40evf_check_reset_complete.description`:

Description
-----------

Returns 0 if device is ready to use, or -EBUSY if it's in reset.

.. _`i40evf_process_config`:

i40evf_process_config
=====================

.. c:function:: int i40evf_process_config(struct i40evf_adapter *adapter)

    Process the config information we got from the PF

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_process_config.description`:

Description
-----------

Verify that we have a valid config struct, and set up our netdev features
and our VSI struct.

.. _`i40evf_init_task`:

i40evf_init_task
================

.. c:function:: void i40evf_init_task(struct work_struct *work)

    worker thread to perform delayed initialization

    :param struct work_struct \*work:
        pointer to work_struct containing our data

.. _`i40evf_init_task.description`:

Description
-----------

This task completes the work that was begun in probe. Due to the nature
of VF-PF communications, we may need to wait tens of milliseconds to get
responses back from the PF. Rather than busy-wait in probe and bog down the
whole system, we'll do it in a task so we can sleep.
This task only runs during driver init. Once we've established
communications with the PF driver and set up our netdev, the watchdog
takes over.

.. _`i40evf_shutdown`:

i40evf_shutdown
===============

.. c:function:: void i40evf_shutdown(struct pci_dev *pdev)

    Shutdown the device in preparation for a reboot

    :param struct pci_dev \*pdev:
        pci device structure

.. _`i40evf_probe`:

i40evf_probe
============

.. c:function:: int i40evf_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in i40evf_pci_tbl

.. _`i40evf_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

i40evf_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`i40evf_suspend`:

i40evf_suspend
==============

.. c:function:: int i40evf_suspend(struct pci_dev *pdev, pm_message_t state)

    Power management suspend routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param pm_message_t state:
        unused

.. _`i40evf_suspend.description`:

Description
-----------

Called when the system (VM) is entering sleep/suspend.

.. _`i40evf_resume`:

i40evf_resume
=============

.. c:function:: int i40evf_resume(struct pci_dev *pdev)

    Power management resume routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40evf_resume.description`:

Description
-----------

Called when the system (VM) is resumed from sleep/suspend.

.. _`i40evf_remove`:

i40evf_remove
=============

.. c:function:: void i40evf_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40evf_remove.description`:

Description
-----------

i40evf_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`i40evf_init_module`:

i40evf_init_module
==================

.. c:function:: int i40evf_init_module( void)

    Driver Registration Routine

    :param  void:
        no arguments

.. _`i40evf_init_module.description`:

Description
-----------

i40e_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`i40evf_exit_module`:

i40evf_exit_module
==================

.. c:function:: void __exit i40evf_exit_module( void)

    Driver Exit Cleanup Routine

    :param  void:
        no arguments

.. _`i40evf_exit_module.description`:

Description
-----------

i40e_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.

