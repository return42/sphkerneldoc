.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/dfs_pattern_detector.h

.. _`ath_dfs_pool_stats`:

struct ath_dfs_pool_stats
=========================

.. c:type:: struct ath_dfs_pool_stats

    DFS Statistics for global pools

.. _`ath_dfs_pool_stats.definition`:

Definition
----------

.. code-block:: c

    struct ath_dfs_pool_stats {
        u32 pool_reference;
        u32 pulse_allocated;
        u32 pulse_alloc_error;
        u32 pulse_used;
        u32 pseq_allocated;
        u32 pseq_alloc_error;
        u32 pseq_used;
    }

.. _`ath_dfs_pool_stats.members`:

Members
-------

pool_reference
    *undescribed*

pulse_allocated
    *undescribed*

pulse_alloc_error
    *undescribed*

pulse_used
    *undescribed*

pseq_allocated
    *undescribed*

pseq_alloc_error
    *undescribed*

pseq_used
    *undescribed*

.. _`pulse_event`:

struct pulse_event
==================

.. c:type:: struct pulse_event

    describing pulses reported by PHY

.. _`pulse_event.definition`:

Definition
----------

.. code-block:: c

    struct pulse_event {
        u64 ts;
        u16 freq;
        u8 width;
        u8 rssi;
        bool chirp;
    }

.. _`pulse_event.members`:

Members
-------

ts
    pulse time stamp in us

freq
    channel frequency in MHz

width
    pulse duration in us

rssi
    rssi of radar event

chirp
    chirp detected in pulse

.. _`radar_detector_specs`:

struct radar_detector_specs
===========================

.. c:type:: struct radar_detector_specs

    detector specs for a radar pattern type

.. _`radar_detector_specs.definition`:

Definition
----------

.. code-block:: c

    struct radar_detector_specs {
        u8 type_id;
        u8 width_min;
        u8 width_max;
        u16 pri_min;
        u16 pri_max;
        u8 num_pri;
        u8 ppb;
        u8 ppb_thresh;
        u8 max_pri_tolerance;
        bool chirp;
    }

.. _`radar_detector_specs.members`:

Members
-------

type_id
    pattern type, as defined by regulatory

width_min
    minimum radar pulse width in [us]

width_max
    maximum radar pulse width in [us]

pri_min
    minimum pulse repetition interval in [us] (including tolerance)

pri_max
    minimum pri in [us] (including tolerance)

num_pri
    maximum number of different pri for this type

ppb
    pulses per bursts for this type

ppb_thresh
    number of pulses required to trigger detection

max_pri_tolerance
    pulse time stamp tolerance on both sides [us]

chirp
    chirp required for the radar pattern

.. _`dfs_pattern_detector`:

struct dfs_pattern_detector
===========================

.. c:type:: struct dfs_pattern_detector

    DFS pattern detector

.. _`dfs_pattern_detector.definition`:

Definition
----------

.. code-block:: c

    struct dfs_pattern_detector {
        void (*exit)(struct dfs_pattern_detector *dpd);
        bool (*set_dfs_domain)(struct dfs_pattern_detector *dpd,enum nl80211_dfs_regions region);
        bool (*add_pulse)(struct dfs_pattern_detector *dpd,struct pulse_event *pe);
        struct ath_dfs_pool_stats (*get_stats)(struct dfs_pattern_detector *dpd);
        enum nl80211_dfs_regions region;
        u8 num_radar_types;
        u64 last_pulse_ts;
        struct ath_common *common;
        const struct radar_detector_specs *radar_spec;
        struct list_head channel_detectors;
    }

.. _`dfs_pattern_detector.members`:

Members
-------

exit
    destructor

set_dfs_domain
    set DFS domain, resets detector lines upon domain changes

add_pulse
    add radar pulse to detector, returns true on detection

get_stats
    *undescribed*

region
    active DFS region, NL80211_DFS_UNSET until set

num_radar_types
    number of different radar types

last_pulse_ts
    time stamp of last valid pulse in usecs

common
    *undescribed*

radar_spec
    *undescribed*

channel_detectors
    list connecting channel_detector elements

.. _`dfs_pattern_detector_init`:

dfs_pattern_detector_init
=========================

.. c:function:: struct dfs_pattern_detector *dfs_pattern_detector_init(struct ath_common *common, enum nl80211_dfs_regions region)

    constructor for pattern detector class

    :param struct ath_common \*common:
        *undescribed*

    :param enum nl80211_dfs_regions region:
        *undescribed*

.. This file was automatic generated / don't edit.

