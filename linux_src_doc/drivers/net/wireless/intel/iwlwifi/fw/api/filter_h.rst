.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/filter.h

.. _`iwl_mcast_filter_cmd`:

struct iwl_mcast_filter_cmd
===========================

.. c:type:: struct iwl_mcast_filter_cmd

    configure multicast filter.

.. _`iwl_mcast_filter_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_mcast_filter_cmd {
        u8 filter_own;
        u8 port_id;
        u8 count;
        u8 pass_all;
        u8 bssid[6];
        u8 reserved[2];
        u8 addr_list[0];
    }

.. _`iwl_mcast_filter_cmd.members`:

Members
-------

filter_own
    Set 1 to filter out multicast packets sent by station itself

port_id
    Multicast MAC addresses array specifier. This is a strange way
    to identify network interface adopted in host-device IF.
    It is used by FW as index in array of addresses. This array has
    MAX_PORT_ID_NUM members.

count
    Number of MAC addresses in the array

pass_all
    Set 1 to pass all multicast packets.

bssid
    current association BSSID.

reserved
    reserved

addr_list
    Place holder for array of MAC addresses.
    IMPORTANT: add padding if necessary to ensure DWORD alignment.

.. _`iwl_mvm_bcast_filter_attr_offset`:

enum iwl_mvm_bcast_filter_attr_offset
=====================================

.. c:type:: enum iwl_mvm_bcast_filter_attr_offset

    written by fw for each Rx packet

.. _`iwl_mvm_bcast_filter_attr_offset.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_bcast_filter_attr_offset {
        BCAST_FILTER_OFFSET_PAYLOAD_START,
        BCAST_FILTER_OFFSET_IP_END
    };

.. _`iwl_mvm_bcast_filter_attr_offset.constants`:

Constants
---------

BCAST_FILTER_OFFSET_PAYLOAD_START
    offset is from payload start.

BCAST_FILTER_OFFSET_IP_END
    offset is from ip header end (i.e.
    start of ip payload).

.. _`iwl_fw_bcast_filter_attr`:

struct iwl_fw_bcast_filter_attr
===============================

.. c:type:: struct iwl_fw_bcast_filter_attr

    broadcast filter attribute

.. _`iwl_fw_bcast_filter_attr.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_bcast_filter_attr {
        u8 offset_type;
        u8 offset;
        __le16 reserved1;
        __be32 val;
        __be32 mask;
    }

.. _`iwl_fw_bcast_filter_attr.members`:

Members
-------

offset_type
    \ :c:type:`enum iwl_mvm_bcast_filter_attr_offset <iwl_mvm_bcast_filter_attr_offset>`\ .

offset
    starting offset of this pattern.

reserved1
    reserved

val
    value to match - big endian (MSB is the first
    byte to match from offset pos).

mask
    mask to match (big endian).

.. _`iwl_mvm_bcast_filter_frame_type`:

enum iwl_mvm_bcast_filter_frame_type
====================================

.. c:type:: enum iwl_mvm_bcast_filter_frame_type

    filter frame type

.. _`iwl_mvm_bcast_filter_frame_type.definition`:

Definition
----------

.. code-block:: c

    enum iwl_mvm_bcast_filter_frame_type {
        BCAST_FILTER_FRAME_TYPE_ALL,
        BCAST_FILTER_FRAME_TYPE_IPV4
    };

.. _`iwl_mvm_bcast_filter_frame_type.constants`:

Constants
---------

BCAST_FILTER_FRAME_TYPE_ALL
    consider all frames.

BCAST_FILTER_FRAME_TYPE_IPV4
    consider only ipv4 frames

.. _`iwl_fw_bcast_filter`:

struct iwl_fw_bcast_filter
==========================

.. c:type:: struct iwl_fw_bcast_filter

    broadcast filter

.. _`iwl_fw_bcast_filter.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_bcast_filter {
        u8 discard;
        u8 frame_type;
        u8 num_attrs;
        u8 reserved1;
        struct iwl_fw_bcast_filter_attr attrs[MAX_BCAST_FILTER_ATTRS];
    }

.. _`iwl_fw_bcast_filter.members`:

Members
-------

discard
    discard frame (1) or let it pass (0).

frame_type
    \ :c:type:`enum iwl_mvm_bcast_filter_frame_type <iwl_mvm_bcast_filter_frame_type>`\ .

num_attrs
    number of valid attributes in this filter.

reserved1
    reserved

attrs
    attributes of this filter. a filter is considered matched
    only when all its attributes are matched (i.e. AND relationship)

.. _`iwl_fw_bcast_mac`:

struct iwl_fw_bcast_mac
=======================

.. c:type:: struct iwl_fw_bcast_mac

    per-mac broadcast filtering configuration.

.. _`iwl_fw_bcast_mac.definition`:

Definition
----------

.. code-block:: c

    struct iwl_fw_bcast_mac {
        u8 default_discard;
        u8 reserved1;
        __le16 attached_filters;
    }

.. _`iwl_fw_bcast_mac.members`:

Members
-------

default_discard
    default action for this mac (discard (1) / pass (0)).

reserved1
    reserved

attached_filters
    bitmap of relevant filters for this mac.

.. _`iwl_bcast_filter_cmd`:

struct iwl_bcast_filter_cmd
===========================

.. c:type:: struct iwl_bcast_filter_cmd

    broadcast filtering configuration

.. _`iwl_bcast_filter_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_bcast_filter_cmd {
        u8 disable;
        u8 max_bcast_filters;
        u8 max_macs;
        u8 reserved1;
        struct iwl_fw_bcast_filter filters[MAX_BCAST_FILTERS];
        struct iwl_fw_bcast_mac macs[NUM_MAC_INDEX_DRIVER];
    }

.. _`iwl_bcast_filter_cmd.members`:

Members
-------

disable
    enable (0) / disable (1)

max_bcast_filters
    max number of filters (MAX_BCAST_FILTERS)

max_macs
    max number of macs (NUM_MAC_INDEX_DRIVER)

reserved1
    reserved

filters
    broadcast filters

macs
    broadcast filtering configuration per-mac

.. This file was automatic generated / don't edit.

