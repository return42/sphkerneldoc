.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/dprc.c

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

.. c:function:: int dprc_get_obj(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int obj_index, struct fsl_mc_obj_desc *obj_desc)

    Get general information on an object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRC object

    :param int obj_index:
        Index of the object to be queried (< obj_count)

    :param struct fsl_mc_obj_desc \*obj_desc:
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

.. _`dprc_get_api_version`:

dprc_get_api_version
====================

.. c:function:: int dprc_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path Resource Container API version

    :param struct fsl_mc_io \*mc_io:
        Pointer to Mc portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 \*major_ver:
        Major version of Data Path Resource Container API

    :param u16 \*minor_ver:
        Minor version of Data Path Resource Container API

.. _`dprc_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprc_get_container_id`:

dprc_get_container_id
=====================

.. c:function:: int dprc_get_container_id(struct fsl_mc_io *mc_io, u32 cmd_flags, int *container_id)

    Get container ID associated with a given portal.

    :param struct fsl_mc_io \*mc_io:
        Pointer to Mc portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int \*container_id:
        Requested container id

.. _`dprc_get_container_id.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

