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

.. c:function:: void i40e_get_settings_link_up(struct i40e_hw *hw, struct ethtool_cmd *ecmd, struct net_device *netdev, struct i40e_pf *pf)

    Get the Link settings for when link is up

    :param struct i40e_hw \*hw:
        hw structure

    :param struct ethtool_cmd \*ecmd:
        ethtool command to fill in

    :param struct net_device \*netdev:
        network interface device structure

    :param struct i40e_pf \*pf:
        *undescribed*

.. _`i40e_get_settings_link_down`:

i40e_get_settings_link_down
===========================

.. c:function:: void i40e_get_settings_link_down(struct i40e_hw *hw, struct ethtool_cmd *ecmd, struct i40e_pf *pf)

    Get the Link settings for when link is down

    :param struct i40e_hw \*hw:
        hw structure

    :param struct ethtool_cmd \*ecmd:
        ethtool command to fill in

    :param struct i40e_pf \*pf:
        *undescribed*

.. _`i40e_get_settings_link_down.description`:

Description
-----------

Reports link settings that can be determined when link is down

.. _`i40e_get_settings`:

i40e_get_settings
=================

.. c:function:: int i40e_get_settings(struct net_device *netdev, struct ethtool_cmd *ecmd)

    Get Link Speed and Duplex settings

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_cmd \*ecmd:
        ethtool command

.. _`i40e_get_settings.description`:

Description
-----------

Reports speed/duplex settings based on media_type

.. _`i40e_set_settings`:

i40e_set_settings
=================

.. c:function:: int i40e_set_settings(struct net_device *netdev, struct ethtool_cmd *ecmd)

    Set Speed and Duplex

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_cmd \*ecmd:
        ethtool command

.. _`i40e_set_settings.description`:

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

.. _`i40e_match_fdir_input_set`:

i40e_match_fdir_input_set
=========================

.. c:function:: bool i40e_match_fdir_input_set(struct i40e_fdir_filter *rule, struct i40e_fdir_filter *input)

    Match a new filter against an existing one

    :param struct i40e_fdir_filter \*rule:
        The filter already added

    :param struct i40e_fdir_filter \*input:
        The new filter to comapre against

.. _`i40e_match_fdir_input_set.description`:

Description
-----------

Returns true if the two input set match

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
flag returned.  Add new strings for each flag to the i40e_priv_flags_strings
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

