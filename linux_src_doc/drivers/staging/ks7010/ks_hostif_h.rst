.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ks7010/ks_hostif.h

.. _`hostif_ps_adhoc_set_request_t`:

struct hostif_ps_adhoc_set_request_t
====================================

.. c:type:: struct hostif_ps_adhoc_set_request_t

    pseudo adhoc mode

.. _`hostif_ps_adhoc_set_request_t.definition`:

Definition
----------

.. code-block:: c

    struct hostif_ps_adhoc_set_request_t {
        struct hostif_hdr header;
        u16 phy_type;
    #define D_11B_ONLY_MODE 0
    #define D_11G_ONLY_MODE 1
    #define D_11BG_COMPATIBLE_MODE 2
    #define D_11A_ONLY_MODE 3
        u16 cts_mode;
    #define CTS_MODE_FALSE 0
    #define CTS_MODE_TRUE 1
        u16 channel;
        struct rate_set16_t rate_set;
        u16 capability;
        u16 scan_type;
    }

.. _`hostif_ps_adhoc_set_request_t.members`:

Members
-------

header
    *undescribed*

phy_type
    *undescribed*

cts_mode
    *undescribed*

channel
    *undescribed*

rate_set
    *undescribed*

capability
    bit5  : preamble
    bit6  : pbcc - Not supported always 0
    bit10 : ShortSlotTime
    bit13 : DSSS-OFDM - Not supported always 0

scan_type
    *undescribed*

.. _`hostif_infrastructure_set_request_t`:

struct hostif_infrastructure_set_request_t
==========================================

.. c:type:: struct hostif_infrastructure_set_request_t


.. _`hostif_infrastructure_set_request_t.definition`:

Definition
----------

.. code-block:: c

    struct hostif_infrastructure_set_request_t {
        struct hostif_hdr header;
        u16 phy_type;
        u16 cts_mode;
        struct rate_set16_t rate_set;
        struct ssid_t ssid;
        u16 capability;
        u16 beacon_lost_count;
        u16 auth_type;
    #define AUTH_TYPE_OPEN_SYSTEM 0
    #define AUTH_TYPE_SHARED_KEY 1
        struct channel_list_t channel_list;
        u16 scan_type;
    }

.. _`hostif_infrastructure_set_request_t.members`:

Members
-------

header
    *undescribed*

phy_type
    *undescribed*

cts_mode
    *undescribed*

rate_set
    *undescribed*

ssid
    *undescribed*

capability
    bit5  : preamble
    bit6  : pbcc - Not supported always 0
    bit10 : ShortSlotTime
    bit13 : DSSS-OFDM - Not supported always 0

beacon_lost_count
    *undescribed*

auth_type
    *undescribed*

channel_list
    *undescribed*

scan_type
    *undescribed*

.. _`hostif_infrastructure_set2_request_t`:

struct hostif_infrastructure_set2_request_t
===========================================

.. c:type:: struct hostif_infrastructure_set2_request_t


.. _`hostif_infrastructure_set2_request_t.definition`:

Definition
----------

.. code-block:: c

    struct hostif_infrastructure_set2_request_t {
        struct hostif_hdr header;
        u16 phy_type;
        u16 cts_mode;
        struct rate_set16_t rate_set;
        struct ssid_t ssid;
        u16 capability;
        u16 beacon_lost_count;
        u16 auth_type;
    #define AUTH_TYPE_OPEN_SYSTEM 0
    #define AUTH_TYPE_SHARED_KEY 1
        struct channel_list_t channel_list;
        u16 scan_type;
        u8 bssid[ETH_ALEN];
    }

.. _`hostif_infrastructure_set2_request_t.members`:

Members
-------

header
    *undescribed*

phy_type
    *undescribed*

cts_mode
    *undescribed*

rate_set
    *undescribed*

ssid
    *undescribed*

capability
    bit5  : preamble
    bit6  : pbcc - Not supported always 0
    bit10 : ShortSlotTime
    bit13 : DSSS-OFDM - Not supported always 0

beacon_lost_count
    *undescribed*

auth_type
    *undescribed*

channel_list
    *undescribed*

scan_type
    *undescribed*

.. _`hostif_adhoc_set_request_t`:

struct hostif_adhoc_set_request_t
=================================

.. c:type:: struct hostif_adhoc_set_request_t


.. _`hostif_adhoc_set_request_t.definition`:

Definition
----------

.. code-block:: c

    struct hostif_adhoc_set_request_t {
        struct hostif_hdr header;
        u16 phy_type;
        u16 cts_mode;
        u16 channel;
        struct rate_set16_t rate_set;
        struct ssid_t ssid;
        u16 capability;
        u16 scan_type;
    }

.. _`hostif_adhoc_set_request_t.members`:

Members
-------

header
    *undescribed*

phy_type
    *undescribed*

cts_mode
    *undescribed*

channel
    *undescribed*

rate_set
    *undescribed*

ssid
    *undescribed*

capability
    bit5  : preamble
    bit6  : pbcc - Not supported always 0
    bit10 : ShortSlotTime
    bit13 : DSSS-OFDM - Not supported always 0

scan_type
    *undescribed*

.. _`hostif_adhoc_set2_request_t`:

struct hostif_adhoc_set2_request_t
==================================

.. c:type:: struct hostif_adhoc_set2_request_t


.. _`hostif_adhoc_set2_request_t.definition`:

Definition
----------

.. code-block:: c

    struct hostif_adhoc_set2_request_t {
        struct hostif_hdr header;
        u16 phy_type;
        u16 cts_mode;
        u16 reserved;
        struct rate_set16_t rate_set;
        struct ssid_t ssid;
        u16 capability;
        u16 scan_type;
        struct channel_list_t channel_list;
        u8 bssid[ETH_ALEN];
    }

.. _`hostif_adhoc_set2_request_t.members`:

Members
-------

header
    *undescribed*

phy_type
    *undescribed*

cts_mode
    *undescribed*

reserved
    *undescribed*

rate_set
    *undescribed*

ssid
    *undescribed*

capability
    bit5  : preamble
    bit6  : pbcc - Not supported always 0
    bit10 : ShortSlotTime
    bit13 : DSSS-OFDM - Not supported always 0

scan_type
    *undescribed*

channel_list
    *undescribed*

.. This file was automatic generated / don't edit.

