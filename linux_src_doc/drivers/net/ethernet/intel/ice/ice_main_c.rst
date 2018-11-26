.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_main.c

.. _`ice_get_tx_pending`:

ice_get_tx_pending
==================

.. c:function:: u32 ice_get_tx_pending(struct ice_ring *ring)

    returns number of Tx descriptors not processed

    :param ring:
        the ring of descriptors
    :type ring: struct ice_ring \*

.. _`ice_check_for_hang_subtask`:

ice_check_for_hang_subtask
==========================

.. c:function:: void ice_check_for_hang_subtask(struct ice_pf *pf)

    check for and recover hung queues

    :param pf:
        pointer to PF struct
    :type pf: struct ice_pf \*

.. _`ice_add_mac_to_sync_list`:

ice_add_mac_to_sync_list
========================

.. c:function:: int ice_add_mac_to_sync_list(struct net_device *netdev, const u8 *addr)

    creates list of mac addresses to be synced

    :param netdev:
        the net device on which the sync is happening
    :type netdev: struct net_device \*

    :param addr:
        mac address to sync
    :type addr: const u8 \*

.. _`ice_add_mac_to_sync_list.description`:

Description
-----------

This is a callback function which is called by the in kernel device sync
functions (like \__dev_uc_sync, \__dev_mc_sync, etc). This function only
populates the tmp_sync_list, which is later used by ice_add_mac to add the
mac filters from the hardware.

.. _`ice_add_mac_to_unsync_list`:

ice_add_mac_to_unsync_list
==========================

.. c:function:: int ice_add_mac_to_unsync_list(struct net_device *netdev, const u8 *addr)

    creates list of mac addresses to be unsynced

    :param netdev:
        the net device on which the unsync is happening
    :type netdev: struct net_device \*

    :param addr:
        mac address to unsync
    :type addr: const u8 \*

.. _`ice_add_mac_to_unsync_list.description`:

Description
-----------

This is a callback function which is called by the in kernel device unsync
functions (like \__dev_uc_unsync, \__dev_mc_unsync, etc). This function only
populates the tmp_unsync_list, which is later used by ice_remove_mac to
delete the mac filters from the hardware.

.. _`ice_vsi_fltr_changed`:

ice_vsi_fltr_changed
====================

.. c:function:: bool ice_vsi_fltr_changed(struct ice_vsi *vsi)

    check if filter state changed

    :param vsi:
        VSI to be checked
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_fltr_changed.description`:

Description
-----------

returns true if filter state has changed, false otherwise.

.. _`ice_vsi_sync_fltr`:

ice_vsi_sync_fltr
=================

.. c:function:: int ice_vsi_sync_fltr(struct ice_vsi *vsi)

    Update the VSI filter list to the HW

    :param vsi:
        ptr to the VSI
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_sync_fltr.description`:

Description
-----------

Push any outstanding VSI filter changes through the AdminQ.

.. _`ice_sync_fltr_subtask`:

ice_sync_fltr_subtask
=====================

.. c:function:: void ice_sync_fltr_subtask(struct ice_pf *pf)

    Sync the VSI filter list with HW

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_prepare_for_reset`:

ice_prepare_for_reset
=====================

.. c:function:: void ice_prepare_for_reset(struct ice_pf *pf)

    prep for the core to reset

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_prepare_for_reset.description`:

Description
-----------

Inform or close all dependent features in prep for reset.

.. _`ice_do_reset`:

ice_do_reset
============

.. c:function:: void ice_do_reset(struct ice_pf *pf, enum ice_reset_req reset_type)

    Initiate one of many types of resets

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

    :param reset_type:
        reset type requested
        before this function was called.
    :type reset_type: enum ice_reset_req

.. _`ice_reset_subtask`:

ice_reset_subtask
=================

.. c:function:: void ice_reset_subtask(struct ice_pf *pf)

    Set up for resetting the device and driver

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_print_link_msg`:

ice_print_link_msg
==================

.. c:function:: void ice_print_link_msg(struct ice_vsi *vsi, bool isup)

    print link up or down message

    :param vsi:
        the VSI whose link status is being queried
    :type vsi: struct ice_vsi \*

    :param isup:
        boolean for if the link is now up or down
    :type isup: bool

.. _`ice_vsi_link_event`:

ice_vsi_link_event
==================

.. c:function:: void ice_vsi_link_event(struct ice_vsi *vsi, bool link_up)

    update the vsi's netdev

    :param vsi:
        the vsi on which the link event occurred
    :type vsi: struct ice_vsi \*

    :param link_up:
        whether or not the vsi needs to be set up or down
    :type link_up: bool

.. _`ice_link_event`:

ice_link_event
==============

.. c:function:: int ice_link_event(struct ice_pf *pf, struct ice_port_info *pi)

    process the link event

    :param pf:
        pf that the link event is associated with
    :type pf: struct ice_pf \*

    :param pi:
        port_info for the port that the link event is associated with
    :type pi: struct ice_port_info \*

.. _`ice_link_event.description`:

Description
-----------

Returns -EIO if \ :c:func:`ice_get_link_status`\  fails
Returns 0 on success

.. _`ice_watchdog_subtask`:

ice_watchdog_subtask
====================

.. c:function:: void ice_watchdog_subtask(struct ice_pf *pf)

    periodic tasks not using event driven scheduling

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`__ice_clean_ctrlq`:

\__ice_clean_ctrlq
==================

.. c:function:: int __ice_clean_ctrlq(struct ice_pf *pf, enum ice_ctl_q q_type)

    helper function to clean controlq rings

    :param pf:
        ptr to struct ice_pf
    :type pf: struct ice_pf \*

    :param q_type:
        specific Control queue type
    :type q_type: enum ice_ctl_q

.. _`ice_ctrlq_pending`:

ice_ctrlq_pending
=================

.. c:function:: bool ice_ctrlq_pending(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    check if there is a difference between ntc and ntu

    :param hw:
        pointer to hardware info
    :type hw: struct ice_hw \*

    :param cq:
        control queue information
    :type cq: struct ice_ctl_q_info \*

.. _`ice_ctrlq_pending.description`:

Description
-----------

returns true if there are pending messages in a queue, false if there aren't

.. _`ice_clean_adminq_subtask`:

ice_clean_adminq_subtask
========================

.. c:function:: void ice_clean_adminq_subtask(struct ice_pf *pf)

    clean the AdminQ rings

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_clean_mailboxq_subtask`:

ice_clean_mailboxq_subtask
==========================

.. c:function:: void ice_clean_mailboxq_subtask(struct ice_pf *pf)

    clean the MailboxQ rings

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_service_task_schedule`:

ice_service_task_schedule
=========================

.. c:function:: void ice_service_task_schedule(struct ice_pf *pf)

    schedule the service task to wake up

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_service_task_schedule.description`:

Description
-----------

If not already scheduled, this puts the task into the work queue.

.. _`ice_service_task_complete`:

ice_service_task_complete
=========================

.. c:function:: void ice_service_task_complete(struct ice_pf *pf)

    finish up the service task

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_service_task_stop`:

ice_service_task_stop
=====================

.. c:function:: void ice_service_task_stop(struct ice_pf *pf)

    stop service task and cancel works

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_service_timer`:

ice_service_timer
=================

.. c:function:: void ice_service_timer(struct timer_list *t)

    timer callback to schedule service task

    :param t:
        pointer to timer_list
    :type t: struct timer_list \*

.. _`ice_handle_mdd_event`:

ice_handle_mdd_event
====================

.. c:function:: void ice_handle_mdd_event(struct ice_pf *pf)

    handle malicious driver detect event

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_handle_mdd_event.description`:

Description
-----------

Called from service task. OICR interrupt handler indicates MDD event

.. _`ice_service_task`:

ice_service_task
================

.. c:function:: void ice_service_task(struct work_struct *work)

    manage and run subtasks

    :param work:
        pointer to work_struct contained by the PF struct
    :type work: struct work_struct \*

.. _`ice_set_ctrlq_len`:

ice_set_ctrlq_len
=================

.. c:function:: void ice_set_ctrlq_len(struct ice_hw *hw)

    helper function to set controlq length

    :param hw:
        pointer to the hw instance
    :type hw: struct ice_hw \*

.. _`ice_irq_affinity_notify`:

ice_irq_affinity_notify
=======================

.. c:function:: void ice_irq_affinity_notify(struct irq_affinity_notify *notify, const cpumask_t *mask)

    Callback for affinity changes

    :param notify:
        context as to what irq was changed
    :type notify: struct irq_affinity_notify \*

    :param mask:
        the new affinity mask
    :type mask: const cpumask_t \*

.. _`ice_irq_affinity_notify.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
so that we may register to receive changes to the irq affinity masks.

.. _`ice_irq_affinity_release`:

ice_irq_affinity_release
========================

.. c:function:: void ice_irq_affinity_release(struct kref __always_unused *ref)

    Callback for affinity notifier release

    :param ref:
        internal core kernel usage
    :type ref: struct kref __always_unused \*

.. _`ice_irq_affinity_release.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
to inform the current notification subscriber that they will no longer
receive notifications.

.. _`ice_vsi_ena_irq`:

ice_vsi_ena_irq
===============

.. c:function:: int ice_vsi_ena_irq(struct ice_vsi *vsi)

    Enable IRQ for the given VSI

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_req_irq_msix`:

ice_vsi_req_irq_msix
====================

.. c:function:: int ice_vsi_req_irq_msix(struct ice_vsi *vsi, char *basename)

    get MSI-X vectors from the OS for the VSI

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param basename:
        name for the vector
    :type basename: char \*

.. _`ice_ena_misc_vector`:

ice_ena_misc_vector
===================

.. c:function:: void ice_ena_misc_vector(struct ice_pf *pf)

    enable the non-queue interrupts

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_misc_intr`:

ice_misc_intr
=============

.. c:function:: irqreturn_t ice_misc_intr(int __always_unused irq, void *data)

    misc interrupt handler

    :param irq:
        interrupt number
    :type irq: int __always_unused

    :param data:
        pointer to a q_vector
    :type data: void \*

.. _`ice_free_irq_msix_misc`:

ice_free_irq_msix_misc
======================

.. c:function:: void ice_free_irq_msix_misc(struct ice_pf *pf)

    Unroll misc vector setup

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_req_irq_msix_misc`:

ice_req_irq_msix_misc
=====================

.. c:function:: int ice_req_irq_msix_misc(struct ice_pf *pf)

    Setup the misc vector to handle non queue events

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_req_irq_msix_misc.description`:

Description
-----------

This sets up the handler for MSIX 0, which is used to manage the
non-queue interrupts, e.g. AdminQ and errors.  This is not used
when in MSI or Legacy interrupt mode.

.. _`ice_napi_del`:

ice_napi_del
============

.. c:function:: void ice_napi_del(struct ice_vsi *vsi)

    Remove NAPI handler for the VSI

    :param vsi:
        VSI for which NAPI handler is to be removed
    :type vsi: struct ice_vsi \*

.. _`ice_napi_add`:

ice_napi_add
============

.. c:function:: void ice_napi_add(struct ice_vsi *vsi)

    register NAPI handler for the VSI

    :param vsi:
        VSI for which NAPI handler is to be registered
    :type vsi: struct ice_vsi \*

.. _`ice_napi_add.description`:

Description
-----------

This function is only called in the driver's load path. Registering the NAPI
handler is done in \ :c:func:`ice_vsi_alloc_q_vector`\  for all other cases (i.e. resume,
reset/rebuild, etc.)

.. _`ice_cfg_netdev`:

ice_cfg_netdev
==============

.. c:function:: int ice_cfg_netdev(struct ice_vsi *vsi)

    Allocate, configure and register a netdev

    :param vsi:
        the VSI associated with the new netdev
    :type vsi: struct ice_vsi \*

.. _`ice_cfg_netdev.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`ice_fill_rss_lut`:

ice_fill_rss_lut
================

.. c:function:: void ice_fill_rss_lut(u8 *lut, u16 rss_table_size, u16 rss_size)

    Fill the RSS lookup table with default values

    :param lut:
        Lookup table
    :type lut: u8 \*

    :param rss_table_size:
        Lookup table size
    :type rss_table_size: u16

    :param rss_size:
        Range of queue number for hashing
    :type rss_size: u16

.. _`ice_pf_vsi_setup`:

ice_pf_vsi_setup
================

.. c:function:: struct ice_vsi *ice_pf_vsi_setup(struct ice_pf *pf, struct ice_port_info *pi)

    Set up a PF VSI

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

    :param pi:
        pointer to the port_info instance
    :type pi: struct ice_port_info \*

.. _`ice_pf_vsi_setup.description`:

Description
-----------

Returns pointer to the successfully allocated VSI sw struct on success,
otherwise returns NULL on failure.

.. _`ice_vlan_rx_add_vid`:

ice_vlan_rx_add_vid
===================

.. c:function:: int ice_vlan_rx_add_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Add a vlan id filter to HW offload

    :param netdev:
        network interface to be adjusted
    :type netdev: struct net_device \*

    :param proto:
        unused protocol
    :type proto: __always_unused __be16

    :param vid:
        vlan id to be added
    :type vid: u16

.. _`ice_vlan_rx_add_vid.description`:

Description
-----------

net_device_ops implementation for adding vlan ids

.. _`ice_vlan_rx_kill_vid`:

ice_vlan_rx_kill_vid
====================

.. c:function:: int ice_vlan_rx_kill_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Remove a vlan id filter from HW offload

    :param netdev:
        network interface to be adjusted
    :type netdev: struct net_device \*

    :param proto:
        unused protocol
    :type proto: __always_unused __be16

    :param vid:
        vlan id to be removed
    :type vid: u16

.. _`ice_vlan_rx_kill_vid.description`:

Description
-----------

net_device_ops implementation for removing vlan ids

.. _`ice_setup_pf_sw`:

ice_setup_pf_sw
===============

.. c:function:: int ice_setup_pf_sw(struct ice_pf *pf)

    Setup the HW switch on startup or after reset

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_setup_pf_sw.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`ice_determine_q_usage`:

ice_determine_q_usage
=====================

.. c:function:: void ice_determine_q_usage(struct ice_pf *pf)

    Calculate queue distribution

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_determine_q_usage.description`:

Description
-----------

Return -ENOMEM if we don't get enough queues for all ports

.. _`ice_deinit_pf`:

ice_deinit_pf
=============

.. c:function:: void ice_deinit_pf(struct ice_pf *pf)

    Unrolls initialziations done by ice_init_pf

    :param pf:
        board private structure to initialize
    :type pf: struct ice_pf \*

.. _`ice_init_pf`:

ice_init_pf
===========

.. c:function:: void ice_init_pf(struct ice_pf *pf)

    Initialize general software structures (struct ice_pf)

    :param pf:
        board private structure to initialize
    :type pf: struct ice_pf \*

.. _`ice_ena_msix_range`:

ice_ena_msix_range
==================

.. c:function:: int ice_ena_msix_range(struct ice_pf *pf)

    Request a range of MSIX vectors from the OS

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_ena_msix_range.description`:

Description
-----------

compute the number of MSIX vectors required (v_budget) and request from
the OS. Return the number of vectors reserved or negative on failure

.. _`ice_dis_msix`:

ice_dis_msix
============

.. c:function:: void ice_dis_msix(struct ice_pf *pf)

    Disable MSI-X interrupt setup in OS

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_clear_interrupt_scheme`:

ice_clear_interrupt_scheme
==========================

.. c:function:: void ice_clear_interrupt_scheme(struct ice_pf *pf)

    Undo things done by ice_init_interrupt_scheme

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

.. _`ice_init_interrupt_scheme`:

ice_init_interrupt_scheme
=========================

.. c:function:: int ice_init_interrupt_scheme(struct ice_pf *pf)

    Determine proper interrupt scheme

    :param pf:
        board private structure to initialize
    :type pf: struct ice_pf \*

.. _`ice_verify_cacheline_size`:

ice_verify_cacheline_size
=========================

.. c:function:: void ice_verify_cacheline_size(struct ice_pf *pf)

    verify driver's assumption of 64 Byte cache lines

    :param pf:
        pointer to the PF structure
    :type pf: struct ice_pf \*

.. _`ice_verify_cacheline_size.description`:

Description
-----------

There is no error returned here because the driver should be able to handle
128 Byte cache lines, so we only print a warning in case issues are seen,
specifically with Tx.

.. _`ice_probe`:

ice_probe
=========

.. c:function:: int ice_probe(struct pci_dev *pdev, const struct pci_device_id __always_unused *ent)

    Device initialization routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in ice_pci_tbl
    :type ent: const struct pci_device_id __always_unused \*

.. _`ice_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_remove`:

ice_remove
==========

.. c:function:: void ice_remove(struct pci_dev *pdev)

    Device removal routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`ice_module_init`:

ice_module_init
===============

.. c:function:: int ice_module_init( void)

    Driver registration routine

    :param void:
        no arguments
    :type void: 

.. _`ice_module_init.description`:

Description
-----------

ice_module_init is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`ice_module_exit`:

ice_module_exit
===============

.. c:function:: void __exit ice_module_exit( void)

    Driver exit cleanup routine

    :param void:
        no arguments
    :type void: 

.. _`ice_module_exit.description`:

Description
-----------

ice_module_exit is called just before the driver is removed
from memory.

.. _`ice_set_mac_address`:

ice_set_mac_address
===================

.. c:function:: int ice_set_mac_address(struct net_device *netdev, void *pi)

    NDO callback to set mac address

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param pi:
        pointer to an address structure
    :type pi: void \*

.. _`ice_set_mac_address.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_set_rx_mode`:

ice_set_rx_mode
===============

.. c:function:: void ice_set_rx_mode(struct net_device *netdev)

    NDO callback to set the netdev filters

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_fdb_add`:

ice_fdb_add
===========

.. c:function:: int ice_fdb_add(struct ndmsg *ndm, struct nlattr __always_unused  *tb, struct net_device *dev, const unsigned char *addr, u16 vid, u16 flags)

    add an entry to the hardware database

    :param ndm:
        the input from the stack
    :type ndm: struct ndmsg \*

    :param tb:
        pointer to array of nladdr (unused)
    :type tb: struct nlattr __always_unused  \*

    :param dev:
        the net device pointer
    :type dev: struct net_device \*

    :param addr:
        the MAC address entry being added
    :type addr: const unsigned char \*

    :param vid:
        VLAN id
    :type vid: u16

    :param flags:
        instructions from stack about fdb operation
    :type flags: u16

.. _`ice_fdb_del`:

ice_fdb_del
===========

.. c:function:: int ice_fdb_del(struct ndmsg *ndm, __always_unused struct nlattr  *tb, struct net_device *dev, const unsigned char *addr, __always_unused u16 vid)

    delete an entry from the hardware database

    :param ndm:
        the input from the stack
    :type ndm: struct ndmsg \*

    :param tb:
        pointer to array of nladdr (unused)
    :type tb: __always_unused struct nlattr  \*

    :param dev:
        the net device pointer
    :type dev: struct net_device \*

    :param addr:
        the MAC address entry being added
    :type addr: const unsigned char \*

    :param vid:
        VLAN id
    :type vid: __always_unused u16

.. _`ice_set_features`:

ice_set_features
================

.. c:function:: int ice_set_features(struct net_device *netdev, netdev_features_t features)

    set the netdev feature flags

    :param netdev:
        ptr to the netdev being adjusted
    :type netdev: struct net_device \*

    :param features:
        the feature set that the stack is suggesting
    :type features: netdev_features_t

.. _`ice_vsi_vlan_setup`:

ice_vsi_vlan_setup
==================

.. c:function:: int ice_vsi_vlan_setup(struct ice_vsi *vsi)

    Setup vlan offload properties on a VSI

    :param vsi:
        VSI to setup vlan properties for
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_cfg`:

ice_vsi_cfg
===========

.. c:function:: int ice_vsi_cfg(struct ice_vsi *vsi)

    Setup the VSI

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_cfg.description`:

Description
-----------

Return 0 on success and negative value on error

.. _`ice_napi_enable_all`:

ice_napi_enable_all
===================

.. c:function:: void ice_napi_enable_all(struct ice_vsi *vsi)

    Enable NAPI for all q_vectors in the VSI

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_up_complete`:

ice_up_complete
===============

.. c:function:: int ice_up_complete(struct ice_vsi *vsi)

    Finish the last steps of bringing up a connection

    :param vsi:
        The VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_up_complete.description`:

Description
-----------

Return 0 on success and negative value on error

.. _`ice_up`:

ice_up
======

.. c:function:: int ice_up(struct ice_vsi *vsi)

    Bring the connection back up after being down

    :param vsi:
        VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_fetch_u64_stats_per_ring`:

ice_fetch_u64_stats_per_ring
============================

.. c:function:: void ice_fetch_u64_stats_per_ring(struct ice_ring *ring, u64 *pkts, u64 *bytes)

    get packets and bytes stats per ring

    :param ring:
        Tx or Rx ring to read stats from
    :type ring: struct ice_ring \*

    :param pkts:
        packets stats counter
    :type pkts: u64 \*

    :param bytes:
        bytes stats counter
    :type bytes: u64 \*

.. _`ice_fetch_u64_stats_per_ring.description`:

Description
-----------

This function fetches stats from the ring considering the atomic operations
that needs to be performed to read u64 values in 32 bit machine.

.. _`ice_update_vsi_ring_stats`:

ice_update_vsi_ring_stats
=========================

.. c:function:: void ice_update_vsi_ring_stats(struct ice_vsi *vsi)

    Update VSI stats counters

    :param vsi:
        the VSI to be updated
    :type vsi: struct ice_vsi \*

.. _`ice_update_vsi_stats`:

ice_update_vsi_stats
====================

.. c:function:: void ice_update_vsi_stats(struct ice_vsi *vsi)

    Update VSI stats counters

    :param vsi:
        the VSI to be updated
    :type vsi: struct ice_vsi \*

.. _`ice_update_pf_stats`:

ice_update_pf_stats
===================

.. c:function:: void ice_update_pf_stats(struct ice_pf *pf)

    Update PF port stats counters

    :param pf:
        PF whose stats needs to be updated
    :type pf: struct ice_pf \*

.. _`ice_get_stats64`:

ice_get_stats64
===============

.. c:function:: void ice_get_stats64(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    get statistics for network device structure

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param stats:
        main device statistics structure
    :type stats: struct rtnl_link_stats64 \*

.. _`ice_napi_disable_all`:

ice_napi_disable_all
====================

.. c:function:: void ice_napi_disable_all(struct ice_vsi *vsi)

    Disable NAPI for all q_vectors in the VSI

    :param vsi:
        VSI having NAPI disabled
    :type vsi: struct ice_vsi \*

.. _`ice_down`:

ice_down
========

.. c:function:: int ice_down(struct ice_vsi *vsi)

    Shutdown the connection

    :param vsi:
        The VSI being stopped
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_setup_tx_rings`:

ice_vsi_setup_tx_rings
======================

.. c:function:: int ice_vsi_setup_tx_rings(struct ice_vsi *vsi)

    Allocate VSI Tx queue resources

    :param vsi:
        VSI having resources allocated
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_setup_tx_rings.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ice_vsi_setup_rx_rings`:

ice_vsi_setup_rx_rings
======================

.. c:function:: int ice_vsi_setup_rx_rings(struct ice_vsi *vsi)

    Allocate VSI Rx queue resources

    :param vsi:
        VSI having resources allocated
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_setup_rx_rings.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ice_vsi_req_irq`:

ice_vsi_req_irq
===============

.. c:function:: int ice_vsi_req_irq(struct ice_vsi *vsi, char *basename)

    Request IRQ from the OS

    :param vsi:
        The VSI IRQ is being requested for
    :type vsi: struct ice_vsi \*

    :param basename:
        name for the vector
    :type basename: char \*

.. _`ice_vsi_req_irq.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_open`:

ice_vsi_open
============

.. c:function:: int ice_vsi_open(struct ice_vsi *vsi)

    Called when a network interface is made active

    :param vsi:
        the VSI to open
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_open.description`:

Description
-----------

Initialization of the VSI

Returns 0 on success, negative value on error

.. _`ice_vsi_release_all`:

ice_vsi_release_all
===================

.. c:function:: void ice_vsi_release_all(struct ice_pf *pf)

    Delete all VSIs

    :param pf:
        PF from which all VSIs are being removed
    :type pf: struct ice_pf \*

.. _`ice_dis_vsi`:

ice_dis_vsi
===========

.. c:function:: void ice_dis_vsi(struct ice_vsi *vsi)

    pause a VSI

    :param vsi:
        the VSI being paused
    :type vsi: struct ice_vsi \*

.. _`ice_ena_vsi`:

ice_ena_vsi
===========

.. c:function:: int ice_ena_vsi(struct ice_vsi *vsi)

    resume a VSI

    :param vsi:
        the VSI being resume
    :type vsi: struct ice_vsi \*

.. _`ice_pf_dis_all_vsi`:

ice_pf_dis_all_vsi
==================

.. c:function:: void ice_pf_dis_all_vsi(struct ice_pf *pf)

    Pause all VSIs on a PF

    :param pf:
        the PF
    :type pf: struct ice_pf \*

.. _`ice_pf_ena_all_vsi`:

ice_pf_ena_all_vsi
==================

.. c:function:: int ice_pf_ena_all_vsi(struct ice_pf *pf)

    Resume all VSIs on a PF

    :param pf:
        the PF
    :type pf: struct ice_pf \*

.. _`ice_vsi_rebuild_all`:

ice_vsi_rebuild_all
===================

.. c:function:: int ice_vsi_rebuild_all(struct ice_pf *pf)

    rebuild all VSIs in pf

    :param pf:
        the PF
    :type pf: struct ice_pf \*

.. _`ice_vsi_replay_all`:

ice_vsi_replay_all
==================

.. c:function:: int ice_vsi_replay_all(struct ice_pf *pf)

    replay all VSIs configuration in the PF

    :param pf:
        the PF
    :type pf: struct ice_pf \*

.. _`ice_rebuild`:

ice_rebuild
===========

.. c:function:: void ice_rebuild(struct ice_pf *pf)

    rebuild after reset

    :param pf:
        pf to rebuild
    :type pf: struct ice_pf \*

.. _`ice_change_mtu`:

ice_change_mtu
==============

.. c:function:: int ice_change_mtu(struct net_device *netdev, int new_mtu)

    NDO callback to change the MTU

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`ice_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_set_rss`:

ice_set_rss
===========

.. c:function:: int ice_set_rss(struct ice_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Set RSS keys and lut

    :param vsi:
        Pointer to VSI structure
    :type vsi: struct ice_vsi \*

    :param seed:
        RSS hash seed
    :type seed: u8 \*

    :param lut:
        Lookup table
    :type lut: u8 \*

    :param lut_size:
        Lookup table size
    :type lut_size: u16

.. _`ice_set_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_get_rss`:

ice_get_rss
===========

.. c:function:: int ice_get_rss(struct ice_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Get RSS keys and lut

    :param vsi:
        Pointer to VSI structure
    :type vsi: struct ice_vsi \*

    :param seed:
        Buffer to store the keys
    :type seed: u8 \*

    :param lut:
        Buffer to store the lookup table entries
    :type lut: u8 \*

    :param lut_size:
        Size of buffer to store the lookup table entries
    :type lut_size: u16

.. _`ice_get_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_bridge_getlink`:

ice_bridge_getlink
==================

.. c:function:: int ice_bridge_getlink(struct sk_buff *skb, u32 pid, u32 seq, struct net_device *dev, u32 filter_mask, int nlflags)

    Get the hardware bridge mode

    :param skb:
        skb buff
    :type skb: struct sk_buff \*

    :param pid:
        process id
    :type pid: u32

    :param seq:
        RTNL message seq
    :type seq: u32

    :param dev:
        the netdev being configured
    :type dev: struct net_device \*

    :param filter_mask:
        filter mask passed in
    :type filter_mask: u32

    :param nlflags:
        netlink flags passed in
    :type nlflags: int

.. _`ice_bridge_getlink.description`:

Description
-----------

Return the bridge mode (VEB/VEPA)

.. _`ice_vsi_update_bridge_mode`:

ice_vsi_update_bridge_mode
==========================

.. c:function:: int ice_vsi_update_bridge_mode(struct ice_vsi *vsi, u16 bmode)

    Update VSI for switching bridge mode (VEB/VEPA)

    :param vsi:
        Pointer to VSI structure
    :type vsi: struct ice_vsi \*

    :param bmode:
        Hardware bridge mode (VEB/VEPA)
    :type bmode: u16

.. _`ice_vsi_update_bridge_mode.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_bridge_setlink`:

ice_bridge_setlink
==================

.. c:function:: int ice_bridge_setlink(struct net_device *dev, struct nlmsghdr *nlh, u16 __always_unused flags)

    Set the hardware bridge mode

    :param dev:
        the netdev being configured
    :type dev: struct net_device \*

    :param nlh:
        RTNL message
    :type nlh: struct nlmsghdr \*

    :param flags:
        bridge setlink flags
    :type flags: u16 __always_unused

.. _`ice_bridge_setlink.description`:

Description
-----------

Sets the bridge mode (VEB/VEPA) of the switch to which the netdev (VSI) is
hooked up to. Iterates through the PF VSI list and sets the loopback mode (if
not already set for all VSIs connected to this switch. And also update the
unicast switch filter rules for the corresponding switch of the netdev.

.. _`ice_tx_timeout`:

ice_tx_timeout
==============

.. c:function:: void ice_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_open`:

ice_open
========

.. c:function:: int ice_open(struct net_device *netdev)

    Called when a network interface becomes active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_open.description`:

Description
-----------

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the netdev watchdog is enabled,
and the stack is notified that the interface is ready.

Returns 0 on success, negative value on failure

.. _`ice_stop`:

ice_stop
========

.. c:function:: int ice_stop(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ice_stop.description`:

Description
-----------

The stop entry point is called when an interface is de-activated by the OS,
and the netdevice enters the DOWN state.  The hardware is still under the
driver's control, but the netdev interface is disabled.

Returns success only - not allowed to fail

.. _`ice_features_check`:

ice_features_check
==================

.. c:function:: netdev_features_t ice_features_check(struct sk_buff *skb, struct net_device __always_unused *netdev, netdev_features_t features)

    Validate encapsulated packet conforms to limits

    :param skb:
        skb buffer
    :type skb: struct sk_buff \*

    :param netdev:
        This port's netdev
    :type netdev: struct net_device __always_unused \*

    :param features:
        Offload features that the stack believes apply
    :type features: netdev_features_t

.. This file was automatic generated / don't edit.

