.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_switch.c

.. _`ice_aq_alloc_free_res`:

ice_aq_alloc_free_res
=====================

.. c:function:: enum ice_status ice_aq_alloc_free_res(struct ice_hw *hw, u16 num_entries, struct ice_aqc_alloc_free_res_elem *buf, u16 buf_size, enum ice_adminq_opc opc, struct ice_sq_cd *cd)

    command to allocate/free resources

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param num_entries:
        number of resource entries in buffer
    :type num_entries: u16

    :param buf:
        Indirect buffer to hold data parameters and response
    :type buf: struct ice_aqc_alloc_free_res_elem \*

    :param buf_size:
        size of buffer for indirect commands
    :type buf_size: u16

    :param opc:
        pass in the command opcode
    :type opc: enum ice_adminq_opc

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_alloc_free_res.description`:

Description
-----------

Helper function to allocate/free resources using the admin queue commands

.. _`ice_init_def_sw_recp`:

ice_init_def_sw_recp
====================

.. c:function:: enum ice_status ice_init_def_sw_recp(struct ice_hw *hw)

    initialize the recipe book keeping tables

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_init_def_sw_recp.description`:

Description
-----------

Allocate memory for the entire recipe table and initialize the structures/
entries corresponding to basic recipes.

.. _`ice_aq_get_sw_cfg`:

ice_aq_get_sw_cfg
=================

.. c:function:: enum ice_status ice_aq_get_sw_cfg(struct ice_hw *hw, struct ice_aqc_get_sw_cfg_resp *buf, u16 buf_size, u16 *req_desc, u16 *num_elems, struct ice_sq_cd *cd)

    get switch configuration

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param buf:
        pointer to the result buffer
    :type buf: struct ice_aqc_get_sw_cfg_resp \*

    :param buf_size:
        length of the buffer available for response
    :type buf_size: u16

    :param req_desc:
        pointer to requested descriptor
    :type req_desc: u16 \*

    :param num_elems:
        pointer to number of elements
    :type num_elems: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

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

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_ctx:
        pointer to a VSI context struct
    :type vsi_ctx: struct ice_vsi_ctx \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_add_vsi.description`:

Description
-----------

Add a VSI context to the hardware (0x0210)

.. _`ice_aq_free_vsi`:

ice_aq_free_vsi
===============

.. c:function:: enum ice_status ice_aq_free_vsi(struct ice_hw *hw, struct ice_vsi_ctx *vsi_ctx, bool keep_vsi_alloc, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_ctx:
        pointer to a VSI context struct
    :type vsi_ctx: struct ice_vsi_ctx \*

    :param keep_vsi_alloc:
        keep VSI allocation as part of this PF's resources
    :type keep_vsi_alloc: bool

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_free_vsi.description`:

Description
-----------

Free VSI context info from hardware (0x0213)

.. _`ice_aq_update_vsi`:

ice_aq_update_vsi
=================

.. c:function:: enum ice_status ice_aq_update_vsi(struct ice_hw *hw, struct ice_vsi_ctx *vsi_ctx, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_ctx:
        pointer to a VSI context struct
    :type vsi_ctx: struct ice_vsi_ctx \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_update_vsi.description`:

Description
-----------

Update VSI context in the hardware (0x0211)

.. _`ice_is_vsi_valid`:

ice_is_vsi_valid
================

.. c:function:: bool ice_is_vsi_valid(struct ice_hw *hw, u16 vsi_handle)

    check whether the VSI is valid or not

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle
    :type vsi_handle: u16

.. _`ice_is_vsi_valid.description`:

Description
-----------

check whether the VSI is valid or not

.. _`ice_get_hw_vsi_num`:

ice_get_hw_vsi_num
==================

.. c:function:: u16 ice_get_hw_vsi_num(struct ice_hw *hw, u16 vsi_handle)

    return the hw VSI number

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle
    :type vsi_handle: u16

.. _`ice_get_hw_vsi_num.description`:

Description
-----------

return the hw VSI number

.. _`ice_get_hw_vsi_num.caution`:

Caution
-------

call this function only if VSI is valid (ice_is_vsi_valid)

.. _`ice_get_vsi_ctx`:

ice_get_vsi_ctx
===============

.. c:function:: struct ice_vsi_ctx *ice_get_vsi_ctx(struct ice_hw *hw, u16 vsi_handle)

    return the VSI context entry for a given VSI handle

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle
    :type vsi_handle: u16

.. _`ice_get_vsi_ctx.description`:

Description
-----------

return the VSI context entry for a given VSI handle

.. _`ice_save_vsi_ctx`:

ice_save_vsi_ctx
================

.. c:function:: void ice_save_vsi_ctx(struct ice_hw *hw, u16 vsi_handle, struct ice_vsi_ctx *vsi)

    save the VSI context for a given VSI handle

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle
    :type vsi_handle: u16

    :param vsi:
        VSI context pointer
    :type vsi: struct ice_vsi_ctx \*

.. _`ice_save_vsi_ctx.description`:

Description
-----------

save the VSI context entry for a given VSI handle

.. _`ice_clear_vsi_ctx`:

ice_clear_vsi_ctx
=================

.. c:function:: void ice_clear_vsi_ctx(struct ice_hw *hw, u16 vsi_handle)

    clear the VSI context entry

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle
    :type vsi_handle: u16

.. _`ice_clear_vsi_ctx.description`:

Description
-----------

clear the VSI context entry

.. _`ice_clear_all_vsi_ctx`:

ice_clear_all_vsi_ctx
=====================

.. c:function:: void ice_clear_all_vsi_ctx(struct ice_hw *hw)

    clear all the VSI context entries

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_add_vsi`:

ice_add_vsi
===========

.. c:function:: enum ice_status ice_add_vsi(struct ice_hw *hw, u16 vsi_handle, struct ice_vsi_ctx *vsi_ctx, struct ice_sq_cd *cd)

    add VSI context to the hardware and VSI handle list

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        unique VSI handle provided by drivers
    :type vsi_handle: u16

    :param vsi_ctx:
        pointer to a VSI context struct
    :type vsi_ctx: struct ice_vsi_ctx \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_add_vsi.description`:

Description
-----------

Add a VSI context to the hardware also add it into the VSI handle list.
If this function gets called after reset for existing VSIs then update
with the new HW VSI number in the corresponding VSI handle list entry.

.. _`ice_free_vsi`:

ice_free_vsi
============

.. c:function:: enum ice_status ice_free_vsi(struct ice_hw *hw, u16 vsi_handle, struct ice_vsi_ctx *vsi_ctx, bool keep_vsi_alloc, struct ice_sq_cd *cd)

    free VSI context from hardware and VSI handle list

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        unique VSI handle
    :type vsi_handle: u16

    :param vsi_ctx:
        pointer to a VSI context struct
    :type vsi_ctx: struct ice_vsi_ctx \*

    :param keep_vsi_alloc:
        keep VSI allocation as part of this PF's resources
    :type keep_vsi_alloc: bool

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_free_vsi.description`:

Description
-----------

Free VSI context info from hardware as well as from VSI handle list

.. _`ice_update_vsi`:

ice_update_vsi
==============

.. c:function:: enum ice_status ice_update_vsi(struct ice_hw *hw, u16 vsi_handle, struct ice_vsi_ctx *vsi_ctx, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        unique VSI handle
    :type vsi_handle: u16

    :param vsi_ctx:
        pointer to a VSI context struct
    :type vsi_ctx: struct ice_vsi_ctx \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_update_vsi.description`:

Description
-----------

Update VSI context in the hardware

.. _`ice_aq_alloc_free_vsi_list`:

ice_aq_alloc_free_vsi_list
==========================

.. c:function:: enum ice_status ice_aq_alloc_free_vsi_list(struct ice_hw *hw, u16 *vsi_list_id, enum ice_sw_lkup_type lkup_type, enum ice_adminq_opc opc)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_list_id:
        VSI list id returned or used for lookup
    :type vsi_list_id: u16 \*

    :param lkup_type:
        switch rule filter lookup type
    :type lkup_type: enum ice_sw_lkup_type

    :param opc:
        switch rules population command type - pass in the command opcode
    :type opc: enum ice_adminq_opc

.. _`ice_aq_alloc_free_vsi_list.description`:

Description
-----------

allocates or free a VSI list resource

.. _`ice_aq_sw_rules`:

ice_aq_sw_rules
===============

.. c:function:: enum ice_status ice_aq_sw_rules(struct ice_hw *hw, void *rule_list, u16 rule_list_sz, u8 num_rules, enum ice_adminq_opc opc, struct ice_sq_cd *cd)

    add/update/remove switch rules

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param rule_list:
        pointer to switch rule population list
    :type rule_list: void \*

    :param rule_list_sz:
        total size of the rule list in bytes
    :type rule_list_sz: u16

    :param num_rules:
        number of switch rules in the rule_list
    :type num_rules: u8

    :param opc:
        switch rules population command type - pass in the command opcode
    :type opc: enum ice_adminq_opc

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_sw_rules.description`:

Description
-----------

Add(0x02a0)/Update(0x02a1)/Remove(0x02a2) switch rules commands to firmware

.. _`ice_fill_sw_info`:

ice_fill_sw_info
================

.. c:function:: void ice_fill_sw_info(struct ice_hw *hw, struct ice_fltr_info *f_info)

    Helper function to populate lb_en and lan_en

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param f_info:
        filter info structure to fill/update
    :type f_info: struct ice_fltr_info \*

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

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param f_info:
        entry containing packet forwarding information
    :type f_info: struct ice_fltr_info \*

    :param s_rule:
        switch rule structure to be filled in based on mac_entry
    :type s_rule: struct ice_aqc_sw_rules_elem \*

    :param opc:
        switch rules population command type - pass in the command opcode
    :type opc: enum ice_adminq_opc

.. _`ice_add_marker_act`:

ice_add_marker_act
==================

.. c:function:: enum ice_status ice_add_marker_act(struct ice_hw *hw, struct ice_fltr_mgmt_list_entry *m_ent, u16 sw_marker, u16 l_id)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param m_ent:
        the management entry for which sw marker needs to be added
    :type m_ent: struct ice_fltr_mgmt_list_entry \*

    :param sw_marker:
        sw marker to tag the Rx descriptor with
    :type sw_marker: u16

    :param l_id:
        large action resource id
    :type l_id: u16

.. _`ice_add_marker_act.description`:

Description
-----------

Create a large action to hold software marker and update the switch rule
entry pointed by m_ent with newly created large action

.. _`ice_create_vsi_list_map`:

ice_create_vsi_list_map
=======================

.. c:function:: struct ice_vsi_list_map_info *ice_create_vsi_list_map(struct ice_hw *hw, u16 *vsi_handle_arr, u16 num_vsi, u16 vsi_list_id)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle_arr:
        array of VSI handles to set in the VSI mapping
    :type vsi_handle_arr: u16 \*

    :param num_vsi:
        number of VSI handles in the array
    :type num_vsi: u16

    :param vsi_list_id:
        VSI list id generated as part of allocate resource
    :type vsi_list_id: u16

.. _`ice_create_vsi_list_map.description`:

Description
-----------

Helper function to create a new entry of VSI list id to VSI mapping
using the given VSI list id

.. _`ice_update_vsi_list_rule`:

ice_update_vsi_list_rule
========================

.. c:function:: enum ice_status ice_update_vsi_list_rule(struct ice_hw *hw, u16 *vsi_handle_arr, u16 num_vsi, u16 vsi_list_id, bool remove, enum ice_adminq_opc opc, enum ice_sw_lkup_type lkup_type)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle_arr:
        array of VSI handles to form a VSI list
    :type vsi_handle_arr: u16 \*

    :param num_vsi:
        number of VSI handles in the array
    :type num_vsi: u16

    :param vsi_list_id:
        VSI list id generated as part of allocate resource
    :type vsi_list_id: u16

    :param remove:
        Boolean value to indicate if this is a remove action
    :type remove: bool

    :param opc:
        switch rules population command type - pass in the command opcode
    :type opc: enum ice_adminq_opc

    :param lkup_type:
        lookup type of the filter
    :type lkup_type: enum ice_sw_lkup_type

.. _`ice_update_vsi_list_rule.description`:

Description
-----------

Call AQ command to add a new switch rule or update existing switch rule
using the given VSI list id

.. _`ice_create_vsi_list_rule`:

ice_create_vsi_list_rule
========================

.. c:function:: enum ice_status ice_create_vsi_list_rule(struct ice_hw *hw, u16 *vsi_handle_arr, u16 num_vsi, u16 *vsi_list_id, enum ice_sw_lkup_type lkup_type)

    Creates and populates a VSI list rule

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle_arr:
        array of VSI handles to form a VSI list
    :type vsi_handle_arr: u16 \*

    :param num_vsi:
        number of VSI handles in the array
    :type num_vsi: u16

    :param vsi_list_id:
        stores the ID of the VSI list to be created
    :type vsi_list_id: u16 \*

    :param lkup_type:
        switch rule filter's lookup type
    :type lkup_type: enum ice_sw_lkup_type

.. _`ice_create_pkt_fwd_rule`:

ice_create_pkt_fwd_rule
=======================

.. c:function:: enum ice_status ice_create_pkt_fwd_rule(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param f_entry:
        entry containing packet forwarding information
    :type f_entry: struct ice_fltr_list_entry \*

.. _`ice_create_pkt_fwd_rule.description`:

Description
-----------

Create switch rule with given filter information and add an entry
to the corresponding filter management list to track this switch rule
and VSI mapping

.. _`ice_update_pkt_fwd_rule`:

ice_update_pkt_fwd_rule
=======================

.. c:function:: enum ice_status ice_update_pkt_fwd_rule(struct ice_hw *hw, struct ice_fltr_info *f_info)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param f_info:
        filter information for switch rule
    :type f_info: struct ice_fltr_info \*

.. _`ice_update_pkt_fwd_rule.description`:

Description
-----------

Call AQ command to update a previously created switch rule with a
VSI list id

.. _`ice_update_sw_rule_bridge_mode`:

ice_update_sw_rule_bridge_mode
==============================

.. c:function:: enum ice_status ice_update_sw_rule_bridge_mode(struct ice_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_update_sw_rule_bridge_mode.description`:

Description
-----------

Updates unicast switch filter rules based on VEB/VEPA mode

.. _`ice_add_update_vsi_list`:

ice_add_update_vsi_list
=======================

.. c:function:: enum ice_status ice_add_update_vsi_list(struct ice_hw *hw, struct ice_fltr_mgmt_list_entry *m_entry, struct ice_fltr_info *cur_fltr, struct ice_fltr_info *new_fltr)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param m_entry:
        pointer to current filter management list entry
    :type m_entry: struct ice_fltr_mgmt_list_entry \*

    :param cur_fltr:
        filter information from the book keeping entry
    :type cur_fltr: struct ice_fltr_info \*

    :param new_fltr:
        filter information with the new VSI to be added
    :type new_fltr: struct ice_fltr_info \*

.. _`ice_add_update_vsi_list.description`:

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

.. _`ice_find_rule_entry`:

ice_find_rule_entry
===================

.. c:function:: struct ice_fltr_mgmt_list_entry *ice_find_rule_entry(struct ice_hw *hw, u8 recp_id, struct ice_fltr_info *f_info)

    Search a rule entry

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param recp_id:
        lookup type for which the specified rule needs to be searched
    :type recp_id: u8

    :param f_info:
        rule information
    :type f_info: struct ice_fltr_info \*

.. _`ice_find_rule_entry.description`:

Description
-----------

Helper function to search for a given rule entry
Returns pointer to entry storing the rule if found

.. _`ice_find_vsi_list_entry`:

ice_find_vsi_list_entry
=======================

.. c:function:: struct ice_vsi_list_map_info *ice_find_vsi_list_entry(struct ice_hw *hw, u8 recp_id, u16 vsi_handle, u16 *vsi_list_id)

    Search VSI list map with VSI count 1

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param recp_id:
        lookup type for which VSI lists needs to be searched
    :type recp_id: u8

    :param vsi_handle:
        VSI handle to be found in VSI list
    :type vsi_handle: u16

    :param vsi_list_id:
        VSI list id found containing vsi_handle
    :type vsi_list_id: u16 \*

.. _`ice_find_vsi_list_entry.description`:

Description
-----------

Helper function to search a VSI list with single entry containing given VSI
handle element. This can be extended further to search VSI list with more
than 1 vsi_count. Returns pointer to VSI list entry if found.

.. _`ice_add_rule_internal`:

ice_add_rule_internal
=====================

.. c:function:: enum ice_status ice_add_rule_internal(struct ice_hw *hw, u8 recp_id, struct ice_fltr_list_entry *f_entry)

    add rule for a given lookup type

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param recp_id:
        lookup type (recipe id) for which rule has to be added
    :type recp_id: u8

    :param f_entry:
        structure containing MAC forwarding information
    :type f_entry: struct ice_fltr_list_entry \*

.. _`ice_add_rule_internal.description`:

Description
-----------

Adds or updates the rule lists for a given recipe

.. _`ice_remove_vsi_list_rule`:

ice_remove_vsi_list_rule
========================

.. c:function:: enum ice_status ice_remove_vsi_list_rule(struct ice_hw *hw, u16 vsi_list_id, enum ice_sw_lkup_type lkup_type)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_list_id:
        VSI list id generated as part of allocate resource
    :type vsi_list_id: u16

    :param lkup_type:
        switch rule filter lookup type
    :type lkup_type: enum ice_sw_lkup_type

.. _`ice_remove_vsi_list_rule.description`:

Description
-----------

The VSI list should be emptied before this function is called to remove the
VSI list.

.. _`ice_rem_update_vsi_list`:

ice_rem_update_vsi_list
=======================

.. c:function:: enum ice_status ice_rem_update_vsi_list(struct ice_hw *hw, u16 vsi_handle, struct ice_fltr_mgmt_list_entry *fm_list)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle of the VSI to remove
    :type vsi_handle: u16

    :param fm_list:
        filter management entry for which the VSI list management needs to
        be done
    :type fm_list: struct ice_fltr_mgmt_list_entry \*

.. _`ice_remove_rule_internal`:

ice_remove_rule_internal
========================

.. c:function:: enum ice_status ice_remove_rule_internal(struct ice_hw *hw, u8 recp_id, struct ice_fltr_list_entry *f_entry)

    Remove a filter rule of a given type

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param recp_id:
        recipe id for which the rule needs to removed
    :type recp_id: u8

    :param f_entry:
        rule entry containing filter information
    :type f_entry: struct ice_fltr_list_entry \*

.. _`ice_add_mac`:

ice_add_mac
===========

.. c:function:: enum ice_status ice_add_mac(struct ice_hw *hw, struct list_head *m_list)

    Add a MAC address based filter rule

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param m_list:
        list of MAC addresses and forwarding information
    :type m_list: struct list_head \*

.. _`ice_add_mac.important`:

IMPORTANT
---------

When the ucast_shared flag is set to false and m_list has
multiple unicast addresses, the function assumes that all the
addresses are unique in a given add_mac call. It doesn't
check for duplicates in this case, removing duplicates from a given
list should be taken care of in the caller of this function.

.. _`ice_add_vlan_internal`:

ice_add_vlan_internal
=====================

.. c:function:: enum ice_status ice_add_vlan_internal(struct ice_hw *hw, struct ice_fltr_list_entry *f_entry)

    Add one VLAN based filter rule

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param f_entry:
        filter entry containing one VLAN information
    :type f_entry: struct ice_fltr_list_entry \*

.. _`ice_add_vlan`:

ice_add_vlan
============

.. c:function:: enum ice_status ice_add_vlan(struct ice_hw *hw, struct list_head *v_list)

    Add VLAN based filter rule

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param v_list:
        list of VLAN entries and forwarding information
    :type v_list: struct list_head \*

.. _`ice_rem_sw_rule_info`:

ice_rem_sw_rule_info
====================

.. c:function:: void ice_rem_sw_rule_info(struct ice_hw *hw, struct list_head *rule_head)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param rule_head:
        pointer to the switch list structure that we want to delete
    :type rule_head: struct list_head \*

.. _`ice_cfg_dflt_vsi`:

ice_cfg_dflt_vsi
================

.. c:function:: enum ice_status ice_cfg_dflt_vsi(struct ice_hw *hw, u16 vsi_handle, bool set, u8 direction)

    change state of VSI to set/clear default

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle to set as default
    :type vsi_handle: u16

    :param set:
        true to add the above mentioned switch rule, false to remove it
    :type set: bool

    :param direction:
        ICE_FLTR_RX or ICE_FLTR_TX
    :type direction: u8

.. _`ice_cfg_dflt_vsi.description`:

Description
-----------

add filter rule to set/unset given VSI as default VSI for the switch
(represented by swid)

.. _`ice_remove_mac`:

ice_remove_mac
==============

.. c:function:: enum ice_status ice_remove_mac(struct ice_hw *hw, struct list_head *m_list)

    remove a MAC address based filter rule

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param m_list:
        list of MAC addresses and forwarding information
    :type m_list: struct list_head \*

.. _`ice_remove_mac.description`:

Description
-----------

This function removes either a MAC filter rule or a specific VSI from a
VSI list for a multicast MAC address.

Returns ICE_ERR_DOES_NOT_EXIST if a given entry was not added by
ice_add_mac. Caller should be aware that this call will only work if all
the entries passed into m_list were added previously. It will not attempt to
do a partial remove of entries that were found.

.. _`ice_remove_vlan`:

ice_remove_vlan
===============

.. c:function:: enum ice_status ice_remove_vlan(struct ice_hw *hw, struct list_head *v_list)

    Remove VLAN based filter rule

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param v_list:
        list of VLAN entries and forwarding information
    :type v_list: struct list_head \*

.. _`ice_vsi_uses_fltr`:

ice_vsi_uses_fltr
=================

.. c:function:: bool ice_vsi_uses_fltr(struct ice_fltr_mgmt_list_entry *fm_entry, u16 vsi_handle)

    Determine if given VSI uses specified filter

    :param fm_entry:
        filter entry to inspect
    :type fm_entry: struct ice_fltr_mgmt_list_entry \*

    :param vsi_handle:
        VSI handle to compare with filter info
    :type vsi_handle: u16

.. _`ice_add_entry_to_vsi_fltr_list`:

ice_add_entry_to_vsi_fltr_list
==============================

.. c:function:: enum ice_status ice_add_entry_to_vsi_fltr_list(struct ice_hw *hw, u16 vsi_handle, struct list_head *vsi_list_head, struct ice_fltr_info *fi)

    Add copy of fltr_list_entry to remove list

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle to remove filters from
    :type vsi_handle: u16

    :param vsi_list_head:
        pointer to the list to add entry to
    :type vsi_list_head: struct list_head \*

    :param fi:
        pointer to fltr_info of filter entry to copy & add
    :type fi: struct ice_fltr_info \*

.. _`ice_add_entry_to_vsi_fltr_list.description`:

Description
-----------

Helper function, used when creating a list of filters to remove from
a specific VSI. The entry added to vsi_list_head is a COPY of the
original filter entry, with the exception of fltr_info.fltr_act and
fltr_info.fwd_id fields. These are set such that later logic can
extract which VSI to remove the fltr from, and pass on that information.

.. _`ice_add_to_vsi_fltr_list`:

ice_add_to_vsi_fltr_list
========================

.. c:function:: enum ice_status ice_add_to_vsi_fltr_list(struct ice_hw *hw, u16 vsi_handle, struct list_head *lkup_list_head, struct list_head *vsi_list_head)

    Add VSI filters to the list

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle to remove filters from
    :type vsi_handle: u16

    :param lkup_list_head:
        pointer to the list that has certain lookup type filters
    :type lkup_list_head: struct list_head \*

    :param vsi_list_head:
        pointer to the list pertaining to VSI with vsi_handle
    :type vsi_list_head: struct list_head \*

.. _`ice_add_to_vsi_fltr_list.description`:

Description
-----------

Locates all filters in lkup_list_head that are used by the given VSI,
and adds COPIES of those entries to vsi_list_head (intended to be used
to remove the listed filters).
Note that this means all entries in vsi_list_head must be explicitly
deallocated by the caller when done with list.

.. _`ice_remove_vsi_lkup_fltr`:

ice_remove_vsi_lkup_fltr
========================

.. c:function:: void ice_remove_vsi_lkup_fltr(struct ice_hw *hw, u16 vsi_handle, enum ice_sw_lkup_type lkup)

    Remove lookup type filters for a VSI

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle to remove filters from
    :type vsi_handle: u16

    :param lkup:
        switch rule filter lookup type
    :type lkup: enum ice_sw_lkup_type

.. _`ice_remove_vsi_fltr`:

ice_remove_vsi_fltr
===================

.. c:function:: void ice_remove_vsi_fltr(struct ice_hw *hw, u16 vsi_handle)

    Remove all filters for a VSI

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        VSI handle to remove filters from
    :type vsi_handle: u16

.. _`ice_replay_vsi_fltr`:

ice_replay_vsi_fltr
===================

.. c:function:: enum ice_status ice_replay_vsi_fltr(struct ice_hw *hw, u16 vsi_handle, u8 recp_id, struct list_head *list_head)

    Replay filters for requested VSI

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        driver VSI handle
    :type vsi_handle: u16

    :param recp_id:
        Recipe id for which rules need to be replayed
    :type recp_id: u8

    :param list_head:
        list for which filters need to be replayed
    :type list_head: struct list_head \*

.. _`ice_replay_vsi_fltr.description`:

Description
-----------

Replays the filter of recipe recp_id for a VSI represented via vsi_handle.
It is required to pass valid VSI handle.

.. _`ice_replay_vsi_all_fltr`:

ice_replay_vsi_all_fltr
=======================

.. c:function:: enum ice_status ice_replay_vsi_all_fltr(struct ice_hw *hw, u16 vsi_handle)

    replay all filters stored in bookkeeping lists

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        driver VSI handle
    :type vsi_handle: u16

.. _`ice_replay_vsi_all_fltr.description`:

Description
-----------

Replays filters for requested VSI via vsi_handle.

.. _`ice_rm_all_sw_replay_rule_info`:

ice_rm_all_sw_replay_rule_info
==============================

.. c:function:: void ice_rm_all_sw_replay_rule_info(struct ice_hw *hw)

    deletes filter replay rules

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_rm_all_sw_replay_rule_info.description`:

Description
-----------

Deletes the filter replay rules.

.. This file was automatic generated / don't edit.

