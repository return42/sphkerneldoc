.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/scan.h

.. _`iwl_ssid_ie`:

struct iwl_ssid_ie
==================

.. c:type:: struct iwl_ssid_ie

    directed scan network information element

.. _`iwl_ssid_ie.definition`:

Definition
----------

.. code-block:: c

    struct iwl_ssid_ie {
        u8 id;
        u8 len;
        u8 ssid;
    }

.. _`iwl_ssid_ie.members`:

Members
-------

id
    element ID

len
    element length

ssid
    element (SSID) data

.. _`iwl_ssid_ie.description`:

Description
-----------

Up to 20 of these may appear in REPLY_SCAN_CMD,
selected by "type" bit field in struct iwl_scan_channel;
each channel may select different ssids from among the 20 entries.
SSID IEs get transmitted in reverse order of entry.

.. _`iwl_scan_offload_blacklist`:

struct iwl_scan_offload_blacklist
=================================

.. c:type:: struct iwl_scan_offload_blacklist

    SCAN_OFFLOAD_BLACKLIST_S

.. _`iwl_scan_offload_blacklist.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_offload_blacklist {
        u8 ssid;
        u8 reported_rssi;
        u8 client_bitmap;
    }

.. _`iwl_scan_offload_blacklist.members`:

Members
-------

ssid
    MAC address to filter out

reported_rssi
    AP rssi reported to the host

client_bitmap
    clients ignore this entry  - enum scan_framework_client

.. _`iwl_scan_offload_profile`:

struct iwl_scan_offload_profile
===============================

.. c:type:: struct iwl_scan_offload_profile

    SCAN_OFFLOAD_PROFILE_S

.. _`iwl_scan_offload_profile.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_offload_profile {
        u8 ssid_index;
        u8 unicast_cipher;
        u8 auth_alg;
        u8 network_type;
        u8 band_selection;
        u8 client_bitmap;
        u8 reserved;
    }

.. _`iwl_scan_offload_profile.members`:

Members
-------

ssid_index
    index to ssid list in fixed part

unicast_cipher
    encryption algorithm to match - bitmap

auth_alg
    authentication algorithm to match - bitmap

network_type
    enum iwl_scan_offload_network_type

band_selection
    enum iwl_scan_offload_band_selection

client_bitmap
    clients waiting for match - enum scan_framework_client

reserved
    reserved

.. _`iwl_scan_offload_profile_cfg`:

struct iwl_scan_offload_profile_cfg
===================================

.. c:type:: struct iwl_scan_offload_profile_cfg

    SCAN_OFFLOAD_PROFILES_CFG_API_S_VER_1

.. _`iwl_scan_offload_profile_cfg.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_offload_profile_cfg {
        struct iwl_scan_offload_profile profiles;
        u8 blacklist_len;
        u8 num_profiles;
        u8 match_notify;
        u8 pass_match;
        u8 active_clients;
        u8 any_beacon_notify;
        u8 reserved;
    }

.. _`iwl_scan_offload_profile_cfg.members`:

Members
-------

profiles
    profiles to search for match

blacklist_len
    length of blacklist

num_profiles
    num of profiles in the list

match_notify
    clients waiting for match found notification

pass_match
    clients waiting for the results

active_clients
    active clients bitmap - enum scan_framework_client

any_beacon_notify
    clients waiting for match notification without match

reserved
    reserved

.. _`iwl_scan_schedule_lmac`:

struct iwl_scan_schedule_lmac
=============================

.. c:type:: struct iwl_scan_schedule_lmac

    schedule of scan offload

.. _`iwl_scan_schedule_lmac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_schedule_lmac {
        __le16 delay;
        u8 iterations;
        u8 full_scan_mul;
    }

.. _`iwl_scan_schedule_lmac.members`:

Members
-------

delay
    delay between iterations, in seconds.

iterations
    num of scan iterations

full_scan_mul
    number of partial scans before each full scan

.. _`iwl_scan_req_tx_cmd`:

struct iwl_scan_req_tx_cmd
==========================

.. c:type:: struct iwl_scan_req_tx_cmd

    SCAN_REQ_TX_CMD_API_S

.. _`iwl_scan_req_tx_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_req_tx_cmd {
        __le32 tx_flags;
        __le32 rate_n_flags;
        u8 sta_id;
        u8 reserved;
    }

.. _`iwl_scan_req_tx_cmd.members`:

Members
-------

tx_flags
    combination of TX_CMD_FLG\_\*

rate_n_flags
    rate for \*all\* Tx attempts, if TX_CMD_FLG_STA_RATE_MSK is
    cleared. Combination of RATE_MCS\_\*

sta_id
    index of destination station in FW station table

reserved
    for alignment and future use

.. _`iwl_scan_channel_cfg_lmac`:

struct iwl_scan_channel_cfg_lmac
================================

.. c:type:: struct iwl_scan_channel_cfg_lmac

    SCAN_CHANNEL_CFG_S_VER2

.. _`iwl_scan_channel_cfg_lmac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_channel_cfg_lmac {
        __le32 flags;
        __le16 channel_num;
        __le16 iter_count;
        __le32 iter_interval;
    }

.. _`iwl_scan_channel_cfg_lmac.members`:

Members
-------

flags
    bits 1-20: directed scan to i'th ssid
    other bits \ :c:type:`enum iwl_scan_channel_flags_lmac <iwl_scan_channel_flags_lmac>`\ 

channel_num
    channel number 1-13 etc

iter_count
    scan iteration on this channel

iter_interval
    interval in seconds between iterations on one channel

.. _`iwl_mvm_lmac_scan_flags`:

enum iwl_mvm_lmac_scan_flags
============================

.. c:type:: enum iwl_mvm_lmac_scan_flags

    LMAC scan flags

.. _`iwl_mvm_lmac_scan_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_lmac_scan_flags {
        IWL_MVM_LMAC_SCAN_FLAG_PASS_ALL,
        IWL_MVM_LMAC_SCAN_FLAG_PASSIVE,
        IWL_MVM_LMAC_SCAN_FLAG_PRE_CONNECTION,
        IWL_MVM_LMAC_SCAN_FLAG_ITER_COMPLETE,
        IWL_MVM_LMAC_SCAN_FLAG_MULTIPLE_SSIDS,
        IWL_MVM_LMAC_SCAN_FLAG_FRAGMENTED,
        IWL_MVM_LMAC_SCAN_FLAGS_RRM_ENABLED,
        IWL_MVM_LMAC_SCAN_FLAG_EXTENDED_DWELL,
        IWL_MVM_LMAC_SCAN_FLAG_MATCH
    };

.. _`iwl_mvm_lmac_scan_flags.constants`:

Constants
---------

IWL_MVM_LMAC_SCAN_FLAG_PASS_ALL
    pass all beacons and probe responses
    without filtering.

IWL_MVM_LMAC_SCAN_FLAG_PASSIVE
    force passive scan on all channels

IWL_MVM_LMAC_SCAN_FLAG_PRE_CONNECTION
    single channel scan

IWL_MVM_LMAC_SCAN_FLAG_ITER_COMPLETE
    send iteration complete notification

IWL_MVM_LMAC_SCAN_FLAG_MULTIPLE_SSIDS
    multiple SSID matching

IWL_MVM_LMAC_SCAN_FLAG_FRAGMENTED
    all passive scans will be fragmented

IWL_MVM_LMAC_SCAN_FLAGS_RRM_ENABLED
    insert WFA vendor-specific TPC report
    and DS parameter set IEs into probe requests.

IWL_MVM_LMAC_SCAN_FLAG_EXTENDED_DWELL
    use extended dwell time on channels
    1, 6 and 11.

IWL_MVM_LMAC_SCAN_FLAG_MATCH
    Send match found notification on matches

.. _`iwl_scan_req_lmac`:

struct iwl_scan_req_lmac
========================

.. c:type:: struct iwl_scan_req_lmac

    SCAN_REQUEST_CMD_API_S_VER_1

.. _`iwl_scan_req_lmac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_req_lmac {
        __le32 reserved1;
        u8 n_channels;
        u8 active_dwell;
        u8 passive_dwell;
        u8 fragmented_dwell;
        u8 extended_dwell;
        u8 reserved2;
        __le16 rx_chain_select;
        __le32 scan_flags;
        __le32 max_out_time;
        __le32 suspend_time;
        __le32 flags;
        __le32 filter_flags;
        struct iwl_scan_req_tx_cmd tx_cmd;
        struct iwl_ssid_ie direct_scan;
        __le32 scan_prio;
        __le32 iter_num;
        __le32 delay;
        struct iwl_scan_schedule_lmac schedule;
        struct iwl_scan_channel_opt channel_opt;
        u8 data;
    }

.. _`iwl_scan_req_lmac.members`:

Members
-------

reserved1
    for alignment and future use

n_channels
    num of channels to scan

active_dwell
    dwell time for active channels

passive_dwell
    dwell time for passive channels

fragmented_dwell
    dwell time for fragmented passive scan

extended_dwell
    dwell time for channels 1, 6 and 11 (in certain cases)

reserved2
    for alignment and future use

rx_chain_select
    PHY_RX_CHAIN\_\* flags

scan_flags
    &enum iwl_mvm_lmac_scan_flags

max_out_time
    max time (in TU) to be out of associated channel

suspend_time
    pause scan this long (TUs) when returning to service channel

flags
    RXON flags

filter_flags
    RXON filter

tx_cmd
    tx command for active scan; for 2GHz and for 5GHz

direct_scan
    list of SSIDs for directed active scan

scan_prio
    enum iwl_scan_priority

iter_num
    number of scan iterations

delay
    delay in seconds before first iteration

schedule
    two scheduling plans. The first one is finite, the second one can
    be infinite.

channel_opt
    channel optimization options, for full and partial scan

data
    channel configuration and probe request packet.

.. _`iwl_scan_results_notif`:

struct iwl_scan_results_notif
=============================

.. c:type:: struct iwl_scan_results_notif

    scan results for one channel - SCAN_RESULT_NTF_API_S_VER_3

.. _`iwl_scan_results_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_results_notif {
        u8 channel;
        u8 band;
        u8 probe_status;
        u8 num_probe_not_sent;
        __le32 duration;
    }

.. _`iwl_scan_results_notif.members`:

Members
-------

channel
    which channel the results are from

band
    0 for 5.2 GHz, 1 for 2.4 GHz

probe_status
    SCAN_PROBE_STATUS\_\*, indicates success of probe request

num_probe_not_sent
    # of request that weren't sent due to not enough time

duration
    duration spent in channel, in usecs

.. _`iwl_lmac_scan_complete_notif`:

struct iwl_lmac_scan_complete_notif
===================================

.. c:type:: struct iwl_lmac_scan_complete_notif

    notifies end of scanning (all channels) SCAN_COMPLETE_NTF_API_S_VER_3

.. _`iwl_lmac_scan_complete_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_lmac_scan_complete_notif {
        u8 scanned_channels;
        u8 status;
        u8 bt_status;
        u8 last_channel;
        __le32 tsf_low;
        __le32 tsf_high;
        struct iwl_scan_results_notif results;
    }

.. _`iwl_lmac_scan_complete_notif.members`:

Members
-------

scanned_channels
    number of channels scanned (and number of valid results)

status
    one of SCAN_COMP_STATUS\_\*

bt_status
    BT on/off status

last_channel
    last channel that was scanned

tsf_low
    TSF timer (lower half) in usecs

tsf_high
    TSF timer (higher half) in usecs

results
    an array of scan results, only "scanned_channels" of them are valid

.. _`iwl_periodic_scan_complete`:

struct iwl_periodic_scan_complete
=================================

.. c:type:: struct iwl_periodic_scan_complete

    PERIODIC_SCAN_COMPLETE_NTF_API_S_VER_2

.. _`iwl_periodic_scan_complete.definition`:

Definition
----------

.. code-block:: c

    struct iwl_periodic_scan_complete {
        u8 last_schedule_line;
        u8 last_schedule_iteration;
        u8 status;
        u8 ebs_status;
        __le32 time_after_last_iter;
        __le32 reserved;
    }

.. _`iwl_periodic_scan_complete.members`:

Members
-------

last_schedule_line
    last schedule line executed (fast or regular)

last_schedule_iteration
    last scan iteration executed before scan abort

status
    &enum iwl_scan_offload_complete_status

ebs_status
    EBS success status \ :c:type:`enum iwl_scan_ebs_status <iwl_scan_ebs_status>`\ 

time_after_last_iter
    time in seconds elapsed after last iteration

reserved
    reserved

.. _`iwl_scan_dwell`:

struct iwl_scan_dwell
=====================

.. c:type:: struct iwl_scan_dwell


.. _`iwl_scan_dwell.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_dwell {
        u8 active;
        u8 passive;
        u8 fragmented;
        u8 extended;
    }

.. _`iwl_scan_dwell.members`:

Members
-------

active
    default dwell time for active scan

passive
    default dwell time for passive scan

fragmented
    default dwell time for fragmented scan

extended
    default dwell time for channels 1, 6 and 11

.. _`iwl_scan_config_v1`:

struct iwl_scan_config_v1
=========================

.. c:type:: struct iwl_scan_config_v1


.. _`iwl_scan_config_v1.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_config_v1 {
        __le32 flags;
        __le32 tx_chains;
        __le32 rx_chains;
        __le32 legacy_rates;
        __le32 out_of_channel_time;
        __le32 suspend_time;
        struct iwl_scan_dwell dwell;
        u8 mac_addr;
        u8 bcast_sta_id;
        u8 channel_flags;
        u8 channel_array;
    }

.. _`iwl_scan_config_v1.members`:

Members
-------

flags
    enum scan_config_flags

tx_chains
    valid_tx antenna - ANT\_\* definitions

rx_chains
    valid_rx antenna - ANT\_\* definitions

legacy_rates
    default legacy rates - enum scan_config_rates

out_of_channel_time
    default max out of serving channel time

suspend_time
    default max suspend time

dwell
    dwells for the scan

mac_addr
    default mac address to be used in probes

bcast_sta_id
    the index of the station in the fw

channel_flags
    default channel flags - enum iwl_channel_flags
    scan_config_channel_flag

channel_array
    default supported channels

.. _`iwl_umac_scan_flags`:

enum iwl_umac_scan_flags
========================

.. c:type:: enum iwl_umac_scan_flags

    UMAC scan flags

.. _`iwl_umac_scan_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_umac_scan_flags {
        IWL_UMAC_SCAN_FLAG_PREEMPTIVE,
        IWL_UMAC_SCAN_FLAG_START_NOTIF
    };

.. _`iwl_umac_scan_flags.constants`:

Constants
---------

IWL_UMAC_SCAN_FLAG_PREEMPTIVE
    scan process triggered by this scan request
    can be preempted by other scan requests with higher priority.
    The low priority scan will be resumed when the higher proirity scan is
    completed.

IWL_UMAC_SCAN_FLAG_START_NOTIF
    notification will be sent to the driver
    when scan starts.

.. _`iwl_scan_channel_cfg_umac`:

struct iwl_scan_channel_cfg_umac
================================

.. c:type:: struct iwl_scan_channel_cfg_umac


.. _`iwl_scan_channel_cfg_umac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_channel_cfg_umac {
        __le32 flags;
        u8 channel_num;
        u8 iter_count;
        __le16 iter_interval;
    }

.. _`iwl_scan_channel_cfg_umac.members`:

Members
-------

flags
    bitmap - 0-19:  directed scan to i'th ssid.

channel_num
    channel number 1-13 etc.

iter_count
    repetition count for the channel.

iter_interval
    interval between two scan iterations on one channel.

.. _`iwl_scan_umac_schedule`:

struct iwl_scan_umac_schedule
=============================

.. c:type:: struct iwl_scan_umac_schedule


.. _`iwl_scan_umac_schedule.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_umac_schedule {
        __le16 interval;
        u8 iter_count;
        u8 reserved;
    }

.. _`iwl_scan_umac_schedule.members`:

Members
-------

interval
    interval in seconds between scan iterations

iter_count
    num of scan iterations for schedule plan, 0xff for infinite loop

reserved
    for alignment and future use

.. _`iwl_scan_req_umac_tail`:

struct iwl_scan_req_umac_tail
=============================

.. c:type:: struct iwl_scan_req_umac_tail

    the rest of the UMAC scan request command parameters following channels configuration array.

.. _`iwl_scan_req_umac_tail.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_req_umac_tail {
        struct iwl_scan_umac_schedule schedule;
        __le16 delay;
        __le16 reserved;
        struct iwl_scan_probe_req preq;
        struct iwl_ssid_ie direct_scan;
    }

.. _`iwl_scan_req_umac_tail.members`:

Members
-------

schedule
    two scheduling plans.

delay
    delay in TUs before starting the first scan iteration

reserved
    for future use and alignment

preq
    probe request with IEs blocks

direct_scan
    list of SSIDs for directed active scan

.. _`iwl_scan_req_umac`:

struct iwl_scan_req_umac
========================

.. c:type:: struct iwl_scan_req_umac


.. _`iwl_scan_req_umac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_req_umac {
        __le32 flags;
        __le32 uid;
        __le32 ooc_priority;
        __le16 general_flags;
        u8 reserved2;
        u8 scan_start_mac_id;
        u8 extended_dwell;
        u8 active_dwell;
        u8 passive_dwell;
        u8 fragmented_dwell;
        union v1;
        struct v6;
         };
    }

.. _`iwl_scan_req_umac.members`:

Members
-------

flags
    &enum iwl_umac_scan_flags

uid
    scan id, \ :c:type:`enum iwl_umac_scan_uid_offsets <iwl_umac_scan_uid_offsets>`\ 

ooc_priority
    out of channel priority - \ :c:type:`enum iwl_scan_priority <iwl_scan_priority>`\ 

general_flags
    &enum iwl_umac_scan_general_flags

reserved2
    for future use and alignment

scan_start_mac_id
    report the scan start TSF time according to this mac TSF

extended_dwell
    dwell time for channels 1, 6 and 11

active_dwell
    dwell time for active scan

passive_dwell
    dwell time for passive scan

fragmented_dwell
    dwell time for fragmented passive scan

v1
    *undescribed*

v6
    *undescribed*

}
    *undescribed*

.. _`iwl_umac_scan_abort`:

struct iwl_umac_scan_abort
==========================

.. c:type:: struct iwl_umac_scan_abort


.. _`iwl_umac_scan_abort.definition`:

Definition
----------

.. code-block:: c

    struct iwl_umac_scan_abort {
        __le32 uid;
        __le32 flags;
    }

.. _`iwl_umac_scan_abort.members`:

Members
-------

uid
    scan id, \ :c:type:`enum iwl_umac_scan_uid_offsets <iwl_umac_scan_uid_offsets>`\ 

flags
    reserved

.. _`iwl_umac_scan_complete`:

struct iwl_umac_scan_complete
=============================

.. c:type:: struct iwl_umac_scan_complete


.. _`iwl_umac_scan_complete.definition`:

Definition
----------

.. code-block:: c

    struct iwl_umac_scan_complete {
        __le32 uid;
        u8 last_schedule;
        u8 last_iter;
        u8 status;
        u8 ebs_status;
        __le32 time_from_last_iter;
        __le32 reserved;
    }

.. _`iwl_umac_scan_complete.members`:

Members
-------

uid
    scan id, \ :c:type:`enum iwl_umac_scan_uid_offsets <iwl_umac_scan_uid_offsets>`\ 

last_schedule
    last scheduling line

last_iter
    last scan iteration number

status
    &enum iwl_scan_offload_complete_status

ebs_status
    &enum iwl_scan_ebs_status

time_from_last_iter
    time elapsed from last iteration

reserved
    for future use

.. _`iwl_scan_offload_profile_match`:

struct iwl_scan_offload_profile_match
=====================================

.. c:type:: struct iwl_scan_offload_profile_match

    match information

.. _`iwl_scan_offload_profile_match.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_offload_profile_match {
        u8 bssid;
        __le16 reserved;
        u8 channel;
        u8 energy;
        u8 matching_feature;
        u8 matching_channels;
    }

.. _`iwl_scan_offload_profile_match.members`:

Members
-------

bssid
    matched bssid

reserved
    reserved

channel
    channel where the match occurred

energy
    energy

matching_feature
    feature matches

matching_channels
    bitmap of channels that matched, referencing
    the channels passed in tue scan offload request

.. _`iwl_scan_offload_profiles_query`:

struct iwl_scan_offload_profiles_query
======================================

.. c:type:: struct iwl_scan_offload_profiles_query

    match results query response

.. _`iwl_scan_offload_profiles_query.definition`:

Definition
----------

.. code-block:: c

    struct iwl_scan_offload_profiles_query {
        __le32 matched_profiles;
        __le32 last_scan_age;
        __le32 n_scans_done;
        __le32 gp2_d0u;
        __le32 gp2_invoked;
        u8 resume_while_scanning;
        u8 self_recovery;
        __le16 reserved;
        struct iwl_scan_offload_profile_match matches;
    }

.. _`iwl_scan_offload_profiles_query.members`:

Members
-------

matched_profiles
    bitmap of matched profiles, referencing the
    matches passed in the scan offload request

last_scan_age
    age of the last offloaded scan

n_scans_done
    number of offloaded scans done

gp2_d0u
    GP2 when D0U occurred

gp2_invoked
    GP2 when scan offload was invoked

resume_while_scanning
    not used

self_recovery
    obsolete

reserved
    reserved

matches
    array of match information, one for each match

.. _`iwl_umac_scan_iter_complete_notif`:

struct iwl_umac_scan_iter_complete_notif
========================================

.. c:type:: struct iwl_umac_scan_iter_complete_notif

    notifies end of scanning iteration

.. _`iwl_umac_scan_iter_complete_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_umac_scan_iter_complete_notif {
        __le32 uid;
        u8 scanned_channels;
        u8 status;
        u8 bt_status;
        u8 last_channel;
        __le64 start_tsf;
        struct iwl_scan_results_notif results;
    }

.. _`iwl_umac_scan_iter_complete_notif.members`:

Members
-------

uid
    scan id, \ :c:type:`enum iwl_umac_scan_uid_offsets <iwl_umac_scan_uid_offsets>`\ 

scanned_channels
    number of channels scanned and number of valid elements in
    results array

status
    one of SCAN_COMP_STATUS\_\*

bt_status
    BT on/off status

last_channel
    last channel that was scanned

start_tsf
    TSF timer in usecs of the scan start time for the mac specified
    in \ :c:type:`struct iwl_scan_req_umac <iwl_scan_req_umac>`\ .

results
    array of scan results, length in \ ``scanned_channels``\ 

.. This file was automatic generated / don't edit.

