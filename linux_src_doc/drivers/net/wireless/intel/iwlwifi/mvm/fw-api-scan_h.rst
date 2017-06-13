.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/fw-api-scan.h

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
        u8 ssid[IEEE80211_MAX_SSID_LEN];
    }

.. _`iwl_ssid_ie.members`:

Members
-------

id
    *undescribed*

len
    *undescribed*

.. _`iwl_ssid_ie.description`:

Description
-----------

Up to 20 of these may appear in REPLY_SCAN_CMD,
selected by "type" bit field in struct iwl_scan_channel;
each channel may select different ssids from among the 20 entries.
SSID IEs get transmitted in reverse order of entry.

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
        struct iwl_scan_results_notif results[];
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
        u8 mac_addr[ETH_ALEN];
        u8 bcast_sta_id;
        u8 channel_flags;
        u8 channel_array[];
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
        struct iwl_scan_umac_schedule schedule[IWL_MAX_SCHED_SCAN_PLANS];
        __le16 delay;
        __le16 reserved;
        struct iwl_scan_probe_req preq;
        struct iwl_ssid_ie direct_scan[PROBE_OPTION_MAX];
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
        union {unnamed_union};
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

{unnamed_union}
    anonymous


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
    *undescribed*

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
        u8 bssid[ETH_ALEN];
        __le16 reserved;
        u8 channel;
        u8 energy;
        u8 matching_feature;
        u8 matching_channels[SCAN_OFFLOAD_MATCHING_CHANNELS_LEN];
    }

.. _`iwl_scan_offload_profile_match.members`:

Members
-------

bssid
    matched bssid

reserved
    *undescribed*

channel
    channel where the match occurred

energy
    *undescribed*

matching_feature
    *undescribed*

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
        struct iwl_scan_offload_profile_match matches[IWL_SCAN_MAX_PROFILES];
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
        struct iwl_scan_results_notif results[];
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
    array of scan results, only "scanned_channels" of them are valid

.. This file was automatic generated / don't edit.

