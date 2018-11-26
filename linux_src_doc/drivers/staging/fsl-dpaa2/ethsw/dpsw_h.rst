.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-dpaa2/ethsw/dpsw.h

.. _`dpsw_max_priorities`:

DPSW_MAX_PRIORITIES
===================

.. c:function::  DPSW_MAX_PRIORITIES()

.. _`dpsw_max_if`:

DPSW_MAX_IF
===========

.. c:function::  DPSW_MAX_IF()

.. _`dpsw_opt_flooding_dis`:

DPSW_OPT_FLOODING_DIS
=====================

.. c:function::  DPSW_OPT_FLOODING_DIS()

.. _`dpsw_opt_multicast_dis`:

DPSW_OPT_MULTICAST_DIS
======================

.. c:function::  DPSW_OPT_MULTICAST_DIS()

.. _`dpsw_opt_ctrl_if_dis`:

DPSW_OPT_CTRL_IF_DIS
====================

.. c:function::  DPSW_OPT_CTRL_IF_DIS()

.. _`dpsw_opt_flooding_metering_dis`:

DPSW_OPT_FLOODING_METERING_DIS
==============================

.. c:function::  DPSW_OPT_FLOODING_METERING_DIS()

.. _`dpsw_opt_metering_en`:

DPSW_OPT_METERING_EN
====================

.. c:function::  DPSW_OPT_METERING_EN()

.. _`dpsw_component_type`:

enum dpsw_component_type
========================

.. c:type:: enum dpsw_component_type

    component type of a bridge

.. _`dpsw_component_type.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_component_type {
        DPSW_COMPONENT_TYPE_C_VLAN,
        DPSW_COMPONENT_TYPE_S_VLAN
    };

.. _`dpsw_component_type.constants`:

Constants
---------

DPSW_COMPONENT_TYPE_C_VLAN
    A C-VLAN component of an
    enterprise VLAN bridge or of a Provider Bridge used
    to process C-tagged frames

DPSW_COMPONENT_TYPE_S_VLAN
    An S-VLAN component of a
    Provider Bridge

.. _`dpsw_cfg`:

struct dpsw_cfg
===============

.. c:type:: struct dpsw_cfg

    DPSW configuration

.. _`dpsw_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_cfg {
        u16 num_ifs;
        struct {
            u64 options;
            u16 max_vlans;
            u8 max_meters_per_if;
            u8 max_fdbs;
            u16 max_fdb_entries;
            u16 fdb_aging_time;
            u16 max_fdb_mc_groups;
            enum dpsw_component_type component_type;
        } adv;
    }

.. _`dpsw_cfg.members`:

Members
-------

num_ifs
    Number of external and internal interfaces

adv
    Advanced parameters; default is all zeros;
    use this structure to change default settings

adv.options
    Enable/Disable DPSW features (bitmap)

adv.max_vlans
    Maximum Number of VLAN's; 0 - indicates default 16

adv.max_meters_per_if
    Number of meters per interface

adv.max_fdbs
    Maximum Number of FDB's; 0 - indicates default 16

adv.max_fdb_entries
    Number of FDB entries for default FDB table;
    0 - indicates default 1024 entries.

adv.fdb_aging_time
    Default FDB aging time for default FDB table;
    0 - indicates default 300 seconds

adv.max_fdb_mc_groups
    Number of multicast groups in each FDB table;
    0 - indicates default 32

adv.component_type
    Indicates the component type of this bridge

.. _`dpsw_irq_index_if`:

DPSW_IRQ_INDEX_IF
=================

.. c:function::  DPSW_IRQ_INDEX_IF()

.. _`dpsw_irq_event_link_changed`:

DPSW_IRQ_EVENT_LINK_CHANGED
===========================

.. c:function::  DPSW_IRQ_EVENT_LINK_CHANGED()

    Indicates that the link state changed

.. _`dpsw_irq_cfg`:

struct dpsw_irq_cfg
===================

.. c:type:: struct dpsw_irq_cfg

    IRQ configuration

.. _`dpsw_irq_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_irq_cfg {
        u64 addr;
        u32 val;
        int irq_num;
    }

.. _`dpsw_irq_cfg.members`:

Members
-------

addr
    Address that must be written to signal a message-based interrupt

val
    Value to write into irq_addr address

irq_num
    A user defined number associated with this IRQ

.. _`dpsw_attr`:

struct dpsw_attr
================

.. c:type:: struct dpsw_attr

    Structure representing DPSW attributes

.. _`dpsw_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_attr {
        int id;
        u64 options;
        u16 max_vlans;
        u8 max_meters_per_if;
        u8 max_fdbs;
        u16 max_fdb_entries;
        u16 fdb_aging_time;
        u16 max_fdb_mc_groups;
        u16 num_ifs;
        u16 mem_size;
        u16 num_vlans;
        u8 num_fdbs;
        enum dpsw_component_type component_type;
    }

.. _`dpsw_attr.members`:

Members
-------

id
    DPSW object ID

options
    Enable/Disable DPSW features

max_vlans
    Maximum Number of VLANs

max_meters_per_if
    Number of meters per interface

max_fdbs
    Maximum Number of FDBs

max_fdb_entries
    Number of FDB entries for default FDB table;
    0 - indicates default 1024 entries.

fdb_aging_time
    Default FDB aging time for default FDB table;
    0 - indicates default 300 seconds

max_fdb_mc_groups
    Number of multicast groups in each FDB table;
    0 - indicates default 32

num_ifs
    Number of interfaces

mem_size
    DPSW frame storage memory size

num_vlans
    Current number of VLANs

num_fdbs
    Current number of FDBs

component_type
    Component type of this bridge

.. _`dpsw_action`:

enum dpsw_action
================

.. c:type:: enum dpsw_action

    Action selection for special/control frames

.. _`dpsw_action.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_action {
        DPSW_ACTION_DROP,
        DPSW_ACTION_REDIRECT
    };

.. _`dpsw_action.constants`:

Constants
---------

DPSW_ACTION_DROP
    Drop frame

DPSW_ACTION_REDIRECT
    Redirect frame to control port

.. _`dpsw_link_opt_autoneg`:

DPSW_LINK_OPT_AUTONEG
=====================

.. c:function::  DPSW_LINK_OPT_AUTONEG()

    negotiation

.. _`dpsw_link_opt_half_duplex`:

DPSW_LINK_OPT_HALF_DUPLEX
=========================

.. c:function::  DPSW_LINK_OPT_HALF_DUPLEX()

    duplex mode

.. _`dpsw_link_opt_pause`:

DPSW_LINK_OPT_PAUSE
===================

.. c:function::  DPSW_LINK_OPT_PAUSE()

.. _`dpsw_link_opt_asym_pause`:

DPSW_LINK_OPT_ASYM_PAUSE
========================

.. c:function::  DPSW_LINK_OPT_ASYM_PAUSE()

    symmetric pause frames

.. _`dpsw_link_cfg`:

struct dpsw_link_cfg
====================

.. c:type:: struct dpsw_link_cfg

    Structure representing DPSW link configuration

.. _`dpsw_link_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_link_cfg {
        u32 rate;
        u64 options;
    }

.. _`dpsw_link_cfg.members`:

Members
-------

rate
    Rate

options
    Mask of available options; use 'DPSW_LINK_OPT_<X>' values

.. _`dpsw_link_state`:

struct dpsw_link_state
======================

.. c:type:: struct dpsw_link_state

    Structure representing DPSW link state

.. _`dpsw_link_state.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_link_state {
        u32 rate;
        u64 options;
        u8 up;
    }

.. _`dpsw_link_state.members`:

Members
-------

rate
    Rate

options
    Mask of available options; use 'DPSW_LINK_OPT_<X>' values

up
    0 - covers two cases: down and disconnected, 1 - up

.. _`dpsw_tci_cfg`:

struct dpsw_tci_cfg
===================

.. c:type:: struct dpsw_tci_cfg

    Tag Control Information (TCI) configuration

.. _`dpsw_tci_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_tci_cfg {
        u8 pcp;
        u8 dei;
        u16 vlan_id;
    }

.. _`dpsw_tci_cfg.members`:

Members
-------

pcp
    Priority Code Point (PCP): a 3-bit field which refers
    to the IEEE 802.1p priority

dei
    Drop Eligible Indicator (DEI): a 1-bit field. May be used
    separately or in conjunction with PCP to indicate frames
    eligible to be dropped in the presence of congestion

vlan_id
    VLAN Identifier (VID): a 12-bit field specifying the VLAN
    to which the frame belongs. The hexadecimal values
    of 0x000 and 0xFFF are reserved;
    all other values may be used as VLAN identifiers,
    allowing up to 4,094 VLANs

.. _`dpsw_stp_state`:

enum dpsw_stp_state
===================

.. c:type:: enum dpsw_stp_state

    Spanning Tree Protocol (STP) states

.. _`dpsw_stp_state.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_stp_state {
        DPSW_STP_STATE_DISABLED,
        DPSW_STP_STATE_LISTENING,
        DPSW_STP_STATE_LEARNING,
        DPSW_STP_STATE_FORWARDING,
        DPSW_STP_STATE_BLOCKING
    };

.. _`dpsw_stp_state.constants`:

Constants
---------

DPSW_STP_STATE_DISABLED
    *undescribed*

DPSW_STP_STATE_LISTENING
    Listening state

DPSW_STP_STATE_LEARNING
    Learning state

DPSW_STP_STATE_FORWARDING
    Forwarding state

DPSW_STP_STATE_BLOCKING
    Blocking state

.. _`dpsw_stp_cfg`:

struct dpsw_stp_cfg
===================

.. c:type:: struct dpsw_stp_cfg

    Spanning Tree Protocol (STP) Configuration

.. _`dpsw_stp_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_stp_cfg {
        u16 vlan_id;
        enum dpsw_stp_state state;
    }

.. _`dpsw_stp_cfg.members`:

Members
-------

vlan_id
    VLAN ID STP state

state
    STP state

.. _`dpsw_accepted_frames`:

enum dpsw_accepted_frames
=========================

.. c:type:: enum dpsw_accepted_frames

    Types of frames to accept

.. _`dpsw_accepted_frames.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_accepted_frames {
        DPSW_ADMIT_ALL,
        DPSW_ADMIT_ONLY_VLAN_TAGGED
    };

.. _`dpsw_accepted_frames.constants`:

Constants
---------

DPSW_ADMIT_ALL
    The device accepts VLAN tagged, untagged and
    priority tagged frames

DPSW_ADMIT_ONLY_VLAN_TAGGED
    The device discards untagged frames or
    Priority-Tagged frames received on this interface.

.. _`dpsw_counter`:

enum dpsw_counter
=================

.. c:type:: enum dpsw_counter

    Counters types

.. _`dpsw_counter.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_counter {
        DPSW_CNT_ING_FRAME,
        DPSW_CNT_ING_BYTE,
        DPSW_CNT_ING_FLTR_FRAME,
        DPSW_CNT_ING_FRAME_DISCARD,
        DPSW_CNT_ING_MCAST_FRAME,
        DPSW_CNT_ING_MCAST_BYTE,
        DPSW_CNT_ING_BCAST_FRAME,
        DPSW_CNT_ING_BCAST_BYTES,
        DPSW_CNT_EGR_FRAME,
        DPSW_CNT_EGR_BYTE,
        DPSW_CNT_EGR_FRAME_DISCARD,
        DPSW_CNT_EGR_STP_FRAME_DISCARD
    };

.. _`dpsw_counter.constants`:

Constants
---------

DPSW_CNT_ING_FRAME
    Counts ingress frames

DPSW_CNT_ING_BYTE
    Counts ingress bytes

DPSW_CNT_ING_FLTR_FRAME
    Counts filtered ingress frames

DPSW_CNT_ING_FRAME_DISCARD
    Counts discarded ingress frame

DPSW_CNT_ING_MCAST_FRAME
    Counts ingress multicast frames

DPSW_CNT_ING_MCAST_BYTE
    Counts ingress multicast bytes

DPSW_CNT_ING_BCAST_FRAME
    Counts ingress broadcast frames

DPSW_CNT_ING_BCAST_BYTES
    Counts ingress broadcast bytes

DPSW_CNT_EGR_FRAME
    Counts egress frames

DPSW_CNT_EGR_BYTE
    Counts eEgress bytes

DPSW_CNT_EGR_FRAME_DISCARD
    Counts discarded egress frames

DPSW_CNT_EGR_STP_FRAME_DISCARD
    Counts egress STP discarded frames

.. _`dpsw_vlan_cfg`:

struct dpsw_vlan_cfg
====================

.. c:type:: struct dpsw_vlan_cfg

    VLAN Configuration

.. _`dpsw_vlan_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_vlan_cfg {
        u16 fdb_id;
    }

.. _`dpsw_vlan_cfg.members`:

Members
-------

fdb_id
    Forwarding Data Base

.. _`dpsw_vlan_if_cfg`:

struct dpsw_vlan_if_cfg
=======================

.. c:type:: struct dpsw_vlan_if_cfg

    Set of VLAN Interfaces

.. _`dpsw_vlan_if_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_vlan_if_cfg {
        u16 num_ifs;
        u16 if_id[DPSW_MAX_IF];
    }

.. _`dpsw_vlan_if_cfg.members`:

Members
-------

num_ifs
    The number of interfaces that are assigned to the egress
    list for this VLAN

if_id
    The set of interfaces that are
    assigned to the egress list for this VLAN

.. _`dpsw_fdb_entry_type`:

enum dpsw_fdb_entry_type
========================

.. c:type:: enum dpsw_fdb_entry_type

    FDB Entry type - Static/Dynamic

.. _`dpsw_fdb_entry_type.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_fdb_entry_type {
        DPSW_FDB_ENTRY_STATIC,
        DPSW_FDB_ENTRY_DINAMIC
    };

.. _`dpsw_fdb_entry_type.constants`:

Constants
---------

DPSW_FDB_ENTRY_STATIC
    Static entry

DPSW_FDB_ENTRY_DINAMIC
    Dynamic entry

.. _`dpsw_fdb_unicast_cfg`:

struct dpsw_fdb_unicast_cfg
===========================

.. c:type:: struct dpsw_fdb_unicast_cfg

    Unicast entry configuration

.. _`dpsw_fdb_unicast_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_fdb_unicast_cfg {
        enum dpsw_fdb_entry_type type;
        u8 mac_addr[6];
        u16 if_egress;
    }

.. _`dpsw_fdb_unicast_cfg.members`:

Members
-------

type
    Select static or dynamic entry

mac_addr
    MAC address

if_egress
    Egress interface ID

.. _`dpsw_fdb_multicast_cfg`:

struct dpsw_fdb_multicast_cfg
=============================

.. c:type:: struct dpsw_fdb_multicast_cfg

    Multi-cast entry configuration

.. _`dpsw_fdb_multicast_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_fdb_multicast_cfg {
        enum dpsw_fdb_entry_type type;
        u8 mac_addr[6];
        u16 num_ifs;
        u16 if_id[DPSW_MAX_IF];
    }

.. _`dpsw_fdb_multicast_cfg.members`:

Members
-------

type
    Select static or dynamic entry

mac_addr
    MAC address

num_ifs
    Number of external and internal interfaces

if_id
    Egress interface IDs

.. _`dpsw_fdb_learning_mode`:

enum dpsw_fdb_learning_mode
===========================

.. c:type:: enum dpsw_fdb_learning_mode

    Auto-learning modes

.. _`dpsw_fdb_learning_mode.definition`:

Definition
----------

.. code-block:: c

    enum dpsw_fdb_learning_mode {
        DPSW_FDB_LEARNING_MODE_DIS,
        DPSW_FDB_LEARNING_MODE_HW,
        DPSW_FDB_LEARNING_MODE_NON_SECURE,
        DPSW_FDB_LEARNING_MODE_SECURE
    };

.. _`dpsw_fdb_learning_mode.constants`:

Constants
---------

DPSW_FDB_LEARNING_MODE_DIS
    Disable Auto-learning

DPSW_FDB_LEARNING_MODE_HW
    Enable HW auto-Learning

DPSW_FDB_LEARNING_MODE_NON_SECURE
    Enable None secure learning by CPU

DPSW_FDB_LEARNING_MODE_SECURE
    Enable secure learning by CPU

.. _`dpsw_fdb_learning_mode.description`:

Description
-----------

NONE - SECURE LEARNING
SMAC found      DMAC found      CTLU Action
v               v       Forward frame to
1.  DMAC destination
-               v       Forward frame to
1.  DMAC destination
2.  Control interface
v               -       Forward frame to
1.  Flooding list of interfaces
-               -       Forward frame to
1.  Flooding list of interfaces
2.  Control interface
SECURE LEARING
SMAC found      DMAC found      CTLU Action
v               v               Forward frame to
1.  DMAC destination
-               v               Forward frame to
1.  Control interface
v               -               Forward frame to
1.  Flooding list of interfaces
-               -               Forward frame to
1.  Control interface

.. _`dpsw_fdb_attr`:

struct dpsw_fdb_attr
====================

.. c:type:: struct dpsw_fdb_attr

    FDB Attributes

.. _`dpsw_fdb_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpsw_fdb_attr {
        u16 max_fdb_entries;
        u16 fdb_aging_time;
        enum dpsw_fdb_learning_mode learning_mode;
        u16 num_fdb_mc_groups;
        u16 max_fdb_mc_groups;
    }

.. _`dpsw_fdb_attr.members`:

Members
-------

max_fdb_entries
    Number of FDB entries

fdb_aging_time
    Aging time in seconds

learning_mode
    Learning mode

num_fdb_mc_groups
    Current number of multicast groups

max_fdb_mc_groups
    Maximum number of multicast groups

.. This file was automatic generated / don't edit.

