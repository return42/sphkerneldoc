.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_common.c

.. _`i40e_set_mac_type`:

i40e_set_mac_type
=================

.. c:function:: i40e_status i40e_set_mac_type(struct i40e_hw *hw)

    Sets MAC type

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

.. _`i40e_set_mac_type.description`:

Description
-----------

This function sets the mac type of the adapter based on the
vendor ID and device ID stored in the hw structure.

.. _`i40e_aq_str`:

i40e_aq_str
===========

.. c:function:: const char *i40e_aq_str(struct i40e_hw *hw, enum i40e_admin_queue_err aq_err)

    convert AQ err code to a string

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param aq_err:
        the AQ error code to convert
    :type aq_err: enum i40e_admin_queue_err

.. _`i40e_stat_str`:

i40e_stat_str
=============

.. c:function:: const char *i40e_stat_str(struct i40e_hw *hw, i40e_status stat_err)

    convert status err code to a string

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param stat_err:
        the status error code to convert
    :type stat_err: i40e_status

.. _`i40e_debug_aq`:

i40e_debug_aq
=============

.. c:function:: void i40e_debug_aq(struct i40e_hw *hw, enum i40e_debug_mask mask, void *desc, void *buffer, u16 buf_len)

    :param hw:
        debug mask related to admin queue
    :type hw: struct i40e_hw \*

    :param mask:
        debug mask
    :type mask: enum i40e_debug_mask

    :param desc:
        pointer to admin queue descriptor
    :type desc: void \*

    :param buffer:
        pointer to command buffer
    :type buffer: void \*

    :param buf_len:
        max length of buffer
    :type buf_len: u16

.. _`i40e_debug_aq.description`:

Description
-----------

Dumps debug log about adminq command with descriptor contents.

.. _`i40e_check_asq_alive`:

i40e_check_asq_alive
====================

.. c:function:: bool i40e_check_asq_alive(struct i40e_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_check_asq_alive.description`:

Description
-----------

Returns true if Queue is enabled else false.

.. _`i40e_aq_queue_shutdown`:

i40e_aq_queue_shutdown
======================

.. c:function:: i40e_status i40e_aq_queue_shutdown(struct i40e_hw *hw, bool unloading)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param unloading:
        is the driver unloading itself
    :type unloading: bool

.. _`i40e_aq_queue_shutdown.description`:

Description
-----------

Tell the Firmware that we're shutting down the AdminQ and whether
or not the driver is unloading as well.

.. _`i40e_aq_get_set_rss_lut`:

i40e_aq_get_set_rss_lut
=======================

.. c:function:: i40e_status i40e_aq_get_set_rss_lut(struct i40e_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size, bool set)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param pf_lut:
        for PF table set true, for VSI table set false
    :type pf_lut: bool

    :param lut:
        pointer to the lut buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the lut buffer
    :type lut_size: u16

    :param set:
        set true to set the table, false to get the table
    :type set: bool

.. _`i40e_aq_get_set_rss_lut.description`:

Description
-----------

Internal function to get or set RSS look up table

.. _`i40e_aq_get_rss_lut`:

i40e_aq_get_rss_lut
===================

.. c:function:: i40e_status i40e_aq_get_rss_lut(struct i40e_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param pf_lut:
        for PF table set true, for VSI table set false
    :type pf_lut: bool

    :param lut:
        pointer to the lut buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the lut buffer
    :type lut_size: u16

.. _`i40e_aq_get_rss_lut.description`:

Description
-----------

get the RSS lookup table, PF or VSI type

.. _`i40e_aq_set_rss_lut`:

i40e_aq_set_rss_lut
===================

.. c:function:: i40e_status i40e_aq_set_rss_lut(struct i40e_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param pf_lut:
        for PF table set true, for VSI table set false
    :type pf_lut: bool

    :param lut:
        pointer to the lut buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the lut buffer
    :type lut_size: u16

.. _`i40e_aq_set_rss_lut.description`:

Description
-----------

set the RSS lookup table, PF or VSI type

.. _`i40e_aq_get_set_rss_key`:

i40e_aq_get_set_rss_key
=======================

.. c:function:: i40e_status i40e_aq_get_set_rss_key(struct i40e_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key, bool set)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct i40e_aqc_get_set_rss_key_data \*

    :param set:
        set true to set the key, false to get the key
    :type set: bool

.. _`i40e_aq_get_set_rss_key.description`:

Description
-----------

get the RSS key per VSI

.. _`i40e_aq_get_rss_key`:

i40e_aq_get_rss_key
===================

.. c:function:: i40e_status i40e_aq_get_rss_key(struct i40e_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct i40e_aqc_get_set_rss_key_data \*

.. _`i40e_aq_set_rss_key`:

i40e_aq_set_rss_key
===================

.. c:function:: i40e_status i40e_aq_set_rss_key(struct i40e_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct i40e_aqc_get_set_rss_key_data \*

.. _`i40e_aq_set_rss_key.description`:

Description
-----------

set the RSS key per VSI

.. _`i40e_init_shared_code`:

i40e_init_shared_code
=====================

.. c:function:: i40e_status i40e_init_shared_code(struct i40e_hw *hw)

    Initialize the shared code

    :param hw:
        pointer to hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_init_shared_code.description`:

Description
-----------

This assigns the MAC type and PHY code and inits the NVM.
Does not touch the hardware. This function must be called prior to any
other function in the shared code. The i40e_hw structure should be
memset to 0 prior to calling this function.  The following fields in

.. _`i40e_init_shared_code.hw-structure-should-be-filled-in-prior-to-calling-this-function`:

hw structure should be filled in prior to calling this function
---------------------------------------------------------------

hw_addr, back, device_id, vendor_id, subsystem_device_id,
subsystem_vendor_id, and revision_id

.. _`i40e_aq_mac_address_read`:

i40e_aq_mac_address_read
========================

.. c:function:: i40e_status i40e_aq_mac_address_read(struct i40e_hw *hw, u16 *flags, struct i40e_aqc_mac_address_read_data *addrs, struct i40e_asq_cmd_details *cmd_details)

    Retrieve the MAC addresses

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param flags:
        a return indicator of what addresses were added to the addr store
    :type flags: u16 \*

    :param addrs:
        the requestor's mac addr store
    :type addrs: struct i40e_aqc_mac_address_read_data \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_mac_address_write`:

i40e_aq_mac_address_write
=========================

.. c:function:: i40e_status i40e_aq_mac_address_write(struct i40e_hw *hw, u16 flags, u8 *mac_addr, struct i40e_asq_cmd_details *cmd_details)

    Change the MAC addresses

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param flags:
        indicates which MAC to be written
    :type flags: u16

    :param mac_addr:
        address to write
    :type mac_addr: u8 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_get_mac_addr`:

i40e_get_mac_addr
=================

.. c:function:: i40e_status i40e_get_mac_addr(struct i40e_hw *hw, u8 *mac_addr)

    get MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param mac_addr:
        pointer to MAC address
    :type mac_addr: u8 \*

.. _`i40e_get_mac_addr.description`:

Description
-----------

Reads the adapter's MAC address from register

.. _`i40e_get_port_mac_addr`:

i40e_get_port_mac_addr
======================

.. c:function:: i40e_status i40e_get_port_mac_addr(struct i40e_hw *hw, u8 *mac_addr)

    get Port MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param mac_addr:
        pointer to Port MAC address
    :type mac_addr: u8 \*

.. _`i40e_get_port_mac_addr.description`:

Description
-----------

Reads the adapter's Port MAC address

.. _`i40e_pre_tx_queue_cfg`:

i40e_pre_tx_queue_cfg
=====================

.. c:function:: void i40e_pre_tx_queue_cfg(struct i40e_hw *hw, u32 queue, bool enable)

    pre tx queue configure

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param queue:
        target PF queue index
    :type queue: u32

    :param enable:
        state change request
    :type enable: bool

.. _`i40e_pre_tx_queue_cfg.description`:

Description
-----------

Handles hw requirement to indicate intention to enable
or disable target queue.

.. _`i40e_read_pba_string`:

i40e_read_pba_string
====================

.. c:function:: i40e_status i40e_read_pba_string(struct i40e_hw *hw, u8 *pba_num, u32 pba_num_size)

    Reads part number string from EEPROM

    :param hw:
        pointer to hardware structure
    :type hw: struct i40e_hw \*

    :param pba_num:
        stores the part number string from the EEPROM
    :type pba_num: u8 \*

    :param pba_num_size:
        part number string buffer length
    :type pba_num_size: u32

.. _`i40e_read_pba_string.description`:

Description
-----------

Reads the part number string from the EEPROM.

.. _`i40e_get_media_type`:

i40e_get_media_type
===================

.. c:function:: enum i40e_media_type i40e_get_media_type(struct i40e_hw *hw)

    Gets media type

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_poll_globr`:

i40e_poll_globr
===============

.. c:function:: i40e_status i40e_poll_globr(struct i40e_hw *hw, u32 retry_limit)

    Poll for Global Reset completion

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param retry_limit:
        how many times to retry before failure
    :type retry_limit: u32

.. _`i40e_pf_reset`:

i40e_pf_reset
=============

.. c:function:: i40e_status i40e_pf_reset(struct i40e_hw *hw)

    Reset the PF

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

.. _`i40e_pf_reset.description`:

Description
-----------

Assuming someone else has triggered a global reset,
assure the global reset is complete and then reset the PF

.. _`i40e_clear_hw`:

i40e_clear_hw
=============

.. c:function:: void i40e_clear_hw(struct i40e_hw *hw)

    clear out any left over hw state

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_clear_hw.description`:

Description
-----------

Clear queues and interrupts, typically called at init time,
but after the capabilities have been found so we know how many
queues and msix vectors have been allocated.

.. _`i40e_clear_pxe_mode`:

i40e_clear_pxe_mode
===================

.. c:function:: void i40e_clear_pxe_mode(struct i40e_hw *hw)

    clear pxe operations mode

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_clear_pxe_mode.description`:

Description
-----------

Make sure all PXE mode settings are cleared, including things
like descriptor fetch/write-back mode.

.. _`i40e_led_is_mine`:

i40e_led_is_mine
================

.. c:function:: u32 i40e_led_is_mine(struct i40e_hw *hw, int idx)

    helper to find matching led

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param idx:
        index into GPIO registers
    :type idx: int

.. _`i40e_led_is_mine.return`:

Return
------

0 if no match, otherwise the value of the GPIO_CTL register

.. _`i40e_led_get`:

i40e_led_get
============

.. c:function:: u32 i40e_led_get(struct i40e_hw *hw)

    return current on/off mode

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_led_get.description`:

Description
-----------

The value returned is the 'mode' field as defined in the

.. _`i40e_led_get.gpio-register-definitions`:

GPIO register definitions
-------------------------

0x0 = off, 0xf = on, and other
values are variations of possible behaviors relating to
blink, link, and wire.

.. _`i40e_led_set`:

i40e_led_set
============

.. c:function:: void i40e_led_set(struct i40e_hw *hw, u32 mode, bool blink)

    set new on/off mode

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param mode:
        0=off, 0xf=on (else see manual for mode details)
    :type mode: u32

    :param blink:
        true if the LED should blink when on, false if steady
    :type blink: bool

.. _`i40e_led_set.description`:

Description
-----------

if this function is used to turn on the blink it should
be used to disable the blink when restoring the original state.

.. _`i40e_aq_get_phy_capabilities`:

i40e_aq_get_phy_capabilities
============================

.. c:function:: i40e_status i40e_aq_get_phy_capabilities(struct i40e_hw *hw, bool qualified_modules, bool report_init, struct i40e_aq_get_phy_abilities_resp *abilities, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param qualified_modules:
        report Qualified Modules
    :type qualified_modules: bool

    :param report_init:
        report init capabilities (active are default)
    :type report_init: bool

    :param abilities:
        structure for PHY capabilities to be filled
    :type abilities: struct i40e_aq_get_phy_abilities_resp \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_phy_capabilities.description`:

Description
-----------

Returns the various PHY abilities supported on the Port.

.. _`i40e_aq_set_phy_config`:

i40e_aq_set_phy_config
======================

.. c:function:: enum i40e_status_code i40e_aq_set_phy_config(struct i40e_hw *hw, struct i40e_aq_set_phy_config *config, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param config:
        structure with PHY configuration to be set
    :type config: struct i40e_aq_set_phy_config \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_phy_config.description`:

Description
-----------

Set the various PHY configuration parameters
supported on the Port.One or more of the Set PHY config parameters may be
ignored in an MFP mode as the PF may not have the privilege to set some
of the PHY Config parameters. This status will be indicated by the
command response.

.. _`i40e_set_fc`:

i40e_set_fc
===========

.. c:function:: enum i40e_status_code i40e_set_fc(struct i40e_hw *hw, u8 *aq_failures, bool atomic_restart)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param aq_failures:
        buffer to return AdminQ failure information
    :type aq_failures: u8 \*

    :param atomic_restart:
        whether to enable atomic link restart
    :type atomic_restart: bool

.. _`i40e_set_fc.description`:

Description
-----------

Set the requested flow control mode using set_phy_config.

.. _`i40e_aq_clear_pxe_mode`:

i40e_aq_clear_pxe_mode
======================

.. c:function:: i40e_status i40e_aq_clear_pxe_mode(struct i40e_hw *hw, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_clear_pxe_mode.description`:

Description
-----------

Tell the firmware that the driver is taking over from PXE

.. _`i40e_aq_set_link_restart_an`:

i40e_aq_set_link_restart_an
===========================

.. c:function:: i40e_status i40e_aq_set_link_restart_an(struct i40e_hw *hw, bool enable_link, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param enable_link:
        if true: enable link, if false: disable link
    :type enable_link: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_link_restart_an.description`:

Description
-----------

Sets up the link and restarts the Auto-Negotiation over the link.

.. _`i40e_aq_get_link_info`:

i40e_aq_get_link_info
=====================

.. c:function:: i40e_status i40e_aq_get_link_info(struct i40e_hw *hw, bool enable_lse, struct i40e_link_status *link, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param enable_lse:
        enable/disable LinkStatusEvent reporting
    :type enable_lse: bool

    :param link:
        pointer to link status structure - optional
    :type link: struct i40e_link_status \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_link_info.description`:

Description
-----------

Returns the link status of the adapter.

.. _`i40e_aq_set_phy_int_mask`:

i40e_aq_set_phy_int_mask
========================

.. c:function:: i40e_status i40e_aq_set_phy_int_mask(struct i40e_hw *hw, u16 mask, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param mask:
        interrupt mask to be set
    :type mask: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_phy_int_mask.description`:

Description
-----------

Set link interrupt mask.

.. _`i40e_aq_set_phy_debug`:

i40e_aq_set_phy_debug
=====================

.. c:function:: i40e_status i40e_aq_set_phy_debug(struct i40e_hw *hw, u8 cmd_flags, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param cmd_flags:
        debug command flags
    :type cmd_flags: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_phy_debug.description`:

Description
-----------

Reset the external PHY.

.. _`i40e_aq_add_vsi`:

i40e_aq_add_vsi
===============

.. c:function:: i40e_status i40e_aq_add_vsi(struct i40e_hw *hw, struct i40e_vsi_context *vsi_ctx, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param vsi_ctx:
        pointer to a vsi context struct
    :type vsi_ctx: struct i40e_vsi_context \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_add_vsi.description`:

Description
-----------

Add a VSI context to the hardware.

.. _`i40e_aq_set_default_vsi`:

i40e_aq_set_default_vsi
=======================

.. c:function:: i40e_status i40e_aq_set_default_vsi(struct i40e_hw *hw, u16 seid, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_clear_default_vsi`:

i40e_aq_clear_default_vsi
=========================

.. c:function:: i40e_status i40e_aq_clear_default_vsi(struct i40e_hw *hw, u16 seid, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_vsi_unicast_promiscuous`:

i40e_aq_set_vsi_unicast_promiscuous
===================================

.. c:function:: i40e_status i40e_aq_set_vsi_unicast_promiscuous(struct i40e_hw *hw, u16 seid, bool set, struct i40e_asq_cmd_details *cmd_details, bool rx_only_promisc)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param set:
        set unicast promiscuous enable/disable
    :type set: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

    :param rx_only_promisc:
        flag to decide if egress traffic gets mirrored in promisc
    :type rx_only_promisc: bool

.. _`i40e_aq_set_vsi_multicast_promiscuous`:

i40e_aq_set_vsi_multicast_promiscuous
=====================================

.. c:function:: i40e_status i40e_aq_set_vsi_multicast_promiscuous(struct i40e_hw *hw, u16 seid, bool set, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param set:
        set multicast promiscuous enable/disable
    :type set: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_vsi_mc_promisc_on_vlan`:

i40e_aq_set_vsi_mc_promisc_on_vlan
==================================

.. c:function:: enum i40e_status_code i40e_aq_set_vsi_mc_promisc_on_vlan(struct i40e_hw *hw, u16 seid, bool enable, u16 vid, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param enable:
        set MAC L2 layer unicast promiscuous enable/disable for a given VLAN
    :type enable: bool

    :param vid:
        The VLAN tag filter - capture any multicast packet with this VLAN tag
    :type vid: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_vsi_uc_promisc_on_vlan`:

i40e_aq_set_vsi_uc_promisc_on_vlan
==================================

.. c:function:: enum i40e_status_code i40e_aq_set_vsi_uc_promisc_on_vlan(struct i40e_hw *hw, u16 seid, bool enable, u16 vid, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param enable:
        set MAC L2 layer unicast promiscuous enable/disable for a given VLAN
    :type enable: bool

    :param vid:
        The VLAN tag filter - capture any unicast packet with this VLAN tag
    :type vid: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_vsi_bc_promisc_on_vlan`:

i40e_aq_set_vsi_bc_promisc_on_vlan
==================================

.. c:function:: i40e_status i40e_aq_set_vsi_bc_promisc_on_vlan(struct i40e_hw *hw, u16 seid, bool enable, u16 vid, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param enable:
        set broadcast promiscuous enable/disable for a given VLAN
    :type enable: bool

    :param vid:
        The VLAN tag filter - capture any broadcast packet with this VLAN tag
    :type vid: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_vsi_broadcast`:

i40e_aq_set_vsi_broadcast
=========================

.. c:function:: i40e_status i40e_aq_set_vsi_broadcast(struct i40e_hw *hw, u16 seid, bool set_filter, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param set_filter:
        true to set filter, false to clear filter
    :type set_filter: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_vsi_broadcast.description`:

Description
-----------

Set or clear the broadcast promiscuous flag (filter) for a given VSI.

.. _`i40e_aq_set_vsi_vlan_promisc`:

i40e_aq_set_vsi_vlan_promisc
============================

.. c:function:: i40e_status i40e_aq_set_vsi_vlan_promisc(struct i40e_hw *hw, u16 seid, bool enable, struct i40e_asq_cmd_details *cmd_details)

    control the VLAN promiscuous setting

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        vsi number
    :type seid: u16

    :param enable:
        set MAC L2 layer unicast promiscuous enable/disable for a given VLAN
    :type enable: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_vsi_params`:

i40e_aq_get_vsi_params
======================

.. c:function:: i40e_status i40e_aq_get_vsi_params(struct i40e_hw *hw, struct i40e_vsi_context *vsi_ctx, struct i40e_asq_cmd_details *cmd_details)

    get VSI configuration info

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param vsi_ctx:
        pointer to a vsi context struct
    :type vsi_ctx: struct i40e_vsi_context \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_update_vsi_params`:

i40e_aq_update_vsi_params
=========================

.. c:function:: i40e_status i40e_aq_update_vsi_params(struct i40e_hw *hw, struct i40e_vsi_context *vsi_ctx, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param vsi_ctx:
        pointer to a vsi context struct
    :type vsi_ctx: struct i40e_vsi_context \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_update_vsi_params.description`:

Description
-----------

Update a VSI context.

.. _`i40e_aq_get_switch_config`:

i40e_aq_get_switch_config
=========================

.. c:function:: i40e_status i40e_aq_get_switch_config(struct i40e_hw *hw, struct i40e_aqc_get_switch_config_resp *buf, u16 buf_size, u16 *start_seid, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param buf:
        pointer to the result buffer
    :type buf: struct i40e_aqc_get_switch_config_resp \*

    :param buf_size:
        length of input buffer
    :type buf_size: u16

    :param start_seid:
        seid to start for the report, 0 == beginning
    :type start_seid: u16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_switch_config.description`:

Description
-----------

Fill the buf with switch configuration returned from AdminQ command

.. _`i40e_aq_set_switch_config`:

i40e_aq_set_switch_config
=========================

.. c:function:: enum i40e_status_code i40e_aq_set_switch_config(struct i40e_hw *hw, u16 flags, u16 valid_flags, u8 mode, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param flags:
        bit flag values to set
    :type flags: u16

    :param valid_flags:
        which bit flags to set
    :type valid_flags: u16

    :param mode:
        cloud filter mode
    :type mode: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_switch_config.description`:

Description
-----------

Set switch configuration bits

.. _`i40e_aq_get_firmware_version`:

i40e_aq_get_firmware_version
============================

.. c:function:: i40e_status i40e_aq_get_firmware_version(struct i40e_hw *hw, u16 *fw_major_version, u16 *fw_minor_version, u32 *fw_build, u16 *api_major_version, u16 *api_minor_version, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param fw_major_version:
        firmware major version
    :type fw_major_version: u16 \*

    :param fw_minor_version:
        firmware minor version
    :type fw_minor_version: u16 \*

    :param fw_build:
        firmware build number
    :type fw_build: u32 \*

    :param api_major_version:
        major queue version
    :type api_major_version: u16 \*

    :param api_minor_version:
        minor queue version
    :type api_minor_version: u16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_firmware_version.description`:

Description
-----------

Get the firmware version from the admin queue commands

.. _`i40e_aq_send_driver_version`:

i40e_aq_send_driver_version
===========================

.. c:function:: i40e_status i40e_aq_send_driver_version(struct i40e_hw *hw, struct i40e_driver_version *dv, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param dv:
        driver's major, minor version
    :type dv: struct i40e_driver_version \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_send_driver_version.description`:

Description
-----------

Send the driver version to the firmware

.. _`i40e_get_link_status`:

i40e_get_link_status
====================

.. c:function:: i40e_status i40e_get_link_status(struct i40e_hw *hw, bool *link_up)

    get status of the HW network link

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param link_up:
        pointer to bool (true/false = linkup/linkdown)
    :type link_up: bool \*

.. _`i40e_get_link_status.description`:

Description
-----------

Variable link_up true if link is up, false if link is down.
The variable link_up is invalid if returned value of status != 0

.. _`i40e_get_link_status.side-effect`:

Side effect
-----------

LinkStatusEvent reporting becomes enabled

.. _`i40e_update_link_info`:

i40e_update_link_info
=====================

.. c:function:: i40e_status i40e_update_link_info(struct i40e_hw *hw)

    update status of the HW network link

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

.. _`i40e_aq_add_veb`:

i40e_aq_add_veb
===============

.. c:function:: i40e_status i40e_aq_add_veb(struct i40e_hw *hw, u16 uplink_seid, u16 downlink_seid, u8 enabled_tc, bool default_port, u16 *veb_seid, bool enable_stats, struct i40e_asq_cmd_details *cmd_details)

    Insert a VEB between the VSI and the MAC

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param uplink_seid:
        the MAC or other gizmo SEID
    :type uplink_seid: u16

    :param downlink_seid:
        the VSI SEID
    :type downlink_seid: u16

    :param enabled_tc:
        bitmap of TCs to be enabled
    :type enabled_tc: u8

    :param default_port:
        true for default port VSI, false for control port
    :type default_port: bool

    :param veb_seid:
        pointer to where to put the resulting VEB SEID
    :type veb_seid: u16 \*

    :param enable_stats:
        true to turn on VEB stats
    :type enable_stats: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_add_veb.description`:

Description
-----------

This asks the FW to add a VEB between the uplink and downlink
elements.  If the uplink SEID is 0, this will be a floating VEB.

.. _`i40e_aq_get_veb_parameters`:

i40e_aq_get_veb_parameters
==========================

.. c:function:: i40e_status i40e_aq_get_veb_parameters(struct i40e_hw *hw, u16 veb_seid, u16 *switch_id, bool *floating, u16 *statistic_index, u16 *vebs_used, u16 *vebs_free, struct i40e_asq_cmd_details *cmd_details)

    Retrieve VEB parameters

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param veb_seid:
        the SEID of the VEB to query
    :type veb_seid: u16

    :param switch_id:
        the uplink switch id
    :type switch_id: u16 \*

    :param floating:
        set to true if the VEB is floating
    :type floating: bool \*

    :param statistic_index:
        index of the stats counter block for this VEB
    :type statistic_index: u16 \*

    :param vebs_used:
        number of VEB's used by function
    :type vebs_used: u16 \*

    :param vebs_free:
        total VEB's not reserved by any function
    :type vebs_free: u16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_veb_parameters.description`:

Description
-----------

This retrieves the parameters for a particular VEB, specified by
uplink_seid, and returns them to the caller.

.. _`i40e_aq_add_macvlan`:

i40e_aq_add_macvlan
===================

.. c:function:: i40e_status i40e_aq_add_macvlan(struct i40e_hw *hw, u16 seid, struct i40e_aqc_add_macvlan_element_data *mv_list, u16 count, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        VSI for the mac address
    :type seid: u16

    :param mv_list:
        list of macvlans to be added
    :type mv_list: struct i40e_aqc_add_macvlan_element_data \*

    :param count:
        length of the list
    :type count: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_add_macvlan.description`:

Description
-----------

Add MAC/VLAN addresses to the HW filtering

.. _`i40e_aq_remove_macvlan`:

i40e_aq_remove_macvlan
======================

.. c:function:: i40e_status i40e_aq_remove_macvlan(struct i40e_hw *hw, u16 seid, struct i40e_aqc_remove_macvlan_element_data *mv_list, u16 count, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        VSI for the mac address
    :type seid: u16

    :param mv_list:
        list of macvlans to be removed
    :type mv_list: struct i40e_aqc_remove_macvlan_element_data \*

    :param count:
        length of the list
    :type count: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_remove_macvlan.description`:

Description
-----------

Remove MAC/VLAN addresses from the HW filtering

.. _`i40e_mirrorrule_op`:

i40e_mirrorrule_op
==================

.. c:function:: i40e_status i40e_mirrorrule_op(struct i40e_hw *hw, u16 opcode, u16 sw_seid, u16 rule_type, u16 id, u16 count, __le16 *mr_list, struct i40e_asq_cmd_details *cmd_details, u16 *rule_id, u16 *rules_used, u16 *rules_free)

    Internal helper function to add/delete mirror rule

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param opcode:
        AQ opcode for add or delete mirror rule
    :type opcode: u16

    :param sw_seid:
        Switch SEID (to which rule refers)
    :type sw_seid: u16

    :param rule_type:
        Rule Type (ingress/egress/VLAN)
    :type rule_type: u16

    :param id:
        Destination VSI SEID or Rule ID
    :type id: u16

    :param count:
        length of the list
    :type count: u16

    :param mr_list:
        list of mirrored VSI SEIDs or VLAN IDs
    :type mr_list: __le16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

    :param rule_id:
        Rule ID returned from FW
    :type rule_id: u16 \*

    :param rules_used:
        Number of rules used in internal switch
    :type rules_used: u16 \*

    :param rules_free:
        Number of rules free in internal switch
    :type rules_free: u16 \*

.. _`i40e_mirrorrule_op.description`:

Description
-----------

Add/Delete a mirror rule to a specific switch. Mirror rules are supported for
VEBs/VEPA elements only

.. _`i40e_aq_add_mirrorrule`:

i40e_aq_add_mirrorrule
======================

.. c:function:: i40e_status i40e_aq_add_mirrorrule(struct i40e_hw *hw, u16 sw_seid, u16 rule_type, u16 dest_vsi, u16 count, __le16 *mr_list, struct i40e_asq_cmd_details *cmd_details, u16 *rule_id, u16 *rules_used, u16 *rules_free)

    add a mirror rule

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param sw_seid:
        Switch SEID (to which rule refers)
    :type sw_seid: u16

    :param rule_type:
        Rule Type (ingress/egress/VLAN)
    :type rule_type: u16

    :param dest_vsi:
        SEID of VSI to which packets will be mirrored
    :type dest_vsi: u16

    :param count:
        length of the list
    :type count: u16

    :param mr_list:
        list of mirrored VSI SEIDs or VLAN IDs
    :type mr_list: __le16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

    :param rule_id:
        Rule ID returned from FW
    :type rule_id: u16 \*

    :param rules_used:
        Number of rules used in internal switch
    :type rules_used: u16 \*

    :param rules_free:
        Number of rules free in internal switch
    :type rules_free: u16 \*

.. _`i40e_aq_add_mirrorrule.description`:

Description
-----------

Add mirror rule. Mirror rules are supported for VEBs or VEPA elements only

.. _`i40e_aq_delete_mirrorrule`:

i40e_aq_delete_mirrorrule
=========================

.. c:function:: i40e_status i40e_aq_delete_mirrorrule(struct i40e_hw *hw, u16 sw_seid, u16 rule_type, u16 rule_id, u16 count, __le16 *mr_list, struct i40e_asq_cmd_details *cmd_details, u16 *rules_used, u16 *rules_free)

    delete a mirror rule

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param sw_seid:
        Switch SEID (to which rule refers)
    :type sw_seid: u16

    :param rule_type:
        Rule Type (ingress/egress/VLAN)
    :type rule_type: u16

    :param rule_id:
        Rule ID that is returned in the receive desc as part of
        add_mirrorrule.
    :type rule_id: u16

    :param count:
        length of the list
    :type count: u16

    :param mr_list:
        list of mirrored VLAN IDs to be removed
    :type mr_list: __le16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

    :param rules_used:
        Number of rules used in internal switch
    :type rules_used: u16 \*

    :param rules_free:
        Number of rules free in internal switch
    :type rules_free: u16 \*

.. _`i40e_aq_delete_mirrorrule.description`:

Description
-----------

Delete a mirror rule. Mirror rules are supported for VEBs/VEPA elements only

.. _`i40e_aq_send_msg_to_vf`:

i40e_aq_send_msg_to_vf
======================

.. c:function:: i40e_status i40e_aq_send_msg_to_vf(struct i40e_hw *hw, u16 vfid, u32 v_opcode, u32 v_retval, u8 *msg, u16 msglen, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param vfid:
        VF id to send msg
    :type vfid: u16

    :param v_opcode:
        opcodes for VF-PF communication
    :type v_opcode: u32

    :param v_retval:
        return error code
    :type v_retval: u32

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

    :param cmd_details:
        pointer to command details
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_send_msg_to_vf.description`:

Description
-----------

send msg to vf

.. _`i40e_aq_debug_read_register`:

i40e_aq_debug_read_register
===========================

.. c:function:: i40e_status i40e_aq_debug_read_register(struct i40e_hw *hw, u32 reg_addr, u64 *reg_val, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param reg_addr:
        register address
    :type reg_addr: u32

    :param reg_val:
        register value
    :type reg_val: u64 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_debug_read_register.description`:

Description
-----------

Read the register using the admin queue commands

.. _`i40e_aq_debug_write_register`:

i40e_aq_debug_write_register
============================

.. c:function:: i40e_status i40e_aq_debug_write_register(struct i40e_hw *hw, u32 reg_addr, u64 reg_val, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param reg_addr:
        register address
    :type reg_addr: u32

    :param reg_val:
        register value
    :type reg_val: u64

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_debug_write_register.description`:

Description
-----------

Write to a register using the admin queue commands

.. _`i40e_aq_request_resource`:

i40e_aq_request_resource
========================

.. c:function:: i40e_status i40e_aq_request_resource(struct i40e_hw *hw, enum i40e_aq_resources_ids resource, enum i40e_aq_resource_access_type access, u8 sdp_number, u64 *timeout, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param resource:
        resource id
    :type resource: enum i40e_aq_resources_ids

    :param access:
        access type
    :type access: enum i40e_aq_resource_access_type

    :param sdp_number:
        resource number
    :type sdp_number: u8

    :param timeout:
        the maximum time in ms that the driver may hold the resource
    :type timeout: u64 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_request_resource.description`:

Description
-----------

requests common resource using the admin queue commands

.. _`i40e_aq_release_resource`:

i40e_aq_release_resource
========================

.. c:function:: i40e_status i40e_aq_release_resource(struct i40e_hw *hw, enum i40e_aq_resources_ids resource, u8 sdp_number, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param resource:
        resource id
    :type resource: enum i40e_aq_resources_ids

    :param sdp_number:
        resource number
    :type sdp_number: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_release_resource.description`:

Description
-----------

release common resource using the admin queue commands

.. _`i40e_aq_read_nvm`:

i40e_aq_read_nvm
================

.. c:function:: i40e_status i40e_aq_read_nvm(struct i40e_hw *hw, u8 module_pointer, u32 offset, u16 length, void *data, bool last_command, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param module_pointer:
        module pointer location in words from the NVM beginning
    :type module_pointer: u8

    :param offset:
        byte offset from the module beginning
    :type offset: u32

    :param length:
        length of the section to be read (in bytes from the offset)
    :type length: u16

    :param data:
        command buffer (size [bytes] = length)
    :type data: void \*

    :param last_command:
        tells if this is the last command in a series
    :type last_command: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_read_nvm.description`:

Description
-----------

Read the NVM using the admin queue commands

.. _`i40e_aq_erase_nvm`:

i40e_aq_erase_nvm
=================

.. c:function:: i40e_status i40e_aq_erase_nvm(struct i40e_hw *hw, u8 module_pointer, u32 offset, u16 length, bool last_command, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param module_pointer:
        module pointer location in words from the NVM beginning
    :type module_pointer: u8

    :param offset:
        offset in the module (expressed in 4 KB from module's beginning)
    :type offset: u32

    :param length:
        length of the section to be erased (expressed in 4 KB)
    :type length: u16

    :param last_command:
        tells if this is the last command in a series
    :type last_command: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_erase_nvm.description`:

Description
-----------

Erase the NVM sector using the admin queue commands

.. _`i40e_parse_discover_capabilities`:

i40e_parse_discover_capabilities
================================

.. c:function:: void i40e_parse_discover_capabilities(struct i40e_hw *hw, void *buff, u32 cap_count, enum i40e_admin_queue_opc list_type_opc)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param buff:
        pointer to a buffer containing device/function capability records
    :type buff: void \*

    :param cap_count:
        number of capability records in the list
    :type cap_count: u32

    :param list_type_opc:
        type of capabilities list to parse
    :type list_type_opc: enum i40e_admin_queue_opc

.. _`i40e_parse_discover_capabilities.description`:

Description
-----------

Parse the device/function capabilities list.

.. _`i40e_aq_discover_capabilities`:

i40e_aq_discover_capabilities
=============================

.. c:function:: i40e_status i40e_aq_discover_capabilities(struct i40e_hw *hw, void *buff, u16 buff_size, u16 *data_size, enum i40e_admin_queue_opc list_type_opc, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param buff:
        a virtual buffer to hold the capabilities
    :type buff: void \*

    :param buff_size:
        Size of the virtual buffer
    :type buff_size: u16

    :param data_size:
        Size of the returned data, or buff size needed if AQ err==ENOMEM
    :type data_size: u16 \*

    :param list_type_opc:
        capabilities type to discover - pass in the command opcode
    :type list_type_opc: enum i40e_admin_queue_opc

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_discover_capabilities.description`:

Description
-----------

Get the device capabilities descriptions from the firmware

.. _`i40e_aq_update_nvm`:

i40e_aq_update_nvm
==================

.. c:function:: i40e_status i40e_aq_update_nvm(struct i40e_hw *hw, u8 module_pointer, u32 offset, u16 length, void *data, bool last_command, u8 preservation_flags, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param module_pointer:
        module pointer location in words from the NVM beginning
    :type module_pointer: u8

    :param offset:
        byte offset from the module beginning
    :type offset: u32

    :param length:
        length of the section to be written (in bytes from the offset)
    :type length: u16

    :param data:
        command buffer (size [bytes] = length)
    :type data: void \*

    :param last_command:
        tells if this is the last command in a series
    :type last_command: bool

    :param preservation_flags:
        Preservation mode flags
    :type preservation_flags: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_update_nvm.description`:

Description
-----------

Update the NVM using the admin queue commands

.. _`i40e_aq_rearrange_nvm`:

i40e_aq_rearrange_nvm
=====================

.. c:function:: i40e_status i40e_aq_rearrange_nvm(struct i40e_hw *hw, u8 rearrange_nvm, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param rearrange_nvm:
        defines direction of rearrangement
    :type rearrange_nvm: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_rearrange_nvm.description`:

Description
-----------

Rearrange NVM structure, available only for transition FW

.. _`i40e_aq_get_lldp_mib`:

i40e_aq_get_lldp_mib
====================

.. c:function:: i40e_status i40e_aq_get_lldp_mib(struct i40e_hw *hw, u8 bridge_type, u8 mib_type, void *buff, u16 buff_size, u16 *local_len, u16 *remote_len, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param bridge_type:
        type of bridge requested
    :type bridge_type: u8

    :param mib_type:
        Local, Remote or both Local and Remote MIBs
    :type mib_type: u8

    :param buff:
        pointer to a user supplied buffer to store the MIB block
    :type buff: void \*

    :param buff_size:
        size of the buffer (in bytes)
    :type buff_size: u16

    :param local_len:
        length of the returned Local LLDP MIB
    :type local_len: u16 \*

    :param remote_len:
        length of the returned Remote LLDP MIB
    :type remote_len: u16 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_lldp_mib.description`:

Description
-----------

Requests the complete LLDP MIB (entire packet).

.. _`i40e_aq_cfg_lldp_mib_change_event`:

i40e_aq_cfg_lldp_mib_change_event
=================================

.. c:function:: i40e_status i40e_aq_cfg_lldp_mib_change_event(struct i40e_hw *hw, bool enable_update, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param enable_update:
        Enable or Disable event posting
    :type enable_update: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_cfg_lldp_mib_change_event.description`:

Description
-----------

Enable or Disable posting of an event on ARQ when LLDP MIB
associated with the interface changes

.. _`i40e_aq_stop_lldp`:

i40e_aq_stop_lldp
=================

.. c:function:: i40e_status i40e_aq_stop_lldp(struct i40e_hw *hw, bool shutdown_agent, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param shutdown_agent:
        True if LLDP Agent needs to be Shutdown
    :type shutdown_agent: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_stop_lldp.description`:

Description
-----------

Stop or Shutdown the embedded LLDP Agent

.. _`i40e_aq_start_lldp`:

i40e_aq_start_lldp
==================

.. c:function:: i40e_status i40e_aq_start_lldp(struct i40e_hw *hw, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_start_lldp.description`:

Description
-----------

Start the embedded LLDP Agent on all ports.

.. _`i40e_aq_set_dcb_parameters`:

i40e_aq_set_dcb_parameters
==========================

.. c:function:: enum i40e_status_code i40e_aq_set_dcb_parameters(struct i40e_hw *hw, bool dcb_enable, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param dcb_enable:
        True if DCB configuration needs to be applied
    :type dcb_enable: bool

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_cee_dcb_config`:

i40e_aq_get_cee_dcb_config
==========================

.. c:function:: i40e_status i40e_aq_get_cee_dcb_config(struct i40e_hw *hw, void *buff, u16 buff_size, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param buff:
        response buffer that stores CEE operational configuration
    :type buff: void \*

    :param buff_size:
        size of the buffer passed
    :type buff_size: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_cee_dcb_config.description`:

Description
-----------

Get CEE DCBX mode operational configuration from firmware

.. _`i40e_aq_add_udp_tunnel`:

i40e_aq_add_udp_tunnel
======================

.. c:function:: i40e_status i40e_aq_add_udp_tunnel(struct i40e_hw *hw, u16 udp_port, u8 protocol_index, u8 *filter_index, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param udp_port:
        the UDP port to add in Host byte order
    :type udp_port: u16

    :param protocol_index:
        protocol index type
    :type protocol_index: u8

    :param filter_index:
        pointer to filter index
    :type filter_index: u8 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_add_udp_tunnel.note`:

Note
----

Firmware expects the udp_port value to be in Little Endian format,
and this function will call cpu_to_le16 to convert from Host byte order to
Little Endian order.

.. _`i40e_aq_del_udp_tunnel`:

i40e_aq_del_udp_tunnel
======================

.. c:function:: i40e_status i40e_aq_del_udp_tunnel(struct i40e_hw *hw, u8 index, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param index:
        filter index
    :type index: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_delete_element`:

i40e_aq_delete_element
======================

.. c:function:: i40e_status i40e_aq_delete_element(struct i40e_hw *hw, u16 seid, struct i40e_asq_cmd_details *cmd_details)

    Delete switch element

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        the SEID to delete from the switch
    :type seid: u16

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_delete_element.description`:

Description
-----------

This deletes a switch element from the switch.

.. _`i40e_aq_dcb_updated`:

i40e_aq_dcb_updated
===================

.. c:function:: i40e_status i40e_aq_dcb_updated(struct i40e_hw *hw, struct i40e_asq_cmd_details *cmd_details)

    DCB Updated Command

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_dcb_updated.description`:

Description
-----------

EMP will return when the shared RPB settings have been
recomputed and modified. The retval field in the descriptor
will be set to 0 when RPB is modified.

.. _`i40e_aq_tx_sched_cmd`:

i40e_aq_tx_sched_cmd
====================

.. c:function:: i40e_status i40e_aq_tx_sched_cmd(struct i40e_hw *hw, u16 seid, void *buff, u16 buff_size, enum i40e_admin_queue_opc opcode, struct i40e_asq_cmd_details *cmd_details)

    generic Tx scheduler AQ command handler

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid for the physical port/switching component/vsi
    :type seid: u16

    :param buff:
        Indirect buffer to hold data parameters and response
    :type buff: void \*

    :param buff_size:
        Indirect buffer size
    :type buff_size: u16

    :param opcode:
        Tx scheduler AQ command opcode
    :type opcode: enum i40e_admin_queue_opc

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_tx_sched_cmd.description`:

Description
-----------

Generic command handler for Tx scheduler AQ commands

.. _`i40e_aq_config_vsi_bw_limit`:

i40e_aq_config_vsi_bw_limit
===========================

.. c:function:: i40e_status i40e_aq_config_vsi_bw_limit(struct i40e_hw *hw, u16 seid, u16 credit, u8 max_credit, struct i40e_asq_cmd_details *cmd_details)

    Configure VSI BW Limit

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid
    :type seid: u16

    :param credit:
        BW limit credits (0 = disabled)
    :type credit: u16

    :param max_credit:
        Max BW limit credits
    :type max_credit: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_config_vsi_tc_bw`:

i40e_aq_config_vsi_tc_bw
========================

.. c:function:: i40e_status i40e_aq_config_vsi_tc_bw(struct i40e_hw *hw, u16 seid, struct i40e_aqc_configure_vsi_tc_bw_data *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Config VSI BW Allocation per TC

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid
    :type seid: u16

    :param bw_data:
        Buffer holding enabled TCs, relative TC BW limit/credits
    :type bw_data: struct i40e_aqc_configure_vsi_tc_bw_data \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_config_switch_comp_ets`:

i40e_aq_config_switch_comp_ets
==============================

.. c:function:: i40e_status i40e_aq_config_switch_comp_ets(struct i40e_hw *hw, u16 seid, struct i40e_aqc_configure_switching_comp_ets_data *ets_data, enum i40e_admin_queue_opc opcode, struct i40e_asq_cmd_details *cmd_details)

    Enable/Disable/Modify ETS on the port

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the switching component connected to Physical Port
    :type seid: u16

    :param ets_data:
        Buffer holding ETS parameters
    :type ets_data: struct i40e_aqc_configure_switching_comp_ets_data \*

    :param opcode:
        Tx scheduler AQ command opcode
    :type opcode: enum i40e_admin_queue_opc

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_config_switch_comp_bw_config`:

i40e_aq_config_switch_comp_bw_config
====================================

.. c:function:: i40e_status i40e_aq_config_switch_comp_bw_config(struct i40e_hw *hw, u16 seid, struct i40e_aqc_configure_switching_comp_bw_config_data *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Config Switch comp BW Alloc per TC

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the switching component
    :type seid: u16

    :param bw_data:
        Buffer holding enabled TCs, relative/absolute TC BW limit/credits
    :type bw_data: struct i40e_aqc_configure_switching_comp_bw_config_data \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_query_vsi_bw_config`:

i40e_aq_query_vsi_bw_config
===========================

.. c:function:: i40e_status i40e_aq_query_vsi_bw_config(struct i40e_hw *hw, u16 seid, struct i40e_aqc_query_vsi_bw_config_resp *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Query VSI BW configuration

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the VSI
    :type seid: u16

    :param bw_data:
        Buffer to hold VSI BW configuration
    :type bw_data: struct i40e_aqc_query_vsi_bw_config_resp \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_query_vsi_ets_sla_config`:

i40e_aq_query_vsi_ets_sla_config
================================

.. c:function:: i40e_status i40e_aq_query_vsi_ets_sla_config(struct i40e_hw *hw, u16 seid, struct i40e_aqc_query_vsi_ets_sla_config_resp *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Query VSI BW configuration per TC

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the VSI
    :type seid: u16

    :param bw_data:
        Buffer to hold VSI BW configuration per TC
    :type bw_data: struct i40e_aqc_query_vsi_ets_sla_config_resp \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_query_switch_comp_ets_config`:

i40e_aq_query_switch_comp_ets_config
====================================

.. c:function:: i40e_status i40e_aq_query_switch_comp_ets_config(struct i40e_hw *hw, u16 seid, struct i40e_aqc_query_switching_comp_ets_config_resp *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Query Switch comp BW config per TC

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the switching component
    :type seid: u16

    :param bw_data:
        Buffer to hold switching component's per TC BW config
    :type bw_data: struct i40e_aqc_query_switching_comp_ets_config_resp \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_query_port_ets_config`:

i40e_aq_query_port_ets_config
=============================

.. c:function:: i40e_status i40e_aq_query_port_ets_config(struct i40e_hw *hw, u16 seid, struct i40e_aqc_query_port_ets_config_resp *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Query Physical Port ETS configuration

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the VSI or switching component connected to Physical Port
    :type seid: u16

    :param bw_data:
        Buffer to hold current ETS configuration for the Physical Port
    :type bw_data: struct i40e_aqc_query_port_ets_config_resp \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_query_switch_comp_bw_config`:

i40e_aq_query_switch_comp_bw_config
===================================

.. c:function:: i40e_status i40e_aq_query_switch_comp_bw_config(struct i40e_hw *hw, u16 seid, struct i40e_aqc_query_switching_comp_bw_config_resp *bw_data, struct i40e_asq_cmd_details *cmd_details)

    Query Switch comp BW configuration

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        seid of the switching component
    :type seid: u16

    :param bw_data:
        Buffer to hold switching component's BW configuration
    :type bw_data: struct i40e_aqc_query_switching_comp_bw_config_resp \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_validate_filter_settings`:

i40e_validate_filter_settings
=============================

.. c:function:: i40e_status i40e_validate_filter_settings(struct i40e_hw *hw, struct i40e_filter_control_settings *settings)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param settings:
        Filter control settings
    :type settings: struct i40e_filter_control_settings \*

.. _`i40e_validate_filter_settings.description`:

Description
-----------

Check and validate the filter control settings passed.
The function checks for the valid filter/context sizes being
passed for FCoE and PE.

Returns 0 if the values passed are valid and within
range else returns an error.

.. _`i40e_set_filter_control`:

i40e_set_filter_control
=======================

.. c:function:: i40e_status i40e_set_filter_control(struct i40e_hw *hw, struct i40e_filter_control_settings *settings)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param settings:
        Filter control settings
    :type settings: struct i40e_filter_control_settings \*

.. _`i40e_set_filter_control.description`:

Description
-----------

Set the Queue Filters for PE/FCoE and enable filters required
for a single PF. It is expected that these settings are programmed
at the driver initialization time.

.. _`i40e_aq_add_rem_control_packet_filter`:

i40e_aq_add_rem_control_packet_filter
=====================================

.. c:function:: i40e_status i40e_aq_add_rem_control_packet_filter(struct i40e_hw *hw, u8 *mac_addr, u16 ethtype, u16 flags, u16 vsi_seid, u16 queue, bool is_add, struct i40e_control_filter_stats *stats, struct i40e_asq_cmd_details *cmd_details)

    Add or Remove Control Packet Filter

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param mac_addr:
        MAC address to use in the filter
    :type mac_addr: u8 \*

    :param ethtype:
        Ethertype to use in the filter
    :type ethtype: u16

    :param flags:
        Flags that needs to be applied to the filter
    :type flags: u16

    :param vsi_seid:
        seid of the control VSI
    :type vsi_seid: u16

    :param queue:
        VSI queue number to send the packet to
    :type queue: u16

    :param is_add:
        Add control packet filter if True else remove
    :type is_add: bool

    :param stats:
        Structure to hold information on control filter counts
    :type stats: struct i40e_control_filter_stats \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_add_rem_control_packet_filter.description`:

Description
-----------

This command will Add or Remove control packet filter for a control VSI.
In return it will update the total number of perfect filter count in
the stats member.

.. _`i40e_add_filter_to_drop_tx_flow_control_frames`:

i40e_add_filter_to_drop_tx_flow_control_frames
==============================================

.. c:function:: void i40e_add_filter_to_drop_tx_flow_control_frames(struct i40e_hw *hw, u16 seid)

    filter to drop flow control

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid to add ethertype filter from
    :type seid: u16

.. _`i40e_aq_alternate_read`:

i40e_aq_alternate_read
======================

.. c:function:: i40e_status i40e_aq_alternate_read(struct i40e_hw *hw, u32 reg_addr0, u32 *reg_val0, u32 reg_addr1, u32 *reg_val1)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param reg_addr0:
        address of first dword to be read
    :type reg_addr0: u32

    :param reg_val0:
        pointer for data read from 'reg_addr0'
    :type reg_val0: u32 \*

    :param reg_addr1:
        address of second dword to be read
    :type reg_addr1: u32

    :param reg_val1:
        pointer for data read from 'reg_addr1'
    :type reg_val1: u32 \*

.. _`i40e_aq_alternate_read.description`:

Description
-----------

Read one or two dwords from alternate structure. Fields are indicated
by 'reg_addr0' and 'reg_addr1' register numbers. If 'reg_val1' pointer
is not passed then only register at 'reg_addr0' is read.

.. _`i40e_aq_resume_port_tx`:

i40e_aq_resume_port_tx
======================

.. c:function:: i40e_status i40e_aq_resume_port_tx(struct i40e_hw *hw, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_resume_port_tx.description`:

Description
-----------

Resume port's Tx traffic

.. _`i40e_set_pci_config_data`:

i40e_set_pci_config_data
========================

.. c:function:: void i40e_set_pci_config_data(struct i40e_hw *hw, u16 link_status)

    store PCI bus info

    :param hw:
        pointer to hardware structure
    :type hw: struct i40e_hw \*

    :param link_status:
        the link status word from PCI config space
    :type link_status: u16

.. _`i40e_set_pci_config_data.description`:

Description
-----------

Stores the PCI bus info (speed, width, type) within the i40e_hw structure

.. _`i40e_aq_debug_dump`:

i40e_aq_debug_dump
==================

.. c:function:: i40e_status i40e_aq_debug_dump(struct i40e_hw *hw, u8 cluster_id, u8 table_id, u32 start_index, u16 buff_size, void *buff, u16 *ret_buff_size, u8 *ret_next_table, u32 *ret_next_index, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param cluster_id:
        specific cluster to dump
    :type cluster_id: u8

    :param table_id:
        table id within cluster
    :type table_id: u8

    :param start_index:
        index of line in the block to read
    :type start_index: u32

    :param buff_size:
        dump buffer size
    :type buff_size: u16

    :param buff:
        dump buffer
    :type buff: void \*

    :param ret_buff_size:
        actual buffer size returned
    :type ret_buff_size: u16 \*

    :param ret_next_table:
        next block to read
    :type ret_next_table: u8 \*

    :param ret_next_index:
        next index to read
    :type ret_next_index: u32 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_debug_dump.description`:

Description
-----------

Dump internal FW/HW data for debug purposes.

.. _`i40e_read_bw_from_alt_ram`:

i40e_read_bw_from_alt_ram
=========================

.. c:function:: i40e_status i40e_read_bw_from_alt_ram(struct i40e_hw *hw, u32 *max_bw, u32 *min_bw, bool *min_valid, bool *max_valid)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param max_bw:
        pointer for max_bw read
    :type max_bw: u32 \*

    :param min_bw:
        pointer for min_bw read
    :type min_bw: u32 \*

    :param min_valid:
        pointer for bool that is true if min_bw is a valid value
    :type min_valid: bool \*

    :param max_valid:
        pointer for bool that is true if max_bw is a valid value
    :type max_valid: bool \*

.. _`i40e_read_bw_from_alt_ram.description`:

Description
-----------

Read bw from the alternate ram for the given pf

.. _`i40e_aq_configure_partition_bw`:

i40e_aq_configure_partition_bw
==============================

.. c:function:: i40e_status i40e_aq_configure_partition_bw(struct i40e_hw *hw, struct i40e_aqc_configure_partition_bw_data *bw_data, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param bw_data:
        Buffer holding valid pfs and bw limits
    :type bw_data: struct i40e_aqc_configure_partition_bw_data \*

    :param cmd_details:
        pointer to command details
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_configure_partition_bw.description`:

Description
-----------

Configure partitions guaranteed/max bw

.. _`i40e_read_phy_register_clause22`:

i40e_read_phy_register_clause22
===============================

.. c:function:: i40e_status i40e_read_phy_register_clause22(struct i40e_hw *hw, u16 reg, u8 phy_addr, u16 *value)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param reg:
        register address in the page
    :type reg: u16

    :param phy_addr:
        PHY address on MDIO interface
    :type phy_addr: u8

    :param value:
        PHY register value
    :type value: u16 \*

.. _`i40e_read_phy_register_clause22.description`:

Description
-----------

Reads specified PHY register value

.. _`i40e_write_phy_register_clause22`:

i40e_write_phy_register_clause22
================================

.. c:function:: i40e_status i40e_write_phy_register_clause22(struct i40e_hw *hw, u16 reg, u8 phy_addr, u16 value)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param reg:
        register address in the page
    :type reg: u16

    :param phy_addr:
        PHY address on MDIO interface
    :type phy_addr: u8

    :param value:
        PHY register value
    :type value: u16

.. _`i40e_write_phy_register_clause22.description`:

Description
-----------

Writes specified PHY register value

.. _`i40e_read_phy_register_clause45`:

i40e_read_phy_register_clause45
===============================

.. c:function:: i40e_status i40e_read_phy_register_clause45(struct i40e_hw *hw, u8 page, u16 reg, u8 phy_addr, u16 *value)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param page:
        registers page number
    :type page: u8

    :param reg:
        register address in the page
    :type reg: u16

    :param phy_addr:
        PHY address on MDIO interface
    :type phy_addr: u8

    :param value:
        PHY register value
    :type value: u16 \*

.. _`i40e_read_phy_register_clause45.description`:

Description
-----------

Reads specified PHY register value

.. _`i40e_write_phy_register_clause45`:

i40e_write_phy_register_clause45
================================

.. c:function:: i40e_status i40e_write_phy_register_clause45(struct i40e_hw *hw, u8 page, u16 reg, u8 phy_addr, u16 value)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param page:
        registers page number
    :type page: u8

    :param reg:
        register address in the page
    :type reg: u16

    :param phy_addr:
        PHY address on MDIO interface
    :type phy_addr: u8

    :param value:
        PHY register value
    :type value: u16

.. _`i40e_write_phy_register_clause45.description`:

Description
-----------

Writes value to specified PHY register

.. _`i40e_write_phy_register`:

i40e_write_phy_register
=======================

.. c:function:: i40e_status i40e_write_phy_register(struct i40e_hw *hw, u8 page, u16 reg, u8 phy_addr, u16 value)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param page:
        registers page number
    :type page: u8

    :param reg:
        register address in the page
    :type reg: u16

    :param phy_addr:
        PHY address on MDIO interface
    :type phy_addr: u8

    :param value:
        PHY register value
    :type value: u16

.. _`i40e_write_phy_register.description`:

Description
-----------

Writes value to specified PHY register

.. _`i40e_read_phy_register`:

i40e_read_phy_register
======================

.. c:function:: i40e_status i40e_read_phy_register(struct i40e_hw *hw, u8 page, u16 reg, u8 phy_addr, u16 *value)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param page:
        registers page number
    :type page: u8

    :param reg:
        register address in the page
    :type reg: u16

    :param phy_addr:
        PHY address on MDIO interface
    :type phy_addr: u8

    :param value:
        PHY register value
    :type value: u16 \*

.. _`i40e_read_phy_register.description`:

Description
-----------

Reads specified PHY register value

.. _`i40e_get_phy_address`:

i40e_get_phy_address
====================

.. c:function:: u8 i40e_get_phy_address(struct i40e_hw *hw, u8 dev_num)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param dev_num:
        PHY port num that address we want
    :type dev_num: u8

.. _`i40e_get_phy_address.description`:

Description
-----------

Gets PHY address for current port

.. _`i40e_blink_phy_link_led`:

i40e_blink_phy_link_led
=======================

.. c:function:: i40e_status i40e_blink_phy_link_led(struct i40e_hw *hw, u32 time, u32 interval)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param time:
        time how long led will blinks in secs
    :type time: u32

    :param interval:
        gap between LED on and off in msecs
    :type interval: u32

.. _`i40e_blink_phy_link_led.description`:

Description
-----------

Blinks PHY link LED

.. _`i40e_led_get_reg`:

i40e_led_get_reg
================

.. c:function:: enum i40e_status_code i40e_led_get_reg(struct i40e_hw *hw, u16 led_addr, u32 *reg_val)

    read LED register

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param led_addr:
        LED register address
    :type led_addr: u16

    :param reg_val:
        read register value
    :type reg_val: u32 \*

.. _`i40e_led_set_reg`:

i40e_led_set_reg
================

.. c:function:: enum i40e_status_code i40e_led_set_reg(struct i40e_hw *hw, u16 led_addr, u32 reg_val)

    write LED register

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param led_addr:
        LED register address
    :type led_addr: u16

    :param reg_val:
        register value to write
    :type reg_val: u32

.. _`i40e_led_get_phy`:

i40e_led_get_phy
================

.. c:function:: i40e_status i40e_led_get_phy(struct i40e_hw *hw, u16 *led_addr, u16 *val)

    return current on/off mode

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param led_addr:
        address of led register to use
    :type led_addr: u16 \*

    :param val:
        original value of register to use
    :type val: u16 \*

.. _`i40e_led_set_phy`:

i40e_led_set_phy
================

.. c:function:: i40e_status i40e_led_set_phy(struct i40e_hw *hw, bool on, u16 led_addr, u32 mode)

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param on:
        true or false
    :type on: bool

    :param led_addr:
        address of led register to use
    :type led_addr: u16

    :param mode:
        original val plus bit for set or ignore
    :type mode: u32

.. _`i40e_led_set_phy.description`:

Description
-----------

Set led's on or off when controlled by the PHY

.. _`i40e_aq_rx_ctl_read_register`:

i40e_aq_rx_ctl_read_register
============================

.. c:function:: i40e_status i40e_aq_rx_ctl_read_register(struct i40e_hw *hw, u32 reg_addr, u32 *reg_val, struct i40e_asq_cmd_details *cmd_details)

    use FW to read from an Rx control register

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param reg_addr:
        register address
    :type reg_addr: u32

    :param reg_val:
        ptr to register value
    :type reg_val: u32 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_rx_ctl_read_register.description`:

Description
-----------

Use the firmware to read the Rx control register,
especially useful if the Rx unit is under heavy pressure

.. _`i40e_read_rx_ctl`:

i40e_read_rx_ctl
================

.. c:function:: u32 i40e_read_rx_ctl(struct i40e_hw *hw, u32 reg_addr)

    read from an Rx control register

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param reg_addr:
        register address
    :type reg_addr: u32

.. _`i40e_aq_rx_ctl_write_register`:

i40e_aq_rx_ctl_write_register
=============================

.. c:function:: i40e_status i40e_aq_rx_ctl_write_register(struct i40e_hw *hw, u32 reg_addr, u32 reg_val, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param reg_addr:
        register address
    :type reg_addr: u32

    :param reg_val:
        register value
    :type reg_val: u32

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_rx_ctl_write_register.description`:

Description
-----------

Use the firmware to write to an Rx control register,
especially useful if the Rx unit is under heavy pressure

.. _`i40e_write_rx_ctl`:

i40e_write_rx_ctl
=================

.. c:function:: void i40e_write_rx_ctl(struct i40e_hw *hw, u32 reg_addr, u32 reg_val)

    write to an Rx control register

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param reg_addr:
        register address
    :type reg_addr: u32

    :param reg_val:
        register value
    :type reg_val: u32

.. _`i40e_aq_set_phy_register`:

i40e_aq_set_phy_register
========================

.. c:function:: i40e_status i40e_aq_set_phy_register(struct i40e_hw *hw, u8 phy_select, u8 dev_addr, u32 reg_addr, u32 reg_val, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param phy_select:
        select which phy should be accessed
    :type phy_select: u8

    :param dev_addr:
        PHY device address
    :type dev_addr: u8

    :param reg_addr:
        PHY register address
    :type reg_addr: u32

    :param reg_val:
        new register value
    :type reg_val: u32

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_set_phy_register.description`:

Description
-----------

Write the external PHY register.

.. _`i40e_aq_get_phy_register`:

i40e_aq_get_phy_register
========================

.. c:function:: i40e_status i40e_aq_get_phy_register(struct i40e_hw *hw, u8 phy_select, u8 dev_addr, u32 reg_addr, u32 *reg_val, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param phy_select:
        select which phy should be accessed
    :type phy_select: u8

    :param dev_addr:
        PHY device address
    :type dev_addr: u8

    :param reg_addr:
        PHY register address
    :type reg_addr: u32

    :param reg_val:
        read register value
    :type reg_val: u32 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_phy_register.description`:

Description
-----------

Read the external PHY register.

.. _`i40e_aq_write_ddp`:

i40e_aq_write_ddp
=================

.. c:function:: enum i40e_status_code i40e_aq_write_ddp(struct i40e_hw *hw, void *buff, u16 buff_size, u32 track_id, u32 *error_offset, u32 *error_info, struct i40e_asq_cmd_details *cmd_details)

    Write dynamic device personalization (ddp)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param buff:
        command buffer (size in bytes = buff_size)
    :type buff: void \*

    :param buff_size:
        buffer size in bytes
    :type buff_size: u16

    :param track_id:
        package tracking id
    :type track_id: u32

    :param error_offset:
        returns error offset
    :type error_offset: u32 \*

    :param error_info:
        returns error information
    :type error_info: u32 \*

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_aq_get_ddp_list`:

i40e_aq_get_ddp_list
====================

.. c:function:: enum i40e_status_code i40e_aq_get_ddp_list(struct i40e_hw *hw, void *buff, u16 buff_size, u8 flags, struct i40e_asq_cmd_details *cmd_details)

    Read dynamic device personalization (ddp)

    :param hw:
        pointer to the hw struct
    :type hw: struct i40e_hw \*

    :param buff:
        command buffer (size in bytes = buff_size)
    :type buff: void \*

    :param buff_size:
        buffer size in bytes
    :type buff_size: u16

    :param flags:
        AdminQ command flags
    :type flags: u8

    :param cmd_details:
        pointer to command details structure or NULL
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`i40e_find_segment_in_package`:

i40e_find_segment_in_package
============================

.. c:function:: struct i40e_generic_seg_header *i40e_find_segment_in_package(u32 segment_type, struct i40e_package_header *pkg_hdr)

    :param segment_type:
        the segment type to search for (i.e., SEGMENT_TYPE_I40E)
    :type segment_type: u32

    :param pkg_hdr:
        pointer to the package header to be searched
    :type pkg_hdr: struct i40e_package_header \*

.. _`i40e_find_segment_in_package.description`:

Description
-----------

This function searches a package file for a particular segment type. On
success it returns a pointer to the segment header, otherwise it will
return NULL.

.. _`i40e_write_profile`:

i40e_write_profile
==================

.. c:function:: enum i40e_status_code i40e_write_profile(struct i40e_hw *hw, struct i40e_profile_segment *profile, u32 track_id)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param profile:
        pointer to the profile segment of the package to be downloaded
    :type profile: struct i40e_profile_segment \*

    :param track_id:
        package tracking id
    :type track_id: u32

.. _`i40e_write_profile.description`:

Description
-----------

Handles the download of a complete package.

.. _`i40e_add_pinfo_to_list`:

i40e_add_pinfo_to_list
======================

.. c:function:: enum i40e_status_code i40e_add_pinfo_to_list(struct i40e_hw *hw, struct i40e_profile_segment *profile, u8 *profile_info_sec, u32 track_id)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param profile:
        pointer to the profile segment of the package
    :type profile: struct i40e_profile_segment \*

    :param profile_info_sec:
        buffer for information section
    :type profile_info_sec: u8 \*

    :param track_id:
        package tracking id
    :type track_id: u32

.. _`i40e_add_pinfo_to_list.description`:

Description
-----------

Register a profile to the list of loaded profiles.

.. _`i40e_aq_add_cloud_filters`:

i40e_aq_add_cloud_filters
=========================

.. c:function:: enum i40e_status_code i40e_aq_add_cloud_filters(struct i40e_hw *hw, u16 seid, struct i40e_aqc_cloud_filters_element_data *filters, u8 filter_count)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid to add cloud filters from
    :type seid: u16

    :param filters:
        Buffer which contains the filters to be added
    :type filters: struct i40e_aqc_cloud_filters_element_data \*

    :param filter_count:
        number of filters contained in the buffer
    :type filter_count: u8

.. _`i40e_aq_add_cloud_filters.description`:

Description
-----------

Set the cloud filters for a given VSI.  The contents of the
i40e_aqc_cloud_filters_element_data are filled in by the caller
of the function.

.. _`i40e_aq_add_cloud_filters_bb`:

i40e_aq_add_cloud_filters_bb
============================

.. c:function:: enum i40e_status_code i40e_aq_add_cloud_filters_bb(struct i40e_hw *hw, u16 seid, struct i40e_aqc_cloud_filters_element_bb *filters, u8 filter_count)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid to add cloud filters from
    :type seid: u16

    :param filters:
        Buffer which contains the filters in big buffer to be added
    :type filters: struct i40e_aqc_cloud_filters_element_bb \*

    :param filter_count:
        number of filters contained in the buffer
    :type filter_count: u8

.. _`i40e_aq_add_cloud_filters_bb.description`:

Description
-----------

Set the big buffer cloud filters for a given VSI.  The contents of the
i40e_aqc_cloud_filters_element_bb are filled in by the caller of the
function.

.. _`i40e_aq_rem_cloud_filters`:

i40e_aq_rem_cloud_filters
=========================

.. c:function:: enum i40e_status_code i40e_aq_rem_cloud_filters(struct i40e_hw *hw, u16 seid, struct i40e_aqc_cloud_filters_element_data *filters, u8 filter_count)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid to remove cloud filters from
    :type seid: u16

    :param filters:
        Buffer which contains the filters to be removed
    :type filters: struct i40e_aqc_cloud_filters_element_data \*

    :param filter_count:
        number of filters contained in the buffer
    :type filter_count: u8

.. _`i40e_aq_rem_cloud_filters.description`:

Description
-----------

Remove the cloud filters for a given VSI.  The contents of the
i40e_aqc_cloud_filters_element_data are filled in by the caller
of the function.

.. _`i40e_aq_rem_cloud_filters_bb`:

i40e_aq_rem_cloud_filters_bb
============================

.. c:function:: enum i40e_status_code i40e_aq_rem_cloud_filters_bb(struct i40e_hw *hw, u16 seid, struct i40e_aqc_cloud_filters_element_bb *filters, u8 filter_count)

    :param hw:
        pointer to the hardware structure
    :type hw: struct i40e_hw \*

    :param seid:
        VSI seid to remove cloud filters from
    :type seid: u16

    :param filters:
        Buffer which contains the filters in big buffer to be removed
    :type filters: struct i40e_aqc_cloud_filters_element_bb \*

    :param filter_count:
        number of filters contained in the buffer
    :type filter_count: u8

.. _`i40e_aq_rem_cloud_filters_bb.description`:

Description
-----------

Remove the big buffer cloud filters for a given VSI.  The contents of the
i40e_aqc_cloud_filters_element_bb are filled in by the caller of the
function.

.. This file was automatic generated / don't edit.

