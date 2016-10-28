.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-tof.h

.. _`iwl_tof_config_cmd`:

struct iwl_tof_config_cmd
=========================

.. c:type:: struct iwl_tof_config_cmd

    ToF configuration

.. _`iwl_tof_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_config_cmd {
        __le32 sub_grp_cmd_id;
        u8 tof_disabled;
        u8 one_sided_disabled;
        u8 is_debug_mode;
        u8 is_buf_required;
    }

.. _`iwl_tof_config_cmd.members`:

Members
-------

sub_grp_cmd_id
    *undescribed*

tof_disabled
    0 enabled, 1 - disabled

one_sided_disabled
    0 enabled, 1 - disabled

is_debug_mode
    1 debug mode, 0 - otherwise

is_buf_required
    1 channel estimation buffer required, 0 - otherwise

.. _`iwl_tof_responder_config_cmd`:

struct iwl_tof_responder_config_cmd
===================================

.. c:type:: struct iwl_tof_responder_config_cmd

    ToF AP mode (for debug)

.. _`iwl_tof_responder_config_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_responder_config_cmd {
        __le32 sub_grp_cmd_id;
        __le16 burst_period;
        u8 min_delta_ftm;
        u8 burst_duration;
        u8 num_of_burst_exp;
        u8 get_ch_est;
        u8 abort_responder;
        u8 recv_sta_req_params;
        u8 channel_num;
        u8 bandwidth;
        u8 rate;
        u8 ctrl_ch_position;
        u8 ftm_per_burst;
        u8 ftm_resp_ts_avail;
        u8 asap_mode;
        u8 sta_id;
        __le16 tsf_timer_offset_msecs;
        __le16 toa_offset;
        u8 bssid[ETH_ALEN];
    }

.. _`iwl_tof_responder_config_cmd.members`:

Members
-------

sub_grp_cmd_id
    *undescribed*

burst_period
    future use: (currently hard coded in the LMAC)
    The interval between two sequential bursts.

min_delta_ftm
    future use: (currently hard coded in the LMAC)
    The minimum delay between two sequential FTM Responses
    in the same burst.

burst_duration
    future use: (currently hard coded in the LMAC)
    The total time for all FTMs handshake in the same burst.
    Affect the time events duration in the LMAC.

num_of_burst_exp
    future use: (currently hard coded in the LMAC)
    The number of bursts for the current ToF request. Affect
    the number of events allocations in the current iteration.

get_ch_est
    for xVT only, NA for driver

abort_responder
    when set to '1' - Responder will terminate its activity
    (all other fields in the command are ignored)

recv_sta_req_params
    1 - Responder will ignore the other Responder's
    params and use the recomended Initiator params.
    0 - otherwise

channel_num
    current AP Channel

bandwidth
    current AP Bandwidth: 0  20MHz, 1  40MHz, 2  80MHz

rate
    current AP rate

ctrl_ch_position
    coding of the control channel position relative to
    the center frequency.
    40MHz  0 below center, 1 above center
    80MHz  bits [0..1]: 0  the near 20MHz to the center,
    1  the far  20MHz to the center
    bit[2]  as above 40MHz

ftm_per_burst
    FTMs per Burst

ftm_resp_ts_avail
    '0' - we don't measure over the Initial FTM Response,
    '1' - we measure over the Initial FTM Response

asap_mode
    ASAP / Non ASAP mode for the current WLS station

sta_id
    index of the AP STA when in AP mode

tsf_timer_offset_msecs
    The dictated time offset (mSec) from the AP's TSF

toa_offset
    Artificial addition [0.1nsec] for the ToA - to be used for debug
    purposes, simulating station movement by adding various values
    to this field

bssid
    Current AP BSSID

.. _`iwl_tof_range_req_ext_cmd`:

struct iwl_tof_range_req_ext_cmd
================================

.. c:type:: struct iwl_tof_range_req_ext_cmd

    extended range req for WLS

.. _`iwl_tof_range_req_ext_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_range_req_ext_cmd {
        __le32 sub_grp_cmd_id;
        __le16 tsf_timer_offset_msec;
        __le16 reserved;
        u8 min_delta_ftm;
        u8 ftm_format_and_bw20M;
        u8 ftm_format_and_bw40M;
        u8 ftm_format_and_bw80M;
    }

.. _`iwl_tof_range_req_ext_cmd.members`:

Members
-------

sub_grp_cmd_id
    *undescribed*

tsf_timer_offset_msec
    the recommended time offset (mSec) from the AP's TSF

reserved
    *undescribed*

min_delta_ftm
    Minimal time between two consecutive measurements,
    in units of 100us. 0 means no preference by station

ftm_format_and_bw20M
    FTM Channel Spacing/Format for 20MHz: recommended
    value be sent to the AP

ftm_format_and_bw40M
    FTM Channel Spacing/Format for 40MHz: recommended
    value to be sent to the AP

ftm_format_and_bw80M
    FTM Channel Spacing/Format for 80MHz: recommended
    value to be sent to the AP

.. _`iwl_tof_range_req_ap_entry`:

struct iwl_tof_range_req_ap_entry
=================================

.. c:type:: struct iwl_tof_range_req_ap_entry

    AP configuration parameters

.. _`iwl_tof_range_req_ap_entry.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_range_req_ap_entry {
        u8 channel_num;
        u8 bandwidth;
        u8 tsf_delta_direction;
        u8 ctrl_ch_position;
        u8 bssid[ETH_ALEN];
        u8 measure_type;
        u8 num_of_bursts;
        __le16 burst_period;
        u8 samples_per_burst;
        u8 retries_per_sample;
        __le32 tsf_delta;
        u8 location_req;
        u8 asap_mode;
        u8 enable_dyn_ack;
        s8 rssi;
    }

.. _`iwl_tof_range_req_ap_entry.members`:

Members
-------

channel_num
    Current AP Channel

bandwidth
    Current AP Bandwidth: 0  20MHz, 1  40MHz, 2  80MHz

tsf_delta_direction
    TSF relatively to the subject AP

ctrl_ch_position
    Coding of the control channel position relative to the
    center frequency.
    40MHz  0 below center, 1 above center
    80MHz  bits [0..1]: 0  the near 20MHz to the center,
    1  the far  20MHz to the center
    bit[2]  as above 40MHz

bssid
    AP's bss id

measure_type
    Measurement type: 0 - two sided, 1 - One sided

num_of_bursts
    Recommended value to be sent to the AP.  2s Exponent of the
    number of measurement iterations (min 2^0 = 1, max 2^14)

burst_period
    Recommended value to be sent to the AP. Measurement
    periodicity In units of 100ms. ignored if num_of_bursts = 0

samples_per_burst
    2-sided: the number of FTMs pairs in single Burst (1-31)
    1-sided: how many rts/cts pairs should be used per burst.

retries_per_sample
    Max number of retries that the LMAC should send
    in case of no replies by the AP.

tsf_delta
    TSF Delta in units of microseconds.
    The difference between the AP TSF and the device local clock.

location_req
    Location Request Bit[0] LCI should be sent in the FTMR
    Bit[1] Civic should be sent in the FTMR

asap_mode
    0 - non asap mode, 1 - asap mode (not relevant for one sided)

enable_dyn_ack
    Enable Dynamic ACK BW.
    0  Initiator interact with regular AP
    1  Initiator interact with Responder machine: need to send the
    Initiator Acks with HT 40MHz / 80MHz, since the Responder should
    use it for its ch est measurement (this flag will be set when we
    configure the opposite machine to be Responder).

rssi
    Last received value

.. _`iwl_tof_range_req_ap_entry.leagal-values`:

leagal values
-------------

-128-0 (0x7f). above 0x0 indicating an invalid value.

.. _`iwl_tof_response_mode`:

enum iwl_tof_response_mode
==========================

.. c:type:: enum iwl_tof_response_mode


.. _`iwl_tof_response_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_tof_response_mode {
        IWL_MVM_TOF_RESPOSE_ASAP,
        IWL_MVM_TOF_RESPOSE_TIMEOUT,
        IWL_MVM_TOF_RESPOSE_COMPLETE
    };

.. _`iwl_tof_response_mode.constants`:

Constants
---------

IWL_MVM_TOF_RESPOSE_ASAP
    report each AP measurement separately as soon as
    possible (not supported for this release)

IWL_MVM_TOF_RESPOSE_TIMEOUT
    report all AP measurements as a batch upon
    timeout expiration

IWL_MVM_TOF_RESPOSE_COMPLETE
    report all AP measurements as a batch at the
    earlier of: measurements completion / timeout
    expiration.

.. _`iwl_tof_range_req_cmd`:

struct iwl_tof_range_req_cmd
============================

.. c:type:: struct iwl_tof_range_req_cmd

    start measurement cmd

.. _`iwl_tof_range_req_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_range_req_cmd {
        __le32 sub_grp_cmd_id;
        u8 request_id;
        u8 initiator;
        u8 one_sided_los_disable;
        u8 req_timeout;
        u8 report_policy;
        u8 los_det_disable;
        u8 num_of_ap;
        u8 macaddr_random;
        u8 macaddr_template[ETH_ALEN];
        u8 macaddr_mask[ETH_ALEN];
        struct iwl_tof_range_req_ap_entry ap[IWL_MVM_TOF_MAX_APS];
    }

.. _`iwl_tof_range_req_cmd.members`:

Members
-------

sub_grp_cmd_id
    *undescribed*

request_id
    A Token incremented per request. The same Token will be
    sent back in the range response

initiator
    0- NW initiated,  1 - Client Initiated

one_sided_los_disable
    '0'- run ML-Algo for both ToF/OneSided,
    '1' - run ML-Algo for ToF only

req_timeout
    Requested timeout of the response in units of 100ms.
    This is equivalent to the session time configured to the
    LMAC in Initiator Request

report_policy
    Supported partially for this release: For current release -
    the range report will be uploaded as a batch when ready or
    when the session is done (successfully / partially).
    one of iwl_tof_response_mode.

los_det_disable
    *undescribed*

num_of_ap
    Number of APs to measure (error if > IWL_MVM_TOF_MAX_APS)

macaddr_random
    '0' Use default source MAC address (i.e. p2_p),
    '1' Use MAC Address randomization according to the below

macaddr_mask
    Bits set to 0 shall be copied from the MAC address template.
    Bits set to 1 shall be randomized by the UMAC

.. _`iwl_tof_gen_resp_cmd`:

struct iwl_tof_gen_resp_cmd
===========================

.. c:type:: struct iwl_tof_gen_resp_cmd

    generic ToF response

.. _`iwl_tof_gen_resp_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_gen_resp_cmd {
        __le32 sub_grp_cmd_id;
        u8 data[];
    }

.. _`iwl_tof_gen_resp_cmd.members`:

Members
-------

sub_grp_cmd_id
    *undescribed*

.. _`iwl_tof_range_rsp_ap_entry_ntfy`:

struct iwl_tof_range_rsp_ap_entry_ntfy
======================================

.. c:type:: struct iwl_tof_range_rsp_ap_entry_ntfy

    AP parameters (response)

.. _`iwl_tof_range_rsp_ap_entry_ntfy.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_range_rsp_ap_entry_ntfy {
        u8 bssid[ETH_ALEN];
        u8 measure_status;
        u8 measure_bw;
        __le32 rtt;
        __le32 rtt_variance;
        __le32 rtt_spread;
        s8 rssi;
        u8 rssi_spread;
        __le16 reserved;
        __le32 range;
        __le32 range_variance;
        __le32 timestamp;
    }

.. _`iwl_tof_range_rsp_ap_entry_ntfy.members`:

Members
-------

measure_status
    current APs measurement status

measure_bw
    Current AP Bandwidth: 0  20MHz, 1  40MHz, 2  80MHz

rtt
    The Round Trip Time that took for the last measurement for
    current AP [nSec]

rtt_variance
    The Variance of the RTT values measured for current AP

rtt_spread
    The Difference between the maximum and the minimum RTT
    values measured for current AP in the current session [nsec]

rssi
    RSSI as uploaded in the Channel Estimation notification

rssi_spread
    The Difference between the maximum and the minimum RSSI values
    measured for current AP in the current session

reserved
    *undescribed*

range
    Measured range [cm]

range_variance
    Measured range variance [cm]

timestamp
    The GP2 Clock [usec] where Channel Estimation notification was
    uploaded by the LMAC

.. _`iwl_tof_range_rsp_ntfy`:

struct iwl_tof_range_rsp_ntfy
=============================

.. c:type:: struct iwl_tof_range_rsp_ntfy


.. _`iwl_tof_range_rsp_ntfy.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_range_rsp_ntfy {
        u8 request_id;
        u8 request_status;
        u8 last_in_batch;
        u8 num_of_aps;
        struct iwl_tof_range_rsp_ap_entry_ntfy ap[IWL_MVM_TOF_MAX_APS];
    }

.. _`iwl_tof_range_rsp_ntfy.members`:

Members
-------

request_id
    A Token ID of the corresponding Range request

request_status
    status of current measurement session

last_in_batch
    reprot policy (when not all responses are uploaded at once)

num_of_aps
    Number of APs to measure (error if > IWL_MVM_TOF_MAX_APS)

.. _`iwl_tof_mcsi_notif`:

struct iwl_tof_mcsi_notif
=========================

.. c:type:: struct iwl_tof_mcsi_notif

    used for debug

.. _`iwl_tof_mcsi_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_mcsi_notif {
        u8 token;
        u8 role;
        __le16 reserved;
        u8 initiator_bssid[ETH_ALEN];
        u8 responder_bssid[ETH_ALEN];
        u8 mcsi_buffer[IWL_MVM_TOF_MCSI_BUF_SIZE * 4];
    }

.. _`iwl_tof_mcsi_notif.members`:

Members
-------

token
    token ID for the current session

role
    '0' - initiator, '1' - responder

reserved
    *undescribed*

initiator_bssid
    initiator machine

responder_bssid
    responder machine

mcsi_buffer
    debug data

.. _`iwl_tof_neighbor_report`:

struct iwl_tof_neighbor_report
==============================

.. c:type:: struct iwl_tof_neighbor_report


.. _`iwl_tof_neighbor_report.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_neighbor_report {
        u8 bssid[ETH_ALEN];
        u8 request_token;
        u8 status;
        __le16 report_ie_len;
        u8 data[];
    }

.. _`iwl_tof_neighbor_report.members`:

Members
-------

bssid
    BSSID of the AP which sent the report

request_token
    same token as the corresponding request

status
    *undescribed*

report_ie_len
    the length of the response frame starting from the Element ID

data
    the IEs

.. _`iwl_tof_range_abort_cmd`:

struct iwl_tof_range_abort_cmd
==============================

.. c:type:: struct iwl_tof_range_abort_cmd


.. _`iwl_tof_range_abort_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_tof_range_abort_cmd {
        __le32 sub_grp_cmd_id;
        u8 request_id;
        u8 reserved[3];
    }

.. _`iwl_tof_range_abort_cmd.members`:

Members
-------

sub_grp_cmd_id
    *undescribed*

request_id
    corresponds to a range request

.. This file was automatic generated / don't edit.

