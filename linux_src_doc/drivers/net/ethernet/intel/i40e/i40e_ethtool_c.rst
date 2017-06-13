.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_ethtool.c

.. _`i40e_partition_setting_complaint`:

i40e_partition_setting_complaint
================================

.. c:function:: void i40e_partition_setting_complaint(struct i40e_pf *pf)

    generic complaint for MFP restriction

    :param struct i40e_pf \*pf:
        the PF struct

.. _`i40e_phy_type_to_ethtool`:

i40e_phy_type_to_ethtool
========================

.. c:function:: void i40e_phy_type_to_ethtool(struct i40e_pf *pf, u32 *supported, u32 *advertising)

    convert the phy_types to ethtool link modes

    :param struct i40e_pf \*pf:
        *undescribed*

    :param u32 \*supported:
        pointer to the ethtool supported variable to fill in

    :param u32 \*advertising:
        pointer to the ethtool advertising variable to fill in

.. _`i40e_get_settings_link_up`:

i40e_get_settings_link_up
=========================

.. c:function:: void i40e_get_settings_link_up(struct i40e_hw *hw, struct ethtool_link_ksettings *cmd, struct net_device *netdev, struct i40e_pf *pf)

    Get the Link settings for when link is up

    :param struct i40e_hw \*hw:
        hw structure

    :param struct ethtool_link_ksettings \*cmd:
        *undescribed*

    :param struct net_device \*netdev:
        network interface device structure

    :param struct i40e_pf \*pf:
        *undescribed*

.. _`i40e_get_settings_link_down`:

i40e_get_settings_link_down
===========================

.. c:function:: void i40e_get_settings_link_down(struct i40e_hw *hw, struct ethtool_link_ksettings *cmd, struct i40e_pf *pf)

    Get the Link settings for when link is down

    :param struct i40e_hw \*hw:
        hw structure

    :param struct ethtool_link_ksettings \*cmd:
        *undescribed*

    :param struct i40e_pf \*pf:
        *undescribed*

.. _`i40e_get_settings_link_down.description`:

Description
-----------

Reports link settings that can be determined when link is down

.. _`i40e_get_link_ksettings`:

i40e_get_link_ksettings
=======================

.. c:function:: int i40e_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *cmd)

    Get Link Speed and Duplex settings

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_link_ksettings \*cmd:
        *undescribed*

.. _`i40e_get_link_ksettings.description`:

Description
-----------

Reports speed/duplex settings based on media_type

.. _`i40e_set_link_ksettings`:

i40e_set_link_ksettings
=======================

.. c:function:: int i40e_set_link_ksettings(struct net_device *netdev, const struct ethtool_link_ksettings *cmd)

    Set Speed and Duplex

    :param struct net_device \*netdev:
        network interface device structure

    :param const struct ethtool_link_ksettings \*cmd:
        *undescribed*

.. _`i40e_set_link_ksettings.description`:

Description
-----------

Set speed/duplex per media_types advertised/forced

.. _`i40e_get_pauseparam`:

i40e_get_pauseparam
===================

.. c:function:: void i40e_get_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Get Flow Control status Return tx/rx-pause status

    :param struct net_device \*netdev:
        *undescribed*

    :param struct ethtool_pauseparam \*pause:
        *undescribed*

.. _`i40e_set_pauseparam`:

i40e_set_pauseparam
===================

.. c:function:: int i40e_set_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *pause)

    Set Flow Control parameter

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_pauseparam \*pause:
        return tx/rx flow control status

.. _`i40e_set_wol`:

i40e_set_wol
============

.. c:function:: int i40e_set_wol(struct net_device *netdev, struct ethtool_wolinfo *wol)

    set the WakeOnLAN configuration

    :param struct net_device \*netdev:
        the netdev in question

    :param struct ethtool_wolinfo \*wol:
        the ethtool WoL setting data

.. _`__i40e_get_coalesce`:

__i40e_get_coalesce
===================

.. c:function:: int __i40e_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec, int queue)

    get per-queue coalesce settings

    :param struct net_device \*netdev:
        the netdev to check

    :param struct ethtool_coalesce \*ec:
        ethtool coalesce data structure

    :param int queue:
        which queue to pick

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

    :param struct net_device \*netdev:
        the netdev to check

    :param struct ethtool_coalesce \*ec:
        ethtool coalesce data structure

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

    :param struct net_device \*netdev:
        netdev structure

    :param u32 queue:
        the particular queue to read

    :param struct ethtool_coalesce \*ec:
        ethtool's coalesce settings

.. _`i40e_get_per_queue_coalesce.description`:

Description
-----------

Will read a specific queue's coalesce settings

.. _`i40e_set_itr_per_queue`:

i40e_set_itr_per_queue
======================

.. c:function:: void i40e_set_itr_per_queue(struct i40e_vsi *vsi, struct ethtool_coalesce *ec, int queue)

    set ITR values for specific queue

    :param struct i40e_vsi \*vsi:
        the VSI to set values for

    :param struct ethtool_coalesce \*ec:
        coalesce settings from ethtool

    :param int queue:
        the queue to modify

.. _`i40e_set_itr_per_queue.description`:

Description
-----------

Change the ITR settings for a specific queue.

.. _`__i40e_set_coalesce`:

__i40e_set_coalesce
===================

.. c:function:: int __i40e_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec, int queue)

    set coalesce settings for particular queue

    :param struct net_device \*netdev:
        the netdev to change

    :param struct ethtool_coalesce \*ec:
        ethtool coalesce settings

    :param int queue:
        the queue to change

.. _`__i40e_set_coalesce.description`:

Description
-----------

Sets the coalesce settings for a particular queue.

.. _`i40e_set_coalesce`:

i40e_set_coalesce
=================

.. c:function:: int i40e_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *ec)

    set coalesce settings for every queue on the netdev

    :param struct net_device \*netdev:
        the netdev to change

    :param struct ethtool_coalesce \*ec:
        ethtool coalesce settings

.. _`i40e_set_coalesce.description`:

Description
-----------

This will set each queue to the same coalesce settings.

.. _`i40e_set_per_queue_coalesce`:

i40e_set_per_queue_coalesce
===========================

.. c:function:: int i40e_set_per_queue_coalesce(struct net_device *netdev, u32 queue, struct ethtool_coalesce *ec)

    set specific queue's coalesce settings

    :param struct net_device \*netdev:
        the netdev to change

    :param u32 queue:
        the queue to change

    :param struct ethtool_coalesce \*ec:
        ethtool's coalesce settings

.. _`i40e_set_per_queue_coalesce.description`:

Description
-----------

Sets the specified queue's coalesce settings.

.. _`i40e_get_rss_hash_opts`:

i40e_get_rss_hash_opts
======================

.. c:function:: int i40e_get_rss_hash_opts(struct i40e_pf *pf, struct ethtool_rxnfc *cmd)

    Get RSS hash Input Set for each flow type

    :param struct i40e_pf \*pf:
        pointer to the physical function struct

    :param struct ethtool_rxnfc \*cmd:
        ethtool rxnfc command

.. _`i40e_get_rss_hash_opts.description`:

Description
-----------

Returns Success if the flow is supported, else Invalid Input.

.. _`i40e_check_mask`:

i40e_check_mask
===============

.. c:function:: int i40e_check_mask(u64 mask, u64 field)

    Check whether a mask field is set

    :param u64 mask:
        the full mask value
        \ ``field``\ ; mask of the field to check

    :param u64 field:
        *undescribed*

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

    :param struct ethtool_rx_flow_spec \*fsp:
        pointer to rx flow specification

    :param struct i40e_rx_flow_userdef \*data:
        pointer to userdef data structure for storage

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

    :param struct ethtool_rx_flow_spec \*fsp:
        pointer to rx_flow specification

    :param struct i40e_rx_flow_userdef \*data:
        *undescribed*

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

    :param struct i40e_pf \*pf:
        Pointer to the physical function struct

    :param struct ethtool_rxnfc \*cmd:
        The command to get or set Rx flow classification rules

    :param u32 \*rule_locs:
        Array of used rule locations

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

    :param struct i40e_pf \*pf:
        Pointer to the physical function struct

    :param struct ethtool_rxnfc \*cmd:
        The command to get or set Rx flow classification rules

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

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_rxnfc \*cmd:
        ethtool rxnfc command

    :param u32 \*rule_locs:
        *undescribed*

.. _`i40e_get_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`i40e_get_rss_hash_bits`:

i40e_get_rss_hash_bits
======================

.. c:function:: u64 i40e_get_rss_hash_bits(struct ethtool_rxnfc *nfc, u64 i_setc)

    Read RSS Hash bits from register

    :param struct ethtool_rxnfc \*nfc:
        pointer to user request
        \ ``i_setc``\  bits currently set

    :param u64 i_setc:
        *undescribed*

.. _`i40e_get_rss_hash_bits.description`:

Description
-----------

Returns value of bits to be set per user request

.. _`i40e_set_rss_hash_opt`:

i40e_set_rss_hash_opt
=====================

.. c:function:: int i40e_set_rss_hash_opt(struct i40e_pf *pf, struct ethtool_rxnfc *nfc)

    Enable/Disable flow types for RSS hash

    :param struct i40e_pf \*pf:
        pointer to the physical function struct

    :param struct ethtool_rxnfc \*nfc:
        *undescribed*

.. _`i40e_set_rss_hash_opt.description`:

Description
-----------

Returns Success if the flow input set is supported.

.. _`i40e_update_ethtool_fdir_entry`:

i40e_update_ethtool_fdir_entry
==============================

.. c:function:: int i40e_update_ethtool_fdir_entry(struct i40e_vsi *vsi, struct i40e_fdir_filter *input, u16 sw_idx, struct ethtool_rxnfc *cmd)

    Updates the fdir filter entry

    :param struct i40e_vsi \*vsi:
        Pointer to the targeted VSI

    :param struct i40e_fdir_filter \*input:
        The filter to update or NULL to indicate deletion

    :param u16 sw_idx:
        Software index to the filter

    :param struct ethtool_rxnfc \*cmd:
        The command to get or set Rx flow classification rules

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

    :param struct i40e_pf \*pf:
        pointer to PF structure

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

    :param struct i40e_vsi \*vsi:
        Pointer to the targeted VSI

    :param struct ethtool_rxnfc \*cmd:
        The command to get or set Rx flow classification rules

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

    :param struct i40e_pf \*pf:
        the PF data structure

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

    :param struct list_head \*flex_pit_list:
        L3 or L4 flex PIT list

    :param u16 src_offset:
        new src_offset to find

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

    :param struct list_head \*flex_pit_list:
        L3 or L4 flex PIT list

    :param u16 src_offset:
        new src_offset to add

    :param u8 pit_index:
        the PIT index to program

.. _`i40e_add_flex_offset.description`:

Description
-----------

This function programs the new src_offset to the list. It is expected that
i40e_find_flex_offset has already been tried and returned NULL, indicating
that this offset is not programmed, and that the list has enough space to
store another offset.

Returns 0 on success, and negative value on error.

.. _`__i40e_reprogram_flex_pit`:

__i40e_reprogram_flex_pit
=========================

.. c:function:: void __i40e_reprogram_flex_pit(struct i40e_pf *pf, struct list_head *flex_pit_list, int flex_pit_start)

    Re-program specific FLX_PIT table

    :param struct i40e_pf \*pf:
        Pointer to the PF structure

    :param struct list_head \*flex_pit_list:
        list of flexible src offsets in use
        #flex_pit_start: index to first entry for this section of the table

    :param int flex_pit_start:
        *undescribed*

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

    :param struct i40e_pf \*pf:
        pointer to the PF structure

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

    :param struct ethtool_rx_flow_spec \*fsp:
        *undescribed*

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

    :param int pit_index:
        PIT index to convert

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

    :param struct i40e_vsi \*vsi:
        the vsi being configured

    :param u64 old:
        the old input set

    :param u64 new:
        the new input set

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

    :param struct i40e_vsi \*vsi:
        pointer to the targeted VSI

    :param struct ethtool_rx_flow_spec \*fsp:
        pointer to Rx flow specification

    :param struct i40e_rx_flow_userdef \*userdef:
        userdefined data from flow specification

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

.. _`i40e_add_fdir_ethtool`:

i40e_add_fdir_ethtool
=====================

.. c:function:: int i40e_add_fdir_ethtool(struct i40e_vsi *vsi, struct ethtool_rxnfc *cmd)

    Add/Remove Flow Director filters

    :param struct i40e_vsi \*vsi:
        pointer to the targeted VSI

    :param struct ethtool_rxnfc \*cmd:
        command to get or set RX flow classification rules

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

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_rxnfc \*cmd:
        ethtool rxnfc command

.. _`i40e_set_rxnfc.description`:

Description
-----------

Returns Success if the command is supported.

.. _`i40e_max_channels`:

i40e_max_channels
=================

.. c:function:: unsigned int i40e_max_channels(struct i40e_vsi *vsi)

    get Max number of combined channels supported

    :param struct i40e_vsi \*vsi:
        vsi pointer

.. _`i40e_get_channels`:

i40e_get_channels
=================

.. c:function:: void i40e_get_channels(struct net_device *dev, struct ethtool_channels *ch)

    Get the current channels enabled and max supported etc.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_channels \*ch:
        ethtool channels structure

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

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_channels \*ch:
        ethtool channels structure

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

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_get_rxfh_key_size.description`:

Description
-----------

Returns the table size.

.. _`i40e_get_rxfh_indir_size`:

i40e_get_rxfh_indir_size
========================

.. c:function:: u32 i40e_get_rxfh_indir_size(struct net_device *netdev)

    get the rx flow hash indirection table size

    :param struct net_device \*netdev:
        network interface device structure

.. _`i40e_get_rxfh_indir_size.description`:

Description
-----------

Returns the table size.

.. _`i40e_set_rxfh`:

i40e_set_rxfh
=============

.. c:function:: int i40e_set_rxfh(struct net_device *netdev, const u32 *indir, const u8 *key, const u8 hfunc)

    set the rx flow hash indirection table

    :param struct net_device \*netdev:
        network interface device structure

    :param const u32 \*indir:
        indirection table

    :param const u8 \*key:
        hash key

    :param const u8 hfunc:
        *undescribed*

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

    :param struct net_device \*dev:
        network interface device structure

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

    :param struct net_device \*dev:
        network interface device structure

    :param u32 flags:
        bit flags to be set

.. This file was automatic generated / don't edit.

