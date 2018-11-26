.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_main.c

.. _`iavf_allocate_dma_mem_d`:

iavf_allocate_dma_mem_d
=======================

.. c:function:: iavf_status iavf_allocate_dma_mem_d(struct iavf_hw *hw, struct iavf_dma_mem *mem, u64 size, u32 alignment)

    OS specific memory alloc for shared code

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

    :param mem:
        ptr to mem struct to fill out
    :type mem: struct iavf_dma_mem \*

    :param size:
        size of memory requested
    :type size: u64

    :param alignment:
        what to align the allocation to
    :type alignment: u32

.. _`iavf_free_dma_mem_d`:

iavf_free_dma_mem_d
===================

.. c:function:: iavf_status iavf_free_dma_mem_d(struct iavf_hw *hw, struct iavf_dma_mem *mem)

    OS specific memory free for shared code

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

    :param mem:
        ptr to mem struct to free
    :type mem: struct iavf_dma_mem \*

.. _`iavf_allocate_virt_mem_d`:

iavf_allocate_virt_mem_d
========================

.. c:function:: iavf_status iavf_allocate_virt_mem_d(struct iavf_hw *hw, struct iavf_virt_mem *mem, u32 size)

    OS specific memory alloc for shared code

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

    :param mem:
        ptr to mem struct to fill out
    :type mem: struct iavf_virt_mem \*

    :param size:
        size of memory requested
    :type size: u32

.. _`iavf_free_virt_mem_d`:

iavf_free_virt_mem_d
====================

.. c:function:: iavf_status iavf_free_virt_mem_d(struct iavf_hw *hw, struct iavf_virt_mem *mem)

    OS specific memory free for shared code

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

    :param mem:
        ptr to mem struct to free
    :type mem: struct iavf_virt_mem \*

.. _`iavf_debug_d`:

iavf_debug_d
============

.. c:function:: void iavf_debug_d(void *hw, u32 mask, char *fmt_str,  ...)

    OS dependent version of debug printing

    :param hw:
        pointer to the HW structure
    :type hw: void \*

    :param mask:
        debug level mask
    :type mask: u32

    :param fmt_str:
        printf-type format description
    :type fmt_str: char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`iavf_schedule_reset`:

iavf_schedule_reset
===================

.. c:function:: void iavf_schedule_reset(struct iavf_adapter *adapter)

    Set the flags and schedule a reset event

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_tx_timeout`:

iavf_tx_timeout
===============

.. c:function:: void iavf_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_misc_irq_disable`:

iavf_misc_irq_disable
=====================

.. c:function:: void iavf_misc_irq_disable(struct iavf_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_misc_irq_enable`:

iavf_misc_irq_enable
====================

.. c:function:: void iavf_misc_irq_enable(struct iavf_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_irq_disable`:

iavf_irq_disable
================

.. c:function:: void iavf_irq_disable(struct iavf_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_irq_enable_queues`:

iavf_irq_enable_queues
======================

.. c:function:: void iavf_irq_enable_queues(struct iavf_adapter *adapter, u32 mask)

    Enable interrupt for specified queues

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param mask:
        bitmap of queues to enable
    :type mask: u32

.. _`iavf_irq_enable`:

iavf_irq_enable
===============

.. c:function:: void iavf_irq_enable(struct iavf_adapter *adapter, bool flush)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param flush:
        boolean value whether to run \ :c:func:`rd32`\ 
    :type flush: bool

.. _`iavf_msix_aq`:

iavf_msix_aq
============

.. c:function:: irqreturn_t iavf_msix_aq(int irq, void *data)

    Interrupt handler for vector 0

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to netdev
    :type data: void \*

.. _`iavf_msix_clean_rings`:

iavf_msix_clean_rings
=====================

.. c:function:: irqreturn_t iavf_msix_clean_rings(int irq, void *data)

    MSIX mode Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a q_vector
    :type data: void \*

.. _`iavf_map_vector_to_rxq`:

iavf_map_vector_to_rxq
======================

.. c:function:: void iavf_map_vector_to_rxq(struct iavf_adapter *adapter, int v_idx, int r_idx)

    associate irqs with rx queues

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param v_idx:
        interrupt number
    :type v_idx: int

    :param r_idx:
        queue number
    :type r_idx: int

.. _`iavf_map_vector_to_txq`:

iavf_map_vector_to_txq
======================

.. c:function:: void iavf_map_vector_to_txq(struct iavf_adapter *adapter, int v_idx, int t_idx)

    associate irqs with tx queues

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param v_idx:
        interrupt number
    :type v_idx: int

    :param t_idx:
        queue number
    :type t_idx: int

.. _`iavf_map_rings_to_vectors`:

iavf_map_rings_to_vectors
=========================

.. c:function:: void iavf_map_rings_to_vectors(struct iavf_adapter *adapter)

    Maps descriptor rings to vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_map_rings_to_vectors.description`:

Description
-----------

This function maps descriptor rings to the queue-specific vectors
we were allotted through the MSI-X enabling code.  Ideally, we'd have
one vector per ring/queue, but on a constrained vector budget, we
group the rings as "efficiently" as possible.  You would add new
mapping configurations in here.

.. _`iavf_irq_affinity_notify`:

iavf_irq_affinity_notify
========================

.. c:function:: void iavf_irq_affinity_notify(struct irq_affinity_notify *notify, const cpumask_t *mask)

    Callback for affinity changes

    :param notify:
        context as to what irq was changed
    :type notify: struct irq_affinity_notify \*

    :param mask:
        the new affinity mask
    :type mask: const cpumask_t \*

.. _`iavf_irq_affinity_notify.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
so that we may register to receive changes to the irq affinity masks.

.. _`iavf_irq_affinity_release`:

iavf_irq_affinity_release
=========================

.. c:function:: void iavf_irq_affinity_release(struct kref *ref)

    Callback for affinity notifier release

    :param ref:
        internal core kernel usage
    :type ref: struct kref \*

.. _`iavf_irq_affinity_release.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
to inform the current notification subscriber that they will no longer
receive notifications.

.. _`iavf_request_traffic_irqs`:

iavf_request_traffic_irqs
=========================

.. c:function:: int iavf_request_traffic_irqs(struct iavf_adapter *adapter, char *basename)

    Initialize MSI-X interrupts

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param basename:
        device basename
    :type basename: char \*

.. _`iavf_request_traffic_irqs.description`:

Description
-----------

Allocates MSI-X vectors for tx and rx handling, and requests
interrupts from the kernel.

.. _`iavf_request_misc_irq`:

iavf_request_misc_irq
=====================

.. c:function:: int iavf_request_misc_irq(struct iavf_adapter *adapter)

    Initialize MSI-X interrupts

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_request_misc_irq.description`:

Description
-----------

Allocates MSI-X vector 0 and requests interrupts from the kernel. This
vector is only for the admin queue, and stays active even when the netdev
is closed.

.. _`iavf_free_traffic_irqs`:

iavf_free_traffic_irqs
======================

.. c:function:: void iavf_free_traffic_irqs(struct iavf_adapter *adapter)

    Free MSI-X interrupts

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_traffic_irqs.description`:

Description
-----------

Frees all MSI-X vectors other than 0.

.. _`iavf_free_misc_irq`:

iavf_free_misc_irq
==================

.. c:function:: void iavf_free_misc_irq(struct iavf_adapter *adapter)

    Free MSI-X miscellaneous vector

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_misc_irq.description`:

Description
-----------

Frees MSI-X vector 0.

.. _`iavf_configure_tx`:

iavf_configure_tx
=================

.. c:function:: void iavf_configure_tx(struct iavf_adapter *adapter)

    Configure Transmit Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`iavf_configure_rx`:

iavf_configure_rx
=================

.. c:function:: void iavf_configure_rx(struct iavf_adapter *adapter)

    Configure Receive Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`iavf_find_vlan`:

iavf_find_vlan
==============

.. c:function:: struct iavf_vlan_filter *iavf_find_vlan(struct iavf_adapter *adapter, u16 vlan)

    Search filter list for specific vlan filter

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param vlan:
        vlan tag
    :type vlan: u16

.. _`iavf_find_vlan.description`:

Description
-----------

Returns ptr to the filter object or NULL. Must be called while holding the
mac_vlan_list_lock.

.. _`iavf_add_vlan`:

iavf_add_vlan
=============

.. c:function:: struct iavf_vlan_filter *iavf_add_vlan(struct iavf_adapter *adapter, u16 vlan)

    Add a vlan filter to the list

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param vlan:
        VLAN tag
    :type vlan: u16

.. _`iavf_add_vlan.description`:

Description
-----------

Returns ptr to the filter object or NULL when no memory available.

.. _`iavf_del_vlan`:

iavf_del_vlan
=============

.. c:function:: void iavf_del_vlan(struct iavf_adapter *adapter, u16 vlan)

    Remove a vlan filter from the list

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param vlan:
        VLAN tag
    :type vlan: u16

.. _`iavf_vlan_rx_add_vid`:

iavf_vlan_rx_add_vid
====================

.. c:function:: int iavf_vlan_rx_add_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Add a VLAN filter to a device

    :param netdev:
        network device struct
    :type netdev: struct net_device \*

    :param proto:
        unused protocol data
    :type proto: __always_unused __be16

    :param vid:
        VLAN tag
    :type vid: u16

.. _`iavf_vlan_rx_kill_vid`:

iavf_vlan_rx_kill_vid
=====================

.. c:function:: int iavf_vlan_rx_kill_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Remove a VLAN filter from a device

    :param netdev:
        network device struct
    :type netdev: struct net_device \*

    :param proto:
        unused protocol data
    :type proto: __always_unused __be16

    :param vid:
        VLAN tag
    :type vid: u16

.. _`iavf_find_filter`:

iavf_find_filter
================

.. c:function:: struct iavf_mac_filter *iavf_find_filter(struct iavf_adapter *adapter, const u8 *macaddr)

    Search filter list for specific mac filter

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param macaddr:
        the MAC address
    :type macaddr: const u8 \*

.. _`iavf_find_filter.description`:

Description
-----------

Returns ptr to the filter object or NULL. Must be called while holding the
mac_vlan_list_lock.

.. _`iavf_add_filter`:

iavf_add_filter
===============

.. c:function:: struct iavf_mac_filter *iavf_add_filter(struct iavf_adapter *adapter, const u8 *macaddr)

    Add a mac filter to the filter list

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param macaddr:
        the MAC address
    :type macaddr: const u8 \*

.. _`iavf_add_filter.description`:

Description
-----------

Returns ptr to the filter object or NULL when no memory available.

.. _`iavf_set_mac`:

iavf_set_mac
============

.. c:function:: int iavf_set_mac(struct net_device *netdev, void *p)

    NDO callback to set port mac address

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`iavf_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`iavf_addr_sync`:

iavf_addr_sync
==============

.. c:function:: int iavf_addr_sync(struct net_device *netdev, const u8 *addr)

    Callback for dev_(mc\|uc)_sync to add address

    :param netdev:
        the netdevice
    :type netdev: struct net_device \*

    :param addr:
        address to add
    :type addr: const u8 \*

.. _`iavf_addr_sync.description`:

Description
-----------

Called by \__dev_(mc\|uc)_sync when an address needs to be added. We call
\__dev_(uc\|mc)_sync from .set_rx_mode and guarantee to hold the hash lock.

.. _`iavf_addr_unsync`:

iavf_addr_unsync
================

.. c:function:: int iavf_addr_unsync(struct net_device *netdev, const u8 *addr)

    Callback for dev_(mc\|uc)_sync to remove address

    :param netdev:
        the netdevice
    :type netdev: struct net_device \*

    :param addr:
        address to add
    :type addr: const u8 \*

.. _`iavf_addr_unsync.description`:

Description
-----------

Called by \__dev_(mc\|uc)_sync when an address needs to be removed. We call
\__dev_(uc\|mc)_sync from .set_rx_mode and guarantee to hold the hash lock.

.. _`iavf_set_rx_mode`:

iavf_set_rx_mode
================

.. c:function:: void iavf_set_rx_mode(struct net_device *netdev)

    NDO callback to set the netdev filters

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_napi_enable_all`:

iavf_napi_enable_all
====================

.. c:function:: void iavf_napi_enable_all(struct iavf_adapter *adapter)

    enable NAPI on all queue vectors

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_napi_disable_all`:

iavf_napi_disable_all
=====================

.. c:function:: void iavf_napi_disable_all(struct iavf_adapter *adapter)

    disable NAPI on all queue vectors

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_configure`:

iavf_configure
==============

.. c:function:: void iavf_configure(struct iavf_adapter *adapter)

    set up transmit and receive data structures

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_up_complete`:

iavf_up_complete
================

.. c:function:: void iavf_up_complete(struct iavf_adapter *adapter)

    Finish the last steps of bringing up a connection

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_up_complete.description`:

Description
-----------

Expects to be called while holding the \__IAVF_IN_CRITICAL_TASK bit lock.

.. _`iavf_down`:

iavf_down
=========

.. c:function:: void iavf_down(struct iavf_adapter *adapter)

    Shutdown the connection processing

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_down.description`:

Description
-----------

Expects to be called while holding the \__IAVF_IN_CRITICAL_TASK bit lock.

.. _`iavf_acquire_msix_vectors`:

iavf_acquire_msix_vectors
=========================

.. c:function:: int iavf_acquire_msix_vectors(struct iavf_adapter *adapter, int vectors)

    Setup the MSIX capability

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param vectors:
        number of vectors to request
    :type vectors: int

.. _`iavf_acquire_msix_vectors.description`:

Description
-----------

Work with the OS to set up the MSIX vectors needed.

Returns 0 on success, negative on failure

.. _`iavf_free_queues`:

iavf_free_queues
================

.. c:function:: void iavf_free_queues(struct iavf_adapter *adapter)

    Free memory for all rings

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_queues.description`:

Description
-----------

Free all of the memory associated with queue pairs.

.. _`iavf_alloc_queues`:

iavf_alloc_queues
=================

.. c:function:: int iavf_alloc_queues(struct iavf_adapter *adapter)

    Allocate memory for all rings

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_alloc_queues.description`:

Description
-----------

We allocate one ring per queue at run-time since we don't know the
number of queues at compile-time.  The polling_netdev array is
intended for Multiqueue, but should work fine with a single queue.

.. _`iavf_set_interrupt_capability`:

iavf_set_interrupt_capability
=============================

.. c:function:: int iavf_set_interrupt_capability(struct iavf_adapter *adapter)

    set MSI-X or FAIL if not supported

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_set_interrupt_capability.description`:

Description
-----------

Attempt to configure the interrupts using the best available
capabilities of the hardware and the kernel.

.. _`iavf_config_rss_aq`:

iavf_config_rss_aq
==================

.. c:function:: int iavf_config_rss_aq(struct iavf_adapter *adapter)

    Configure RSS keys and lut by using AQ commands

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_config_rss_aq.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`iavf_config_rss_reg`:

iavf_config_rss_reg
===================

.. c:function:: int iavf_config_rss_reg(struct iavf_adapter *adapter)

    Configure RSS keys and lut by writing registers

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_config_rss_reg.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`iavf_config_rss`:

iavf_config_rss
===============

.. c:function:: int iavf_config_rss(struct iavf_adapter *adapter)

    Configure RSS keys and lut

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_config_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`iavf_fill_rss_lut`:

iavf_fill_rss_lut
=================

.. c:function:: void iavf_fill_rss_lut(struct iavf_adapter *adapter)

    Fill the lut with default values

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_init_rss`:

iavf_init_rss
=============

.. c:function:: int iavf_init_rss(struct iavf_adapter *adapter)

    Prepare for RSS

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_init_rss.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`iavf_alloc_q_vectors`:

iavf_alloc_q_vectors
====================

.. c:function:: int iavf_alloc_q_vectors(struct iavf_adapter *adapter)

    Allocate memory for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`iavf_free_q_vectors`:

iavf_free_q_vectors
===================

.. c:function:: void iavf_free_q_vectors(struct iavf_adapter *adapter)

    Free memory allocated for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`iavf_reset_interrupt_capability`:

iavf_reset_interrupt_capability
===============================

.. c:function:: void iavf_reset_interrupt_capability(struct iavf_adapter *adapter)

    Reset MSIX setup

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_init_interrupt_scheme`:

iavf_init_interrupt_scheme
==========================

.. c:function:: int iavf_init_interrupt_scheme(struct iavf_adapter *adapter)

    Determine if MSIX is supported and init

    :param adapter:
        board private structure to initialize
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_rss`:

iavf_free_rss
=============

.. c:function:: void iavf_free_rss(struct iavf_adapter *adapter)

    Free memory used by RSS structs

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_reinit_interrupt_scheme`:

iavf_reinit_interrupt_scheme
============================

.. c:function:: int iavf_reinit_interrupt_scheme(struct iavf_adapter *adapter)

    Reallocate queues and vectors

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_reinit_interrupt_scheme.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`iavf_watchdog_timer`:

iavf_watchdog_timer
===================

.. c:function:: void iavf_watchdog_timer(struct timer_list *t)

    Periodic call-back timer

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`iavf_watchdog_task`:

iavf_watchdog_task
==================

.. c:function:: void iavf_watchdog_task(struct work_struct *work)

    Periodic call-back task

    :param work:
        pointer to work_struct
    :type work: struct work_struct \*

.. _`iavf_reset_task`:

iavf_reset_task
===============

.. c:function:: void iavf_reset_task(struct work_struct *work)

    Call-back task to handle hardware reset

    :param work:
        pointer to work_struct
    :type work: struct work_struct \*

.. _`iavf_reset_task.description`:

Description
-----------

During reset we need to shut down and reinitialize the admin queue
before we can use it to communicate with the PF again. We also clear
and reinit the rings because that context is lost as well.

.. _`iavf_adminq_task`:

iavf_adminq_task
================

.. c:function:: void iavf_adminq_task(struct work_struct *work)

    worker thread to clean the admin queue

    :param work:
        pointer to work_struct containing our data
    :type work: struct work_struct \*

.. _`iavf_client_task`:

iavf_client_task
================

.. c:function:: void iavf_client_task(struct work_struct *work)

    worker thread to perform client work

    :param work:
        pointer to work_struct containing our data
    :type work: struct work_struct \*

.. _`iavf_client_task.description`:

Description
-----------

This task handles client interactions. Because client calls can be
reentrant, we can't handle them in the watchdog.

.. _`iavf_free_all_tx_resources`:

iavf_free_all_tx_resources
==========================

.. c:function:: void iavf_free_all_tx_resources(struct iavf_adapter *adapter)

    Free Tx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`iavf_setup_all_tx_resources`:

iavf_setup_all_tx_resources
===========================

.. c:function:: int iavf_setup_all_tx_resources(struct iavf_adapter *adapter)

    allocate all queues Tx resources

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_setup_all_tx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`iavf_setup_all_rx_resources`:

iavf_setup_all_rx_resources
===========================

.. c:function:: int iavf_setup_all_rx_resources(struct iavf_adapter *adapter)

    allocate all queues Rx resources

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_setup_all_rx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`iavf_free_all_rx_resources`:

iavf_free_all_rx_resources
==========================

.. c:function:: void iavf_free_all_rx_resources(struct iavf_adapter *adapter)

    Free Rx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`iavf_validate_tx_bandwidth`:

iavf_validate_tx_bandwidth
==========================

.. c:function:: int iavf_validate_tx_bandwidth(struct iavf_adapter *adapter, u64 max_tx_rate)

    validate the max Tx bandwidth

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param max_tx_rate:
        max Tx bw for a tc
    :type max_tx_rate: u64

.. _`iavf_validate_ch_config`:

iavf_validate_ch_config
=======================

.. c:function:: int iavf_validate_ch_config(struct iavf_adapter *adapter, struct tc_mqprio_qopt_offload *mqprio_qopt)

    validate queue mapping info

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param mqprio_qopt:
        queue parameters
    :type mqprio_qopt: struct tc_mqprio_qopt_offload \*

.. _`iavf_validate_ch_config.description`:

Description
-----------

This function validates if the config provided by the user to
configure queue channels is valid or not. Returns 0 on a valid
config.

.. _`iavf_del_all_cloud_filters`:

iavf_del_all_cloud_filters
==========================

.. c:function:: void iavf_del_all_cloud_filters(struct iavf_adapter *adapter)

    delete all cloud filters on the traffic classes

    :param adapter:
        *undescribed*
    :type adapter: struct iavf_adapter \*

.. _`__iavf_setup_tc`:

\__iavf_setup_tc
================

.. c:function:: int __iavf_setup_tc(struct net_device *netdev, void *type_data)

    configure multiple traffic classes

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param type_data:
        *undescribed*
    :type type_data: void \*

.. _`__iavf_setup_tc.description`:

Description
-----------

This function processes the config information provided by the
user to configure traffic classes/queue channels and packages the
information to request the PF to setup traffic classes.

Returns 0 on success.

.. _`iavf_parse_cls_flower`:

iavf_parse_cls_flower
=====================

.. c:function:: int iavf_parse_cls_flower(struct iavf_adapter *adapter, struct tc_cls_flower_offload *f, struct iavf_cloud_filter *filter)

    Parse tc flower filters provided by kernel

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param f:
        *undescribed*
    :type f: struct tc_cls_flower_offload \*

    :param filter:
        pointer to cloud filter structure
    :type filter: struct iavf_cloud_filter \*

.. _`iavf_handle_tclass`:

iavf_handle_tclass
==================

.. c:function:: int iavf_handle_tclass(struct iavf_adapter *adapter, u32 tc, struct iavf_cloud_filter *filter)

    Forward to a traffic class on the device

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param tc:
        traffic class index on the device
    :type tc: u32

    :param filter:
        pointer to cloud filter structure
    :type filter: struct iavf_cloud_filter \*

.. _`iavf_configure_clsflower`:

iavf_configure_clsflower
========================

.. c:function:: int iavf_configure_clsflower(struct iavf_adapter *adapter, struct tc_cls_flower_offload *cls_flower)

    Add tc flower filters

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param cls_flower:
        Pointer to struct tc_cls_flower_offload
    :type cls_flower: struct tc_cls_flower_offload \*

.. _`iavf_delete_clsflower`:

iavf_delete_clsflower
=====================

.. c:function:: int iavf_delete_clsflower(struct iavf_adapter *adapter, struct tc_cls_flower_offload *cls_flower)

    Remove tc flower filters

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

    :param cls_flower:
        Pointer to struct tc_cls_flower_offload
    :type cls_flower: struct tc_cls_flower_offload \*

.. _`iavf_setup_tc_cls_flower`:

iavf_setup_tc_cls_flower
========================

.. c:function:: int iavf_setup_tc_cls_flower(struct iavf_adapter *adapter, struct tc_cls_flower_offload *cls_flower)

    flower classifier offloads

    :param adapter:
        *undescribed*
    :type adapter: struct iavf_adapter \*

    :param cls_flower:
        *undescribed*
    :type cls_flower: struct tc_cls_flower_offload \*

.. _`iavf_setup_tc_block_cb`:

iavf_setup_tc_block_cb
======================

.. c:function:: int iavf_setup_tc_block_cb(enum tc_setup_type type, void *type_data, void *cb_priv)

    block callback for tc

    :param type:
        type of offload
    :type type: enum tc_setup_type

    :param type_data:
        offload data
    :type type_data: void \*

    :param cb_priv:
        *undescribed*
    :type cb_priv: void \*

.. _`iavf_setup_tc_block_cb.description`:

Description
-----------

This function is the block callback for traffic classes

.. _`iavf_setup_tc_block`:

iavf_setup_tc_block
===================

.. c:function:: int iavf_setup_tc_block(struct net_device *dev, struct tc_block_offload *f)

    register callbacks for tc

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param f:
        tc offload data
    :type f: struct tc_block_offload \*

.. _`iavf_setup_tc_block.description`:

Description
-----------

This function registers block callbacks for tc
offloads

.. _`iavf_setup_tc`:

iavf_setup_tc
=============

.. c:function:: int iavf_setup_tc(struct net_device *netdev, enum tc_setup_type type, void *type_data)

    configure multiple traffic classes

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param type:
        type of offload
    :type type: enum tc_setup_type

    :param type_data:
        *undescribed*
    :type type_data: void \*

.. _`iavf_setup_tc.description`:

Description
-----------

This function is the callback to ndo_setup_tc in the
netdev_ops.

Returns 0 on success

.. _`iavf_open`:

iavf_open
=========

.. c:function:: int iavf_open(struct net_device *netdev)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`iavf_close`:

iavf_close
==========

.. c:function:: int iavf_close(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`iavf_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled. All IRQs except vector 0 (reserved for admin queue)
are freed, along with all transmit and receive resources.

.. _`iavf_change_mtu`:

iavf_change_mtu
===============

.. c:function:: int iavf_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`iavf_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`iavf_set_features`:

iavf_set_features
=================

.. c:function:: int iavf_set_features(struct net_device *netdev, netdev_features_t features)

    set the netdev feature flags

    :param netdev:
        ptr to the netdev being adjusted
    :type netdev: struct net_device \*

    :param features:
        the feature set that the stack is suggesting
    :type features: netdev_features_t

.. _`iavf_set_features.note`:

Note
----

expects to be called while under \ :c:func:`rtnl_lock`\ 

.. _`iavf_features_check`:

iavf_features_check
===================

.. c:function:: netdev_features_t iavf_features_check(struct sk_buff *skb, struct net_device *dev, netdev_features_t features)

    Validate encapsulated packet conforms to limits

    :param skb:
        skb buff
    :type skb: struct sk_buff \*

    :param dev:
        This physical port's netdev
    :type dev: struct net_device \*

    :param features:
        Offload features that the stack believes apply
    :type features: netdev_features_t

.. _`iavf_fix_features`:

iavf_fix_features
=================

.. c:function:: netdev_features_t iavf_fix_features(struct net_device *netdev, netdev_features_t features)

    fix up the netdev feature bits

    :param netdev:
        our net device
    :type netdev: struct net_device \*

    :param features:
        desired feature bits
    :type features: netdev_features_t

.. _`iavf_fix_features.description`:

Description
-----------

Returns fixed-up features bits

.. _`iavf_check_reset_complete`:

iavf_check_reset_complete
=========================

.. c:function:: int iavf_check_reset_complete(struct iavf_hw *hw)

    check that VF reset is complete

    :param hw:
        pointer to hw struct
    :type hw: struct iavf_hw \*

.. _`iavf_check_reset_complete.description`:

Description
-----------

Returns 0 if device is ready to use, or -EBUSY if it's in reset.

.. _`iavf_process_config`:

iavf_process_config
===================

.. c:function:: int iavf_process_config(struct iavf_adapter *adapter)

    Process the config information we got from the PF

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_process_config.description`:

Description
-----------

Verify that we have a valid config struct, and set up our netdev features
and our VSI struct.

.. _`iavf_init_task`:

iavf_init_task
==============

.. c:function:: void iavf_init_task(struct work_struct *work)

    worker thread to perform delayed initialization

    :param work:
        pointer to work_struct containing our data
    :type work: struct work_struct \*

.. _`iavf_init_task.description`:

Description
-----------

This task completes the work that was begun in probe. Due to the nature
of VF-PF communications, we may need to wait tens of milliseconds to get
responses back from the PF. Rather than busy-wait in probe and bog down the
whole system, we'll do it in a task so we can sleep.
This task only runs during driver init. Once we've established
communications with the PF driver and set up our netdev, the watchdog
takes over.

.. _`iavf_shutdown`:

iavf_shutdown
=============

.. c:function:: void iavf_shutdown(struct pci_dev *pdev)

    Shutdown the device in preparation for a reboot

    :param pdev:
        pci device structure
    :type pdev: struct pci_dev \*

.. _`iavf_probe`:

iavf_probe
==========

.. c:function:: int iavf_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in iavf_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`iavf_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

iavf_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`iavf_suspend`:

iavf_suspend
============

.. c:function:: int iavf_suspend(struct pci_dev *pdev, pm_message_t state)

    Power management suspend routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param state:
        unused
    :type state: pm_message_t

.. _`iavf_suspend.description`:

Description
-----------

Called when the system (VM) is entering sleep/suspend.

.. _`iavf_resume`:

iavf_resume
===========

.. c:function:: int iavf_resume(struct pci_dev *pdev)

    Power management resume routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`iavf_resume.description`:

Description
-----------

Called when the system (VM) is resumed from sleep/suspend.

.. _`iavf_remove`:

iavf_remove
===========

.. c:function:: void iavf_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`iavf_remove.description`:

Description
-----------

iavf_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`iavf_init_module`:

iavf_init_module
================

.. c:function:: int iavf_init_module( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`iavf_init_module.description`:

Description
-----------

iavf_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`iavf_exit_module`:

iavf_exit_module
================

.. c:function:: void __exit iavf_exit_module( void)

    Driver Exit Cleanup Routine

    :param void:
        no arguments
    :type void: 

.. _`iavf_exit_module.description`:

Description
-----------

iavf_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.

