.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-dpaa2/ethsw/dpsw.c

.. _`dpsw_open`:

dpsw_open
=========

.. c:function:: int dpsw_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpsw_id, u16 *token)

    Open a control session for the specified object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dpsw_id:
        DPSW unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpsw_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the \ :c:func:`dpsw_create`\  function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object

.. _`dpsw_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_close`:

dpsw_close
==========

.. c:function:: int dpsw_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

.. _`dpsw_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpsw_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_enable`:

dpsw_enable
===========

.. c:function:: int dpsw_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable DPSW functionality

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

.. _`dpsw_enable.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_disable`:

dpsw_disable
============

.. c:function:: int dpsw_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable DPSW functionality

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

.. _`dpsw_disable.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_reset`:

dpsw_reset
==========

.. c:function:: int dpsw_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPSW, returns the object to initial state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

.. _`dpsw_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_set_irq_enable`:

dpsw_set_irq_enable
===================

.. c:function:: int dpsw_set_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 en)

    Set overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPCI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 en:
        Interrupt state - enable = 1, disable = 0

.. _`dpsw_set_irq_enable.description`:

Description
-----------

Allows GPP software to control when interrupts are generated.
Each interrupt can have up to 32 causes.  The enable/disable control's the
overall interrupt state. if the interrupt is disabled no causes will cause
an interrupt

.. _`dpsw_set_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_set_irq_mask`:

dpsw_set_irq_mask
=================

.. c:function:: int dpsw_set_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 mask)

    Set interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPCI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 mask:
        Event mask to trigger interrupt;
        each bit:
        0 = ignore event
        1 = consider event for asserting IRQ

.. _`dpsw_set_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpsw_set_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_get_irq_status`:

dpsw_get_irq_status
===================

.. c:function:: int dpsw_get_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *status)

    Get the current status of any pending interrupts

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*status:
        Returned interrupts status - one bit per cause:
        0 = no interrupt pending
        1 = interrupt pending

.. _`dpsw_get_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_clear_irq_status`:

dpsw_clear_irq_status
=====================

.. c:function:: int dpsw_clear_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 status)

    Clear a pending interrupt's status

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPCI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 status:
        bits to clear (W1C) - one bit per cause:
        0 = don't change
        1 = clear status bit

.. _`dpsw_clear_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_get_attributes`:

dpsw_get_attributes
===================

.. c:function:: int dpsw_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpsw_attr *attr)

    Retrieve DPSW attributes

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param struct dpsw_attr \*attr:
        Returned DPSW attributes

.. _`dpsw_get_attributes.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_set_link_cfg`:

dpsw_if_set_link_cfg
====================

.. c:function:: int dpsw_if_set_link_cfg(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, struct dpsw_link_cfg *cfg)

    Set the link configuration.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface id

    :param struct dpsw_link_cfg \*cfg:
        Link configuration

.. _`dpsw_if_set_link_cfg.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpsw_if_get_link_state`:

dpsw_if_get_link_state
======================

.. c:function:: int dpsw_if_get_link_state(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, struct dpsw_link_state *state)

    Return the link state

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface id

    :param struct dpsw_link_state \*state:
        Link state      1 - linkup, 0 - link down or disconnected

.. _`dpsw_if_get_link_state.description`:

Description
-----------

\ ``Return``\       '0' on Success; Error code otherwise.

.. _`dpsw_if_set_flooding`:

dpsw_if_set_flooding
====================

.. c:function:: int dpsw_if_set_flooding(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, u8 en)

    Enable Disable flooding for particular interface

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param u8 en:
        1 - enable, 0 - disable

.. _`dpsw_if_set_flooding.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_set_broadcast`:

dpsw_if_set_broadcast
=====================

.. c:function:: int dpsw_if_set_broadcast(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, u8 en)

    Enable/disable broadcast for particular interface

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param u8 en:
        1 - enable, 0 - disable

.. _`dpsw_if_set_broadcast.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_set_tci`:

dpsw_if_set_tci
===============

.. c:function:: int dpsw_if_set_tci(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, const struct dpsw_tci_cfg *cfg)

    Set default VLAN Tag Control Information (TCI)

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param const struct dpsw_tci_cfg \*cfg:
        Tag Control Information Configuration

.. _`dpsw_if_set_tci.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_get_tci`:

dpsw_if_get_tci
===============

.. c:function:: int dpsw_if_get_tci(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, struct dpsw_tci_cfg *cfg)

    Get default VLAN Tag Control Information (TCI)

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param struct dpsw_tci_cfg \*cfg:
        Tag Control Information Configuration

.. _`dpsw_if_get_tci.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_set_stp`:

dpsw_if_set_stp
===============

.. c:function:: int dpsw_if_set_stp(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, const struct dpsw_stp_cfg *cfg)

    Function sets Spanning Tree Protocol (STP) state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param const struct dpsw_stp_cfg \*cfg:
        STP State configuration parameters

.. _`dpsw_if_set_stp.description`:

Description
-----------

The following STP states are supported -
blocking, listening, learning, forwarding and disabled.

.. _`dpsw_if_set_stp.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_get_counter`:

dpsw_if_get_counter
===================

.. c:function:: int dpsw_if_get_counter(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, enum dpsw_counter type, u64 *counter)

    Get specific counter of particular interface

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param enum dpsw_counter type:
        Counter type

    :param u64 \*counter:
        return value

.. _`dpsw_if_get_counter.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_enable`:

dpsw_if_enable
==============

.. c:function:: int dpsw_if_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id)

    Enable Interface

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

.. _`dpsw_if_enable.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_disable`:

dpsw_if_disable
===============

.. c:function:: int dpsw_if_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id)

    Disable Interface

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

.. _`dpsw_if_disable.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_if_set_max_frame_length`:

dpsw_if_set_max_frame_length
============================

.. c:function:: int dpsw_if_set_max_frame_length(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 if_id, u16 frame_length)

    Set Maximum Receive frame length.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 if_id:
        Interface Identifier

    :param u16 frame_length:
        Maximum Frame Length

.. _`dpsw_if_set_max_frame_length.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_vlan_add`:

dpsw_vlan_add
=============

.. c:function:: int dpsw_vlan_add(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 vlan_id, const struct dpsw_vlan_cfg *cfg)

    Adding new VLAN to DPSW.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 vlan_id:
        VLAN Identifier

    :param const struct dpsw_vlan_cfg \*cfg:
        VLAN configuration

.. _`dpsw_vlan_add.description`:

Description
-----------

Only VLAN ID and FDB ID are required parameters here.
12 bit VLAN ID is defined in IEEE802.1Q.
Adding a duplicate VLAN ID is not allowed.
FDB ID can be shared across multiple VLANs. Shared learning
is obtained by calling dpsw_vlan_add for multiple VLAN IDs
with same fdb_id

.. _`dpsw_vlan_add.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_vlan_add_if`:

dpsw_vlan_add_if
================

.. c:function:: int dpsw_vlan_add_if(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 vlan_id, const struct dpsw_vlan_if_cfg *cfg)

    Adding a set of interfaces to an existing VLAN.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 vlan_id:
        VLAN Identifier

    :param const struct dpsw_vlan_if_cfg \*cfg:
        Set of interfaces to add

.. _`dpsw_vlan_add_if.description`:

Description
-----------

It adds only interfaces not belonging to this VLAN yet,
otherwise an error is generated and an entire command is
ignored. This function can be called numerous times always
providing required interfaces delta.

.. _`dpsw_vlan_add_if.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_vlan_add_if_untagged`:

dpsw_vlan_add_if_untagged
=========================

.. c:function:: int dpsw_vlan_add_if_untagged(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 vlan_id, const struct dpsw_vlan_if_cfg *cfg)

    Defining a set of interfaces that should be transmitted as untagged.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 vlan_id:
        VLAN Identifier

    :param const struct dpsw_vlan_if_cfg \*cfg:
        Set of interfaces that should be transmitted as untagged

.. _`dpsw_vlan_add_if_untagged.description`:

Description
-----------

These interfaces should already belong to this VLAN.
By default all interfaces are transmitted as tagged.
Providing un-existing interface or untagged interface that is
configured untagged already generates an error and the entire
command is ignored.

.. _`dpsw_vlan_add_if_untagged.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_vlan_remove_if`:

dpsw_vlan_remove_if
===================

.. c:function:: int dpsw_vlan_remove_if(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 vlan_id, const struct dpsw_vlan_if_cfg *cfg)

    Remove interfaces from an existing VLAN.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 vlan_id:
        VLAN Identifier

    :param const struct dpsw_vlan_if_cfg \*cfg:
        Set of interfaces that should be removed

.. _`dpsw_vlan_remove_if.description`:

Description
-----------

Interfaces must belong to this VLAN, otherwise an error
is returned and an the command is ignored

.. _`dpsw_vlan_remove_if.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_vlan_remove_if_untagged`:

dpsw_vlan_remove_if_untagged
============================

.. c:function:: int dpsw_vlan_remove_if_untagged(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 vlan_id, const struct dpsw_vlan_if_cfg *cfg)

    Define a set of interfaces that should be converted from transmitted as untagged to transmit as tagged.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 vlan_id:
        VLAN Identifier

    :param const struct dpsw_vlan_if_cfg \*cfg:
        Set of interfaces that should be removed

.. _`dpsw_vlan_remove_if_untagged.description`:

Description
-----------

Interfaces provided by API have to belong to this VLAN and
configured untagged, otherwise an error is returned and the
command is ignored

.. _`dpsw_vlan_remove_if_untagged.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_vlan_remove`:

dpsw_vlan_remove
================

.. c:function:: int dpsw_vlan_remove(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 vlan_id)

    Remove an entire VLAN

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 vlan_id:
        VLAN Identifier

.. _`dpsw_vlan_remove.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_fdb_add_unicast`:

dpsw_fdb_add_unicast
====================

.. c:function:: int dpsw_fdb_add_unicast(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 fdb_id, const struct dpsw_fdb_unicast_cfg *cfg)

    Function adds an unicast entry into MAC lookup table

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 fdb_id:
        Forwarding Database Identifier

    :param const struct dpsw_fdb_unicast_cfg \*cfg:
        Unicast entry configuration

.. _`dpsw_fdb_add_unicast.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_fdb_remove_unicast`:

dpsw_fdb_remove_unicast
=======================

.. c:function:: int dpsw_fdb_remove_unicast(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 fdb_id, const struct dpsw_fdb_unicast_cfg *cfg)

    removes an entry from MAC lookup table

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 fdb_id:
        Forwarding Database Identifier

    :param const struct dpsw_fdb_unicast_cfg \*cfg:
        Unicast entry configuration

.. _`dpsw_fdb_remove_unicast.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_fdb_add_multicast`:

dpsw_fdb_add_multicast
======================

.. c:function:: int dpsw_fdb_add_multicast(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 fdb_id, const struct dpsw_fdb_multicast_cfg *cfg)

    Add a set of egress interfaces to multi-cast group

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 fdb_id:
        Forwarding Database Identifier

    :param const struct dpsw_fdb_multicast_cfg \*cfg:
        Multicast entry configuration

.. _`dpsw_fdb_add_multicast.description`:

Description
-----------

If group doesn't exist, it will be created.
It adds only interfaces not belonging to this multicast group
yet, otherwise error will be generated and the command is
ignored.
This function may be called numerous times always providing
required interfaces delta.

.. _`dpsw_fdb_add_multicast.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_fdb_remove_multicast`:

dpsw_fdb_remove_multicast
=========================

.. c:function:: int dpsw_fdb_remove_multicast(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 fdb_id, const struct dpsw_fdb_multicast_cfg *cfg)

    Removing interfaces from an existing multicast group.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 fdb_id:
        Forwarding Database Identifier

    :param const struct dpsw_fdb_multicast_cfg \*cfg:
        Multicast entry configuration

.. _`dpsw_fdb_remove_multicast.description`:

Description
-----------

Interfaces provided by this API have to exist in the group,
otherwise an error will be returned and an entire command
ignored. If there is no interface left in the group,
an entire group is deleted

.. _`dpsw_fdb_remove_multicast.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_fdb_set_learning_mode`:

dpsw_fdb_set_learning_mode
==========================

.. c:function:: int dpsw_fdb_set_learning_mode(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 fdb_id, enum dpsw_fdb_learning_mode mode)

    Define FDB learning mode

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPSW object

    :param u16 fdb_id:
        Forwarding Database Identifier

    :param enum dpsw_fdb_learning_mode mode:
        Learning mode

.. _`dpsw_fdb_set_learning_mode.return`:

Return
------

Completion status. '0' on Success; Error code otherwise.

.. _`dpsw_get_api_version`:

dpsw_get_api_version
====================

.. c:function:: int dpsw_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path Switch API version

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 \*major_ver:
        Major version of data path switch API

    :param u16 \*minor_ver:
        Minor version of data path switch API

.. _`dpsw_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

