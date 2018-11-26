.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_lib.c

.. _`ice_setup_rx_ctx`:

ice_setup_rx_ctx
================

.. c:function:: int ice_setup_rx_ctx(struct ice_ring *ring)

    Configure a receive ring context

    :param ring:
        The Rx ring to configure
    :type ring: struct ice_ring \*

.. _`ice_setup_rx_ctx.description`:

Description
-----------

Configure the Rx descriptor ring in RLAN context.

.. _`ice_setup_tx_ctx`:

ice_setup_tx_ctx
================

.. c:function:: void ice_setup_tx_ctx(struct ice_ring *ring, struct ice_tlan_ctx *tlan_ctx, u16 pf_q)

    setup a struct ice_tlan_ctx instance

    :param ring:
        The Tx ring to configure
    :type ring: struct ice_ring \*

    :param tlan_ctx:
        Pointer to the Tx LAN queue context structure to be initialized
    :type tlan_ctx: struct ice_tlan_ctx \*

    :param pf_q:
        queue index in the PF space
    :type pf_q: u16

.. _`ice_setup_tx_ctx.description`:

Description
-----------

Configure the Tx descriptor ring in TLAN context.

.. _`ice_pf_rxq_wait`:

ice_pf_rxq_wait
===============

.. c:function:: int ice_pf_rxq_wait(struct ice_pf *pf, int pf_q, bool ena)

    Wait for a PF's Rx queue to be enabled or disabled

    :param pf:
        the PF being configured
    :type pf: struct ice_pf \*

    :param pf_q:
        the PF queue
    :type pf_q: int

    :param ena:
        enable or disable state of the queue
    :type ena: bool

.. _`ice_pf_rxq_wait.description`:

Description
-----------

This routine will wait for the given Rx queue of the PF to reach the
enabled or disabled state.
Returns -ETIMEDOUT in case of failing to reach the requested state after
multiple retries; else will return 0 in case of success.

.. _`ice_vsi_ctrl_rx_rings`:

ice_vsi_ctrl_rx_rings
=====================

.. c:function:: int ice_vsi_ctrl_rx_rings(struct ice_vsi *vsi, bool ena)

    Start or stop a VSI's Rx rings

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param ena:
        start or stop the Rx rings
    :type ena: bool

.. _`ice_vsi_alloc_arrays`:

ice_vsi_alloc_arrays
====================

.. c:function:: int ice_vsi_alloc_arrays(struct ice_vsi *vsi, bool alloc_qvectors)

    Allocate queue and vector pointer arrays for the VSI

    :param vsi:
        VSI pointer
    :type vsi: struct ice_vsi \*

    :param alloc_qvectors:
        a bool to specify if q_vectors need to be allocated.
    :type alloc_qvectors: bool

.. _`ice_vsi_alloc_arrays.on-error`:

On error
--------

returns error code (negative)

.. _`ice_vsi_alloc_arrays.on-success`:

On success
----------

returns 0

.. _`ice_vsi_set_num_qs`:

ice_vsi_set_num_qs
==================

.. c:function:: void ice_vsi_set_num_qs(struct ice_vsi *vsi)

    Set num queues, descriptors and vectors for a VSI

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_set_num_qs.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_get_free_slot`:

ice_get_free_slot
=================

.. c:function:: int ice_get_free_slot(void *array, int size, int curr)

    get the next non-NULL location index in array

    :param array:
        array to search
    :type array: void \*

    :param size:
        size of the array
    :type size: int

    :param curr:
        last known occupied index to be used as a search hint
    :type curr: int

.. _`ice_get_free_slot.description`:

Description
-----------

void \* is being used to keep the functionality generic. This lets us use this
function on any array of pointers.

.. _`ice_vsi_delete`:

ice_vsi_delete
==============

.. c:function:: void ice_vsi_delete(struct ice_vsi *vsi)

    delete a VSI from the switch

    :param vsi:
        pointer to VSI being removed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_free_arrays`:

ice_vsi_free_arrays
===================

.. c:function:: void ice_vsi_free_arrays(struct ice_vsi *vsi, bool free_qvectors)

    clean up VSI resources

    :param vsi:
        pointer to VSI being cleared
    :type vsi: struct ice_vsi \*

    :param free_qvectors:
        bool to specify if q_vectors should be deallocated
    :type free_qvectors: bool

.. _`ice_vsi_clear`:

ice_vsi_clear
=============

.. c:function:: int ice_vsi_clear(struct ice_vsi *vsi)

    clean up and deallocate the provided VSI

    :param vsi:
        pointer to VSI being cleared
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_clear.description`:

Description
-----------

This deallocates the VSI's queue resources, removes it from the PF's
VSI array if necessary, and deallocates the VSI

Returns 0 on success, negative on failure

.. _`ice_msix_clean_rings`:

ice_msix_clean_rings
====================

.. c:function:: irqreturn_t ice_msix_clean_rings(int __always_unused irq, void *data)

    MSIX mode Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int __always_unused

    :param data:
        pointer to a q_vector
    :type data: void \*

.. _`ice_vsi_alloc`:

ice_vsi_alloc
=============

.. c:function:: struct ice_vsi *ice_vsi_alloc(struct ice_pf *pf, enum ice_vsi_type type)

    Allocates the next available struct VSI in the PF

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

    :param type:
        type of VSI
    :type type: enum ice_vsi_type

.. _`ice_vsi_alloc.description`:

Description
-----------

returns a pointer to a VSI on success, NULL on failure.

.. _`ice_vsi_get_qs_contig`:

ice_vsi_get_qs_contig
=====================

.. c:function:: int ice_vsi_get_qs_contig(struct ice_vsi *vsi)

    Assign a contiguous chunk of queues to VSI

    :param vsi:
        the VSI getting queues
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_get_qs_contig.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_get_qs_scatter`:

ice_vsi_get_qs_scatter
======================

.. c:function:: int ice_vsi_get_qs_scatter(struct ice_vsi *vsi)

    Assign a scattered queues to VSI

    :param vsi:
        the VSI getting queues
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_get_qs_scatter.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_get_qs`:

ice_vsi_get_qs
==============

.. c:function:: int ice_vsi_get_qs(struct ice_vsi *vsi)

    Assign queues from PF to VSI

    :param vsi:
        the VSI to assign queues to
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_get_qs.description`:

Description
-----------

Returns 0 on success and a negative value on error

.. _`ice_vsi_put_qs`:

ice_vsi_put_qs
==============

.. c:function:: void ice_vsi_put_qs(struct ice_vsi *vsi)

    Release queues from VSI to PF

    :param vsi:
        the VSI that is going to release queues
    :type vsi: struct ice_vsi \*

.. _`ice_rss_clean`:

ice_rss_clean
=============

.. c:function:: void ice_rss_clean(struct ice_vsi *vsi)

    Delete RSS related VSI structures that hold user inputs

    :param vsi:
        the VSI being removed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_set_rss_params`:

ice_vsi_set_rss_params
======================

.. c:function:: void ice_vsi_set_rss_params(struct ice_vsi *vsi)

    Setup RSS capabilities per VSI type

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_set_dflt_vsi_ctx`:

ice_set_dflt_vsi_ctx
====================

.. c:function:: void ice_set_dflt_vsi_ctx(struct ice_vsi_ctx *ctxt)

    Set default VSI context before adding a VSI

    :param ctxt:
        the VSI context being set
    :type ctxt: struct ice_vsi_ctx \*

.. _`ice_set_dflt_vsi_ctx.description`:

Description
-----------

This initializes a default VSI context for all sections except the Queues.

.. _`ice_vsi_setup_q_map`:

ice_vsi_setup_q_map
===================

.. c:function:: void ice_vsi_setup_q_map(struct ice_vsi *vsi, struct ice_vsi_ctx *ctxt)

    Setup a VSI queue map

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param ctxt:
        VSI context structure
    :type ctxt: struct ice_vsi_ctx \*

.. _`ice_set_rss_vsi_ctx`:

ice_set_rss_vsi_ctx
===================

.. c:function:: void ice_set_rss_vsi_ctx(struct ice_vsi_ctx *ctxt, struct ice_vsi *vsi)

    Set RSS VSI context before adding a VSI

    :param ctxt:
        the VSI context being set
    :type ctxt: struct ice_vsi_ctx \*

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_init`:

ice_vsi_init
============

.. c:function:: int ice_vsi_init(struct ice_vsi *vsi)

    Create and initialize a VSI

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_init.description`:

Description
-----------

This initializes a VSI context depending on the VSI type to be added and
passes it down to the add_vsi aq command to create a new VSI.

.. _`ice_free_q_vector`:

ice_free_q_vector
=================

.. c:function:: void ice_free_q_vector(struct ice_vsi *vsi, int v_idx)

    Free memory allocated for a specific interrupt vector

    :param vsi:
        VSI having the memory freed
    :type vsi: struct ice_vsi \*

    :param v_idx:
        index of the vector to be freed
    :type v_idx: int

.. _`ice_vsi_free_q_vectors`:

ice_vsi_free_q_vectors
======================

.. c:function:: void ice_vsi_free_q_vectors(struct ice_vsi *vsi)

    Free memory allocated for interrupt vectors

    :param vsi:
        the VSI having memory freed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_alloc_q_vector`:

ice_vsi_alloc_q_vector
======================

.. c:function:: int ice_vsi_alloc_q_vector(struct ice_vsi *vsi, int v_idx)

    Allocate memory for a single interrupt vector

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param v_idx:
        index of the vector in the VSI struct
    :type v_idx: int

.. _`ice_vsi_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`ice_vsi_alloc_q_vectors`:

ice_vsi_alloc_q_vectors
=======================

.. c:function:: int ice_vsi_alloc_q_vectors(struct ice_vsi *vsi)

    Allocate memory for interrupt vectors

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`ice_vsi_setup_vector_base`:

ice_vsi_setup_vector_base
=========================

.. c:function:: int ice_vsi_setup_vector_base(struct ice_vsi *vsi)

    Set up the base vector for the given VSI

    :param vsi:
        ptr to the VSI
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_setup_vector_base.description`:

Description
-----------

This should only be called after \ :c:func:`ice_vsi_alloc`\  which allocates the
corresponding SW VSI structure and initializes num_queue_pairs for the
newly allocated VSI.

Returns 0 on success or negative on failure

.. _`ice_vsi_clear_rings`:

ice_vsi_clear_rings
===================

.. c:function:: void ice_vsi_clear_rings(struct ice_vsi *vsi)

    Deallocates the Tx and Rx rings for VSI

    :param vsi:
        the VSI having rings deallocated
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_alloc_rings`:

ice_vsi_alloc_rings
===================

.. c:function:: int ice_vsi_alloc_rings(struct ice_vsi *vsi)

    Allocates Tx and Rx rings for the VSI

    :param vsi:
        VSI which is having rings allocated
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_map_rings_to_vectors`:

ice_vsi_map_rings_to_vectors
============================

.. c:function:: void ice_vsi_map_rings_to_vectors(struct ice_vsi *vsi)

    Map VSI rings to interrupt vectors

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_map_rings_to_vectors.description`:

Description
-----------

This function maps descriptor rings to the queue-specific vectors allotted
through the MSI-X enabling code. On a constrained vector budget, we map Tx
and Rx rings to the vector as "efficiently" as possible.

.. _`ice_vsi_manage_rss_lut`:

ice_vsi_manage_rss_lut
======================

.. c:function:: int ice_vsi_manage_rss_lut(struct ice_vsi *vsi, bool ena)

    disable/enable RSS

    :param vsi:
        the VSI being changed
    :type vsi: struct ice_vsi \*

    :param ena:
        boolean value indicating if this is an enable or disable request
    :type ena: bool

.. _`ice_vsi_manage_rss_lut.description`:

Description
-----------

In the event of disable request for RSS, this function will zero out RSS
LUT, while in the event of enable request for RSS, it will reconfigure RSS
LUT.

.. _`ice_vsi_cfg_rss_lut_key`:

ice_vsi_cfg_rss_lut_key
=======================

.. c:function:: int ice_vsi_cfg_rss_lut_key(struct ice_vsi *vsi)

    Configure RSS params for a VSI

    :param vsi:
        VSI to be configured
    :type vsi: struct ice_vsi \*

.. _`ice_add_mac_to_list`:

ice_add_mac_to_list
===================

.. c:function:: int ice_add_mac_to_list(struct ice_vsi *vsi, struct list_head *add_list, const u8 *macaddr)

    Add a mac address filter entry to the list

    :param vsi:
        the VSI to be forwarded to
    :type vsi: struct ice_vsi \*

    :param add_list:
        pointer to the list which contains MAC filter entries
    :type add_list: struct list_head \*

    :param macaddr:
        the MAC address to be added.
    :type macaddr: const u8 \*

.. _`ice_add_mac_to_list.description`:

Description
-----------

Adds mac address filter entry to the temp list

Returns 0 on success or ENOMEM on failure.

.. _`ice_update_eth_stats`:

ice_update_eth_stats
====================

.. c:function:: void ice_update_eth_stats(struct ice_vsi *vsi)

    Update VSI-specific ethernet statistics counters

    :param vsi:
        the VSI to be updated
    :type vsi: struct ice_vsi \*

.. _`ice_free_fltr_list`:

ice_free_fltr_list
==================

.. c:function:: void ice_free_fltr_list(struct device *dev, struct list_head *h)

    free filter lists helper

    :param dev:
        pointer to the device struct
    :type dev: struct device \*

    :param h:
        pointer to the list head to be freed
    :type h: struct list_head \*

.. _`ice_free_fltr_list.description`:

Description
-----------

Helper function to free filter lists previously created using
ice_add_mac_to_list

.. _`ice_vsi_add_vlan`:

ice_vsi_add_vlan
================

.. c:function:: int ice_vsi_add_vlan(struct ice_vsi *vsi, u16 vid)

    Add VSI membership for given VLAN

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param vid:
        VLAN id to be added
    :type vid: u16

.. _`ice_vsi_kill_vlan`:

ice_vsi_kill_vlan
=================

.. c:function:: int ice_vsi_kill_vlan(struct ice_vsi *vsi, u16 vid)

    Remove VSI membership for a given VLAN

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param vid:
        VLAN id to be removed
    :type vid: u16

.. _`ice_vsi_kill_vlan.description`:

Description
-----------

Returns 0 on success and negative on failure

.. _`ice_vsi_cfg_rxqs`:

ice_vsi_cfg_rxqs
================

.. c:function:: int ice_vsi_cfg_rxqs(struct ice_vsi *vsi)

    Configure the VSI for Rx

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_cfg_rxqs.description`:

Description
-----------

Return 0 on success and a negative value on error
Configure the Rx VSI for operation.

.. _`ice_vsi_cfg_txqs`:

ice_vsi_cfg_txqs
================

.. c:function:: int ice_vsi_cfg_txqs(struct ice_vsi *vsi)

    Configure the VSI for Tx

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_cfg_txqs.description`:

Description
-----------

Return 0 on success and a negative value on error
Configure the Tx VSI for operation.

.. _`ice_intrl_usec_to_reg`:

ice_intrl_usec_to_reg
=====================

.. c:function:: u32 ice_intrl_usec_to_reg(u8 intrl, u8 gran)

    convert interrupt rate limit to register value

    :param intrl:
        interrupt rate limit in usecs
    :type intrl: u8

    :param gran:
        interrupt rate limit granularity in usecs
    :type gran: u8

.. _`ice_intrl_usec_to_reg.description`:

Description
-----------

This function converts a decimal interrupt rate limit in usecs to the format
expected by firmware.

.. _`ice_cfg_itr`:

ice_cfg_itr
===========

.. c:function:: void ice_cfg_itr(struct ice_hw *hw, struct ice_q_vector *q_vector, u16 vector)

    configure the initial interrupt throttle values

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param q_vector:
        interrupt vector that's being configured
    :type q_vector: struct ice_q_vector \*

    :param vector:
        HW vector index to apply the interrupt throttling to
    :type vector: u16

.. _`ice_cfg_itr.description`:

Description
-----------

Configure interrupt throttling values for the ring containers that are
associated with the interrupt vector passed in.

.. _`ice_vsi_cfg_msix`:

ice_vsi_cfg_msix
================

.. c:function:: void ice_vsi_cfg_msix(struct ice_vsi *vsi)

    MSIX mode Interrupt Config in the HW

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_manage_vlan_insertion`:

ice_vsi_manage_vlan_insertion
=============================

.. c:function:: int ice_vsi_manage_vlan_insertion(struct ice_vsi *vsi)

    Manage VLAN insertion for the VSI for Tx

    :param vsi:
        the VSI being changed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_manage_vlan_stripping`:

ice_vsi_manage_vlan_stripping
=============================

.. c:function:: int ice_vsi_manage_vlan_stripping(struct ice_vsi *vsi, bool ena)

    Manage VLAN stripping for the VSI for Rx

    :param vsi:
        the VSI being changed
    :type vsi: struct ice_vsi \*

    :param ena:
        boolean value indicating if this is a enable or disable request
    :type ena: bool

.. _`ice_vsi_start_rx_rings`:

ice_vsi_start_rx_rings
======================

.. c:function:: int ice_vsi_start_rx_rings(struct ice_vsi *vsi)

    start VSI's Rx rings

    :param vsi:
        the VSI whose rings are to be started
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_start_rx_rings.description`:

Description
-----------

Returns 0 on success and a negative value on error

.. _`ice_vsi_stop_rx_rings`:

ice_vsi_stop_rx_rings
=====================

.. c:function:: int ice_vsi_stop_rx_rings(struct ice_vsi *vsi)

    stop VSI's Rx rings

    :param vsi:
        the VSI
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_stop_rx_rings.description`:

Description
-----------

Returns 0 on success and a negative value on error

.. _`ice_vsi_stop_tx_rings`:

ice_vsi_stop_tx_rings
=====================

.. c:function:: int ice_vsi_stop_tx_rings(struct ice_vsi *vsi, enum ice_disq_rst_src rst_src, u16 rel_vmvf_num)

    Disable Tx rings

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

    :param rst_src:
        reset source
    :type rst_src: enum ice_disq_rst_src

    :param rel_vmvf_num:
        Relative id of VF/VM
    :type rel_vmvf_num: u16

.. _`ice_cfg_vlan_pruning`:

ice_cfg_vlan_pruning
====================

.. c:function:: int ice_cfg_vlan_pruning(struct ice_vsi *vsi, bool ena)

    enable or disable VLAN pruning on the VSI

    :param vsi:
        VSI to enable or disable VLAN pruning on
    :type vsi: struct ice_vsi \*

    :param ena:
        set to true to enable VLAN pruning and false to disable it
    :type ena: bool

.. _`ice_cfg_vlan_pruning.description`:

Description
-----------

returns 0 if VSI is updated, negative otherwise

.. _`ice_vsi_setup`:

ice_vsi_setup
=============

.. c:function:: struct ice_vsi *ice_vsi_setup(struct ice_pf *pf, struct ice_port_info *pi, enum ice_vsi_type type, u16 vf_id)

    Set up a VSI by a given type

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

    :param pi:
        pointer to the port_info instance
    :type pi: struct ice_port_info \*

    :param type:
        VSI type
    :type type: enum ice_vsi_type

    :param vf_id:
        defines VF id to which this VSI connects. This field is meant to be
        used only for ICE_VSI_VF VSI type. For other VSI types, should
        fill-in ICE_INVAL_VFID as input.
    :type vf_id: u16

.. _`ice_vsi_setup.description`:

Description
-----------

This allocates the sw VSI structure and its queue resources.

Returns pointer to the successfully allocated and configured VSI sw struct on
success, NULL on failure.

.. _`ice_vsi_release_msix`:

ice_vsi_release_msix
====================

.. c:function:: void ice_vsi_release_msix(struct ice_vsi *vsi)

    Clear the queue to Interrupt mapping in HW

    :param vsi:
        the VSI being cleaned up
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_free_irq`:

ice_vsi_free_irq
================

.. c:function:: void ice_vsi_free_irq(struct ice_vsi *vsi)

    Free the IRQ association with the OS

    :param vsi:
        the VSI being configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_free_tx_rings`:

ice_vsi_free_tx_rings
=====================

.. c:function:: void ice_vsi_free_tx_rings(struct ice_vsi *vsi)

    Free Tx resources for VSI queues

    :param vsi:
        the VSI having resources freed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_free_rx_rings`:

ice_vsi_free_rx_rings
=====================

.. c:function:: void ice_vsi_free_rx_rings(struct ice_vsi *vsi)

    Free Rx resources for VSI queues

    :param vsi:
        the VSI having resources freed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_close`:

ice_vsi_close
=============

.. c:function:: void ice_vsi_close(struct ice_vsi *vsi)

    Shut down a VSI

    :param vsi:
        the VSI being shut down
    :type vsi: struct ice_vsi \*

.. _`ice_free_res`:

ice_free_res
============

.. c:function:: int ice_free_res(struct ice_res_tracker *res, u16 index, u16 id)

    free a block of resources

    :param res:
        pointer to the resource
    :type res: struct ice_res_tracker \*

    :param index:
        starting index previously returned by ice_get_res
    :type index: u16

    :param id:
        identifier to track owner
    :type id: u16

.. _`ice_free_res.description`:

Description
-----------

Returns number of resources freed

.. _`ice_search_res`:

ice_search_res
==============

.. c:function:: int ice_search_res(struct ice_res_tracker *res, u16 needed, u16 id)

    Search the tracker for a block of resources

    :param res:
        pointer to the resource
    :type res: struct ice_res_tracker \*

    :param needed:
        size of the block needed
    :type needed: u16

    :param id:
        identifier to track owner
    :type id: u16

.. _`ice_search_res.description`:

Description
-----------

Returns the base item index of the block, or -ENOMEM for error

.. _`ice_get_res`:

ice_get_res
===========

.. c:function:: int ice_get_res(struct ice_pf *pf, struct ice_res_tracker *res, u16 needed, u16 id)

    get a block of resources

    :param pf:
        board private structure
    :type pf: struct ice_pf \*

    :param res:
        pointer to the resource
    :type res: struct ice_res_tracker \*

    :param needed:
        size of the block needed
    :type needed: u16

    :param id:
        identifier to track owner
    :type id: u16

.. _`ice_get_res.description`:

Description
-----------

Returns the base item index of the block, or -ENOMEM for error
The search_hint trick and lack of advanced fit-finding only works
because we're highly likely to have all the same sized requests.
Linear search time and any fragmentation should be minimal.

.. _`ice_vsi_dis_irq`:

ice_vsi_dis_irq
===============

.. c:function:: void ice_vsi_dis_irq(struct ice_vsi *vsi)

    Mask off queue interrupt generation on the VSI

    :param vsi:
        the VSI being un-configured
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_release`:

ice_vsi_release
===============

.. c:function:: int ice_vsi_release(struct ice_vsi *vsi)

    Delete a VSI and free its resources

    :param vsi:
        the VSI being removed
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_release.description`:

Description
-----------

Returns 0 on success or < 0 on error

.. _`ice_vsi_rebuild`:

ice_vsi_rebuild
===============

.. c:function:: int ice_vsi_rebuild(struct ice_vsi *vsi)

    Rebuild VSI after reset

    :param vsi:
        VSI to be rebuild
    :type vsi: struct ice_vsi \*

.. _`ice_vsi_rebuild.description`:

Description
-----------

Returns 0 on success and negative value on failure

.. _`ice_is_reset_in_progress`:

ice_is_reset_in_progress
========================

.. c:function:: bool ice_is_reset_in_progress(unsigned long *state)

    check for a reset in progress

    :param state:
        pf state field
    :type state: unsigned long \*

.. This file was automatic generated / don't edit.

