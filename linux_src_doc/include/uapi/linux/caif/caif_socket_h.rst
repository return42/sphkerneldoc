.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/caif/caif_socket.h

.. _`caif_link_selector`:

enum caif_link_selector
=======================

.. c:type:: enum caif_link_selector

    Physical Link Selection.

.. _`caif_link_selector.definition`:

Definition
----------

.. code-block:: c

    enum caif_link_selector {
        CAIF_LINK_HIGH_BANDW,
        CAIF_LINK_LOW_LATENCY
    };

.. _`caif_link_selector.constants`:

Constants
---------

CAIF_LINK_HIGH_BANDW
    Physical interface for high-bandwidth
    traffic.

CAIF_LINK_LOW_LATENCY
    Physical interface for low-latency
    traffic.

.. _`caif_link_selector.description`:

Description
-----------

CAIF Link Layers can register their link properties.
This enum is used for choosing between CAIF Link Layers when
setting up CAIF Channels when multiple CAIF Link Layers exists.

.. _`caif_channel_priority`:

enum caif_channel_priority
==========================

.. c:type:: enum caif_channel_priority

    CAIF channel priorities.

.. _`caif_channel_priority.definition`:

Definition
----------

.. code-block:: c

    enum caif_channel_priority {
        CAIF_PRIO_MIN,
        CAIF_PRIO_LOW,
        CAIF_PRIO_NORMAL,
        CAIF_PRIO_HIGH,
        CAIF_PRIO_MAX
    };

.. _`caif_channel_priority.constants`:

Constants
---------

CAIF_PRIO_MIN
    Min priority for a channel.

CAIF_PRIO_LOW
    Low-priority channel.

CAIF_PRIO_NORMAL
    Normal/default priority level.

CAIF_PRIO_HIGH
    High priority level

CAIF_PRIO_MAX
    Max priority for channel

.. _`caif_channel_priority.description`:

Description
-----------

Priority can be set on CAIF Channels in order to
prioritize between traffic on different CAIF Channels.
These priority levels are recommended, but the priority value
is not restricted to the values defined in this enum, any value
between CAIF_PRIO_MIN and CAIF_PRIO_MAX could be used.

.. _`caif_protocol_type`:

enum caif_protocol_type
=======================

.. c:type:: enum caif_protocol_type

    CAIF Channel type.

.. _`caif_protocol_type.definition`:

Definition
----------

.. code-block:: c

    enum caif_protocol_type {
        CAIFPROTO_AT,
        CAIFPROTO_DATAGRAM,
        CAIFPROTO_DATAGRAM_LOOP,
        CAIFPROTO_UTIL,
        CAIFPROTO_RFM,
        CAIFPROTO_DEBUG,
        _CAIFPROTO_MAX
    };

.. _`caif_protocol_type.constants`:

Constants
---------

CAIFPROTO_AT
    Classic AT channel.

CAIFPROTO_DATAGRAM
    Datagram channel.

CAIFPROTO_DATAGRAM_LOOP
    Datagram loopback channel, used for testing.

CAIFPROTO_UTIL
    Utility (Psock) channel.

CAIFPROTO_RFM
    Remote File Manager

CAIFPROTO_DEBUG
    Debug link

_CAIFPROTO_MAX
    *undescribed*

.. _`caif_protocol_type.description`:

Description
-----------

This enum defines the CAIF Channel type to be used. This defines
the service to connect to on the modem.

.. _`caif_at_type`:

enum caif_at_type
=================

.. c:type:: enum caif_at_type

    AT Service Endpoint

.. _`caif_at_type.definition`:

Definition
----------

.. code-block:: c

    enum caif_at_type {
        CAIF_ATTYPE_PLAIN
    };

.. _`caif_at_type.constants`:

Constants
---------

CAIF_ATTYPE_PLAIN
    Connects to a plain vanilla AT channel.

.. _`caif_debug_service`:

enum caif_debug_service
=======================

.. c:type:: enum caif_debug_service

    Debug Service Endpoint

.. _`caif_debug_service.definition`:

Definition
----------

.. code-block:: c

    enum caif_debug_service {
        CAIF_RADIO_DEBUG_SERVICE,
        CAIF_APP_DEBUG_SERVICE
    };

.. _`caif_debug_service.constants`:

Constants
---------

CAIF_RADIO_DEBUG_SERVICE
    Debug service on the Radio sub-system

CAIF_APP_DEBUG_SERVICE
    Debug for the applications sub-system

.. _`sockaddr_caif`:

struct sockaddr_caif
====================

.. c:type:: struct sockaddr_caif

    the sockaddr structure for CAIF sockets.

.. _`sockaddr_caif.definition`:

Definition
----------

.. code-block:: c

    struct sockaddr_caif {
        __kernel_sa_family_t family;
        union {
            struct {
                __u8 type;
            } at;
            struct {
                char service[16];
            } util;
            union {
                __u32 connection_id;
                __u8 nsapi;
            } dgm;
            struct {
                __u32 connection_id;
                char volume[16];
            } rfm;
            struct {
                __u8 type;
                __u8 service;
            } dbg;
        } u;
    }

.. _`sockaddr_caif.members`:

Members
-------

family
    Address family number, must be AF_CAIF.

u
    Union of address data 'switched' by family.
    :

u.at
    Applies when family = CAIFPROTO_AT.

u.at.type
    Type of AT link to set up (enum caif_at_type).

u.util
    Applies when family = CAIFPROTO_UTIL

u.util.service
    Utility service name.

u.dgm
    Applies when family = CAIFPROTO_DATAGRAM

u.dgm.connection_id
    Datagram connection id.

u.dgm.nsapi
    NSAPI of the PDP-Context.

u.rfm
    Applies when family = CAIFPROTO_RFM

u.rfm.connection_id
    Connection ID for RFM.

u.rfm.volume
    Volume to mount.

u.dbg
    Applies when family = CAIFPROTO_DEBUG.

u.dbg.type
    Type of debug connection to set up
    (caif_debug_type).

u.dbg.service
    Service sub-system to connect (caif_debug_service

at
    *undescribed*

type
    *undescribed*

util
    *undescribed*

service
    *undescribed*

dgm
    *undescribed*

connection_id
    *undescribed*

nsapi
    *undescribed*

rfm
    *undescribed*

connection_id
    *undescribed*

volume
    *undescribed*

dbg
    *undescribed*

type
    *undescribed*

service
    *undescribed*

.. _`sockaddr_caif.description`:

Description
-----------

This structure holds the connect parameters used for setting up a
CAIF Channel. It defines the service to connect to on the modem.

.. _`caif_socket_opts`:

enum caif_socket_opts
=====================

.. c:type:: enum caif_socket_opts

    CAIF option values for getsockopt and setsockopt.

.. _`caif_socket_opts.definition`:

Definition
----------

.. code-block:: c

    enum caif_socket_opts {
        CAIFSO_LINK_SELECT,
        CAIFSO_REQ_PARAM,
        CAIFSO_RSP_PARAM
    };

.. _`caif_socket_opts.constants`:

Constants
---------

CAIFSO_LINK_SELECT
    Selector used if multiple CAIF Link layers are
    available. Either a high bandwidth
    link can be selected (CAIF_LINK_HIGH_BANDW) or
    or a low latency link (CAIF_LINK_LOW_LATENCY).
    This option is of type \__u32.
    Alternatively SO_BINDTODEVICE can be used.

CAIFSO_REQ_PARAM
    Used to set the request parameters for a
    utility channel. (maximum 256 bytes). This
    option must be set before connecting.

CAIFSO_RSP_PARAM
    Gets the response parameters for a utility
    channel. (maximum 256 bytes). This option
    is valid after a successful connect.

.. _`caif_socket_opts.description`:

Description
-----------


This enum defines the CAIF Socket options to be used on a socket
of type PF_CAIF.

.. This file was automatic generated / don't edit.

