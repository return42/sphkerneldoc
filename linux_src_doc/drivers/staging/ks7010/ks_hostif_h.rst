.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ks7010/ks_hostif.h

.. _`mib_attribute`:

enum mib_attribute
==================

.. c:type:: enum mib_attribute

    Management Information Base attribute Attribute value used for accessing and updating MIB

.. _`mib_attribute.definition`:

Definition
----------

.. code-block:: c

    enum mib_attribute {
        DOT11_MAC_ADDRESS,
        DOT11_PRODUCT_VERSION,
        DOT11_RTS_THRESHOLD,
        DOT11_FRAGMENTATION_THRESHOLD,
        DOT11_PRIVACY_INVOKED,
        DOT11_WEP_DEFAULT_KEY_ID,
        DOT11_WEP_DEFAULT_KEY_VALUE1,
        DOT11_WEP_DEFAULT_KEY_VALUE2,
        DOT11_WEP_DEFAULT_KEY_VALUE3,
        DOT11_WEP_DEFAULT_KEY_VALUE4,
        DOT11_WEP_LIST,
        DOT11_DESIRED_SSID,
        DOT11_CURRENT_CHANNEL,
        DOT11_OPERATION_RATE_SET,
        LOCAL_AP_SEARCH_INTERVAL,
        LOCAL_CURRENTADDRESS,
        LOCAL_MULTICAST_ADDRESS,
        LOCAL_MULTICAST_FILTER,
        LOCAL_SEARCHED_AP_LIST,
        LOCAL_LINK_AP_STATUS,
        LOCAL_PACKET_STATISTICS,
        LOCAL_AP_SCAN_LIST_TYPE_SET,
        DOT11_RSN_ENABLED,
        LOCAL_RSN_MODE,
        DOT11_RSN_CONFIG_MULTICAST_CIPHER,
        DOT11_RSN_CONFIG_UNICAST_CIPHER,
        DOT11_RSN_CONFIG_AUTH_SUITE,
        DOT11_RSN_CONFIG_VERSION,
        LOCAL_RSN_CONFIG_ALL,
        DOT11_PMK_TSC,
        DOT11_GMK1_TSC,
        DOT11_GMK2_TSC,
        DOT11_GMK3_TSC,
        LOCAL_PMK,
        LOCAL_REGION,
        LOCAL_WPS_ENABLE,
        LOCAL_WPS_PROBE_REQ,
        LOCAL_GAIN,
        LOCAL_EEPROM_SUM
    };

.. _`mib_attribute.constants`:

Constants
---------

DOT11_MAC_ADDRESS
    MAC Address (R)

DOT11_PRODUCT_VERSION
    FirmWare Version (R)

DOT11_RTS_THRESHOLD
    RTS Threshold (R/W)

DOT11_FRAGMENTATION_THRESHOLD
    Fragment Threshold (R/W)

DOT11_PRIVACY_INVOKED
    WEP ON/OFF (W)

DOT11_WEP_DEFAULT_KEY_ID
    WEP Index (W)

DOT11_WEP_DEFAULT_KEY_VALUE1
    WEP Key#1(TKIP AES: PairwiseTemporalKey) (W)

DOT11_WEP_DEFAULT_KEY_VALUE2
    WEP Key#2(TKIP AES: GroupKey1) (W)

DOT11_WEP_DEFAULT_KEY_VALUE3
    WEP Key#3(TKIP AES: GroupKey2) (W)

DOT11_WEP_DEFAULT_KEY_VALUE4
    WEP Key#4 (W)

DOT11_WEP_LIST
    WEP LIST

DOT11_DESIRED_SSID
    SSID

DOT11_CURRENT_CHANNEL
    channel set

DOT11_OPERATION_RATE_SET
    rate set

LOCAL_AP_SEARCH_INTERVAL
    AP search interval (R/W)

LOCAL_CURRENTADDRESS
    MAC Address change (W)

LOCAL_MULTICAST_ADDRESS
    Multicast Address (W)

LOCAL_MULTICAST_FILTER
    Multicast Address Filter enable/disable (W)

LOCAL_SEARCHED_AP_LIST
    AP list (R)

LOCAL_LINK_AP_STATUS
    Link AP status (R)

LOCAL_PACKET_STATISTICS
    tx,rx packets statistics

LOCAL_AP_SCAN_LIST_TYPE_SET
    AP_SCAN_LIST_TYPE

DOT11_RSN_ENABLED
    WPA enable/disable (W)

LOCAL_RSN_MODE
    RSN mode WPA/WPA2 (W)

DOT11_RSN_CONFIG_MULTICAST_CIPHER
    GroupKeyCipherSuite (W)

DOT11_RSN_CONFIG_UNICAST_CIPHER
    PairwiseKeyCipherSuite (W)

DOT11_RSN_CONFIG_AUTH_SUITE
    AuthenticationKeyManagementSuite (W)

DOT11_RSN_CONFIG_VERSION
    RSN version (W)

LOCAL_RSN_CONFIG_ALL
    RSN CONFIG ALL (W)

DOT11_PMK_TSC
    PMK_TSC (W)

DOT11_GMK1_TSC
    GMK1_TSC (W)

DOT11_GMK2_TSC
    GMK2_TSC (W)

DOT11_GMK3_TSC
    GMK3_TSC

LOCAL_PMK
    Pairwise Master Key cache (W)

LOCAL_REGION
    Region setting

LOCAL_WPS_ENABLE
    WiFi Protected Setup

LOCAL_WPS_PROBE_REQ
    WPS Probe Request

LOCAL_GAIN
    Carrer sense threshold for demo ato show

LOCAL_EEPROM_SUM
    EEPROM checksum information

.. _`mib_data_type`:

enum mib_data_type
==================

.. c:type:: enum mib_data_type

    Message Information Base data type.

.. _`mib_data_type.definition`:

Definition
----------

.. code-block:: c

    enum mib_data_type {
        MIB_VALUE_TYPE_NULL,
        MIB_VALUE_TYPE_INT,
        MIB_VALUE_TYPE_BOOL,
        MIB_VALUE_TYPE_COUNT32,
        MIB_VALUE_TYPE_OSTRING
    };

.. _`mib_data_type.constants`:

Constants
---------

MIB_VALUE_TYPE_NULL
    NULL type

MIB_VALUE_TYPE_INT
    INTEGER type

MIB_VALUE_TYPE_BOOL
    BOOL type

MIB_VALUE_TYPE_COUNT32
    unused

MIB_VALUE_TYPE_OSTRING
    Chunk of memory

.. _`hostif_ps_adhoc_set_request`:

struct hostif_ps_adhoc_set_request
==================================

.. c:type:: struct hostif_ps_adhoc_set_request

    pseudo adhoc mode

.. _`hostif_ps_adhoc_set_request.definition`:

Definition
----------

.. code-block:: c

    struct hostif_ps_adhoc_set_request {
        struct hostif_hdr header;
        struct hostif_request request;
        __le16 channel;
    }

.. _`hostif_ps_adhoc_set_request.members`:

Members
-------

header
    *undescribed*

request
    *undescribed*

channel
    *undescribed*

.. _`hostif_infrastructure_set_request`:

struct hostif_infrastructure_set_request
========================================

.. c:type:: struct hostif_infrastructure_set_request


.. _`hostif_infrastructure_set_request.definition`:

Definition
----------

.. code-block:: c

    struct hostif_infrastructure_set_request {
        struct hostif_hdr header;
        struct hostif_request request;
        struct ssid ssid;
        __le16 beacon_lost_count;
        __le16 auth_type;
        struct channel_list channel_list;
        u8 bssid[ETH_ALEN];
    }

.. _`hostif_infrastructure_set_request.members`:

Members
-------

header
    *undescribed*

request
    *undescribed*

ssid
    *undescribed*

beacon_lost_count
    *undescribed*

auth_type
    *undescribed*

channel_list
    *undescribed*

bssid
    *undescribed*

.. _`hostif_adhoc_set_request`:

struct hostif_adhoc_set_request
===============================

.. c:type:: struct hostif_adhoc_set_request


.. _`hostif_adhoc_set_request.definition`:

Definition
----------

.. code-block:: c

    struct hostif_adhoc_set_request {
        struct hostif_hdr header;
        struct hostif_request request;
        struct ssid ssid;
        __le16 channel;
    }

.. _`hostif_adhoc_set_request.members`:

Members
-------

header
    *undescribed*

request
    *undescribed*

ssid
    *undescribed*

channel
    *undescribed*

.. _`hostif_adhoc_set2_request`:

struct hostif_adhoc_set2_request
================================

.. c:type:: struct hostif_adhoc_set2_request


.. _`hostif_adhoc_set2_request.definition`:

Definition
----------

.. code-block:: c

    struct hostif_adhoc_set2_request {
        struct hostif_hdr header;
        struct hostif_request request;
        __le16 reserved;
        struct ssid ssid;
        struct channel_list channel_list;
        u8 bssid[ETH_ALEN];
    }

.. _`hostif_adhoc_set2_request.members`:

Members
-------

header
    *undescribed*

request
    *undescribed*

reserved
    *undescribed*

ssid
    *undescribed*

channel_list
    *undescribed*

bssid
    *undescribed*

.. This file was automatic generated / don't edit.

