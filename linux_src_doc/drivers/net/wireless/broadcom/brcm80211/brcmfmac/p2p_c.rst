.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/p2p.c

.. _`brcmf_p2p_disc_st_le`:

struct brcmf_p2p_disc_st_le
===========================

.. c:type:: struct brcmf_p2p_disc_st_le

    set discovery state in firmware.

.. _`brcmf_p2p_disc_st_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_p2p_disc_st_le {
        u8 state;
        __le16 chspec;
        __le16 dwell;
    }

.. _`brcmf_p2p_disc_st_le.members`:

Members
-------

state
    requested discovery state (see enum brcmf_p2p_disc_state).

chspec
    channel parameter for \ ``WL_P2P_DISC_ST_LISTEN``\  state.

dwell
    dwell time in ms for \ ``WL_P2P_DISC_ST_LISTEN``\  state.

.. _`brcmf_p2p_disc_state`:

enum brcmf_p2p_disc_state
=========================

.. c:type:: enum brcmf_p2p_disc_state

    P2P discovery state values

.. _`brcmf_p2p_disc_state.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_p2p_disc_state {
        WL_P2P_DISC_ST_SCAN,
        WL_P2P_DISC_ST_LISTEN,
        WL_P2P_DISC_ST_SEARCH
    };

.. _`brcmf_p2p_disc_state.constants`:

Constants
---------

WL_P2P_DISC_ST_SCAN
    P2P discovery with wildcard SSID and P2P IE.

WL_P2P_DISC_ST_LISTEN
    P2P discovery off-channel for specified time.

WL_P2P_DISC_ST_SEARCH
    P2P discovery with P2P wildcard SSID and P2P IE.

.. _`brcmf_p2p_scan_le`:

struct brcmf_p2p_scan_le
========================

.. c:type:: struct brcmf_p2p_scan_le

    P2P specific scan request.

.. _`brcmf_p2p_scan_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_p2p_scan_le {
        u8 type;
        u8 reserved[3];
        union {
            struct brcmf_escan_params_le eparams;
            struct brcmf_scan_params_le sparams;
        } ;
    }

.. _`brcmf_p2p_scan_le.members`:

Members
-------

type
    type of scan method requested (values: 'E' or 'S').

reserved
    reserved (ignored).

{unnamed_union}
    anonymous

eparams
    parameters used for type 'E'.

sparams
    parameters used for type 'S'.

.. _`brcmf_p2p_pub_act_frame`:

struct brcmf_p2p_pub_act_frame
==============================

.. c:type:: struct brcmf_p2p_pub_act_frame

    WiFi P2P Public Action Frame

.. _`brcmf_p2p_pub_act_frame.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_p2p_pub_act_frame {
        u8 category;
        u8 action;
        u8 oui[3];
        u8 oui_type;
        u8 subtype;
        u8 dialog_token;
        u8 elts[1];
    }

.. _`brcmf_p2p_pub_act_frame.members`:

Members
-------

category
    P2P_PUB_AF_CATEGORY

action
    P2P_PUB_AF_ACTION

oui
    P2P_OUI

oui_type
    OUI type - P2P_VER

subtype
    OUI subtype - P2P_TYPE\_\*

dialog_token
    nonzero, identifies req/rsp transaction

elts
    Variable length information elements.

.. _`brcmf_p2p_action_frame`:

struct brcmf_p2p_action_frame
=============================

.. c:type:: struct brcmf_p2p_action_frame

    WiFi P2P Action Frame

.. _`brcmf_p2p_action_frame.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_p2p_action_frame {
        u8 category;
        u8 oui[3];
        u8 type;
        u8 subtype;
        u8 dialog_token;
        u8 elts[1];
    }

.. _`brcmf_p2p_action_frame.members`:

Members
-------

category
    P2P_AF_CATEGORY

oui
    *undescribed*

type
    OUI Type - P2P_VER

subtype
    OUI Subtype - P2P_AF\_\*

dialog_token
    nonzero, identifies req/resp tranaction

elts
    Variable length information elements.

.. _`brcmf_p2psd_gas_pub_act_frame`:

struct brcmf_p2psd_gas_pub_act_frame
====================================

.. c:type:: struct brcmf_p2psd_gas_pub_act_frame

    Wi-Fi GAS Public Action Frame

.. _`brcmf_p2psd_gas_pub_act_frame.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_p2psd_gas_pub_act_frame {
        u8 category;
        u8 action;
        u8 dialog_token;
        u8 query_data[1];
    }

.. _`brcmf_p2psd_gas_pub_act_frame.members`:

Members
-------

category
    0x04 Public Action Frame

action
    0x6c Advertisement Protocol

dialog_token
    nonzero, identifies req/rsp transaction

query_data
    Query Data. SD gas ireq SD gas iresp

.. _`brcmf_config_af_params`:

struct brcmf_config_af_params
=============================

.. c:type:: struct brcmf_config_af_params

    Action Frame Parameters for tx.

.. _`brcmf_config_af_params.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_config_af_params {
        s32 mpc_onoff;
        bool search_channel;
        bool extra_listen;
    }

.. _`brcmf_config_af_params.members`:

Members
-------

mpc_onoff
    To make sure to send successfully action frame, we have to
    turn off mpc  0: off, 1: on,  (-1): do nothing

search_channel
    1: search peer's channel to send af

extra_listen
    *undescribed*

.. _`brcmf_config_af_params.extra_listen`:

extra_listen
------------

keep the dwell time to get af response frame.

.. _`brcmf_p2p_is_pub_action`:

brcmf_p2p_is_pub_action
=======================

.. c:function:: bool brcmf_p2p_is_pub_action(void *frame, u32 frame_len)

    true if p2p public type frame.

    :param frame:
        action frame data.
    :type frame: void \*

    :param frame_len:
        length of action frame data.
    :type frame_len: u32

.. _`brcmf_p2p_is_pub_action.description`:

Description
-----------

Determine if action frame is p2p public action type

.. _`brcmf_p2p_is_p2p_action`:

brcmf_p2p_is_p2p_action
=======================

.. c:function:: bool brcmf_p2p_is_p2p_action(void *frame, u32 frame_len)

    true if p2p action type frame.

    :param frame:
        action frame data.
    :type frame: void \*

    :param frame_len:
        length of action frame data.
    :type frame_len: u32

.. _`brcmf_p2p_is_p2p_action.description`:

Description
-----------

Determine if action frame is p2p action type

.. _`brcmf_p2p_is_gas_action`:

brcmf_p2p_is_gas_action
=======================

.. c:function:: bool brcmf_p2p_is_gas_action(void *frame, u32 frame_len)

    true if p2p gas action type frame.

    :param frame:
        action frame data.
    :type frame: void \*

    :param frame_len:
        length of action frame data.
    :type frame_len: u32

.. _`brcmf_p2p_is_gas_action.description`:

Description
-----------

Determine if action frame is p2p gas action type

.. _`brcmf_p2p_print_actframe`:

brcmf_p2p_print_actframe
========================

.. c:function:: void brcmf_p2p_print_actframe(bool tx, void *frame, u32 frame_len)

    debug print routine.

    :param tx:
        Received or to be transmitted
    :type tx: bool

    :param frame:
        action frame data.
    :type frame: void \*

    :param frame_len:
        length of action frame data.
    :type frame_len: u32

.. _`brcmf_p2p_print_actframe.description`:

Description
-----------

Print information about the p2p action frame

.. _`brcmf_p2p_set_firmware`:

brcmf_p2p_set_firmware
======================

.. c:function:: int brcmf_p2p_set_firmware(struct brcmf_if *ifp, u8 *p2p_mac)

    prepare firmware for peer-to-peer operation.

    :param ifp:
        ifp to use for iovars (primary).
    :type ifp: struct brcmf_if \*

    :param p2p_mac:
        mac address to configure for p2p_da_override
    :type p2p_mac: u8 \*

.. _`brcmf_p2p_generate_bss_mac`:

brcmf_p2p_generate_bss_mac
==========================

.. c:function:: void brcmf_p2p_generate_bss_mac(struct brcmf_p2p_info *p2p, u8 *dev_addr)

    derive mac addresses for P2P.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

    :param dev_addr:
        optional device address.
    :type dev_addr: u8 \*

.. _`brcmf_p2p_generate_bss_mac.description`:

Description
-----------

P2P needs mac addresses for P2P device and interface. If no device
address it specified, these are derived from a random ethernet
address.

.. _`brcmf_p2p_scan_is_p2p_request`:

brcmf_p2p_scan_is_p2p_request
=============================

.. c:function:: bool brcmf_p2p_scan_is_p2p_request(struct cfg80211_scan_request *request)

    is cfg80211 scan request a P2P scan.

    :param request:
        the scan request as received from cfg80211.
    :type request: struct cfg80211_scan_request \*

.. _`brcmf_p2p_scan_is_p2p_request.description`:

Description
-----------

returns true if one of the ssids in the request matches the
P2P wildcard ssid; otherwise returns false.

.. _`brcmf_p2p_set_discover_state`:

brcmf_p2p_set_discover_state
============================

.. c:function:: s32 brcmf_p2p_set_discover_state(struct brcmf_if *ifp, u8 state, u16 chanspec, u16 listen_ms)

    set discover state in firmware.

    :param ifp:
        low-level interface object.
    :type ifp: struct brcmf_if \*

    :param state:
        discover state to set.
    :type state: u8

    :param chanspec:
        channel parameters (for state \ ``WL_P2P_DISC_ST_LISTEN``\  only).
    :type chanspec: u16

    :param listen_ms:
        duration to listen (for state \ ``WL_P2P_DISC_ST_LISTEN``\  only).
    :type listen_ms: u16

.. _`brcmf_p2p_deinit_discovery`:

brcmf_p2p_deinit_discovery
==========================

.. c:function:: s32 brcmf_p2p_deinit_discovery(struct brcmf_p2p_info *p2p)

    disable P2P device discovery.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

.. _`brcmf_p2p_deinit_discovery.description`:

Description
-----------

Resets the discovery state and disables it in firmware.

.. _`brcmf_p2p_enable_discovery`:

brcmf_p2p_enable_discovery
==========================

.. c:function:: int brcmf_p2p_enable_discovery(struct brcmf_p2p_info *p2p)

    initialize and configure discovery.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

.. _`brcmf_p2p_enable_discovery.description`:

Description
-----------

Initializes the discovery device and configure the virtual interface.

.. _`brcmf_p2p_escan`:

brcmf_p2p_escan
===============

.. c:function:: s32 brcmf_p2p_escan(struct brcmf_p2p_info *p2p, u32 num_chans, u16 chanspecs, s32 search_state, enum p2p_bss_type bss_type)

    initiate a P2P scan.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

    :param num_chans:
        number of channels to scan.
    :type num_chans: u32

    :param chanspecs:
        channel parameters for \ ``num_chans``\  channels.
    :type chanspecs: u16

    :param search_state:
        P2P discover state to use.
    :type search_state: s32

    :param bss_type:
        type of P2P bss.
    :type bss_type: enum p2p_bss_type

.. _`brcmf_p2p_run_escan`:

brcmf_p2p_run_escan
===================

.. c:function:: s32 brcmf_p2p_run_escan(struct brcmf_cfg80211_info *cfg, struct brcmf_if *ifp, struct cfg80211_scan_request *request)

    escan callback for peer-to-peer.

    :param cfg:
        driver private data for cfg80211 interface.
    :type cfg: struct brcmf_cfg80211_info \*

    :param ifp:
        *undescribed*
    :type ifp: struct brcmf_if \*

    :param request:
        scan request from cfg80211.
    :type request: struct cfg80211_scan_request \*

.. _`brcmf_p2p_run_escan.description`:

Description
-----------

Determines the P2P discovery state based to scan request parameters and
validates the channels in the request.

.. _`brcmf_p2p_find_listen_channel`:

brcmf_p2p_find_listen_channel
=============================

.. c:function:: s32 brcmf_p2p_find_listen_channel(const u8 *ie, u32 ie_len)

    find listen channel in ie string.

    :param ie:
        string of information elements.
    :type ie: const u8 \*

    :param ie_len:
        length of string.
    :type ie_len: u32

.. _`brcmf_p2p_find_listen_channel.description`:

Description
-----------

Scan ie for p2p ie and look for attribute 6 channel. If available determine
channel and return it.

.. _`brcmf_p2p_scan_prep`:

brcmf_p2p_scan_prep
===================

.. c:function:: int brcmf_p2p_scan_prep(struct wiphy *wiphy, struct cfg80211_scan_request *request, struct brcmf_cfg80211_vif *vif)

    prepare scan based on request.

    :param wiphy:
        wiphy device.
    :type wiphy: struct wiphy \*

    :param request:
        scan request from cfg80211.
    :type request: struct cfg80211_scan_request \*

    :param vif:
        vif on which scan request is to be executed.
    :type vif: struct brcmf_cfg80211_vif \*

.. _`brcmf_p2p_scan_prep.description`:

Description
-----------

Prepare the scan appropriately for type of scan requested. Overrides the
escan .run() callback for peer-to-peer scanning.

.. _`brcmf_p2p_discover_listen`:

brcmf_p2p_discover_listen
=========================

.. c:function:: s32 brcmf_p2p_discover_listen(struct brcmf_p2p_info *p2p, u16 channel, u32 duration)

    set firmware to discover listen state.

    :param p2p:
        p2p device.
    :type p2p: struct brcmf_p2p_info \*

    :param channel:
        channel nr for discover listen.
    :type channel: u16

    :param duration:
        time in ms to stay on channel.
    :type duration: u32

.. _`brcmf_p2p_remain_on_channel`:

brcmf_p2p_remain_on_channel
===========================

.. c:function:: int brcmf_p2p_remain_on_channel(struct wiphy *wiphy, struct wireless_dev *wdev, struct ieee80211_channel *channel, unsigned int duration, u64 *cookie)

    put device on channel and stay there.

    :param wiphy:
        wiphy device.
    :type wiphy: struct wiphy \*

    :param wdev:
        *undescribed*
    :type wdev: struct wireless_dev \*

    :param channel:
        channel to stay on.
    :type channel: struct ieee80211_channel \*

    :param duration:
        time in ms to remain on channel.
    :type duration: unsigned int

    :param cookie:
        *undescribed*
    :type cookie: u64 \*

.. _`brcmf_p2p_notify_listen_complete`:

brcmf_p2p_notify_listen_complete
================================

.. c:function:: int brcmf_p2p_notify_listen_complete(struct brcmf_if *ifp, const struct brcmf_event_msg *e, void *data)

    p2p listen has completed.

    :param ifp:
        interfac control.
    :type ifp: struct brcmf_if \*

    :param e:
        event message. Not used, to make it usable for fweh event dispatcher.
    :type e: const struct brcmf_event_msg \*

    :param data:
        payload of message. Not used.
    :type data: void \*

.. _`brcmf_p2p_cancel_remain_on_channel`:

brcmf_p2p_cancel_remain_on_channel
==================================

.. c:function:: void brcmf_p2p_cancel_remain_on_channel(struct brcmf_if *ifp)

    cancel p2p listen state.

    :param ifp:
        interfac control.
    :type ifp: struct brcmf_if \*

.. _`brcmf_p2p_act_frm_search`:

brcmf_p2p_act_frm_search
========================

.. c:function:: s32 brcmf_p2p_act_frm_search(struct brcmf_p2p_info *p2p, u16 channel)

    search function for action frame.

    :param p2p:
        p2p device.
    :type p2p: struct brcmf_p2p_info \*

    :param channel:
        *undescribed*
    :type channel: u16

.. _`brcmf_p2p_act_frm_search.channel`:

channel
-------

channel on which action frame is to be trasmitted.

search function to reach at common channel to send action frame. When
channel is 0 then all social channels will be used to send af

.. _`brcmf_p2p_afx_handler`:

brcmf_p2p_afx_handler
=====================

.. c:function:: void brcmf_p2p_afx_handler(struct work_struct *work)

    afx worker thread.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`brcmf_p2p_af_searching_channel`:

brcmf_p2p_af_searching_channel
==============================

.. c:function:: s32 brcmf_p2p_af_searching_channel(struct brcmf_p2p_info *p2p)

    search channel.

    :param p2p:
        p2p device info struct.
    :type p2p: struct brcmf_p2p_info \*

.. _`brcmf_p2p_scan_finding_common_channel`:

brcmf_p2p_scan_finding_common_channel
=====================================

.. c:function:: bool brcmf_p2p_scan_finding_common_channel(struct brcmf_cfg80211_info *cfg, struct brcmf_bss_info_le *bi)

    was escan used for finding channel

    :param cfg:
        common configuration struct.
    :type cfg: struct brcmf_cfg80211_info \*

    :param bi:
        bss info struct, result from scan.
    :type bi: struct brcmf_bss_info_le \*

.. _`brcmf_p2p_stop_wait_next_action_frame`:

brcmf_p2p_stop_wait_next_action_frame
=====================================

.. c:function:: void brcmf_p2p_stop_wait_next_action_frame(struct brcmf_cfg80211_info *cfg)

    finish scan if af tx complete.

    :param cfg:
        common configuration struct.
    :type cfg: struct brcmf_cfg80211_info \*

.. _`brcmf_p2p_gon_req_collision`:

brcmf_p2p_gon_req_collision
===========================

.. c:function:: bool brcmf_p2p_gon_req_collision(struct brcmf_p2p_info *p2p, u8 *mac)

    Check if go negotiaton collission

    :param p2p:
        p2p device info struct.
    :type p2p: struct brcmf_p2p_info \*

    :param mac:
        *undescribed*
    :type mac: u8 \*

.. _`brcmf_p2p_gon_req_collision.description`:

Description
-----------

return true if recevied action frame is to be dropped.

.. _`brcmf_p2p_notify_action_frame_rx`:

brcmf_p2p_notify_action_frame_rx
================================

.. c:function:: int brcmf_p2p_notify_action_frame_rx(struct brcmf_if *ifp, const struct brcmf_event_msg *e, void *data)

    received action frame.

    :param ifp:
        interfac control.
    :type ifp: struct brcmf_if \*

    :param e:
        event message. Not used, to make it usable for fweh event dispatcher.
    :type e: const struct brcmf_event_msg \*

    :param data:
        payload of message, containing action frame data.
    :type data: void \*

.. _`brcmf_p2p_notify_action_tx_complete`:

brcmf_p2p_notify_action_tx_complete
===================================

.. c:function:: int brcmf_p2p_notify_action_tx_complete(struct brcmf_if *ifp, const struct brcmf_event_msg *e, void *data)

    transmit action frame complete

    :param ifp:
        interfac control.
    :type ifp: struct brcmf_if \*

    :param e:
        event message. Not used, to make it usable for fweh event dispatcher.
    :type e: const struct brcmf_event_msg \*

    :param data:
        not used.
    :type data: void \*

.. _`brcmf_p2p_tx_action_frame`:

brcmf_p2p_tx_action_frame
=========================

.. c:function:: s32 brcmf_p2p_tx_action_frame(struct brcmf_p2p_info *p2p, struct brcmf_fil_af_params_le *af_params)

    send action frame over fil.

    :param p2p:
        p2p info struct for vif.
    :type p2p: struct brcmf_p2p_info \*

    :param af_params:
        action frame data/info.
    :type af_params: struct brcmf_fil_af_params_le \*

.. _`brcmf_p2p_tx_action_frame.description`:

Description
-----------

Send an action frame immediately without doing channel synchronization.

This function waits for a completion event before returning.
The WLC_E_ACTION_FRAME_COMPLETE event will be received when the action
frame is transmitted.

.. _`brcmf_p2p_pub_af_tx`:

brcmf_p2p_pub_af_tx
===================

.. c:function:: s32 brcmf_p2p_pub_af_tx(struct brcmf_cfg80211_info *cfg, struct brcmf_fil_af_params_le *af_params, struct brcmf_config_af_params *config_af_params)

    public action frame tx routine.

    :param cfg:
        driver private data for cfg80211 interface.
    :type cfg: struct brcmf_cfg80211_info \*

    :param af_params:
        action frame data/info.
    :type af_params: struct brcmf_fil_af_params_le \*

    :param config_af_params:
        configuration data for action frame.
    :type config_af_params: struct brcmf_config_af_params \*

.. _`brcmf_p2p_pub_af_tx.description`:

Description
-----------

routine which transmits ation frame public type.

.. _`brcmf_p2p_send_action_frame`:

brcmf_p2p_send_action_frame
===========================

.. c:function:: bool brcmf_p2p_send_action_frame(struct brcmf_cfg80211_info *cfg, struct net_device *ndev, struct brcmf_fil_af_params_le *af_params)

    send action frame .

    :param cfg:
        driver private data for cfg80211 interface.
    :type cfg: struct brcmf_cfg80211_info \*

    :param ndev:
        net device to transmit on.
    :type ndev: struct net_device \*

    :param af_params:
        configuration data for action frame.
    :type af_params: struct brcmf_fil_af_params_le \*

.. _`brcmf_p2p_notify_rx_mgmt_p2p_probereq`:

brcmf_p2p_notify_rx_mgmt_p2p_probereq
=====================================

.. c:function:: s32 brcmf_p2p_notify_rx_mgmt_p2p_probereq(struct brcmf_if *ifp, const struct brcmf_event_msg *e, void *data)

    Event handler for p2p probe req.

    :param ifp:
        interface pointer for which event was received.
    :type ifp: struct brcmf_if \*

    :param e:
        even message.
    :type e: const struct brcmf_event_msg \*

    :param data:
        payload of event message (probe request).
    :type data: void \*

.. _`brcmf_p2p_get_current_chanspec`:

brcmf_p2p_get_current_chanspec
==============================

.. c:function:: void brcmf_p2p_get_current_chanspec(struct brcmf_p2p_info *p2p, u16 *chanspec)

    Get current operation channel.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

    :param chanspec:
        chanspec to be returned.
    :type chanspec: u16 \*

.. _`brcmf_p2p_ifchange`:

brcmf_p2p_ifchange
==================

.. c:function:: int brcmf_p2p_ifchange(struct brcmf_cfg80211_info *cfg, enum brcmf_fil_p2p_if_types if_type)

    :param cfg:
        *undescribed*
    :type cfg: struct brcmf_cfg80211_info \*

    :param if_type:
        *undescribed*
    :type if_type: enum brcmf_fil_p2p_if_types

.. _`brcmf_p2p_create_p2pdev`:

brcmf_p2p_create_p2pdev
=======================

.. c:function:: struct wireless_dev *brcmf_p2p_create_p2pdev(struct brcmf_p2p_info *p2p, struct wiphy *wiphy, u8 *addr)

    create a P2P_DEVICE virtual interface.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

    :param wiphy:
        wiphy device of new interface.
    :type wiphy: struct wiphy \*

    :param addr:
        mac address for this new interface.
    :type addr: u8 \*

.. _`brcmf_p2p_add_vif`:

brcmf_p2p_add_vif
=================

.. c:function:: struct wireless_dev *brcmf_p2p_add_vif(struct wiphy *wiphy, const char *name, unsigned char name_assign_type, enum nl80211_iftype type, struct vif_params *params)

    create a new P2P virtual interface.

    :param wiphy:
        wiphy device of new interface.
    :type wiphy: struct wiphy \*

    :param name:
        name of the new interface.
    :type name: const char \*

    :param name_assign_type:
        origin of the interface name
    :type name_assign_type: unsigned char

    :param type:
        nl80211 interface type.
    :type type: enum nl80211_iftype

    :param params:
        contains mac address for P2P device.
    :type params: struct vif_params \*

.. _`brcmf_p2p_del_vif`:

brcmf_p2p_del_vif
=================

.. c:function:: int brcmf_p2p_del_vif(struct wiphy *wiphy, struct wireless_dev *wdev)

    delete a P2P virtual interface.

    :param wiphy:
        wiphy device of interface.
    :type wiphy: struct wiphy \*

    :param wdev:
        wireless device of interface.
    :type wdev: struct wireless_dev \*

.. _`brcmf_p2p_attach`:

brcmf_p2p_attach
================

.. c:function:: s32 brcmf_p2p_attach(struct brcmf_cfg80211_info *cfg, bool p2pdev_forced)

    attach for P2P.

    :param cfg:
        driver private data for cfg80211 interface.
    :type cfg: struct brcmf_cfg80211_info \*

    :param p2pdev_forced:
        create p2p device interface at attach.
    :type p2pdev_forced: bool

.. _`brcmf_p2p_detach`:

brcmf_p2p_detach
================

.. c:function:: void brcmf_p2p_detach(struct brcmf_p2p_info *p2p)

    detach P2P.

    :param p2p:
        P2P specific data.
    :type p2p: struct brcmf_p2p_info \*

.. This file was automatic generated / don't edit.

