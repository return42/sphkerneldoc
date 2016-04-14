.. -*- coding: utf-8; mode: rst -*-

=======
dcbnl.h
=======

.. _`cee_pg`:

struct cee_pg
=============

.. c:type:: struct cee_pg

    CEE Priority-Group managed object



Definition
----------

.. code-block:: c

  struct cee_pg {
    __u8 willing;
    __u8 error;
    __u8 pg_en;
    __u8 tcs_supported;
    __u8 pg_bw[CEE_DCBX_MAX_PGS];
    __u8 prio_pg[CEE_DCBX_MAX_PGS];
  };



Members
-------

:``willing``:
    willing bit in the PG tlv

:``error``:
    error bit in the PG tlv

:``pg_en``:
    enable bit of the PG feature

:``tcs_supported``:
    number of traffic classes supported

:``pg_bw[CEE_DCBX_MAX_PGS]``:
    bandwidth percentage for each priority group

:``prio_pg[CEE_DCBX_MAX_PGS]``:
    priority to PG mapping indexed by priority



.. _`cee_pfc`:

struct cee_pfc
==============

.. c:type:: struct cee_pfc

    CEE PFC managed object



Definition
----------

.. code-block:: c

  struct cee_pfc {
    __u8 willing;
    __u8 error;
    __u8 pfc_en;
    __u8 tcs_supported;
  };



Members
-------

:``willing``:
    willing bit in the PFC tlv

:``error``:
    error bit in the PFC tlv

:``pfc_en``:
    bitmap indicating pfc enabled traffic classes

:``tcs_supported``:
    number of traffic classes supported



.. _`dcb_peer_app_info`:

struct dcb_peer_app_info
========================

.. c:type:: struct dcb_peer_app_info

    APP feature information sent by the peer



Definition
----------

.. code-block:: c

  struct dcb_peer_app_info {
    __u8 willing;
    __u8 error;
  };



Members
-------

:``willing``:
    willing bit in the peer APP tlv

:``error``:
    error bit in the peer APP tlv



Description
-----------

In addition to this information the full peer APP tlv also contains
a table of 'app_count' APP objects defined above.


.. _`dcbnl_commands`:

enum dcbnl_commands
===================

.. c:type:: enum dcbnl_commands

    supported DCB commands



Constants
---------

:``DCB_CMD_UNDEFINED``:
    unspecified command to catch errors

:``DCB_CMD_GSTATE``:
    request the state of DCB in the device

:``DCB_CMD_SSTATE``:
    set the state of DCB in the device

:``DCB_CMD_PGTX_GCFG``:
    request the priority group configuration for Tx

:``DCB_CMD_PGTX_SCFG``:
    set the priority group configuration for Tx

:``DCB_CMD_PGRX_GCFG``:
    request the priority group configuration for Rx

:``DCB_CMD_PGRX_SCFG``:
    set the priority group configuration for Rx

:``DCB_CMD_PFC_GCFG``:
    request the priority flow control configuration

:``DCB_CMD_PFC_SCFG``:
    set the priority flow control configuration

:``DCB_CMD_SET_ALL``:
    apply all changes to the underlying device

:``DCB_CMD_GPERM_HWADDR``:
    get the permanent MAC address of the underlying
    device.  Only useful when using bonding.

:``DCB_CMD_GCAP``:
    request the DCB capabilities of the device

:``DCB_CMD_GNUMTCS``:
    get the number of traffic classes currently supported

:``DCB_CMD_SNUMTCS``:
    set the number of traffic classes

:``DCB_CMD_PFC_GSTATE``:
    -- undescribed --

:``DCB_CMD_PFC_SSTATE``:
    -- undescribed --

:``DCB_CMD_BCN_GCFG``:
    -- undescribed --

:``DCB_CMD_BCN_SCFG``:
    -- undescribed --

:``DCB_CMD_GAPP``:
    get application protocol configuration

:``DCB_CMD_SAPP``:
    set application protocol configuration

:``DCB_CMD_IEEE_SET``:
    set IEEE 802.1Qaz configuration

:``DCB_CMD_IEEE_GET``:
    get IEEE 802.1Qaz configuration

:``DCB_CMD_GDCBX``:
    get DCBX engine configuration

:``DCB_CMD_SDCBX``:
    set DCBX engine configuration

:``DCB_CMD_GFEATCFG``:
    get DCBX features flags

:``DCB_CMD_SFEATCFG``:
    set DCBX features negotiation flags

:``DCB_CMD_CEE_GET``:
    get CEE aggregated configuration

:``DCB_CMD_IEEE_DEL``:
    delete IEEE 802.1Qaz configuration

:``__DCB_CMD_ENUM_MAX``:
    -- undescribed --

:``DCB_CMD_MAX``:
    -- undescribed --


.. _`dcbnl_attrs`:

enum dcbnl_attrs
================

.. c:type:: enum dcbnl_attrs

    DCB top-level netlink attributes



Constants
---------

:``DCB_ATTR_UNDEFINED``:
    unspecified attribute to catch errors

:``DCB_ATTR_IFNAME``:
    interface name of the underlying device (NLA_STRING)

:``DCB_ATTR_STATE``:
    enable state of DCB in the device (NLA_U8)

:``DCB_ATTR_PFC_STATE``:
    enable state of PFC in the device (NLA_U8)

:``DCB_ATTR_PFC_CFG``:
    priority flow control configuration (NLA_NESTED)

:``DCB_ATTR_NUM_TC``:
    number of traffic classes supported in the device (NLA_U8)

:``DCB_ATTR_PG_CFG``:
    priority group configuration (NLA_NESTED)

:``DCB_ATTR_SET_ALL``:
    bool to commit changes to hardware or not (NLA_U8)

:``DCB_ATTR_PERM_HWADDR``:
    MAC address of the physical device (NLA_NESTED)

:``DCB_ATTR_CAP``:
    DCB capabilities of the device (NLA_NESTED)

:``DCB_ATTR_NUMTCS``:
    number of traffic classes supported (NLA_NESTED)

:``DCB_ATTR_BCN``:
    backward congestion notification configuration (NLA_NESTED)

:``DCB_ATTR_APP``:
    -- undescribed --

:``DCB_ATTR_IEEE``:
    IEEE 802.1Qaz supported attributes (NLA_NESTED)

:``DCB_ATTR_DCBX``:
    DCBX engine configuration in the device (NLA_U8)

:``DCB_ATTR_FEATCFG``:
    DCBX features flags (NLA_NESTED)

:``DCB_ATTR_CEE``:
    CEE std supported attributes (NLA_NESTED)

:``__DCB_ATTR_ENUM_MAX``:
    -- undescribed --

:``DCB_ATTR_MAX``:
    -- undescribed --


.. _`ieee_attrs`:

enum ieee_attrs
===============

.. c:type:: enum ieee_attrs

    IEEE 802.1Qaz get/set attributes



Constants
---------

:``DCB_ATTR_IEEE_UNSPEC``:
    unspecified

:``DCB_ATTR_IEEE_ETS``:
    negotiated ETS configuration

:``DCB_ATTR_IEEE_PFC``:
    negotiated PFC configuration

:``DCB_ATTR_IEEE_APP_TABLE``:
    negotiated APP configuration

:``DCB_ATTR_IEEE_PEER_ETS``:
    peer ETS configuration - get only

:``DCB_ATTR_IEEE_PEER_PFC``:
    peer PFC configuration - get only

:``DCB_ATTR_IEEE_PEER_APP``:
    peer APP tlv - get only

:``DCB_ATTR_IEEE_MAXRATE``:
    -- undescribed --

:``DCB_ATTR_IEEE_QCN``:
    -- undescribed --

:``DCB_ATTR_IEEE_QCN_STATS``:
    -- undescribed --

:``__DCB_ATTR_IEEE_MAX``:
    -- undescribed --


.. _`cee_attrs`:

enum cee_attrs
==============

.. c:type:: enum cee_attrs

    CEE DCBX get attributes.



Constants
---------

:``DCB_ATTR_CEE_UNSPEC``:
    unspecified

:``DCB_ATTR_CEE_PEER_PG``:
    peer PG configuration - get only

:``DCB_ATTR_CEE_PEER_PFC``:
    peer PFC configuration - get only

:``DCB_ATTR_CEE_PEER_APP_TABLE``:
    peer APP tlv - get only

:``DCB_ATTR_CEE_TX_PG``:
    TX PG configuration (DCB_CMD_PGTX_GCFG)

:``DCB_ATTR_CEE_RX_PG``:
    RX PG configuration (DCB_CMD_PGRX_GCFG)

:``DCB_ATTR_CEE_PFC``:
    PFC configuration (DCB_CMD_PFC_GCFG)

:``DCB_ATTR_CEE_APP_TABLE``:
    APP configuration (multi DCB_CMD_GAPP)

:``DCB_ATTR_CEE_FEAT``:
    DCBX features flags (DCB_CMD_GFEATCFG)

:``__DCB_ATTR_CEE_MAX``:
    -- undescribed --


Description
-----------

An aggregated collection of the cee std negotiated parameters.


.. _`dcbnl_pfc_up_attrs`:

enum dcbnl_pfc_up_attrs
=======================

.. c:type:: enum dcbnl_pfc_up_attrs

    DCB Priority Flow Control user priority nested attrs



Constants
---------

:``DCB_PFC_UP_ATTR_UNDEFINED``:
    unspecified attribute to catch errors

:``DCB_PFC_UP_ATTR_0``:
    Priority Flow Control value for User Priority 0 (NLA_U8)

:``DCB_PFC_UP_ATTR_1``:
    Priority Flow Control value for User Priority 1 (NLA_U8)

:``DCB_PFC_UP_ATTR_2``:
    Priority Flow Control value for User Priority 2 (NLA_U8)

:``DCB_PFC_UP_ATTR_3``:
    Priority Flow Control value for User Priority 3 (NLA_U8)

:``DCB_PFC_UP_ATTR_4``:
    Priority Flow Control value for User Priority 4 (NLA_U8)

:``DCB_PFC_UP_ATTR_5``:
    Priority Flow Control value for User Priority 5 (NLA_U8)

:``DCB_PFC_UP_ATTR_6``:
    Priority Flow Control value for User Priority 6 (NLA_U8)

:``DCB_PFC_UP_ATTR_7``:
    Priority Flow Control value for User Priority 7 (NLA_U8)

:``DCB_PFC_UP_ATTR_ALL``:
    apply to all priority flow control attrs (NLA_FLAG)

:``__DCB_PFC_UP_ATTR_ENUM_MAX``:
    -- undescribed --

:``DCB_PFC_UP_ATTR_MAX``:
    highest attribute number currently defined


.. _`dcbnl_pg_attrs`:

enum dcbnl_pg_attrs
===================

.. c:type:: enum dcbnl_pg_attrs

    DCB Priority Group attributes



Constants
---------

:``DCB_PG_ATTR_UNDEFINED``:
    unspecified attribute to catch errors

:``DCB_PG_ATTR_TC_0``:
    Priority Group Traffic Class 0 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_1``:
    Priority Group Traffic Class 1 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_2``:
    Priority Group Traffic Class 2 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_3``:
    Priority Group Traffic Class 3 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_4``:
    Priority Group Traffic Class 4 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_5``:
    Priority Group Traffic Class 5 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_6``:
    Priority Group Traffic Class 6 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_7``:
    Priority Group Traffic Class 7 configuration (NLA_NESTED)

:``DCB_PG_ATTR_TC_MAX``:
    highest attribute number currently defined

:``DCB_PG_ATTR_TC_ALL``:
    apply to all traffic classes (NLA_NESTED)

:``DCB_PG_ATTR_BW_ID_0``:
    Percent of link bandwidth for Priority Group 0 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_1``:
    Percent of link bandwidth for Priority Group 1 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_2``:
    Percent of link bandwidth for Priority Group 2 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_3``:
    Percent of link bandwidth for Priority Group 3 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_4``:
    Percent of link bandwidth for Priority Group 4 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_5``:
    Percent of link bandwidth for Priority Group 5 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_6``:
    Percent of link bandwidth for Priority Group 6 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_7``:
    Percent of link bandwidth for Priority Group 7 (NLA_U8)

:``DCB_PG_ATTR_BW_ID_MAX``:
    highest attribute number currently defined

:``DCB_PG_ATTR_BW_ID_ALL``:
    apply to all priority groups (NLA_FLAG)

:``__DCB_PG_ATTR_ENUM_MAX``:
    -- undescribed --

:``DCB_PG_ATTR_MAX``:
    -- undescribed --


.. _`dcbnl_tc_attrs`:

enum dcbnl_tc_attrs
===================

.. c:type:: enum dcbnl_tc_attrs

    DCB Traffic Class attributes



Constants
---------

:``DCB_TC_ATTR_PARAM_UNDEFINED``:
    unspecified attribute to catch errors

:``DCB_TC_ATTR_PARAM_PGID``:
    (NLA_U8) Priority group the traffic class belongs to
    Valid values are:  0-7

:``DCB_TC_ATTR_PARAM_UP_MAPPING``:
    (NLA_U8) Traffic class to user priority map
    Some devices may not support changing the
    user priority map of a TC.

:``DCB_TC_ATTR_PARAM_STRICT_PRIO``:
    (NLA_U8) Strict priority setting
    0 - none
    1 - group strict
    2 - link strict

:``DCB_TC_ATTR_PARAM_BW_PCT``:
    optional - (NLA_U8) If supported by the device and
    not configured to use link strict priority,
    this is the percentage of bandwidth of the
    priority group this traffic class belongs to

:``DCB_TC_ATTR_PARAM_ALL``:
    (NLA_FLAG) all traffic class parameters

:``__DCB_TC_ATTR_PARAM_ENUM_MAX``:
    -- undescribed --

:``DCB_TC_ATTR_PARAM_MAX``:
    -- undescribed --


.. _`dcbnl_cap_attrs`:

enum dcbnl_cap_attrs
====================

.. c:type:: enum dcbnl_cap_attrs

    DCB Capability attributes



Constants
---------

:``DCB_CAP_ATTR_UNDEFINED``:
    unspecified attribute to catch errors

:``DCB_CAP_ATTR_ALL``:
    (NLA_FLAG) all capability parameters

:``DCB_CAP_ATTR_PG``:
    (NLA_U8) device supports Priority Groups

:``DCB_CAP_ATTR_PFC``:
    (NLA_U8) device supports Priority Flow Control

:``DCB_CAP_ATTR_UP2TC``:
    (NLA_U8) device supports user priority to
    traffic class mapping

:``DCB_CAP_ATTR_PG_TCS``:
    (NLA_U8) bitmap where each bit represents a
    number of traffic classes the device
    can be configured to use for Priority Groups

:``DCB_CAP_ATTR_PFC_TCS``:
    (NLA_U8) bitmap where each bit represents a
    number of traffic classes the device can be
    configured to use for Priority Flow Control

:``DCB_CAP_ATTR_GSP``:
    (NLA_U8) device supports group strict priority

:``DCB_CAP_ATTR_BCN``:
    (NLA_U8) device supports Backwards Congestion
    Notification

:``DCB_CAP_ATTR_DCBX``:
    (NLA_U8) device supports DCBX engine

:``__DCB_CAP_ATTR_ENUM_MAX``:
    -- undescribed --

:``DCB_CAP_ATTR_MAX``:
    -- undescribed --


.. _`dcb_cap_dcbx_host`:

DCB_CAP_DCBX_HOST
=================

.. c:function:: DCB_CAP_DCBX_HOST ()


.. _`dcbnl_numtcs_attrs`:

enum dcbnl_numtcs_attrs
=======================

.. c:type:: enum dcbnl_numtcs_attrs

    number of traffic classes



Constants
---------

:``DCB_NUMTCS_ATTR_UNDEFINED``:
    unspecified attribute to catch errors

:``DCB_NUMTCS_ATTR_ALL``:
    (NLA_FLAG) all traffic class attributes

:``DCB_NUMTCS_ATTR_PG``:
    (NLA_U8) number of traffic classes used for
    priority groups

:``DCB_NUMTCS_ATTR_PFC``:
    (NLA_U8) number of traffic classes which can
    support priority flow control

:``__DCB_NUMTCS_ATTR_ENUM_MAX``:
    -- undescribed --

:``DCB_NUMTCS_ATTR_MAX``:
    -- undescribed --


.. _`dcb_general_attr_values`:

enum dcb_general_attr_values
============================

.. c:type:: enum dcb_general_attr_values

    general DCB attribute values



Constants
---------

:``DCB_ATTR_VALUE_UNDEFINED``:
    -- undescribed --

