.. -*- coding: utf-8; mode: rst -*-

=============
openvswitch.h
=============


.. _`ovs_header`:

struct ovs_header
=================

.. c:type:: ovs_header

    header for OVS Generic Netlink messages.


.. _`ovs_header.definition`:

Definition
----------

.. code-block:: c

  struct ovs_header {
    int dp_ifindex;
  };


.. _`ovs_header.members`:

Members
-------

:``dp_ifindex``:
    ifindex of local port for datapath (0 to make a request not
    specific to a datapath).




.. _`ovs_header.description`:

Description
-----------

Attributes following the header are specific to a particular OVS Generic
Netlink family, but all of the OVS families use this header.



.. _`ovs_datapath_attr`:

enum ovs_datapath_attr
======================

.. c:type:: ovs_datapath_attr

    attributes for %OVS_DP_* commands.


.. _`ovs_datapath_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_datapath_attr {
      OVS_DP_ATTR_UNSPEC,
      OVS_DP_ATTR_NAME,
      OVS_DP_ATTR_UPCALL_PID,
      OVS_DP_ATTR_STATS,
      OVS_DP_ATTR_MEGAFLOW_STATS,
      OVS_DP_ATTR_USER_FEATURES,
      __OVS_DP_ATTR_MAX
    };


.. _`ovs_datapath_attr.constants`:

Constants
---------

:``OVS_DP_ATTR_UNSPEC``:
-- undescribed --

:``OVS_DP_ATTR_NAME``:
    Name of the network device that serves as the "local
    port".  This is the name of the network device whose dp_ifindex is given in
    the :c:type:`struct ovs_header <ovs_header>`.  Always present in notifications.  Required in
    ``OVS_DP_NEW`` requests.  May be used as an alternative to specifying
    dp_ifindex in other requests (with a dp_ifindex of 0).

:``OVS_DP_ATTR_UPCALL_PID``:
    The Netlink socket in userspace that is initially
    set on the datapath port (for OVS_ACTION_ATTR_MISS).  Only valid on
    ``OVS_DP_CMD_NEW`` requests. A value of zero indicates that upcalls should
    not be sent.

:``OVS_DP_ATTR_STATS``:
    Statistics about packets that have passed through the
    datapath.  Always present in notifications.

:``OVS_DP_ATTR_MEGAFLOW_STATS``:
    Statistics about mega flow masks usage for the
    datapath. Always present in notifications.

:``OVS_DP_ATTR_USER_FEATURES``:
-- undescribed --

:``__OVS_DP_ATTR_MAX``:
-- undescribed --


.. _`ovs_datapath_attr.description`:

Description
-----------

These attributes follow the :c:type:`struct ovs_header <ovs_header>` within the Generic Netlink
payload for ``OVS_DP_``\ \* commands.



.. _`ovs_packet_attr`:

enum ovs_packet_attr
====================

.. c:type:: ovs_packet_attr

    attributes for %OVS_PACKET_* commands.


.. _`ovs_packet_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_packet_attr {
      OVS_PACKET_ATTR_UNSPEC,
      OVS_PACKET_ATTR_PACKET,
      OVS_PACKET_ATTR_KEY,
      OVS_PACKET_ATTR_ACTIONS,
      OVS_PACKET_ATTR_USERDATA,
      OVS_PACKET_ATTR_EGRESS_TUN_KEY,
      OVS_PACKET_ATTR_UNUSED1,
      OVS_PACKET_ATTR_UNUSED2,
      OVS_PACKET_ATTR_PROBE,
      OVS_PACKET_ATTR_MRU,
      __OVS_PACKET_ATTR_MAX
    };


.. _`ovs_packet_attr.constants`:

Constants
---------

:``OVS_PACKET_ATTR_UNSPEC``:
-- undescribed --

:``OVS_PACKET_ATTR_PACKET``:
    Present for all notifications.  Contains the entire
    packet as received, from the start of the Ethernet header onward.  For
    ``OVS_PACKET_CMD_ACTION``\ , ``OVS_PACKET_ATTR_PACKET`` reflects changes made by
    actions preceding ``OVS_ACTION_ATTR_USERSPACE``\ , but ``OVS_PACKET_ATTR_KEY`` is
    the flow key extracted from the packet as originally received.

:``OVS_PACKET_ATTR_KEY``:
    Present for all notifications.  Contains the flow key
    extracted from the packet as nested ``OVS_KEY_ATTR_``\ \* attributes.  This allows
    userspace to adapt its flow setup strategy by comparing its notion of the
    flow key against the kernel's.

:``OVS_PACKET_ATTR_ACTIONS``:
    Contains actions for the packet.  Used
    for ``OVS_PACKET_CMD_EXECUTE``\ .  It has nested ``OVS_ACTION_ATTR_``\ \* attributes.
    Also used in upcall when ``OVS_ACTION_ATTR_USERSPACE`` has optional
    ``OVS_USERSPACE_ATTR_ACTIONS`` attribute.

:``OVS_PACKET_ATTR_USERDATA``:
    Present for an ``OVS_PACKET_CMD_ACTION``
    notification if the ``OVS_ACTION_ATTR_USERSPACE`` action specified an
    ``OVS_USERSPACE_ATTR_USERDATA`` attribute, with the same length and content
    specified there.

:``OVS_PACKET_ATTR_EGRESS_TUN_KEY``:
    Present for an ``OVS_PACKET_CMD_ACTION``
    notification if the ``OVS_ACTION_ATTR_USERSPACE`` action specified an
    ``OVS_USERSPACE_ATTR_EGRESS_TUN_PORT`` attribute, which is sent only if the
    output port is actually a tunnel port. Contains the output tunnel key
    extracted from the packet as nested ``OVS_TUNNEL_KEY_ATTR_``\ \* attributes.

:``OVS_PACKET_ATTR_UNUSED1``:
-- undescribed --

:``OVS_PACKET_ATTR_UNUSED2``:
-- undescribed --

:``OVS_PACKET_ATTR_PROBE``:
-- undescribed --

:``OVS_PACKET_ATTR_MRU``:
    Present for an ``OVS_PACKET_CMD_ACTION`` and
    ``OVS_PACKET_ATTR_USERSPACE`` action specify the Maximum received fragment
    size.

:``__OVS_PACKET_ATTR_MAX``:
-- undescribed --


.. _`ovs_packet_attr.description`:

Description
-----------

These attributes follow the :c:type:`struct ovs_header <ovs_header>` within the Generic Netlink
payload for ``OVS_PACKET_``\ \* commands.



.. _`ovs_vport_attr`:

enum ovs_vport_attr
===================

.. c:type:: ovs_vport_attr

    attributes for %OVS_VPORT_* commands.


.. _`ovs_vport_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_vport_attr {
      OVS_VPORT_ATTR_UNSPEC,
      OVS_VPORT_ATTR_PORT_NO,
      OVS_VPORT_ATTR_TYPE,
      OVS_VPORT_ATTR_NAME,
      OVS_VPORT_ATTR_OPTIONS,
      OVS_VPORT_ATTR_UPCALL_PID,
      OVS_VPORT_ATTR_STATS,
      __OVS_VPORT_ATTR_MAX
    };


.. _`ovs_vport_attr.constants`:

Constants
---------

:``OVS_VPORT_ATTR_UNSPEC``:
-- undescribed --

:``OVS_VPORT_ATTR_PORT_NO``:
    32-bit port number within datapath.

:``OVS_VPORT_ATTR_TYPE``:
    32-bit ``OVS_VPORT_TYPE_``\ \* constant describing the type
    of vport.

:``OVS_VPORT_ATTR_NAME``:
    Name of vport.  For a vport based on a network device
    this is the name of the network device.  Maximum length ``IFNAMSIZ-1`` bytes
    plus a null terminator.

:``OVS_VPORT_ATTR_OPTIONS``:
    Vport-specific configuration information.

:``OVS_VPORT_ATTR_UPCALL_PID``:
    The array of Netlink socket pids in userspace
    among which OVS_PACKET_CMD_MISS upcalls will be distributed for packets
    received on this port.  If this is a single-element array of value 0,
    upcalls should not be sent.

:``OVS_VPORT_ATTR_STATS``:
    A :c:type:`struct ovs_vport_stats <ovs_vport_stats>` giving statistics for
    packets sent or received through the vport.

:``__OVS_VPORT_ATTR_MAX``:
-- undescribed --


.. _`ovs_vport_attr.description`:

Description
-----------

These attributes follow the :c:type:`struct ovs_header <ovs_header>` within the Generic Netlink
payload for ``OVS_VPORT_``\ \* commands.

For ``OVS_VPORT_CMD_NEW`` requests, the ``OVS_VPORT_ATTR_TYPE`` and
``OVS_VPORT_ATTR_NAME`` attributes are required.  ``OVS_VPORT_ATTR_PORT_NO`` is
optional; if not specified a free port number is automatically selected.
Whether ``OVS_VPORT_ATTR_OPTIONS`` is required or optional depends on the type
of vport.

For other requests, if ``OVS_VPORT_ATTR_NAME`` is specified then it is used to
look up the vport to operate on; otherwise dp_idx from the :c:type:`struct ovs_header <ovs_header>` plus ``OVS_VPORT_ATTR_PORT_NO`` determine the vport.



.. _`ovs_frag_type`:

enum ovs_frag_type
==================

.. c:type:: ovs_frag_type

    IPv4 and IPv6 fragment type


.. _`ovs_frag_type.definition`:

Definition
----------

.. code-block:: c

    enum ovs_frag_type {
      OVS_FRAG_TYPE_NONE,
      OVS_FRAG_TYPE_FIRST,
      OVS_FRAG_TYPE_LATER,
      __OVS_FRAG_TYPE_MAX
    };


.. _`ovs_frag_type.constants`:

Constants
---------

:``OVS_FRAG_TYPE_NONE``:
    Packet is not a fragment.

:``OVS_FRAG_TYPE_FIRST``:
    Packet is a fragment with offset 0.

:``OVS_FRAG_TYPE_LATER``:
    Packet is a fragment with nonzero offset.

:``__OVS_FRAG_TYPE_MAX``:
-- undescribed --


.. _`ovs_frag_type.description`:

Description
-----------

Used as the ``ipv4_frag`` in :c:type:`struct ovs_key_ipv4 <ovs_key_ipv4>` and as ``ipv6_frag`` :c:type:`struct ovs_key_ipv6 <ovs_key_ipv6>`.



.. _`ovs_flow_attr`:

enum ovs_flow_attr
==================

.. c:type:: ovs_flow_attr

    attributes for %OVS_FLOW_* commands.


.. _`ovs_flow_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_flow_attr {
      OVS_FLOW_ATTR_UNSPEC,
      OVS_FLOW_ATTR_KEY,
      OVS_FLOW_ATTR_ACTIONS,
      OVS_FLOW_ATTR_STATS,
      OVS_FLOW_ATTR_TCP_FLAGS,
      OVS_FLOW_ATTR_USED,
      OVS_FLOW_ATTR_CLEAR,
      OVS_FLOW_ATTR_MASK,
      OVS_FLOW_ATTR_PROBE,
      OVS_FLOW_ATTR_UFID,
      OVS_FLOW_ATTR_UFID_FLAGS,
      __OVS_FLOW_ATTR_MAX
    };


.. _`ovs_flow_attr.constants`:

Constants
---------

:``OVS_FLOW_ATTR_UNSPEC``:
-- undescribed --

:``OVS_FLOW_ATTR_KEY``:
    Nested ``OVS_KEY_ATTR_``\ \* attributes specifying the flow
    key.  Always present in notifications.  Required for all requests (except
    dumps).

:``OVS_FLOW_ATTR_ACTIONS``:
    Nested ``OVS_ACTION_ATTR_``\ \* attributes specifying
    the actions to take for packets that match the key.  Always present in
    notifications.  Required for ``OVS_FLOW_CMD_NEW`` requests, optional for
    ``OVS_FLOW_CMD_SET`` requests.  An ``OVS_FLOW_CMD_SET`` without
    ``OVS_FLOW_ATTR_ACTIONS`` will not modify the actions.  To clear the actions,
    an ``OVS_FLOW_ATTR_ACTIONS`` without any nested attributes must be given.

:``OVS_FLOW_ATTR_STATS``:
    :c:type:`struct ovs_flow_stats <ovs_flow_stats>` giving statistics for this
    flow.  Present in notifications if the stats would be nonzero.  Ignored in
    requests.

:``OVS_FLOW_ATTR_TCP_FLAGS``:
    An 8-bit value giving the OR'd value of all of the
    TCP flags seen on packets in this flow.  Only present in notifications for
    TCP flows, and only if it would be nonzero.  Ignored in requests.

:``OVS_FLOW_ATTR_USED``:
    A 64-bit integer giving the time, in milliseconds on
    the system monotonic clock, at which a packet was last processed for this
    flow.  Only present in notifications if a packet has been processed for this
    flow.  Ignored in requests.

:``OVS_FLOW_ATTR_CLEAR``:
    If present in a ``OVS_FLOW_CMD_SET`` request, clears the
    last-used time, accumulated TCP flags, and statistics for this flow.
    Otherwise ignored in requests.  Never present in notifications.

:``OVS_FLOW_ATTR_MASK``:
    Nested ``OVS_KEY_ATTR_``\ \* attributes specifying the
    mask bits for wildcarded flow match. Mask bit value '1' specifies exact
    match with corresponding flow key bit, while mask bit value '0' specifies
    a wildcarded match. Omitting attribute is treated as wildcarding all
    corresponding fields. Optional for all requests. If not present,
    all flow key bits are exact match bits.

:``OVS_FLOW_ATTR_PROBE``:
-- undescribed --

:``OVS_FLOW_ATTR_UFID``:
    A value between 1-16 octets specifying a unique
    identifier for the flow. Causes the flow to be indexed by this value rather
    than the value of the ``OVS_FLOW_ATTR_KEY`` attribute. Optional for all
    requests. Present in notifications if the flow was created with this
    attribute.

:``OVS_FLOW_ATTR_UFID_FLAGS``:
    A 32-bit value of OR'd ``OVS_UFID_F_``\ *
    flags that provide alternative semantics for flow installation and
    retrieval. Optional for all requests.

:``__OVS_FLOW_ATTR_MAX``:
-- undescribed --


.. _`ovs_flow_attr.description`:

Description
-----------

These attributes follow the :c:type:`struct ovs_header <ovs_header>` within the Generic Netlink
payload for ``OVS_FLOW_``\ \* commands.



.. _`ovs_ufid_f_omit_key`:

OVS_UFID_F_OMIT_KEY
===================

.. c:function:: OVS_UFID_F_OMIT_KEY ()



.. _`ovs_ufid_f_omit_key.description`:

Description
-----------


If a datapath request contains an ``OVS_UFID_F_OMIT_``\ \* flag, then the datapath
may omit the corresponding ``OVS_FLOW_ATTR_``\ \* from the response.



.. _`ovs_sample_attr`:

enum ovs_sample_attr
====================

.. c:type:: ovs_sample_attr

    Attributes for %OVS_ACTION_ATTR_SAMPLE action.


.. _`ovs_sample_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_sample_attr {
      OVS_SAMPLE_ATTR_UNSPEC,
      OVS_SAMPLE_ATTR_PROBABILITY,
      OVS_SAMPLE_ATTR_ACTIONS,
      __OVS_SAMPLE_ATTR_MAX
    };


.. _`ovs_sample_attr.constants`:

Constants
---------

:``OVS_SAMPLE_ATTR_UNSPEC``:
-- undescribed --

:``OVS_SAMPLE_ATTR_PROBABILITY``:
    32-bit fraction of packets to sample with
    ``OVS_ACTION_ATTR_SAMPLE``\ .  A value of 0 samples no packets, a value of
    ``UINT32_MAX`` samples all packets and intermediate values sample intermediate
    fractions of packets.

:``OVS_SAMPLE_ATTR_ACTIONS``:
    Set of actions to execute in sampling event.
    Actions are passed as nested attributes.

:``__OVS_SAMPLE_ATTR_MAX``:
-- undescribed --


.. _`ovs_sample_attr.description`:

Description
-----------

Executes the specified actions with the given probability on a per-packet
basis.



.. _`ovs_userspace_attr`:

enum ovs_userspace_attr
=======================

.. c:type:: ovs_userspace_attr

    Attributes for %OVS_ACTION_ATTR_USERSPACE action.


.. _`ovs_userspace_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_userspace_attr {
      OVS_USERSPACE_ATTR_UNSPEC,
      OVS_USERSPACE_ATTR_PID,
      OVS_USERSPACE_ATTR_USERDATA,
      OVS_USERSPACE_ATTR_EGRESS_TUN_PORT,
      OVS_USERSPACE_ATTR_ACTIONS,
      __OVS_USERSPACE_ATTR_MAX
    };


.. _`ovs_userspace_attr.constants`:

Constants
---------

:``OVS_USERSPACE_ATTR_UNSPEC``:
-- undescribed --

:``OVS_USERSPACE_ATTR_PID``:
    u32 Netlink PID to which the ``OVS_PACKET_CMD_ACTION``
    message should be sent.  Required.

:``OVS_USERSPACE_ATTR_USERDATA``:
    If present, its variable-length argument is
    copied to the ``OVS_PACKET_CMD_ACTION`` message as ``OVS_PACKET_ATTR_USERDATA``\ .

:``OVS_USERSPACE_ATTR_EGRESS_TUN_PORT``:
    If present, u32 output port to get
    tunnel info.

:``OVS_USERSPACE_ATTR_ACTIONS``:
    If present, send actions with upcall.

:``__OVS_USERSPACE_ATTR_MAX``:
-- undescribed --


.. _`ovs_action_push_mpls`:

struct ovs_action_push_mpls
===========================

.. c:type:: ovs_action_push_mpls

    %OVS_ACTION_ATTR_PUSH_MPLS action argument.


.. _`ovs_action_push_mpls.definition`:

Definition
----------

.. code-block:: c

  struct ovs_action_push_mpls {
    __be32 mpls_lse;
    __be16 mpls_ethertype;
  };


.. _`ovs_action_push_mpls.members`:

Members
-------

:``mpls_lse``:
    MPLS label stack entry to push.

:``mpls_ethertype``:
    Ethertype to set in the encapsulating ethernet frame.




.. _`ovs_action_push_mpls.description`:

Description
-----------

The only values ``mpls_ethertype`` should ever be given are ``ETH_P_MPLS_UC`` and
``ETH_P_MPLS_MC``\ , indicating MPLS unicast or multicast. Other are rejected.



.. _`ovs_action_push_vlan`:

struct ovs_action_push_vlan
===========================

.. c:type:: ovs_action_push_vlan

    %OVS_ACTION_ATTR_PUSH_VLAN action argument.


.. _`ovs_action_push_vlan.definition`:

Definition
----------

.. code-block:: c

  struct ovs_action_push_vlan {
    __be16 vlan_tpid;
    __be16 vlan_tci;
  };


.. _`ovs_action_push_vlan.members`:

Members
-------

:``vlan_tpid``:
    Tag protocol identifier (TPID) to push.

:``vlan_tci``:
    Tag control identifier (TCI) to push.  The CFI bit must be set
    (but it will not be set in the 802.1Q header that is pushed).




.. _`ovs_action_push_vlan.description`:

Description
-----------

The ``vlan_tpid`` value is typically ``ETH_P_8021Q``\ .  The only acceptable TPID
values are those that the kernel module also parses as 802.1Q headers, to
prevent ``OVS_ACTION_ATTR_PUSH_VLAN`` followed by ``OVS_ACTION_ATTR_POP_VLAN``
from having surprising results.



.. _`ovs_ct_attr`:

enum ovs_ct_attr
================

.. c:type:: ovs_ct_attr

    Attributes for %OVS_ACTION_ATTR_CT action.


.. _`ovs_ct_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_ct_attr {
      OVS_CT_ATTR_UNSPEC,
      OVS_CT_ATTR_COMMIT,
      OVS_CT_ATTR_ZONE,
      OVS_CT_ATTR_MARK,
      OVS_CT_ATTR_LABELS,
      OVS_CT_ATTR_HELPER,
      OVS_CT_ATTR_NAT,
      __OVS_CT_ATTR_MAX
    };


.. _`ovs_ct_attr.constants`:

Constants
---------

:``OVS_CT_ATTR_UNSPEC``:
-- undescribed --

:``OVS_CT_ATTR_COMMIT``:
    If present, commits the connection to the conntrack
    table. This allows future packets for the same connection to be identified
    as 'established' or 'related'. The flow key for the current packet will
    retain the pre-commit connection state.

:``OVS_CT_ATTR_ZONE``:
    u16 connection tracking zone.

:``OVS_CT_ATTR_MARK``:
    u32 value followed by u32 mask. For each bit set in the
    mask, the corresponding bit in the value is copied to the connection
    tracking mark field in the connection.

:``OVS_CT_ATTR_LABELS``:
    ``OVS_CT_LABELS_LEN`` value followed by ``OVS_CT_LABELS_LEN``
    mask. For each bit set in the mask, the corresponding bit in the value is
    copied to the connection tracking label field in the connection.

:``OVS_CT_ATTR_HELPER``:
    variable length string defining conntrack ALG.

:``OVS_CT_ATTR_NAT``:
    Nested OVS_NAT_ATTR\_\* for performing L3 network address
    translation (NAT) on the packet.

:``__OVS_CT_ATTR_MAX``:
-- undescribed --


.. _`ovs_nat_attr`:

enum ovs_nat_attr
=================

.. c:type:: ovs_nat_attr

    Attributes for %OVS_CT_ATTR_NAT.


.. _`ovs_nat_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_nat_attr {
      OVS_NAT_ATTR_UNSPEC,
      OVS_NAT_ATTR_SRC,
      OVS_NAT_ATTR_DST,
      OVS_NAT_ATTR_IP_MIN,
      OVS_NAT_ATTR_IP_MAX,
      OVS_NAT_ATTR_PROTO_MIN,
      OVS_NAT_ATTR_PROTO_MAX,
      OVS_NAT_ATTR_PERSISTENT,
      OVS_NAT_ATTR_PROTO_HASH,
      OVS_NAT_ATTR_PROTO_RANDOM,
      __OVS_NAT_ATTR_MAX
    };


.. _`ovs_nat_attr.constants`:

Constants
---------

:``OVS_NAT_ATTR_UNSPEC``:
-- undescribed --

:``OVS_NAT_ATTR_SRC``:
    Flag for Source NAT (mangle source address/port).

:``OVS_NAT_ATTR_DST``:
    Flag for Destination NAT (mangle destination
    address/port).  Only one of (\ ``OVS_NAT_ATTR_SRC``\ , ``OVS_NAT_ATTR_DST``\ ) may be
    specified.  Effective only for packets for ct_state NEW connections.
    Packets of committed connections are mangled by the NAT action according to
    the committed NAT type regardless of the flags specified.  As a corollary, a
    NAT action without a NAT type flag will only mangle packets of committed
    connections.  The following NAT attributes only apply for NEW
    (non-committed) connections, and they may be included only when the CT
    action has the ``OVS_CT_ATTR_COMMIT`` flag and either ``OVS_NAT_ATTR_SRC`` or
    ``OVS_NAT_ATTR_DST`` is also included.

:``OVS_NAT_ATTR_IP_MIN``:
    struct in_addr or struct in6_addr

:``OVS_NAT_ATTR_IP_MAX``:
    struct in_addr or struct in6_addr

:``OVS_NAT_ATTR_PROTO_MIN``:
    u16 L4 protocol specific lower boundary (port)

:``OVS_NAT_ATTR_PROTO_MAX``:
    u16 L4 protocol specific upper boundary (port)

:``OVS_NAT_ATTR_PERSISTENT``:
    Flag for persistent IP mapping across reboots

:``OVS_NAT_ATTR_PROTO_HASH``:
    Flag for pseudo random L4 port mapping (MD5)

:``OVS_NAT_ATTR_PROTO_RANDOM``:
    Flag for fully randomized L4 port mapping

:``__OVS_NAT_ATTR_MAX``:
-- undescribed --


.. _`ovs_action_attr`:

enum ovs_action_attr
====================

.. c:type:: ovs_action_attr

    Action types.


.. _`ovs_action_attr.definition`:

Definition
----------

.. code-block:: c

    enum ovs_action_attr {
      OVS_ACTION_ATTR_UNSPEC,
      OVS_ACTION_ATTR_OUTPUT,
      OVS_ACTION_ATTR_USERSPACE,
      OVS_ACTION_ATTR_SET,
      OVS_ACTION_ATTR_PUSH_VLAN,
      OVS_ACTION_ATTR_POP_VLAN,
      OVS_ACTION_ATTR_SAMPLE,
      OVS_ACTION_ATTR_RECIRC,
      OVS_ACTION_ATTR_HASH,
      OVS_ACTION_ATTR_PUSH_MPLS,
      OVS_ACTION_ATTR_POP_MPLS,
      OVS_ACTION_ATTR_SET_MASKED,
      OVS_ACTION_ATTR_CT,
      __OVS_ACTION_ATTR_MAX,
      OVS_ACTION_ATTR_SET_TO_MASKED,
       
    };


.. _`ovs_action_attr.constants`:

Constants
---------

:``OVS_ACTION_ATTR_UNSPEC``:
-- undescribed --

:``OVS_ACTION_ATTR_OUTPUT``:
    Output packet to port.

:``OVS_ACTION_ATTR_USERSPACE``:
    Send packet to userspace according to nested
    ``OVS_USERSPACE_ATTR_``\ \* attributes.

:``OVS_ACTION_ATTR_SET``:
    Replaces the contents of an existing header.  The
    single nested ``OVS_KEY_ATTR_``\ \* attribute specifies a header to modify and its
    value.

:``OVS_ACTION_ATTR_PUSH_VLAN``:
    Push a new outermost 802.1Q header onto the
    packet.

:``OVS_ACTION_ATTR_POP_VLAN``:
    Pop the outermost 802.1Q header off the packet.

:``OVS_ACTION_ATTR_SAMPLE``:
    Probabilitically executes actions, as specified in
    the nested ``OVS_SAMPLE_ATTR_``\ \* attributes.

:``OVS_ACTION_ATTR_RECIRC``:
-- undescribed --

:``OVS_ACTION_ATTR_HASH``:
-- undescribed --

:``OVS_ACTION_ATTR_PUSH_MPLS``:
    Push a new MPLS label stack entry onto the
    top of the packets MPLS label stack.  Set the ethertype of the
    encapsulating frame to either ``ETH_P_MPLS_UC`` or ``ETH_P_MPLS_MC`` to
    indicate the new packet contents.

:``OVS_ACTION_ATTR_POP_MPLS``:
    Pop an MPLS label stack entry off of the
    packet's MPLS label stack.  Set the encapsulating frame's ethertype to
    indicate the new packet contents. This could potentially still be
    ``ETH_P_MPLS`` if the resulting MPLS label stack is not empty.  If there
    is no MPLS label stack, as determined by ethertype, no action is taken.

:``OVS_ACTION_ATTR_SET_MASKED``:
    Replaces the contents of an existing header.  A
    nested ``OVS_KEY_ATTR_``\ \* attribute specifies a header to modify, its value,
    and a mask.  For every bit set in the mask, the corresponding bit value
    is copied from the value to the packet header field, rest of the bits are
    left unchanged.  The non-masked value bits must be passed in as zeroes.
    Masking is not supported for the ``OVS_KEY_ATTR_TUNNEL`` attribute.

:``OVS_ACTION_ATTR_CT``:
    Track the connection. Populate the conntrack-related
    entries in the flow key.

:``__OVS_ACTION_ATTR_MAX``:
-- undescribed --

:``OVS_ACTION_ATTR_SET_TO_MASKED``:
    Kernel internal masked set action translated
    from the ``OVS_ACTION_ATTR_SET``\ .

:`` ``:
-- undescribed --


.. _`ovs_action_attr.description`:

Description
-----------

Only a single header can be set with a single ``OVS_ACTION_ATTR_SET``\ .  Not all
fields within a header are modifiable, e.g. the IPv4 protocol and fragment
type may not be changed.

