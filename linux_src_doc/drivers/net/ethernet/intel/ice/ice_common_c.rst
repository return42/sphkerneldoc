.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_common.c

.. _`ice_set_mac_type`:

ice_set_mac_type
================

.. c:function:: enum ice_status ice_set_mac_type(struct ice_hw *hw)

    Sets MAC type

    :param struct ice_hw \*hw:
        pointer to the HW structure

.. _`ice_set_mac_type.description`:

Description
-----------

This function sets the MAC type of the adapter based on the
vendor ID and device ID stored in the hw structure.

.. _`ice_clear_pf_cfg`:

ice_clear_pf_cfg
================

.. c:function:: enum ice_status ice_clear_pf_cfg(struct ice_hw *hw)

    Clear PF configuration

    :param struct ice_hw \*hw:
        pointer to the hardware structure

.. _`ice_aq_manage_mac_read`:

ice_aq_manage_mac_read
======================

.. c:function:: enum ice_status ice_aq_manage_mac_read(struct ice_hw *hw, void *buf, u16 buf_size, struct ice_sq_cd *cd)

    manage MAC address read command

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param void \*buf:
        a virtual buffer to hold the manage MAC read response

    :param u16 buf_size:
        Size of the virtual buffer

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

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

    :param struct ice_port_info \*pi:
        port information structure

    :param bool qual_mods:
        report qualified modules

    :param u8 report_mode:
        report mode capabilities

    :param struct ice_aqc_get_phy_caps_data \*pcaps:
        structure for PHY capabilities to be filled

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_get_phy_caps.description`:

Description
-----------

Returns the various PHY capabilities supported on the Port (0x0600)

.. _`ice_get_media_type`:

ice_get_media_type
==================

.. c:function:: enum ice_media_type ice_get_media_type(struct ice_port_info *pi)

    Gets media type

    :param struct ice_port_info \*pi:
        port information structure

.. _`ice_aq_get_link_info`:

ice_aq_get_link_info
====================

.. c:function:: enum ice_status ice_aq_get_link_info(struct ice_port_info *pi, bool ena_lse, struct ice_link_status *link, struct ice_sq_cd *cd)

    :param struct ice_port_info \*pi:
        port information structure

    :param bool ena_lse:
        enable/disable LinkStatusEvent reporting

    :param struct ice_link_status \*link:
        pointer to link status structure - optional

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_get_link_info.description`:

Description
-----------

Get Link Status (0x607). Returns the link status of the adapter.

.. _`ice_init_flex_parser`:

ice_init_flex_parser
====================

.. c:function:: void ice_init_flex_parser(struct ice_hw *hw)

    initialize rx flex parser

    :param struct ice_hw \*hw:
        pointer to the hardware structure

.. _`ice_init_flex_parser.description`:

Description
-----------

Function to initialize flex descriptors

.. _`ice_init_fltr_mgmt_struct`:

ice_init_fltr_mgmt_struct
=========================

.. c:function:: enum ice_status ice_init_fltr_mgmt_struct(struct ice_hw *hw)

    initializes filter management list and locks

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_cleanup_fltr_mgmt_struct`:

ice_cleanup_fltr_mgmt_struct
============================

.. c:function:: void ice_cleanup_fltr_mgmt_struct(struct ice_hw *hw)

    cleanup filter management list and locks

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_init_hw`:

ice_init_hw
===========

.. c:function:: enum ice_status ice_init_hw(struct ice_hw *hw)

    main hardware initialization routine

    :param struct ice_hw \*hw:
        pointer to the hardware structure

.. _`ice_deinit_hw`:

ice_deinit_hw
=============

.. c:function:: void ice_deinit_hw(struct ice_hw *hw)

    unroll initialization operations done by ice_init_hw

    :param struct ice_hw \*hw:
        pointer to the hardware structure

.. _`ice_check_reset`:

ice_check_reset
===============

.. c:function:: enum ice_status ice_check_reset(struct ice_hw *hw)

    Check to see if a global reset is complete

    :param struct ice_hw \*hw:
        pointer to the hardware structure

.. _`ice_pf_reset`:

ice_pf_reset
============

.. c:function:: enum ice_status ice_pf_reset(struct ice_hw *hw)

    Reset the PF

    :param struct ice_hw \*hw:
        pointer to the hardware structure

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

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param enum ice_reset_req req:
        reset request

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

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u8 \*ice_rxq_ctx:
        pointer to the rxq context

    :param u32 rxq_index:
        the index of the rx queue

.. _`ice_copy_rxq_ctx_to_hw.description`:

Description
-----------

Copies rxq context from dense structure to hw register space

.. _`ice_write_rxq_ctx`:

ice_write_rxq_ctx
=================

.. c:function:: enum ice_status ice_write_rxq_ctx(struct ice_hw *hw, struct ice_rlan_ctx *rlan_ctx, u32 rxq_index)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param struct ice_rlan_ctx \*rlan_ctx:
        pointer to the rxq context

    :param u32 rxq_index:
        the index of the rx queue

.. _`ice_write_rxq_ctx.description`:

Description
-----------

Converts rxq context from sparse to dense structure and then writes
it to hw register space

.. _`ice_debug_cq`:

ice_debug_cq
============

.. c:function:: void ice_debug_cq(struct ice_hw *hw, u32 __maybe_unused mask, void *desc, void *buf, u16 buf_len)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u32 __maybe_unused mask:
        debug mask

    :param void \*desc:
        pointer to control queue descriptor

    :param void \*buf:
        pointer to command buffer

    :param u16 buf_len:
        max length of buf

.. _`ice_debug_cq.description`:

Description
-----------

Dumps debug log about control command with descriptor contents.

.. _`ice_aq_send_cmd`:

ice_aq_send_cmd
===============

.. c:function:: enum ice_status ice_aq_send_cmd(struct ice_hw *hw, struct ice_aq_desc *desc, void *buf, u16 buf_size, struct ice_sq_cd *cd)

    send FW Admin Queue command to FW Admin Queue

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_aq_desc \*desc:
        descriptor describing the command

    :param void \*buf:
        buffer to use for indirect commands (NULL for direct commands)

    :param u16 buf_size:
        size of buffer for indirect commands (0 for direct commands)

    :param struct ice_sq_cd \*cd:
        pointer to command details structure

.. _`ice_aq_send_cmd.description`:

Description
-----------

Helper function to send FW Admin Queue commands to the FW Admin Queue.

.. _`ice_aq_get_fw_ver`:

ice_aq_get_fw_ver
=================

.. c:function:: enum ice_status ice_aq_get_fw_ver(struct ice_hw *hw, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_get_fw_ver.description`:

Description
-----------

Get the firmware version (0x0001) from the admin queue commands

.. _`ice_aq_q_shutdown`:

ice_aq_q_shutdown
=================

.. c:function:: enum ice_status ice_aq_q_shutdown(struct ice_hw *hw, bool unloading)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param bool unloading:
        is the driver unloading itself

.. _`ice_aq_q_shutdown.description`:

Description
-----------

Tell the Firmware that we're shutting down the AdminQ and whether
or not the driver is unloading as well (0x0003).

.. _`ice_aq_req_res`:

ice_aq_req_res
==============

.. c:function:: enum ice_status ice_aq_req_res(struct ice_hw *hw, enum ice_aq_res_ids res, enum ice_aq_res_access_type access, u8 sdp_number, u32 *timeout, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param enum ice_aq_res_ids res:
        resource id

    :param enum ice_aq_res_access_type access:
        access type

    :param u8 sdp_number:
        resource number

    :param u32 \*timeout:
        the maximum time in ms that the driver may hold the resource

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_req_res.description`:

Description
-----------

requests common resource using the admin queue commands (0x0008)

.. _`ice_aq_release_res`:

ice_aq_release_res
==================

.. c:function:: enum ice_status ice_aq_release_res(struct ice_hw *hw, enum ice_aq_res_ids res, u8 sdp_number, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param enum ice_aq_res_ids res:
        resource id

    :param u8 sdp_number:
        resource number

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_release_res.description`:

Description
-----------

release common resource using the admin queue commands (0x0009)

.. _`ice_acquire_res`:

ice_acquire_res
===============

.. c:function:: enum ice_status ice_acquire_res(struct ice_hw *hw, enum ice_aq_res_ids res, enum ice_aq_res_access_type access)

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param enum ice_aq_res_ids res:
        resource id

    :param enum ice_aq_res_access_type access:
        access type (read or write)

.. _`ice_acquire_res.description`:

Description
-----------

This function will attempt to acquire the ownership of a resource.

.. _`ice_release_res`:

ice_release_res
===============

.. c:function:: void ice_release_res(struct ice_hw *hw, enum ice_aq_res_ids res)

    :param struct ice_hw \*hw:
        pointer to the HW structure

    :param enum ice_aq_res_ids res:
        resource id

.. _`ice_release_res.description`:

Description
-----------

This function will release a resource using the proper Admin Command.

.. _`ice_parse_caps`:

ice_parse_caps
==============

.. c:function:: void ice_parse_caps(struct ice_hw *hw, void *buf, u32 cap_count, enum ice_adminq_opc opc)

    parse function/device capabilities

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param void \*buf:
        pointer to a buffer containing function/device capability records

    :param u32 cap_count:
        number of capability records in the list

    :param enum ice_adminq_opc opc:
        type of capabilities list to parse

.. _`ice_parse_caps.description`:

Description
-----------

Helper function to parse function(0x000a)/device(0x000b) capabilities list.

.. _`ice_aq_discover_caps`:

ice_aq_discover_caps
====================

.. c:function:: enum ice_status ice_aq_discover_caps(struct ice_hw *hw, void *buf, u16 buf_size, u16 *data_size, enum ice_adminq_opc opc, struct ice_sq_cd *cd)

    query function/device capabilities

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param void \*buf:
        a virtual buffer to hold the capabilities

    :param u16 buf_size:
        Size of the virtual buffer

    :param u16 \*data_size:
        Size of the returned data, or buf size needed if AQ err==ENOMEM

    :param enum ice_adminq_opc opc:
        capabilities type to discover - pass in the command opcode

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_discover_caps.description`:

Description
-----------

Get the function(0x000a)/device(0x000b) capabilities description from
the firmware.

.. _`ice_get_caps`:

ice_get_caps
============

.. c:function:: enum ice_status ice_get_caps(struct ice_hw *hw)

    get info about the HW

    :param struct ice_hw \*hw:
        pointer to the hardware structure

.. _`ice_aq_manage_mac_write`:

ice_aq_manage_mac_write
=======================

.. c:function:: enum ice_status ice_aq_manage_mac_write(struct ice_hw *hw, u8 *mac_addr, u8 flags, struct ice_sq_cd *cd)

    manage MAC address write command

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u8 \*mac_addr:
        MAC address to be written as LAA/LAA+WoL/Port address

    :param u8 flags:
        flags to control write behavior

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_manage_mac_write.description`:

Description
-----------

This function is used to write MAC address to the NVM (0x0108).

.. _`ice_aq_clear_pxe_mode`:

ice_aq_clear_pxe_mode
=====================

.. c:function:: enum ice_status ice_aq_clear_pxe_mode(struct ice_hw *hw)

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_aq_clear_pxe_mode.description`:

Description
-----------

Tell the firmware that the driver is taking over from PXE (0x0110).

.. _`ice_clear_pxe_mode`:

ice_clear_pxe_mode
==================

.. c:function:: void ice_clear_pxe_mode(struct ice_hw *hw)

    clear pxe operations mode

    :param struct ice_hw \*hw:
        pointer to the hw struct

.. _`ice_clear_pxe_mode.description`:

Description
-----------

Make sure all PXE mode settings are cleared, including things
like descriptor fetch/write-back mode.

.. _`ice_aq_set_phy_cfg`:

ice_aq_set_phy_cfg
==================

.. c:function:: enum ice_status ice_aq_set_phy_cfg(struct ice_hw *hw, u8 lport, struct ice_aqc_set_phy_cfg_data *cfg, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u8 lport:
        logical port number

    :param struct ice_aqc_set_phy_cfg_data \*cfg:
        structure with PHY configuration data to be set

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

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

    :param struct ice_port_info \*pi:
        port info structure of the interested logical port

.. _`ice_set_fc`:

ice_set_fc
==========

.. c:function:: enum ice_status ice_set_fc(struct ice_port_info *pi, u8 *aq_failures, bool atomic_restart)

    :param struct ice_port_info \*pi:
        port information structure

    :param u8 \*aq_failures:
        pointer to status code, specific to ice_set_fc routine

    :param bool atomic_restart:
        enable automatic link update

.. _`ice_set_fc.description`:

Description
-----------

Set the requested flow control mode.

.. _`ice_get_link_status`:

ice_get_link_status
===================

.. c:function:: enum ice_status ice_get_link_status(struct ice_port_info *pi, bool *link_up)

    get status of the HW network link

    :param struct ice_port_info \*pi:
        port information structure

    :param bool \*link_up:
        pointer to bool (true/false = linkup/linkdown)

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

    :param struct ice_port_info \*pi:
        pointer to the port information structure

    :param bool ena_link:
        if true: enable link, if false: disable link

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_set_link_restart_an.description`:

Description
-----------

Sets up the link and restarts the Auto-Negotiation over the link.

.. _`ice_aq_set_event_mask`:

ice_aq_set_event_mask
=====================

.. c:function:: enum ice_status ice_aq_set_event_mask(struct ice_hw *hw, u8 port_num, u16 mask, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u8 port_num:
        port number of the physical function

    :param u16 mask:
        event mask to be set

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_set_event_mask.description`:

Description
-----------

Set event mask (0x0613)

.. _`__ice_aq_get_set_rss_lut`:

\__ice_aq_get_set_rss_lut
=========================

.. c:function:: enum ice_status __ice_aq_get_set_rss_lut(struct ice_hw *hw, u16 vsi_id, u8 lut_type, u8 *lut, u16 lut_size, u8 glob_lut_idx, bool set)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        VSI FW index

    :param u8 lut_type:
        LUT table type

    :param u8 \*lut:
        pointer to the LUT buffer provided by the caller

    :param u16 lut_size:
        size of the LUT buffer

    :param u8 glob_lut_idx:
        global LUT index

    :param bool set:
        set true to set the table, false to get the table

.. _`__ice_aq_get_set_rss_lut.description`:

Description
-----------

Internal function to get (0x0B05) or set (0x0B03) RSS look up table

.. _`ice_aq_get_rss_lut`:

ice_aq_get_rss_lut
==================

.. c:function:: enum ice_status ice_aq_get_rss_lut(struct ice_hw *hw, u16 vsi_id, u8 lut_type, u8 *lut, u16 lut_size)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        VSI FW index

    :param u8 lut_type:
        LUT table type

    :param u8 \*lut:
        pointer to the LUT buffer provided by the caller

    :param u16 lut_size:
        size of the LUT buffer

.. _`ice_aq_get_rss_lut.description`:

Description
-----------

get the RSS lookup table, PF or VSI type

.. _`ice_aq_set_rss_lut`:

ice_aq_set_rss_lut
==================

.. c:function:: enum ice_status ice_aq_set_rss_lut(struct ice_hw *hw, u16 vsi_id, u8 lut_type, u8 *lut, u16 lut_size)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        VSI FW index

    :param u8 lut_type:
        LUT table type

    :param u8 \*lut:
        pointer to the LUT buffer provided by the caller

    :param u16 lut_size:
        size of the LUT buffer

.. _`ice_aq_set_rss_lut.description`:

Description
-----------

set the RSS lookup table, PF or VSI type

.. _`__ice_aq_get_set_rss_key`:

\__ice_aq_get_set_rss_key
=========================

.. c:function:: enum ice_status __ice_aq_get_set_rss_key(struct ice_hw *hw, u16 vsi_id, struct ice_aqc_get_set_rss_keys *key, bool set)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 vsi_id:
        VSI FW index

    :param struct ice_aqc_get_set_rss_keys \*key:
        pointer to key info struct

    :param bool set:
        set true to set the key, false to get the key

.. _`__ice_aq_get_set_rss_key.description`:

Description
-----------

get (0x0B04) or set (0x0B02) the RSS key per VSI

.. _`ice_aq_get_rss_key`:

ice_aq_get_rss_key
==================

.. c:function:: enum ice_status ice_aq_get_rss_key(struct ice_hw *hw, u16 vsi_id, struct ice_aqc_get_set_rss_keys *key)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 vsi_id:
        VSI FW index

    :param struct ice_aqc_get_set_rss_keys \*key:
        pointer to key info struct

.. _`ice_aq_get_rss_key.description`:

Description
-----------

get the RSS key per VSI

.. _`ice_aq_set_rss_key`:

ice_aq_set_rss_key
==================

.. c:function:: enum ice_status ice_aq_set_rss_key(struct ice_hw *hw, u16 vsi_id, struct ice_aqc_get_set_rss_keys *keys)

    :param struct ice_hw \*hw:
        pointer to the hw struct

    :param u16 vsi_id:
        VSI FW index

    :param struct ice_aqc_get_set_rss_keys \*keys:
        pointer to key info struct

.. _`ice_aq_set_rss_key.description`:

Description
-----------

set the RSS key per VSI

.. _`ice_aq_add_lan_txq`:

ice_aq_add_lan_txq
==================

.. c:function:: enum ice_status ice_aq_add_lan_txq(struct ice_hw *hw, u8 num_qgrps, struct ice_aqc_add_tx_qgrp *qg_list, u16 buf_size, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u8 num_qgrps:
        Number of added queue groups

    :param struct ice_aqc_add_tx_qgrp \*qg_list:
        list of queue groups to be added

    :param u16 buf_size:
        size of buffer for indirect command

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

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

.. c:function:: enum ice_status ice_aq_dis_lan_txq(struct ice_hw *hw, u8 num_qgrps, struct ice_aqc_dis_txq_item *qg_list, u16 buf_size, struct ice_sq_cd *cd)

    :param struct ice_hw \*hw:
        pointer to the hardware structure

    :param u8 num_qgrps:
        number of groups in the list

    :param struct ice_aqc_dis_txq_item \*qg_list:
        the list of groups to disable

    :param u16 buf_size:
        the total size of the qg_list buffer in bytes

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_aq_dis_lan_txq.description`:

Description
-----------

Disable LAN Tx queue (0x0C31)

.. _`ice_write_byte`:

ice_write_byte
==============

.. c:function:: void ice_write_byte(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a byte to a packed context structure

    :param u8 \*src_ctx:
        the context structure to read from

    :param u8 \*dest_ctx:
        the context to be written to

    :param const struct ice_ctx_ele \*ce_info:
        a description of the struct to be filled

.. _`ice_write_word`:

ice_write_word
==============

.. c:function:: void ice_write_word(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a word to a packed context structure

    :param u8 \*src_ctx:
        the context structure to read from

    :param u8 \*dest_ctx:
        the context to be written to

    :param const struct ice_ctx_ele \*ce_info:
        a description of the struct to be filled

.. _`ice_write_dword`:

ice_write_dword
===============

.. c:function:: void ice_write_dword(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a dword to a packed context structure

    :param u8 \*src_ctx:
        the context structure to read from

    :param u8 \*dest_ctx:
        the context to be written to

    :param const struct ice_ctx_ele \*ce_info:
        a description of the struct to be filled

.. _`ice_write_qword`:

ice_write_qword
===============

.. c:function:: void ice_write_qword(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    write a qword to a packed context structure

    :param u8 \*src_ctx:
        the context structure to read from

    :param u8 \*dest_ctx:
        the context to be written to

    :param const struct ice_ctx_ele \*ce_info:
        a description of the struct to be filled

.. _`ice_set_ctx`:

ice_set_ctx
===========

.. c:function:: enum ice_status ice_set_ctx(u8 *src_ctx, u8 *dest_ctx, const struct ice_ctx_ele *ce_info)

    set context bits in packed structure

    :param u8 \*src_ctx:
        pointer to a generic non-packed context structure

    :param u8 \*dest_ctx:
        pointer to memory for the packed structure

    :param const struct ice_ctx_ele \*ce_info:
        a description of the structure to be transformed

.. _`ice_ena_vsi_txq`:

ice_ena_vsi_txq
===============

.. c:function:: enum ice_status ice_ena_vsi_txq(struct ice_port_info *pi, u16 vsi_id, u8 tc, u8 num_qgrps, struct ice_aqc_add_tx_qgrp *buf, u16 buf_size, struct ice_sq_cd *cd)

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI id

    :param u8 tc:
        tc number

    :param u8 num_qgrps:
        Number of added queue groups

    :param struct ice_aqc_add_tx_qgrp \*buf:
        list of queue groups to be added

    :param u16 buf_size:
        size of buffer for indirect command

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_ena_vsi_txq.description`:

Description
-----------

This function adds one lan q

.. _`ice_dis_vsi_txq`:

ice_dis_vsi_txq
===============

.. c:function:: enum ice_status ice_dis_vsi_txq(struct ice_port_info *pi, u8 num_queues, u16 *q_ids, u32 *q_teids, struct ice_sq_cd *cd)

    :param struct ice_port_info \*pi:
        port information structure

    :param u8 num_queues:
        number of queues

    :param u16 \*q_ids:
        pointer to the q_id array

    :param u32 \*q_teids:
        pointer to queue node teids

    :param struct ice_sq_cd \*cd:
        pointer to command details structure or NULL

.. _`ice_dis_vsi_txq.description`:

Description
-----------

This function removes queues and their corresponding nodes in SW DB

.. _`ice_cfg_vsi_qs`:

ice_cfg_vsi_qs
==============

.. c:function:: enum ice_status ice_cfg_vsi_qs(struct ice_port_info *pi, u16 vsi_id, u8 tc_bitmap, u16 *maxqs, u8 owner)

    configure the new/exisiting VSI queues

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

    :param u8 tc_bitmap:
        TC bitmap

    :param u16 \*maxqs:
        max queues array per TC

    :param u8 owner:
        lan or rdma

.. _`ice_cfg_vsi_qs.description`:

Description
-----------

This function adds/updates the VSI queues per TC.

.. _`ice_cfg_vsi_lan`:

ice_cfg_vsi_lan
===============

.. c:function:: enum ice_status ice_cfg_vsi_lan(struct ice_port_info *pi, u16 vsi_id, u8 tc_bitmap, u16 *max_lanqs)

    configure VSI lan queues

    :param struct ice_port_info \*pi:
        port information structure

    :param u16 vsi_id:
        VSI Id

    :param u8 tc_bitmap:
        TC bitmap

    :param u16 \*max_lanqs:
        max lan queues array per TC

.. _`ice_cfg_vsi_lan.description`:

Description
-----------

This function adds/updates the VSI lan queues per TC.

.. This file was automatic generated / don't edit.

