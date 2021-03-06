.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ice/ice_controlq.c

.. _`ice_adminq_init_regs`:

ice_adminq_init_regs
====================

.. c:function:: void ice_adminq_init_regs(struct ice_hw *hw)

    Initialize AdminQ registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_adminq_init_regs.description`:

Description
-----------

This assumes the alloc_sq and alloc_rq functions have already been called

.. _`ice_mailbox_init_regs`:

ice_mailbox_init_regs
=====================

.. c:function:: void ice_mailbox_init_regs(struct ice_hw *hw)

    Initialize Mailbox registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_mailbox_init_regs.description`:

Description
-----------

This assumes the alloc_sq and alloc_rq functions have already been called

.. _`ice_check_sq_alive`:

ice_check_sq_alive
==================

.. c:function:: bool ice_check_sq_alive(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_check_sq_alive.description`:

Description
-----------

Returns true if Queue is enabled else false.

.. _`ice_alloc_ctrlq_sq_ring`:

ice_alloc_ctrlq_sq_ring
=======================

.. c:function:: enum ice_status ice_alloc_ctrlq_sq_ring(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Allocate Control Transmit Queue (ATQ) rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_alloc_ctrlq_rq_ring`:

ice_alloc_ctrlq_rq_ring
=======================

.. c:function:: enum ice_status ice_alloc_ctrlq_rq_ring(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Allocate Control Receive Queue (ARQ) rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_free_ctrlq_sq_ring`:

ice_free_ctrlq_sq_ring
======================

.. c:function:: void ice_free_ctrlq_sq_ring(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Free Control Transmit Queue (ATQ) rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_free_ctrlq_sq_ring.description`:

Description
-----------

This assumes the posted send buffers have already been cleaned
and de-allocated

.. _`ice_free_ctrlq_rq_ring`:

ice_free_ctrlq_rq_ring
======================

.. c:function:: void ice_free_ctrlq_rq_ring(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Free Control Receive Queue (ARQ) rings

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_free_ctrlq_rq_ring.description`:

Description
-----------

This assumes the posted receive buffers have already been cleaned
and de-allocated

.. _`ice_alloc_rq_bufs`:

ice_alloc_rq_bufs
=================

.. c:function:: enum ice_status ice_alloc_rq_bufs(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Allocate pre-posted buffers for the ARQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_alloc_sq_bufs`:

ice_alloc_sq_bufs
=================

.. c:function:: enum ice_status ice_alloc_sq_bufs(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Allocate empty buffer structs for the ATQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_free_rq_bufs`:

ice_free_rq_bufs
================

.. c:function:: void ice_free_rq_bufs(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Free ARQ buffer info elements

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_free_sq_bufs`:

ice_free_sq_bufs
================

.. c:function:: void ice_free_sq_bufs(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    Free ATQ buffer info elements

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_cfg_sq_regs`:

ice_cfg_sq_regs
===============

.. c:function:: enum ice_status ice_cfg_sq_regs(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    configure Control ATQ registers

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_cfg_sq_regs.description`:

Description
-----------

Configure base address and length registers for the transmit queue

.. _`ice_cfg_rq_regs`:

ice_cfg_rq_regs
===============

.. c:function:: enum ice_status ice_cfg_rq_regs(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    configure Control ARQ register

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_cfg_rq_regs.description`:

Description
-----------

Configure base address and length registers for the receive (event q)

.. _`ice_init_sq`:

ice_init_sq
===========

.. c:function:: enum ice_status ice_init_sq(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    main initialization routine for Control ATQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_init_sq.description`:

Description
-----------

This is the main initialization routine for the Control Send Queue
Prior to calling this function, drivers \*MUST\* set the following fields
in the cq->structure:
- cq->num_sq_entries
- cq->sq_buf_size

Do \*NOT\* hold the lock when calling this as the memory allocation routines
called are not going to be atomic context safe

.. _`ice_init_rq`:

ice_init_rq
===========

.. c:function:: enum ice_status ice_init_rq(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    initialize ARQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_init_rq.description`:

Description
-----------

The main initialization routine for the Admin Receive (Event) Queue.
Prior to calling this function, drivers \*MUST\* set the following fields
in the cq->structure:
- cq->num_rq_entries
- cq->rq_buf_size

Do \*NOT\* hold the lock when calling this as the memory allocation routines
called are not going to be atomic context safe

.. _`ice_shutdown_sq`:

ice_shutdown_sq
===============

.. c:function:: enum ice_status ice_shutdown_sq(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    shutdown the Control ATQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_shutdown_sq.description`:

Description
-----------

The main shutdown routine for the Control Transmit Queue

.. _`ice_aq_ver_check`:

ice_aq_ver_check
================

.. c:function:: bool ice_aq_ver_check(struct ice_hw *hw)

    Check the reported AQ API version.

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_aq_ver_check.description`:

Description
-----------

Checks if the driver should load on a given AQ API version.

.. _`ice_aq_ver_check.return`:

Return
------

'true' iff the driver should attempt to load. 'false' otherwise.

.. _`ice_shutdown_rq`:

ice_shutdown_rq
===============

.. c:function:: enum ice_status ice_shutdown_rq(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    shutdown Control ARQ

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_shutdown_rq.description`:

Description
-----------

The main shutdown routine for the Control Receive Queue

.. _`ice_init_check_adminq`:

ice_init_check_adminq
=====================

.. c:function:: enum ice_status ice_init_check_adminq(struct ice_hw *hw)

    Check version for Admin Queue to know if its alive

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_init_ctrlq`:

ice_init_ctrlq
==============

.. c:function:: enum ice_status ice_init_ctrlq(struct ice_hw *hw, enum ice_ctl_q q_type)

    main initialization routine for any control Queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param q_type:
        specific Control queue type
    :type q_type: enum ice_ctl_q

.. _`ice_init_ctrlq.description`:

Description
-----------

Prior to calling this function, drivers \*MUST\* set the following fields
in the cq->structure:
- cq->num_sq_entries
- cq->num_rq_entries
- cq->rq_buf_size
- cq->sq_buf_size

.. _`ice_init_all_ctrlq`:

ice_init_all_ctrlq
==================

.. c:function:: enum ice_status ice_init_all_ctrlq(struct ice_hw *hw)

    main initialization routine for all control queues

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_init_all_ctrlq.description`:

Description
-----------

Prior to calling this function, drivers \*MUST\* set the following fields
in the cq->structure for all control queues:
- cq->num_sq_entries
- cq->num_rq_entries
- cq->rq_buf_size
- cq->sq_buf_size

.. _`ice_shutdown_ctrlq`:

ice_shutdown_ctrlq
==================

.. c:function:: void ice_shutdown_ctrlq(struct ice_hw *hw, enum ice_ctl_q q_type)

    shutdown routine for any control queue

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param q_type:
        specific Control queue type
    :type q_type: enum ice_ctl_q

.. _`ice_shutdown_all_ctrlq`:

ice_shutdown_all_ctrlq
======================

.. c:function:: void ice_shutdown_all_ctrlq(struct ice_hw *hw)

    shutdown routine for all control queues

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

.. _`ice_clean_sq`:

ice_clean_sq
============

.. c:function:: u16 ice_clean_sq(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    cleans Admin send queue (ATQ)

    :param hw:
        pointer to the hardware structure
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_clean_sq.description`:

Description
-----------

returns the number of free desc

.. _`ice_sq_done`:

ice_sq_done
===========

.. c:function:: bool ice_sq_done(struct ice_hw *hw, struct ice_ctl_q_info *cq)

    check if FW has processed the Admin Send Queue (ATQ)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

.. _`ice_sq_done.description`:

Description
-----------

Returns true if the firmware has processed all descriptors on the
admin send queue. Returns false if there are still requests pending.

.. _`ice_sq_send_cmd`:

ice_sq_send_cmd
===============

.. c:function:: enum ice_status ice_sq_send_cmd(struct ice_hw *hw, struct ice_ctl_q_info *cq, struct ice_aq_desc *desc, void *buf, u16 buf_size, struct ice_sq_cd *cd)

    send command to Control Queue (ATQ)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

    :param desc:
        prefilled descriptor describing the command (non DMA mem)
    :type desc: struct ice_aq_desc \*

    :param buf:
        buffer to use for indirect commands (or NULL for direct commands)
    :type buf: void \*

    :param buf_size:
        size of buffer for indirect commands (or 0 for direct commands)
    :type buf_size: u16

    :param cd:
        pointer to command details structure
    :type cd: struct ice_sq_cd \*

.. _`ice_sq_send_cmd.description`:

Description
-----------

This is the main send command routine for the ATQ.  It runs the q,
cleans the queue, etc.

.. _`ice_fill_dflt_direct_cmd_desc`:

ice_fill_dflt_direct_cmd_desc
=============================

.. c:function:: void ice_fill_dflt_direct_cmd_desc(struct ice_aq_desc *desc, u16 opcode)

    AQ descriptor helper function

    :param desc:
        pointer to the temp descriptor (non DMA mem)
    :type desc: struct ice_aq_desc \*

    :param opcode:
        the opcode can be used to decide which flags to turn off or on
    :type opcode: u16

.. _`ice_fill_dflt_direct_cmd_desc.description`:

Description
-----------

Fill the desc with default values

.. _`ice_clean_rq_elem`:

ice_clean_rq_elem
=================

.. c:function:: enum ice_status ice_clean_rq_elem(struct ice_hw *hw, struct ice_ctl_q_info *cq, struct ice_rq_event_info *e, u16 *pending)

    :param hw:
        pointer to the hw struct
    :type hw: struct ice_hw \*

    :param cq:
        pointer to the specific Control queue
    :type cq: struct ice_ctl_q_info \*

    :param e:
        event info from the receive descriptor, includes any buffers
    :type e: struct ice_rq_event_info \*

    :param pending:
        number of events that could be left to process
    :type pending: u16 \*

.. _`ice_clean_rq_elem.description`:

Description
-----------

This function cleans one Admin Receive Queue element and returns
the contents through e.  It can also return how many events are
left to process through 'pending'.

.. This file was automatic generated / don't edit.

