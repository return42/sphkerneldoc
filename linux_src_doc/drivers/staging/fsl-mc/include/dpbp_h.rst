.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dpbp.h

.. _`dpbp_cfg`:

struct dpbp_cfg
===============

.. c:type:: struct dpbp_cfg

    Structure representing DPBP configuration

.. _`dpbp_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpbp_cfg {
        u32 options;
    }

.. _`dpbp_cfg.members`:

Members
-------

options
    place holder

.. _`dpbp_irq_cfg`:

struct dpbp_irq_cfg
===================

.. c:type:: struct dpbp_irq_cfg

    IRQ configuration

.. _`dpbp_irq_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpbp_irq_cfg {
        u64 addr;
        u32 val;
        int irq_num;
    }

.. _`dpbp_irq_cfg.members`:

Members
-------

addr
    Address that must be written to signal a message-based interrupt

val
    Value to write into irq_addr address

irq_num
    A user defined number associated with this IRQ

.. _`dpbp_attr`:

struct dpbp_attr
================

.. c:type:: struct dpbp_attr

    Structure representing DPBP attributes

.. _`dpbp_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpbp_attr {
        int id;
        struct version;
        u16 bpid;
    }

.. _`dpbp_attr.members`:

Members
-------

id
    DPBP object ID

version
    DPBP version

bpid
    Hardware buffer pool ID; should be used as an argument in
    acquire/release operations on buffers

.. _`dpbp_notif_opt_coherent_write`:

DPBP_NOTIF_OPT_COHERENT_WRITE
=============================

.. c:function::  DPBP_NOTIF_OPT_COHERENT_WRITE()

.. _`dpbp_notification_cfg`:

struct dpbp_notification_cfg
============================

.. c:type:: struct dpbp_notification_cfg

    Structure representing DPBP notifications towards software

.. _`dpbp_notification_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpbp_notification_cfg {
        u32 depletion_entry;
        u32 depletion_exit;
        u32 surplus_entry;
        u32 surplus_exit;
        u64 message_iova;
        u64 message_ctx;
        u16 options;
    }

.. _`dpbp_notification_cfg.members`:

Members
-------

depletion_entry
    below this threshold the pool is "depleted";
    set it to '0' to disable it

depletion_exit
    greater than or equal to this threshold the pool exit its
    "depleted" state

surplus_entry
    above this threshold the pool is in "surplus" state;
    set it to '0' to disable it

surplus_exit
    less than or equal to this threshold the pool exit its
    "surplus" state

message_iova
    MUST be given if either 'depletion_entry' or 'surplus_entry'
    is not '0' (enable); I/O virtual address (must be in DMA-able memory),
    must be 16B aligned.

message_ctx
    The context that will be part of the BPSCN message and will
    be written to 'message_iova'

options
    Mask of available options; use 'DPBP_NOTIF_OPT_<X>' values

.. This file was automatic generated / don't edit.

