.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dprc.c

.. _`dprc_open`:

dprc_open
=========

.. c:function:: int dprc_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int container_id, u16 *token)

    Open DPRC object for use

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int container_id:
        Container ID to open

    :param u16 \*token:
        Returned token of DPRC object

.. _`dprc_open.return`:

Return
------

'0' on Success; Error code otherwise.

\ ``warning``\      Required before any operation on the object.

.. _`dprc_close`:

dprc_close
==========

.. c:function:: int dprc_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

.. _`dprc_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dprc_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_create_container`:

dprc_create_container
=====================

.. c:function:: int dprc_create_container(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dprc_cfg *cfg, int *child_container_id, u64 *child_portal_offset)

    Create child container

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param struct dprc_cfg \*cfg:
        Child container configuration

    :param int \*child_container_id:
        Returned child container ID

    :param u64 \*child_portal_offset:
        Returned child portal offset from MC portal base

.. _`dprc_create_container.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_destroy_container`:

dprc_destroy_container
======================

.. c:function:: int dprc_destroy_container(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int child_container_id)

    Destroy child container.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int child_container_id:
        ID of the container to destroy

.. _`dprc_destroy_container.description`:

Description
-----------

This function terminates the child container, so following this call the
child container ID becomes invalid.

.. _`dprc_destroy_container.notes`:

Notes
-----

- All resources and objects of the destroyed container are returned to the
parent container or destroyed if were created be the destroyed container.
- This function destroy all the child containers of the specified
container prior to destroying the container itself.

.. _`dprc_destroy_container.warning`:

warning
-------

Only the parent container is allowed to destroy a child policy
Container 0 can't be destroyed

.. _`dprc_destroy_container.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_reset_container`:

dprc_reset_container
====================

.. c:function:: int dprc_reset_container(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int child_container_id)

    Reset child container.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int child_container_id:
        ID of the container to reset

.. _`dprc_reset_container.description`:

Description
-----------

In case a software context crashes or becomes non-responsive, the parent
may wish to reset its resources container before the software context is
restarted.

This routine informs all objects assigned to the child container that the
container is being reset, so they may perform any cleanup operations that are
needed. All objects handles that were owned by the child container shall be
closed.

Note that such request may be submitted even if the child software context
has not crashed, but the resulting object cleanup operations will not be
aware of that.

.. _`dprc_reset_container.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_irq`:

dprc_get_irq
============

.. c:function:: int dprc_get_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, int *type, struct dprc_irq_cfg *irq_cfg)

    Get IRQ information from the DPRC.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param int \*type:
        Interrupt type: 0 represents message interrupt
        type (both irq_addr and irq_val are valid)

    :param struct dprc_irq_cfg \*irq_cfg:
        IRQ attributes

.. _`dprc_get_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_set_irq`:

dprc_set_irq
============

.. c:function:: int dprc_set_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, struct dprc_irq_cfg *irq_cfg)

    Set IRQ information for the DPRC to trigger an interrupt.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        Identifies the interrupt index to configure

    :param struct dprc_irq_cfg \*irq_cfg:
        IRQ configuration

.. _`dprc_set_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_irq_enable`:

dprc_get_irq_enable
===================

.. c:function:: int dprc_get_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 *en)

    Get overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 \*en:
        Returned interrupt state - enable = 1, disable = 0

.. _`dprc_get_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_set_irq_enable`:

dprc_set_irq_enable
===================

.. c:function:: int dprc_set_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 en)

    Set overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 en:
        Interrupt state - enable = 1, disable = 0

.. _`dprc_set_irq_enable.description`:

Description
-----------

Allows GPP software to control when interrupts are generated.
Each interrupt can have up to 32 causes.  The enable/disable control's the
overall interrupt state. if the interrupt is disabled no causes will cause
an interrupt.

.. _`dprc_set_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_irq_mask`:

dprc_get_irq_mask
=================

.. c:function:: int dprc_get_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *mask)

    Get interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*mask:
        Returned event mask to trigger interrupt

.. _`dprc_get_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dprc_get_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_set_irq_mask`:

dprc_set_irq_mask
=================

.. c:function:: int dprc_set_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 mask)

    Set interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 mask:
        event mask to trigger interrupt;
        each bit:
        0 = ignore event
        1 = consider event for asserting irq

.. _`dprc_set_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dprc_set_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_irq_status`:

dprc_get_irq_status
===================

.. c:function:: int dprc_get_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *status)

    Get the current status of any pending interrupts.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*status:
        Returned interrupts status - one bit per cause:
        0 = no interrupt pending
        1 = interrupt pending

.. _`dprc_get_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_clear_irq_status`:

dprc_clear_irq_status
=====================

.. c:function:: int dprc_clear_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 status)

    Clear a pending interrupt's status

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 status:
        bits to clear (W1C) - one bit per cause:
        0 = don't change
        1 = clear status bit

.. _`dprc_clear_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_attributes`:

dprc_get_attributes
===================

.. c:function:: int dprc_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dprc_attributes *attr)

    Obtains container attributes

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object
        \ ``attributes``\   Returned container attributes

    :param struct dprc_attributes \*attr:
        *undescribed*

.. _`dprc_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_set_res_quota`:

dprc_set_res_quota
==================

.. c:function:: int dprc_set_res_quota(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int child_container_id, char *type, u16 quota)

    Set allocation policy for a specific resource/object type in a child container

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int child_container_id:
        ID of the child container

    :param char \*type:
        Resource/object type

    :param u16 quota:
        Sets the maximum number of resources of the selected type
        that the child container is allowed to allocate from its parent;
        when quota is set to -1, the policy is the same as container's
        general policy.

.. _`dprc_set_res_quota.description`:

Description
-----------

Allocation policy determines whether or not a container may allocate
resources from its parent. Each container has a 'global' allocation policy
that is set when the container is created.

This function sets allocation policy for a specific resource type.
The default policy for all resource types matches the container's 'global'
allocation policy.

.. _`dprc_set_res_quota.return`:

Return
------

'0' on Success; Error code otherwise.

\ ``warning``\      Only the parent container is allowed to change a child policy.

.. _`dprc_get_res_quota`:

dprc_get_res_quota
==================

.. c:function:: int dprc_get_res_quota(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int child_container_id, char *type, u16 *quota)

    Gets the allocation policy of a specific resource/object type in a child container

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object
        \ ``child_container_id``\ ; ID of the child container

    :param int child_container_id:
        *undescribed*

    :param char \*type:
        resource/object type

    :param u16 \*quota:
        Returnes the maximum number of resources of the selected type
        that the child container is allowed to allocate from the parent;
        when quota is set to -1, the policy is the same as container's
        general policy.

.. _`dprc_get_res_quota.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_assign`:

dprc_assign
===========

.. c:function:: int dprc_assign(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int container_id, struct dprc_res_req *res_req)

    Assigns objects or resource to a child container.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int container_id:
        ID of the child container

    :param struct dprc_res_req \*res_req:
        Describes the type and amount of resources to
        assign to the given container

.. _`dprc_assign.description`:

Description
-----------

Assignment is usually done by a parent (this DPRC) to one of its child
containers.

According to the DPRC allocation policy, the assigned resources may be taken
(allocated) from the container's ancestors, if not enough resources are
available in the container itself.

The type of assignment depends on the dprc_res_req options, as follows:
- DPRC_RES_REQ_OPT_EXPLICIT: indicates that assigned resources should have
the explicit base ID specified at the id_base_align field of res_req.
- DPRC_RES_REQ_OPT_ALIGNED: indicates that the assigned resources should be
aligned to the value given at id_base_align field of res_req.
- DPRC_RES_REQ_OPT_PLUGGED: Relevant only for object assignment,
and indicates that the object must be set to the plugged state.

A container may use this function with its own ID in order to change a
object state to plugged or unplugged.

If IRQ information has been set in the child DPRC, it will signal an
interrupt following every change in its object assignment.

.. _`dprc_assign.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_unassign`:

dprc_unassign
=============

.. c:function:: int dprc_unassign(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int child_container_id, struct dprc_res_req *res_req)

    Un-assigns objects or resources from a child container and moves them into this (parent) DPRC.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int child_container_id:
        ID of the child container

    :param struct dprc_res_req \*res_req:
        Describes the type and amount of resources to un-assign from
        the child container

.. _`dprc_unassign.description`:

Description
-----------

Un-assignment of objects can succeed only if the object is not in the
plugged or opened state.

.. _`dprc_unassign.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_pool_count`:

dprc_get_pool_count
===================

.. c:function:: int dprc_get_pool_count(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *pool_count)

    Get the number of dprc's pools

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int \*pool_count:
        Returned number of resource pools in the dprc

.. _`dprc_get_pool_count.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_pool`:

dprc_get_pool
=============

.. c:function:: int dprc_get_pool(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int pool_index, char *type)

    Get the type (string) of a certain dprc's pool

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object
        \ ``pool_index``\ ; Index of the pool to be queried (< pool_count)

    :param int pool_index:
        *undescribed*

    :param char \*type:
        The type of the pool

.. _`dprc_get_pool.description`:

Description
-----------

The pool types retrieved one by one by incrementing
pool_index up to (not including) the value of pool_count returned
from \ :c:func:`dprc_get_pool_count`\ . \ :c:func:`dprc_get_pool_count`\  must
be called prior to \ :c:func:`dprc_get_pool`\ .

.. _`dprc_get_pool.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_obj_count`:

dprc_get_obj_count
==================

.. c:function:: int dprc_get_obj_count(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *obj_count)

    Obtains the number of objects in the DPRC

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int \*obj_count:
        Number of objects assigned to the DPRC

.. _`dprc_get_obj_count.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_obj`:

dprc_get_obj
============

.. c:function:: int dprc_get_obj(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int obj_index, struct dprc_obj_desc *obj_desc)

    Get general information on an object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int obj_index:
        Index of the object to be queried (< obj_count)

    :param struct dprc_obj_desc \*obj_desc:
        Returns the requested object descriptor

.. _`dprc_get_obj.description`:

Description
-----------

The object descriptors are retrieved one by one by incrementing
obj_index up to (not including) the value of obj_count returned
from \ :c:func:`dprc_get_obj_count`\ . \ :c:func:`dprc_get_obj_count`\  must
be called prior to \ :c:func:`dprc_get_obj`\ .

.. _`dprc_get_obj.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_obj_desc`:

dprc_get_obj_desc
=================

.. c:function:: int dprc_get_obj_desc(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *obj_type, int obj_id, struct dprc_obj_desc *obj_desc)

    Get object descriptor.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param char \*obj_type:
        The type of the object to get its descriptor.

    :param int obj_id:
        The id of the object to get its descriptor

    :param struct dprc_obj_desc \*obj_desc:
        The returned descriptor to fill and return to the user

.. _`dprc_get_obj_desc.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_set_obj_irq`:

dprc_set_obj_irq
================

.. c:function:: int dprc_set_obj_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *obj_type, int obj_id, u8 irq_index, struct dprc_irq_cfg *irq_cfg)

    Set IRQ information for object to trigger an interrupt.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param char \*obj_type:
        Type of the object to set its IRQ

    :param int obj_id:
        ID of the object to set its IRQ

    :param u8 irq_index:
        The interrupt index to configure

    :param struct dprc_irq_cfg \*irq_cfg:
        IRQ configuration

.. _`dprc_set_obj_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_obj_irq`:

dprc_get_obj_irq
================

.. c:function:: int dprc_get_obj_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *obj_type, int obj_id, u8 irq_index, int *type, struct dprc_irq_cfg *irq_cfg)

    Get IRQ information from object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param char \*obj_type:
        Type od the object to get its IRQ

    :param int obj_id:
        ID of the object to get its IRQ

    :param u8 irq_index:
        The interrupt index to configure

    :param int \*type:
        Interrupt type: 0 represents message interrupt
        type (both irq_addr and irq_val are valid)

    :param struct dprc_irq_cfg \*irq_cfg:
        The returned IRQ attributes

.. _`dprc_get_obj_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_res_count`:

dprc_get_res_count
==================

.. c:function:: int dprc_get_res_count(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *type, int *res_count)

    Obtains the number of free resources that are assigned to this container, by pool type

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param char \*type:
        pool type

    :param int \*res_count:
        Returned number of free resources of the given
        resource type that are assigned to this DPRC

.. _`dprc_get_res_count.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_res_ids`:

dprc_get_res_ids
================

.. c:function:: int dprc_get_res_ids(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *type, struct dprc_res_ids_range_desc *range_desc)

    Obtains IDs of free resources in the container

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param char \*type:
        pool type

    :param struct dprc_res_ids_range_desc \*range_desc:
        range descriptor

.. _`dprc_get_res_ids.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_obj_region`:

dprc_get_obj_region
===================

.. c:function:: int dprc_get_obj_region(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *obj_type, int obj_id, u8 region_index, struct dprc_region_desc *region_desc)

    Get region information for a specified object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object
        \ ``obj_type``\ ;   Object type as returned in \ :c:func:`dprc_get_obj`\ 

    :param char \*obj_type:
        *undescribed*

    :param int obj_id:
        Unique object instance as returned in \ :c:func:`dprc_get_obj`\ 

    :param u8 region_index:
        The specific region to query

    :param struct dprc_region_desc \*region_desc:
        Returns the requested region descriptor

.. _`dprc_get_obj_region.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_set_obj_label`:

dprc_set_obj_label
==================

.. c:function:: int dprc_set_obj_label(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, char *obj_type, int obj_id, char *label)

    Set object label.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param char \*obj_type:
        Object's type

    :param int obj_id:
        Object's ID

    :param char \*label:
        The required label. The maximum length is 16 chars.

.. _`dprc_set_obj_label.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_connect`:

dprc_connect
============

.. c:function:: int dprc_connect(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const struct dprc_endpoint *endpoint1, const struct dprc_endpoint *endpoint2, const struct dprc_connection_cfg *cfg)

    Connect two endpoints to create a network link between them

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param const struct dprc_endpoint \*endpoint1:
        Endpoint 1 configuration parameters

    :param const struct dprc_endpoint \*endpoint2:
        Endpoint 2 configuration parameters

    :param const struct dprc_connection_cfg \*cfg:
        Connection configuration. The connection configuration is ignored for
        connections made to DPMAC objects, where rate is retrieved from the
        MAC configuration.

.. _`dprc_connect.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_disconnect`:

dprc_disconnect
===============

.. c:function:: int dprc_disconnect(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const struct dprc_endpoint *endpoint)

    Disconnect one endpoint to remove its network connection

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param const struct dprc_endpoint \*endpoint:
        Endpoint configuration parameters

.. _`dprc_disconnect.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_connection`:

dprc_get_connection
===================

.. c:function:: int dprc_get_connection(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const struct dprc_endpoint *endpoint1, struct dprc_endpoint *endpoint2, int *state)

    Get connected endpoint and link status if connection exists.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param const struct dprc_endpoint \*endpoint1:
        Endpoint 1 configuration parameters

    :param struct dprc_endpoint \*endpoint2:
        Returned endpoint 2 configuration parameters

    :param int \*state:
        Returned link state:
        1 - link is up;
        0 - link is down;
        -1 - no connection (endpoint2 information is irrelevant)

.. _`dprc_get_connection.return`:

Return
------

'0' on Success; -ENAVAIL if connection does not exist.

.. This file was automatic generated / don't edit.

