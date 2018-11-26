.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_common.c

.. _`ice_set_mac_type`:

ice_set_mac_type
================

.. c:function:: enum ice_status ice_set_mac_type(struct ice_hw *hw)

    Sets MAC type

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

.. _`ice_set_mac_type.description`:

Description
-----------

This function sets the MAC type of the adapter based on the
vendor ID and device ID stored in the hw structure.

.. _`ice_dev_onetime_setup`:

ice_dev_onetime_setup
=====================

.. c:function:: void ice_dev_onetime_setup(struct ice_hw *hw)

    Temporary HW/FW workarounds

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

.. _`ice_dev_onetime_setup.description`:

Description
-----------

This function provides temporary workarounds for certain issues
that are expected to be fixed in the HW/FW.

.. _`ice_clear_pf_cfg`:

ice_clear_pf_cfg
================

.. c:function:: enum ice_status ice_clear_pf_cfg(struct ice_hw *hw)

    Clear PF configuration

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_clear_pf_cfg.description`:

Description
-----------

Clears any existing PF configuration (VSIs, VSI lists, switch rules, port
configuration, flow director filters, etc.).

.. _`ice_aq_manage_mac_read`:

ice_aq_manage_mac_read
======================

.. c:function:: enum ice_status ice_aq_manage_mac_read(struct ice_hw *hw, void *buf, u16 buf_size, struct ice_sq_cd *cd)

    manage MAC address read command

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param buf:
        a virtual buffer to hold the manage MAC read response
    :type buf: void \*

    :param buf_size:
        Size of the virtual buffer
    :type buf_size: u16

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_manage_mac_read.description`:

Description
-----------

This function is used to return per PF station MAC address (0x0107).

.. _`ice_aq_manage_mac_read.note`:

NOTE
----

Upon successful completion of this command, MAC address information
is returned in user specified buffer. Please interpret user specified
buffer as "manage_mac_read" response.
Response such as various MAC addresses are stored in HW struct (port.mac)
ice_aq_discover_caps is expected to be called before this function is called.

.. _`ice_aq_get_phy_caps`:

ice_aq_get_phy_caps
===================

.. c:function:: enum ice_status ice_aq_get_phy_caps(struct ice_port_info *pi, bool qual_mods, u8 report_mode, struct ice_aqc_get_phy_caps_data *pcaps, struct ice_sq_cd *cd)

    returns PHY capabilities

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param qual_mods:
        report qualified modules
    :type qual_mods: bool

    :param report_mode:
        report mode capabilities
    :type report_mode: u8

    :param pcaps:
        structure for PHY capabilities to be filled
    :type pcaps: struct ice_aqc_get_phy_caps_data \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_get_phy_caps.description`:

Description
-----------

Returns the various PHY capabilities supported on the Port (0x0600)

.. _`ice_get_media_type`:

ice_get_media_type
==================

.. c:function:: enum ice_media_type ice_get_media_type(struct ice_port_info *pi)

    Gets media type

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

.. _`ice_aq_get_link_info`:

ice_aq_get_link_info
====================

.. c:function:: enum ice_status ice_aq_get_link_info(struct ice_port_info *pi, bool ena_lse, struct ice_link_status *link, struct ice_sq_cd *cd)

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param ena_lse:
        enable/disable LinkStatusEvent reporting
    :type ena_lse: bool

    :param link:
        pointer to link status structure - optional
    :type link: struct ice_link_status \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_get_link_info.description`:

Description
-----------

Get Link Status (0x607). Returns the link status of the adapter.

.. _`ice_init_flex_flags`:

ice_init_flex_flags
===================

.. c:function:: void ice_init_flex_flags(struct ice_hw *hw, enum ice_rxdid prof_id)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param prof_id:
        Rx Descriptor Builder profile ID
    :type prof_id: enum ice_rxdid

.. _`ice_init_flex_flags.description`:

Description
-----------

Function to initialize Rx flex flags

.. _`ice_init_flex_flds`:

ice_init_flex_flds
==================

.. c:function:: void ice_init_flex_flds(struct ice_hw *hw, enum ice_rxdid prof_id)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param prof_id:
        Rx Descriptor Builder profile ID
    :type prof_id: enum ice_rxdid

.. _`ice_init_flex_flds.description`:

Description
-----------

Function to initialize flex descriptors

.. _`ice_init_fltr_mgmt_struct`:

ice_init_fltr_mgmt_struct
=========================

.. c:function:: enum ice_status ice_init_fltr_mgmt_struct(struct ice_hw *hw)

    initializes filter management list and locks

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_cleanup_fltr_mgmt_struct`:

ice_cleanup_fltr_mgmt_struct
============================

.. c:function:: void ice_cleanup_fltr_mgmt_struct(struct ice_hw *hw)

    cleanup filter management list and locks

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_cfg_fw_log`:

ice_cfg_fw_log
==============

.. c:function:: enum ice_status ice_cfg_fw_log(struct ice_hw *hw, bool enable)

    configure FW logging

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param enable:
        enable certain FW logging events if true, disable all if false
    :type enable: bool

.. _`ice_cfg_fw_log.description`:

Description
-----------

This function enables/disables the FW logging via Rx CQ events and a UART
port based on predetermined configurations. FW logging via the Rx CQ can be
enabled/disabled for individual PF's. However, FW logging via the UART can
only be enabled/disabled for all PFs on the same device.

To enable overall FW logging, the "cq_en" and "uart_en" enable bits in
hw->fw_log need to be set accordingly, e.g. based on user-provided input,
before initializing the device.

When re/configuring FW logging, callers need to update the "cfg" elements of
the hw->fw_log.evnts array with the desired logging event configurations for
modules of interest. When disabling FW logging completely, the callers can
just pass false in the "enable" parameter. On completion, the function will
update the "cur" element of the hw->fw_log.evnts array with the resulting
logging event configurations of the modules that are being re/configured. FW
logging modules that are not part of a reconfiguration operation retain their
previous states.

Before resetting the device, it is recommended that the driver disables FW
logging before shutting down the control queue. When disabling FW logging
("enable" = false), the latest configurations of FW logging events stored in
hw->fw_log.evnts[] are not overridden to allow them to be reconfigured after
a device reset.

When enabling FW logging to emit log messages via the Rx CQ during the
device's initialization phase, a mechanism alternative to interrupt handlers
needs to be used to extract FW log messages from the Rx CQ periodically and
to prevent the Rx CQ from being full and stalling other types of control
messages from FW to SW. Interrupts are typically disabled during the device's
initialization phase.

.. _`ice_output_fw_log`:

ice_output_fw_log
=================

.. c:function:: void ice_output_fw_log(struct ice_hw *hw, struct ice_aq_desc *desc, void *buf)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param desc:
        pointer to the AQ message descriptor
    :type desc: struct ice_aq_desc \*

    :param buf:
        pointer to the buffer accompanying the AQ message
    :type buf: void \*

.. _`ice_output_fw_log.description`:

Description
-----------

Formats a FW Log message and outputs it via the standard driver logs.

.. _`ice_get_itr_intrl_gran`:

ice_get_itr_intrl_gran
======================

.. c:function:: enum ice_status ice_get_itr_intrl_gran(struct ice_hw *hw)

    determine int/intrl granularity

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_get_itr_intrl_gran.description`:

Description
-----------

Determines the itr/intrl granularities based on the maximum aggregate
bandwidth according to the device's configuration during power-on.

.. _`ice_init_hw`:

ice_init_hw
===========

.. c:function:: enum ice_status ice_init_hw(struct ice_hw *hw)

    main hardware initialization routine

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_deinit_hw`:

ice_deinit_hw
=============

.. c:function:: void ice_deinit_hw(struct ice_hw *hw)

    unroll initialization operations done by ice_init_hw

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_check_reset`:

ice_check_reset
===============

.. c:function:: enum ice_status ice_check_reset(struct ice_hw *hw)

    Check to see if a global reset is complete

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_pf_reset`:

ice_pf_reset
============

.. c:function:: enum ice_status ice_pf_reset(struct ice_hw *hw)

    Reset the PF

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_pf_reset.description`:

Description
-----------

If a global reset has been triggered, this function checks
for its completion and then issues the PF reset

.. _`ice_reset`:

ice_reset
=========

.. c:function:: enum ice_status ice_reset(struct ice_hw *hw, enum ice_reset_req req)

    Perform different types of reset

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param req:
        reset request
    :type req: enum ice_reset_req

.. _`ice_reset.description`:

Description
-----------

This function triggers a reset as specified by the req parameter.

.. _`ice_reset.note`:

Note
----

If anything other than a PF reset is triggered, PXE mode is restored.
This has to be cleared using ice_clear_pxe_mode again, once the AQ
interface has been restored in the rebuild flow.

.. _`ice_copy_rxq_ctx_to_hw`:

ice_copy_rxq_ctx_to_hw
======================

.. c:function:: enum ice_status ice_copy_rxq_ctx_to_hw(struct ice_hw *hw, u8 *ice_rxq_ctx, u32 rxq_index)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param ice_rxq_ctx:
        pointer to the rxq context
    :type ice_rxq_ctx: u8 \*

    :param rxq_index:
        the index of the rx queue
    :type rxq_index: u32

.. _`ice_copy_rxq_ctx_to_hw.description`:

Description
-----------

Copies rxq context from dense structure to hw register space

.. _`ice_write_rxq_ctx`:

ice_write_rxq_ctx
=================

.. c:function:: enum ice_status ice_write_rxq_ctx(struct ice_hw *hw, struct ice_rlan_ctx *rlan_ctx, u32 rxq_index)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param rlan_ctx:
        pointer to the rxq context
    :type rlan_ctx: struct ice_rlan_ctx \*

    :param rxq_index:
        the index of the rx queue
    :type rxq_index: u32

.. _`ice_write_rxq_ctx.description`:

Description
-----------

Converts rxq context from sparse to dense structure and then writes
it to hw register space

.. _`ice_debug_cq`:

ice_debug_cq
============

.. c:function:: void ice_debug_cq(struct ice_hw *hw, u32 __maybe_unused mask, void *desc, void *buf, u16 buf_len)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param mask:
        debug mask
    :type mask: u32 __maybe_unused

    :param desc:
        pointer to control queue descriptor
    :type desc: void \*

    :param buf:
        pointer to command buffer
    :type buf: void \*

    :param buf_len:
        max length of buf
    :type buf_len: u16

.. _`ice_debug_cq.description`:

Description
-----------

Dumps debug log about control command with descriptor contents.

.. _`ice_aq_send_cmd`:

ice_aq_send_cmd
===============

.. c:function:: enum ice_status ice_aq_send_cmd(struct ice_hw *hw, struct ice_aq_desc *desc, void *buf, u16 buf_size, struct ice_sq_cd *cd)

    send FW Admin Queue command to FW Admin Queue

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param desc:
        descriptor describing the command
    :type desc: struct ice_aq_desc \*

    :param buf:
        buffer to use for indirect commands (NULL for direct commands)
    :type buf: void \*

    :param buf_size:
        size of buffer for indirect commands (0 for direct commands)
    :type buf_size: u16

    :param cd:
        pointer to command details structure
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_send_cmd.description`:

Description
-----------

Helper function to send FW Admin Queue commands to the FW Admin Queue.

.. _`ice_aq_get_fw_ver`:

ice_aq_get_fw_ver
=================

.. c:function:: enum ice_status ice_aq_get_fw_ver(struct ice_hw *hw, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_get_fw_ver.description`:

Description
-----------

Get the firmware version (0x0001) from the admin queue commands

.. _`ice_aq_q_shutdown`:

ice_aq_q_shutdown
=================

.. c:function:: enum ice_status ice_aq_q_shutdown(struct ice_hw *hw, bool unloading)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param unloading:
        is the driver unloading itself
    :type unloading: bool

.. _`ice_aq_q_shutdown.description`:

Description
-----------

Tell the Firmware that we're shutting down the AdminQ and whether
or not the driver is unloading as well (0x0003).

.. _`ice_aq_req_res`:

ice_aq_req_res
==============

.. c:function:: enum ice_status ice_aq_req_res(struct ice_hw *hw, enum ice_aq_res_ids res, enum ice_aq_res_access_type access, u8 sdp_number, u32 *timeout, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param res:
        resource id
    :type res: enum ice_aq_res_ids

    :param access:
        access type
    :type access: enum ice_aq_res_access_type

    :param sdp_number:
        resource number
    :type sdp_number: u8

    :param timeout:
        the maximum time in ms that the driver may hold the resource
    :type timeout: u32 \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_req_res.description`:

Description
-----------

Requests common resource using the admin queue commands (0x0008).
When attempting to acquire the Global Config Lock, the driver can

.. _`ice_aq_req_res.learn-of-three-states`:

learn of three states
---------------------

1) ICE_SUCCESS -        acquired lock, and can perform download package
2) ICE_ERR_AQ_ERROR -   did not get lock, driver should fail to load
3) ICE_ERR_AQ_NO_WORK - did not get lock, but another driver has
successfully downloaded the package; the driver does
not have to download the package and can continue
loading

Note that if the caller is in an acquire lock, perform action, release lock
phase of operation, it is possible that the FW may detect a timeout and issue
a CORER. In this case, the driver will receive a CORER interrupt and will
have to determine its cause. The calling thread that is handling this flow
will likely get an error propagated back to it indicating the Download
Package, Update Package or the Release Resource AQ commands timed out.

.. _`ice_aq_release_res`:

ice_aq_release_res
==================

.. c:function:: enum ice_status ice_aq_release_res(struct ice_hw *hw, enum ice_aq_res_ids res, u8 sdp_number, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param res:
        resource id
    :type res: enum ice_aq_res_ids

    :param sdp_number:
        resource number
    :type sdp_number: u8

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_release_res.description`:

Description
-----------

release common resource using the admin queue commands (0x0009)

.. _`ice_acquire_res`:

ice_acquire_res
===============

.. c:function:: enum ice_status ice_acquire_res(struct ice_hw *hw, enum ice_aq_res_ids res, enum ice_aq_res_access_type access, u32 timeout)

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param res:
        resource id
    :type res: enum ice_aq_res_ids

    :param access:
        access type (read or write)
    :type access: enum ice_aq_res_access_type

    :param timeout:
        timeout in milliseconds
    :type timeout: u32

.. _`ice_acquire_res.description`:

Description
-----------

This function will attempt to acquire the ownership of a resource.

.. _`ice_release_res`:

ice_release_res
===============

.. c:function:: void ice_release_res(struct ice_hw *hw, enum ice_aq_res_ids res)

    :param hw:
        pointer to the HW structure
    :type hw: struct ice_hw \*

    :param res:
        resource id
    :type res: enum ice_aq_res_ids

.. _`ice_release_res.description`:

Description
-----------

This function will release a resource using the proper Admin Command.

.. _`ice_parse_caps`:

ice_parse_caps
==============

.. c:function:: void ice_parse_caps(struct ice_hw *hw, void *buf, u32 cap_count, enum ice_adminq_opc opc)

    parse function/device capabilities

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param buf:
        pointer to a buffer containing function/device capability records
    :type buf: void \*

    :param cap_count:
        number of capability records in the list
    :type cap_count: u32

    :param opc:
        type of capabilities list to parse
    :type opc: enum ice_adminq_opc

.. _`ice_parse_caps.description`:

Description
-----------

Helper function to parse function(0x000a)/device(0x000b) capabilities list.

.. _`ice_aq_discover_caps`:

ice_aq_discover_caps
====================

.. c:function:: enum ice_status ice_aq_discover_caps(struct ice_hw *hw, void *buf, u16 buf_size, u32 *cap_count, enum ice_adminq_opc opc, struct ice_sq_cd *cd)

    query function/device capabilities

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param buf:
        a virtual buffer to hold the capabilities
    :type buf: void \*

    :param buf_size:
        Size of the virtual buffer
    :type buf_size: u16

    :param cap_count:
        cap count needed if AQ err==ENOMEM
    :type cap_count: u32 \*

    :param opc:
        capabilities type to discover - pass in the command opcode
    :type opc: enum ice_adminq_opc

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_discover_caps.description`:

Description
-----------

Get the function(0x000a)/device(0x000b) capabilities description from
the firmware.

.. _`ice_discover_caps`:

ice_discover_caps
=================

.. c:function:: enum ice_status ice_discover_caps(struct ice_hw *hw, enum ice_adminq_opc opc)

    get info about the HW

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param opc:
        capabilities type to discover - pass in the command opcode
    :type opc: enum ice_adminq_opc

.. _`ice_get_caps`:

ice_get_caps
============

.. c:function:: enum ice_status ice_get_caps(struct ice_hw *hw)

    get info about the HW

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_aq_manage_mac_write`:

ice_aq_manage_mac_write
=======================

.. c:function:: enum ice_status ice_aq_manage_mac_write(struct ice_hw *hw, u8 *mac_addr, u8 flags, struct ice_sq_cd *cd)

    manage MAC address write command

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param mac_addr:
        MAC address to be written as LAA/LAA+WoL/Port address
    :type mac_addr: u8 \*

    :param flags:
        flags to control write behavior
    :type flags: u8

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_manage_mac_write.description`:

Description
-----------

This function is used to write MAC address to the NVM (0x0108).

.. _`ice_aq_clear_pxe_mode`:

ice_aq_clear_pxe_mode
=====================

.. c:function:: enum ice_status ice_aq_clear_pxe_mode(struct ice_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_aq_clear_pxe_mode.description`:

Description
-----------

Tell the firmware that the driver is taking over from PXE (0x0110).

.. _`ice_clear_pxe_mode`:

ice_clear_pxe_mode
==================

.. c:function:: void ice_clear_pxe_mode(struct ice_hw *hw)

    clear pxe operations mode

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_clear_pxe_mode.description`:

Description
-----------

Make sure all PXE mode settings are cleared, including things
like descriptor fetch/write-back mode.

.. _`ice_get_link_speed_based_on_phy_type`:

ice_get_link_speed_based_on_phy_type
====================================

.. c:function:: u16 ice_get_link_speed_based_on_phy_type(u64 phy_type_low)

    returns link speed

    :param phy_type_low:
        lower part of phy_type
    :type phy_type_low: u64

.. _`ice_get_link_speed_based_on_phy_type.description`:

Description
-----------

This helper function will convert a phy_type_low to its corresponding link
speed.

.. _`ice_get_link_speed_based_on_phy_type.note`:

Note
----

In the structure of phy_type_low, there should be one bit set, as
this function will convert one phy type to its speed.
If no bit gets set, ICE_LINK_SPEED_UNKNOWN will be returned
If more than one bit gets set, ICE_LINK_SPEED_UNKNOWN will be returned

.. _`ice_update_phy_type`:

ice_update_phy_type
===================

.. c:function:: void ice_update_phy_type(u64 *phy_type_low, u16 link_speeds_bitmap)

    :param phy_type_low:
        pointer to the lower part of phy_type
    :type phy_type_low: u64 \*

    :param link_speeds_bitmap:
        targeted link speeds bitmap
    :type link_speeds_bitmap: u16

.. _`ice_update_phy_type.note`:

Note
----

For the link_speeds_bitmap structure, you can check it at
[ice_aqc_get_link_status->link_speed]. Caller can pass in
link_speeds_bitmap include multiple speeds.

The value of phy_type_low will present a certain link speed. This helper
function will turn on bits in the phy_type_low based on the value of
link_speeds_bitmap input parameter.

.. _`ice_aq_set_phy_cfg`:

ice_aq_set_phy_cfg
==================

.. c:function:: enum ice_status ice_aq_set_phy_cfg(struct ice_hw *hw, u8 lport, struct ice_aqc_set_phy_cfg_data *cfg, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param lport:
        logical port number
    :type lport: u8

    :param cfg:
        structure with PHY configuration data to be set
    :type cfg: struct ice_aqc_set_phy_cfg_data \*

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_set_phy_cfg.description`:

Description
-----------

Set the various PHY configuration parameters supported on the Port.
One or more of the Set PHY config parameters may be ignored in an MFP
mode as the PF may not have the privilege to set some of the PHY Config
parameters. This status will be indicated by the command response (0x0601).

.. _`ice_update_link_info`:

ice_update_link_info
====================

.. c:function:: enum ice_status ice_update_link_info(struct ice_port_info *pi)

    update status of the HW network link

    :param pi:
        port info structure of the interested logical port
    :type pi: struct ice_port_info \*

.. _`ice_set_fc`:

ice_set_fc
==========

.. c:function:: enum ice_status ice_set_fc(struct ice_port_info *pi, u8 *aq_failures, bool ena_auto_link_update)

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param aq_failures:
        pointer to status code, specific to ice_set_fc routine
    :type aq_failures: u8 \*

    :param ena_auto_link_update:
        enable automatic link update
    :type ena_auto_link_update: bool

.. _`ice_set_fc.description`:

Description
-----------

Set the requested flow control mode.

.. _`ice_get_link_status`:

ice_get_link_status
===================

.. c:function:: enum ice_status ice_get_link_status(struct ice_port_info *pi, bool *link_up)

    get status of the HW network link

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param link_up:
        pointer to bool (true/false = linkup/linkdown)
    :type link_up: bool \*

.. _`ice_get_link_status.description`:

Description
-----------

Variable link_up is true if link is up, false if link is down.
The variable link_up is invalid if status is non zero. As a
result of this call, link status reporting becomes enabled

.. _`ice_aq_set_link_restart_an`:

ice_aq_set_link_restart_an
==========================

.. c:function:: enum ice_status ice_aq_set_link_restart_an(struct ice_port_info *pi, bool ena_link, struct ice_sq_cd *cd)

    :param pi:
        pointer to the port information structure
    :type pi: struct ice_port_info \*

    :param ena_link:
        if true: enable link, if false: disable link
    :type ena_link: bool

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_set_link_restart_an.description`:

Description
-----------

Sets up the link and restarts the Auto-Negotiation over the link.

.. _`__ice_aq_get_set_rss_lut`:

\__ice_aq_get_set_rss_lut
=========================

.. c:function:: enum ice_status __ice_aq_get_set_rss_lut(struct ice_hw *hw, u16 vsi_id, u8 lut_type, u8 *lut, u16 lut_size, u8 glob_lut_idx, bool set)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_id:
        VSI FW index
    :type vsi_id: u16

    :param lut_type:
        LUT table type
    :type lut_type: u8

    :param lut:
        pointer to the LUT buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the LUT buffer
    :type lut_size: u16

    :param glob_lut_idx:
        global LUT index
    :type glob_lut_idx: u8

    :param set:
        set true to set the table, false to get the table
    :type set: bool

.. _`__ice_aq_get_set_rss_lut.description`:

Description
-----------

Internal function to get (0x0B05) or set (0x0B03) RSS look up table

.. _`ice_aq_get_rss_lut`:

ice_aq_get_rss_lut
==================

.. c:function:: enum ice_status ice_aq_get_rss_lut(struct ice_hw *hw, u16 vsi_handle, u8 lut_type, u8 *lut, u16 lut_size)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param lut_type:
        LUT table type
    :type lut_type: u8

    :param lut:
        pointer to the LUT buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the LUT buffer
    :type lut_size: u16

.. _`ice_aq_get_rss_lut.description`:

Description
-----------

get the RSS lookup table, PF or VSI type

.. _`ice_aq_set_rss_lut`:

ice_aq_set_rss_lut
==================

.. c:function:: enum ice_status ice_aq_set_rss_lut(struct ice_hw *hw, u16 vsi_handle, u8 lut_type, u8 *lut, u16 lut_size)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param lut_type:
        LUT table type
    :type lut_type: u8

    :param lut:
        pointer to the LUT buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the LUT buffer
    :type lut_size: u16

.. _`ice_aq_set_rss_lut.description`:

Description
-----------

set the RSS lookup table, PF or VSI type

.. _`__ice_aq_get_set_rss_key`:

\__ice_aq_get_set_rss_key
=========================

.. c:function:: enum ice_status __ice_aq_get_set_rss_key(struct ice_hw *hw, u16 vsi_id, struct ice_aqc_get_set_rss_keys *key, bool set)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_id:
        VSI FW index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct ice_aqc_get_set_rss_keys \*

    :param set:
        set true to set the key, false to get the key
    :type set: bool

.. _`__ice_aq_get_set_rss_key.description`:

Description
-----------

get (0x0B04) or set (0x0B02) the RSS key per VSI

.. _`ice_aq_get_rss_key`:

ice_aq_get_rss_key
==================

.. c:function:: enum ice_status ice_aq_get_rss_key(struct ice_hw *hw, u16 vsi_handle, struct ice_aqc_get_set_rss_keys *key)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param key:
        pointer to key info struct
    :type key: struct ice_aqc_get_set_rss_keys \*

.. _`ice_aq_get_rss_key.description`:

Description
-----------

get the RSS key per VSI

.. _`ice_aq_set_rss_key`:

ice_aq_set_rss_key
==================

.. c:function:: enum ice_status ice_aq_set_rss_key(struct ice_hw *hw, u16 vsi_handle, struct ice_aqc_get_set_rss_keys *keys)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param keys:
        pointer to key info struct
    :type keys: struct ice_aqc_get_set_rss_keys \*

.. _`ice_aq_set_rss_key.description`:

Description
-----------

set the RSS key per VSI

.. _`ice_aq_add_lan_txq`:

ice_aq_add_lan_txq
==================

.. c:function:: enum ice_status ice_aq_add_lan_txq(struct ice_hw *hw, u8 num_qgrps, struct ice_aqc_add_tx_qgrp *qg_list, u16 buf_size, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param num_qgrps:
        Number of added queue groups
    :type num_qgrps: u8

    :param qg_list:
        list of queue groups to be added
    :type qg_list: struct ice_aqc_add_tx_qgrp \*

    :param buf_size:
        size of buffer for indirect command
    :type buf_size: u16

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_add_lan_txq.description`:

Description
-----------

Add Tx LAN queue (0x0C30)

.. _`ice_aq_add_lan_txq.initialize-the-following-as-part-of-the-tx-queue-context`:

Initialize the following as part of the Tx queue context
--------------------------------------------------------

Completion queue ID if the queue uses Completion queue, Quanta profile,
Cache profile and Packet shaper profile.

.. _`ice_aq_add_lan_txq.after-add-tx-lan-queue-aq-command-is-completed`:

After add Tx LAN queue AQ command is completed
----------------------------------------------

Interrupts should be associated with specific queues,
Association of Tx queue to Doorbell queue is not part of Add LAN Tx queue
flow.

.. _`ice_aq_dis_lan_txq`:

ice_aq_dis_lan_txq
==================

.. c:function:: enum ice_status ice_aq_dis_lan_txq(struct ice_hw *hw, u8 num_qgrps, struct ice_aqc_dis_txq_item *qg_list, u16 buf_size, enum ice_disq_rst_src rst_src, u16 vmvf_num, struct ice_sq_cd *cd)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param num_qgrps:
        number of groups in the list
    :type num_qgrps: u8

    :param qg_list:
        the list of groups to disable
    :type qg_list: struct ice_aqc_dis_txq_item \*

    :param buf_size:
        the total size of the qg_list buffer in bytes
    :type buf_size: u16

    :param rst_src:
        if called due to reset, specifies the RST source
    :type rst_src: enum ice_disq_rst_src

    :param vmvf_num:
        the relative VM or VF number that is undergoing the reset
    :type vmvf_num: u16

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_aq_dis_lan_txq.description`:

Description
-----------

Disable LAN Tx queue (0x0C31)

.. _`ice_write_byte`:

ice_write_byte
==============

.. c:function:: void ice_write_byte(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a byte to a packed context structure

    :param src_ctx:
        the context structure to read from
    :type src_ctx: u8 \*

    :param dest_ctx:
        the context to be written to
    :type dest_ctx: u8 \*

    :param ce_info:
        a description of the struct to be filled
    :type ce_info: const struct ice_ctx_ele \*

.. _`ice_write_word`:

ice_write_word
==============

.. c:function:: void ice_write_word(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a word to a packed context structure

    :param src_ctx:
        the context structure to read from
    :type src_ctx: u8 \*

    :param dest_ctx:
        the context to be written to
    :type dest_ctx: u8 \*

    :param ce_info:
        a description of the struct to be filled
    :type ce_info: const struct ice_ctx_ele \*

.. _`ice_write_dword`:

ice_write_dword
===============

.. c:function:: void ice_write_dword(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a dword to a packed context structure

    :param src_ctx:
        the context structure to read from
    :type src_ctx: u8 \*

    :param dest_ctx:
        the context to be written to
    :type dest_ctx: u8 \*

    :param ce_info:
        a description of the struct to be filled
    :type ce_info: const struct ice_ctx_ele \*

.. _`ice_write_qword`:

ice_write_qword
===============

.. c:function:: void ice_write_qword(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a qword to a packed context structure

    :param src_ctx:
        the context structure to read from
    :type src_ctx: u8 \*

    :param dest_ctx:
        the context to be written to
    :type dest_ctx: u8 \*

    :param ce_info:
        a description of the struct to be filled
    :type ce_info: const struct ice_ctx_ele \*

.. _`ice_set_ctx`:

ice_set_ctx
===========

.. c:function:: enum ice_status ice_set_ctx(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    set context bits in packed structure

    :param src_ctx:
        pointer to a generic non-packed context structure
    :type src_ctx: u8 \*

    :param dest_ctx:
        pointer to memory for the packed structure
    :type dest_ctx: u8 \*

    :param ce_info:
        a description of the structure to be transformed
    :type ce_info: const struct ice_ctx_ele \*

.. _`ice_ena_vsi_txq`:

ice_ena_vsi_txq
===============

.. c:function:: enum ice_status ice_ena_vsi_txq(struct ice_port_info *pi, u16 vsi_handle, u8 tc, u8 num_qgrps, struct ice_aqc_add_tx_qgrp *buf, u16 buf_size, struct ice_sq_cd *cd)

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc:
        tc number
    :type tc: u8

    :param num_qgrps:
        Number of added queue groups
    :type num_qgrps: u8

    :param buf:
        list of queue groups to be added
    :type buf: struct ice_aqc_add_tx_qgrp \*

    :param buf_size:
        size of buffer for indirect command
    :type buf_size: u16

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_ena_vsi_txq.description`:

Description
-----------

This function adds one lan q

.. _`ice_dis_vsi_txq`:

ice_dis_vsi_txq
===============

.. c:function:: enum ice_status ice_dis_vsi_txq(struct ice_port_info *pi, u8 num_queues, u16 *q_ids, u32 *q_teids, enum ice_disq_rst_src rst_src, u16 vmvf_num, struct ice_sq_cd *cd)

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param num_queues:
        number of queues
    :type num_queues: u8

    :param q_ids:
        pointer to the q_id array
    :type q_ids: u16 \*

    :param q_teids:
        pointer to queue node teids
    :type q_teids: u32 \*

    :param rst_src:
        if called due to reset, specifies the RST source
    :type rst_src: enum ice_disq_rst_src

    :param vmvf_num:
        the relative VM or VF number that is undergoing the reset
    :type vmvf_num: u16

    :param cd:
        pointer to command details structure or NULL
    :type cd: struct ice_sq_cd \*

.. _`ice_dis_vsi_txq.description`:

Description
-----------

This function removes queues and their corresponding nodes in SW DB

.. _`ice_cfg_vsi_qs`:

ice_cfg_vsi_qs
==============

.. c:function:: enum ice_status ice_cfg_vsi_qs(struct ice_port_info *pi, u16 vsi_handle, u8 tc_bitmap, u16 *maxqs, u8 owner)

    configure the new/exisiting VSI queues

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc_bitmap:
        TC bitmap
    :type tc_bitmap: u8

    :param maxqs:
        max queues array per TC
    :type maxqs: u16 \*

    :param owner:
        lan or rdma
    :type owner: u8

.. _`ice_cfg_vsi_qs.description`:

Description
-----------

This function adds/updates the VSI queues per TC.

.. _`ice_cfg_vsi_lan`:

ice_cfg_vsi_lan
===============

.. c:function:: enum ice_status ice_cfg_vsi_lan(struct ice_port_info *pi, u16 vsi_handle, u8 tc_bitmap, u16 *max_lanqs)

    configure VSI lan queues

    :param pi:
        port information structure
    :type pi: struct ice_port_info \*

    :param vsi_handle:
        software VSI handle
    :type vsi_handle: u16

    :param tc_bitmap:
        TC bitmap
    :type tc_bitmap: u8

    :param max_lanqs:
        max lan queues array per TC
    :type max_lanqs: u16 \*

.. _`ice_cfg_vsi_lan.description`:

Description
-----------

This function adds/updates the VSI lan queues per TC.

.. _`ice_replay_pre_init`:

ice_replay_pre_init
===================

.. c:function:: enum ice_status ice_replay_pre_init(struct ice_hw *hw)

    replay pre initialization

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_replay_pre_init.description`:

Description
-----------

Initializes required config data for VSI, FD, ACL, and RSS before replay.

.. _`ice_replay_vsi`:

ice_replay_vsi
==============

.. c:function:: enum ice_status ice_replay_vsi(struct ice_hw *hw, u16 vsi_handle)

    replay VSI configuration

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param vsi_handle:
        driver VSI handle
    :type vsi_handle: u16

.. _`ice_replay_vsi.description`:

Description
-----------

Restore all VSI configuration after reset. It is required to call this
function with main VSI first.

.. _`ice_replay_post`:

ice_replay_post
===============

.. c:function:: void ice_replay_post(struct ice_hw *hw)

    post replay configuration cleanup

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

.. _`ice_replay_post.description`:

Description
-----------

Post replay cleanup.

.. _`ice_stat_update40`:

ice_stat_update40
=================

.. c:function:: void ice_stat_update40(struct ice_hw *hw, u32 hireg, u32 loreg, bool prev_stat_loaded, u64 *prev_stat, u64 *cur_stat)

    read 40 bit stat from the chip and update stat values

    :param hw:
        ptr to the hardware info
    :type hw: struct ice_hw \*

    :param hireg:
        high 32 bit HW register to read from
    :type hireg: u32

    :param loreg:
        low 32 bit HW register to read from
    :type loreg: u32

    :param prev_stat_loaded:
        bool to specify if previous stats are loaded
    :type prev_stat_loaded: bool

    :param prev_stat:
        ptr to previous loaded stat value
    :type prev_stat: u64 \*

    :param cur_stat:
        ptr to current stat value
    :type cur_stat: u64 \*

.. _`ice_stat_update32`:

ice_stat_update32
=================

.. c:function:: void ice_stat_update32(struct ice_hw *hw, u32 reg, bool prev_stat_loaded, u64 *prev_stat, u64 *cur_stat)

    read 32 bit stat from the chip and update stat values

    :param hw:
        ptr to the hardware info
    :type hw: struct ice_hw \*

    :param reg:
        HW register to read from
    :type reg: u32

    :param prev_stat_loaded:
        bool to specify if previous stats are loaded
    :type prev_stat_loaded: bool

    :param prev_stat:
        ptr to previous loaded stat value
    :type prev_stat: u64 \*

    :param cur_stat:
        ptr to current stat value
    :type cur_stat: u64 \*

.. This file was automatic generated / don't edit.

