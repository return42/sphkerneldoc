.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_sched.c

.. _`ice_sched_add_root_node`:

ice_sched_add_root_node
=======================

.. c:function:: enum ice_status ice_sched_add_root_node(struct ice_port_info *pi, struct ice_aqc_txsched_elem_data *info)

    Insert the Tx scheduler root node in SW DB

    :param struct ice_port_info \*pi:
        port information structure

    :param struct ice_aqc_txsched_elem_data \*info:
        Scheduler element information from firmware

.. _`ice_sched_add_root_node.description`:

Description
-----------

This function inserts the root node of the scheduling tree topology
to the SW DB.

.. _`ice_sched_find_node_by_teid`:

ice_sched_find_node_by_teid
===========================

.. c:function:: struct ice_sched_node *ice_sched_find_node_by_teid(struct ice_sched_node *start_node, u32 teid)

    Find the Tx scheduler node in SW DB

    :param struct ice_sched_node \*start_node:
        pointer to the starting ice_sched_node struct in a sub-tree

    :param u32 teid:
        node teid to search

.. _`ice_sched_find_node_by_teid.description`:

Description
-----------

This function searches for a node matching the teid in the scheduling tree
from the SW DB. The search is recursive and is restricted by the number of
layers it has searched through; stopping at the max supported layer.

This function needs to be called when holding the port_info->sched_lock

.. _`ice_sched_add_node`:

ice_sched_add_node
==================

.. c:function:: enum ice_status ice_sched_add_node(struct ice_port_info *pi, u8 layer, struct ice_aqc_txsched_elem_data *info)

    Insert the Tx scheduler node in SW DB

    :param struct ice_port_info \*pi:
        port information structure

    :param u8 layer:
        Scheduler layer of the node

    :param struct ice_aqc_txsched_elem_data \*info:
        Scheduler element information from firmware

.. _`ice_sched_add_node.description`:

Description
-----------

This function inserts a scheduler node to the SW DB.

.. _`ice_aq_delete_sched_elems`:

ice_aq_delete_sched_elems
=========================

.. c:function:: enum ice_status ice_aq_delete_sched_elems(struct ice_hw *hw, u16 grps_req, struct ice_aqc_delete_elem *buf, u16 buf_size, u16 *grps_del, struct ice_sq_cd *cd)

    delete scheduler elements

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 grps_req:
        number of groups to delete

    :param struct ice_aqc_delete_elem \*buf:
        pointer to buffer

    :param u16 buf_size:
        buffer size in bytes

    :param u16 \*grps_del:
        returns total number of elements deleted

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_delete_sched_elems.description`:

Description
-----------

Delete scheduling elements (0x040F)

.. _`ice_sched_remove_elems`:

ice_sched_remove_elems
======================

.. c:function:: enum ice_status ice_sched_remove_elems(struct ice_hw *hw, struct ice_sched_node *parent, u16 num_nodes, u32 *node_teids)

    remove nodes from hw

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_sched_node \*parent:
        pointer to the parent node

    :param u16 num_nodes:
        number of nodes

    :param u32 \*node_teids:
        array of node teids to be deleted

.. _`ice_sched_remove_elems.description`:

Description
-----------

This function remove nodes from hw

.. _`ice_sched_get_first_node`:

ice_sched_get_first_node
========================

.. c:function:: struct ice_sched_node *ice_sched_get_first_node(struct ice_hw *hw, struct ice_sched_node *parent, u8 layer)

    get the first node of the given layer

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_sched_node \*parent:
        pointer the base node of the subtree

    :param u8 layer:
        layer number

.. _`ice_sched_get_first_node.description`:

Description
-----------

This function retrieves the first node of the given layer from the subtree

.. _`ice_sched_get_tc_node`:

ice_sched_get_tc_node
=====================

.. c:function:: struct ice_sched_node *ice_sched_get_tc_node(struct ice_port_info *pi, u8 tc)

    get pointer to TC node

    :param struct ice_port_info \*pi:
        port information structure

    :param u8 tc:
        TC number

.. _`ice_sched_get_tc_node.description`:

Description
-----------

This function returns the TC node pointer

.. _`ice_free_sched_node`:

ice_free_sched_node
===================

.. c:function:: void ice_free_sched_node(struct ice_port_info *pi, struct ice_sched_node *node)

    Free a Tx scheduler node from SW DB

    :param struct ice_port_info \*pi:
        port information structure

    :param struct ice_sched_node \*node:
        pointer to the ice_sched_node struct

.. _`ice_free_sched_node.description`:

Description
-----------

This function frees up a node from SW DB as well as from HW

This function needs to be called with the port_info->sched_lock held

.. _`ice_aq_get_dflt_topo`:

ice_aq_get_dflt_topo
====================

.. c:function:: enum ice_status ice_aq_get_dflt_topo(struct ice_hw *hw, u8 lport, struct ice_aqc_get_topo_elem *buf, u16 buf_size, u8 *num_branches, struct ice_sq_cd *cd)

    gets default scheduler topology

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u8 lport:
        logical port number

    :param struct ice_aqc_get_topo_elem \*buf:
        pointer to buffer

    :param u16 buf_size:
        buffer size in bytes

    :param u8 \*num_branches:
        returns total number of queue to port branches

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_get_dflt_topo.description`:

Description
-----------

Get default scheduler topology (0x400)

.. _`ice_aq_add_sched_elems`:

ice_aq_add_sched_elems
======================

.. c:function:: enum ice_status ice_aq_add_sched_elems(struct ice_hw *hw, u16 grps_req, struct ice_aqc_add_elem *buf, u16 buf_size, u16 *grps_added, struct ice_sq_cd *cd)

    adds scheduling element

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 grps_req:
        the number of groups that are requested to be added

    :param struct ice_aqc_add_elem \*buf:
        pointer to buffer

    :param u16 buf_size:
        buffer size in bytes

    :param u16 \*grps_added:
        returns total number of groups added

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_add_sched_elems.description`:

Description
-----------

Add scheduling elements (0x0401)

.. _`ice_suspend_resume_elems`:

ice_suspend_resume_elems
========================

.. c:function:: enum ice_status ice_suspend_resume_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_suspend_resume_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd, enum ice_adminq_opc cmd_code)

    suspend/resume scheduler elements

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 elems_req:
        number of elements to suspend

    :param struct ice_aqc_suspend_resume_elem \*buf:
        pointer to buffer

    :param u16 buf_size:
        buffer size in bytes

    :param u16 \*elems_ret:
        returns total number of elements suspended

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

    :param enum ice_adminq_opc cmd_code:
        command code for suspend or resume

.. _`ice_suspend_resume_elems.description`:

Description
-----------

suspend/resume scheduler elements

.. _`ice_aq_suspend_sched_elems`:

ice_aq_suspend_sched_elems
==========================

.. c:function:: enum ice_status ice_aq_suspend_sched_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_suspend_resume_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd)

    suspend scheduler elements

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 elems_req:
        number of elements to suspend

    :param struct ice_aqc_suspend_resume_elem \*buf:
        pointer to buffer

    :param u16 buf_size:
        buffer size in bytes

    :param u16 \*elems_ret:
        returns total number of elements suspended

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_suspend_sched_elems.description`:

Description
-----------

Suspend scheduling elements (0x0409)

.. _`ice_aq_resume_sched_elems`:

ice_aq_resume_sched_elems
=========================

.. c:function:: enum ice_status ice_aq_resume_sched_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_suspend_resume_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd)

    resume scheduler elements

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 elems_req:
        number of elements to resume

    :param struct ice_aqc_suspend_resume_elem \*buf:
        pointer to buffer

    :param u16 buf_size:
        buffer size in bytes

    :param u16 \*elems_ret:
        returns total number of elements resumed

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_resume_sched_elems.description`:

Description
-----------

resume scheduling elements (0x040A)

.. _`ice_aq_query_sched_res`:

ice_aq_query_sched_res
======================

.. c:function:: enum ice_status ice_aq_query_sched_res(struct ice_hw *hw, u16 buf_size, struct ice_aqc_query_txsched_res_resp *buf, struct ice_sq_cd *cd)

    query scheduler resource

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 buf_size:
        buffer size in bytes

    :param struct ice_aqc_query_txsched_res_resp \*buf:
        pointer to buffer

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_query_sched_res.description`:

Description
-----------

Query scheduler resource allocation (0x0412)

.. _`ice_sched_suspend_resume_elems`:

ice_sched_suspend_resume_elems
==============================

.. c:function:: enum ice_status ice_sched_suspend_resume_elems(struct ice_hw *hw, u8 num_nodes, u32 *node_teids, bool suspend)

    suspend or resume hw nodes

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u8 num_nodes:
        number of nodes

    :param u32 \*node_teids:
        array of node teids to be suspended or resumed

    :param bool suspend:
        true means suspend / false means resume

.. _`ice_sched_suspend_resume_elems.description`:

Description
-----------

This function suspends or resumes hw nodes

.. _`ice_sched_clear_tx_topo`:

ice_sched_clear_tx_topo
=======================

.. c:function:: void ice_sched_clear_tx_topo(struct ice_port_info *pi)

    clears the schduler tree nodes

    :param struct ice_port_info \*pi:
        port information structure

.. _`ice_sched_clear_tx_topo.description`:

Description
-----------

This function removes all the nodes from HW as well as from SW DB.

.. _`ice_sched_clear_port`:

ice_sched_clear_port
====================

.. c:function:: void ice_sched_clear_port(struct ice_port_info *pi)

    clear the scheduler elements from SW DB for a port

    :param struct ice_port_info \*pi:
        port information structure

.. _`ice_sched_clear_port.description`:

Description
-----------

Cleanup scheduling elements from SW DB

.. _`ice_sched_cleanup_all`:

ice_sched_cleanup_all
=====================

.. c:function:: void ice_sched_cleanup_all(struct ice_hw *hw)

    cleanup scheduler elements from SW DB for all ports

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_sched_cleanup_all.description`:

Description
-----------

Cleanup scheduling elements from SW DB for all the ports

.. _`ice_sched_create_vsi_info_entry`:

ice_sched_create_vsi_info_entry
===============================

.. c:function:: struct ice_sched_vsi_info *ice_sched_create_vsi_info_entry(struct ice_port_info *pi, u16 vsi_id)

    create an empty new VSI entry

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

.. _`ice_sched_create_vsi_info_entry.description`:

Description
-----------

This function creates a new VSI entry and adds it to list

.. _`ice_sched_add_elems`:

ice_sched_add_elems
===================

.. c:function:: enum ice_status ice_sched_add_elems(struct ice_port_info *pi, struct ice_sched_node *tc_node, struct ice_sched_node *parent, u8 layer, u16 num_nodes, u16 *num_nodes_added, u32 *first_node_teid)

    add nodes to hw and SW DB

    :param struct ice_port_info \*pi:
        port information structure

    :param struct ice_sched_node \*tc_node:
        pointer to the branch node

    :param struct ice_sched_node \*parent:
        pointer to the parent node

    :param u8 layer:
        layer number to add nodes

    :param u16 num_nodes:
        number of nodes

    :param u16 \*num_nodes_added:
        pointer to num nodes added

    :param u32 \*first_node_teid:
        if new nodes are added then return the teid of first node

.. _`ice_sched_add_elems.description`:

Description
-----------

This function add nodes to hw as well as to SW DB for a given layer

.. _`ice_sched_add_nodes_to_layer`:

ice_sched_add_nodes_to_layer
============================

.. c:function:: enum ice_status ice_sched_add_nodes_to_layer(struct ice_port_info *pi, struct ice_sched_node *tc_node, struct ice_sched_node *parent, u8 layer, u16 num_nodes, u32 *first_node_teid, u16 *num_nodes_added)

    Add nodes to a given layer

    :param struct ice_port_info \*pi:
        port information structure

    :param struct ice_sched_node \*tc_node:
        pointer to TC node

    :param struct ice_sched_node \*parent:
        pointer to parent node

    :param u8 layer:
        layer number to add nodes

    :param u16 num_nodes:
        number of nodes to be added

    :param u32 \*first_node_teid:
        pointer to the first node teid

    :param u16 \*num_nodes_added:
        pointer to number of nodes added

.. _`ice_sched_add_nodes_to_layer.description`:

Description
-----------

This function add nodes to a given layer.

.. _`ice_sched_get_qgrp_layer`:

ice_sched_get_qgrp_layer
========================

.. c:function:: u8 ice_sched_get_qgrp_layer(struct ice_hw *hw)

    get the current queue group layer number

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_sched_get_qgrp_layer.description`:

Description
-----------

This function returns the current queue group layer number

.. _`ice_sched_get_vsi_layer`:

ice_sched_get_vsi_layer
=======================

.. c:function:: u8 ice_sched_get_vsi_layer(struct ice_hw *hw)

    get the current VSI layer number

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_sched_get_vsi_layer.description`:

Description
-----------

This function returns the current VSI layer number

.. _`ice_sched_get_num_nodes_per_layer`:

ice_sched_get_num_nodes_per_layer
=================================

.. c:function:: u16 ice_sched_get_num_nodes_per_layer(struct ice_port_info *pi, u8 layer)

    Get the total number of nodes per layer

    :param struct ice_port_info \*pi:
        pointer to the port info struct

    :param u8 layer:
        layer number

.. _`ice_sched_get_num_nodes_per_layer.description`:

Description
-----------

This function calculates the number of nodes present in the scheduler tree
including all the branches for a given layer

.. _`ice_sched_validate_for_max_nodes`:

ice_sched_validate_for_max_nodes
================================

.. c:function:: enum ice_status ice_sched_validate_for_max_nodes(struct ice_port_info *pi, u16 *new_num_nodes_per_layer)

    check max number of nodes reached or not

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 \*new_num_nodes_per_layer:
        pointer to the new number of nodes array

.. _`ice_sched_validate_for_max_nodes.description`:

Description
-----------

This function checks whether the scheduler tree layers have enough space to
add new nodes

.. _`ice_rm_dflt_leaf_node`:

ice_rm_dflt_leaf_node
=====================

.. c:function:: void ice_rm_dflt_leaf_node(struct ice_port_info *pi)

    remove the default leaf node in the tree

    :param struct ice_port_info \*pi:
        port information structure

.. _`ice_rm_dflt_leaf_node.description`:

Description
-----------

This function removes the leaf node that was created by the FW
during initialization

.. _`ice_sched_rm_dflt_nodes`:

ice_sched_rm_dflt_nodes
=======================

.. c:function:: void ice_sched_rm_dflt_nodes(struct ice_port_info *pi)

    free the default nodes in the tree

    :param struct ice_port_info \*pi:
        port information structure

.. _`ice_sched_rm_dflt_nodes.description`:

Description
-----------

This function frees all the nodes except root and TC that were created by
the FW during initialization

.. _`ice_sched_init_port`:

ice_sched_init_port
===================

.. c:function:: enum ice_status ice_sched_init_port(struct ice_port_info *pi)

    Initialize scheduler by querying information from FW

    :param struct ice_port_info \*pi:
        port info structure for the tree to cleanup

.. _`ice_sched_init_port.description`:

Description
-----------

This function is the initial call to find the total number of Tx scheduler
resources, default topology created by firmware and storing the information
in SW DB.

.. _`ice_sched_query_res_alloc`:

ice_sched_query_res_alloc
=========================

.. c:function:: enum ice_status ice_sched_query_res_alloc(struct ice_hw *hw)

    query the FW for num of logical sched layers

    :param struct ice_hw \*hw:
        pointer to the HW struct

.. _`ice_sched_query_res_alloc.description`:

Description
-----------

query FW for allocated scheduler resources and store in HW struct

.. _`ice_sched_get_vsi_info_entry`:

ice_sched_get_vsi_info_entry
============================

.. c:function:: struct ice_sched_vsi_info *ice_sched_get_vsi_info_entry(struct ice_port_info *pi, u16 vsi_id)

    Get the vsi entry list for given vsi_id

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        vsi id

.. _`ice_sched_get_vsi_info_entry.description`:

Description
-----------

This function retrieves the vsi list for the given vsi id

.. _`ice_sched_find_node_in_subtree`:

ice_sched_find_node_in_subtree
==============================

.. c:function:: bool ice_sched_find_node_in_subtree(struct ice_hw *hw, struct ice_sched_node *base, struct ice_sched_node *node)

    Find node in part of base node subtree

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_sched_node \*base:
        pointer to the base node

    :param struct ice_sched_node \*node:
        pointer to the node to search

.. _`ice_sched_find_node_in_subtree.description`:

Description
-----------

This function checks whether a given node is part of the base node
subtree or not

.. _`ice_sched_get_free_qparent`:

ice_sched_get_free_qparent
==========================

.. c:function:: struct ice_sched_node *ice_sched_get_free_qparent(struct ice_port_info *pi, u16 vsi_id, u8 tc, u8 owner)

    Get a free lan or rdma q group node

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        vsi id

    :param u8 tc:
        branch number

    :param u8 owner:
        lan or rdma

.. _`ice_sched_get_free_qparent.description`:

Description
-----------

This function retrieves a free lan or rdma q group node

.. _`ice_sched_get_vsi_node`:

ice_sched_get_vsi_node
======================

.. c:function:: struct ice_sched_node *ice_sched_get_vsi_node(struct ice_hw *hw, struct ice_sched_node *tc_node, u16 vsi_id)

    Get a VSI node based on VSI id

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_sched_node \*tc_node:
        pointer to the TC node

    :param u16 vsi_id:
        VSI id

.. _`ice_sched_get_vsi_node.description`:

Description
-----------

This function retrieves a VSI node for a given VSI id from a given
TC branch

.. _`ice_sched_calc_vsi_child_nodes`:

ice_sched_calc_vsi_child_nodes
==============================

.. c:function:: void ice_sched_calc_vsi_child_nodes(struct ice_hw *hw, u16 num_qs, u16 *num_nodes)

    calculate number of VSI child nodes

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 num_qs:
        number of queues

    :param u16 \*num_nodes:
        num nodes array

.. _`ice_sched_calc_vsi_child_nodes.description`:

Description
-----------

This function calculates the number of VSI child nodes based on the
number of queues.

.. _`ice_sched_add_vsi_child_nodes`:

ice_sched_add_vsi_child_nodes
=============================

.. c:function:: enum ice_status ice_sched_add_vsi_child_nodes(struct ice_port_info *pi, u16 vsi_id, struct ice_sched_node *tc_node, u16 *num_nodes, u8 owner)

    add VSI child nodes to tree

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI id

    :param struct ice_sched_node \*tc_node:
        pointer to the TC node

    :param u16 \*num_nodes:
        pointer to the num nodes that needs to be added per layer

    :param u8 owner:
        node owner (lan or rdma)

.. _`ice_sched_add_vsi_child_nodes.description`:

Description
-----------

This function adds the VSI child nodes to tree. It gets called for
lan and rdma separately.

.. _`ice_sched_rm_vsi_child_nodes`:

ice_sched_rm_vsi_child_nodes
============================

.. c:function:: void ice_sched_rm_vsi_child_nodes(struct ice_port_info *pi, struct ice_sched_node *vsi_node, u16 *num_nodes, u8 owner)

    remove VSI child nodes from the tree

    :param struct ice_port_info \*pi:
        port information structure

    :param struct ice_sched_node \*vsi_node:
        pointer to the VSI node

    :param u16 \*num_nodes:
        pointer to the num nodes that needs to be removed per layer

    :param u8 owner:
        node owner (lan or rdma)

.. _`ice_sched_rm_vsi_child_nodes.description`:

Description
-----------

This function removes the VSI child nodes from the tree. It gets called for
lan and rdma separately.

.. _`ice_sched_calc_vsi_support_nodes`:

ice_sched_calc_vsi_support_nodes
================================

.. c:function:: void ice_sched_calc_vsi_support_nodes(struct ice_hw *hw, struct ice_sched_node *tc_node, u16 *num_nodes)

    calculate number of VSI support nodes

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_sched_node \*tc_node:
        pointer to TC node

    :param u16 \*num_nodes:
        pointer to num nodes array

.. _`ice_sched_calc_vsi_support_nodes.description`:

Description
-----------

This function calculates the number of supported nodes needed to add this
VSI into tx tree including the VSI, parent and intermediate nodes in below
layers

.. _`ice_sched_add_vsi_support_nodes`:

ice_sched_add_vsi_support_nodes
===============================

.. c:function:: enum ice_status ice_sched_add_vsi_support_nodes(struct ice_port_info *pi, u16 vsi_id, struct ice_sched_node *tc_node, u16 *num_nodes)

    add VSI supported nodes into tx tree

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

    :param struct ice_sched_node \*tc_node:
        pointer to TC node

    :param u16 \*num_nodes:
        pointer to num nodes array

.. _`ice_sched_add_vsi_support_nodes.description`:

Description
-----------

This function adds the VSI supported nodes into tx tree including the
VSI, its parent and intermediate nodes in below layers

.. _`ice_sched_add_vsi_to_topo`:

ice_sched_add_vsi_to_topo
=========================

.. c:function:: enum ice_status ice_sched_add_vsi_to_topo(struct ice_port_info *pi, u16 vsi_id, u8 tc)

    add a new VSI into tree

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

    :param u8 tc:
        TC number

.. _`ice_sched_add_vsi_to_topo.description`:

Description
-----------

This function adds a new VSI into scheduler tree

.. _`ice_sched_update_vsi_child_nodes`:

ice_sched_update_vsi_child_nodes
================================

.. c:function:: enum ice_status ice_sched_update_vsi_child_nodes(struct ice_port_info *pi, u16 vsi_id, u8 tc, u16 new_numqs, u8 owner)

    update VSI child nodes

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

    :param u8 tc:
        TC number

    :param u16 new_numqs:
        new number of max queues

    :param u8 owner:
        owner of this subtree

.. _`ice_sched_update_vsi_child_nodes.description`:

Description
-----------

This function updates the VSI child nodes based on the number of queues

.. _`ice_sched_cfg_vsi`:

ice_sched_cfg_vsi
=================

.. c:function:: enum ice_status ice_sched_cfg_vsi(struct ice_port_info *pi, u16 vsi_id, u8 tc, u16 maxqs, u8 owner, bool enable)

    configure the new/exisiting VSI

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

    :param u8 tc:
        TC number

    :param u16 maxqs:
        max number of queues

    :param u8 owner:
        lan or rdma

    :param bool enable:
        TC enabled or disabled

.. _`ice_sched_cfg_vsi.description`:

Description
-----------

This function adds/updates VSI nodes based on the number of queues. If TC is
enabled and VSI is in suspended state then resume the VSI back. If TC is
disabled then suspend the VSI if it is not already.

.. This file was automatic generated / don't edit.

