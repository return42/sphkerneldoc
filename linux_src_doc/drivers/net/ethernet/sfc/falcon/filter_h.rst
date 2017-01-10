.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/filter.h

.. _`ef4_filter_match_flags`:

enum ef4_filter_match_flags
===========================

.. c:type:: enum ef4_filter_match_flags

    Flags for hardware filter match type

.. _`ef4_filter_match_flags.definition`:

Definition
----------

.. code-block:: c

    enum ef4_filter_match_flags {
        EF4_FILTER_MATCH_REM_HOST,
        EF4_FILTER_MATCH_LOC_HOST,
        EF4_FILTER_MATCH_REM_MAC,
        EF4_FILTER_MATCH_REM_PORT,
        EF4_FILTER_MATCH_LOC_MAC,
        EF4_FILTER_MATCH_LOC_PORT,
        EF4_FILTER_MATCH_ETHER_TYPE,
        EF4_FILTER_MATCH_INNER_VID,
        EF4_FILTER_MATCH_OUTER_VID,
        EF4_FILTER_MATCH_IP_PROTO,
        EF4_FILTER_MATCH_LOC_MAC_IG
    };

.. _`ef4_filter_match_flags.constants`:

Constants
---------

EF4_FILTER_MATCH_REM_HOST
    Match by remote IP host address

EF4_FILTER_MATCH_LOC_HOST
    Match by local IP host address

EF4_FILTER_MATCH_REM_MAC
    Match by remote MAC address

EF4_FILTER_MATCH_REM_PORT
    Match by remote TCP/UDP port

EF4_FILTER_MATCH_LOC_MAC
    Match by local MAC address

EF4_FILTER_MATCH_LOC_PORT
    Match by local TCP/UDP port

EF4_FILTER_MATCH_ETHER_TYPE
    Match by Ether-type

EF4_FILTER_MATCH_INNER_VID
    Match by inner VLAN ID

EF4_FILTER_MATCH_OUTER_VID
    Match by outer VLAN ID

EF4_FILTER_MATCH_IP_PROTO
    Match by IP transport protocol

EF4_FILTER_MATCH_LOC_MAC_IG
    Match by local MAC address I/G bit.
    Used for RX default unicast and multicast/broadcast filters.

.. _`ef4_filter_match_flags.description`:

Description
-----------

Only some combinations are supported, depending on NIC type:

- Falcon supports RX filters matching by {TCP,UDP}/IPv4 4-tuple or
local 2-tuple (only implemented for Falcon B0)

- Siena supports RX and TX filters matching by {TCP,UDP}/IPv4 4-tuple
or local 2-tuple, or local MAC with or without outer VID, and RX
default filters

- Huntington supports filter matching controlled by firmware, potentially
using {TCP,UDP}/IPv{4,6} 4-tuple or local 2-tuple, local MAC or I/G bit,
with or without outer and inner VID

.. _`ef4_filter_priority`:

enum ef4_filter_priority
========================

.. c:type:: enum ef4_filter_priority

    priority of a hardware filter specification

.. _`ef4_filter_priority.definition`:

Definition
----------

.. code-block:: c

    enum ef4_filter_priority {
        EF4_FILTER_PRI_HINT,
        EF4_FILTER_PRI_AUTO,
        EF4_FILTER_PRI_MANUAL,
        EF4_FILTER_PRI_REQUIRED
    };

.. _`ef4_filter_priority.constants`:

Constants
---------

EF4_FILTER_PRI_HINT
    Performance hint

EF4_FILTER_PRI_AUTO
    Automatic filter based on device address list
    or hardware requirements.  This may only be used by the filter
    implementation for each NIC type.

EF4_FILTER_PRI_MANUAL
    Manually configured filter

EF4_FILTER_PRI_REQUIRED
    Required for correct behaviour (user-level
    networking and SR-IOV)

.. _`ef4_filter_flags`:

enum ef4_filter_flags
=====================

.. c:type:: enum ef4_filter_flags

    flags for hardware filter specifications

.. _`ef4_filter_flags.definition`:

Definition
----------

.. code-block:: c

    enum ef4_filter_flags {
        EF4_FILTER_FLAG_RX_RSS,
        EF4_FILTER_FLAG_RX_SCATTER,
        EF4_FILTER_FLAG_RX_OVER_AUTO,
        EF4_FILTER_FLAG_RX,
        EF4_FILTER_FLAG_TX
    };

.. _`ef4_filter_flags.constants`:

Constants
---------

EF4_FILTER_FLAG_RX_RSS
    Use RSS to spread across multiple queues.
    By default, matching packets will be delivered only to the
    specified queue. If this flag is set, they will be delivered
    to a range of queues offset from the specified queue number
    according to the indirection table.

EF4_FILTER_FLAG_RX_SCATTER
    Enable DMA scatter on the receiving
    queue.

EF4_FILTER_FLAG_RX_OVER_AUTO
    Indicates a filter that is
    overriding an automatic filter (priority
    \ ``EF4_FILTER_PRI_AUTO``\ ).  This may only be set by the filter
    implementation for each type.  A removal request will restore
    the automatic filter in its place.

EF4_FILTER_FLAG_RX
    Filter is for RX

EF4_FILTER_FLAG_TX
    Filter is for TX

.. _`ef4_filter_spec`:

struct ef4_filter_spec
======================

.. c:type:: struct ef4_filter_spec

    specification for a hardware filter

.. _`ef4_filter_spec.definition`:

Definition
----------

.. code-block:: c

    struct ef4_filter_spec {
        u32 match_flags:12;
        u32 priority:2;
        u32 flags:6;
        u32 dmaq_id:12;
        u32 rss_context;
        __be16 outer_vid;
        __be16 inner_vid;
        u8 loc_mac[ETH_ALEN];
        u8 rem_mac[ETH_ALEN];
        __be16 ether_type;
        u8 ip_proto;
        __be32 loc_host[4];
        __be32 rem_host[4];
        __be16 loc_port;
        __be16 rem_port;
    }

.. _`ef4_filter_spec.members`:

Members
-------

match_flags
    Match type flags, from \ :c:type:`enum ef4_filter_match_flags <ef4_filter_match_flags>`\ 

priority
    Priority of the filter, from \ :c:type:`enum ef4_filter_priority <ef4_filter_priority>`\ 

flags
    Miscellaneous flags, from \ :c:type:`enum ef4_filter_flags <ef4_filter_flags>`\ 

dmaq_id
    Source/target queue index, or \ ``EF4_FILTER_RX_DMAQ_ID_DROP``\  for
    an RX drop filter

rss_context
    RSS context to use, if \ ``EF4_FILTER_FLAG_RX_RSS``\  is set

outer_vid
    Outer VLAN ID to match, if \ ``EF4_FILTER_MATCH_OUTER_VID``\  is set

inner_vid
    Inner VLAN ID to match, if \ ``EF4_FILTER_MATCH_INNER_VID``\  is set

loc_mac
    Local MAC address to match, if \ ``EF4_FILTER_MATCH_LOC_MAC``\  or
    \ ``EF4_FILTER_MATCH_LOC_MAC_IG``\  is set

rem_mac
    Remote MAC address to match, if \ ``EF4_FILTER_MATCH_REM_MAC``\  is set

ether_type
    Ether-type to match, if \ ``EF4_FILTER_MATCH_ETHER_TYPE``\  is set

ip_proto
    IP transport protocol to match, if \ ``EF4_FILTER_MATCH_IP_PROTO``\ 
    is set

loc_host
    Local IP host to match, if \ ``EF4_FILTER_MATCH_LOC_HOST``\  is set

rem_host
    Remote IP host to match, if \ ``EF4_FILTER_MATCH_REM_HOST``\  is set

loc_port
    Local TCP/UDP port to match, if \ ``EF4_FILTER_MATCH_LOC_PORT``\  is set

rem_port
    Remote TCP/UDP port to match, if \ ``EF4_FILTER_MATCH_REM_PORT``\  is set

.. _`ef4_filter_spec.description`:

Description
-----------

The \ :c:func:`ef4_filter_init_rx`\  or \ :c:func:`ef4_filter_init_tx`\  function \*must\* be
used to initialise the structure.  The ef4_filter_set\_\*() functions
may then be used to set \ ``rss_context``\ , \ ``match_flags``\  and related
fields.

The \ ``priority``\  field is used by software to determine whether a new
filter may replace an old one.  The hardware priority of a filter
depends on which fields are matched.

.. _`ef4_filter_set_ipv4_local`:

ef4_filter_set_ipv4_local
=========================

.. c:function:: int ef4_filter_set_ipv4_local(struct ef4_filter_spec *spec, u8 proto, __be32 host, __be16 port)

    specify IPv4 host, transport protocol and port

    :param struct ef4_filter_spec \*spec:
        Specification to initialise

    :param u8 proto:
        Transport layer protocol number

    :param __be32 host:
        Local host address (network byte order)

    :param __be16 port:
        Local port (network byte order)

.. _`ef4_filter_set_ipv4_full`:

ef4_filter_set_ipv4_full
========================

.. c:function:: int ef4_filter_set_ipv4_full(struct ef4_filter_spec *spec, u8 proto, __be32 lhost, __be16 lport, __be32 rhost, __be16 rport)

    specify IPv4 hosts, transport protocol and ports

    :param struct ef4_filter_spec \*spec:
        Specification to initialise

    :param u8 proto:
        Transport layer protocol number

    :param __be32 lhost:
        Local host address (network byte order)

    :param __be16 lport:
        Local port (network byte order)

    :param __be32 rhost:
        Remote host address (network byte order)

    :param __be16 rport:
        Remote port (network byte order)

.. _`ef4_filter_set_eth_local`:

ef4_filter_set_eth_local
========================

.. c:function:: int ef4_filter_set_eth_local(struct ef4_filter_spec *spec, u16 vid, const u8 *addr)

    specify local Ethernet address and/or VID

    :param struct ef4_filter_spec \*spec:
        Specification to initialise

    :param u16 vid:
        Outer VLAN ID to match, or \ ``EF4_FILTER_VID_UNSPEC``\ 

    :param const u8 \*addr:
        Local Ethernet MAC address, or \ ``NULL``\ 

.. _`ef4_filter_set_uc_def`:

ef4_filter_set_uc_def
=====================

.. c:function:: int ef4_filter_set_uc_def(struct ef4_filter_spec *spec)

    specify matching otherwise-unmatched unicast

    :param struct ef4_filter_spec \*spec:
        Specification to initialise

.. _`ef4_filter_set_mc_def`:

ef4_filter_set_mc_def
=====================

.. c:function:: int ef4_filter_set_mc_def(struct ef4_filter_spec *spec)

    specify matching otherwise-unmatched multicast

    :param struct ef4_filter_spec \*spec:
        Specification to initialise

.. This file was automatic generated / don't edit.

