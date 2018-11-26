.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_transport.c

.. _`transport_init_session`:

transport_init_session
======================

.. c:function:: void transport_init_session(struct se_session *se_sess)

    initialize a session object

    :param se_sess:
        Session object pointer.
    :type se_sess: struct se_session \*

.. _`transport_init_session.description`:

Description
-----------

The caller must have zero-initialized \ ``se_sess``\  before calling this function.

.. _`transport_alloc_session`:

transport_alloc_session
=======================

.. c:function:: struct se_session *transport_alloc_session(enum target_prot_op sup_prot_ops)

    allocate a session object and initialize it

    :param sup_prot_ops:
        bitmask that defines which T10-PI modes are supported.
    :type sup_prot_ops: enum target_prot_op

.. _`transport_alloc_session_tags`:

transport_alloc_session_tags
============================

.. c:function:: int transport_alloc_session_tags(struct se_session *se_sess, unsigned int tag_num, unsigned int tag_size)

    allocate target driver private data

    :param se_sess:
        Session pointer.
    :type se_sess: struct se_session \*

    :param tag_num:
        Maximum number of in-flight commands between initiator and target.
    :type tag_num: unsigned int

    :param tag_size:
        Size in bytes of the private data a target driver associates with
        each command.
    :type tag_size: unsigned int

.. _`transport_init_session_tags`:

transport_init_session_tags
===========================

.. c:function:: struct se_session *transport_init_session_tags(unsigned int tag_num, unsigned int tag_size, enum target_prot_op sup_prot_ops)

    allocate a session and target driver private data

    :param tag_num:
        Maximum number of in-flight commands between initiator and target.
    :type tag_num: unsigned int

    :param tag_size:
        Size in bytes of the private data a target driver associates with
        each command.
    :type tag_size: unsigned int

    :param sup_prot_ops:
        bitmask that defines which T10-PI modes are supported.
    :type sup_prot_ops: enum target_prot_op

.. _`target_submit_cmd_map_sgls`:

target_submit_cmd_map_sgls
==========================

.. c:function:: int target_submit_cmd_map_sgls(struct se_cmd *se_cmd, struct se_session *se_sess, unsigned char *cdb, unsigned char *sense, u64 unpacked_lun, u32 data_length, int task_attr, int data_dir, int flags, struct scatterlist *sgl, u32 sgl_count, struct scatterlist *sgl_bidi, u32 sgl_bidi_count, struct scatterlist *sgl_prot, u32 sgl_prot_count)

    lookup unpacked lun and submit uninitialized se_cmd + use pre-allocated SGL memory.

    :param se_cmd:
        command descriptor to submit
    :type se_cmd: struct se_cmd \*

    :param se_sess:
        associated se_sess for endpoint
    :type se_sess: struct se_session \*

    :param cdb:
        pointer to SCSI CDB
    :type cdb: unsigned char \*

    :param sense:
        pointer to SCSI sense buffer
    :type sense: unsigned char \*

    :param unpacked_lun:
        unpacked LUN to reference for struct se_lun
    :type unpacked_lun: u64

    :param data_length:
        fabric expected data transfer length
    :type data_length: u32

    :param task_attr:
        SAM task attribute
    :type task_attr: int

    :param data_dir:
        DMA data direction
    :type data_dir: int

    :param flags:
        flags for command submission from target_sc_flags_tables
    :type flags: int

    :param sgl:
        struct scatterlist memory for unidirectional mapping
    :type sgl: struct scatterlist \*

    :param sgl_count:
        scatterlist count for unidirectional mapping
    :type sgl_count: u32

    :param sgl_bidi:
        struct scatterlist memory for bidirectional READ mapping
    :type sgl_bidi: struct scatterlist \*

    :param sgl_bidi_count:
        scatterlist count for bidirectional READ mapping
    :type sgl_bidi_count: u32

    :param sgl_prot:
        struct scatterlist memory protection information
    :type sgl_prot: struct scatterlist \*

    :param sgl_prot_count:
        scatterlist count for protection information
    :type sgl_prot_count: u32

.. _`target_submit_cmd_map_sgls.description`:

Description
-----------

Task tags are supported if the caller has set \ ``se_cmd->tag``\ .

Returns non zero to signal active I/O shutdown failure.  All other
setup exceptions will be returned as a SCSI CHECK_CONDITION response,
but still return zero here.

This may only be called from process context, and also currently
assumes internal allocation of fabric payload buffer by target-core.

.. _`target_submit_cmd`:

target_submit_cmd
=================

.. c:function:: int target_submit_cmd(struct se_cmd *se_cmd, struct se_session *se_sess, unsigned char *cdb, unsigned char *sense, u64 unpacked_lun, u32 data_length, int task_attr, int data_dir, int flags)

    lookup unpacked lun and submit uninitialized se_cmd

    :param se_cmd:
        command descriptor to submit
    :type se_cmd: struct se_cmd \*

    :param se_sess:
        associated se_sess for endpoint
    :type se_sess: struct se_session \*

    :param cdb:
        pointer to SCSI CDB
    :type cdb: unsigned char \*

    :param sense:
        pointer to SCSI sense buffer
    :type sense: unsigned char \*

    :param unpacked_lun:
        unpacked LUN to reference for struct se_lun
    :type unpacked_lun: u64

    :param data_length:
        fabric expected data transfer length
    :type data_length: u32

    :param task_attr:
        SAM task attribute
    :type task_attr: int

    :param data_dir:
        DMA data direction
    :type data_dir: int

    :param flags:
        flags for command submission from target_sc_flags_tables
    :type flags: int

.. _`target_submit_cmd.description`:

Description
-----------

Task tags are supported if the caller has set \ ``se_cmd->tag``\ .

Returns non zero to signal active I/O shutdown failure.  All other
setup exceptions will be returned as a SCSI CHECK_CONDITION response,
but still return zero here.

This may only be called from process context, and also currently
assumes internal allocation of fabric payload buffer by target-core.

It also assumes interal target core SGL memory allocation.

.. _`target_submit_tmr`:

target_submit_tmr
=================

.. c:function:: int target_submit_tmr(struct se_cmd *se_cmd, struct se_session *se_sess, unsigned char *sense, u64 unpacked_lun, void *fabric_tmr_ptr, unsigned char tm_type, gfp_t gfp, u64 tag, int flags)

    lookup unpacked lun and submit uninitialized se_cmd for TMR CDBs

    :param se_cmd:
        command descriptor to submit
    :type se_cmd: struct se_cmd \*

    :param se_sess:
        associated se_sess for endpoint
    :type se_sess: struct se_session \*

    :param sense:
        pointer to SCSI sense buffer
    :type sense: unsigned char \*

    :param unpacked_lun:
        unpacked LUN to reference for struct se_lun
    :type unpacked_lun: u64

    :param fabric_tmr_ptr:
        fabric context for TMR req
    :type fabric_tmr_ptr: void \*

    :param tm_type:
        Type of TM request
    :type tm_type: unsigned char

    :param gfp:
        gfp type for caller
    :type gfp: gfp_t

    :param tag:
        referenced task tag for TMR_ABORT_TASK
    :type tag: u64

    :param flags:
        submit cmd flags
    :type flags: int

.. _`target_submit_tmr.description`:

Description
-----------

Callable from all contexts.

.. _`target_get_sess_cmd`:

target_get_sess_cmd
===================

.. c:function:: int target_get_sess_cmd(struct se_cmd *se_cmd, bool ack_kref)

    Add command to active ->sess_cmd_list

    :param se_cmd:
        command descriptor to add
    :type se_cmd: struct se_cmd \*

    :param ack_kref:
        Signal that fabric will perform an ack \ :c:func:`target_put_sess_cmd`\ 
    :type ack_kref: bool

.. _`target_put_sess_cmd`:

target_put_sess_cmd
===================

.. c:function:: int target_put_sess_cmd(struct se_cmd *se_cmd)

    decrease the command reference count

    :param se_cmd:
        command to drop a reference from
    :type se_cmd: struct se_cmd \*

.. _`target_put_sess_cmd.description`:

Description
-----------

Returns 1 if and only if this \ :c:func:`target_put_sess_cmd`\  call caused the
refcount to drop to zero. Returns zero otherwise.

.. _`target_sess_cmd_list_set_waiting`:

target_sess_cmd_list_set_waiting
================================

.. c:function:: void target_sess_cmd_list_set_waiting(struct se_session *se_sess)

    Set sess_tearing_down so no new commands are queued.

    :param se_sess:
        session to flag
    :type se_sess: struct se_session \*

.. _`target_wait_for_sess_cmds`:

target_wait_for_sess_cmds
=========================

.. c:function:: void target_wait_for_sess_cmds(struct se_session *se_sess)

    Wait for outstanding commands

    :param se_sess:
        session to wait for active I/O
    :type se_sess: struct se_session \*

.. _`transport_wait_for_tasks`:

transport_wait_for_tasks
========================

.. c:function:: bool transport_wait_for_tasks(struct se_cmd *cmd)

    set CMD_T_STOP and wait for t_transport_stop_comp

    :param cmd:
        command to wait on
    :type cmd: struct se_cmd \*

.. _`translate_sense_reason`:

translate_sense_reason
======================

.. c:function:: void translate_sense_reason(struct se_cmd *cmd, sense_reason_t reason)

    translate a sense reason into T10 key, asc and ascq

    :param cmd:
        SCSI command in which the resulting sense buffer or SCSI status will
        be stored.
    :type cmd: struct se_cmd \*

    :param reason:
        LIO sense reason code. If this argument has the value
        TCM_CHECK_CONDITION_UNIT_ATTENTION, try to dequeue a unit attention. If
        dequeuing a unit attention fails due to multiple commands being processed
        concurrently, set the command status to BUSY.
    :type reason: sense_reason_t

.. _`translate_sense_reason.return`:

Return
------

0 upon success or -EINVAL if the sense buffer is too small.

.. This file was automatic generated / don't edit.

