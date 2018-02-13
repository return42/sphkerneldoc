.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/batman_adv.h

.. _`batadv_tt_client_flags`:

enum batadv_tt_client_flags
===========================

.. c:type:: enum batadv_tt_client_flags

    TT client specific flags

.. _`batadv_tt_client_flags.definition`:

Definition
----------

.. code-block:: c

    enum batadv_tt_client_flags {
        BATADV_TT_CLIENT_DEL,
        BATADV_TT_CLIENT_ROAM,
        BATADV_TT_CLIENT_WIFI,
        BATADV_TT_CLIENT_ISOLA,
        BATADV_TT_CLIENT_NOPURGE,
        BATADV_TT_CLIENT_NEW,
        BATADV_TT_CLIENT_PENDING,
        BATADV_TT_CLIENT_TEMP
    };

.. _`batadv_tt_client_flags.constants`:

Constants
---------

BATADV_TT_CLIENT_DEL
    the client has to be deleted from the table

BATADV_TT_CLIENT_ROAM
    the client roamed to/from another node andthe new update telling its new real location has not been
    received/sent yet

BATADV_TT_CLIENT_WIFI
    this client is connected through a wifiinterface. This information is used by the "AP Isolation" feature

BATADV_TT_CLIENT_ISOLA
    this client is considered "isolated". Thisinformation is used by the Extended Isolation feature

BATADV_TT_CLIENT_NOPURGE
    this client should never be removed fromthe table

BATADV_TT_CLIENT_NEW
    this client has been added to the local tablebut has not been announced yet

BATADV_TT_CLIENT_PENDING
    this client is marked for removal but itis kept in the table for one more originator interval for consistency
    purposes

BATADV_TT_CLIENT_TEMP
    this global client has been detected to bepart of the network but no nnode has already announced it

.. _`batadv_tt_client_flags.description`:

Description
-----------

Bits from 0 to 7 are called \_remote flags\_ because they are sent on the wire.
Bits from 8 to 15 are called \_local flags\_ because they are used for local
computations only.

Bits from 4 to 7 - a subset of remote flags - are ensured to be in sync with
the other nodes in the network. To achieve this goal these flags are included
in the TT CRC computation.

.. _`batadv_nl_attrs`:

enum batadv_nl_attrs
====================

.. c:type:: enum batadv_nl_attrs

    batman-adv netlink attributes

.. _`batadv_nl_attrs.definition`:

Definition
----------

.. code-block:: c

    enum batadv_nl_attrs {
        BATADV_ATTR_UNSPEC,
        BATADV_ATTR_VERSION,
        BATADV_ATTR_ALGO_NAME,
        BATADV_ATTR_MESH_IFINDEX,
        BATADV_ATTR_MESH_IFNAME,
        BATADV_ATTR_MESH_ADDRESS,
        BATADV_ATTR_HARD_IFINDEX,
        BATADV_ATTR_HARD_IFNAME,
        BATADV_ATTR_HARD_ADDRESS,
        BATADV_ATTR_ORIG_ADDRESS,
        BATADV_ATTR_TPMETER_RESULT,
        BATADV_ATTR_TPMETER_TEST_TIME,
        BATADV_ATTR_TPMETER_BYTES,
        BATADV_ATTR_TPMETER_COOKIE,
        BATADV_ATTR_PAD,
        BATADV_ATTR_ACTIVE,
        BATADV_ATTR_TT_ADDRESS,
        BATADV_ATTR_TT_TTVN,
        BATADV_ATTR_TT_LAST_TTVN,
        BATADV_ATTR_TT_CRC32,
        BATADV_ATTR_TT_VID,
        BATADV_ATTR_TT_FLAGS,
        BATADV_ATTR_FLAG_BEST,
        BATADV_ATTR_LAST_SEEN_MSECS,
        BATADV_ATTR_NEIGH_ADDRESS,
        BATADV_ATTR_TQ,
        BATADV_ATTR_THROUGHPUT,
        BATADV_ATTR_BANDWIDTH_UP,
        BATADV_ATTR_BANDWIDTH_DOWN,
        BATADV_ATTR_ROUTER,
        BATADV_ATTR_BLA_OWN,
        BATADV_ATTR_BLA_ADDRESS,
        BATADV_ATTR_BLA_VID,
        BATADV_ATTR_BLA_BACKBONE,
        BATADV_ATTR_BLA_CRC,
        __BATADV_ATTR_AFTER_LAST,
        NUM_BATADV_ATTR,
        BATADV_ATTR_MAX
    };

.. _`batadv_nl_attrs.constants`:

Constants
---------

BATADV_ATTR_UNSPEC
    unspecified attribute to catch errors

BATADV_ATTR_VERSION
    batman-adv version string

BATADV_ATTR_ALGO_NAME
    name of routing algorithm

BATADV_ATTR_MESH_IFINDEX
    index of the batman-adv interface

BATADV_ATTR_MESH_IFNAME
    name of the batman-adv interface

BATADV_ATTR_MESH_ADDRESS
    mac address of the batman-adv interface

BATADV_ATTR_HARD_IFINDEX
    index of the non-batman-adv interface

BATADV_ATTR_HARD_IFNAME
    name of the non-batman-adv interface

BATADV_ATTR_HARD_ADDRESS
    mac address of the non-batman-advinterface

BATADV_ATTR_ORIG_ADDRESS
    originator mac address

BATADV_ATTR_TPMETER_RESULT
    result of run (seebatadv_tp_meter_status)

BATADV_ATTR_TPMETER_TEST_TIME
    time (msec) the run took

BATADV_ATTR_TPMETER_BYTES
    amount of acked bytes during run

BATADV_ATTR_TPMETER_COOKIE
    session cookie to match tp_meter session

BATADV_ATTR_PAD
    attribute used for padding for 64-bit alignment

BATADV_ATTR_ACTIVE
    Flag indicating if the hard interface is active

BATADV_ATTR_TT_ADDRESS
    Client MAC address

BATADV_ATTR_TT_TTVN
    Translation table version

BATADV_ATTR_TT_LAST_TTVN
    Previous translation table version

BATADV_ATTR_TT_CRC32
    CRC32 over translation table

BATADV_ATTR_TT_VID
    VLAN ID

BATADV_ATTR_TT_FLAGS
    Translation table client flags

BATADV_ATTR_FLAG_BEST
    Flags indicating entry is the best

BATADV_ATTR_LAST_SEEN_MSECS
    Time in milliseconds since last seen

BATADV_ATTR_NEIGH_ADDRESS
    Neighbour MAC address

BATADV_ATTR_TQ
    TQ to neighbour

BATADV_ATTR_THROUGHPUT
    Estimated throughput to Neighbour

BATADV_ATTR_BANDWIDTH_UP
    Reported uplink bandwidth

BATADV_ATTR_BANDWIDTH_DOWN
    Reported downlink bandwidth

BATADV_ATTR_ROUTER
    Gateway router MAC address

BATADV_ATTR_BLA_OWN
    Flag indicating own originator

BATADV_ATTR_BLA_ADDRESS
    Bridge loop avoidance claim MAC address

BATADV_ATTR_BLA_VID
    BLA VLAN ID

BATADV_ATTR_BLA_BACKBONE
    BLA gateway originator MAC address

BATADV_ATTR_BLA_CRC
    BLA CRC

\__BATADV_ATTR_AFTER_LAST
    internal use

NUM_BATADV_ATTR
    total number of batadv_nl_attrs available

BATADV_ATTR_MAX
    highest attribute number currently defined

.. _`batadv_nl_commands`:

enum batadv_nl_commands
=======================

.. c:type:: enum batadv_nl_commands

    supported batman-adv netlink commands

.. _`batadv_nl_commands.definition`:

Definition
----------

.. code-block:: c

    enum batadv_nl_commands {
        BATADV_CMD_UNSPEC,
        BATADV_CMD_GET_MESH_INFO,
        BATADV_CMD_TP_METER,
        BATADV_CMD_TP_METER_CANCEL,
        BATADV_CMD_GET_ROUTING_ALGOS,
        BATADV_CMD_GET_HARDIFS,
        BATADV_CMD_GET_TRANSTABLE_LOCAL,
        BATADV_CMD_GET_TRANSTABLE_GLOBAL,
        BATADV_CMD_GET_ORIGINATORS,
        BATADV_CMD_GET_NEIGHBORS,
        BATADV_CMD_GET_GATEWAYS,
        BATADV_CMD_GET_BLA_CLAIM,
        BATADV_CMD_GET_BLA_BACKBONE,
        __BATADV_CMD_AFTER_LAST,
        BATADV_CMD_MAX
    };

.. _`batadv_nl_commands.constants`:

Constants
---------

BATADV_CMD_UNSPEC
    unspecified command to catch errors

BATADV_CMD_GET_MESH_INFO
    Query basic information about batman-advdevice

BATADV_CMD_TP_METER
    Start a tp meter session

BATADV_CMD_TP_METER_CANCEL
    Cancel a tp meter session

BATADV_CMD_GET_ROUTING_ALGOS
    Query the list of routing algorithms.

BATADV_CMD_GET_HARDIFS
    Query list of hard interfaces

BATADV_CMD_GET_TRANSTABLE_LOCAL
    Query list of local translations

BATADV_CMD_GET_TRANSTABLE_GLOBAL
    Query list of global translations

BATADV_CMD_GET_ORIGINATORS
    Query list of originators

BATADV_CMD_GET_NEIGHBORS
    Query list of neighbours

BATADV_CMD_GET_GATEWAYS
    Query list of gateways

BATADV_CMD_GET_BLA_CLAIM
    Query list of bridge loop avoidance claims

BATADV_CMD_GET_BLA_BACKBONE
    Query list of bridge loop avoidancebackbones

\__BATADV_CMD_AFTER_LAST
    internal use

BATADV_CMD_MAX
    highest used command number

.. _`batadv_tp_meter_reason`:

enum batadv_tp_meter_reason
===========================

.. c:type:: enum batadv_tp_meter_reason

    reason of a tp meter test run stop

.. _`batadv_tp_meter_reason.definition`:

Definition
----------

.. code-block:: c

    enum batadv_tp_meter_reason {
        BATADV_TP_REASON_COMPLETE,
        BATADV_TP_REASON_CANCEL,
        BATADV_TP_REASON_DST_UNREACHABLE,
        BATADV_TP_REASON_RESEND_LIMIT,
        BATADV_TP_REASON_ALREADY_ONGOING,
        BATADV_TP_REASON_MEMORY_ERROR,
        BATADV_TP_REASON_CANT_SEND,
        BATADV_TP_REASON_TOO_MANY
    };

.. _`batadv_tp_meter_reason.constants`:

Constants
---------

BATADV_TP_REASON_COMPLETE
    sender finished tp run

BATADV_TP_REASON_CANCEL
    sender was stopped during run

BATADV_TP_REASON_DST_UNREACHABLE
    receiver could not be reached ordidn't answer

BATADV_TP_REASON_RESEND_LIMIT
    (unused) sender retry reached limit

BATADV_TP_REASON_ALREADY_ONGOING
    test to or from the same nodealready ongoing

BATADV_TP_REASON_MEMORY_ERROR
    test was stopped due to low memory

BATADV_TP_REASON_CANT_SEND
    failed to send via outgoing interface

BATADV_TP_REASON_TOO_MANY
    too many ongoing sessions

.. This file was automatic generated / don't edit.

