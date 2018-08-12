.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_adminq_cmd.h

.. _`ice_aq_desc`:

struct ice_aq_desc
==================

.. c:type:: struct ice_aq_desc

    Admin Queue (AQ) descriptor

.. _`ice_aq_desc.definition`:

Definition
----------

.. code-block:: c

    struct ice_aq_desc {
        __le16 flags;
        __le16 opcode;
        __le16 datalen;
        __le16 retval;
        __le32 cookie_high;
        __le32 cookie_low;
        union {
            u8 raw[16];
            struct ice_aqc_generic generic;
            struct ice_aqc_get_ver get_ver;
            struct ice_aqc_q_shutdown q_shutdown;
            struct ice_aqc_req_res res_owner;
            struct ice_aqc_manage_mac_read mac_read;
            struct ice_aqc_manage_mac_write mac_write;
            struct ice_aqc_clear_pxe clear_pxe;
            struct ice_aqc_list_caps get_cap;
            struct ice_aqc_get_phy_caps get_phy;
            struct ice_aqc_set_phy_cfg set_phy;
            struct ice_aqc_restart_an restart_an;
            struct ice_aqc_get_sw_cfg get_sw_conf;
            struct ice_aqc_sw_rules sw_rules;
            struct ice_aqc_get_topo get_topo;
            struct ice_aqc_get_cfg_elem get_update_elem;
            struct ice_aqc_query_txsched_res query_sched_res;
            struct ice_aqc_add_move_delete_elem add_move_delete_elem;
            struct ice_aqc_nvm nvm;
            struct ice_aqc_get_set_rss_lut get_set_rss_lut;
            struct ice_aqc_get_set_rss_key get_set_rss_key;
            struct ice_aqc_add_txqs add_txqs;
            struct ice_aqc_dis_txqs dis_txqs;
            struct ice_aqc_add_get_update_free_vsi vsi_cmd;
            struct ice_aqc_alloc_free_res_cmd sw_res_ctrl;
            struct ice_aqc_set_event_mask set_event_mask;
            struct ice_aqc_get_link_status get_link_status;
        } params;
    }

.. _`ice_aq_desc.members`:

Members
-------

flags
    ICE_AQ_FLAG\_\* flags

opcode
    AQ command opcode

datalen
    length in bytes of indirect/external data buffer

retval
    return value from firmware

cookie_high
    *undescribed*

cookie_low
    *undescribed*

params
    command-specific parameters

.. _`ice_aq_desc.description`:

Description
-----------

Descriptor format for commands the driver posts on the Admin Transmit Queue
(ATQ).  The firmware writes back onto the command descriptor and returns
the result of the command.  Asynchronous events that are not an immediate
result of the command are written to the Admin Receive Queue (ARQ) using
the same descriptor format.  Descriptors are in little-endian notation with
32-bit words.

.. This file was automatic generated / don't edit.

