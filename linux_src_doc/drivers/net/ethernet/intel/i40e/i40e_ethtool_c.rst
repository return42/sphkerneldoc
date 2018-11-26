.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_ethtool.c

.. _`i40e_stats`:

struct i40e_stats
=================

.. c:type:: struct i40e_stats

    definition for an ethtool statistic

.. _`i40e_stats.definition`:

Definition
----------

.. code-block:: c

    struct i40e_stats {
        char stat_string[ETH_GSTRING_LEN];
        int sizeof_stat;
        int stat_offset;
    }

.. _`i40e_stats.members`:

Members
-------

stat_string
    statistic name to display in ethtool -S output

sizeof_stat
    the \ :c:func:`sizeof`\  the stat, must be no greater than sizeof(u64)

stat_offset
    \ :c:func:`offsetof`\  the stat from a base pointer

.. _`i40e_stats.description`:

Description
-----------

This structure defines a statistic to be added to the ethtool stats buffer.
It defines a statistic as offset from a common base pointer. Stats should
be defined in constant arrays using the I40E_STAT macro, with every element
of the array using the same \_type for calculating the sizeof_stat and
stat_offset.

The \ ``sizeof_stat``\  is expected to be sizeof(u8), sizeof(u16), sizeof(u32) or
sizeof(u64). Other sizes are not expected and will produce a WARN_ONCE from
the \ :c:func:`i40e_add_ethtool_stat`\  helper function.

The \ ``stat_string``\  is interpreted as a format string, allowing formatted
values to be inserted while looping over multiple structures for a given
statistics array. Thus, every statistic string in an array should have the
same type and number of format specifiers, to be formatted by variadic
arguments to the \ :c:func:`i40e_add_stat_string`\  helper function.

.. _`i40e_add_one_ethtool_stat`:

i40e_add_one_ethtool_stat
=========================

.. c:function:: void i40e_add_one_ethtool_stat(u64 *data, void *pointer, const struct i40e_stats *stat)

    copy the stat into the supplied buffer

    :param data:
        location to store the stat value
    :type data: u64 \*

    :param pointer:
        basis for where to copy from
    :type pointer: void \*

    :param stat:
        the stat definition
    :type stat: const struct i40e_stats \*

.. _`i40e_add_one_ethtool_stat.description`:

Description
-----------

Copies the stat data defined by the pointer and stat structure pair into
the memory supplied as data. Used to implement i40e_add_ethtool_stats and
i40e_add_queue_stats. If the pointer is null, data will be zero'd.

.. _`__i40e_add_ethtool_stats`:

\__i40e_add_ethtool_stats
=========================

.. c:function:: void __i40e_add_ethtool_stats(u64 **data, void *pointer, const struct i40e_stats stats, const unsigned int size)

    copy stats into the ethtool supplied buffer

    :param data:
        ethtool stats buffer
    :type data: u64 \*\*

    :param pointer:
        location to copy stats from
    :type pointer: void \*

    :param stats:
        array of stats to copy
    :type stats: const struct i40e_stats

    :param size:
        the size of the stats definition
    :type size: const unsigned int

.. _`__i40e_add_ethtool_stats.description`:

Description
-----------

Copy the stats defined by the stats array using the pointer as a base into
the data buffer supplied by ethtool. Updates the data pointer to point to
the next empty location for successive calls to \__i40e_add_ethtool_stats.
If pointer is null, set the data values to zero and update the pointer to
skip these stats.

.. _`i40e_add_ethtool_stats`:

i40e_add_ethtool_stats
======================

.. c:function::  i40e_add_ethtool_stats( data,  pointer,  stats)

    copy stats into ethtool supplied buffer

    :param data:
        ethtool stats buffer
    :type data: 

    :param pointer:
        location where stats are stored
    :type pointer: 

    :param stats:
        static const array of stat definitions
    :type stats: 

.. _`i40e_add_ethtool_stats.description`:

Description
-----------

Macro to ease the use of \__i40e_add_ethtool_stats by taking a static
constant stats array and passing the \ :c:func:`ARRAY_SIZE`\ . This avoids typos by
ensuring that we pass the size associated with the given stats array.

The parameter \ ``stats``\  is evaluated twice, so parameters with side effects
should be avoided.

.. _`i40e_add_queue_stats`:

i40e_add_queue_stats
====================

.. c:function:: void i40e_add_queue_stats(u64 **data, struct i40e_ring *ring)

    copy queue statistics into supplied buffer

    :param data:
        ethtool stats buffer
    :type data: u64 \*\*

    :param ring:
        the ring to copy
    :type ring: struct i40e_ring \*

.. _`i40e_add_queue_stats.description`:

Description
-----------

Queue statistics must be copied while protected by
u64_stats_fetch_begin_irq, so we can't directly use i40e_add_ethtool_stats.
Assumes that queue stats are defined in i40e_gstrings_queue_stats. If the
ring pointer is null, zero out the queue stat values and update the data
pointer. Otherwise safely copy the stats from the ring into the supplied
buffer and update the data pointer when finished.

This function expects to be called while under \ :c:func:`rcu_read_lock`\ .

.. _`__i40e_add_stat_strings`:

\__i40e_add_stat_strings
========================

.. c:function:: void __i40e_add_stat_strings(u8 **p, const struct i40e_stats stats, const unsigned int size,  ...)

    copy stat strings into ethtool buffer

    :param p:
        ethtool supplied buffer
    :type p: u8 \*\*

    :param stats:
        stat definitions array
    :type stats: const struct i40e_stats

    :param size:
        size of the stats array
    :type size: const unsigned int

    :param ellipsis ellipsis:
        variable arguments

.. _`__i40e_add_stat_strings.description`:

Description
-----------

Format and copy the strings described by stats into the buffer pointed at
by p.

.. _`i40e_add_stat_strings`:

i40e_add_stat_strings
=====================

.. c:function::  i40e_add_stat_strings( p,  stats,  ...)

    copy stat strings into ethtool buffer

    :param p:
        ethtool supplied buffer
    :type p: 

    :param stats:
        stat definitions array
    :type stats: 

    :param ellipsis ellipsis:
        variable arguments

.. _`i40e_add_stat_strings.description`:

Description
-----------

Format and copy the strings described by the const static stats value into
the buffer pointed at by p.

The parameter \ ``stats``\  is evaluated twice, so parameters with side effects
should be avoided. Additionally, stats must be an array such that
ARRAY_SIZE can be called on it.

.. _`i40e_partition_setting_complaint`:

i40e_partition_setting_complaint
================================

.. c:function:: void i40e_partition_setting_complaint(struct i40e_pf *pf)

    generic complaint for MFP restriction

    :param pf:
        the PF struct
    :type pf: struct i40e_pf \*

.. _`i40e_phy_type_to_ethtool`:

i40e_phy_type_to_ethtool
========================

.. c:function:: void i40e_phy_type_to_ethtool(struct i40e_pf *pf, struct ethtool_link_ksettings *ks)

    convert the phy_types to ethtool link modes

    :param pf:
        PF struct with phy_types
    :type pf: struct i40e_pf \*

    :param ks:
        ethtool link ksettings struct to fill out
    :type ks: struct ethtool_link_ksettings \*

.. _`i40e_get_settings_link_up`:

i40e_get_settings_link_up
=========================

.. c:function:: void i40e_get_settings_link_up(struct i40e_hw *hw, struct ethtool_link_ksettings *ks, struct net_device *netdev, struct i40e_pf *pf)

    Get the Link settings for when link is up

    :param hw:
        hw structure
    :type hw: struct i40e_hw \*

    :param ks:
        ethtool ksettings to fill in
    :type ks: struct ethtool_link_ksettings \*

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param pf:
        pointer to physical function struct
    :type pf: struct i40e_pf \*

.. _`i40e_get_settings_link_down`:

i40e_get_settings_link_down
===========================

.. c:function:: void i40e_get_settings_link_down(struct i40e_hw *hw, struct ethtool_link_ksettings *ks, struct i40e_pf *pf)

    Get the Link settings for when link is down

    :param hw:
        hw structure
    :type hw: struct i40e_hw \*

    :param ks:
        ethtool ksettings to fill in
    :type ks: struct ethtool_link_ksettings \*

    :param pf:
        pointer to physical function struct
    :type pf: struct i40e_pf \*

.. _`i40e_get_settings_link_down.description`:

Description
-----------

Reports link settings that can be determined when link is down

.. _`i40e_get_link_ksettings`:

i40e_get_link_ksettings
=======================

.. c:function:: int i40e_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *ks)

    Get Link Speed and Duplex settings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ks:
        ethtool ksettings
    :type ks: struct ethtool_link_ksettings \*

.. _`i40e_get_link_ksettings.description`:

Description
-----------

Reports speed/duplex settings based on media_type

.. _`i40e_set_link_ksettings`:

i40e_set_link_ksettings
=======================

.. c:function:: int i40e_set_link_ksettings(struct net_device *netdev, const struct ethtool_link_ksettings *ks)

    Set Speed and Duplex

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ks:
        ethtool ksettings
    :type ks: const struct ethtool_link_ksettings \*

.. _`i40e_set_link_ksettings.description`:

Description
-----------

Set speed/duplex per media_types advertised/forced

.. _`i40e_get_pauseparam`:

i40e_get_pauseparam
===================

.. c:function:: void i40e_get_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Get Flow Control status

    :param netdev:
        netdevice structure
    :type netdev: struct net_device \*

    :param pause:
        buffer to return pause parameters
    :type pause: struct ethtool_pauseparam \*

.. _`i40e_get_pauseparam.description`:

Description
-----------

Return tx/rx-pause status

.. _`i40e_set_pauseparam`:

i40e_set_pauseparam
===================

.. c:function:: int i40e_set_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Set Flow Control parameter

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param pause:
        return tx/rx flow control status
    :type pause: struct ethtool_pauseparam \*

.. _`i40e_get_stats_count`:

i40e_get_stats_count
====================

.. c:function:: int i40e_get_stats_count(struct net_device *netdev)

    return the stats count for a device

    :param netdev:
        the netdev to return the count for
    :type netdev: struct net_device \*

.. _`i40e_get_stats_count.description`:

Description
-----------

Returns the total number of statistics for this netdev. Note that even
though this is a function, it is required that the count for a specific
netdev must never change. Basing the count on static values such as the
maximum number of queues or the device type is ok. However, the API for
obtaining stats is \*not\* safe against changes based on non-static
values such as the \*current\* number of queues, or runtime flags.

If a statistic is not always enabled, return it as part of the count
anyways, always return its string, and report its value as zero.

.. _`i40e_get_pfc_stats`:

i40e_get_pfc_stats
==================

.. c:function:: struct i40e_pfc_stats i40e_get_pfc_stats(struct i40e_pf *pf, unsigned int i)

    copy HW PFC statistics to formatted structure

    :param pf:
        the PF device structure
    :type pf: struct i40e_pf \*

    :param i:
        the priority value to copy
    :type i: unsigned int

.. _`i40e_get_pfc_stats.description`:

Description
-----------

The PFC stats are found as arrays in pf->stats, which is not easy to pass
into i40e_add_ethtool_stats. Produce a formatted i40e_pfc_stats structure
of the PFC stats for the given priority.

.. _`i40e_get_ethtool_stats`:

i40e_get_ethtool_stats
======================

.. c:function:: void i40e_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *stats, u64 *data)

    copy stat values into supplied buffer

    :param netdev:
        the netdev to collect stats for
    :type netdev: struct net_device \*

    :param stats:
        ethtool stats command structure
    :type stats: struct ethtool_stats \*

    :param data:
        ethtool supplied buffer
    :type data: u64 \*

.. _`i40e_get_ethtool_stats.description`:

Description
-----------

Copy the stats values for this netdev into the buffer. Expects data to be
pre-allocated to the size returned by i40e_get_stats_count.. Note that all
statistics must be copied in a static order, and the count must not change
for a given netdev. See i40e_get_stats_count for more details.

If a statistic is not currently valid (such as a disabled queue), this
function reports its value as zero.

.. _`i40e_get_stat_strings`:

i40e_get_stat_strings
=====================

.. c:function:: void i40e_get_stat_strings(struct net_device *netdev, u8 *data)

    copy stat strings into supplied buffer

    :param netdev:
        the netdev to collect strings for
    :type netdev: struct net_device \*

    :param data:
        supplied buffer to copy strings into
    :type data: u8 \*

.. _`i40e_get_stat_strings.description`:

Description
-----------

Copy the strings related to stats for this netdev. Expects data to be
pre-allocated with the size reported by i40e_get_stats_count. Note that the
strings must be copied in a static order and the total count must not
change for a given netdev. See i40e_get_stats_count for more details.

.. _`i40e_set_wol`:

i40e_set_wol
============

.. c:function:: int i40e_set_wol(struct net_device *netdev, struct ethtool_wolinfo *wol)

    set the WakeOnLAN configuration

    :param netdev:
        the netdev in question
    :type netdev: struct net_device \*

    :param wol:
        the ethtool WoL setting data
    :type wol: struct ethtool_wolinfo \*

.. _`__i40e_get_coalesce`:

\__i40e_get_coalesce
====================

.. c:function:: int __i40e_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec, int queue)

    get per-queue coalesce settings

    :param netdev:
        the netdev to check
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce data structure
    :type ec: struct ethtool_coalesce \*

    :param queue:
        which queue to pick
    :type queue: int

.. _`__i40e_get_coalesce.description`:

Description
-----------

Gets the per-queue settings for coalescence. Specifically Rx and Tx usecs
are per queue. If queue is <0 then we default to queue 0 as the
representative value.

.. _`i40e_get_coalesce`:

i40e_get_coalesce
=================

.. c:function:: int i40e_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    get a netdev's coalesce settings

    :param netdev:
        the netdev to check
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce data structure
    :type ec: struct ethtool_coalesce \*

.. _`i40e_get_coalesce.description`:

Description
-----------

Gets the coalesce settings for a particular netdev. Note that if user has
modified per-queue settings, this only guarantees to represent queue 0. See
\__i40e_get_coalesce for more details.

.. _`i40e_get_per_queue_coalesce`:

i40e_get_per_queue_coalesce
===========================

.. c:function:: int i40e_get_per_queue_coalesce(struct net_device *netdev, u32 queue, struct ethtool_coalesce *ec)

    gets coalesce settings for particular queue

    :param netdev:
        netdev structure
    :type netdev: struct net_device \*

    :param queue:
        the particular queue to read
    :type queue: u32

    :param ec:
        ethtool's coalesce settings
    :type ec: struct ethtool_coalesce \*

.. _`i40e_get_per_queue_coalesce.description`:

Description
-----------

Will read a specific queue's coalesce settings

.. _`i40e_set_itr_per_queue`:

i40e_set_itr_per_queue
======================

.. c:function:: void i40e_set_itr_per_queue(struct i40e_vsi *vsi, struct ethtool_coalesce *ec, int queue)

    set ITR values for specific queue

    :param vsi:
        the VSI to set values for
    :type vsi: struct i40e_vsi \*

    :param ec:
        coalesce settings from ethtool
    :type ec: struct ethtool_coalesce \*

    :param queue:
        the queue to modify
    :type queue: int

.. _`i40e_set_itr_per_queue.description`:

Description
-----------

Change the ITR settings for a specific queue.

.. _`__i40e_set_coalesce`:

\__i40e_set_coalesce
====================

.. c:function:: int __i40e_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec, int queue)

    set coalesce settings for particular queue

    :param netdev:
        the netdev to change
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce settings
    :type ec: struct ethtool_coalesce \*

    :param queue:
        the queue to change
    :type queue: int

.. _`__i40e_set_coalesce.description`:

Description
-----------

Sets the coalesce settings for a particular queue.

.. _`i40e_set_coalesce`:

i40e_set_coalesce
=================

.. c:function:: int i40e_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    set coalesce settings for every queue on the netdev

    :param netdev:
        the netdev to change
    :type netdev: struct net_device \*

    :param ec:
        ethtool coalesce settings
    :type ec: struct ethtool_coalesce \*

.. _`i40e_set_coalesce.description`:

Description
-----------

This will set each queue to the same coalesce settings.

.. _`i40e_set_per_queue_coalesce`:

i40e_set_per_queue_coalesce
===========================

.. c:function:: int i40e_set_per_queue_coalesce(struct net_device *netdev, u32 queue, struct ethtool_coalesce *ec)

    set specific queue's coalesce settings

    :param netdev:
        the netdev to change
    :type netdev: struct net_device \*

    :param queue:
        the queue to change
    :type queue: u32

    :param ec:
        ethtool's coalesce settings
    :type ec: struct ethtool_coalesce \*

.. _`i40e_set_per_queue_coalesce.description`:

Description
-----------

Sets the specified queue's coalesce settings.

.. _`i40e_get_rss_hash_opts`:

i40e_get_rss_hash_opts
======================

.. c:function:: int i40e_get_rss_hash_opts(struct i40e_pf *pf, struct ethtool_rxnfc *cmd)

    Get RSS hash Input Set for each flow type

    :param pf:
        pointer to the physical function struct
    :type pf: struct i40e_pf \*

    :param cmd:
        ethtool rxnfc command
    :type cmd: struct ethtool_rxnfc \*

.. _`i40e_get_rss_hash_opts.description`:

Description
-----------

Returns Success if the flow is supported, else Invalid Input.

.. _`i40e_check_mask`:

i40e_check_mask
===============

.. c:function:: int i40e_check_mask(u64 mask, u64 field)

    Check whether a mask field is set

    :param mask:
        the full mask value
    :type mask: u64

    :param field:
        mask of the field to check
    :type field: u64

.. _`i40e_check_mask.description`:

Description
-----------

If the given mask is fully set, return positive value. If the mask for the
field is fully unset, return zero. Otherwise return a negative error code.

.. _`i40e_parse_rx_flow_user_data`:

i40e_parse_rx_flow_user_data
============================

.. c:function:: int i40e_parse_rx_flow_user_data(struct ethtool_rx_flow_spec *fsp, struct i40e_rx_flow_userdef *data)

    Deconstruct user-defined data

    :param fsp:
        pointer to rx flow specification
    :type fsp: struct ethtool_rx_flow_spec \*

    :param data:
        pointer to userdef data structure for storage
    :type data: struct i40e_rx_flow_userdef \*

.. _`i40e_parse_rx_flow_user_data.description`:

Description
-----------

Read the user-defined data and deconstruct the value into a structure. No
other code should read the user-defined data, so as to ensure that every
place consistently reads the value correctly.

The user-defined field is a 64bit Big Endian format value, which we
deconstruct by reading bits or bit fields from it. Single bit flags shall
be defined starting from the highest bits, while small bit field values
shall be defined starting from the lowest bits.

Returns 0 if the data is valid, and non-zero if the userdef data is invalid
and the filter should be rejected. The data structure will always be
modified even if FLOW_EXT is not set.

.. _`i40e_fill_rx_flow_user_data`:

i40e_fill_rx_flow_user_data
===========================

.. c:function:: void i40e_fill_rx_flow_user_data(struct ethtool_rx_flow_spec *fsp, struct i40e_rx_flow_userdef *data)

    Fill in user-defined data field

    :param fsp:
        pointer to rx_flow specification
    :type fsp: struct ethtool_rx_flow_spec \*

    :param data:
        pointer to return userdef data
    :type data: struct i40e_rx_flow_userdef \*

.. _`i40e_fill_rx_flow_user_data.description`:

Description
-----------

Reads the userdef data structure and properly fills in the user defined
fields of the rx_flow_spec.

.. _`i40e_get_ethtool_fdir_all`:

i40e_get_ethtool_fdir_all
=========================

.. c:function:: int i40e_get_ethtool_fdir_all(struct i40e_pf *pf, struct ethtool_rxnfc *cmd, u32 *rule_locs)

    Populates the rule count of a command

    :param pf:
        Pointer to the physical function struct
    :type pf: struct i40e_pf \*

    :param cmd:
        The command to get or set Rx flow classification rules
    :type cmd: struct ethtool_rxnfc \*

    :param rule_locs:
        Array of used rule locations
    :type rule_locs: u32 \*

.. _`i40e_get_ethtool_fdir_all.description`:

Description
-----------

This function populates both the total and actual rule count of
the ethtool flow classification command

Returns 0 on success or -EMSGSIZE if entry not found

.. _`i40e_get_ethtool_fdir_entry`:

i40e_get_ethtool_fdir_entry
===========================

.. c:function:: int i40e_get_ethtool_fdir_entry(struct i40e_pf *pf, struct ethtool_rxnfc *cmd)

    Look up a filter based on Rx flow

    :param pf:
        Pointer to the physical function struct
    :type pf: struct i40e_pf \*

    :param cmd:
        The command to get or set Rx flow classification rules
    :type cmd: struct ethtool_rxnfc \*

.. _`i40e_get_ethtool_fdir_entry.description`:

Description
-----------

This function looks up a filter based on the Rx flow classification
command and fills the flow spec info for it if found

Returns 0 on success or -EINVAL if filter not found

.. _`i40e_get_rxnfc`:

i40e_get_rxnfc
==============

.. c:function:: int i40e_get_rxnfc(struct net_device *netdev, struct ethtool_rxnfc *cmd, u32 *rule_locs)

    command to get RX flow classification rules

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param cmd:
        ethtool rxnfc command
    :type cmd: struct ethtool_rxnfc \*

    :param rule_locs:
        pointer to store rule data
    :type rule_locs: u32 \*

.. _`i40e_get_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`i40e_get_rss_hash_bits`:

i40e_get_rss_hash_bits
======================

.. c:function:: u64 i40e_get_rss_hash_bits(struct ethtool_rxnfc *nfc, u64 i_setc)

    Read RSS Hash bits from register

    :param nfc:
        pointer to user request
    :type nfc: struct ethtool_rxnfc \*

    :param i_setc:
        bits currently set
    :type i_setc: u64

.. _`i40e_get_rss_hash_bits.description`:

Description
-----------

Returns value of bits to be set per user request

.. _`i40e_set_rss_hash_opt`:

i40e_set_rss_hash_opt
=====================

.. c:function:: int i40e_set_rss_hash_opt(struct i40e_pf *pf, struct ethtool_rxnfc *nfc)

    Enable/Disable flow types for RSS hash

    :param pf:
        pointer to the physical function struct
    :type pf: struct i40e_pf \*

    :param nfc:
        ethtool rxnfc command
    :type nfc: struct ethtool_rxnfc \*

.. _`i40e_set_rss_hash_opt.description`:

Description
-----------

Returns Success if the flow input set is supported.

.. _`i40e_update_ethtool_fdir_entry`:

i40e_update_ethtool_fdir_entry
==============================

.. c:function:: int i40e_update_ethtool_fdir_entry(struct i40e_vsi *vsi, struct i40e_fdir_filter *input, u16 sw_idx, struct ethtool_rxnfc *cmd)

    Updates the fdir filter entry

    :param vsi:
        Pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param input:
        The filter to update or NULL to indicate deletion
    :type input: struct i40e_fdir_filter \*

    :param sw_idx:
        Software index to the filter
    :type sw_idx: u16

    :param cmd:
        The command to get or set Rx flow classification rules
    :type cmd: struct ethtool_rxnfc \*

.. _`i40e_update_ethtool_fdir_entry.description`:

Description
-----------

This function updates (or deletes) a Flow Director entry from
the hlist of the corresponding PF

Returns 0 on success

.. _`i40e_prune_flex_pit_list`:

i40e_prune_flex_pit_list
========================

.. c:function:: void i40e_prune_flex_pit_list(struct i40e_pf *pf)

    Cleanup unused entries in FLX_PIT table

    :param pf:
        pointer to PF structure
    :type pf: struct i40e_pf \*

.. _`i40e_prune_flex_pit_list.description`:

Description
-----------

This function searches the list of filters and determines which FLX_PIT
entries are still required. It will prune any entries which are no longer
in use after the deletion.

.. _`i40e_del_fdir_entry`:

i40e_del_fdir_entry
===================

.. c:function:: int i40e_del_fdir_entry(struct i40e_vsi *vsi, struct ethtool_rxnfc *cmd)

    Deletes a Flow Director filter entry

    :param vsi:
        Pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param cmd:
        The command to get or set Rx flow classification rules
    :type cmd: struct ethtool_rxnfc \*

.. _`i40e_del_fdir_entry.description`:

Description
-----------

The function removes a Flow Director filter entry from the
hlist of the corresponding PF

Returns 0 on success

.. _`i40e_unused_pit_index`:

i40e_unused_pit_index
=====================

.. c:function:: u8 i40e_unused_pit_index(struct i40e_pf *pf)

    Find an unused PIT index for given list

    :param pf:
        the PF data structure
    :type pf: struct i40e_pf \*

.. _`i40e_unused_pit_index.description`:

Description
-----------

Find the first unused flexible PIT index entry. We search both the L3 and
L4 flexible PIT lists so that the returned index is unique and unused by
either currently programmed L3 or L4 filters. We use a bit field as storage
to track which indexes are already used.

.. _`i40e_find_flex_offset`:

i40e_find_flex_offset
=====================

.. c:function:: struct i40e_flex_pit *i40e_find_flex_offset(struct list_head *flex_pit_list, u16 src_offset)

    Find an existing flex src_offset

    :param flex_pit_list:
        L3 or L4 flex PIT list
    :type flex_pit_list: struct list_head \*

    :param src_offset:
        new src_offset to find
    :type src_offset: u16

.. _`i40e_find_flex_offset.description`:

Description
-----------

Searches the flex_pit_list for an existing offset. If no offset is
currently programmed, then this will return an ERR_PTR if there is no space
to add a new offset, otherwise it returns NULL.

.. _`i40e_add_flex_offset`:

i40e_add_flex_offset
====================

.. c:function:: int i40e_add_flex_offset(struct list_head *flex_pit_list, u16 src_offset, u8 pit_index)

    Add src_offset to flex PIT table list

    :param flex_pit_list:
        L3 or L4 flex PIT list
    :type flex_pit_list: struct list_head \*

    :param src_offset:
        new src_offset to add
    :type src_offset: u16

    :param pit_index:
        the PIT index to program
    :type pit_index: u8

.. _`i40e_add_flex_offset.description`:

Description
-----------

This function programs the new src_offset to the list. It is expected that
i40e_find_flex_offset has already been tried and returned NULL, indicating
that this offset is not programmed, and that the list has enough space to
store another offset.

Returns 0 on success, and negative value on error.

.. _`__i40e_reprogram_flex_pit`:

\__i40e_reprogram_flex_pit
==========================

.. c:function:: void __i40e_reprogram_flex_pit(struct i40e_pf *pf, struct list_head *flex_pit_list, int flex_pit_start)

    Re-program specific FLX_PIT table

    :param pf:
        Pointer to the PF structure
    :type pf: struct i40e_pf \*

    :param flex_pit_list:
        list of flexible src offsets in use
    :type flex_pit_list: struct list_head \*

    :param flex_pit_start:
        index to first entry for this section of the table
    :type flex_pit_start: int

.. _`__i40e_reprogram_flex_pit.description`:

Description
-----------

In order to handle flexible data, the hardware uses a table of values
called the FLX_PIT table. This table is used to indicate which sections of
the input correspond to what PIT index values. Unfortunately, hardware is
very restrictive about programming this table. Entries must be ordered by
src_offset in ascending order, without duplicates. Additionally, unused
entries must be set to the unused index value, and must have valid size and
length according to the src_offset ordering.

This function will reprogram the FLX_PIT register from a book-keeping
structure that we guarantee is already ordered correctly, and has no more
than 3 entries.

To make things easier, we only support flexible values of one word length,
rather than allowing variable length flexible values.

.. _`i40e_reprogram_flex_pit`:

i40e_reprogram_flex_pit
=======================

.. c:function:: void i40e_reprogram_flex_pit(struct i40e_pf *pf)

    Reprogram all FLX_PIT tables after input set change

    :param pf:
        pointer to the PF structure
    :type pf: struct i40e_pf \*

.. _`i40e_reprogram_flex_pit.description`:

Description
-----------

This function reprograms both the L3 and L4 FLX_PIT tables. See the
internal helper function for implementation details.

.. _`i40e_flow_str`:

i40e_flow_str
=============

.. c:function:: const char *i40e_flow_str(struct ethtool_rx_flow_spec *fsp)

    Converts a flow_type into a human readable string

    :param fsp:
        the flow specification
    :type fsp: struct ethtool_rx_flow_spec \*

.. _`i40e_flow_str.description`:

Description
-----------

Currently only flow types we support are included here, and the string
value attempts to match what ethtool would use to configure this flow type.

.. _`i40e_pit_index_to_mask`:

i40e_pit_index_to_mask
======================

.. c:function:: u64 i40e_pit_index_to_mask(int pit_index)

    Return the FLEX mask for a given PIT index

    :param pit_index:
        PIT index to convert
    :type pit_index: int

.. _`i40e_pit_index_to_mask.description`:

Description
-----------

Returns the mask for a given PIT index. Will return 0 if the pit_index is
of range.

.. _`i40e_print_input_set`:

i40e_print_input_set
====================

.. c:function:: void i40e_print_input_set(struct i40e_vsi *vsi, u64 old, u64 new)

    Show changes between two input sets

    :param vsi:
        the vsi being configured
    :type vsi: struct i40e_vsi \*

    :param old:
        the old input set
    :type old: u64

    :param new:
        the new input set
    :type new: u64

.. _`i40e_print_input_set.description`:

Description
-----------

Print the difference between old and new input sets by showing which series
of words are toggled on or off. Only displays the bits we actually support
changing.

.. _`i40e_check_fdir_input_set`:

i40e_check_fdir_input_set
=========================

.. c:function:: int i40e_check_fdir_input_set(struct i40e_vsi *vsi, struct ethtool_rx_flow_spec *fsp, struct i40e_rx_flow_userdef *userdef)

    Check that a given rx_flow_spec mask is valid

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param fsp:
        pointer to Rx flow specification
    :type fsp: struct ethtool_rx_flow_spec \*

    :param userdef:
        userdefined data from flow specification
    :type userdef: struct i40e_rx_flow_userdef \*

.. _`i40e_check_fdir_input_set.description`:

Description
-----------

Ensures that a given ethtool_rx_flow_spec has a valid mask. Some support
for partial matches exists with a few limitations. First, hardware only
supports masking by word boundary (2 bytes) and not per individual bit.
Second, hardware is limited to using one mask for a flow type and cannot
use a separate mask for each filter.

To support these limitations, if we already have a configured filter for
the specified type, this function enforces that new filters of the type
match the configured input set. Otherwise, if we do not have a filter of
the specified type, we allow the input set to be updated to match the
desired filter.

To help ensure that administrators understand why filters weren't displayed
as supported, we print a diagnostic message displaying how the input set
would change and warning to delete the preexisting filters if required.

Returns 0 on successful input set match, and a negative return code on
failure.

.. _`i40e_match_fdir_filter`:

i40e_match_fdir_filter
======================

.. c:function:: bool i40e_match_fdir_filter(struct i40e_fdir_filter *a, struct i40e_fdir_filter *b)

    Return true of two filters match

    :param a:
        pointer to filter struct
    :type a: struct i40e_fdir_filter \*

    :param b:
        pointer to filter struct
    :type b: struct i40e_fdir_filter \*

.. _`i40e_match_fdir_filter.description`:

Description
-----------

Returns true if the two filters match exactly the same criteria. I.e. they
match the same flow type and have the same parameters. We don't need to
check any input-set since all filters of the same flow type must use the
same input set.

.. _`i40e_disallow_matching_filters`:

i40e_disallow_matching_filters
==============================

.. c:function:: int i40e_disallow_matching_filters(struct i40e_vsi *vsi, struct i40e_fdir_filter *input)

    Check that new filters differ

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param input:
        new filter to check
    :type input: struct i40e_fdir_filter \*

.. _`i40e_disallow_matching_filters.description`:

Description
-----------

Due to hardware limitations, it is not possible for two filters that match
similar criteria to be programmed at the same time. This is true for a few

.. _`i40e_disallow_matching_filters.reasons`:

reasons
-------


(a) all filters matching a particular flow type must use the same input
set, that is they must match the same criteria.
(b) different flow types will never match the same packet, as the flow type
is decided by hardware before checking which rules apply.
(c) hardware has no way to distinguish which order filters apply in.

Due to this, we can't really support using the location data to order
filters in the hardware parsing. It is technically possible for the user to
request two filters matching the same criteria but which select different
queues. In this case, rather than keep both filters in the list, we reject
the 2nd filter when the user requests adding it.

This avoids needing to track location for programming the filter to
hardware, and ensures that we avoid some strange scenarios involving
deleting filters which match the same criteria.

.. _`i40e_add_fdir_ethtool`:

i40e_add_fdir_ethtool
=====================

.. c:function:: int i40e_add_fdir_ethtool(struct i40e_vsi *vsi, struct ethtool_rxnfc *cmd)

    Add/Remove Flow Director filters

    :param vsi:
        pointer to the targeted VSI
    :type vsi: struct i40e_vsi \*

    :param cmd:
        command to get or set RX flow classification rules
    :type cmd: struct ethtool_rxnfc \*

.. _`i40e_add_fdir_ethtool.description`:

Description
-----------

Add Flow Director filters for a specific flow spec based on their
protocol.  Returns 0 if the filters were successfully added.

.. _`i40e_set_rxnfc`:

i40e_set_rxnfc
==============

.. c:function:: int i40e_set_rxnfc(struct net_device *netdev, struct ethtool_rxnfc *cmd)

    command to set RX flow classification rules

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param cmd:
        ethtool rxnfc command
    :type cmd: struct ethtool_rxnfc \*

.. _`i40e_set_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`i40e_max_channels`:

i40e_max_channels
=================

.. c:function:: unsigned int i40e_max_channels(struct i40e_vsi *vsi)

    get Max number of combined channels supported

    :param vsi:
        vsi pointer
    :type vsi: struct i40e_vsi \*

.. _`i40e_get_channels`:

i40e_get_channels
=================

.. c:function:: void i40e_get_channels(struct net_device *dev, struct ethtool_channels *ch)

    Get the current channels enabled and max supported etc.

    :param dev:
        network interface device structure
    :type dev: struct net_device \*

    :param ch:
        ethtool channels structure
    :type ch: struct ethtool_channels \*

.. _`i40e_get_channels.description`:

Description
-----------

We don't support separate tx and rx queues as channels. The other count
represents how many queues are being used for control. max_combined counts
how many queue pairs we can support. They may not be mapped 1 to 1 with
q_vectors since we support a lot more queue pairs than q_vectors.

.. _`i40e_set_channels`:

i40e_set_channels
=================

.. c:function:: int i40e_set_channels(struct net_device *dev, struct ethtool_channels *ch)

    Set the new channels count.

    :param dev:
        network interface device structure
    :type dev: struct net_device \*

    :param ch:
        ethtool channels structure
    :type ch: struct ethtool_channels \*

.. _`i40e_set_channels.description`:

Description
-----------

The new channels count may not be the same as requested by the user
since it gets rounded down to a power of 2 value.

.. _`i40e_get_rxfh_key_size`:

i40e_get_rxfh_key_size
======================

.. c:function:: u32 i40e_get_rxfh_key_size(struct net_device *netdev)

    get the RSS hash key size

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`i40e_get_rxfh_key_size.description`:

Description
-----------

Returns the table size.

.. _`i40e_get_rxfh_indir_size`:

i40e_get_rxfh_indir_size
========================

.. c:function:: u32 i40e_get_rxfh_indir_size(struct net_device *netdev)

    get the rx flow hash indirection table size

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`i40e_get_rxfh_indir_size.description`:

Description
-----------

Returns the table size.

.. _`i40e_get_rxfh`:

i40e_get_rxfh
=============

.. c:function:: int i40e_get_rxfh(struct net_device *netdev, u32 *indir, u8 *key, u8 *hfunc)

    get the rx flow hash indirection table

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param indir:
        indirection table
    :type indir: u32 \*

    :param key:
        hash key
    :type key: u8 \*

    :param hfunc:
        hash function
    :type hfunc: u8 \*

.. _`i40e_get_rxfh.description`:

Description
-----------

Reads the indirection table directly from the hardware. Returns 0 on
success.

.. _`i40e_set_rxfh`:

i40e_set_rxfh
=============

.. c:function:: int i40e_set_rxfh(struct net_device *netdev, const u32 *indir, const u8 *key, const u8 hfunc)

    set the rx flow hash indirection table

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param indir:
        indirection table
    :type indir: const u32 \*

    :param key:
        hash key
    :type key: const u8 \*

    :param hfunc:
        hash function to use
    :type hfunc: const u8

.. _`i40e_set_rxfh.description`:

Description
-----------

Returns -EINVAL if the table specifies an invalid queue id, otherwise
returns 0 after programming the table.

.. _`i40e_get_priv_flags`:

i40e_get_priv_flags
===================

.. c:function:: u32 i40e_get_priv_flags(struct net_device *dev)

    report device private flags

    :param dev:
        network interface device structure
    :type dev: struct net_device \*

.. _`i40e_get_priv_flags.description`:

Description
-----------

The get string set count and the string set should be matched for each
flag returned.  Add new strings for each flag to the i40e_gstrings_priv_flags
array.

Returns a u32 bitmap of flags.

.. _`i40e_set_priv_flags`:

i40e_set_priv_flags
===================

.. c:function:: int i40e_set_priv_flags(struct net_device *dev, u32 flags)

    set private flags

    :param dev:
        network interface device structure
    :type dev: struct net_device \*

    :param flags:
        bit flags to be set
    :type flags: u32

.. _`i40e_get_module_info`:

i40e_get_module_info
====================

.. c:function:: int i40e_get_module_info(struct net_device *netdev, struct ethtool_modinfo *modinfo)

    get (Q)SFP+ module type info

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param modinfo:
        module EEPROM size and layout information structure
    :type modinfo: struct ethtool_modinfo \*

.. _`i40e_get_module_eeprom`:

i40e_get_module_eeprom
======================

.. c:function:: int i40e_get_module_eeprom(struct net_device *netdev, struct ethtool_eeprom *ee, u8 *data)

    fills buffer with (Q)SFP+ module memory contents

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ee:
        EEPROM dump request structure
    :type ee: struct ethtool_eeprom \*

    :param data:
        buffer to be filled with EEPROM contents
    :type data: u8 \*

.. This file was automatic generated / don't edit.

