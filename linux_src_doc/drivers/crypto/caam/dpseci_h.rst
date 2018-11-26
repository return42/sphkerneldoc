.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/dpseci.h

.. _`dpseci_max_queue_num`:

DPSECI_MAX_QUEUE_NUM
====================

.. c:function::  DPSECI_MAX_QUEUE_NUM()

.. _`dpseci_all_queues`:

DPSECI_ALL_QUEUES
=================

.. c:function::  DPSECI_ALL_QUEUES()

.. _`dpseci_opt_has_cg`:

DPSECI_OPT_HAS_CG
=================

.. c:function::  DPSECI_OPT_HAS_CG()

.. _`dpseci_cfg`:

struct dpseci_cfg
=================

.. c:type:: struct dpseci_cfg

    Structure representing DPSECI configuration

.. _`dpseci_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_cfg {
        u32 options;
        u8 num_tx_queues;
        u8 num_rx_queues;
        u8 priorities[DPSECI_MAX_QUEUE_NUM];
    }

.. _`dpseci_cfg.members`:

Members
-------

options
    Any combination of the following flags:
    DPSECI_OPT_HAS_CG

num_tx_queues
    num of queues towards the SEC

num_rx_queues
    num of queues back from the SEC

priorities
    Priorities for the SEC hardware processing;
    each place in the array is the priority of the tx queue
    towards the SEC;
    valid priorities are configured with values 1-8;

.. _`dpseci_attr`:

struct dpseci_attr
==================

.. c:type:: struct dpseci_attr

    Structure representing DPSECI attributes

.. _`dpseci_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_attr {
        int id;
        u8 num_tx_queues;
        u8 num_rx_queues;
        u32 options;
    }

.. _`dpseci_attr.members`:

Members
-------

id
    DPSECI object ID

num_tx_queues
    number of queues towards the SEC

num_rx_queues
    number of queues back from the SEC

options
    any combination of the following flags:
    DPSECI_OPT_HAS_CG

.. _`dpseci_dest`:

enum dpseci_dest
================

.. c:type:: enum dpseci_dest

    DPSECI destination types

.. _`dpseci_dest.definition`:

Definition
----------

.. code-block:: c

    enum dpseci_dest {
        DPSECI_DEST_NONE,
        DPSECI_DEST_DPIO,
        DPSECI_DEST_DPCON
    };

.. _`dpseci_dest.constants`:

Constants
---------

DPSECI_DEST_NONE
    Unassigned destination; The queue is set in parked mode
    and does not generate FQDAN notifications; user is expected to dequeue
    from the queue based on polling or other user-defined method

DPSECI_DEST_DPIO
    The queue is set in schedule mode and generates FQDAN
    notifications to the specified DPIO; user is expected to dequeue from
    the queue only after notification is received

DPSECI_DEST_DPCON
    The queue is set in schedule mode and does not generate
    FQDAN notifications, but is connected to the specified DPCON object;
    user is expected to dequeue from the DPCON channel

.. _`dpseci_dest_cfg`:

struct dpseci_dest_cfg
======================

.. c:type:: struct dpseci_dest_cfg

    Structure representing DPSECI destination parameters

.. _`dpseci_dest_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_dest_cfg {
        enum dpseci_dest dest_type;
        int dest_id;
        u8 priority;
    }

.. _`dpseci_dest_cfg.members`:

Members
-------

dest_type
    Destination type

dest_id
    Either DPIO ID or DPCON ID, depending on the destination type

priority
    Priority selection within the DPIO or DPCON channel; valid values
    are 0-1 or 0-7, depending on the number of priorities in that channel;
    not relevant for 'DPSECI_DEST_NONE' option

.. _`dpseci_queue_opt_user_ctx`:

DPSECI_QUEUE_OPT_USER_CTX
=========================

.. c:function::  DPSECI_QUEUE_OPT_USER_CTX()

.. _`dpseci_queue_opt_dest`:

DPSECI_QUEUE_OPT_DEST
=====================

.. c:function::  DPSECI_QUEUE_OPT_DEST()

.. _`dpseci_queue_opt_order_preservation`:

DPSECI_QUEUE_OPT_ORDER_PRESERVATION
===================================

.. c:function::  DPSECI_QUEUE_OPT_ORDER_PRESERVATION()

.. _`dpseci_rx_queue_cfg`:

struct dpseci_rx_queue_cfg
==========================

.. c:type:: struct dpseci_rx_queue_cfg

    DPSECI RX queue configuration

.. _`dpseci_rx_queue_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_rx_queue_cfg {
        u32 options;
        int order_preservation_en;
        u64 user_ctx;
        struct dpseci_dest_cfg dest_cfg;
    }

.. _`dpseci_rx_queue_cfg.members`:

Members
-------

options
    Flags representing the suggested modifications to the queue;
    Use any combination of 'DPSECI_QUEUE_OPT_<X>' flags

order_preservation_en
    order preservation configuration for the rx queue
    valid only if 'DPSECI_QUEUE_OPT_ORDER_PRESERVATION' is contained in 'options'

user_ctx
    User context value provided in the frame descriptor of each
    dequeued frame; valid only if 'DPSECI_QUEUE_OPT_USER_CTX' is contained
    in 'options'

dest_cfg
    Queue destination parameters; valid only if
    'DPSECI_QUEUE_OPT_DEST' is contained in 'options'

.. _`dpseci_rx_queue_attr`:

struct dpseci_rx_queue_attr
===========================

.. c:type:: struct dpseci_rx_queue_attr

    Structure representing attributes of Rx queues

.. _`dpseci_rx_queue_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_rx_queue_attr {
        u64 user_ctx;
        int order_preservation_en;
        struct dpseci_dest_cfg dest_cfg;
        u32 fqid;
    }

.. _`dpseci_rx_queue_attr.members`:

Members
-------

user_ctx
    User context value provided in the frame descriptor of each
    dequeued frame

order_preservation_en
    Status of the order preservation configuration on the
    queue

dest_cfg
    Queue destination configuration

fqid
    Virtual FQID value to be used for dequeue operations

.. _`dpseci_tx_queue_attr`:

struct dpseci_tx_queue_attr
===========================

.. c:type:: struct dpseci_tx_queue_attr

    Structure representing attributes of Tx queues

.. _`dpseci_tx_queue_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_tx_queue_attr {
        u32 fqid;
        u8 priority;
    }

.. _`dpseci_tx_queue_attr.members`:

Members
-------

fqid
    Virtual FQID to be used for sending frames to SEC hardware

priority
    SEC hardware processing priority for the queue

.. _`dpseci_sec_attr`:

struct dpseci_sec_attr
======================

.. c:type:: struct dpseci_sec_attr

    Structure representing attributes of the SEC hardware accelerator

.. _`dpseci_sec_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_sec_attr {
        u16 ip_id;
        u8 major_rev;
        u8 minor_rev;
        u8 era;
        u8 deco_num;
        u8 zuc_auth_acc_num;
        u8 zuc_enc_acc_num;
        u8 snow_f8_acc_num;
        u8 snow_f9_acc_num;
        u8 crc_acc_num;
        u8 pk_acc_num;
        u8 kasumi_acc_num;
        u8 rng_acc_num;
        u8 md_acc_num;
        u8 arc4_acc_num;
        u8 des_acc_num;
        u8 aes_acc_num;
        u8 ccha_acc_num;
        u8 ptha_acc_num;
    }

.. _`dpseci_sec_attr.members`:

Members
-------

ip_id
    ID for SEC

major_rev
    Major revision number for SEC

minor_rev
    Minor revision number for SEC

era
    SEC Era

deco_num
    The number of copies of the DECO that are implemented in this
    version of SEC

zuc_auth_acc_num
    The number of copies of ZUCA that are implemented in this
    version of SEC

zuc_enc_acc_num
    The number of copies of ZUCE that are implemented in this
    version of SEC

snow_f8_acc_num
    The number of copies of the SNOW-f8 module that are
    implemented in this version of SEC

snow_f9_acc_num
    The number of copies of the SNOW-f9 module that are
    implemented in this version of SEC

crc_acc_num
    The number of copies of the CRC module that are implemented in
    this version of SEC

pk_acc_num
    The number of copies of the Public Key module that are
    implemented in this version of SEC

kasumi_acc_num
    The number of copies of the Kasumi module that are
    implemented in this version of SEC

rng_acc_num
    The number of copies of the Random Number Generator that are
    implemented in this version of SEC

md_acc_num
    The number of copies of the MDHA (Hashing module) that are
    implemented in this version of SEC

arc4_acc_num
    The number of copies of the ARC4 module that are implemented
    in this version of SEC

des_acc_num
    The number of copies of the DES module that are implemented in
    this version of SEC

aes_acc_num
    The number of copies of the AES module that are implemented in
    this version of SEC

ccha_acc_num
    The number of copies of the ChaCha20 module that are
    implemented in this version of SEC.

ptha_acc_num
    The number of copies of the Poly1305 module that are
    implemented in this version of SEC.

.. _`dpseci_congestion_unit`:

enum dpseci_congestion_unit
===========================

.. c:type:: enum dpseci_congestion_unit

    DPSECI congestion units

.. _`dpseci_congestion_unit.definition`:

Definition
----------

.. code-block:: c

    enum dpseci_congestion_unit {
        DPSECI_CONGESTION_UNIT_BYTES,
        DPSECI_CONGESTION_UNIT_FRAMES
    };

.. _`dpseci_congestion_unit.constants`:

Constants
---------

DPSECI_CONGESTION_UNIT_BYTES
    bytes units

DPSECI_CONGESTION_UNIT_FRAMES
    frames units

.. _`dpseci_cgn_mode_write_mem_on_enter`:

DPSECI_CGN_MODE_WRITE_MEM_ON_ENTER
==================================

.. c:function::  DPSECI_CGN_MODE_WRITE_MEM_ON_ENTER()

    congestion state (see 'threshold_entry')

.. _`dpseci_cgn_mode_write_mem_on_exit`:

DPSECI_CGN_MODE_WRITE_MEM_ON_EXIT
=================================

.. c:function::  DPSECI_CGN_MODE_WRITE_MEM_ON_EXIT()

    congestion state (see 'threshold_exit')

.. _`dpseci_cgn_mode_coherent_write`:

DPSECI_CGN_MODE_COHERENT_WRITE
==============================

.. c:function::  DPSECI_CGN_MODE_COHERENT_WRITE()

    valid only if 'DPSECI_CGN_MODE_WRITE_MEM_<X>' is selected

.. _`dpseci_cgn_mode_notify_dest_on_enter`:

DPSECI_CGN_MODE_NOTIFY_DEST_ON_ENTER
====================================

.. c:function::  DPSECI_CGN_MODE_NOTIFY_DEST_ON_ENTER()

    DPIO/DPCON's WQ channel once entering a congestion state (see 'threshold_entry')

.. _`dpseci_cgn_mode_notify_dest_on_exit`:

DPSECI_CGN_MODE_NOTIFY_DEST_ON_EXIT
===================================

.. c:function::  DPSECI_CGN_MODE_NOTIFY_DEST_ON_EXIT()

    DPIO/DPCON's WQ channel once exiting a congestion state (see 'threshold_exit')

.. _`dpseci_cgn_mode_intr_coalescing_disabled`:

DPSECI_CGN_MODE_INTR_COALESCING_DISABLED
========================================

.. c:function::  DPSECI_CGN_MODE_INTR_COALESCING_DISABLED()

    to the sw-portal's DQRR, the DQRI interrupt is asserted immediately (if enabled)

.. _`dpseci_congestion_notification_cfg`:

struct dpseci_congestion_notification_cfg
=========================================

.. c:type:: struct dpseci_congestion_notification_cfg

    congestion notification configuration

.. _`dpseci_congestion_notification_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpseci_congestion_notification_cfg {
        enum dpseci_congestion_unit units;
        u32 threshold_entry;
        u32 threshold_exit;
        u64 message_ctx;
        u64 message_iova;
        struct dpseci_dest_cfg dest_cfg;
        u16 notification_mode;
    }

.. _`dpseci_congestion_notification_cfg.members`:

Members
-------

units
    units type

threshold_entry
    above this threshold we enter a congestion state.
    set it to '0' to disable it

threshold_exit
    below this threshold we exit the congestion state.

message_ctx
    The context that will be part of the CSCN message

message_iova
    I/O virtual address (must be in DMA-able memory),
    must be 16B aligned;

dest_cfg
    CSCN can be send to either DPIO or DPCON WQ channel

notification_mode
    Mask of available options; use 'DPSECI_CGN_MODE_<X>'
    values

.. This file was automatic generated / don't edit.

