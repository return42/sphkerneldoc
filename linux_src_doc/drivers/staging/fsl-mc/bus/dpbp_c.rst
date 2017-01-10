.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpbp.c

.. _`dpbp_open`:

dpbp_open
=========

.. c:function:: int dpbp_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpbp_id, u16 *token)

    Open a control session for the specified object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dpbp_id:
        DPBP unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpbp_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the dpbp_create function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object

.. _`dpbp_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_close`:

dpbp_close
==========

.. c:function:: int dpbp_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

.. _`dpbp_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpbp_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_create`:

dpbp_create
===========

.. c:function:: int dpbp_create(struct fsl_mc_io *mc_io, u16 dprc_token, u32 cmd_flags, const struct dpbp_cfg *cfg, u32 *obj_id)

    Create the DPBP object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u16 dprc_token:
        Parent container token; '0' for default container

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param const struct dpbp_cfg \*cfg:
        Configuration structure

    :param u32 \*obj_id:
        Returned object id; use in subsequent API calls

.. _`dpbp_create.description`:

Description
-----------

Create the DPBP object, allocate required resources and
perform required initialization.

This function accepts an authentication token of a parent
container that this object should be assigned to and returns
an object id. This object_id will be used in all subsequent calls to
this specific object.

.. _`dpbp_create.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_destroy`:

dpbp_destroy
============

.. c:function:: int dpbp_destroy(struct fsl_mc_io *mc_io, u16 dprc_token, u32 cmd_flags, u32 obj_id)

    Destroy the DPBP object and release all its resources.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u16 dprc_token:
        Parent container token; '0' for default container

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u32 obj_id:
        ID of DPBP object

.. _`dpbp_destroy.return`:

Return
------

'0' on Success; error code otherwise.

.. _`dpbp_enable`:

dpbp_enable
===========

.. c:function:: int dpbp_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPBP.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

.. _`dpbp_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_disable`:

dpbp_disable
============

.. c:function:: int dpbp_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPBP.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

.. _`dpbp_disable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_is_enabled`:

dpbp_is_enabled
===============

.. c:function:: int dpbp_is_enabled(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *en)

    Check if the DPBP is enabled.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param int \*en:
        Returns '1' if object is enabled; '0' otherwise

.. _`dpbp_is_enabled.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_reset`:

dpbp_reset
==========

.. c:function:: int dpbp_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPBP, returns the object to initial state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

.. _`dpbp_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_set_irq`:

dpbp_set_irq
============

.. c:function:: int dpbp_set_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, struct dpbp_irq_cfg *irq_cfg)

    Set IRQ information for the DPBP to trigger an interrupt.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        Identifies the interrupt index to configure

    :param struct dpbp_irq_cfg \*irq_cfg:
        IRQ configuration

.. _`dpbp_set_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_irq`:

dpbp_get_irq
============

.. c:function:: int dpbp_get_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, int *type, struct dpbp_irq_cfg *irq_cfg)

    Get IRQ information from the DPBP.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param int \*type:
        Interrupt type: 0 represents message interrupt
        type (both irq_addr and irq_val are valid)

    :param struct dpbp_irq_cfg \*irq_cfg:
        IRQ attributes

.. _`dpbp_get_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_set_irq_enable`:

dpbp_set_irq_enable
===================

.. c:function:: int dpbp_set_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 en)

    Set overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 en:
        Interrupt state - enable = 1, disable = 0

.. _`dpbp_set_irq_enable.description`:

Description
-----------

Allows GPP software to control when interrupts are generated.
Each interrupt can have up to 32 causes.  The enable/disable control's the
overall interrupt state. if the interrupt is disabled no causes will cause
an interrupt.

.. _`dpbp_set_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_irq_enable`:

dpbp_get_irq_enable
===================

.. c:function:: int dpbp_get_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 *en)

    Get overall interrupt state

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 \*en:
        Returned interrupt state - enable = 1, disable = 0

.. _`dpbp_get_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_set_irq_mask`:

dpbp_set_irq_mask
=================

.. c:function:: int dpbp_set_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 mask)

    Set interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 mask:
        Event mask to trigger interrupt;
        each bit:
        0 = ignore event
        1 = consider event for asserting IRQ

.. _`dpbp_set_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpbp_set_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_irq_mask`:

dpbp_get_irq_mask
=================

.. c:function:: int dpbp_get_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *mask)

    Get interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*mask:
        Returned event mask to trigger interrupt

.. _`dpbp_get_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpbp_get_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_irq_status`:

dpbp_get_irq_status
===================

.. c:function:: int dpbp_get_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *status)

    Get the current status of any pending interrupts.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*status:
        Returned interrupts status - one bit per cause:
        0 = no interrupt pending
        1 = interrupt pending

.. _`dpbp_get_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_clear_irq_status`:

dpbp_clear_irq_status
=====================

.. c:function:: int dpbp_clear_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 status)

    Clear a pending interrupt's status

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 status:
        Bits to clear (W1C) - one bit per cause:
        0 = don't change
        1 = clear status bit

.. _`dpbp_clear_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_attributes`:

dpbp_get_attributes
===================

.. c:function:: int dpbp_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpbp_attr *attr)

    Retrieve DPBP attributes.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param struct dpbp_attr \*attr:
        Returned object's attributes

.. _`dpbp_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_set_notifications`:

dpbp_set_notifications
======================

.. c:function:: int dpbp_set_notifications(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpbp_notification_cfg *cfg)

    Set notifications towards software

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param struct dpbp_notification_cfg \*cfg:
        notifications configuration

.. _`dpbp_set_notifications.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_notifications`:

dpbp_get_notifications
======================

.. c:function:: int dpbp_get_notifications(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpbp_notification_cfg *cfg)

    Get the notifications configuration

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPBP object

    :param struct dpbp_notification_cfg \*cfg:
        notifications configuration

.. _`dpbp_get_notifications.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_api_version`:

dpbp_get_api_version
====================

.. c:function:: int dpbp_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path Buffer Pool API version

    :param struct fsl_mc_io \*mc_io:
        Pointer to Mc portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 \*major_ver:
        Major version of Buffer Pool API

    :param u16 \*minor_ver:
        Minor version of Buffer Pool API

.. _`dpbp_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

