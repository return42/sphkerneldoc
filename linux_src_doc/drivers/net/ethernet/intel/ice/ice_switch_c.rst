.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_switch.c

.. _`ice_aq_alloc_free_res`:

ice_aq_alloc_free_res
=====================

.. c:function:: enum ice_status ice_aq_alloc_free_res(struct ice_hw *hw, u16 num_entries, struct ice_aqc_alloc_free_res_elem *buf, u16 buf_size, enum ice_adminq_opc opc, struct ice_sq_cd *cd)

    command to allocate/free resources

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 num_entries:
        number of resource entries in buffer

    :param struct ice_aqc_alloc_free_res_elem \*buf:
        Indirect buffer to hold data parameters and response

    :param u16 buf_size:
        size of buffer for indirect commands

    :param enum ice_adminq_opc opc:
        pass in the command opcode

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_alloc_free_res.description`:

Description
-----------

Helper function to allocate/free resources using the admin queue commands

.. _`ice_aq_get_sw_cfg`:

ice_aq_get_sw_cfg
=================

.. c:function:: enum ice_status ice_aq_get_sw_cfg(struct ice_hw *hw, struct ice_aqc_get_sw_cfg_resp *buf, u16 buf_size, u16 *req_desc, u16 *num_elems, struct ice_sq_cd *cd)

    get switch configuration

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_aqc_get_sw_cfg_resp \*buf:
        pointer to the result buffer

    :param u16 buf_size:
        length of the buffer available for response

    :param u16 \*req_desc:
        pointer to requested descriptor

    :param u16 \*num_elems:
        pointer to number of elements

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_get_sw_cfg.description`:

Description
-----------

Get switch configuration (0x0200) to be placed in 'buff'.
This admin command returns information such as initial VSI/port number
and switch ID it belongs to.

.. _`ice_aq_get_sw_cfg.note`:

NOTE
----

\*req_desc is both an input/output parameter.
The caller of this function first calls this function with \*request_desc set
to 0.  If the response from f/w has \*req_desc set to 0, all the switch
configuration information has been returned; if non-zero (meaning not all
the information was returned), the caller should call this function again
with \*req_desc set to the previous value returned by f/w to get the
next block of switch configuration information.

\*num_elems is output only parameter. This reflects the number of elements
in response buffer. The caller of this function to use \*num_elems while
parsing the response buffer.

.. _`ice_aq_add_vsi`:

ice_aq_add_vsi
==============

.. c:function:: enum ice_status ice_aq_add_vsi(struct ice_hw *hw, struct ice_vsi_ctx *vsi_ctx, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_vsi_ctx \*vsi_ctx:
        pointer to a VSI context struct

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_add_vsi.description`:

Description
-----------

Add a VSI context to the hardware (0x0210)

.. _`ice_aq_update_vsi`:

ice_aq_update_vsi
=================

.. c:function:: enum ice_status ice_aq_update_vsi(struct ice_hw *hw, struct ice_vsi_ctx *vsi_ctx, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_vsi_ctx \*vsi_ctx:
        pointer to a VSI context struct

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_update_vsi.description`:

Description
-----------

Update VSI context in the hardware (0x0211)

.. _`ice_aq_free_vsi`:

ice_aq_free_vsi
===============

.. c:function:: enum ice_status ice_aq_free_vsi(struct ice_hw *hw, struct ice_vsi_ctx *vsi_ctx, bool keep_vsi_alloc, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_vsi_ctx \*vsi_ctx:
        pointer to a VSI context struct

    :param bool keep_vsi_alloc:
        keep VSI allocation as part of this PF's resources

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_free_vsi.description`:

Description
-----------

Get VSI context info from hardware (0x0213)

.. _`ice_aq_alloc_free_vsi_list`:

ice_aq_alloc_free_vsi_list
==========================

.. c:function:: enum ice_status ice_aq_alloc_free_vsi_list(struct ice_hw *hw, u16 *vsi_list_id, enum ice_sw_lkup_type lkup_type, enum ice_adminq_opc opc)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 \*vsi_list_id:
        VSI list id returned or used for lookup

    :param enum ice_sw_lkup_type lkup_type:
        switch rule filter lookup type

    :param enum ice_adminq_opc opc:
        switch rules population command type - pass in the command opcode

.. _`ice_aq_alloc_free_vsi_list.description`:

Description
-----------

allocates or free a VSI list resource

.. _`ice_aq_sw_rules`:

ice_aq_sw_rules
===============

.. c:function:: enum ice_status ice_aq_sw_rules(struct ice_hw *hw, void *rule_list, u16 rule_list_sz, u8 num_rules, enum ice_adminq_opc opc, struct ice_sq_cd *cd)

    add/update/remove switch rules

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param void \*rule_list:
        pointer to switch rule population list

    :param u16 rule_list_sz:
        total size of the rule list in bytes

    :param u8 num_rules:
        number of switch rules in the rule_list

    :param enum ice_adminq_opc opc:
        switch rules population command type - pass in the command opcode

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_sw_rules.description`:

Description
-----------

Add(0x02a0)/Update(0x02a1)/Remove(0x02a2) switch rules commands to firmware

.. _`ice_fill_sw_info`:

ice_fill_sw_info
================

.. c:function:: void ice_fill_sw_info(struct ice_hw *hw, struct ice_fltr_info *f_info)

    Helper function to populate lb_en and lan_en

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_info \*f_info:
        filter info structure to fill/update

.. _`ice_fill_sw_info.description`:

Description
-----------

This helper function populates the lb_en and lan_en elements of the provided
ice_fltr_info struct using the switch's type and characteristics of the
switch rule being configured.

.. _`ice_fill_sw_rule`:

ice_fill_sw_rule
================

.. c:function:: void ice_fill_sw_rule(struct ice_hw *hw, struct ice_fltr_info *f_info, struct ice_aqc_sw_rules_elem *s_rule, enum ice_adminq_opc opc)

    Helper function to fill switch rule structure

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_info \*f_info:
        entry containing packet forwarding information

    :param struct ice_aqc_sw_rules_elem \*s_rule:
        switch rule structure to be filled in based on mac_entry

    :param enum ice_adminq_opc opc:
        switch rules population command type - pass in the command opcode

.. _`ice_add_marker_act`:

ice_add_marker_act
==================

.. c:function:: enum ice_status ice_add_marker_act(struct ice_hw *hw, struct ice_fltr_mgmt_list_entry *m_ent, u16 sw_marker, u16 l_id)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_mgmt_list_entry \*m_ent:
        the management entry for which sw marker needs to be added

    :param u16 sw_marker:
        sw marker to tag the Rx descriptor with

    :param u16 l_id:
        large action resource id

.. _`ice_add_marker_act.description`:

Description
-----------

Create a large action to hold software marker and update the switch rule
entry pointed by m_ent with newly created large action

.. _`ice_create_vsi_list_map`:

ice_create_vsi_list_map
=======================

.. c:function:: struct ice_vsi_list_map_info *ice_create_vsi_list_map(struct ice_hw *hw, u16 *vsi_array, u16 num_vsi, u16 vsi_list_id)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 \*vsi_array:
        array of VSIs to form a VSI list

    :param u16 num_vsi:
        num VSI in the array

    :param u16 vsi_list_id:
        VSI list id generated as part of allocate resource

.. _`ice_create_vsi_list_map.description`:

Description
-----------

Helper function to create a new entry of VSI list id to VSI mapping
using the given VSI list id

.. _`ice_update_vsi_list_rule`:

ice_update_vsi_list_rule
========================

.. c:function:: enum ice_status ice_update_vsi_list_rule(struct ice_hw *hw, u16 *vsi_array, u16 num_vsi, u16 vsi_list_id, bool remove, enum ice_adminq_opc opc, enum ice_sw_lkup_type lkup_type)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 \*vsi_array:
        array of VSIs to form a VSI list

    :param u16 num_vsi:
        num VSI in the array

    :param u16 vsi_list_id:
        VSI list id generated as part of allocate resource

    :param bool remove:
        Boolean value to indicate if this is a remove action

    :param enum ice_adminq_opc opc:
        switch rules population command type - pass in the command opcode

    :param enum ice_sw_lkup_type lkup_type:
        lookup type of the filter

.. _`ice_update_vsi_list_rule.description`:

Description
-----------

Call AQ command to add a new switch rule or update existing switch rule
using the given VSI list id

.. _`ice_create_vsi_list_rule`:

ice_create_vsi_list_rule
========================

.. c:function:: enum ice_status ice_create_vsi_list_rule(struct ice_hw *hw, u16 *vsi_array, u16 num_vsi, u16 *vsi_list_id, enum ice_sw_lkup_type lkup_type)

    Creates and populates a VSI list rule

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 \*vsi_array:
        array of VSIs to form a VSI list

    :param u16 num_vsi:
        number of VSIs in the array

    :param u16 \*vsi_list_id:
        stores the ID of the VSI list to be created

    :param enum ice_sw_lkup_type lkup_type:
        switch rule filter's lookup type

.. _`ice_create_pkt_fwd_rule`:

ice_create_pkt_fwd_rule
=======================

.. c:function:: enum ice_status ice_create_pkt_fwd_rule(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_list_entry \*f_entry:
        entry containing packet forwarding information

.. _`ice_create_pkt_fwd_rule.description`:

Description
-----------

Create switch rule with given filter information and add an entry
to the corresponding filter management list to track this switch rule
and VSI mapping

.. _`ice_update_pkt_fwd_rule`:

ice_update_pkt_fwd_rule
=======================

.. c:function:: enum ice_status ice_update_pkt_fwd_rule(struct ice_hw *hw, u16 rule_id, u16 vsi_list_id, struct ice_fltr_info f_info)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 rule_id:
        rule of previously created switch rule to update

    :param u16 vsi_list_id:
        VSI list id to be updated with

    :param struct ice_fltr_info f_info:
        ice_fltr_info to pull other information for switch rule

.. _`ice_update_pkt_fwd_rule.description`:

Description
-----------

Call AQ command to update a previously created switch rule with a
VSI list id

.. _`ice_handle_vsi_list_mgmt`:

ice_handle_vsi_list_mgmt
========================

.. c:function:: enum ice_status ice_handle_vsi_list_mgmt(struct ice_hw *hw, struct ice_fltr_mgmt_list_entry *m_entry, struct ice_fltr_info *cur_fltr, struct ice_fltr_info *new_fltr)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_mgmt_list_entry \*m_entry:
        pointer to current filter management list entry

    :param struct ice_fltr_info \*cur_fltr:
        filter information from the book keeping entry

    :param struct ice_fltr_info \*new_fltr:
        filter information with the new VSI to be added

.. _`ice_handle_vsi_list_mgmt.description`:

Description
-----------

Call AQ command to add or update previously created VSI list with new VSI.

Helper function to do book keeping associated with adding filter information
The algorithm to do the booking keeping is described below :
When a VSI needs to subscribe to a given filter( MAC/VLAN/Ethtype etc.)
if only one VSI has been added till now
Allocate a new VSI list and add two VSIs
to this list using switch rule command
Update the previously created switch rule with the
newly created VSI list id
if a VSI list was previously created
Add the new VSI to the previously created VSI list set
using the update switch rule command

.. _`ice_find_mac_entry`:

ice_find_mac_entry
==================

.. c:function:: struct ice_fltr_mgmt_list_entry *ice_find_mac_entry(struct ice_hw *hw, u8 *mac_addr)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u8 \*mac_addr:
        MAC address to search for

.. _`ice_find_mac_entry.description`:

Description
-----------

Helper function to search for a MAC entry using a given MAC address
Returns pointer to the entry if found.

.. _`ice_add_shared_mac`:

ice_add_shared_mac
==================

.. c:function:: enum ice_status ice_add_shared_mac(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    Add one MAC shared filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_list_entry \*f_entry:
        structure containing MAC forwarding information

.. _`ice_add_shared_mac.description`:

Description
-----------

Adds or updates the book keeping list for the MAC addresses

.. _`ice_add_mac`:

ice_add_mac
===========

.. c:function:: enum ice_status ice_add_mac(struct ice_hw *hw, struct list_head *m_list)

    Add a MAC address based filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct list_head \*m_list:
        list of MAC addresses and forwarding information

.. _`ice_add_mac.important`:

IMPORTANT
---------

When the ucast_shared flag is set to false and m_list has
multiple unicast addresses, the function assumes that all the
addresses are unique in a given add_mac call. It doesn't
check for duplicates in this case, removing duplicates from a given
list should be taken care of in the caller of this function.

.. _`ice_find_vlan_entry`:

ice_find_vlan_entry
===================

.. c:function:: struct ice_fltr_mgmt_list_entry *ice_find_vlan_entry(struct ice_hw *hw, u16 vlan_id)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vlan_id:
        VLAN id to search for

.. _`ice_find_vlan_entry.description`:

Description
-----------

Helper function to search for a VLAN entry using a given VLAN id
Returns pointer to the entry if found.

.. _`ice_add_vlan_internal`:

ice_add_vlan_internal
=====================

.. c:function:: enum ice_status ice_add_vlan_internal(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    Add one VLAN based filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_list_entry \*f_entry:
        filter entry containing one VLAN information

.. _`ice_add_vlan`:

ice_add_vlan
============

.. c:function:: enum ice_status ice_add_vlan(struct ice_hw *hw, struct list_head *v_list)

    Add VLAN based filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct list_head \*v_list:
        list of VLAN entries and forwarding information

.. _`ice_remove_vsi_list_rule`:

ice_remove_vsi_list_rule
========================

.. c:function:: enum ice_status ice_remove_vsi_list_rule(struct ice_hw *hw, u16 vsi_list_id, enum ice_sw_lkup_type lkup_type)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_list_id:
        VSI list id generated as part of allocate resource

    :param enum ice_sw_lkup_type lkup_type:
        switch rule filter lookup type

.. _`ice_handle_rem_vsi_list_mgmt`:

ice_handle_rem_vsi_list_mgmt
============================

.. c:function:: enum ice_status ice_handle_rem_vsi_list_mgmt(struct ice_hw *hw, u16 vsi_id, struct ice_fltr_mgmt_list_entry *fm_list_itr)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        ID of the VSI to remove

    :param struct ice_fltr_mgmt_list_entry \*fm_list_itr:
        filter management entry for which the VSI list management
        needs to be done

.. _`ice_remove_mac_entry`:

ice_remove_mac_entry
====================

.. c:function:: enum ice_status ice_remove_mac_entry(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_list_entry \*f_entry:
        structure containing MAC forwarding information

.. _`ice_remove_mac`:

ice_remove_mac
==============

.. c:function:: enum ice_status ice_remove_mac(struct ice_hw *hw, struct list_head *m_list)

    remove a MAC address based filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct list_head \*m_list:
        list of MAC addresses and forwarding information

.. _`ice_remove_mac.description`:

Description
-----------

This function removes either a MAC filter rule or a specific VSI from a
VSI list for a multicast MAC address.

Returns ICE_ERR_DOES_NOT_EXIST if a given entry was not added by
ice_add_mac. Caller should be aware that this call will only work if all
the entries passed into m_list were added previously. It will not attempt to
do a partial remove of entries that were found.

.. _`ice_cfg_dflt_vsi`:

ice_cfg_dflt_vsi
================

.. c:function:: enum ice_status ice_cfg_dflt_vsi(struct ice_hw *hw, u16 vsi_id, bool set, u8 direction)

    add filter rule to set/unset given VSI as default VSI for the switch (represented by swid)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        number of VSI to set as default

    :param bool set:
        true to add the above mentioned switch rule, false to remove it

    :param u8 direction:
        ICE_FLTR_RX or ICE_FLTR_TX

.. _`ice_remove_vlan_internal`:

ice_remove_vlan_internal
========================

.. c:function:: enum ice_status ice_remove_vlan_internal(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    Remove one VLAN based filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_fltr_list_entry \*f_entry:
        filter entry containing one VLAN information

.. _`ice_remove_vlan`:

ice_remove_vlan
===============

.. c:function:: enum ice_status ice_remove_vlan(struct ice_hw *hw, struct list_head *v_list)

    Remove VLAN based filter rule

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct list_head \*v_list:
        list of VLAN entries and forwarding information

.. _`ice_add_to_vsi_fltr_list`:

ice_add_to_vsi_fltr_list
========================

.. c:function:: enum ice_status ice_add_to_vsi_fltr_list(struct ice_hw *hw, u16 vsi_id, struct list_head *lkup_list_head, struct list_head *vsi_list_head)

    Add VSI filters to the list

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        ID of VSI to remove filters from

    :param struct list_head \*lkup_list_head:
        pointer to the list that has certain lookup type filters

    :param struct list_head \*vsi_list_head:
        pointer to the list pertaining to VSI with vsi_id

.. _`ice_remove_vsi_lkup_fltr`:

ice_remove_vsi_lkup_fltr
========================

.. c:function:: void ice_remove_vsi_lkup_fltr(struct ice_hw *hw, u16 vsi_id, enum ice_sw_lkup_type lkup)

    Remove lookup type filters for a VSI

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        ID of VSI to remove filters from

    :param enum ice_sw_lkup_type lkup:
        switch rule filter lookup type

.. _`ice_remove_vsi_fltr`:

ice_remove_vsi_fltr
===================

.. c:function:: void ice_remove_vsi_fltr(struct ice_hw *hw, u16 vsi_id)

    Remove all filters for a VSI

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        ID of VSI to remove filters from

.. This file was automatic generated / don't edit.

