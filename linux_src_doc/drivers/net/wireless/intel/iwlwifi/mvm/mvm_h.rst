.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/mvm/mvm.h

.. _`iwl_mvm_mod_params`:

struct iwl_mvm_mod_params
=========================

.. c:type:: struct iwl_mvm_mod_params

    module parameters for iwlmvm

.. _`iwl_mvm_mod_params.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_mod_params {
        bool init_dbg;
        bool tfd_q_hang_detect;
        int power_scheme;
    }

.. _`iwl_mvm_mod_params.members`:

Members
-------

init_dbg
    if true, then the NIC won't be stopped if the INIT fw asserted.
    We will register to mac80211 to have testmode working. The NIC must not
    be up'ed after the INIT fw asserted. This is useful to be able to use
    proprietary tools over testmode to debug the INIT fw.

tfd_q_hang_detect
    enabled the detection of hung transmit queues

power_scheme
    one of enum iwl_power_scheme

.. _`iwl_mvm_dump_ptrs`:

struct iwl_mvm_dump_ptrs
========================

.. c:type:: struct iwl_mvm_dump_ptrs

    set of pointers needed for the fw-error-dump

.. _`iwl_mvm_dump_ptrs.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_dump_ptrs {
        struct iwl_trans_dump_data *trans_ptr;
        void *op_mode_ptr;
        u32 op_mode_len;
    }

.. _`iwl_mvm_dump_ptrs.members`:

Members
-------

trans_ptr
    pointer to struct \ ``iwl_trans_dump_data``\  which contains the
    transport's data.

op_mode_ptr
    pointer to the buffer coming from the mvm op_mode

op_mode_len
    length of the valid data in op_mode_ptr

.. _`iwl_mvm_dump_desc`:

struct iwl_mvm_dump_desc
========================

.. c:type:: struct iwl_mvm_dump_desc

    describes the dump

.. _`iwl_mvm_dump_desc.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_dump_desc {
        size_t len;
        struct iwl_fw_error_dump_trigger_desc trig_desc;
    }

.. _`iwl_mvm_dump_desc.members`:

Members
-------

len
    length of trig_desc->data

trig_desc
    the description of the dump

.. _`iwl_power_scheme`:

enum iwl_power_scheme
=====================

.. c:type:: enum iwl_power_scheme

    \ ``IWL_POWER_LEVEL_CAM``\  - Continuously Active Mode \ ``IWL_POWER_LEVEL_BPS``\  - Balanced Power Save (default) \ ``IWL_POWER_LEVEL_LP``\   - Low Power

.. _`iwl_power_scheme.definition`:

Definition
----------

.. code-block:: c

    enum iwl_power_scheme {
        IWL_POWER_SCHEME_CAM,
        IWL_POWER_SCHEME_BPS,
        IWL_POWER_SCHEME_LP
    };

.. _`iwl_power_scheme.constants`:

Constants
---------

IWL_POWER_SCHEME_CAM
    *undescribed*

IWL_POWER_SCHEME_BPS
    *undescribed*

IWL_POWER_SCHEME_LP
    *undescribed*

.. _`iwl_mvm_vif_bf_data`:

struct iwl_mvm_vif_bf_data
==========================

.. c:type:: struct iwl_mvm_vif_bf_data

    beacon filtering related data

.. _`iwl_mvm_vif_bf_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_vif_bf_data {
        bool bf_enabled;
        bool ba_enabled;
        int ave_beacon_signal;
        int last_cqm_event;
        int bt_coex_min_thold;
        int bt_coex_max_thold;
        int last_bt_coex_event;
    }

.. _`iwl_mvm_vif_bf_data.members`:

Members
-------

bf_enabled
    indicates if beacon filtering is enabled

ba_enabled
    indicated if beacon abort is enabled

ave_beacon_signal
    average beacon signal

last_cqm_event
    rssi of the last cqm event

bt_coex_min_thold
    minimum threshold for BT coex

bt_coex_max_thold
    maximum threshold for BT coex

last_bt_coex_event
    rssi of the last BT coex event

.. _`iwl_mvm_vif`:

struct iwl_mvm_vif
==================

.. c:type:: struct iwl_mvm_vif

    data per Virtual Interface, it is a MAC context

.. _`iwl_mvm_vif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_vif {
        struct iwl_mvm *mvm;
        u16 id;
        u16 color;
        u8 ap_sta_id;
        u8 bssid[ETH_ALEN];
        bool associated;
        u8 ap_assoc_sta_count;
        bool uploaded;
        bool ap_ibss_active;
        bool pm_enabled;
        bool monitor_active;
        bool low_latency_traffic;
        bool low_latency_dbgfs;
        bool low_latency_vcmd;
        bool ps_disabled;
        struct iwl_mvm_vif_bf_data bf_data;
        struct rekey_data;
        int tx_key_idx;
        bool seqno_valid;
        u16 seqno;
    #endif
    #if IS_ENABLED(CONFIG_IPV6)
        struct in6_addr target_ipv6_addrs[IWL_PROTO_OFFLOAD_NUM_IPV6_ADDRS_MAX];
        unsigned long tentative_addrs[BITS_TO_LONGS(IWL_PROTO_OFFLOAD_NUM_IPV6_ADDRS_MAX)];
        int num_target_ipv6_addrs;
    #endif
    #ifdef CONFIG_IWLWIFI_DEBUGFS
        struct dentry *dbgfs_dir;
        struct dentry *dbgfs_slink;
        struct iwl_dbgfs_pm dbgfs_pm;
        struct iwl_dbgfs_bf dbgfs_bf;
        struct iwl_mac_power_cmd mac_pwr_cmd;
        int dbgfs_quota_min;
    #endif
        enum ieee80211_smps_mode smps_requests[NUM_IWL_MVM_SMPS_REQ];
        u8 uapsd_misbehaving_bssid[ETH_ALEN];
        bool csa_countdown;
        bool csa_failed;
        netdev_features_t features;
        bool lqm_active;
    }

.. _`iwl_mvm_vif.members`:

Members
-------

mvm
    *undescribed*

id
    between 0 and 3

color
    to solve races upon MAC addition and removal

ap_sta_id
    the sta_id of the AP - valid only if VIF type is STA

bssid
    BSSID for this (client) interface

associated
    indicates that we're currently associated, used only for
    managing the firmware state in \ :c:func:`iwl_mvm_bss_info_changed_station`\ 

ap_assoc_sta_count
    count of stations associated to us - valid only
    if VIF type is AP

uploaded
    indicates the MAC context has been added to the device

ap_ibss_active
    indicates that AP/IBSS is configured and that the interface
    should get quota etc.
    \ ``pm_enabled``\  - Indicate if MAC power management is allowed

pm_enabled
    *undescribed*

monitor_active
    indicates that monitor context is configured, and that the
    interface should get quota etc.

low_latency_traffic
    indicates low latency traffic was detected

low_latency_dbgfs
    low latency mode set from debugfs

low_latency_vcmd
    low latency mode set from vendor command

ps_disabled
    indicates that this interface requires PS to be disabled

bf_data
    *undescribed*

rekey_data
    *undescribed*

tx_key_idx
    *undescribed*

seqno_valid
    *undescribed*

seqno
    *undescribed*

num_target_ipv6_addrs
    *undescribed*

dbgfs_dir
    *undescribed*

dbgfs_slink
    *undescribed*

dbgfs_pm
    *undescribed*

dbgfs_bf
    *undescribed*

mac_pwr_cmd
    *undescribed*

dbgfs_quota_min
    *undescribed*

smps_requests
    the SMPS requests of different parts of the driver,
    combined on update to yield the overall request to mac80211.

csa_countdown
    *undescribed*

csa_failed
    CSA failed to schedule time event, report an error later

features
    hw features active for this vif

lqm_active
    *undescribed*

.. _`iwl_mvm_vif.vifs`:

vifs
----

P2P_DEVICE, GO and AP.

.. _`iwl_nvm_section`:

struct iwl_nvm_section
======================

.. c:type:: struct iwl_nvm_section

    describes an NVM section in memory.

.. _`iwl_nvm_section.definition`:

Definition
----------

.. code-block:: c

    struct iwl_nvm_section {
        u16 length;
        const u8 *data;
    }

.. _`iwl_nvm_section.members`:

Members
-------

length
    *undescribed*

data
    *undescribed*

.. _`iwl_nvm_section.description`:

Description
-----------

This struct holds an NVM section read from the NIC using NVM_ACCESS_CMD,
and saved for later use by the driver. Not all NVM sections are saved
this way, only the needed ones.

.. _`iwl_mvm_tt_mgmt`:

struct iwl_mvm_tt_mgmt
======================

.. c:type:: struct iwl_mvm_tt_mgmt

    Thermal Throttling Management structure

.. _`iwl_mvm_tt_mgmt.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_tt_mgmt {
        struct delayed_work ct_kill_exit;
        bool dynamic_smps;
        u32 tx_backoff;
        u32 min_backoff;
        struct iwl_tt_params params;
        bool throttle;
    }

.. _`iwl_mvm_tt_mgmt.members`:

Members
-------

ct_kill_exit
    worker to exit thermal kill

dynamic_smps
    Is thermal throttling enabled dynamic_smps?

tx_backoff
    The current thremal throttling tx backoff in uSec.

min_backoff
    The minimal tx backoff due to power restrictions

params
    Parameters to configure the thermal throttling algorithm.

throttle
    Is thermal throttling is active?

.. _`iwl_mvm_thermal_device`:

struct iwl_mvm_thermal_device
=============================

.. c:type:: struct iwl_mvm_thermal_device

    thermal zone related data

.. _`iwl_mvm_thermal_device.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_thermal_device {
        s16 temp_trips[IWL_MAX_DTS_TRIPS];
        u8 fw_trips_index[IWL_MAX_DTS_TRIPS];
        struct thermal_zone_device *tzone;
    }

.. _`iwl_mvm_thermal_device.members`:

Members
-------

temp_trips
    temperature thresholds for report

fw_trips_index
    keep indexes to original array - temp_trips

tzone
    thermal zone device data

.. _`iwl_mvm_reorder_buffer`:

struct iwl_mvm_reorder_buffer
=============================

.. c:type:: struct iwl_mvm_reorder_buffer

    per ra/tid/queue reorder buffer

.. _`iwl_mvm_reorder_buffer.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_reorder_buffer {
        u16 head_sn;
        u16 num_stored;
        u8 buf_size;
        u8 sta_id;
        int queue;
        u16 last_amsdu;
        u8 last_sub_index;
        struct sk_buff_head entries[IEEE80211_MAX_AMPDU_BUF];
        unsigned long reorder_time[IEEE80211_MAX_AMPDU_BUF];
        struct timer_list reorder_timer;
        bool removed;
        spinlock_t lock;
        struct iwl_mvm *mvm;
    }

.. _`iwl_mvm_reorder_buffer.members`:

Members
-------

head_sn
    reorder window head sn

num_stored
    number of mpdus stored in the buffer

buf_size
    the reorder buffer size as set by the last addba request

sta_id
    sta id of this reorder buffer

queue
    queue of this reorder buffer

last_amsdu
    track last ASMDU SN for duplication detection

last_sub_index
    track ASMDU sub frame index for duplication detection

entries
    list of skbs stored

reorder_time
    time the packet was stored in the reorder buffer

reorder_timer
    timer for frames are in the reorder buffer. For AMSDU
    it is the time of last received sub-frame

removed
    prevent timer re-arming

lock
    protect reorder buffer internal state

mvm
    mvm pointer, needed for frame timer context

.. _`iwl_mvm_baid_data`:

struct iwl_mvm_baid_data
========================

.. c:type:: struct iwl_mvm_baid_data

    BA session data

.. _`iwl_mvm_baid_data.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mvm_baid_data {
        struct rcu_head rcu_head;
        u8 sta_id;
        u8 tid;
        u8 baid;
        u16 timeout;
        unsigned long last_rx;
        struct timer_list session_timer;
        struct iwl_mvm *mvm;
        struct iwl_mvm_reorder_buffer reorder_buf[];
    }

.. _`iwl_mvm_baid_data.members`:

Members
-------

rcu_head
    *undescribed*

sta_id
    station id

tid
    tid of the session
    \ ``baid``\  baid of the session

baid
    *undescribed*

timeout
    the timeout set in the addba request

last_rx
    last rx jiffies, updated only if timeout passed from last update

session_timer
    timer to check if BA session expired, runs at 2 \* timeout

mvm
    mvm pointer, needed for timer context

reorder_buf
    reorder buffer, allocated per queue

.. This file was automatic generated / don't edit.
