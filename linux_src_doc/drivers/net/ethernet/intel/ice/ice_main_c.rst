.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_main.c

.. _`ice_get_free_slot`:

ice_get_free_slot
=================

.. c:function:: int ice_get_free_slot(void *array, int size, int curr)

    get the next non-NULL location index in array

    :param void \*array:
        array to search

    :param int size:
        size of the array

    :param int curr:
        last known occupied index to be used as a search hint

.. _`ice_get_free_slot.description`:

Description
-----------

void \* is being used to keep the functionality generic. This lets us use this
function on any array of pointers.

.. _`ice_search_res`:

ice_search_res
==============

.. c:function:: int ice_search_res(struct ice_res_tracker *res, u16 needed, u16 id)

    Search the tracker for a block of resources

    :param struct ice_res_tracker \*res:
        pointer to the resource

    :param u16 needed:
        size of the block needed

    :param u16 id:
        identifier to track owner
        Returns the base item index of the block, or -ENOMEM for error

.. _`ice_get_res`:

ice_get_res
===========

.. c:function:: int ice_get_res(struct ice_pf *pf, struct ice_res_tracker *res, u16 needed, u16 id)

    get a block of resources

    :param struct ice_pf \*pf:
        board private structure

    :param struct ice_res_tracker \*res:
        pointer to the resource

    :param u16 needed:
        size of the block needed

    :param u16 id:
        identifier to track owner

.. _`ice_get_res.description`:

Description
-----------

Returns the base item index of the block, or -ENOMEM for error
The search_hint trick and lack of advanced fit-finding only works
because we're highly likely to have all the same sized requests.
Linear search time and any fragmentation should be minimal.

.. _`ice_free_res`:

ice_free_res
============

.. c:function:: int ice_free_res(struct ice_res_tracker *res, u16 index, u16 id)

    free a block of resources

    :param struct ice_res_tracker \*res:
        pointer to the resource

    :param u16 index:
        starting index previously returned by ice_get_res

    :param u16 id:
        identifier to track owner
        Returns number of resources freed

.. _`ice_add_mac_to_list`:

ice_add_mac_to_list
===================

.. c:function:: int ice_add_mac_to_list(struct ice_vsi *vsi, struct list_head *add_list, const u8 *macaddr)

    Add a mac address filter entry to the list

    :param struct ice_vsi \*vsi:
        the VSI to be forwarded to

    :param struct list_head \*add_list:
        pointer to the list which contains MAC filter entries

    :param const u8 \*macaddr:
        the MAC address to be added.

.. _`ice_add_mac_to_list.description`:

Description
-----------

Adds mac address filter entry to the temp list

Returns 0 on success or ENOMEM on failure.

.. _`ice_add_mac_to_sync_list`:

ice_add_mac_to_sync_list
========================

.. c:function:: int ice_add_mac_to_sync_list(struct net_device *netdev, const u8 *addr)

    creates list of mac addresses to be synced

    :param struct net_device \*netdev:
        the net device on which the sync is happening

    :param const u8 \*addr:
        mac address to sync

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

    :param struct net_device \*netdev:
        the net device on which the unsync is happening

    :param const u8 \*addr:
        mac address to unsync

.. _`ice_add_mac_to_unsync_list.description`:

Description
-----------

This is a callback function which is called by the in kernel device unsync
functions (like \__dev_uc_unsync, \__dev_mc_unsync, etc). This function only
populates the tmp_unsync_list, which is later used by ice_remove_mac to
delete the mac filters from the hardware.

.. _`ice_free_fltr_list`:

ice_free_fltr_list
==================

.. c:function:: void ice_free_fltr_list(struct device *dev, struct list_head *h)

    free filter lists helper

    :param struct device \*dev:
        pointer to the device struct

    :param struct list_head \*h:
        pointer to the list head to be freed

.. _`ice_free_fltr_list.description`:

Description
-----------

Helper function to free filter lists previously created using
ice_add_mac_to_list

.. _`ice_vsi_fltr_changed`:

ice_vsi_fltr_changed
====================

.. c:function:: bool ice_vsi_fltr_changed(struct ice_vsi *vsi)

    check if filter state changed

    :param struct ice_vsi \*vsi:
        VSI to be checked

.. _`ice_vsi_fltr_changed.description`:

Description
-----------

returns true if filter state has changed, false otherwise.

.. _`ice_vsi_sync_fltr`:

ice_vsi_sync_fltr
=================

.. c:function:: int ice_vsi_sync_fltr(struct ice_vsi *vsi)

    Update the VSI filter list to the HW

    :param struct ice_vsi \*vsi:
        ptr to the VSI

.. _`ice_vsi_sync_fltr.description`:

Description
-----------

Push any outstanding VSI filter changes through the AdminQ.

.. _`ice_sync_fltr_subtask`:

ice_sync_fltr_subtask
=====================

.. c:function:: void ice_sync_fltr_subtask(struct ice_pf *pf)

    Sync the VSI filter list with HW

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_is_reset_recovery_pending`:

ice_is_reset_recovery_pending
=============================

.. c:function:: bool ice_is_reset_recovery_pending(unsigned long int *state)

    schedule a reset

    :param unsigned long int \*state:
        pf state field

.. _`ice_prepare_for_reset`:

ice_prepare_for_reset
=====================

.. c:function:: void ice_prepare_for_reset(struct ice_pf *pf)

    prep for the core to reset

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_prepare_for_reset.description`:

Description
-----------

Inform or close all dependent features in prep for reset.

.. _`ice_do_reset`:

ice_do_reset
============

.. c:function:: void ice_do_reset(struct ice_pf *pf, enum ice_reset_req reset_type)

    Initiate one of many types of resets

    :param struct ice_pf \*pf:
        board private structure

    :param enum ice_reset_req reset_type:
        reset type requested
        before this function was called.

.. _`ice_reset_subtask`:

ice_reset_subtask
=================

.. c:function:: void ice_reset_subtask(struct ice_pf *pf)

    Set up for resetting the device and driver

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_watchdog_subtask`:

ice_watchdog_subtask
====================

.. c:function:: void ice_watchdog_subtask(struct ice_pf *pf)

    periodic tasks not using event driven scheduling

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_print_link_msg`:

ice_print_link_msg
==================

.. c:function:: void ice_print_link_msg(struct ice_vsi *vsi, bool isup)

    print link up or down message

    :param struct ice_vsi \*vsi:
        the VSI whose link status is being queried

    :param bool isup:
        boolean for if the link is now up or down

.. _`ice_init_link_events`:

ice_init_link_events
====================

.. c:function:: int ice_init_link_events(struct ice_port_info *pi)

    enable/initialize link events

    :param struct ice_port_info \*pi:
        pointer to the port_info instance

.. _`ice_init_link_events.description`:

Description
-----------

Returns -EIO on failure, 0 on success

.. _`ice_vsi_link_event`:

ice_vsi_link_event
==================

.. c:function:: void ice_vsi_link_event(struct ice_vsi *vsi, bool link_up)

    update the vsi's netdev

    :param struct ice_vsi \*vsi:
        the vsi on which the link event occurred

    :param bool link_up:
        whether or not the vsi needs to be set up or down

.. _`ice_link_event`:

ice_link_event
==============

.. c:function:: int ice_link_event(struct ice_pf *pf, struct ice_port_info *pi)

    process the link event

    :param struct ice_pf \*pf:
        pf that the link event is associated with

    :param struct ice_port_info \*pi:
        port_info for the port that the link event is associated with

.. _`ice_link_event.description`:

Description
-----------

Returns -EIO if \ :c:func:`ice_get_link_status`\  fails
Returns 0 on success

.. _`ice_handle_link_event`:

ice_handle_link_event
=====================

.. c:function:: int ice_handle_link_event(struct ice_pf *pf)

    handle link event via ARQ

    :param struct ice_pf \*pf:
        pf that the link event is associated with

.. _`ice_handle_link_event.description`:

Description
-----------

Return -EINVAL if port_info is null
Return status on succes

.. _`__ice_clean_ctrlq`:

\__ice_clean_ctrlq
==================

.. c:function:: int __ice_clean_ctrlq(struct ice_pf *pf, enum ice_ctl_q q_type)

    helper function to clean controlq rings

    :param struct ice_pf \*pf:
        ptr to struct ice_pf

    :param enum ice_ctl_q q_type:
        specific Control queue type

.. _`ice_clean_adminq_subtask`:

ice_clean_adminq_subtask
========================

.. c:function:: void ice_clean_adminq_subtask(struct ice_pf *pf)

    clean the AdminQ rings

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_service_task_schedule`:

ice_service_task_schedule
=========================

.. c:function:: void ice_service_task_schedule(struct ice_pf *pf)

    schedule the service task to wake up

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_service_task_schedule.description`:

Description
-----------

If not already scheduled, this puts the task into the work queue.

.. _`ice_service_task_complete`:

ice_service_task_complete
=========================

.. c:function:: void ice_service_task_complete(struct ice_pf *pf)

    finish up the service task

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_service_timer`:

ice_service_timer
=================

.. c:function:: void ice_service_timer(struct timer_list *t)

    timer callback to schedule service task

    :param struct timer_list \*t:
        pointer to timer_list

.. _`ice_service_task`:

ice_service_task
================

.. c:function:: void ice_service_task(struct work_struct *work)

    manage and run subtasks

    :param struct work_struct \*work:
        pointer to work_struct contained by the PF struct

.. _`ice_set_ctrlq_len`:

ice_set_ctrlq_len
=================

.. c:function:: void ice_set_ctrlq_len(struct ice_hw *hw)

    helper function to set controlq length

    :param struct ice_hw \*hw:
        pointer to the hw instance

.. _`ice_irq_affinity_notify`:

ice_irq_affinity_notify
=======================

.. c:function:: void ice_irq_affinity_notify(struct irq_affinity_notify *notify, const cpumask_t *mask)

    Callback for affinity changes

    :param struct irq_affinity_notify \*notify:
        context as to what irq was changed

    :param const cpumask_t \*mask:
        the new affinity mask

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

    :param struct kref __always_unused \*ref:
        internal core kernel usage

.. _`ice_irq_affinity_release.description`:

Description
-----------

This is a callback function used by the irq_set_affinity_notifier function
to inform the current notification subscriber that they will no longer
receive notifications.

.. _`ice_vsi_dis_irq`:

ice_vsi_dis_irq
===============

.. c:function:: void ice_vsi_dis_irq(struct ice_vsi *vsi)

    Mask off queue interrupt generation on the VSI

    :param struct ice_vsi \*vsi:
        the VSI being un-configured

.. _`ice_vsi_ena_irq`:

ice_vsi_ena_irq
===============

.. c:function:: int ice_vsi_ena_irq(struct ice_vsi *vsi)

    Enable IRQ for the given VSI

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_delete`:

ice_vsi_delete
==============

.. c:function:: void ice_vsi_delete(struct ice_vsi *vsi)

    delete a VSI from the switch

    :param struct ice_vsi \*vsi:
        pointer to VSI being removed

.. _`ice_vsi_req_irq_msix`:

ice_vsi_req_irq_msix
====================

.. c:function:: int ice_vsi_req_irq_msix(struct ice_vsi *vsi, char *basename)

    get MSI-X vectors from the OS for the VSI

    :param struct ice_vsi \*vsi:
        the VSI being configured

    :param char \*basename:
        name for the vector

.. _`ice_vsi_set_rss_params`:

ice_vsi_set_rss_params
======================

.. c:function:: void ice_vsi_set_rss_params(struct ice_vsi *vsi)

    Setup RSS capabilities per VSI type

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_setup_q_map`:

ice_vsi_setup_q_map
===================

.. c:function:: void ice_vsi_setup_q_map(struct ice_vsi *vsi, struct ice_vsi_ctx *ctxt)

    Setup a VSI queue map

    :param struct ice_vsi \*vsi:
        the VSI being configured

    :param struct ice_vsi_ctx \*ctxt:
        VSI context structure

.. _`ice_set_dflt_vsi_ctx`:

ice_set_dflt_vsi_ctx
====================

.. c:function:: void ice_set_dflt_vsi_ctx(struct ice_vsi_ctx *ctxt)

    Set default VSI context before adding a VSI

    :param struct ice_vsi_ctx \*ctxt:
        the VSI context being set

.. _`ice_set_dflt_vsi_ctx.description`:

Description
-----------

This initializes a default VSI context for all sections except the Queues.

.. _`ice_set_rss_vsi_ctx`:

ice_set_rss_vsi_ctx
===================

.. c:function:: void ice_set_rss_vsi_ctx(struct ice_vsi_ctx *ctxt, struct ice_vsi *vsi)

    Set RSS VSI context before adding a VSI

    :param struct ice_vsi_ctx \*ctxt:
        the VSI context being set

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_add`:

ice_vsi_add
===========

.. c:function:: int ice_vsi_add(struct ice_vsi *vsi)

    Create a new VSI or fetch preallocated VSI

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_add.description`:

Description
-----------

This initializes a VSI context depending on the VSI type to be added and
passes it down to the add_vsi aq command to create a new VSI.

.. _`ice_vsi_release_msix`:

ice_vsi_release_msix
====================

.. c:function:: void ice_vsi_release_msix(struct ice_vsi *vsi)

    Clear the queue to Interrupt mapping in HW

    :param struct ice_vsi \*vsi:
        the VSI being cleaned up

.. _`ice_vsi_clear_rings`:

ice_vsi_clear_rings
===================

.. c:function:: void ice_vsi_clear_rings(struct ice_vsi *vsi)

    Deallocates the Tx and Rx rings for VSI

    :param struct ice_vsi \*vsi:
        the VSI having rings deallocated

.. _`ice_vsi_alloc_rings`:

ice_vsi_alloc_rings
===================

.. c:function:: int ice_vsi_alloc_rings(struct ice_vsi *vsi)

    Allocates Tx and Rx rings for the VSI

    :param struct ice_vsi \*vsi:
        VSI which is having rings allocated

.. _`ice_vsi_free_irq`:

ice_vsi_free_irq
================

.. c:function:: void ice_vsi_free_irq(struct ice_vsi *vsi)

    Free the irq association with the OS

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_cfg_msix`:

ice_vsi_cfg_msix
================

.. c:function:: void ice_vsi_cfg_msix(struct ice_vsi *vsi)

    MSIX mode Interrupt Config in the HW

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_ena_misc_vector`:

ice_ena_misc_vector
===================

.. c:function:: void ice_ena_misc_vector(struct ice_pf *pf)

    enable the non-queue interrupts

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_misc_intr`:

ice_misc_intr
=============

.. c:function:: irqreturn_t ice_misc_intr(int __always_unused irq, void *data)

    misc interrupt handler

    :param int __always_unused irq:
        interrupt number

    :param void \*data:
        pointer to a q_vector

.. _`ice_vsi_map_rings_to_vectors`:

ice_vsi_map_rings_to_vectors
============================

.. c:function:: void ice_vsi_map_rings_to_vectors(struct ice_vsi *vsi)

    Map VSI rings to interrupt vectors

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_map_rings_to_vectors.description`:

Description
-----------

This function maps descriptor rings to the queue-specific vectors allotted
through the MSI-X enabling code. On a constrained vector budget, we map Tx
and Rx rings to the vector as "efficiently" as possible.

.. _`ice_vsi_set_num_qs`:

ice_vsi_set_num_qs
==================

.. c:function:: void ice_vsi_set_num_qs(struct ice_vsi *vsi)

    Set num queues, descriptors and vectors for a VSI

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_set_num_qs.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_alloc_arrays`:

ice_vsi_alloc_arrays
====================

.. c:function:: int ice_vsi_alloc_arrays(struct ice_vsi *vsi, bool alloc_qvectors)

    Allocate queue and vector pointer arrays for the vsi

    :param struct ice_vsi \*vsi:
        VSI pointer

    :param bool alloc_qvectors:
        a bool to specify if q_vectors need to be allocated.

.. _`ice_vsi_alloc_arrays.on-error`:

On error
--------

returns error code (negative)

.. _`ice_vsi_alloc_arrays.on-success`:

On success
----------

returns 0

.. _`ice_msix_clean_rings`:

ice_msix_clean_rings
====================

.. c:function:: irqreturn_t ice_msix_clean_rings(int __always_unused irq, void *data)

    MSIX mode Interrupt Handler

    :param int __always_unused irq:
        interrupt number

    :param void \*data:
        pointer to a q_vector

.. _`ice_vsi_alloc`:

ice_vsi_alloc
=============

.. c:function:: struct ice_vsi *ice_vsi_alloc(struct ice_pf *pf, enum ice_vsi_type type)

    Allocates the next available struct vsi in the PF

    :param struct ice_pf \*pf:
        board private structure

    :param enum ice_vsi_type type:
        type of VSI

.. _`ice_vsi_alloc.description`:

Description
-----------

returns a pointer to a VSI on success, NULL on failure.

.. _`ice_free_irq_msix_misc`:

ice_free_irq_msix_misc
======================

.. c:function:: void ice_free_irq_msix_misc(struct ice_pf *pf)

    Unroll misc vector setup

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_req_irq_msix_misc`:

ice_req_irq_msix_misc
=====================

.. c:function:: int ice_req_irq_msix_misc(struct ice_pf *pf)

    Setup the misc vector to handle non queue events

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_req_irq_msix_misc.description`:

Description
-----------

This sets up the handler for MSIX 0, which is used to manage the
non-queue interrupts, e.g. AdminQ and errors.  This is not used
when in MSI or Legacy interrupt mode.

.. _`ice_vsi_get_qs_contig`:

ice_vsi_get_qs_contig
=====================

.. c:function:: int ice_vsi_get_qs_contig(struct ice_vsi *vsi)

    Assign a contiguous chunk of queues to VSI

    :param struct ice_vsi \*vsi:
        the VSI getting queues

.. _`ice_vsi_get_qs_contig.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_get_qs_scatter`:

ice_vsi_get_qs_scatter
======================

.. c:function:: int ice_vsi_get_qs_scatter(struct ice_vsi *vsi)

    Assign a scattered queues to VSI

    :param struct ice_vsi \*vsi:
        the VSI getting queues

.. _`ice_vsi_get_qs_scatter.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_get_qs`:

ice_vsi_get_qs
==============

.. c:function:: int ice_vsi_get_qs(struct ice_vsi *vsi)

    Assign queues from PF to VSI

    :param struct ice_vsi \*vsi:
        the VSI to assign queues to

.. _`ice_vsi_get_qs.description`:

Description
-----------

Returns 0 on success and a negative value on error

.. _`ice_vsi_put_qs`:

ice_vsi_put_qs
==============

.. c:function:: void ice_vsi_put_qs(struct ice_vsi *vsi)

    Release queues from VSI to PF

    :param struct ice_vsi \*vsi:
        the VSI thats going to release queues

.. _`ice_free_q_vector`:

ice_free_q_vector
=================

.. c:function:: void ice_free_q_vector(struct ice_vsi *vsi, int v_idx)

    Free memory allocated for a specific interrupt vector

    :param struct ice_vsi \*vsi:
        VSI having the memory freed

    :param int v_idx:
        index of the vector to be freed

.. _`ice_vsi_free_q_vectors`:

ice_vsi_free_q_vectors
======================

.. c:function:: void ice_vsi_free_q_vectors(struct ice_vsi *vsi)

    Free memory allocated for interrupt vectors

    :param struct ice_vsi \*vsi:
        the VSI having memory freed

.. _`ice_cfg_netdev`:

ice_cfg_netdev
==============

.. c:function:: int ice_cfg_netdev(struct ice_vsi *vsi)

    Setup the netdev flags

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_cfg_netdev.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`ice_vsi_free_arrays`:

ice_vsi_free_arrays
===================

.. c:function:: void ice_vsi_free_arrays(struct ice_vsi *vsi, bool free_qvectors)

    clean up vsi resources

    :param struct ice_vsi \*vsi:
        pointer to VSI being cleared

    :param bool free_qvectors:
        bool to specify if q_vectors should be deallocated

.. _`ice_vsi_clear`:

ice_vsi_clear
=============

.. c:function:: int ice_vsi_clear(struct ice_vsi *vsi)

    clean up and deallocate the provided vsi

    :param struct ice_vsi \*vsi:
        pointer to VSI being cleared

.. _`ice_vsi_clear.description`:

Description
-----------

This deallocates the vsi's queue resources, removes it from the PF's
VSI array if necessary, and deallocates the VSI

Returns 0 on success, negative on failure

.. _`ice_vsi_alloc_q_vector`:

ice_vsi_alloc_q_vector
======================

.. c:function:: int ice_vsi_alloc_q_vector(struct ice_vsi *vsi, int v_idx)

    Allocate memory for a single interrupt vector

    :param struct ice_vsi \*vsi:
        the VSI being configured

    :param int v_idx:
        index of the vector in the vsi struct

.. _`ice_vsi_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`ice_vsi_alloc_q_vectors`:

ice_vsi_alloc_q_vectors
=======================

.. c:function:: int ice_vsi_alloc_q_vectors(struct ice_vsi *vsi)

    Allocate memory for interrupt vectors

    :param struct ice_vsi \*vsi:
        the VSI being configured

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

    :param struct ice_vsi \*vsi:
        ptr to the VSI

.. _`ice_vsi_setup_vector_base.description`:

Description
-----------

This should only be called after \ :c:func:`ice_vsi_alloc`\  which allocates the
corresponding SW VSI structure and initializes num_queue_pairs for the
newly allocated VSI.

Returns 0 on success or negative on failure

.. _`ice_fill_rss_lut`:

ice_fill_rss_lut
================

.. c:function:: void ice_fill_rss_lut(u8 *lut, u16 rss_table_size, u16 rss_size)

    Fill the RSS lookup table with default values

    :param u8 \*lut:
        Lookup table

    :param u16 rss_table_size:
        Lookup table size

    :param u16 rss_size:
        Range of queue number for hashing

.. _`ice_vsi_cfg_rss`:

ice_vsi_cfg_rss
===============

.. c:function:: int ice_vsi_cfg_rss(struct ice_vsi *vsi)

    Configure RSS params for a VSI

    :param struct ice_vsi \*vsi:
        VSI to be configured

.. _`ice_vsi_reinit_setup`:

ice_vsi_reinit_setup
====================

.. c:function:: int ice_vsi_reinit_setup(struct ice_vsi *vsi)

    return resource and reallocate resource for a VSI

    :param struct ice_vsi \*vsi:
        pointer to the ice_vsi

.. _`ice_vsi_reinit_setup.description`:

Description
-----------

This reallocates the VSIs queue resources

Returns 0 on success and negative value on failure

.. _`ice_vsi_setup`:

ice_vsi_setup
=============

.. c:function:: struct ice_vsi *ice_vsi_setup(struct ice_pf *pf, enum ice_vsi_type type, struct ice_port_info *pi)

    Set up a VSI by a given type

    :param struct ice_pf \*pf:
        board private structure

    :param enum ice_vsi_type type:
        VSI type

    :param struct ice_port_info \*pi:
        pointer to the port_info instance

.. _`ice_vsi_setup.description`:

Description
-----------

This allocates the sw VSI structure and its queue resources.

Returns pointer to the successfully allocated and configure VSI sw struct on
success, otherwise returns NULL on failure.

.. _`ice_vsi_add_vlan`:

ice_vsi_add_vlan
================

.. c:function:: int ice_vsi_add_vlan(struct ice_vsi *vsi, u16 vid)

    Add vsi membership for given vlan

    :param struct ice_vsi \*vsi:
        the vsi being configured

    :param u16 vid:
        vlan id to be added

.. _`ice_vlan_rx_add_vid`:

ice_vlan_rx_add_vid
===================

.. c:function:: int ice_vlan_rx_add_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Add a vlan id filter to HW offload

    :param struct net_device \*netdev:
        network interface to be adjusted

    :param __always_unused __be16 proto:
        unused protocol

    :param u16 vid:
        vlan id to be added

.. _`ice_vlan_rx_add_vid.description`:

Description
-----------

net_device_ops implementation for adding vlan ids

.. _`ice_vsi_kill_vlan`:

ice_vsi_kill_vlan
=================

.. c:function:: void ice_vsi_kill_vlan(struct ice_vsi *vsi, u16 vid)

    Remove VSI membership for a given VLAN

    :param struct ice_vsi \*vsi:
        the VSI being configured

    :param u16 vid:
        VLAN id to be removed

.. _`ice_vlan_rx_kill_vid`:

ice_vlan_rx_kill_vid
====================

.. c:function:: int ice_vlan_rx_kill_vid(struct net_device *netdev, __always_unused __be16 proto, u16 vid)

    Remove a vlan id filter from HW offload

    :param struct net_device \*netdev:
        network interface to be adjusted

    :param __always_unused __be16 proto:
        unused protocol

    :param u16 vid:
        vlan id to be removed

.. _`ice_vlan_rx_kill_vid.description`:

Description
-----------

net_device_ops implementation for removing vlan ids

.. _`ice_setup_pf_sw`:

ice_setup_pf_sw
===============

.. c:function:: int ice_setup_pf_sw(struct ice_pf *pf)

    Setup the HW switch on startup or after reset

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_setup_pf_sw.description`:

Description
-----------

Returns 0 on success, negative value on failure

.. _`ice_determine_q_usage`:

ice_determine_q_usage
=====================

.. c:function:: void ice_determine_q_usage(struct ice_pf *pf)

    Calculate queue distribution

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_determine_q_usage.description`:

Description
-----------

Return -ENOMEM if we don't get enough queues for all ports

.. _`ice_deinit_pf`:

ice_deinit_pf
=============

.. c:function:: void ice_deinit_pf(struct ice_pf *pf)

    Unrolls initialziations done by ice_init_pf

    :param struct ice_pf \*pf:
        board private structure to initialize

.. _`ice_init_pf`:

ice_init_pf
===========

.. c:function:: void ice_init_pf(struct ice_pf *pf)

    Initialize general software structures (struct ice_pf)

    :param struct ice_pf \*pf:
        board private structure to initialize

.. _`ice_ena_msix_range`:

ice_ena_msix_range
==================

.. c:function:: int ice_ena_msix_range(struct ice_pf *pf)

    Request a range of MSIX vectors from the OS

    :param struct ice_pf \*pf:
        board private structure

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

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_init_interrupt_scheme`:

ice_init_interrupt_scheme
=========================

.. c:function:: int ice_init_interrupt_scheme(struct ice_pf *pf)

    Determine proper interrupt scheme

    :param struct ice_pf \*pf:
        board private structure to initialize

.. _`ice_clear_interrupt_scheme`:

ice_clear_interrupt_scheme
==========================

.. c:function:: void ice_clear_interrupt_scheme(struct ice_pf *pf)

    Undo things done by ice_init_interrupt_scheme

    :param struct ice_pf \*pf:
        board private structure

.. _`ice_probe`:

ice_probe
=========

.. c:function:: int ice_probe(struct pci_dev *pdev, const struct pci_device_id __always_unused *ent)

    Device initialization routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id __always_unused \*ent:
        entry in ice_pci_tbl

.. _`ice_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_remove`:

ice_remove
==========

.. c:function:: void ice_remove(struct pci_dev *pdev)

    Device removal routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`ice_module_init`:

ice_module_init
===============

.. c:function:: int ice_module_init( void)

    Driver registration routine

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*pi:
        pointer to an address structure

.. _`ice_set_mac_address.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_set_rx_mode`:

ice_set_rx_mode
===============

.. c:function:: void ice_set_rx_mode(struct net_device *netdev)

    NDO callback to set the netdev filters

    :param struct net_device \*netdev:
        network interface device structure

.. _`ice_fdb_add`:

ice_fdb_add
===========

.. c:function:: int ice_fdb_add(struct ndmsg *ndm, struct nlattr __always_unused  *tb, struct net_device *dev, const unsigned char *addr, u16 vid, u16 flags)

    add an entry to the hardware database

    :param struct ndmsg \*ndm:
        the input from the stack

    :param struct nlattr __always_unused  \*tb:
        pointer to array of nladdr (unused)

    :param struct net_device \*dev:
        the net device pointer

    :param const unsigned char \*addr:
        the MAC address entry being added

    :param u16 vid:
        VLAN id

    :param u16 flags:
        instructions from stack about fdb operation

.. _`ice_fdb_del`:

ice_fdb_del
===========

.. c:function:: int ice_fdb_del(struct ndmsg *ndm, __always_unused struct nlattr  *tb, struct net_device *dev, const unsigned char *addr, __always_unused u16 vid)

    delete an entry from the hardware database

    :param struct ndmsg \*ndm:
        the input from the stack

    :param __always_unused struct nlattr  \*tb:
        pointer to array of nladdr (unused)

    :param struct net_device \*dev:
        the net device pointer

    :param const unsigned char \*addr:
        the MAC address entry being added

    :param __always_unused u16 vid:
        VLAN id

.. _`ice_vsi_manage_vlan_insertion`:

ice_vsi_manage_vlan_insertion
=============================

.. c:function:: int ice_vsi_manage_vlan_insertion(struct ice_vsi *vsi)

    Manage VLAN insertion for the VSI for Tx

    :param struct ice_vsi \*vsi:
        the vsi being changed

.. _`ice_vsi_manage_vlan_stripping`:

ice_vsi_manage_vlan_stripping
=============================

.. c:function:: int ice_vsi_manage_vlan_stripping(struct ice_vsi *vsi, bool ena)

    Manage VLAN stripping for the VSI for Rx

    :param struct ice_vsi \*vsi:
        the vsi being changed

    :param bool ena:
        boolean value indicating if this is a enable or disable request

.. _`ice_set_features`:

ice_set_features
================

.. c:function:: int ice_set_features(struct net_device *netdev, netdev_features_t features)

    set the netdev feature flags

    :param struct net_device \*netdev:
        ptr to the netdev being adjusted

    :param netdev_features_t features:
        the feature set that the stack is suggesting

.. _`ice_vsi_vlan_setup`:

ice_vsi_vlan_setup
==================

.. c:function:: int ice_vsi_vlan_setup(struct ice_vsi *vsi)

    Setup vlan offload properties on a VSI

    :param struct ice_vsi \*vsi:
        VSI to setup vlan properties for

.. _`ice_restore_vlan`:

ice_restore_vlan
================

.. c:function:: int ice_restore_vlan(struct ice_vsi *vsi)

    Reinstate VLANs when vsi/netdev comes back up

    :param struct ice_vsi \*vsi:
        the VSI being brought back up

.. _`ice_setup_tx_ctx`:

ice_setup_tx_ctx
================

.. c:function:: void ice_setup_tx_ctx(struct ice_ring *ring, struct ice_tlan_ctx *tlan_ctx, u16 pf_q)

    setup a struct ice_tlan_ctx instance

    :param struct ice_ring \*ring:
        The Tx ring to configure

    :param struct ice_tlan_ctx \*tlan_ctx:
        Pointer to the Tx LAN queue context structure to be initialized

    :param u16 pf_q:
        queue index in the PF space

.. _`ice_setup_tx_ctx.description`:

Description
-----------

Configure the Tx descriptor ring in TLAN context.

.. _`ice_vsi_cfg_txqs`:

ice_vsi_cfg_txqs
================

.. c:function:: int ice_vsi_cfg_txqs(struct ice_vsi *vsi)

    Configure the VSI for Tx

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_cfg_txqs.description`:

Description
-----------

Return 0 on success and a negative value on error
Configure the Tx VSI for operation.

.. _`ice_setup_rx_ctx`:

ice_setup_rx_ctx
================

.. c:function:: int ice_setup_rx_ctx(struct ice_ring *ring)

    Configure a receive ring context

    :param struct ice_ring \*ring:
        The Rx ring to configure

.. _`ice_setup_rx_ctx.description`:

Description
-----------

Configure the Rx descriptor ring in RLAN context.

.. _`ice_vsi_cfg_rxqs`:

ice_vsi_cfg_rxqs
================

.. c:function:: int ice_vsi_cfg_rxqs(struct ice_vsi *vsi)

    Configure the VSI for Rx

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_cfg_rxqs.description`:

Description
-----------

Return 0 on success and a negative value on error
Configure the Rx VSI for operation.

.. _`ice_vsi_cfg`:

ice_vsi_cfg
===========

.. c:function:: int ice_vsi_cfg(struct ice_vsi *vsi)

    Setup the VSI

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_vsi_cfg.description`:

Description
-----------

Return 0 on success and negative value on error

.. _`ice_vsi_stop_tx_rings`:

ice_vsi_stop_tx_rings
=====================

.. c:function:: int ice_vsi_stop_tx_rings(struct ice_vsi *vsi)

    Disable Tx rings

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_pf_rxq_wait`:

ice_pf_rxq_wait
===============

.. c:function:: int ice_pf_rxq_wait(struct ice_pf *pf, int pf_q, bool ena)

    Wait for a PF's Rx queue to be enabled or disabled

    :param struct ice_pf \*pf:
        the PF being configured

    :param int pf_q:
        the PF queue

    :param bool ena:
        enable or disable state of the queue

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

    Start or stop a VSI's rx rings

    :param struct ice_vsi \*vsi:
        the VSI being configured

    :param bool ena:
        start or stop the rx rings

.. _`ice_vsi_start_rx_rings`:

ice_vsi_start_rx_rings
======================

.. c:function:: int ice_vsi_start_rx_rings(struct ice_vsi *vsi)

    start VSI's rx rings

    :param struct ice_vsi \*vsi:
        the VSI whose rings are to be started

.. _`ice_vsi_start_rx_rings.description`:

Description
-----------

Returns 0 on success and a negative value on error

.. _`ice_vsi_stop_rx_rings`:

ice_vsi_stop_rx_rings
=====================

.. c:function:: int ice_vsi_stop_rx_rings(struct ice_vsi *vsi)

    stop VSI's rx rings

    :param struct ice_vsi \*vsi:
        the VSI

.. _`ice_vsi_stop_rx_rings.description`:

Description
-----------

Returns 0 on success and a negative value on error

.. _`ice_vsi_stop_tx_rx_rings`:

ice_vsi_stop_tx_rx_rings
========================

.. c:function:: int ice_vsi_stop_tx_rx_rings(struct ice_vsi *vsi)

    stop VSI's tx and rx rings

    :param struct ice_vsi \*vsi:
        the VSI
        Returns 0 on success and a negative value on error

.. _`ice_napi_enable_all`:

ice_napi_enable_all
===================

.. c:function:: void ice_napi_enable_all(struct ice_vsi *vsi)

    Enable NAPI for all q_vectors in the VSI

    :param struct ice_vsi \*vsi:
        the VSI being configured

.. _`ice_up_complete`:

ice_up_complete
===============

.. c:function:: int ice_up_complete(struct ice_vsi *vsi)

    Finish the last steps of bringing up a connection

    :param struct ice_vsi \*vsi:
        The VSI being configured

.. _`ice_up_complete.description`:

Description
-----------

Return 0 on success and negative value on error

.. _`ice_up`:

ice_up
======

.. c:function:: int ice_up(struct ice_vsi *vsi)

    Bring the connection back up after being down

    :param struct ice_vsi \*vsi:
        VSI being configured

.. _`ice_fetch_u64_stats_per_ring`:

ice_fetch_u64_stats_per_ring
============================

.. c:function:: void ice_fetch_u64_stats_per_ring(struct ice_ring *ring, u64 *pkts, u64 *bytes)

    get packets and bytes stats per ring

    :param struct ice_ring \*ring:
        Tx or Rx ring to read stats from

    :param u64 \*pkts:
        packets stats counter

    :param u64 \*bytes:
        bytes stats counter

.. _`ice_fetch_u64_stats_per_ring.description`:

Description
-----------

This function fetches stats from the ring considering the atomic operations
that needs to be performed to read u64 values in 32 bit machine.

.. _`ice_stat_update40`:

ice_stat_update40
=================

.. c:function:: void ice_stat_update40(struct ice_hw *hw, u32 hireg, u32 loreg, bool prev_stat_loaded, u64 *prev_stat, u64 *cur_stat)

    read 40 bit stat from the chip and update stat values

    :param struct ice_hw \*hw:
        ptr to the hardware info

    :param u32 hireg:
        high 32 bit HW register to read from

    :param u32 loreg:
        low 32 bit HW register to read from

    :param bool prev_stat_loaded:
        bool to specify if previous stats are loaded

    :param u64 \*prev_stat:
        ptr to previous loaded stat value

    :param u64 \*cur_stat:
        ptr to current stat value

.. _`ice_stat_update32`:

ice_stat_update32
=================

.. c:function:: void ice_stat_update32(struct ice_hw *hw, u32 reg, bool prev_stat_loaded, u64 *prev_stat, u64 *cur_stat)

    read 32 bit stat from the chip and update stat values

    :param struct ice_hw \*hw:
        ptr to the hardware info

    :param u32 reg:
        HW register to read from

    :param bool prev_stat_loaded:
        bool to specify if previous stats are loaded

    :param u64 \*prev_stat:
        ptr to previous loaded stat value

    :param u64 \*cur_stat:
        ptr to current stat value

.. _`ice_update_eth_stats`:

ice_update_eth_stats
====================

.. c:function:: void ice_update_eth_stats(struct ice_vsi *vsi)

    Update VSI-specific ethernet statistics counters

    :param struct ice_vsi \*vsi:
        the VSI to be updated

.. _`ice_update_vsi_ring_stats`:

ice_update_vsi_ring_stats
=========================

.. c:function:: void ice_update_vsi_ring_stats(struct ice_vsi *vsi)

    Update VSI stats counters

    :param struct ice_vsi \*vsi:
        the VSI to be updated

.. _`ice_update_vsi_stats`:

ice_update_vsi_stats
====================

.. c:function:: void ice_update_vsi_stats(struct ice_vsi *vsi)

    Update VSI stats counters

    :param struct ice_vsi \*vsi:
        the VSI to be updated

.. _`ice_update_pf_stats`:

ice_update_pf_stats
===================

.. c:function:: void ice_update_pf_stats(struct ice_pf *pf)

    Update PF port stats counters

    :param struct ice_pf \*pf:
        PF whose stats needs to be updated

.. _`ice_get_stats64`:

ice_get_stats64
===============

.. c:function:: void ice_get_stats64(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    get statistics for network device structure

    :param struct net_device \*netdev:
        network interface device structure

    :param struct rtnl_link_stats64 \*stats:
        main device statistics structure

.. _`ice_netpoll`:

ice_netpoll
===========

.. c:function:: void ice_netpoll(struct net_device *netdev)

    polling "interrupt" handler

    :param struct net_device \*netdev:
        network interface device structure

.. _`ice_netpoll.description`:

Description
-----------

Used by netconsole to send skbs without having to re-enable interrupts.
This is not called in the normal interrupt path.

.. _`ice_napi_disable_all`:

ice_napi_disable_all
====================

.. c:function:: void ice_napi_disable_all(struct ice_vsi *vsi)

    Disable NAPI for all q_vectors in the VSI

    :param struct ice_vsi \*vsi:
        VSI having NAPI disabled

.. _`ice_down`:

ice_down
========

.. c:function:: int ice_down(struct ice_vsi *vsi)

    Shutdown the connection

    :param struct ice_vsi \*vsi:
        The VSI being stopped

.. _`ice_vsi_setup_tx_rings`:

ice_vsi_setup_tx_rings
======================

.. c:function:: int ice_vsi_setup_tx_rings(struct ice_vsi *vsi)

    Allocate VSI Tx queue resources

    :param struct ice_vsi \*vsi:
        VSI having resources allocated

.. _`ice_vsi_setup_tx_rings.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ice_vsi_setup_rx_rings`:

ice_vsi_setup_rx_rings
======================

.. c:function:: int ice_vsi_setup_rx_rings(struct ice_vsi *vsi)

    Allocate VSI Rx queue resources

    :param struct ice_vsi \*vsi:
        VSI having resources allocated

.. _`ice_vsi_setup_rx_rings.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ice_vsi_req_irq`:

ice_vsi_req_irq
===============

.. c:function:: int ice_vsi_req_irq(struct ice_vsi *vsi, char *basename)

    Request IRQ from the OS

    :param struct ice_vsi \*vsi:
        The VSI IRQ is being requested for

    :param char \*basename:
        name for the vector

.. _`ice_vsi_req_irq.description`:

Description
-----------

Return 0 on success and a negative value on error

.. _`ice_vsi_free_tx_rings`:

ice_vsi_free_tx_rings
=====================

.. c:function:: void ice_vsi_free_tx_rings(struct ice_vsi *vsi)

    Free Tx resources for VSI queues

    :param struct ice_vsi \*vsi:
        the VSI having resources freed

.. _`ice_vsi_free_rx_rings`:

ice_vsi_free_rx_rings
=====================

.. c:function:: void ice_vsi_free_rx_rings(struct ice_vsi *vsi)

    Free Rx resources for VSI queues

    :param struct ice_vsi \*vsi:
        the VSI having resources freed

.. _`ice_vsi_open`:

ice_vsi_open
============

.. c:function:: int ice_vsi_open(struct ice_vsi *vsi)

    Called when a network interface is made active

    :param struct ice_vsi \*vsi:
        the VSI to open

.. _`ice_vsi_open.description`:

Description
-----------

Initialization of the VSI

Returns 0 on success, negative value on error

.. _`ice_vsi_close`:

ice_vsi_close
=============

.. c:function:: void ice_vsi_close(struct ice_vsi *vsi)

    Shut down a VSI

    :param struct ice_vsi \*vsi:
        the VSI being shut down

.. _`ice_rss_clean`:

ice_rss_clean
=============

.. c:function:: void ice_rss_clean(struct ice_vsi *vsi)

    Delete RSS related VSI structures that hold user inputs

    :param struct ice_vsi \*vsi:
        the VSI being removed

.. _`ice_vsi_release`:

ice_vsi_release
===============

.. c:function:: int ice_vsi_release(struct ice_vsi *vsi)

    Delete a VSI and free its resources

    :param struct ice_vsi \*vsi:
        the VSI being removed

.. _`ice_vsi_release.description`:

Description
-----------

Returns 0 on success or < 0 on error

.. _`ice_dis_vsi`:

ice_dis_vsi
===========

.. c:function:: void ice_dis_vsi(struct ice_vsi *vsi)

    pause a VSI

    :param struct ice_vsi \*vsi:
        the VSI being paused

.. _`ice_ena_vsi`:

ice_ena_vsi
===========

.. c:function:: void ice_ena_vsi(struct ice_vsi *vsi)

    resume a VSI

    :param struct ice_vsi \*vsi:
        the VSI being resume

.. _`ice_pf_dis_all_vsi`:

ice_pf_dis_all_vsi
==================

.. c:function:: void ice_pf_dis_all_vsi(struct ice_pf *pf)

    Pause all VSIs on a PF

    :param struct ice_pf \*pf:
        the PF

.. _`ice_pf_ena_all_vsi`:

ice_pf_ena_all_vsi
==================

.. c:function:: void ice_pf_ena_all_vsi(struct ice_pf *pf)

    Resume all VSIs on a PF

    :param struct ice_pf \*pf:
        the PF

.. _`ice_rebuild`:

ice_rebuild
===========

.. c:function:: void ice_rebuild(struct ice_pf *pf)

    rebuild after reset

    :param struct ice_pf \*pf:
        pf to rebuild

.. _`ice_change_mtu`:

ice_change_mtu
==============

.. c:function:: int ice_change_mtu(struct net_device *netdev, int new_mtu)

    NDO callback to change the MTU

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`ice_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_set_rss`:

ice_set_rss
===========

.. c:function:: int ice_set_rss(struct ice_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Set RSS keys and lut

    :param struct ice_vsi \*vsi:
        Pointer to VSI structure

    :param u8 \*seed:
        RSS hash seed

    :param u8 \*lut:
        Lookup table

    :param u16 lut_size:
        Lookup table size

.. _`ice_set_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_get_rss`:

ice_get_rss
===========

.. c:function:: int ice_get_rss(struct ice_vsi *vsi, u8 *seed, u8 *lut, u16 lut_size)

    Get RSS keys and lut

    :param struct ice_vsi \*vsi:
        Pointer to VSI structure

    :param u8 \*seed:
        Buffer to store the keys

    :param u8 \*lut:
        Buffer to store the lookup table entries

    :param u16 lut_size:
        Size of buffer to store the lookup table entries

.. _`ice_get_rss.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ice_open`:

ice_open
========

.. c:function:: int ice_open(struct net_device *netdev)

    Called when a network interface becomes active

    :param struct net_device \*netdev:
        network interface device structure

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

    :param struct net_device \*netdev:
        network interface device structure

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

    :param struct sk_buff \*skb:
        skb buffer

    :param struct net_device __always_unused \*netdev:
        This port's netdev

    :param netdev_features_t features:
        Offload features that the stack believes apply

.. This file was automatic generated / don't edit.

