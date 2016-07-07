.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpmcp.c

.. _`dpmcp_open`:

dpmcp_open
==========

.. c:function:: int dpmcp_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpmcp_id, u16 *token)

    Open a control session for the specified object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dpmcp_id:
        DPMCP unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpmcp_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the dpmcp_create function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object

.. _`dpmcp_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_close`:

dpmcp_close
===========

.. c:function:: int dpmcp_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

.. _`dpmcp_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpmcp_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_create`:

dpmcp_create
============

.. c:function:: int dpmcp_create(struct fsl_mc_io *mc_io, u32 cmd_flags, const struct dpmcp_cfg *cfg, u16 *token)

    Create the DPMCP object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param const struct dpmcp_cfg \*cfg:
        Configuration structure

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpmcp_create.description`:

Description
-----------

Create the DPMCP object, allocate required resources and
perform required initialization.

The object can be created either by declaring it in the
DPL file, or by calling this function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent calls to
this specific object. For objects that are created using the
DPL file, call dpmcp_open function to get an authentication
token first.

.. _`dpmcp_create.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_destroy`:

dpmcp_destroy
=============

.. c:function:: int dpmcp_destroy(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Destroy the DPMCP object and release all its resources.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

.. _`dpmcp_destroy.return`:

Return
------

'0' on Success; error code otherwise.

.. _`dpmcp_reset`:

dpmcp_reset
===========

.. c:function:: int dpmcp_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPMCP, returns the object to initial state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

.. _`dpmcp_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_set_irq`:

dpmcp_set_irq
=============

.. c:function:: int dpmcp_set_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, struct dpmcp_irq_cfg *irq_cfg)

    Set IRQ information for the DPMCP to trigger an interrupt.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        Identifies the interrupt index to configure

    :param struct dpmcp_irq_cfg \*irq_cfg:
        IRQ configuration

.. _`dpmcp_set_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_get_irq`:

dpmcp_get_irq
=============

.. c:function:: int dpmcp_get_irq(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, int *type, struct dpmcp_irq_cfg *irq_cfg)

    Get IRQ information from the DPMCP.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        The interrupt index to configure

    :param int \*type:
        Interrupt type: 0 represents message interrupt
        type (both irq_addr and irq_val are valid)

    :param struct dpmcp_irq_cfg \*irq_cfg:
        IRQ attributes

.. _`dpmcp_get_irq.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_set_irq_enable`:

dpmcp_set_irq_enable
====================

.. c:function:: int dpmcp_set_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 en)

    Set overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 en:
        Interrupt state - enable = 1, disable = 0

.. _`dpmcp_set_irq_enable.description`:

Description
-----------

Allows GPP software to control when interrupts are generated.
Each interrupt can have up to 32 causes.  The enable/disable control's the
overall interrupt state. if the interrupt is disabled no causes will cause
an interrupt.

.. _`dpmcp_set_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_get_irq_enable`:

dpmcp_get_irq_enable
====================

.. c:function:: int dpmcp_get_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 *en)

    Get overall interrupt state

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 \*en:
        Returned interrupt state - enable = 1, disable = 0

.. _`dpmcp_get_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_set_irq_mask`:

dpmcp_set_irq_mask
==================

.. c:function:: int dpmcp_set_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 mask)

    Set interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 mask:
        Event mask to trigger interrupt;
        each bit:
        0 = ignore event
        1 = consider event for asserting IRQ

.. _`dpmcp_set_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpmcp_set_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_get_irq_mask`:

dpmcp_get_irq_mask
==================

.. c:function:: int dpmcp_get_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *mask)

    Get interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*mask:
        Returned event mask to trigger interrupt

.. _`dpmcp_get_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpmcp_get_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_get_irq_status`:

dpmcp_get_irq_status
====================

.. c:function:: int dpmcp_get_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *status)

    Get the current status of any pending interrupts.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*status:
        Returned interrupts status - one bit per cause:
        0 = no interrupt pending
        1 = interrupt pending

.. _`dpmcp_get_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_get_attributes`:

dpmcp_get_attributes
====================

.. c:function:: int dpmcp_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpmcp_attr *attr)

    Retrieve DPMCP attributes.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

    :param struct dpmcp_attr \*attr:
        Returned object's attributes

.. _`dpmcp_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

