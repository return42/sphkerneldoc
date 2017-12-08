.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-dpaa2/ethernet/dpni.c

.. _`dpni_prepare_key_cfg`:

dpni_prepare_key_cfg
====================

.. c:function:: int dpni_prepare_key_cfg(const struct dpkg_profile_cfg *cfg, u8 *key_cfg_buf)

    function prepare extract parameters

    :param const struct dpkg_profile_cfg \*cfg:
        defining a full Key Generation profile (rule)

    :param u8 \*key_cfg_buf:
        Zeroed 256 bytes of memory before mapping it to DMA

.. _`dpni_prepare_key_cfg.this-function-has-to-be-called-before-the-following-functions`:

This function has to be called before the following functions
-------------------------------------------------------------

- \ :c:func:`dpni_set_rx_tc_dist`\ 
- \ :c:func:`dpni_set_qos_table`\ 

.. _`dpni_open`:

dpni_open
=========

.. c:function:: int dpni_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpni_id, u16 *token)

    Open a control session for the specified object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dpni_id:
        DPNI unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpni_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the \ :c:func:`dpni_create`\  function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object.

.. _`dpni_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_close`:

dpni_close
==========

.. c:function:: int dpni_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

.. _`dpni_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpni_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_pools`:

dpni_set_pools
==============

.. c:function:: int dpni_set_pools(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const struct dpni_pools_cfg *cfg)

    Set buffer pools configuration

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param const struct dpni_pools_cfg \*cfg:
        Buffer pools configuration

.. _`dpni_set_pools.description`:

Description
-----------

mandatory for DPNI operation
warning:Allowed only when DPNI is disabled

.. _`dpni_set_pools.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_enable`:

dpni_enable
===========

.. c:function:: int dpni_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPNI, allow sending and receiving frames.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

.. _`dpni_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_disable`:

dpni_disable
============

.. c:function:: int dpni_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPNI, stop sending and receiving frames.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

.. _`dpni_disable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_is_enabled`:

dpni_is_enabled
===============

.. c:function:: int dpni_is_enabled(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *en)

    Check if the DPNI is enabled.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param int \*en:
        Returns '1' if object is enabled; '0' otherwise

.. _`dpni_is_enabled.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_reset`:

dpni_reset
==========

.. c:function:: int dpni_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPNI, returns the object to initial state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

.. _`dpni_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_irq_enable`:

dpni_set_irq_enable
===================

.. c:function:: int dpni_set_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 en)

    Set overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 en:
        Interrupt state: - enable = 1, disable = 0

.. _`dpni_set_irq_enable.description`:

Description
-----------

Allows GPP software to control when interrupts are generated.
Each interrupt can have up to 32 causes.  The enable/disable control's the
overall interrupt state. if the interrupt is disabled no causes will cause
an interrupt.

.. _`dpni_set_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_irq_enable`:

dpni_get_irq_enable
===================

.. c:function:: int dpni_get_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 *en)

    Get overall interrupt state

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 \*en:
        Returned interrupt state - enable = 1, disable = 0

.. _`dpni_get_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_irq_mask`:

dpni_set_irq_mask
=================

.. c:function:: int dpni_set_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 mask)

    Set interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 mask:
        event mask to trigger interrupt;
        each bit:
        0 = ignore event
        1 = consider event for asserting IRQ

.. _`dpni_set_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpni_set_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_irq_mask`:

dpni_get_irq_mask
=================

.. c:function:: int dpni_get_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *mask)

    Get interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*mask:
        Returned event mask to trigger interrupt

.. _`dpni_get_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dpni_get_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_irq_status`:

dpni_get_irq_status
===================

.. c:function:: int dpni_get_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *status)

    Get the current status of any pending interrupts.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*status:
        Returned interrupts status - one bit per cause:
        0 = no interrupt pending
        1 = interrupt pending

.. _`dpni_get_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_clear_irq_status`:

dpni_clear_irq_status
=====================

.. c:function:: int dpni_clear_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 status)

    Clear a pending interrupt's status

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 status:
        bits to clear (W1C) - one bit per cause:
        0 = don't change
        1 = clear status bit

.. _`dpni_clear_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_attributes`:

dpni_get_attributes
===================

.. c:function:: int dpni_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpni_attr *attr)

    Retrieve DPNI attributes.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param struct dpni_attr \*attr:
        Object's attributes

.. _`dpni_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_errors_behavior`:

dpni_set_errors_behavior
========================

.. c:function:: int dpni_set_errors_behavior(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpni_error_cfg *cfg)

    Set errors behavior

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param struct dpni_error_cfg \*cfg:
        Errors configuration

.. _`dpni_set_errors_behavior.description`:

Description
-----------

this function may be called numerous times with different
error masks

.. _`dpni_set_errors_behavior.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_buffer_layout`:

dpni_get_buffer_layout
======================

.. c:function:: int dpni_get_buffer_layout(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_queue_type qtype, struct dpni_buffer_layout *layout)

    Retrieve buffer layout attributes.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_queue_type qtype:
        Type of queue to retrieve configuration for

    :param struct dpni_buffer_layout \*layout:
        Returns buffer layout attributes

.. _`dpni_get_buffer_layout.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_buffer_layout`:

dpni_set_buffer_layout
======================

.. c:function:: int dpni_set_buffer_layout(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_queue_type qtype, const struct dpni_buffer_layout *layout)

    Set buffer layout configuration.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_queue_type qtype:
        Type of queue this configuration applies to

    :param const struct dpni_buffer_layout \*layout:
        Buffer layout configuration

.. _`dpni_set_buffer_layout.return`:

Return
------

'0' on Success; Error code otherwise.

\ ``warning``\      Allowed only when DPNI is disabled

.. _`dpni_set_offload`:

dpni_set_offload
================

.. c:function:: int dpni_set_offload(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_offload type, u32 config)

    Set DPNI offload configuration.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_offload type:
        Type of DPNI offload

    :param u32 config:
        Offload configuration.
        For checksum offloads, non-zero value enables the offload

.. _`dpni_set_offload.return`:

Return
------

'0' on Success; Error code otherwise.

\ ``warning``\     Allowed only when DPNI is disabled

.. _`dpni_get_qdid`:

dpni_get_qdid
=============

.. c:function:: int dpni_get_qdid(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_queue_type qtype, u16 *qdid)

    Get the Queuing Destination ID (QDID) that should be used for enqueue operations

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_queue_type qtype:
        Type of queue to receive QDID for

    :param u16 \*qdid:
        Returned virtual QDID value that should be used as an argument
        in all enqueue operations

.. _`dpni_get_qdid.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_tx_data_offset`:

dpni_get_tx_data_offset
=======================

.. c:function:: int dpni_get_tx_data_offset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 *data_offset)

    Get the Tx data offset (from start of buffer)

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u16 \*data_offset:
        Tx data offset (from start of buffer)

.. _`dpni_get_tx_data_offset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_link_cfg`:

dpni_set_link_cfg
=================

.. c:function:: int dpni_set_link_cfg(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const struct dpni_link_cfg *cfg)

    set the link configuration.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param const struct dpni_link_cfg \*cfg:
        Link configuration

.. _`dpni_set_link_cfg.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_link_state`:

dpni_get_link_state
===================

.. c:function:: int dpni_get_link_state(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpni_link_state *state)

    Return the link state (either up or down)

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param struct dpni_link_state \*state:
        Returned link state;

.. _`dpni_get_link_state.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_max_frame_length`:

dpni_set_max_frame_length
=========================

.. c:function:: int dpni_set_max_frame_length(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 max_frame_length)

    Set the maximum received frame length.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u16 max_frame_length:
        Maximum received frame length (in
        bytes); frame is discarded if its
        length exceeds this value

.. _`dpni_set_max_frame_length.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_max_frame_length`:

dpni_get_max_frame_length
=========================

.. c:function:: int dpni_get_max_frame_length(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u16 *max_frame_length)

    Get the maximum received frame length.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u16 \*max_frame_length:
        Maximum received frame length (in
        bytes); frame is discarded if its
        length exceeds this value

.. _`dpni_get_max_frame_length.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_multicast_promisc`:

dpni_set_multicast_promisc
==========================

.. c:function:: int dpni_set_multicast_promisc(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int en)

    Enable/disable multicast promiscuous mode

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param int en:
        Set to '1' to enable; '0' to disable

.. _`dpni_set_multicast_promisc.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_multicast_promisc`:

dpni_get_multicast_promisc
==========================

.. c:function:: int dpni_get_multicast_promisc(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *en)

    Get multicast promiscuous mode

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param int \*en:
        Returns '1' if enabled; '0' otherwise

.. _`dpni_get_multicast_promisc.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_unicast_promisc`:

dpni_set_unicast_promisc
========================

.. c:function:: int dpni_set_unicast_promisc(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int en)

    Enable/disable unicast promiscuous mode

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param int en:
        Set to '1' to enable; '0' to disable

.. _`dpni_set_unicast_promisc.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_unicast_promisc`:

dpni_get_unicast_promisc
========================

.. c:function:: int dpni_get_unicast_promisc(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *en)

    Get unicast promiscuous mode

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param int \*en:
        Returns '1' if enabled; '0' otherwise

.. _`dpni_get_unicast_promisc.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_primary_mac_addr`:

dpni_set_primary_mac_addr
=========================

.. c:function:: int dpni_set_primary_mac_addr(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const u8 mac_addr)

    Set the primary MAC address

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param const u8 mac_addr:
        MAC address to set as primary address

.. _`dpni_set_primary_mac_addr.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_primary_mac_addr`:

dpni_get_primary_mac_addr
=========================

.. c:function:: int dpni_get_primary_mac_addr(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 mac_addr)

    Get the primary MAC address

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 mac_addr:
        Returned MAC address

.. _`dpni_get_primary_mac_addr.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_port_mac_addr`:

dpni_get_port_mac_addr
======================

.. c:function:: int dpni_get_port_mac_addr(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 mac_addr)

    Retrieve MAC address associated to the physical port the DPNI is attached to

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 mac_addr:
        MAC address of the physical port, if any, otherwise 0

.. _`dpni_get_port_mac_addr.description`:

Description
-----------

The primary MAC address is not cleared by this operation.

.. _`dpni_get_port_mac_addr.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_add_mac_addr`:

dpni_add_mac_addr
=================

.. c:function:: int dpni_add_mac_addr(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const u8 mac_addr)

    Add MAC address filter

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param const u8 mac_addr:
        MAC address to add

.. _`dpni_add_mac_addr.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_remove_mac_addr`:

dpni_remove_mac_addr
====================

.. c:function:: int dpni_remove_mac_addr(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const u8 mac_addr)

    Remove MAC address filter

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param const u8 mac_addr:
        MAC address to remove

.. _`dpni_remove_mac_addr.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_clear_mac_filters`:

dpni_clear_mac_filters
======================

.. c:function:: int dpni_clear_mac_filters(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int unicast, int multicast)

    Clear all unicast and/or multicast MAC filters

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param int unicast:
        Set to '1' to clear unicast addresses

    :param int multicast:
        Set to '1' to clear multicast addresses

.. _`dpni_clear_mac_filters.description`:

Description
-----------

The primary MAC address is not cleared by this operation.

.. _`dpni_clear_mac_filters.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_rx_tc_dist`:

dpni_set_rx_tc_dist
===================

.. c:function:: int dpni_set_rx_tc_dist(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 tc_id, const struct dpni_rx_tc_dist_cfg *cfg)

    Set Rx traffic class distribution configuration

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 tc_id:
        Traffic class selection (0-7)

    :param const struct dpni_rx_tc_dist_cfg \*cfg:
        Traffic class distribution configuration

.. _`dpni_set_rx_tc_dist.warning`:

warning
-------

if 'dist_mode != DPNI_DIST_MODE_NONE', call \ :c:func:`dpni_prepare_key_cfg`\ 
first to prepare the key_cfg_iova parameter

.. _`dpni_set_rx_tc_dist.return`:

Return
------

'0' on Success; error code otherwise.

.. _`dpni_set_queue`:

dpni_set_queue
==============

.. c:function:: int dpni_set_queue(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_queue_type qtype, u8 tc, u8 index, u8 options, const struct dpni_queue *queue)

    Set queue parameters

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_queue_type qtype:
        Type of queue - all queue types are supported, although
        the command is ignored for Tx

    :param u8 tc:
        Traffic class, in range 0 to NUM_TCS - 1

    :param u8 index:
        Selects the specific queue out of the set allocated for the
        same TC. Value must be in range 0 to NUM_QUEUES - 1

    :param u8 options:
        A combination of DPNI_QUEUE_OPT\_ values that control what
        configuration options are set on the queue

    :param const struct dpni_queue \*queue:
        Queue structure

.. _`dpni_set_queue.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_queue`:

dpni_get_queue
==============

.. c:function:: int dpni_get_queue(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_queue_type qtype, u8 tc, u8 index, struct dpni_queue *queue, struct dpni_queue_id *qid)

    Get queue parameters

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_queue_type qtype:
        Type of queue - all queue types are supported

    :param u8 tc:
        Traffic class, in range 0 to NUM_TCS - 1

    :param u8 index:
        Selects the specific queue out of the set allocated for the
        same TC. Value must be in range 0 to NUM_QUEUES - 1

    :param struct dpni_queue \*queue:
        Queue configuration structure

    :param struct dpni_queue_id \*qid:
        Queue identification

.. _`dpni_get_queue.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_statistics`:

dpni_get_statistics
===================

.. c:function:: int dpni_get_statistics(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 page, union dpni_statistics *stat)

    Get DPNI statistics

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param u8 page:
        Selects the statistics page to retrieve, see
        DPNI_GET_STATISTICS output. Pages are numbered 0 to 2.

    :param union dpni_statistics \*stat:
        Structure containing the statistics

.. _`dpni_get_statistics.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_set_taildrop`:

dpni_set_taildrop
=================

.. c:function:: int dpni_set_taildrop(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_congestion_point cg_point, enum dpni_queue_type qtype, u8 tc, u8 index, struct dpni_taildrop *taildrop)

    Set taildrop per queue or TC

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_congestion_point cg_point:
        Congestion point

    :param enum dpni_queue_type qtype:
        *undescribed*

    :param u8 tc:
        Traffic class to apply this taildrop to

    :param u8 index:
        *undescribed*

    :param struct dpni_taildrop \*taildrop:
        Taildrop structure

.. _`dpni_set_taildrop.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_taildrop`:

dpni_get_taildrop
=================

.. c:function:: int dpni_get_taildrop(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, enum dpni_congestion_point cg_point, enum dpni_queue_type qtype, u8 tc, u8 index, struct dpni_taildrop *taildrop)

    Get taildrop information

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPNI object

    :param enum dpni_congestion_point cg_point:
        Congestion point

    :param enum dpni_queue_type qtype:
        *undescribed*

    :param u8 tc:
        Traffic class to apply this taildrop to

    :param u8 index:
        *undescribed*

    :param struct dpni_taildrop \*taildrop:
        Taildrop structure

.. _`dpni_get_taildrop.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpni_get_api_version`:

dpni_get_api_version
====================

.. c:function:: int dpni_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path Network Interface API version

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 \*major_ver:
        Major version of data path network interface API

    :param u16 \*minor_ver:
        Minor version of data path network interface API

.. _`dpni_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

