.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/dfs_pattern_detector.c

.. _`radar_types`:

struct radar_types
==================

.. c:type:: struct radar_types

    contains array of patterns defined for one DFS domain

.. _`radar_types.definition`:

Definition
----------

.. code-block:: c

    struct radar_types {
        enum nl80211_dfs_regions region;
        u32 num_radar_types;
        const struct radar_detector_specs *radar_types;
    }

.. _`radar_types.members`:

Members
-------

region
    *undescribed*

num_radar_types
    number of radar types to follow

radar_types
    radar types array

.. _`get_dfs_domain_radar_types`:

get_dfs_domain_radar_types
==========================

.. c:function:: const struct radar_types *get_dfs_domain_radar_types(enum nl80211_dfs_regions region)

    get radar types for a given DFS domain \ ``param``\  domain DFS domain \ ``return``\  radar_types ptr on success, NULL if DFS domain is not supported

    :param enum nl80211_dfs_regions region:
        *undescribed*

.. _`channel_detector`:

struct channel_detector
=======================

.. c:type:: struct channel_detector

    detector elements for a DFS channel

.. _`channel_detector.definition`:

Definition
----------

.. code-block:: c

    struct channel_detector {
        struct list_head head;
        u16 freq;
        struct pri_detector **detectors;
    }

.. _`channel_detector.members`:

Members
-------

head
    list_head

freq
    frequency for this channel detector in MHz

detectors
    array of dynamically created detector elements for this freq

.. _`channel_detector.description`:

Description
-----------

Channel detectors are required to provide multi-channel DFS detection, e.g.
to support off-channel scanning. A pattern detector has a list of channels
radar pulses have been reported for in the past.

.. _`channel_detector_get`:

channel_detector_get
====================

.. c:function:: struct channel_detector *channel_detector_get(struct dfs_pattern_detector *dpd, u16 freq)

    get channel detector for given frequency \ ``param``\  dpd instance pointer \ ``param``\  freq frequency in MHz \ ``return``\  pointer to channel detector on success, NULL otherwise

    :param struct dfs_pattern_detector \*dpd:
        *undescribed*

    :param u16 freq:
        *undescribed*

.. _`channel_detector_get.description`:

Description
-----------

Return existing channel detector for the given frequency or return a
newly create one.

.. This file was automatic generated / don't edit.

