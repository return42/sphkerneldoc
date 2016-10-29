.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_main.c

.. _`i40e_allocate_dma_mem_d`:

i40e_allocate_dma_mem_d
=======================

.. c:function:: int i40e_allocate_dma_mem_d(struct i40e_hw *hw, struct i40e_dma_mem *mem, u64 size, u32 alignment)

    OS specific memory alloc for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_dma_mem \*mem:
        ptr to mem struct to fill out

    :param u64 size:
        size of memory requested

    :param u32 alignment:
        what to align the allocation to

.. _`i40e_free_dma_mem_d`:

i40e_free_dma_mem_d
===================

.. c:function:: int i40e_free_dma_mem_d(struct i40e_hw *hw, struct i40e_dma_mem *mem)

    OS specific memory free for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_dma_mem \*mem:
        ptr to mem struct to free

.. _`i40e_allocate_virt_mem_d`:

i40e_allocate_virt_mem_d
========================

.. c:function:: int i40e_allocate_virt_mem_d(struct i40e_hw *hw, struct i40e_virt_mem *mem, u32 size)

    OS specific memory alloc for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_virt_mem \*mem:
        ptr to mem struct to fill out

    :param u32 size:
        size of memory requested

.. _`i40e_free_virt_mem_d`:

i40e_free_virt_mem_d
====================

.. c:function:: int i40e_free_virt_mem_d(struct i40e_hw *hw, struct i40e_virt_mem *mem)

    OS specific memory free for shared code

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param struct i40e_virt_mem \*mem:
        ptr to mem struct to free

.. _`i40e_get_lump`:

i40e_get_lump
=============

.. c:function:: int i40e_get_lump(struct i40e_pf *pf, struct i40e_lump_tracking *pile, u16 needed, u16 id)

    find a lump of free generic resource

    :param struct i40e_pf \*pf:
        board private structure

    :param struct i40e_lump_tracking \*pile:
        the pile of resource to search

    :param u16 needed:
        the number of items needed

    :param u16 id:
        an owner id to stick on the items assigned

.. _`i40e_get_lump.description`:

Description
-----------

Returns the base item index of the lump, or negative for error

The search_hint trick and lack of advanced fit-finding only work
because we're highly likely to have all the same size lump requests.
Linear search time and any fragmentation should be minimal.

.. _`i40e_put_lump`:

i40e_put_lump
=============

.. c:function:: int i40e_put_lump(struct i40e_lump_tracking *pile, u16 index, u16 id)

    return a lump of generic resource

    :param struct i40e_lump_tracking \*pile:
        the pile of resource to search

    :param u16 index:
        the base item index

    :param u16 id:
        the owner id of the items assigned

.. _`i40e_put_lump.description`:

Description
-----------

Returns the count of items in the lump

.. _`i40e_find_vsi_from_id`:

i40e_find_vsi_from_id
=====================

.. c:function:: struct i40e_vsi *i40e_find_vsi_from_id(struct i40e_pf *pf, u16 id)

    searches for the vsi with the given id \ ``pf``\  - the pf structure to search for the vsi \ ``id``\  - id of the vsi it is searching for

    :param struct i40e_pf \*pf:
        *undescribed*

    :param u16 id:
        *undescribed*

.. _`i40e_service_event_schedule`:

i40e_service_event_schedule
===========================

.. c:function:: void i40e_service_event_schedule(struct i40e_pf *pf)

    Schedule the service task to wake up

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_service_event_schedule.description`:

Description
-----------

If not already scheduled, this puts the task into the work queue

.. _`i40e_tx_timeout`:

i40e_tx_timeout
===============

.. c:function:: void i40e_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_tx_timeout.description`:

Description
-----------

If any port has noticed a Tx timeout, it is likely that the whole
device is munged, not just the one netdev port, so go for the full
reset.

.. _`i40e_get_vsi_stats_struct`:

i40e_get_vsi_stats_struct
=========================

.. c:function:: struct rtnl_link_stats64 *i40e_get_vsi_stats_struct(struct i40e_vsi *vsi)

    Get System Network Statistics

    :param struct i40e_vsi \*vsi:
        the VSI we care about

.. _`i40e_get_vsi_stats_struct.description`:

Description
-----------

Returns the address of the device statistics structure.
The statistics are actually updated from the service task.

.. _`i40e_get_netdev_stats_struct`:

i40e_get_netdev_stats_struct
============================

.. c:function:: struct rtnl_link_stats64 *i40e_get_netdev_stats_struct(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    Get statistics for netdev interface

    :param struct net_device \*netdev:
        network interface device structure

    :param struct rtnl_link_stats64 \*stats:
        *undescribed*

.. _`i40e_get_netdev_stats_struct.description`:

Description
-----------

Returns the address of the device statistics structure.
The statistics are actually updated from the service task.

.. _`i40e_vsi_reset_stats`:

i40e_vsi_reset_stats
====================

.. c:function:: void i40e_vsi_reset_stats(struct i40e_vsi *vsi)

    Resets all stats of the given vsi

    :param struct i40e_vsi \*vsi:
        the VSI to have its stats reset

.. _`i40e_pf_reset_stats`:

i40e_pf_reset_stats
===================

.. c:function:: void i40e_pf_reset_stats(struct i40e_pf *pf)

    Reset all of the stats for the given PF

    :param struct i40e_pf \*pf:
        the PF to be reset

.. _`i40e_stat_update48`:

i40e_stat_update48
==================

.. c:function:: void i40e_stat_update48(struct i40e_hw *hw, u32 hireg, u32 loreg, bool offset_loaded, u64 *offset, u64 *stat)

    read and update a 48 bit stat from the chip

    :param struct i40e_hw \*hw:
        ptr to the hardware info

    :param u32 hireg:
        the high 32 bit reg to read

    :param u32 loreg:
        the low 32 bit reg to read

    :param bool offset_loaded:
        has the initial offset been loaded yet

    :param u64 \*offset:
        ptr to current offset value

    :param u64 \*stat:
        ptr to the stat

.. _`i40e_stat_update48.description`:

Description
-----------

Since the device stats are not reset at PFReset, they likely will not
be zeroed when the driver starts.  We'll save the first values read
and use them as offsets to be subtracted from the raw values in order
to report stats that count from zero.  In the process, we also manage
the potential roll-over.

.. _`i40e_stat_update32`:

i40e_stat_update32
==================

.. c:function:: void i40e_stat_update32(struct i40e_hw *hw, u32 reg, bool offset_loaded, u64 *offset, u64 *stat)

    read and update a 32 bit stat from the chip

    :param struct i40e_hw \*hw:
        ptr to the hardware info

    :param u32 reg:
        the hw reg to read

    :param bool offset_loaded:
        has the initial offset been loaded yet

    :param u64 \*offset:
        ptr to current offset value

    :param u64 \*stat:
        ptr to the stat

.. _`i40e_update_eth_stats`:

i40e_update_eth_stats
=====================

.. c:function:: void i40e_update_eth_stats(struct i40e_vsi *vsi)

    Update VSI-specific ethernet statistics counters.

    :param struct i40e_vsi \*vsi:
        the VSI to be updated

.. _`i40e_update_veb_stats`:

i40e_update_veb_stats
=====================

.. c:function:: void i40e_update_veb_stats(struct i40e_veb *veb)

    Update Switch component statistics

    :param struct i40e_veb \*veb:
        the VEB being updated

.. _`i40e_update_fcoe_stats`:

i40e_update_fcoe_stats
======================

.. c:function:: void i40e_update_fcoe_stats(struct i40e_vsi *vsi)

    Update FCoE-specific ethernet statistics counters.

    :param struct i40e_vsi \*vsi:
        the VSI that is capable of doing FCoE

.. _`i40e_update_vsi_stats`:

i40e_update_vsi_stats
=====================

.. c:function:: void i40e_update_vsi_stats(struct i40e_vsi *vsi)

    Update the vsi statistics counters.

    :param struct i40e_vsi \*vsi:
        the VSI to be updated

.. _`i40e_update_vsi_stats.description`:

Description
-----------

There are a few instances where we store the same stat in a
couple of different structs.  This is partly because we have
the netdev stats that need to be filled out, which is slightly
different from the "eth_stats" defined by the chip and used in
VF communications.  We sort it out here.

.. _`i40e_update_pf_stats`:

i40e_update_pf_stats
====================

.. c:function:: void i40e_update_pf_stats(struct i40e_pf *pf)

    Update the PF statistics counters.

    :param struct i40e_pf \*pf:
        the PF to be updated

.. _`i40e_update_stats`:

i40e_update_stats
=================

.. c:function:: void i40e_update_stats(struct i40e_vsi *vsi)

    Update the various statistics counters.

    :param struct i40e_vsi \*vsi:
        the VSI to be updated

.. _`i40e_update_stats.description`:

Description
-----------

Update the various stats for this VSI and its related entities.

.. _`i40e_find_filter`:

i40e_find_filter
================

.. c:function:: struct i40e_mac_filter *i40e_find_filter(struct i40e_vsi *vsi, u8 *macaddr, s16 vlan, bool is_vf, bool is_netdev)

    Search VSI filter list for specific mac/vlan filter

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

    :param u8 \*macaddr:
        the MAC address

    :param s16 vlan:
        the vlan

    :param bool is_vf:
        make sure its a VF filter, else doesn't matter

    :param bool is_netdev:
        make sure its a netdev filter, else doesn't matter

.. _`i40e_find_filter.description`:

Description
-----------

Returns ptr to the filter object or NULL

.. _`i40e_find_mac`:

i40e_find_mac
=============

.. c:function:: struct i40e_mac_filter *i40e_find_mac(struct i40e_vsi *vsi, u8 *macaddr, bool is_vf, bool is_netdev)

    Find a mac addr in the macvlan filters list

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

    :param u8 \*macaddr:
        the MAC address we are searching for

    :param bool is_vf:
        make sure its a VF filter, else doesn't matter

    :param bool is_netdev:
        make sure its a netdev filter, else doesn't matter

.. _`i40e_find_mac.description`:

Description
-----------

Returns the first filter with the provided MAC address or NULL if
MAC address was not found

.. _`i40e_is_vsi_in_vlan`:

i40e_is_vsi_in_vlan
===================

.. c:function:: bool i40e_is_vsi_in_vlan(struct i40e_vsi *vsi)

    Check if VSI is in vlan mode

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

.. _`i40e_is_vsi_in_vlan.description`:

Description
-----------

Returns true if VSI is in vlan mode or false otherwise

.. _`i40e_put_mac_in_vlan`:

i40e_put_mac_in_vlan
====================

.. c:function:: struct i40e_mac_filter *i40e_put_mac_in_vlan(struct i40e_vsi *vsi, u8 *macaddr, bool is_vf, bool is_netdev)

    Make macvlan filters from macaddrs and vlans

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

    :param u8 \*macaddr:
        the mac address to be filtered

    :param bool is_vf:
        true if it is a VF

    :param bool is_netdev:
        true if it is a netdev

.. _`i40e_put_mac_in_vlan.description`:

Description
-----------

Goes through all the macvlan filters and adds a
macvlan filter for each unique vlan that already exists

Returns first filter found on success, else NULL

.. _`i40e_del_mac_all_vlan`:

i40e_del_mac_all_vlan
=====================

.. c:function:: int i40e_del_mac_all_vlan(struct i40e_vsi *vsi, u8 *macaddr, bool is_vf, bool is_netdev)

    Remove a MAC filter from all VLANS

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

    :param u8 \*macaddr:
        the mac address to be removed

    :param bool is_vf:
        true if it is a VF

    :param bool is_netdev:
        true if it is a netdev

.. _`i40e_del_mac_all_vlan.description`:

Description
-----------

Removes a given MAC address from a VSI, regardless of VLAN

Returns 0 for success, or error

.. _`i40e_rm_default_mac_filter`:

i40e_rm_default_mac_filter
==========================

.. c:function:: int i40e_rm_default_mac_filter(struct i40e_vsi *vsi, u8 *macaddr)

    Remove the default MAC filter set by NVM

    :param struct i40e_vsi \*vsi:
        the PF Main VSI - inappropriate for any other VSI

    :param u8 \*macaddr:
        the MAC address

.. _`i40e_rm_default_mac_filter.description`:

Description
-----------

Some older firmware configurations set up a default promiscuous VLAN
filter that needs to be removed.

.. _`i40e_add_filter`:

i40e_add_filter
===============

.. c:function:: struct i40e_mac_filter *i40e_add_filter(struct i40e_vsi *vsi, u8 *macaddr, s16 vlan, bool is_vf, bool is_netdev)

    Add a mac/vlan filter to the VSI

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

    :param u8 \*macaddr:
        the MAC address

    :param s16 vlan:
        the vlan

    :param bool is_vf:
        make sure its a VF filter, else doesn't matter

    :param bool is_netdev:
        make sure its a netdev filter, else doesn't matter

.. _`i40e_add_filter.description`:

Description
-----------

Returns ptr to the filter object or NULL when no memory available.

.. _`i40e_add_filter.note`:

NOTE
----

This function is expected to be called with mac_filter_list_lock
being held.

.. _`i40e_del_filter`:

i40e_del_filter
===============

.. c:function:: void i40e_del_filter(struct i40e_vsi *vsi, u8 *macaddr, s16 vlan, bool is_vf, bool is_netdev)

    Remove a mac/vlan filter from the VSI

    :param struct i40e_vsi \*vsi:
        the VSI to be searched

    :param u8 \*macaddr:
        the MAC address

    :param s16 vlan:
        the vlan

    :param bool is_vf:
        make sure it's a VF filter, else doesn't matter

    :param bool is_netdev:
        make sure it's a netdev filter, else doesn't matter

.. _`i40e_del_filter.note`:

NOTE
----

This function is expected to be called with mac_filter_list_lock
being held.

.. _`i40e_set_mac`:

i40e_set_mac
============

.. c:function:: int i40e_set_mac(struct net_device *netdev, void *p)

    NDO callback to set mac address

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`i40e_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40e_vsi_setup_queue_map`:

i40e_vsi_setup_queue_map
========================

.. c:function:: void i40e_vsi_setup_queue_map(struct i40e_vsi *vsi, struct i40e_vsi_context *ctxt, u8 enabled_tc, bool is_add)

    Setup a VSI queue map based on enabled_tc

    :param struct i40e_vsi \*vsi:
        the VSI being setup

    :param struct i40e_vsi_context \*ctxt:
        VSI context structure

    :param u8 enabled_tc:
        Enabled TCs bitmap

    :param bool is_add:
        True if called before Add VSI

.. _`i40e_vsi_setup_queue_map.description`:

Description
-----------

Setup VSI queue mapping for enabled traffic classes.

.. _`i40e_set_rx_mode`:

i40e_set_rx_mode
================

.. c:function:: void i40e_set_rx_mode(struct net_device *netdev)

    NDO callback to set the netdev filters

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_mac_filter_entry_clone`:

i40e_mac_filter_entry_clone
===========================

.. c:function:: struct i40e_mac_filter *i40e_mac_filter_entry_clone(struct i40e_mac_filter *src)

    Clones a MAC filter entry

    :param struct i40e_mac_filter \*src:
        source MAC filter entry to be clones

.. _`i40e_mac_filter_entry_clone.description`:

Description
-----------

Returns the pointer to newly cloned MAC filter entry or NULL
in case of error

.. _`i40e_undo_del_filter_entries`:

i40e_undo_del_filter_entries
============================

.. c:function:: void i40e_undo_del_filter_entries(struct i40e_vsi *vsi, struct list_head *from)

    Undo the changes made to MAC filter entries

    :param struct i40e_vsi \*vsi:
        pointer to vsi struct

    :param struct list_head \*from:
        Pointer to list which contains MAC filter entries - changes to
        those entries needs to be undone.

.. _`i40e_undo_del_filter_entries.description`:

Description
-----------

MAC filter entries from list were slated to be removed from device.

.. _`i40e_undo_add_filter_entries`:

i40e_undo_add_filter_entries
============================

.. c:function:: void i40e_undo_add_filter_entries(struct i40e_vsi *vsi)

    Undo the changes made to MAC filter entries

    :param struct i40e_vsi \*vsi:
        pointer to vsi struct

.. _`i40e_undo_add_filter_entries.description`:

Description
-----------

MAC filter entries from list were slated to be added from device.

.. _`i40e_cleanup_add_list`:

i40e_cleanup_add_list
=====================

.. c:function:: void i40e_cleanup_add_list(struct list_head *add_list)

    Deletes the element from add list and release memory

    :param struct list_head \*add_list:
        Pointer to list which contains MAC filter entries

.. _`i40e_sync_vsi_filters`:

i40e_sync_vsi_filters
=====================

.. c:function:: int i40e_sync_vsi_filters(struct i40e_vsi *vsi)

    Update the VSI filter list to the HW

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_sync_vsi_filters.description`:

Description
-----------

Push any outstanding VSI filter changes through the AdminQ.

Returns 0 or error value

.. _`i40e_sync_filters_subtask`:

i40e_sync_filters_subtask
=========================

.. c:function:: void i40e_sync_filters_subtask(struct i40e_pf *pf)

    Sync the VSI filter list with HW

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_change_mtu`:

i40e_change_mtu
===============

.. c:function:: int i40e_change_mtu(struct net_device *netdev, int new_mtu)

    NDO callback to change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`i40e_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40e_ioctl`:

i40e_ioctl
==========

.. c:function:: int i40e_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    Access the hwtstamp interface

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ifreq \*ifr:
        interface request data

    :param int cmd:
        ioctl command

.. _`i40e_vlan_stripping_enable`:

i40e_vlan_stripping_enable
==========================

.. c:function:: void i40e_vlan_stripping_enable(struct i40e_vsi *vsi)

    Turn on vlan stripping for the VSI

    :param struct i40e_vsi \*vsi:
        the vsi being adjusted

.. _`i40e_vlan_stripping_disable`:

i40e_vlan_stripping_disable
===========================

.. c:function:: void i40e_vlan_stripping_disable(struct i40e_vsi *vsi)

    Turn off vlan stripping for the VSI

    :param struct i40e_vsi \*vsi:
        the vsi being adjusted

.. _`i40e_vlan_rx_register`:

i40e_vlan_rx_register
=====================

.. c:function:: void i40e_vlan_rx_register(struct net_device *netdev, u32 features)

    Setup or shutdown vlan offload

    :param struct net_device \*netdev:
        network interface to be adjusted

    :param u32 features:
        netdev features to test if VLAN offload is enabled or not

.. _`i40e_vsi_add_vlan`:

i40e_vsi_add_vlan
=================

.. c:function:: int i40e_vsi_add_vlan(struct i40e_vsi *vsi, s16 vid)

    Add vsi membership for given vlan

    :param struct i40e_vsi \*vsi:
        the vsi being configured

    :param s16 vid:
        vlan id to be added (0 = untagged only , -1 = any)

.. _`i40e_vsi_kill_vlan`:

i40e_vsi_kill_vlan
==================

.. c:function:: int i40e_vsi_kill_vlan(struct i40e_vsi *vsi, s16 vid)

    Remove vsi membership for given vlan

    :param struct i40e_vsi \*vsi:
        the vsi being configured

    :param s16 vid:
        vlan id to be removed (0 = untagged only , -1 = any)

.. _`i40e_vsi_kill_vlan.return`:

Return
------

0 on success or negative otherwise

.. _`i40e_vlan_rx_add_vid`:

i40e_vlan_rx_add_vid
====================

.. c:function:: int i40e_vlan_rx_add_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Add a vlan id filter to HW offload

    :param struct net_device \*netdev:
        network interface to be adjusted

    :param __always_unused __be16 proto:
        *undescribed*

    :param u16 vid:
        vlan id to be added

.. _`i40e_vlan_rx_add_vid.description`:

Description
-----------

net_device_ops implementation for adding vlan ids

.. _`i40e_vlan_rx_kill_vid`:

i40e_vlan_rx_kill_vid
=====================

.. c:function:: int i40e_vlan_rx_kill_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Remove a vlan id filter from HW offload

    :param struct net_device \*netdev:
        network interface to be adjusted

    :param __always_unused __be16 proto:
        *undescribed*

    :param u16 vid:
        vlan id to be removed

.. _`i40e_vlan_rx_kill_vid.description`:

Description
-----------

net_device_ops implementation for removing vlan ids

.. _`i40e_restore_vlan`:

i40e_restore_vlan
=================

.. c:function:: void i40e_restore_vlan(struct i40e_vsi *vsi)

    Reinstate vlans when vsi/netdev comes back up

    :param struct i40e_vsi \*vsi:
        the vsi being brought back up

.. _`i40e_vsi_add_pvid`:

i40e_vsi_add_pvid
=================

.. c:function:: int i40e_vsi_add_pvid(struct i40e_vsi *vsi, u16 vid)

    Add pvid for the VSI

    :param struct i40e_vsi \*vsi:
        the vsi being adjusted

    :param u16 vid:
        the vlan id to set as a PVID

.. _`i40e_vsi_remove_pvid`:

i40e_vsi_remove_pvid
====================

.. c:function:: void i40e_vsi_remove_pvid(struct i40e_vsi *vsi)

    Remove the pvid from the VSI

    :param struct i40e_vsi \*vsi:
        the vsi being adjusted

.. _`i40e_vsi_remove_pvid.description`:

Description
-----------

Just use the \ :c:func:`vlan_rx_register`\  service to put it back to normal

.. _`i40e_vsi_setup_tx_resources`:

i40e_vsi_setup_tx_resources
===========================

.. c:function:: int i40e_vsi_setup_tx_resources(struct i40e_vsi *vsi)

    Allocate VSI Tx queue resources

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_vsi_setup_tx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`i40e_vsi_free_tx_resources`:

i40e_vsi_free_tx_resources
==========================

.. c:function:: void i40e_vsi_free_tx_resources(struct i40e_vsi *vsi)

    Free Tx resources for VSI queues

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_vsi_free_tx_resources.description`:

Description
-----------

Free VSI's transmit software resources

.. _`i40e_vsi_setup_rx_resources`:

i40e_vsi_setup_rx_resources
===========================

.. c:function:: int i40e_vsi_setup_rx_resources(struct i40e_vsi *vsi)

    Allocate VSI queues Rx resources

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_vsi_setup_rx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`i40e_vsi_free_rx_resources`:

i40e_vsi_free_rx_resources
==========================

.. c:function:: void i40e_vsi_free_rx_resources(struct i40e_vsi *vsi)

    Free Rx Resources for VSI queues

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_vsi_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`i40e_config_xps_tx_ring`:

i40e_config_xps_tx_ring
=======================

.. c:function:: void i40e_config_xps_tx_ring(struct i40e_ring *ring)

    Configure XPS for a Tx ring

    :param struct i40e_ring \*ring:
        The Tx ring to configure

.. _`i40e_config_xps_tx_ring.description`:

Description
-----------

This enables/disables XPS for a given Tx descriptor ring
based on the TCs enabled for the VSI that ring belongs to.

.. _`i40e_configure_tx_ring`:

i40e_configure_tx_ring
======================

.. c:function:: int i40e_configure_tx_ring(struct i40e_ring *ring)

    Configure a transmit ring context and rest

    :param struct i40e_ring \*ring:
        The Tx ring to configure

.. _`i40e_configure_tx_ring.description`:

Description
-----------

Configure the Tx descriptor ring in the HMC context.

.. _`i40e_configure_rx_ring`:

i40e_configure_rx_ring
======================

.. c:function:: int i40e_configure_rx_ring(struct i40e_ring *ring)

    Configure a receive ring context

    :param struct i40e_ring \*ring:
        The Rx ring to configure

.. _`i40e_configure_rx_ring.description`:

Description
-----------

Configure the Rx descriptor ring in the HMC context.

.. _`i40e_vsi_configure_tx`:

i40e_vsi_configure_tx
=====================

.. c:function:: int i40e_vsi_configure_tx(struct i40e_vsi *vsi)

    Configure the VSI for Tx

    :param struct i40e_vsi \*vsi:
        VSI structure describing this set of rings and resources

.. _`i40e_vsi_configure_tx.description`:

Description
-----------

Configure the Tx VSI for operation.

.. _`i40e_vsi_configure_rx`:

i40e_vsi_configure_rx
=====================

.. c:function:: int i40e_vsi_configure_rx(struct i40e_vsi *vsi)

    Configure the VSI for Rx

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_configure_rx.description`:

Description
-----------

Configure the Rx VSI for operation.

.. _`i40e_vsi_config_dcb_rings`:

i40e_vsi_config_dcb_rings
=========================

.. c:function:: void i40e_vsi_config_dcb_rings(struct i40e_vsi *vsi)

    Update rings to reflect DCB TC

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_set_vsi_rx_mode`:

i40e_set_vsi_rx_mode
====================

.. c:function:: void i40e_set_vsi_rx_mode(struct i40e_vsi *vsi)

    Call set_rx_mode on a VSI

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_fdir_filter_restore`:

i40e_fdir_filter_restore
========================

.. c:function:: void i40e_fdir_filter_restore(struct i40e_vsi *vsi)

    Restore the Sideband Flow Director filters

    :param struct i40e_vsi \*vsi:
        Pointer to the targeted VSI

.. _`i40e_fdir_filter_restore.description`:

Description
-----------

This function replays the hlist on the hw where all the SB Flow Director
filters were saved.

.. _`i40e_vsi_configure`:

i40e_vsi_configure
==================

.. c:function:: int i40e_vsi_configure(struct i40e_vsi *vsi)

    Set up the VSI for action

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_configure_msix`:

i40e_vsi_configure_msix
=======================

.. c:function:: void i40e_vsi_configure_msix(struct i40e_vsi *vsi)

    MSIX mode Interrupt Config in the HW

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_enable_misc_int_causes`:

i40e_enable_misc_int_causes
===========================

.. c:function:: void i40e_enable_misc_int_causes(struct i40e_pf *pf)

    enable the non-queue interrupts

    :param struct i40e_pf \*pf:
        *undescribed*

.. _`i40e_configure_msi_and_legacy`:

i40e_configure_msi_and_legacy
=============================

.. c:function:: void i40e_configure_msi_and_legacy(struct i40e_vsi *vsi)

    Legacy mode interrupt config in the HW

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_irq_dynamic_disable_icr0`:

i40e_irq_dynamic_disable_icr0
=============================

.. c:function:: void i40e_irq_dynamic_disable_icr0(struct i40e_pf *pf)

    Disable default interrupt generation for icr0

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_irq_dynamic_enable_icr0`:

i40e_irq_dynamic_enable_icr0
============================

.. c:function:: void i40e_irq_dynamic_enable_icr0(struct i40e_pf *pf, bool clearpba)

    Enable default interrupt generation for icr0

    :param struct i40e_pf \*pf:
        board private structure

    :param bool clearpba:
        true when all pending interrupt events should be cleared

.. _`i40e_msix_clean_rings`:

i40e_msix_clean_rings
=====================

.. c:function:: irqreturn_t i40e_msix_clean_rings(int irq, void *data)

    MSIX mode Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a q_vector

.. _`i40e_vsi_request_irq_msix`:

i40e_vsi_request_irq_msix
=========================

.. c:function:: int i40e_vsi_request_irq_msix(struct i40e_vsi *vsi, char *basename)

    Initialize MSI-X interrupts

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param char \*basename:
        name for the vector

.. _`i40e_vsi_request_irq_msix.description`:

Description
-----------

Allocates MSI-X vectors and requests interrupts from the kernel.

.. _`i40e_vsi_disable_irq`:

i40e_vsi_disable_irq
====================

.. c:function:: void i40e_vsi_disable_irq(struct i40e_vsi *vsi)

    Mask off queue interrupt generation on the VSI

    :param struct i40e_vsi \*vsi:
        the VSI being un-configured

.. _`i40e_vsi_enable_irq`:

i40e_vsi_enable_irq
===================

.. c:function:: int i40e_vsi_enable_irq(struct i40e_vsi *vsi)

    Enable IRQ for the given VSI

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_stop_misc_vector`:

i40e_stop_misc_vector
=====================

.. c:function:: void i40e_stop_misc_vector(struct i40e_pf *pf)

    Stop the vector that handles non-queue events

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_intr`:

i40e_intr
=========

.. c:function:: irqreturn_t i40e_intr(int irq, void *data)

    MSI/Legacy and non-queue interrupt handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a q_vector

.. _`i40e_intr.description`:

Description
-----------

This is the handler used for all MSI/Legacy interrupts, and deals
with both queue and non-queue interrupts.  This is also used in
MSIX mode to handle the non-queue interrupts.

.. _`i40e_clean_fdir_tx_irq`:

i40e_clean_fdir_tx_irq
======================

.. c:function:: bool i40e_clean_fdir_tx_irq(struct i40e_ring *tx_ring, int budget)

    Reclaim resources after transmit completes

    :param struct i40e_ring \*tx_ring:
        tx ring to clean

    :param int budget:
        how many cleans we're allowed

.. _`i40e_clean_fdir_tx_irq.description`:

Description
-----------

Returns true if there's any budget left (e.g. the clean is finished)

.. _`i40e_fdir_clean_ring`:

i40e_fdir_clean_ring
====================

.. c:function:: irqreturn_t i40e_fdir_clean_ring(int irq, void *data)

    Interrupt Handler for FDIR SB ring

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a q_vector

.. _`i40e_map_vector_to_qp`:

i40e_map_vector_to_qp
=====================

.. c:function:: void i40e_map_vector_to_qp(struct i40e_vsi *vsi, int v_idx, int qp_idx)

    Assigns the queue pair to the vector

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param int v_idx:
        vector index

    :param int qp_idx:
        queue pair index

.. _`i40e_vsi_map_rings_to_vectors`:

i40e_vsi_map_rings_to_vectors
=============================

.. c:function:: void i40e_vsi_map_rings_to_vectors(struct i40e_vsi *vsi)

    Maps descriptor rings to vectors

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_map_rings_to_vectors.description`:

Description
-----------

This function maps descriptor rings to the queue-specific vectors
we were allotted through the MSI-X enabling code.  Ideally, we'd have
one vector per queue pair, but on a constrained vector budget, we
group the queue pairs as "efficiently" as possible.

.. _`i40e_vsi_request_irq`:

i40e_vsi_request_irq
====================

.. c:function:: int i40e_vsi_request_irq(struct i40e_vsi *vsi, char *basename)

    Request IRQ from the OS

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param char \*basename:
        name for the vector

.. _`i40e_netpoll`:

i40e_netpoll
============

.. c:function:: void i40e_netpoll(struct net_device *netdev)

    A Polling 'interrupt' handler

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_netpoll.description`:

Description
-----------

This is used by netconsole to send skbs without having to re-enable
interrupts.  It's not called while the normal interrupt routine is executing.

.. _`i40e_pf_txq_wait`:

i40e_pf_txq_wait
================

.. c:function:: int i40e_pf_txq_wait(struct i40e_pf *pf, int pf_q, bool enable)

    Wait for a PF's Tx queue to be enabled or disabled

    :param struct i40e_pf \*pf:
        the PF being configured

    :param int pf_q:
        the PF queue

    :param bool enable:
        enable or disable state of the queue

.. _`i40e_pf_txq_wait.description`:

Description
-----------

This routine will wait for the given Tx queue of the PF to reach the
enabled or disabled state.
Returns -ETIMEDOUT in case of failing to reach the requested state after
multiple retries; else will return 0 in case of success.

.. _`i40e_vsi_control_tx`:

i40e_vsi_control_tx
===================

.. c:function:: int i40e_vsi_control_tx(struct i40e_vsi *vsi, bool enable)

    Start or stop a VSI's rings

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param bool enable:
        start or stop the rings

.. _`i40e_pf_rxq_wait`:

i40e_pf_rxq_wait
================

.. c:function:: int i40e_pf_rxq_wait(struct i40e_pf *pf, int pf_q, bool enable)

    Wait for a PF's Rx queue to be enabled or disabled

    :param struct i40e_pf \*pf:
        the PF being configured

    :param int pf_q:
        the PF queue

    :param bool enable:
        enable or disable state of the queue

.. _`i40e_pf_rxq_wait.description`:

Description
-----------

This routine will wait for the given Rx queue of the PF to reach the
enabled or disabled state.
Returns -ETIMEDOUT in case of failing to reach the requested state after
multiple retries; else will return 0 in case of success.

.. _`i40e_vsi_control_rx`:

i40e_vsi_control_rx
===================

.. c:function:: int i40e_vsi_control_rx(struct i40e_vsi *vsi, bool enable)

    Start or stop a VSI's rings

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param bool enable:
        start or stop the rings

.. _`i40e_vsi_control_rings`:

i40e_vsi_control_rings
======================

.. c:function:: int i40e_vsi_control_rings(struct i40e_vsi *vsi, bool request)

    Start or stop a VSI's rings

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param bool request:
        *undescribed*

.. _`i40e_vsi_free_irq`:

i40e_vsi_free_irq
=================

.. c:function:: void i40e_vsi_free_irq(struct i40e_vsi *vsi)

    Free the irq association with the OS

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_free_q_vector`:

i40e_free_q_vector
==================

.. c:function:: void i40e_free_q_vector(struct i40e_vsi *vsi, int v_idx)

    Free memory allocated for specific interrupt vector

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param int v_idx:
        Index of vector to be freed

.. _`i40e_free_q_vector.description`:

Description
-----------

This function frees the memory allocated to the q_vector.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`i40e_vsi_free_q_vectors`:

i40e_vsi_free_q_vectors
=======================

.. c:function:: void i40e_vsi_free_q_vectors(struct i40e_vsi *vsi)

    Free memory allocated for interrupt vectors

    :param struct i40e_vsi \*vsi:
        the VSI being un-configured

.. _`i40e_vsi_free_q_vectors.description`:

Description
-----------

This frees the memory allocated to the q_vectors and
deletes references to the NAPI struct.

.. _`i40e_reset_interrupt_capability`:

i40e_reset_interrupt_capability
===============================

.. c:function:: void i40e_reset_interrupt_capability(struct i40e_pf *pf)

    Disable interrupt setup in OS

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_clear_interrupt_scheme`:

i40e_clear_interrupt_scheme
===========================

.. c:function:: void i40e_clear_interrupt_scheme(struct i40e_pf *pf)

    Clear the current interrupt scheme settings

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_clear_interrupt_scheme.description`:

Description
-----------

We go through and clear interrupt specific resources and reset the structure
to pre-load conditions

.. _`i40e_napi_enable_all`:

i40e_napi_enable_all
====================

.. c:function:: void i40e_napi_enable_all(struct i40e_vsi *vsi)

    Enable NAPI for all q_vectors in the VSI

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_napi_disable_all`:

i40e_napi_disable_all
=====================

.. c:function:: void i40e_napi_disable_all(struct i40e_vsi *vsi)

    Disable NAPI for all q_vectors in the VSI

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_close`:

i40e_vsi_close
==============

.. c:function:: void i40e_vsi_close(struct i40e_vsi *vsi)

    Shut down a VSI

    :param struct i40e_vsi \*vsi:
        the vsi to be quelled

.. _`i40e_quiesce_vsi`:

i40e_quiesce_vsi
================

.. c:function:: void i40e_quiesce_vsi(struct i40e_vsi *vsi)

    Pause a given VSI

    :param struct i40e_vsi \*vsi:
        the VSI being paused

.. _`i40e_unquiesce_vsi`:

i40e_unquiesce_vsi
==================

.. c:function:: void i40e_unquiesce_vsi(struct i40e_vsi *vsi)

    Resume a given VSI

    :param struct i40e_vsi \*vsi:
        the VSI being resumed

.. _`i40e_pf_quiesce_all_vsi`:

i40e_pf_quiesce_all_vsi
=======================

.. c:function:: void i40e_pf_quiesce_all_vsi(struct i40e_pf *pf)

    Pause all VSIs on a PF

    :param struct i40e_pf \*pf:
        the PF

.. _`i40e_pf_unquiesce_all_vsi`:

i40e_pf_unquiesce_all_vsi
=========================

.. c:function:: void i40e_pf_unquiesce_all_vsi(struct i40e_pf *pf)

    Resume all VSIs on a PF

    :param struct i40e_pf \*pf:
        the PF

.. _`i40e_vsi_wait_queues_disabled`:

i40e_vsi_wait_queues_disabled
=============================

.. c:function:: int i40e_vsi_wait_queues_disabled(struct i40e_vsi *vsi)

    Wait for VSI's queues to be disabled

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_wait_queues_disabled.description`:

Description
-----------

This function waits for the given VSI's queues to be disabled.

.. _`i40e_pf_wait_queues_disabled`:

i40e_pf_wait_queues_disabled
============================

.. c:function:: int i40e_pf_wait_queues_disabled(struct i40e_pf *pf)

    Wait for all queues of PF VSIs to be disabled

    :param struct i40e_pf \*pf:
        the PF

.. _`i40e_pf_wait_queues_disabled.description`:

Description
-----------

This function waits for the queues to be in disabled state for all the
VSIs that are managed by this PF.

.. _`i40e_detect_recover_hung_queue`:

i40e_detect_recover_hung_queue
==============================

.. c:function:: void i40e_detect_recover_hung_queue(int q_idx, struct i40e_vsi *vsi)

    Function to detect and recover hung_queue

    :param int q_idx:
        TX queue number

    :param struct i40e_vsi \*vsi:
        Pointer to VSI struct

.. _`i40e_detect_recover_hung_queue.description`:

Description
-----------

This function checks specified queue for given VSI. Detects hung condition.
Sets hung bit since it is two step process. Before next run of service task
if napi_poll runs, it reset 'hung' bit for respective q_vector. If not,
hung condition remain unchanged and during subsequent run, this function
issues SW interrupt to recover from hung condition.

.. _`i40e_detect_recover_hung`:

i40e_detect_recover_hung
========================

.. c:function:: void i40e_detect_recover_hung(struct i40e_pf *pf)

    Function to detect and recover hung_queues

    :param struct i40e_pf \*pf:
        pointer to PF struct

.. _`i40e_detect_recover_hung.description`:

Description
-----------

LAN VSI has netdev and netdev has TX queues. This function is to check
each of those TX queues if they are hung, trigger recovery by issuing
SW interrupt.

.. _`i40e_get_iscsi_tc_map`:

i40e_get_iscsi_tc_map
=====================

.. c:function:: u8 i40e_get_iscsi_tc_map(struct i40e_pf *pf)

    Return TC map for iSCSI APP

    :param struct i40e_pf \*pf:
        pointer to PF

.. _`i40e_get_iscsi_tc_map.description`:

Description
-----------

Get TC map for ISCSI PF type that will include iSCSI TC
and LAN TC.

.. _`i40e_dcb_get_num_tc`:

i40e_dcb_get_num_tc
===================

.. c:function:: u8 i40e_dcb_get_num_tc(struct i40e_dcbx_config *dcbcfg)

    Get the number of TCs from DCBx config

    :param struct i40e_dcbx_config \*dcbcfg:
        the corresponding DCBx configuration structure

.. _`i40e_dcb_get_num_tc.description`:

Description
-----------

Return the number of TCs from given DCBx configuration

.. _`i40e_dcb_get_enabled_tc`:

i40e_dcb_get_enabled_tc
=======================

.. c:function:: u8 i40e_dcb_get_enabled_tc(struct i40e_dcbx_config *dcbcfg)

    Get enabled traffic classes

    :param struct i40e_dcbx_config \*dcbcfg:
        the corresponding DCBx configuration structure

.. _`i40e_dcb_get_enabled_tc.description`:

Description
-----------

Query the current DCB configuration and return the number of
traffic classes enabled from the given DCBX config

.. _`i40e_pf_get_num_tc`:

i40e_pf_get_num_tc
==================

.. c:function:: u8 i40e_pf_get_num_tc(struct i40e_pf *pf)

    Get enabled traffic classes for PF

    :param struct i40e_pf \*pf:
        PF being queried

.. _`i40e_pf_get_num_tc.description`:

Description
-----------

Return number of traffic classes enabled for the given PF

.. _`i40e_pf_get_default_tc`:

i40e_pf_get_default_tc
======================

.. c:function:: u8 i40e_pf_get_default_tc(struct i40e_pf *pf)

    Get bitmap for first enabled TC

    :param struct i40e_pf \*pf:
        PF being queried

.. _`i40e_pf_get_default_tc.description`:

Description
-----------

Return a bitmap for first enabled traffic class for this PF.

.. _`i40e_pf_get_tc_map`:

i40e_pf_get_tc_map
==================

.. c:function:: u8 i40e_pf_get_tc_map(struct i40e_pf *pf)

    Get bitmap for enabled traffic classes

    :param struct i40e_pf \*pf:
        PF being queried

.. _`i40e_pf_get_tc_map.description`:

Description
-----------

Return a bitmap for enabled traffic classes for this PF.

.. _`i40e_vsi_get_bw_info`:

i40e_vsi_get_bw_info
====================

.. c:function:: int i40e_vsi_get_bw_info(struct i40e_vsi *vsi)

    Query VSI BW Information

    :param struct i40e_vsi \*vsi:
        the VSI being queried

.. _`i40e_vsi_get_bw_info.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`i40e_vsi_configure_bw_alloc`:

i40e_vsi_configure_bw_alloc
===========================

.. c:function:: int i40e_vsi_configure_bw_alloc(struct i40e_vsi *vsi, u8 enabled_tc, u8 *bw_share)

    Configure VSI BW allocation per TC

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param u8 enabled_tc:
        TC bitmap

    :param u8 \*bw_share:
        *undescribed*

.. _`i40e_vsi_configure_bw_alloc.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`i40e_vsi_config_netdev_tc`:

i40e_vsi_config_netdev_tc
=========================

.. c:function:: void i40e_vsi_config_netdev_tc(struct i40e_vsi *vsi, u8 enabled_tc)

    Setup the netdev TC configuration

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param u8 enabled_tc:
        TC map to be enabled

.. _`i40e_vsi_update_queue_map`:

i40e_vsi_update_queue_map
=========================

.. c:function:: void i40e_vsi_update_queue_map(struct i40e_vsi *vsi, struct i40e_vsi_context *ctxt)

    Update our copy of VSi info with new queue map

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param struct i40e_vsi_context \*ctxt:
        the ctxt buffer returned from AQ VSI update param command

.. _`i40e_vsi_config_tc`:

i40e_vsi_config_tc
==================

.. c:function:: int i40e_vsi_config_tc(struct i40e_vsi *vsi, u8 enabled_tc)

    Configure VSI Tx Scheduler for given TC map

    :param struct i40e_vsi \*vsi:
        VSI to be configured

    :param u8 enabled_tc:
        TC bitmap

.. _`i40e_vsi_config_tc.description`:

Description
-----------

This configures a particular VSI for TCs that are mapped to the
given TC bitmap. It uses default bandwidth share for TCs across
VSIs to configure TC for a particular VSI.

.. _`i40e_vsi_config_tc.note`:

NOTE
----

It is expected that the VSI queues have been quisced before calling
this function.

.. _`i40e_veb_config_tc`:

i40e_veb_config_tc
==================

.. c:function:: int i40e_veb_config_tc(struct i40e_veb *veb, u8 enabled_tc)

    Configure TCs for given VEB

    :param struct i40e_veb \*veb:
        given VEB

    :param u8 enabled_tc:
        TC bitmap

.. _`i40e_veb_config_tc.description`:

Description
-----------

Configures given TC bitmap for VEB (switching) element

.. _`i40e_dcb_reconfigure`:

i40e_dcb_reconfigure
====================

.. c:function:: void i40e_dcb_reconfigure(struct i40e_pf *pf)

    Reconfigure all VEBs and VSIs

    :param struct i40e_pf \*pf:
        PF struct

.. _`i40e_dcb_reconfigure.description`:

Description
-----------

Reconfigure VEB/VSIs on a given PF; it is assumed that
the caller would've quiesce all the VSIs before calling
this function

.. _`i40e_resume_port_tx`:

i40e_resume_port_tx
===================

.. c:function:: int i40e_resume_port_tx(struct i40e_pf *pf)

    Resume port Tx

    :param struct i40e_pf \*pf:
        PF struct

.. _`i40e_resume_port_tx.description`:

Description
-----------

Resume a port's Tx and issue a PF reset in case of failure to
resume.

.. _`i40e_init_pf_dcb`:

i40e_init_pf_dcb
================

.. c:function:: int i40e_init_pf_dcb(struct i40e_pf *pf)

    Initialize DCB configuration

    :param struct i40e_pf \*pf:
        PF being configured

.. _`i40e_init_pf_dcb.description`:

Description
-----------

Query the current DCB configuration and cache it
in the hardware structure

.. _`i40e_print_link_message`:

i40e_print_link_message
=======================

.. c:function:: void i40e_print_link_message(struct i40e_vsi *vsi, bool isup)

    print link up or down

    :param struct i40e_vsi \*vsi:
        the VSI for which link needs a message

    :param bool isup:
        *undescribed*

.. _`i40e_up_complete`:

i40e_up_complete
================

.. c:function:: int i40e_up_complete(struct i40e_vsi *vsi)

    Finish the last steps of bringing up a connection

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_reinit_locked`:

i40e_vsi_reinit_locked
======================

.. c:function:: void i40e_vsi_reinit_locked(struct i40e_vsi *vsi)

    Reset the VSI

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_reinit_locked.description`:

Description
-----------

Rebuild the ring structs after some configuration
has changed, e.g. MTU size.

.. _`i40e_up`:

i40e_up
=======

.. c:function:: int i40e_up(struct i40e_vsi *vsi)

    Bring the connection back up after being down

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_down`:

i40e_down
=========

.. c:function:: void i40e_down(struct i40e_vsi *vsi)

    Shutdown the connection processing

    :param struct i40e_vsi \*vsi:
        the VSI being stopped

.. _`i40e_setup_tc`:

i40e_setup_tc
=============

.. c:function:: int i40e_setup_tc(struct net_device *netdev, u8 tc)

    configure multiple traffic classes

    :param struct net_device \*netdev:
        net device to configure

    :param u8 tc:
        number of traffic classes to enable

.. _`i40e_open`:

i40e_open
=========

.. c:function:: int i40e_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_open.description`:

Description
-----------

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the netdev watchdog subtask is
enabled, and the stack is notified that the interface is ready.

Returns 0 on success, negative value on failure

.. _`i40e_vsi_open`:

i40e_vsi_open
=============

.. c:function:: int i40e_vsi_open(struct i40e_vsi *vsi)

    :param struct i40e_vsi \*vsi:
        the VSI to open

.. _`i40e_vsi_open.description`:

Description
-----------

Finish initialization of the VSI.

Returns 0 on success, negative value on failure

.. _`i40e_fdir_filter_exit`:

i40e_fdir_filter_exit
=====================

.. c:function:: void i40e_fdir_filter_exit(struct i40e_pf *pf)

    Cleans up the Flow Director accounting

    :param struct i40e_pf \*pf:
        Pointer to PF

.. _`i40e_fdir_filter_exit.description`:

Description
-----------

This function destroys the hlist where all the Flow Director
filters were saved.

.. _`i40e_close`:

i40e_close
==========

.. c:function:: int i40e_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_close.description`:

Description
-----------

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the driver's control, but
this netdev interface is disabled.

Returns 0, this is not allowed to fail

.. _`i40e_do_reset`:

i40e_do_reset
=============

.. c:function:: void i40e_do_reset(struct i40e_pf *pf, u32 reset_flags)

    Start a PF or Core Reset sequence

    :param struct i40e_pf \*pf:
        board private structure

    :param u32 reset_flags:
        which reset is requested

.. _`i40e_do_reset.description`:

Description
-----------

The essential difference in resets is that the PF Reset
doesn't clear the packet buffers, doesn't reset the PE
firmware, and doesn't bother the other PFs on the chip.

.. _`i40e_dcb_need_reconfig`:

i40e_dcb_need_reconfig
======================

.. c:function:: bool i40e_dcb_need_reconfig(struct i40e_pf *pf, struct i40e_dcbx_config *old_cfg, struct i40e_dcbx_config *new_cfg)

    Check if DCB needs reconfig

    :param struct i40e_pf \*pf:
        board private structure

    :param struct i40e_dcbx_config \*old_cfg:
        current DCB config

    :param struct i40e_dcbx_config \*new_cfg:
        new DCB config

.. _`i40e_handle_lldp_event`:

i40e_handle_lldp_event
======================

.. c:function:: int i40e_handle_lldp_event(struct i40e_pf *pf, struct i40e_arq_event_info *e)

    Handle LLDP Change MIB event

    :param struct i40e_pf \*pf:
        board private structure

    :param struct i40e_arq_event_info \*e:
        event info posted on ARQ

.. _`i40e_do_reset_safe`:

i40e_do_reset_safe
==================

.. c:function:: void i40e_do_reset_safe(struct i40e_pf *pf, u32 reset_flags)

    Protected reset path for userland calls.

    :param struct i40e_pf \*pf:
        board private structure

    :param u32 reset_flags:
        which reset is requested

.. _`i40e_handle_lan_overflow_event`:

i40e_handle_lan_overflow_event
==============================

.. c:function:: void i40e_handle_lan_overflow_event(struct i40e_pf *pf, struct i40e_arq_event_info *e)

    Handler for LAN queue overflow event

    :param struct i40e_pf \*pf:
        board private structure

    :param struct i40e_arq_event_info \*e:
        event info posted on ARQ

.. _`i40e_handle_lan_overflow_event.description`:

Description
-----------

Handler for LAN Queue Overflow Event generated by the firmware for PF
and VF queues

.. _`i40e_service_event_complete`:

i40e_service_event_complete
===========================

.. c:function:: void i40e_service_event_complete(struct i40e_pf *pf)

    Finish up the service event

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_get_cur_guaranteed_fd_count`:

i40e_get_cur_guaranteed_fd_count
================================

.. c:function:: u32 i40e_get_cur_guaranteed_fd_count(struct i40e_pf *pf)

    Get the consumed guaranteed FD filters

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_get_current_fd_count`:

i40e_get_current_fd_count
=========================

.. c:function:: u32 i40e_get_current_fd_count(struct i40e_pf *pf)

    Get total FD filters programmed for this PF

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_get_global_fd_count`:

i40e_get_global_fd_count
========================

.. c:function:: u32 i40e_get_global_fd_count(struct i40e_pf *pf)

    Get total FD filters programmed on device

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_fdir_check_and_reenable`:

i40e_fdir_check_and_reenable
============================

.. c:function:: void i40e_fdir_check_and_reenable(struct i40e_pf *pf)

    Function to reenabe FD ATR or SB if disabled

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_fdir_flush_and_replay`:

i40e_fdir_flush_and_replay
==========================

.. c:function:: void i40e_fdir_flush_and_replay(struct i40e_pf *pf)

    Function to flush all FD filters and replay SB

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_get_current_atr_cnt`:

i40e_get_current_atr_cnt
========================

.. c:function:: u32 i40e_get_current_atr_cnt(struct i40e_pf *pf)

    Get the count of total FD ATR filters programmed

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_fdir_reinit_subtask`:

i40e_fdir_reinit_subtask
========================

.. c:function:: void i40e_fdir_reinit_subtask(struct i40e_pf *pf)

    Worker thread to reinit FDIR filter table

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_vsi_link_event`:

i40e_vsi_link_event
===================

.. c:function:: void i40e_vsi_link_event(struct i40e_vsi *vsi, bool link_up)

    notify VSI of a link event

    :param struct i40e_vsi \*vsi:
        vsi to be notified

    :param bool link_up:
        link up or down

.. _`i40e_veb_link_event`:

i40e_veb_link_event
===================

.. c:function:: void i40e_veb_link_event(struct i40e_veb *veb, bool link_up)

    notify elements on the veb of a link event

    :param struct i40e_veb \*veb:
        veb to be notified

    :param bool link_up:
        link up or down

.. _`i40e_link_event`:

i40e_link_event
===============

.. c:function:: void i40e_link_event(struct i40e_pf *pf)

    Update netif_carrier status

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_watchdog_subtask`:

i40e_watchdog_subtask
=====================

.. c:function:: void i40e_watchdog_subtask(struct i40e_pf *pf)

    periodic checks not using event driven response

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_reset_subtask`:

i40e_reset_subtask
==================

.. c:function:: void i40e_reset_subtask(struct i40e_pf *pf)

    Set up for resetting the device and driver

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_handle_link_event`:

i40e_handle_link_event
======================

.. c:function:: void i40e_handle_link_event(struct i40e_pf *pf, struct i40e_arq_event_info *e)

    Handle link event

    :param struct i40e_pf \*pf:
        board private structure

    :param struct i40e_arq_event_info \*e:
        event info posted on ARQ

.. _`i40e_clean_adminq_subtask`:

i40e_clean_adminq_subtask
=========================

.. c:function:: void i40e_clean_adminq_subtask(struct i40e_pf *pf)

    Clean the AdminQ rings

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_verify_eeprom`:

i40e_verify_eeprom
==================

.. c:function:: void i40e_verify_eeprom(struct i40e_pf *pf)

    make sure eeprom is good to use

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_enable_pf_switch_lb`:

i40e_enable_pf_switch_lb
========================

.. c:function:: void i40e_enable_pf_switch_lb(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_enable_pf_switch_lb.description`:

Description
-----------

enable switch loop back or die - no point in a return value

.. _`i40e_disable_pf_switch_lb`:

i40e_disable_pf_switch_lb
=========================

.. c:function:: void i40e_disable_pf_switch_lb(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_disable_pf_switch_lb.description`:

Description
-----------

disable switch loop back or die - no point in a return value

.. _`i40e_config_bridge_mode`:

i40e_config_bridge_mode
=======================

.. c:function:: void i40e_config_bridge_mode(struct i40e_veb *veb)

    Configure the HW bridge mode

    :param struct i40e_veb \*veb:
        pointer to the bridge instance

.. _`i40e_config_bridge_mode.description`:

Description
-----------

Configure the loop back mode for the LAN VSI that is downlink to the
specified HW bridge instance. It is expected this function is called
when a new HW bridge is instantiated.

.. _`i40e_reconstitute_veb`:

i40e_reconstitute_veb
=====================

.. c:function:: int i40e_reconstitute_veb(struct i40e_veb *veb)

    rebuild the VEB and anything connected to it

    :param struct i40e_veb \*veb:
        pointer to the VEB instance

.. _`i40e_reconstitute_veb.description`:

Description
-----------

This is a recursive function that first builds the attached VSIs then
recurses in to build the next layer of VEB.  We track the connections
through our own index numbers because the seid's from the HW could
change across the reset.

.. _`i40e_get_capabilities`:

i40e_get_capabilities
=====================

.. c:function:: int i40e_get_capabilities(struct i40e_pf *pf)

    get info about the HW

    :param struct i40e_pf \*pf:
        the PF struct

.. _`i40e_fdir_sb_setup`:

i40e_fdir_sb_setup
==================

.. c:function:: void i40e_fdir_sb_setup(struct i40e_pf *pf)

    initialize the Flow Director resources for Sideband

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_fdir_teardown`:

i40e_fdir_teardown
==================

.. c:function:: void i40e_fdir_teardown(struct i40e_pf *pf)

    release the Flow Director resources

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_prep_for_reset`:

i40e_prep_for_reset
===================

.. c:function:: void i40e_prep_for_reset(struct i40e_pf *pf)

    prep for the core to reset

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_prep_for_reset.description`:

Description
-----------

Close up the VFs and other things in prep for PF Reset.

.. _`i40e_send_version`:

i40e_send_version
=================

.. c:function:: void i40e_send_version(struct i40e_pf *pf)

    update firmware with driver version

    :param struct i40e_pf \*pf:
        PF struct

.. _`i40e_reset_and_rebuild`:

i40e_reset_and_rebuild
======================

.. c:function:: void i40e_reset_and_rebuild(struct i40e_pf *pf, bool reinit)

    reset and rebuild using a saved config

    :param struct i40e_pf \*pf:
        board private structure

    :param bool reinit:
        if the Main VSI needs to re-initialized.

.. _`i40e_handle_reset_warning`:

i40e_handle_reset_warning
=========================

.. c:function:: void i40e_handle_reset_warning(struct i40e_pf *pf)

    prep for the PF to reset, reset and rebuild

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_handle_reset_warning.description`:

Description
-----------

Close up the VFs and other things in prep for a Core Reset,
then get ready to rebuild the world.

.. _`i40e_handle_mdd_event`:

i40e_handle_mdd_event
=====================

.. c:function:: void i40e_handle_mdd_event(struct i40e_pf *pf)

    :param struct i40e_pf \*pf:
        pointer to the PF structure

.. _`i40e_handle_mdd_event.description`:

Description
-----------

Called from the MDD irq handler to identify possibly malicious vfs

.. _`i40e_sync_udp_filters_subtask`:

i40e_sync_udp_filters_subtask
=============================

.. c:function:: void i40e_sync_udp_filters_subtask(struct i40e_pf *pf)

    Sync the VSI filter list with HW

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_service_task`:

i40e_service_task
=================

.. c:function:: void i40e_service_task(struct work_struct *work)

    Run the driver's async subtasks

    :param struct work_struct \*work:
        pointer to work_struct containing our data

.. _`i40e_service_timer`:

i40e_service_timer
==================

.. c:function:: void i40e_service_timer(unsigned long data)

    timer callback

    :param unsigned long data:
        pointer to PF struct

.. _`i40e_set_num_rings_in_vsi`:

i40e_set_num_rings_in_vsi
=========================

.. c:function:: int i40e_set_num_rings_in_vsi(struct i40e_vsi *vsi)

    Determine number of rings in the VSI

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_alloc_arrays`:

i40e_vsi_alloc_arrays
=====================

.. c:function:: int i40e_vsi_alloc_arrays(struct i40e_vsi *vsi, bool alloc_qvectors)

    Allocate queue and vector pointer arrays for the vsi

    :param struct i40e_vsi \*vsi:
        *undescribed*

    :param bool alloc_qvectors:
        a bool to specify if q_vectors need to be allocated.

.. _`i40e_vsi_alloc_arrays.on-error`:

On error
--------

returns error code (negative)

.. _`i40e_vsi_alloc_arrays.on-success`:

On success
----------

returns 0

.. _`i40e_vsi_mem_alloc`:

i40e_vsi_mem_alloc
==================

.. c:function:: int i40e_vsi_mem_alloc(struct i40e_pf *pf, enum i40e_vsi_type type)

    Allocates the next available struct vsi in the PF

    :param struct i40e_pf \*pf:
        board private structure

    :param enum i40e_vsi_type type:
        type of VSI

.. _`i40e_vsi_mem_alloc.on-error`:

On error
--------

returns error code (negative)

.. _`i40e_vsi_mem_alloc.on-success`:

On success
----------

returns vsi index in PF (positive)

.. _`i40e_vsi_free_arrays`:

i40e_vsi_free_arrays
====================

.. c:function:: void i40e_vsi_free_arrays(struct i40e_vsi *vsi, bool free_qvectors)

    Free queue and vector pointer arrays for the VSI

    :param struct i40e_vsi \*vsi:
        *undescribed*

    :param bool free_qvectors:
        a bool to specify if q_vectors need to be freed.

.. _`i40e_vsi_free_arrays.on-error`:

On error
--------

returns error code (negative)

.. _`i40e_vsi_free_arrays.on-success`:

On success
----------

returns 0

.. _`i40e_clear_rss_config_user`:

i40e_clear_rss_config_user
==========================

.. c:function:: void i40e_clear_rss_config_user(struct i40e_vsi *vsi)

    clear the user configured RSS hash keys and lookup table

    :param struct i40e_vsi \*vsi:
        Pointer to VSI structure

.. _`i40e_vsi_clear`:

i40e_vsi_clear
==============

.. c:function:: int i40e_vsi_clear(struct i40e_vsi *vsi)

    Deallocate the VSI provided

    :param struct i40e_vsi \*vsi:
        the VSI being un-configured

.. _`i40e_vsi_clear_rings`:

i40e_vsi_clear_rings
====================

.. c:function:: void i40e_vsi_clear_rings(struct i40e_vsi *vsi)

    Deallocates the Rx and Tx rings for the provided VSI

    :param struct i40e_vsi \*vsi:
        the VSI being cleaned

.. _`i40e_alloc_rings`:

i40e_alloc_rings
================

.. c:function:: int i40e_alloc_rings(struct i40e_vsi *vsi)

    Allocates the Rx and Tx rings for the provided VSI

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_reserve_msix_vectors`:

i40e_reserve_msix_vectors
=========================

.. c:function:: int i40e_reserve_msix_vectors(struct i40e_pf *pf, int vectors)

    Reserve MSI-X vectors in the kernel

    :param struct i40e_pf \*pf:
        board private structure

    :param int vectors:
        the number of MSI-X vectors to request

.. _`i40e_reserve_msix_vectors.description`:

Description
-----------

Returns the number of vectors reserved, or error

.. _`i40e_init_msix`:

i40e_init_msix
==============

.. c:function:: int i40e_init_msix(struct i40e_pf *pf)

    Setup the MSIX capability

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_init_msix.description`:

Description
-----------

Work with the OS to set up the MSIX vectors needed.

Returns the number of vectors reserved or negative on failure

.. _`i40e_vsi_alloc_q_vector`:

i40e_vsi_alloc_q_vector
=======================

.. c:function:: int i40e_vsi_alloc_q_vector(struct i40e_vsi *vsi, int v_idx, int cpu)

    Allocate memory for a single interrupt vector

    :param struct i40e_vsi \*vsi:
        the VSI being configured

    :param int v_idx:
        index of the vector in the vsi struct

    :param int cpu:
        cpu to be used on affinity_mask

.. _`i40e_vsi_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`i40e_vsi_alloc_q_vectors`:

i40e_vsi_alloc_q_vectors
========================

.. c:function:: int i40e_vsi_alloc_q_vectors(struct i40e_vsi *vsi)

    Allocate memory for interrupt vectors

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_vsi_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`i40e_init_interrupt_scheme`:

i40e_init_interrupt_scheme
==========================

.. c:function:: int i40e_init_interrupt_scheme(struct i40e_pf *pf)

    Determine proper interrupt scheme

    :param struct i40e_pf \*pf:
        board private structure to initialize

.. _`i40e_setup_misc_vector`:

i40e_setup_misc_vector
======================

.. c:function:: int i40e_setup_misc_vector(struct i40e_pf *pf)

    Setup the misc vector to handle non queue events

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_setup_misc_vector.description`:

Description
-----------

This sets up the handler for MSIX 0, which is used to manage the
non-queue interrupts, e.g. AdminQ and errors.  This is not used
when in MSI or Legacy interrupt mode.

.. _`i40e_config_rss_aq`:

i40e_config_rss_aq
==================

.. c:function:: int i40e_config_rss_aq(struct i40e_vsi *vsi, const u8 *seed, u8 *lut, u16 lut_size)

    Prepare for RSS using AQ commands

    :param struct i40e_vsi \*vsi:
        vsi structure

    :param const u8 \*seed:
        RSS hash seed

    :param u8 \*lut:
        *undescribed*

    :param u16 lut_size:
        *undescribed*

.. _`i40e_vsi_config_rss`:

i40e_vsi_config_rss
===================

.. c:function:: int i40e_vsi_config_rss(struct i40e_vsi *vsi)

    Prepare for VSI(VMDq) RSS if used

    :param struct i40e_vsi \*vsi:
        VSI structure

.. _`i40e_get_rss_aq`:

i40e_get_rss_aq
===============

.. c:function:: int i40e_get_rss_aq(struct i40e_vsi *vsi, const u8 *seed, u8 *lut, u16 lut_size)

    Get RSS keys and lut by using AQ commands

    :param struct i40e_vsi \*vsi:
        Pointer to vsi structure

    :param const u8 \*seed:
        Buffter to store the hash keys

    :param u8 \*lut:
        Buffer to store the lookup table entries

    :param u16 lut_size:
        Size of buffer to store the lookup table entries

.. _`i40e_get_rss_aq.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`i40e_config_rss_reg`:

i40e_config_rss_reg
===================

.. c:function:: int i40e_config_rss_reg(struct i40e_vsi *vsi, const u8 *seed, const u8 *lut, u16 lut_size)

    Configure RSS keys and lut by writing registers

    :param struct i40e_vsi \*vsi:
        Pointer to vsi structure

    :param const u8 \*seed:
        RSS hash seed

    :param const u8 \*lut:
        Lookup table

    :param u16 lut_size:
        Lookup table size

.. _`i40e_config_rss_reg.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40e_get_rss_reg`:

i40e_get_rss_reg
================

.. c:function:: int i40e_get_rss_reg(struct i40e_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Get the RSS keys and lut by reading registers

    :param struct i40e_vsi \*vsi:
        Pointer to VSI structure

    :param u8 \*seed:
        Buffer to store the keys

    :param u8 \*lut:
        Buffer to store the lookup table entries

    :param u16 lut_size:
        Size of buffer to store the lookup table entries

.. _`i40e_get_rss_reg.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40e_config_rss`:

i40e_config_rss
===============

.. c:function:: int i40e_config_rss(struct i40e_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Configure RSS keys and lut

    :param struct i40e_vsi \*vsi:
        Pointer to VSI structure

    :param u8 \*seed:
        RSS hash seed

    :param u8 \*lut:
        Lookup table

    :param u16 lut_size:
        Lookup table size

.. _`i40e_config_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`i40e_get_rss`:

i40e_get_rss
============

.. c:function:: int i40e_get_rss(struct i40e_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Get RSS keys and lut

    :param struct i40e_vsi \*vsi:
        Pointer to VSI structure

    :param u8 \*seed:
        Buffer to store the keys

    :param u8 \*lut:
        Buffer to store the lookup table entries

    :param u16 lut_size:
        *undescribed*

.. _`i40e_get_rss.lut_size`:

lut_size
--------

Size of buffer to store the lookup table entries

Returns 0 on success, negative on failure

.. _`i40e_fill_rss_lut`:

i40e_fill_rss_lut
=================

.. c:function:: void i40e_fill_rss_lut(struct i40e_pf *pf, u8 *lut, u16 rss_table_size, u16 rss_size)

    Fill the RSS lookup table with default values

    :param struct i40e_pf \*pf:
        Pointer to board private structure

    :param u8 \*lut:
        Lookup table

    :param u16 rss_table_size:
        Lookup table size

    :param u16 rss_size:
        Range of queue number for hashing

.. _`i40e_pf_config_rss`:

i40e_pf_config_rss
==================

.. c:function:: int i40e_pf_config_rss(struct i40e_pf *pf)

    Prepare for RSS if used

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_reconfig_rss_queues`:

i40e_reconfig_rss_queues
========================

.. c:function:: int i40e_reconfig_rss_queues(struct i40e_pf *pf, int queue_count)

    change number of queues for rss and rebuild

    :param struct i40e_pf \*pf:
        board private structure

    :param int queue_count:
        the requested queue count for rss.

.. _`i40e_reconfig_rss_queues.description`:

Description
-----------

returns 0 if rss is not enabled, if enabled returns the final rss queue
count which may be different from the requested queue count.

.. _`i40e_get_npar_bw_setting`:

i40e_get_npar_bw_setting
========================

.. c:function:: i40e_status i40e_get_npar_bw_setting(struct i40e_pf *pf)

    Retrieve BW settings for this PF partition

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_set_npar_bw_setting`:

i40e_set_npar_bw_setting
========================

.. c:function:: i40e_status i40e_set_npar_bw_setting(struct i40e_pf *pf)

    Set BW settings for this PF partition

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_commit_npar_bw_setting`:

i40e_commit_npar_bw_setting
===========================

.. c:function:: i40e_status i40e_commit_npar_bw_setting(struct i40e_pf *pf)

    Commit BW settings for this PF partition

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_sw_init`:

i40e_sw_init
============

.. c:function:: int i40e_sw_init(struct i40e_pf *pf)

    Initialize general software structures (struct i40e_pf)

    :param struct i40e_pf \*pf:
        board private structure to initialize

.. _`i40e_sw_init.description`:

Description
-----------

i40e_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`i40e_set_ntuple`:

i40e_set_ntuple
===============

.. c:function:: bool i40e_set_ntuple(struct i40e_pf *pf, netdev_features_t features)

    set the ntuple feature flag and take action

    :param struct i40e_pf \*pf:
        board private structure to initialize

    :param netdev_features_t features:
        the feature set that the stack is suggesting

.. _`i40e_set_ntuple.description`:

Description
-----------

returns a bool to indicate if reset needs to happen

.. _`i40e_set_features`:

i40e_set_features
=================

.. c:function:: int i40e_set_features(struct net_device *netdev, netdev_features_t features)

    set the netdev feature flags

    :param struct net_device \*netdev:
        ptr to the netdev being adjusted

    :param netdev_features_t features:
        the feature set that the stack is suggesting

.. _`i40e_get_udp_port_idx`:

i40e_get_udp_port_idx
=====================

.. c:function:: u8 i40e_get_udp_port_idx(struct i40e_pf *pf, __be16 port)

    Lookup a possibly offloaded for Rx UDP port

    :param struct i40e_pf \*pf:
        board private structure

    :param __be16 port:
        The UDP port to look up

.. _`i40e_get_udp_port_idx.description`:

Description
-----------

Returns the index number or I40E_MAX_PF_UDP_OFFLOAD_PORTS if port not found

.. _`i40e_add_vxlan_port`:

i40e_add_vxlan_port
===================

.. c:function:: void i40e_add_vxlan_port(struct net_device *netdev, sa_family_t sa_family, __be16 port)

    Get notifications about VXLAN ports that come up

    :param struct net_device \*netdev:
        This physical port's netdev

    :param sa_family_t sa_family:
        Socket Family that VXLAN is notifying us about

    :param __be16 port:
        New UDP port number that VXLAN started listening to

.. _`i40e_del_vxlan_port`:

i40e_del_vxlan_port
===================

.. c:function:: void i40e_del_vxlan_port(struct net_device *netdev, sa_family_t sa_family, __be16 port)

    Get notifications about VXLAN ports that go away

    :param struct net_device \*netdev:
        This physical port's netdev

    :param sa_family_t sa_family:
        Socket Family that VXLAN is notifying us about

    :param __be16 port:
        UDP port number that VXLAN stopped listening to

.. _`i40e_add_geneve_port`:

i40e_add_geneve_port
====================

.. c:function:: void i40e_add_geneve_port(struct net_device *netdev, sa_family_t sa_family, __be16 port)

    Get notifications about GENEVE ports that come up

    :param struct net_device \*netdev:
        This physical port's netdev

    :param sa_family_t sa_family:
        Socket Family that GENEVE is notifying us about

    :param __be16 port:
        New UDP port number that GENEVE started listening to

.. _`i40e_del_geneve_port`:

i40e_del_geneve_port
====================

.. c:function:: void i40e_del_geneve_port(struct net_device *netdev, sa_family_t sa_family, __be16 port)

    Get notifications about GENEVE ports that go away

    :param struct net_device \*netdev:
        This physical port's netdev

    :param sa_family_t sa_family:
        Socket Family that GENEVE is notifying us about

    :param __be16 port:
        UDP port number that GENEVE stopped listening to

.. _`i40e_ndo_fdb_add`:

i40e_ndo_fdb_add
================

.. c:function:: int i40e_ndo_fdb_add(struct ndmsg *ndm, struct nlattr  *tb[], struct net_device *dev, const unsigned char *addr, u16 vid, u16 flags)

    add an entry to the hardware database

    :param struct ndmsg \*ndm:
        the input from the stack

    :param struct nlattr  \*tb:
        pointer to array of nladdr (unused)

    :param struct net_device \*dev:
        the net device pointer

    :param const unsigned char \*addr:
        the MAC address entry being added

    :param u16 vid:
        *undescribed*

    :param u16 flags:
        instructions from stack about fdb operation

.. _`i40e_ndo_bridge_setlink`:

i40e_ndo_bridge_setlink
=======================

.. c:function:: int i40e_ndo_bridge_setlink(struct net_device *dev, struct nlmsghdr *nlh, u16 flags)

    Set the hardware bridge mode

    :param struct net_device \*dev:
        the netdev being configured

    :param struct nlmsghdr \*nlh:
        RTNL message

    :param u16 flags:
        *undescribed*

.. _`i40e_ndo_bridge_setlink.description`:

Description
-----------

Inserts a new hardware bridge if not already created and
enables the bridging mode requested (VEB or VEPA). If the
hardware bridge has already been inserted and the request
is to change the mode then that requires a PF reset to
allow rebuild of the components with required hardware
bridge mode enabled.

.. _`i40e_ndo_bridge_getlink`:

i40e_ndo_bridge_getlink
=======================

.. c:function:: int i40e_ndo_bridge_getlink(struct sk_buff *skb, u32 pid, u32 seq, struct net_device *dev, u32 __always_unused filter_mask, int nlflags)

    Get the hardware bridge mode

    :param struct sk_buff \*skb:
        skb buff

    :param u32 pid:
        process id

    :param u32 seq:
        RTNL message seq #

    :param struct net_device \*dev:
        the netdev being configured

    :param u32 __always_unused filter_mask:
        unused

    :param int nlflags:
        netlink flags passed in

.. _`i40e_ndo_bridge_getlink.description`:

Description
-----------

Return the mode in which the hardware bridge is operating in
i.e VEB or VEPA.

.. _`i40e_features_check`:

i40e_features_check
===================

.. c:function:: netdev_features_t i40e_features_check(struct sk_buff *skb, struct net_device *dev, netdev_features_t features)

    Validate encapsulated packet conforms to limits

    :param struct sk_buff \*skb:
        skb buff

    :param struct net_device \*dev:
        This physical port's netdev

    :param netdev_features_t features:
        Offload features that the stack believes apply

.. _`i40e_config_netdev`:

i40e_config_netdev
==================

.. c:function:: int i40e_config_netdev(struct i40e_vsi *vsi)

    Setup the netdev flags

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_config_netdev.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`i40e_vsi_delete`:

i40e_vsi_delete
===============

.. c:function:: void i40e_vsi_delete(struct i40e_vsi *vsi)

    Delete a VSI from the switch

    :param struct i40e_vsi \*vsi:
        the VSI being removed

.. _`i40e_vsi_delete.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`i40e_is_vsi_uplink_mode_veb`:

i40e_is_vsi_uplink_mode_veb
===========================

.. c:function:: int i40e_is_vsi_uplink_mode_veb(struct i40e_vsi *vsi)

    Check if the VSI's uplink bridge mode is VEB

    :param struct i40e_vsi \*vsi:
        the VSI being queried

.. _`i40e_is_vsi_uplink_mode_veb.description`:

Description
-----------

Returns 1 if HW bridge mode is VEB and return 0 in case of VEPA mode

.. _`i40e_add_vsi`:

i40e_add_vsi
============

.. c:function:: int i40e_add_vsi(struct i40e_vsi *vsi)

    Add a VSI to the switch

    :param struct i40e_vsi \*vsi:
        the VSI being configured

.. _`i40e_add_vsi.description`:

Description
-----------

This initializes a VSI context depending on the VSI type to be added and
passes it down to the add_vsi aq command.

.. _`i40e_vsi_release`:

i40e_vsi_release
================

.. c:function:: int i40e_vsi_release(struct i40e_vsi *vsi)

    Delete a VSI and free its resources

    :param struct i40e_vsi \*vsi:
        the VSI being removed

.. _`i40e_vsi_release.description`:

Description
-----------

Returns 0 on success or < 0 on error

.. _`i40e_vsi_setup_vectors`:

i40e_vsi_setup_vectors
======================

.. c:function:: int i40e_vsi_setup_vectors(struct i40e_vsi *vsi)

    Set up the q_vectors for the given VSI

    :param struct i40e_vsi \*vsi:
        ptr to the VSI

.. _`i40e_vsi_setup_vectors.description`:

Description
-----------

This should only be called after \ :c:func:`i40e_vsi_mem_alloc`\  which allocates the
corresponding SW VSI structure and initializes num_queue_pairs for the
newly allocated VSI.

Returns 0 on success or negative on failure

.. _`i40e_vsi_reinit_setup`:

i40e_vsi_reinit_setup
=====================

.. c:function:: struct i40e_vsi *i40e_vsi_reinit_setup(struct i40e_vsi *vsi)

    return and reallocate resources for a VSI

    :param struct i40e_vsi \*vsi:
        pointer to the vsi.

.. _`i40e_vsi_reinit_setup.description`:

Description
-----------

This re-allocates a vsi's queue resources.

Returns pointer to the successfully allocated and configured VSI sw struct
on success, otherwise returns NULL on failure.

.. _`i40e_macaddr_init`:

i40e_macaddr_init
=================

.. c:function:: int i40e_macaddr_init(struct i40e_vsi *vsi, u8 *macaddr)

    explicitly write the mac address filters.

    :param struct i40e_vsi \*vsi:
        pointer to the vsi.

    :param u8 \*macaddr:
        the MAC address

.. _`i40e_macaddr_init.description`:

Description
-----------

This is needed when the macaddr has been obtained by other
means than the default, e.g., from Open Firmware or IDPROM.
Returns 0 on success, negative on failure

.. _`i40e_vsi_setup`:

i40e_vsi_setup
==============

.. c:function:: struct i40e_vsi *i40e_vsi_setup(struct i40e_pf *pf, u8 type, u16 uplink_seid, u32 param1)

    Set up a VSI by a given type

    :param struct i40e_pf \*pf:
        board private structure

    :param u8 type:
        VSI type

    :param u16 uplink_seid:
        the switch element to link to

    :param u32 param1:
        usage depends upon VSI type. For VF types, indicates VF id

.. _`i40e_vsi_setup.description`:

Description
-----------

This allocates the sw VSI structure and its queue resources, then add a VSI
to the identified VEB.

Returns pointer to the successfully allocated and configure VSI sw struct on
success, otherwise returns NULL on failure.

.. _`i40e_veb_get_bw_info`:

i40e_veb_get_bw_info
====================

.. c:function:: int i40e_veb_get_bw_info(struct i40e_veb *veb)

    Query VEB BW information

    :param struct i40e_veb \*veb:
        the veb to query

.. _`i40e_veb_get_bw_info.description`:

Description
-----------

Query the Tx scheduler BW configuration data for given VEB

.. _`i40e_veb_mem_alloc`:

i40e_veb_mem_alloc
==================

.. c:function:: int i40e_veb_mem_alloc(struct i40e_pf *pf)

    Allocates the next available struct veb in the PF

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_veb_mem_alloc.on-error`:

On error
--------

returns error code (negative)

.. _`i40e_veb_mem_alloc.on-success`:

On success
----------

returns vsi index in PF (positive)

.. _`i40e_switch_branch_release`:

i40e_switch_branch_release
==========================

.. c:function:: void i40e_switch_branch_release(struct i40e_veb *branch)

    Delete a branch of the switch tree

    :param struct i40e_veb \*branch:
        where to start deleting

.. _`i40e_switch_branch_release.description`:

Description
-----------

This uses recursion to find the tips of the branch to be
removed, deleting until we get back to and can delete this VEB.

.. _`i40e_veb_clear`:

i40e_veb_clear
==============

.. c:function:: void i40e_veb_clear(struct i40e_veb *veb)

    remove veb struct

    :param struct i40e_veb \*veb:
        the veb to remove

.. _`i40e_veb_release`:

i40e_veb_release
================

.. c:function:: void i40e_veb_release(struct i40e_veb *veb)

    Delete a VEB and free its resources

    :param struct i40e_veb \*veb:
        the VEB being removed

.. _`i40e_add_veb`:

i40e_add_veb
============

.. c:function:: int i40e_add_veb(struct i40e_veb *veb, struct i40e_vsi *vsi)

    create the VEB in the switch

    :param struct i40e_veb \*veb:
        the VEB to be instantiated

    :param struct i40e_vsi \*vsi:
        the controlling VSI

.. _`i40e_veb_setup`:

i40e_veb_setup
==============

.. c:function:: struct i40e_veb *i40e_veb_setup(struct i40e_pf *pf, u16 flags, u16 uplink_seid, u16 vsi_seid, u8 enabled_tc)

    Set up a VEB

    :param struct i40e_pf \*pf:
        board private structure

    :param u16 flags:
        VEB setup flags

    :param u16 uplink_seid:
        the switch element to link to

    :param u16 vsi_seid:
        the initial VSI seid

    :param u8 enabled_tc:
        Enabled TC bit-map

.. _`i40e_veb_setup.description`:

Description
-----------

This allocates the sw VEB structure and links it into the switch
It is possible and legal for this to be a duplicate of an already
existing VEB.  It is also possible for both uplink and vsi seids
to be zero, in order to create a floating VEB.

Returns pointer to the successfully allocated VEB sw struct on
success, otherwise returns NULL on failure.

.. _`i40e_setup_pf_switch_element`:

i40e_setup_pf_switch_element
============================

.. c:function:: void i40e_setup_pf_switch_element(struct i40e_pf *pf, struct i40e_aqc_switch_config_element_resp *ele, u16 num_reported, bool printconfig)

    set PF vars based on switch type

    :param struct i40e_pf \*pf:
        board private structure

    :param struct i40e_aqc_switch_config_element_resp \*ele:
        element we are building info from

    :param u16 num_reported:
        total number of elements

    :param bool printconfig:
        should we print the contents

.. _`i40e_setup_pf_switch_element.description`:

Description
-----------

helper function to assist in extracting a few useful SEID values.

.. _`i40e_fetch_switch_configuration`:

i40e_fetch_switch_configuration
===============================

.. c:function:: int i40e_fetch_switch_configuration(struct i40e_pf *pf, bool printconfig)

    Get switch config from firmware

    :param struct i40e_pf \*pf:
        board private structure

    :param bool printconfig:
        should we print the contents

.. _`i40e_fetch_switch_configuration.description`:

Description
-----------

Get the current switch configuration from the device and
extract a few useful SEID values.

.. _`i40e_setup_pf_switch`:

i40e_setup_pf_switch
====================

.. c:function:: int i40e_setup_pf_switch(struct i40e_pf *pf, bool reinit)

    Setup the HW switch on startup or after reset

    :param struct i40e_pf \*pf:
        board private structure

    :param bool reinit:
        if the Main VSI needs to re-initialized.

.. _`i40e_setup_pf_switch.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`i40e_determine_queue_usage`:

i40e_determine_queue_usage
==========================

.. c:function:: void i40e_determine_queue_usage(struct i40e_pf *pf)

    Work out queue distribution

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_setup_pf_filter_control`:

i40e_setup_pf_filter_control
============================

.. c:function:: int i40e_setup_pf_filter_control(struct i40e_pf *pf)

    Setup PF static filter control

    :param struct i40e_pf \*pf:
        PF to be setup

.. _`i40e_setup_pf_filter_control.description`:

Description
-----------

i40e_setup_pf_filter_control sets up a PF's initial filter control
settings. If PE/FCoE are enabled then it will also set the per PF
based filter sizes required for them. It also enables Flow director,
ethertype and macvlan type filter settings for the pf.

Returns 0 on success, negative on failure

.. _`i40e_get_platform_mac_addr`:

i40e_get_platform_mac_addr
==========================

.. c:function:: void i40e_get_platform_mac_addr(struct pci_dev *pdev, struct i40e_pf *pf)

    get platform-specific MAC address

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_get_platform_mac_addr.description`:

Description
-----------

Look up the MAC address in Open Firmware  on systems that support it,
and use IDPROM on SPARC if no OF address is found. On return, the
I40E_FLAG_PF_MAC will be wset in pf->flags if a platform-specific value
has been selected.

.. _`i40e_probe`:

i40e_probe
==========

.. c:function:: int i40e_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device initialization routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in i40e_pci_tbl

.. _`i40e_probe.description`:

Description
-----------

i40e_probe initializes a PF identified by a pci_dev structure.
The OS initialization, configuring of the PF private structure,
and a hardware reset occur.

Returns 0 on success, negative on failure

.. _`i40e_remove`:

i40e_remove
===========

.. c:function:: void i40e_remove(struct pci_dev *pdev)

    Device removal routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40e_remove.description`:

Description
-----------

i40e_remove is called by the PCI subsystem to alert the driver
that is should release a PCI device.  This could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`i40e_pci_error_detected`:

i40e_pci_error_detected
=======================

.. c:function:: pci_ers_result_t i40e_pci_error_detected(struct pci_dev *pdev, enum pci_channel_state error)

    warning that something funky happened in PCI land

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param enum pci_channel_state error:
        *undescribed*

.. _`i40e_pci_error_detected.description`:

Description
-----------

Called to warn that something happened and the error handling steps
are in progress.  Allows the driver to quiesce things, be ready for
remediation.

.. _`i40e_pci_error_slot_reset`:

i40e_pci_error_slot_reset
=========================

.. c:function:: pci_ers_result_t i40e_pci_error_slot_reset(struct pci_dev *pdev)

    a PCI slot reset just happened

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40e_pci_error_slot_reset.description`:

Description
-----------

Called to find if the driver can work with the device now that
the pci slot has been reset.  If a basic connection seems good
(registers are readable and have sane content) then return a
happy little PCI_ERS_RESULT_xxx.

.. _`i40e_pci_error_resume`:

i40e_pci_error_resume
=====================

.. c:function:: void i40e_pci_error_resume(struct pci_dev *pdev)

    restart operations after PCI error recovery

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40e_pci_error_resume.description`:

Description
-----------

Called to allow the driver to bring things back up after PCI error
and/or reset recovery has finished.

.. _`i40e_shutdown`:

i40e_shutdown
=============

.. c:function:: void i40e_shutdown(struct pci_dev *pdev)

    PCI callback for shutting down

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40e_suspend`:

i40e_suspend
============

.. c:function:: int i40e_suspend(struct pci_dev *pdev, pm_message_t state)

    PCI callback for moving to D3

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param pm_message_t state:
        *undescribed*

.. _`i40e_resume`:

i40e_resume
===========

.. c:function:: int i40e_resume(struct pci_dev *pdev)

    PCI callback for waking up from D3

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`i40e_init_module`:

i40e_init_module
================

.. c:function:: int i40e_init_module( void)

    Driver registration routine

    :param  void:
        no arguments

.. _`i40e_init_module.description`:

Description
-----------

i40e_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`i40e_exit_module`:

i40e_exit_module
================

.. c:function:: void __exit i40e_exit_module( void)

    Driver exit cleanup routine

    :param  void:
        no arguments

.. _`i40e_exit_module.description`:

Description
-----------

i40e_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.
