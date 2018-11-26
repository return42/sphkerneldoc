.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_sched.c

.. _`ice_sched_add_root_node`:

ice_sched_add_root_node
=======================

.. c:function:: enum ice_status ice_sched_add_root_node(struct ice_port_info *pi, struct ice_aqc_txsched_elem_data *info)

    Insert the Tx scheduler root node in SW DB

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param info:
        Scheduler element information from firmware
    :type info: struct ice_aqc_txsched_elem_data \*

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

    :param start_node:
        pointer to the starting ice_sched_node struct in a sub-tree
    :type start_node: struct ice_sched_node \*

    :param teid:
        node teid to search
    :type teid: u32

.. _`ice_sched_find_node_by_teid.description`:

Description
-----------

This function searches for a node matching the teid in the scheduling tree
from the SW DB. The search is recursive and is restricted by the number of
layers it has searched through; stopping at the max supported layer.

This function needs to be called when holding the port_info->sched_lock

.. _`ice_aq_query_sched_elems`:

ice_aq_query_sched_elems
========================

.. c:function:: enum ice_status ice_aq_query_sched_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_get_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd)

    query scheduler elements

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param elems_req:
        number of elements to query
    :type elems_req: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_get_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param elems_ret:
        returns total number of elements returned
    :type elems_ret: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_query_sched_elems.description`:

Description
-----------

Query scheduling elements (0x0404)

.. _`ice_sched_query_elem`:

ice_sched_query_elem
====================

.. c:function:: enum ice_status ice_sched_query_elem(struct ice_hw *hw, u32 node_teid, struct ice_aqc_get_elem *buf)

    query element information from hw

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param node_teid:
        node teid to be queried
    :type node_teid: u32

    :param buf:
        buffer to element information
    :type buf: struct ice_aqc_get_elem \*

.. _`ice_sched_query_elem.description`:

Description
-----------

This function queries HW element information

.. _`ice_sched_add_node`:

ice_sched_add_node
==================

.. c:function:: enum ice_status ice_sched_add_node(struct ice_port_info *pi, u8 layer, struct ice_aqc_txsched_elem_data *info)

    Insert the Tx scheduler node in SW DB

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param layer:
        Scheduler layer of the node
    :type layer: u8

    :param info:
        Scheduler element information from firmware
    :type info: struct ice_aqc_txsched_elem_data \*

.. _`ice_sched_add_node.description`:

Description
-----------

This function inserts a scheduler node to the SW DB.

.. _`ice_aq_delete_sched_elems`:

ice_aq_delete_sched_elems
=========================

.. c:function:: enum ice_status ice_aq_delete_sched_elems(struct ice_hw *hw, u16 grps_req, struct ice_aqc_delete_elem *buf, u16 buf_size, u16 *grps_del, struct ice_sq_cd *cd)

    delete scheduler elements

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param grps_req:
        number of groups to delete
    :type grps_req: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_delete_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param grps_del:
        returns total number of elements deleted
    :type grps_del: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_delete_sched_elems.description`:

Description
-----------

Delete scheduling elements (0x040F)

.. _`ice_sched_remove_elems`:

ice_sched_remove_elems
======================

.. c:function:: enum ice_status ice_sched_remove_elems(struct ice_hw *hw, struct ice_sched_node *parent, u16 num_nodes, u32 *node_teids)

    remove nodes from hw

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param parent:
        pointer to the parent node
    :type parent: struct ice_sched_node \*

    :param num_nodes:
        number of nodes
    :type num_nodes: u16

    :param node_teids:
        array of node teids to be deleted
    :type node_teids: u32 \*

.. _`ice_sched_remove_elems.description`:

Description
-----------

This function remove nodes from hw

.. _`ice_sched_get_first_node`:

ice_sched_get_first_node
========================

.. c:function:: struct ice_sched_node *ice_sched_get_first_node(struct ice_hw *hw, struct ice_sched_node *parent, u8 layer)

    get the first node of the given layer

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param parent:
        pointer the base node of the subtree
    :type parent: struct ice_sched_node \*

    :param layer:
        layer number
    :type layer: u8

.. _`ice_sched_get_first_node.description`:

Description
-----------

This function retrieves the first node of the given layer from the subtree

.. _`ice_sched_get_tc_node`:

ice_sched_get_tc_node
=====================

.. c:function:: struct ice_sched_node *ice_sched_get_tc_node(struct ice_port_info *pi, u8 tc)

    get pointer to TC node

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param tc:
        TC number
    :type tc: u8

.. _`ice_sched_get_tc_node.description`:

Description
-----------

This function returns the TC node pointer

.. _`ice_free_sched_node`:

ice_free_sched_node
===================

.. c:function:: void ice_free_sched_node(struct ice_port_info *pi, struct ice_sched_node *node)

    Free a Tx scheduler node from SW DB

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param node:
        pointer to the ice_sched_node struct
    :type node: struct ice_sched_node \*

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

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param lport:
        logical port number
    :type lport: u8

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_get_topo_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param num_branches:
        returns total number of queue to port branches
    :type num_branches: u8 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_get_dflt_topo.description`:

Description
-----------

Get default scheduler topology (0x400)

.. _`ice_aq_add_sched_elems`:

ice_aq_add_sched_elems
======================

.. c:function:: enum ice_status ice_aq_add_sched_elems(struct ice_hw *hw, u16 grps_req, struct ice_aqc_add_elem *buf, u16 buf_size, u16 *grps_added, struct ice_sq_cd *cd)

    adds scheduling element

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param grps_req:
        the number of groups that are requested to be added
    :type grps_req: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_add_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param grps_added:
        returns total number of groups added
    :type grps_added: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_add_sched_elems.description`:

Description
-----------

Add scheduling elements (0x0401)

.. _`ice_suspend_resume_elems`:

ice_suspend_resume_elems
========================

.. c:function:: enum ice_status ice_suspend_resume_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_suspend_resume_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd, enum ice_adminq_opc cmd_code)

    suspend/resume scheduler elements

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param elems_req:
        number of elements to suspend
    :type elems_req: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_suspend_resume_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param elems_ret:
        returns total number of elements suspended
    :type elems_ret: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

    :param cmd_code:
        command code for suspend or resume
    :type cmd_code: enum ice_adminq_opc

.. _`ice_suspend_resume_elems.description`:

Description
-----------

suspend/resume scheduler elements

.. _`ice_aq_suspend_sched_elems`:

ice_aq_suspend_sched_elems
==========================

.. c:function:: enum ice_status ice_aq_suspend_sched_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_suspend_resume_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd)

    suspend scheduler elements

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param elems_req:
        number of elements to suspend
    :type elems_req: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_suspend_resume_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param elems_ret:
        returns total number of elements suspended
    :type elems_ret: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_suspend_sched_elems.description`:

Description
-----------

Suspend scheduling elements (0x0409)

.. _`ice_aq_resume_sched_elems`:

ice_aq_resume_sched_elems
=========================

.. c:function:: enum ice_status ice_aq_resume_sched_elems(struct ice_hw *hw, u16 elems_req, struct ice_aqc_suspend_resume_elem *buf, u16 buf_size, u16 *elems_ret, struct ice_sq_cd *cd)

    resume scheduler elements

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param elems_req:
        number of elements to resume
    :type elems_req: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_suspend_resume_elem \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param elems_ret:
        returns total number of elements resumed
    :type elems_ret: u16 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_resume_sched_elems.description`:

Description
-----------

resume scheduling elements (0x040A)

.. _`ice_aq_query_sched_res`:

ice_aq_query_sched_res
======================

.. c:function:: enum ice_status ice_aq_query_sched_res(struct ice_hw *hw, u16 buf_size, struct ice_aqc_query_txsched_res_resp *buf, struct ice_sq_cd *cd)

    query scheduler resource

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param buf_size:
        buffer size in bytes
    :type buf_size: u16

    :param buf:
        pointer to buffer
    :type buf: struct ice_aqc_query_txsched_res_resp \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_query_sched_res.description`:

Description
-----------

Query scheduler resource allocation (0x0412)

.. _`ice_sched_suspend_resume_elems`:

ice_sched_suspend_resume_elems
==============================

.. c:function:: enum ice_status ice_sched_suspend_resume_elems(struct ice_hw *hw, u8 num_nodes, u32 *node_teids, bool suspend)

    suspend or resume hw nodes

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param num_nodes:
        number of nodes
    :type num_nodes: u8

    :param node_teids:
        array of node teids to be suspended or resumed
    :type node_teids: u32 \*

    :param suspend:
        true means suspend / false means resume
    :type suspend: bool

.. _`ice_sched_suspend_resume_elems.description`:

Description
-----------

This function suspends or resumes hw nodes

.. _`ice_sched_clear_tx_topo`:

ice_sched_clear_tx_topo
=======================

.. c:function:: void ice_sched_clear_tx_topo(struct ice_port_info *pi)

    clears the schduler tree nodes

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

.. _`ice_sched_clear_tx_topo.description`:

Description
-----------

This function removes all the nodes from HW as well as from SW DB.

.. _`ice_sched_clear_port`:

ice_sched_clear_port
====================

.. c:function:: void ice_sched_clear_port(struct ice_port_info *pi)

    clear the scheduler elements from SW DB for a port

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

.. _`ice_sched_clear_port.description`:

Description
-----------

Cleanup scheduling elements from SW DB

.. _`ice_sched_cleanup_all`:

ice_sched_cleanup_all
=====================

.. c:function:: void ice_sched_cleanup_all(struct ice_hw *hw)

    cleanup scheduler elements from SW DB for all ports

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_sched_cleanup_all.description`:

Description
-----------

Cleanup scheduling elements from SW DB for all the ports

.. _`ice_sched_add_elems`:

ice_sched_add_elems
===================

.. c:function:: enum ice_status ice_sched_add_elems(struct ice_port_info *pi, struct ice_sched_node *tc_node, struct ice_sched_node *parent, u8 layer, u16 num_nodes, u16 *num_nodes_added, u32 *first_node_teid)

    add nodes to hw and SW DB

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param tc_node:
        pointer to the branch node
    :type tc_node: struct ice_sched_node \*

    :param parent:
        pointer to the parent node
    :type parent: struct ice_sched_node \*

    :param layer:
        layer number to add nodes
    :type layer: u8

    :param num_nodes:
        number of nodes
    :type num_nodes: u16

    :param num_nodes_added:
        pointer to num nodes added
    :type num_nodes_added: u16 \*

    :param first_node_teid:
        if new nodes are added then return the teid of first node
    :type first_node_teid: u32 \*

.. _`ice_sched_add_elems.description`:

Description
-----------

This function add nodes to hw as well as to SW DB for a given layer

.. _`ice_sched_add_nodes_to_layer`:

ice_sched_add_nodes_to_layer
============================

.. c:function:: enum ice_status ice_sched_add_nodes_to_layer(struct ice_port_info *pi, struct ice_sched_node *tc_node, struct ice_sched_node *parent, u8 layer, u16 num_nodes, u32 *first_node_teid, u16 *num_nodes_added)

    Add nodes to a given layer

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param tc_node:
        pointer to TC node
    :type tc_node: struct ice_sched_node \*

    :param parent:
        pointer to parent node
    :type parent: struct ice_sched_node \*

    :param layer:
        layer number to add nodes
    :type layer: u8

    :param num_nodes:
        number of nodes to be added
    :type num_nodes: u16

    :param first_node_teid:
        pointer to the first node teid
    :type first_node_teid: u32 \*

    :param num_nodes_added:
        pointer to number of nodes added
    :type num_nodes_added: u16 \*

.. _`ice_sched_add_nodes_to_layer.description`:

Description
-----------

This function add nodes to a given layer.

.. _`ice_sched_get_qgrp_layer`:

ice_sched_get_qgrp_layer
========================

.. c:function:: u8 ice_sched_get_qgrp_layer(struct ice_hw *hw)

    get the current queue group layer number

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_sched_get_qgrp_layer.description`:

Description
-----------

This function returns the current queue group layer number

.. _`ice_sched_get_vsi_layer`:

ice_sched_get_vsi_layer
=======================

.. c:function:: u8 ice_sched_get_vsi_layer(struct ice_hw *hw)

    get the current VSI layer number

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_sched_get_vsi_layer.description`:

Description
-----------

This function returns the current VSI layer number

.. _`ice_rm_dflt_leaf_node`:

ice_rm_dflt_leaf_node
=====================

.. c:function:: void ice_rm_dflt_leaf_node(struct ice_port_info *pi)

    remove the default leaf node in the tree

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

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

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

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

    :param pi:
        port info structure for the tree to cleanup
    :type pi: struct ice_port_info \*

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

    :param hw:
        pointer to the HW struct
    :type hw: struct ice_hw \*

.. _`ice_sched_query_res_alloc.description`:

Description
-----------

query FW for allocated scheduler resources and store in HW struct

.. _`ice_sched_find_node_in_subtree`:

ice_sched_find_node_in_subtree
==============================

.. c:function:: bool ice_sched_find_node_in_subtree(struct ice_hw *hw, struct ice_sched_node *base, struct ice_sched_node *node)

    Find node in part of base node subtree

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param base:
        pointer to the base node
    :type base: struct ice_sched_node \*

    :param node:
        pointer to the node to search
    :type node: struct ice_sched_node \*

.. _`ice_sched_find_node_in_subtree.description`:

Description
-----------

This function checks whether a given node is part of the base node
subtree or not

.. _`ice_sched_get_free_qparent`:

ice_sched_get_free_qparent
==========================

.. c:function:: struct ice_sched_node *ice_sched_get_free_qparent(struct ice_port_info *pi, u16 vsi_handle, u8 tc, u8 owner)

    Get a free lan or rdma q group node

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc:
        branch number
    :type tc: u8

    :param owner:
        lan or rdma
    :type owner: u8

.. _`ice_sched_get_free_qparent.description`:

Description
-----------

This function retrieves a free lan or rdma q group node

.. _`ice_sched_get_vsi_node`:

ice_sched_get_vsi_node
======================

.. c:function:: struct ice_sched_node *ice_sched_get_vsi_node(struct ice_hw *hw, struct ice_sched_node *tc_node, u16 vsi_handle)

    Get a VSI node based on VSI id

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param tc_node:
        pointer to the TC node
    :type tc_node: struct ice_sched_node \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

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

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param num_qs:
        number of queues
    :type num_qs: u16

    :param num_nodes:
        num nodes array
    :type num_nodes: u16 \*

.. _`ice_sched_calc_vsi_child_nodes.description`:

Description
-----------

This function calculates the number of VSI child nodes based on the
number of queues.

.. _`ice_sched_add_vsi_child_nodes`:

ice_sched_add_vsi_child_nodes
=============================

.. c:function:: enum ice_status ice_sched_add_vsi_child_nodes(struct ice_port_info *pi, u16 vsi_handle, struct ice_sched_node *tc_node, u16 *num_nodes, u8 owner)

    add VSI child nodes to tree

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc_node:
        pointer to the TC node
    :type tc_node: struct ice_sched_node \*

    :param num_nodes:
        pointer to the num nodes that needs to be added per layer
    :type num_nodes: u16 \*

    :param owner:
        node owner (lan or rdma)
    :type owner: u8

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

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_node:
        pointer to the VSI node
    :type vsi_node: struct ice_sched_node \*

    :param num_nodes:
        pointer to the num nodes that needs to be removed per layer
    :type num_nodes: u16 \*

    :param owner:
        node owner (lan or rdma)
    :type owner: u8

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

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param tc_node:
        pointer to TC node
    :type tc_node: struct ice_sched_node \*

    :param num_nodes:
        pointer to num nodes array
    :type num_nodes: u16 \*

.. _`ice_sched_calc_vsi_support_nodes.description`:

Description
-----------

This function calculates the number of supported nodes needed to add this
VSI into tx tree including the VSI, parent and intermediate nodes in below
layers

.. _`ice_sched_add_vsi_support_nodes`:

ice_sched_add_vsi_support_nodes
===============================

.. c:function:: enum ice_status ice_sched_add_vsi_support_nodes(struct ice_port_info *pi, u16 vsi_handle, struct ice_sched_node *tc_node, u16 *num_nodes)

    add VSI supported nodes into tx tree

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc_node:
        pointer to TC node
    :type tc_node: struct ice_sched_node \*

    :param num_nodes:
        pointer to num nodes array
    :type num_nodes: u16 \*

.. _`ice_sched_add_vsi_support_nodes.description`:

Description
-----------

This function adds the VSI supported nodes into tx tree including the
VSI, its parent and intermediate nodes in below layers

.. _`ice_sched_add_vsi_to_topo`:

ice_sched_add_vsi_to_topo
=========================

.. c:function:: enum ice_status ice_sched_add_vsi_to_topo(struct ice_port_info *pi, u16 vsi_handle, u8 tc)

    add a new VSI into tree

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc:
        TC number
    :type tc: u8

.. _`ice_sched_add_vsi_to_topo.description`:

Description
-----------

This function adds a new VSI into scheduler tree

.. _`ice_sched_update_vsi_child_nodes`:

ice_sched_update_vsi_child_nodes
================================

.. c:function:: enum ice_status ice_sched_update_vsi_child_nodes(struct ice_port_info *pi, u16 vsi_handle, u8 tc, u16 new_numqs, u8 owner)

    update VSI child nodes

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc:
        TC number
    :type tc: u8

    :param new_numqs:
        new number of max queues
    :type new_numqs: u16

    :param owner:
        owner of this subtree
    :type owner: u8

.. _`ice_sched_update_vsi_child_nodes.description`:

Description
-----------

This function updates the VSI child nodes based on the number of queues

.. _`ice_sched_cfg_vsi`:

ice_sched_cfg_vsi
=================

.. c:function:: enum ice_status ice_sched_cfg_vsi(struct ice_port_info *pi, u16 vsi_handle, u8 tc, u16 maxqs, u8 owner, bool enable)

    configure the new/exisiting VSI

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc:
        TC number
    :type tc: u8

    :param maxqs:
        max number of queues
    :type maxqs: u16

    :param owner:
        lan or rdma
    :type owner: u8

    :param enable:
        TC enabled or disabled
    :type enable: bool

.. _`ice_sched_cfg_vsi.description`:

Description
-----------

This function adds/updates VSI nodes based on the number of queues. If TC is
enabled and VSI is in suspended state then resume the VSI back. If TC is
disabled then suspend the VSI if it is not already.

.. This file was automatic generated / don't edit.

