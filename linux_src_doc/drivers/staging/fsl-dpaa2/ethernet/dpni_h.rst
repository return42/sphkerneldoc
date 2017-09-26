.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-dpaa2/ethernet/dpni.h

.. _`dpni_max_tc`:

DPNI_MAX_TC
===========

.. c:function::  DPNI_MAX_TC()

    Contains initialization APIs and runtime control APIs for DPNI

.. _`dpni_max_dpbp`:

DPNI_MAX_DPBP
=============

.. c:function::  DPNI_MAX_DPBP()

.. _`dpni_all_tcs`:

DPNI_ALL_TCS
============

.. c:function::  DPNI_ALL_TCS()

.. _`dpni_all_tc_flows`:

DPNI_ALL_TC_FLOWS
=================

.. c:function::  DPNI_ALL_TC_FLOWS()

.. _`dpni_new_flow_id`:

DPNI_NEW_FLOW_ID
================

.. c:function::  DPNI_NEW_FLOW_ID()

.. _`dpni_opt_tx_frm_release`:

DPNI_OPT_TX_FRM_RELEASE
=======================

.. c:function::  DPNI_OPT_TX_FRM_RELEASE()

    resources allocated to have the frames confirmed back to the source after transmission.

.. _`dpni_opt_no_mac_filter`:

DPNI_OPT_NO_MAC_FILTER
======================

.. c:function::  DPNI_OPT_NO_MAC_FILTER()

    MAC address. This affects both unicast and multicast. Promiscuous mode can still be enabled/disabled for both unicast and multicast. If promiscuous mode is disabled, only traffic matching the primary MAC address will be accepted.

.. _`dpni_opt_has_policing`:

DPNI_OPT_HAS_POLICING
=====================

.. c:function::  DPNI_OPT_HAS_POLICING()

    limit traffic per traffic class (TC) basis.

.. _`dpni_opt_shared_congestion`:

DPNI_OPT_SHARED_CONGESTION
==========================

.. c:function::  DPNI_OPT_SHARED_CONGESTION()

    deplete on ingress, taildrop on each queue or use congestion groups for sets of queues. If set, it configures a single congestion groups across all TCs. If reset, a congestion group is allocated for each TC. Only relevant if the DPNI has multiple traffic classes.

.. _`dpni_opt_has_key_masking`:

DPNI_OPT_HAS_KEY_MASKING
========================

.. c:function::  DPNI_OPT_HAS_KEY_MASKING()

    ups. If not specified, all look-ups are exact match. Note that TCAM is not available on LS1088 and its variants. Setting this bit on these SoCs will trigger an error.

.. _`dpni_opt_no_fs`:

DPNI_OPT_NO_FS
==============

.. c:function::  DPNI_OPT_NO_FS()

.. _`dpni_pools_cfg`:

struct dpni_pools_cfg
=====================

.. c:type:: struct dpni_pools_cfg

    Structure representing buffer pools configuration

.. _`dpni_pools_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpni_pools_cfg {
        u8 num_dpbp;
        struct {
            int dpbp_id;
            u16 buffer_size;
            int backup_pool;
        } pools[DPNI_MAX_DPBP];
    }

.. _`dpni_pools_cfg.members`:

Members
-------

num_dpbp
    Number of DPBPs

pools
    Array of buffer pools parameters; The number of valid entries
    must match 'num_dpbp' value

dpbp_id
    *undescribed*

buffer_size
    *undescribed*

backup_pool
    *undescribed*

.. _`dpni_irq_index`:

DPNI_IRQ_INDEX
==============

.. c:function::  DPNI_IRQ_INDEX()

.. _`dpni_irq_event_link_changed`:

DPNI_IRQ_EVENT_LINK_CHANGED
===========================

.. c:function::  DPNI_IRQ_EVENT_LINK_CHANGED()

    indicates a change in link state

.. _`dpni_attr`:

struct dpni_attr
================

.. c:type:: struct dpni_attr

    Structure representing DPNI attributes

.. _`dpni_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpni_attr {
        u32 options;
        u8 num_queues;
        u8 num_tcs;
        u8 mac_filter_entries;
        u8 vlan_filter_entries;
        u8 qos_entries;
        u16 fs_entries;
        u8 qos_key_size;
        u8 fs_key_size;
        u16 wriop_version;
    }

.. _`dpni_attr.members`:

Members
-------

options
    Any combination of the following options:
    DPNI_OPT_TX_FRM_RELEASE
    DPNI_OPT_NO_MAC_FILTER
    DPNI_OPT_HAS_POLICING
    DPNI_OPT_SHARED_CONGESTION
    DPNI_OPT_HAS_KEY_MASKING
    DPNI_OPT_NO_FS

num_queues
    Number of Tx and Rx queues used for traffic distribution.

num_tcs
    Number of traffic classes (TCs), reserved for the DPNI.

mac_filter_entries
    Number of entries in the MAC address filtering table.

vlan_filter_entries
    Number of entries in the VLAN address filtering table.

qos_entries
    Number of entries in the QoS classification table.

fs_entries
    Number of entries in the flow steering table.

qos_key_size
    Size, in bytes, of the QoS look-up key. Defining a key larger
    than this when adding QoS entries will result in an error.

fs_key_size
    Size, in bytes, of the flow steering look-up key. Defining a
    key larger than this when composing the hash + FS key will
    result in an error.

wriop_version
    Version of WRIOP HW block. The 3 version values are stored
    on 6, 5, 5 bits respectively.

.. _`dpni_error_eofhe`:

DPNI_ERROR_EOFHE
================

.. c:function::  DPNI_ERROR_EOFHE()

.. _`dpni_error_fle`:

DPNI_ERROR_FLE
==============

.. c:function::  DPNI_ERROR_FLE()

.. _`dpni_error_fpe`:

DPNI_ERROR_FPE
==============

.. c:function::  DPNI_ERROR_FPE()

.. _`dpni_error_phe`:

DPNI_ERROR_PHE
==============

.. c:function::  DPNI_ERROR_PHE()

.. _`dpni_error_l3ce`:

DPNI_ERROR_L3CE
===============

.. c:function::  DPNI_ERROR_L3CE()

.. _`dpni_error_l4ce`:

DPNI_ERROR_L4CE
===============

.. c:function::  DPNI_ERROR_L4CE()

.. _`dpni_error_action`:

enum dpni_error_action
======================

.. c:type:: enum dpni_error_action

    Defines DPNI behavior for errors

.. _`dpni_error_action.definition`:

Definition
----------

.. code-block:: c

    enum dpni_error_action {
        DPNI_ERROR_ACTION_DISCARD,
        DPNI_ERROR_ACTION_CONTINUE,
        DPNI_ERROR_ACTION_SEND_TO_ERROR_QUEUE
    };

.. _`dpni_error_action.constants`:

Constants
---------

DPNI_ERROR_ACTION_DISCARD
    Discard the frame

DPNI_ERROR_ACTION_CONTINUE
    Continue with the normal flow

DPNI_ERROR_ACTION_SEND_TO_ERROR_QUEUE
    Send the frame to the error queue

.. _`dpni_error_cfg`:

struct dpni_error_cfg
=====================

.. c:type:: struct dpni_error_cfg

    Structure representing DPNI errors treatment

.. _`dpni_error_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpni_error_cfg {
        u32 errors;
        enum dpni_error_action error_action;
        int set_frame_annotation;
    }

.. _`dpni_error_cfg.members`:

Members
-------

errors
    Errors mask; use 'DPNI_ERROR__<X>

error_action
    The desired action for the errors mask

set_frame_annotation
    Set to '1' to mark the errors in frame annotation
    status (FAS); relevant only for the non-discard action

.. _`dpni_buf_layout_opt_timestamp`:

DPNI_BUF_LAYOUT_OPT_TIMESTAMP
=============================

.. c:function::  DPNI_BUF_LAYOUT_OPT_TIMESTAMP()

.. _`dpni_buf_layout_opt_parser_result`:

DPNI_BUF_LAYOUT_OPT_PARSER_RESULT
=================================

.. c:function::  DPNI_BUF_LAYOUT_OPT_PARSER_RESULT()

    result setting; not applicable for Tx

.. _`dpni_buf_layout_opt_frame_status`:

DPNI_BUF_LAYOUT_OPT_FRAME_STATUS
================================

.. c:function::  DPNI_BUF_LAYOUT_OPT_FRAME_STATUS()

    status setting

.. _`dpni_buf_layout_opt_private_data_size`:

DPNI_BUF_LAYOUT_OPT_PRIVATE_DATA_SIZE
=====================================

.. c:function::  DPNI_BUF_LAYOUT_OPT_PRIVATE_DATA_SIZE()

    data-size setting

.. _`dpni_buf_layout_opt_data_align`:

DPNI_BUF_LAYOUT_OPT_DATA_ALIGN
==============================

.. c:function::  DPNI_BUF_LAYOUT_OPT_DATA_ALIGN()

    alignment setting

.. _`dpni_buf_layout_opt_data_head_room`:

DPNI_BUF_LAYOUT_OPT_DATA_HEAD_ROOM
==================================

.. c:function::  DPNI_BUF_LAYOUT_OPT_DATA_HEAD_ROOM()

    head-room setting

.. _`dpni_buf_layout_opt_data_tail_room`:

DPNI_BUF_LAYOUT_OPT_DATA_TAIL_ROOM
==================================

.. c:function::  DPNI_BUF_LAYOUT_OPT_DATA_TAIL_ROOM()

    tail-room setting

.. _`dpni_buffer_layout`:

struct dpni_buffer_layout
=========================

.. c:type:: struct dpni_buffer_layout

    Structure representing DPNI buffer layout

.. _`dpni_buffer_layout.definition`:

Definition
----------

.. code-block:: c

    struct dpni_buffer_layout {
        u32 options;
        int pass_timestamp;
        int pass_parser_result;
        int pass_frame_status;
        u16 private_data_size;
        u16 data_align;
        u16 data_head_room;
        u16 data_tail_room;
    }

.. _`dpni_buffer_layout.members`:

Members
-------

options
    Flags representing the suggested modifications to the buffer
    layout; Use any combination of 'DPNI_BUF_LAYOUT_OPT_<X>' flags

pass_timestamp
    Pass timestamp value

pass_parser_result
    Pass parser results

pass_frame_status
    Pass frame status

private_data_size
    Size kept for private data (in bytes)

data_align
    Data alignment

data_head_room
    Data head room

data_tail_room
    Data tail room

.. _`dpni_offload`:

enum dpni_offload
=================

.. c:type:: enum dpni_offload

    Identifies a type of queue targeted by the command

.. _`dpni_offload.definition`:

Definition
----------

.. code-block:: c

    enum dpni_offload {
        DPNI_OFF_RX_L3_CSUM,
        DPNI_OFF_RX_L4_CSUM,
        DPNI_OFF_TX_L3_CSUM,
        DPNI_OFF_TX_L4_CSUM,
         } ;int dpni_set_offload(struct fsl_mc_io *mc_io,
        u32,
        u16,
        enum,
        u32,
        u32,
        u16,
        enum,
        u32,
        u32,
        u16,
        enum,
        u16,
        u32,
        u16,
        u16
    };

.. _`dpni_offload.constants`:

Constants
---------

DPNI_OFF_RX_L3_CSUM
    *undescribed*

DPNI_OFF_RX_L4_CSUM
    *undescribed*

DPNI_OFF_TX_L3_CSUM
    *undescribed*

DPNI_OFF_TX_L4_CSUM
    *undescribed*

} ;int dpni_set_offload(struct fsl_mc_io \*mc_io
    *undescribed*

u32
    *undescribed*

u16
    *undescribed*

enum
    *undescribed*

u32
    *undescribed*

u32
    *undescribed*

u16
    *undescribed*

enum
    *undescribed*

u32
    *undescribed*

u32
    *undescribed*

u16
    *undescribed*

enum
    *undescribed*

u16
    *undescribed*

u32
    *undescribed*

u16
    *undescribed*

u16
    *undescribed*

.. _`dpni_link_opt_autoneg`:

DPNI_LINK_OPT_AUTONEG
=====================

.. c:function::  DPNI_LINK_OPT_AUTONEG()

    negotiation

.. _`dpni_link_opt_half_duplex`:

DPNI_LINK_OPT_HALF_DUPLEX
=========================

.. c:function::  DPNI_LINK_OPT_HALF_DUPLEX()

    duplex mode

.. _`dpni_link_opt_pause`:

DPNI_LINK_OPT_PAUSE
===================

.. c:function::  DPNI_LINK_OPT_PAUSE()

.. _`dpni_link_opt_asym_pause`:

DPNI_LINK_OPT_ASYM_PAUSE
========================

.. c:function::  DPNI_LINK_OPT_ASYM_PAUSE()

    symmetric pause frames

.. _`dpni_link_state`:

struct dpni_link_state
======================

.. c:type:: struct dpni_link_state

    Structure representing DPNI link state

.. _`dpni_link_state.definition`:

Definition
----------

.. code-block:: c

    struct dpni_link_state {
        u32 rate;
        u64 options;
        int up;
    }

.. _`dpni_link_state.members`:

Members
-------

rate
    Rate

options
    Mask of available options; use 'DPNI_LINK_OPT_<X>' values

up
    Link state; '0' for down, '1' for up

.. _`dpni_dist_mode`:

enum dpni_dist_mode
===================

.. c:type:: enum dpni_dist_mode

    DPNI distribution mode

.. _`dpni_dist_mode.definition`:

Definition
----------

.. code-block:: c

    enum dpni_dist_mode {
        DPNI_DIST_MODE_NONE,
        DPNI_DIST_MODE_HASH,
        DPNI_DIST_MODE_FS
    };

.. _`dpni_dist_mode.constants`:

Constants
---------

DPNI_DIST_MODE_NONE
    No distribution

DPNI_DIST_MODE_HASH
    Use hash distribution; only relevant if
    the 'DPNI_OPT_DIST_HASH' option was set at DPNI creation

DPNI_DIST_MODE_FS
    Use explicit flow steering; only relevant if
    the 'DPNI_OPT_DIST_FS' option was set at DPNI creation

.. _`dpni_fs_miss_action`:

enum dpni_fs_miss_action
========================

.. c:type:: enum dpni_fs_miss_action

    DPNI Flow Steering miss action

.. _`dpni_fs_miss_action.definition`:

Definition
----------

.. code-block:: c

    enum dpni_fs_miss_action {
        DPNI_FS_MISS_DROP,
        DPNI_FS_MISS_EXPLICIT_FLOWID,
        DPNI_FS_MISS_HASH
    };

.. _`dpni_fs_miss_action.constants`:

Constants
---------

DPNI_FS_MISS_DROP
    In case of no-match, drop the frame

DPNI_FS_MISS_EXPLICIT_FLOWID
    In case of no-match, use explicit flow-id

DPNI_FS_MISS_HASH
    In case of no-match, distribute using hash

.. _`dpni_fs_tbl_cfg`:

struct dpni_fs_tbl_cfg
======================

.. c:type:: struct dpni_fs_tbl_cfg

    Flow Steering table configuration

.. _`dpni_fs_tbl_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpni_fs_tbl_cfg {
        enum dpni_fs_miss_action miss_action;
        u16 default_flow_id;
    }

.. _`dpni_fs_tbl_cfg.members`:

Members
-------

miss_action
    Miss action selection

default_flow_id
    Used when 'miss_action = DPNI_FS_MISS_EXPLICIT_FLOWID'

.. _`dpni_rx_tc_dist_cfg`:

struct dpni_rx_tc_dist_cfg
==========================

.. c:type:: struct dpni_rx_tc_dist_cfg

    Rx traffic class distribution configuration

.. _`dpni_rx_tc_dist_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpni_rx_tc_dist_cfg {
        u16 dist_size;
        enum dpni_dist_mode dist_mode;
        u64 key_cfg_iova;
        struct dpni_fs_tbl_cfg fs_cfg;
    }

.. _`dpni_rx_tc_dist_cfg.members`:

Members
-------

dist_size
    Set the distribution size;

dist_mode
    Distribution mode

key_cfg_iova
    I/O virtual address of 256 bytes DMA-able memory filled with
    the extractions to be used for the distribution key by calling
    \ :c:func:`dpni_prepare_key_cfg`\  relevant only when
    'dist_mode != DPNI_DIST_MODE_NONE', otherwise it can be '0'

fs_cfg
    Flow Steering table configuration; only relevant if
    'dist_mode = DPNI_DIST_MODE_FS'

.. _`dpni_rx_tc_dist_cfg.supported-values`:

supported values
----------------

1,2,3,4,6,7,8,12,14,16,24,28,32,48,56,64,96,
112,128,192,224,256,384,448,512,768,896,1024

.. _`dpni_dest`:

enum dpni_dest
==============

.. c:type:: enum dpni_dest

    DPNI destination types

.. _`dpni_dest.definition`:

Definition
----------

.. code-block:: c

    enum dpni_dest {
        DPNI_DEST_NONE,
        DPNI_DEST_DPIO,
        DPNI_DEST_DPCON
    };

.. _`dpni_dest.constants`:

Constants
---------

DPNI_DEST_NONE
    Unassigned destination; The queue is set in parked mode and
    does not generate FQDAN notifications; user is expected to
    dequeue from the queue based on polling or other user-defined
    method

DPNI_DEST_DPIO
    The queue is set in schedule mode and generates FQDAN
    notifications to the specified DPIO; user is expected to dequeue
    from the queue only after notification is received

DPNI_DEST_DPCON
    The queue is set in schedule mode and does not generate
    FQDAN notifications, but is connected to the specified DPCON
    object; user is expected to dequeue from the DPCON channel

.. _`dpni_queue`:

struct dpni_queue
=================

.. c:type:: struct dpni_queue

    Queue structure

.. _`dpni_queue.definition`:

Definition
----------

.. code-block:: c

    struct dpni_queue {
        struct {
            u16 id;
            enum dpni_dest type;
            char hold_active;
            u8 priority;
        } destination;
        u64 user_context;
        struct {
            u64 value;
            char stash_control;
        } flc;
    }

.. _`dpni_queue.members`:

Members
-------

destination
    *undescribed*

id
    *undescribed*

type
    *undescribed*

hold_active
    *undescribed*

priority
    *undescribed*

user_context
    User data, presented to the user along with any frames from
    this queue. Not relevant for Tx queues.

flc
    *undescribed*

value
    *undescribed*

stash_control
    *undescribed*

.. _`dpni_queue_id`:

struct dpni_queue_id
====================

.. c:type:: struct dpni_queue_id

    Queue identification, used for enqueue commands or queue control

.. _`dpni_queue_id.definition`:

Definition
----------

.. code-block:: c

    struct dpni_queue_id {
        u32 fqid;
        u16 qdbin;
    }

.. _`dpni_queue_id.members`:

Members
-------

fqid
    FQID used for enqueueing to and/or configuration of this specific FQ

qdbin
    Queueing bin, used to enqueue using QDID, DQBIN, QPRI. Only relevant
    for Tx queues.

.. _`dpni_queue_opt_user_ctx`:

DPNI_QUEUE_OPT_USER_CTX
=======================

.. c:function::  DPNI_QUEUE_OPT_USER_CTX()

.. _`dpni_congestion_unit`:

enum dpni_congestion_unit
=========================

.. c:type:: enum dpni_congestion_unit

    DPNI congestion units

.. _`dpni_congestion_unit.definition`:

Definition
----------

.. code-block:: c

    enum dpni_congestion_unit {
        DPNI_CONGESTION_UNIT_BYTES,
        DPNI_CONGESTION_UNIT_FRAMES
    };

.. _`dpni_congestion_unit.constants`:

Constants
---------

DPNI_CONGESTION_UNIT_BYTES
    bytes units

DPNI_CONGESTION_UNIT_FRAMES
    frames units

.. _`dpni_congestion_point`:

enum dpni_congestion_point
==========================

.. c:type:: enum dpni_congestion_point

    Structure representing congestion point

.. _`dpni_congestion_point.definition`:

Definition
----------

.. code-block:: c

    enum dpni_congestion_point {
        DPNI_CP_QUEUE,
        DPNI_CP_GROUP
    };

.. _`dpni_congestion_point.constants`:

Constants
---------

DPNI_CP_QUEUE
    Set taildrop per queue, identified by QUEUE_TYPE, TC and
    QUEUE_INDEX

DPNI_CP_GROUP
    Set taildrop per queue group. Depending on options used to
    define the DPNI this can be either per TC (default) or per
    interface (DPNI_OPT_SHARED_CONGESTION set at DPNI create).
    QUEUE_INDEX is ignored if this type is used.

.. _`dpni_taildrop`:

struct dpni_taildrop
====================

.. c:type:: struct dpni_taildrop

    Structure representing the taildrop

.. _`dpni_taildrop.definition`:

Definition
----------

.. code-block:: c

    struct dpni_taildrop {
        char enable;
        enum dpni_congestion_unit units;
        u32 threshold;
    }

.. _`dpni_taildrop.members`:

Members
-------

enable
    Indicates whether the taildrop is active or not.

units
    Indicates the unit of THRESHOLD. Queue taildrop only supports
    byte units, this field is ignored and assumed = 0 if
    CONGESTION_POINT is 0.

threshold
    Threshold value, in units identified by UNITS field. Value 0
    cannot be used as a valid taildrop threshold, THRESHOLD must
    be > 0 if the taildrop is enabled.

.. _`dpni_rule_cfg`:

struct dpni_rule_cfg
====================

.. c:type:: struct dpni_rule_cfg

    Rule configuration for table lookup

.. _`dpni_rule_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpni_rule_cfg {
        u64 key_iova;
        u64 mask_iova;
        u8 key_size;
    }

.. _`dpni_rule_cfg.members`:

Members
-------

key_iova
    I/O virtual address of the key (must be in DMA-able memory)

mask_iova
    I/O virtual address of the mask (must be in DMA-able memory)

key_size
    key and mask size (in bytes)

.. This file was automatic generated / don't edit.

