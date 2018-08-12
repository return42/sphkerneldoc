.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_transport.c

.. _`target_submit_cmd_map_sgls`:

target_submit_cmd_map_sgls
==========================

.. c:function:: int target_submit_cmd_map_sgls(struct se_cmd *se_cmd, struct se_session *se_sess, unsigned char *cdb, unsigned char *sense, u64 unpacked_lun, u32 data_length, int task_attr, int data_dir, int flags, struct scatterlist *sgl, u32 sgl_count, struct scatterlist *sgl_bidi, u32 sgl_bidi_count, struct scatterlist *sgl_prot, u32 sgl_prot_count)

    lookup unpacked lun and submit uninitialized se_cmd + use pre-allocated SGL memory.

    :param struct se_cmd \*se_cmd:
        command descriptor to submit

    :param struct se_session \*se_sess:
        associated se_sess for endpoint

    :param unsigned char \*cdb:
        pointer to SCSI CDB

    :param unsigned char \*sense:
        pointer to SCSI sense buffer

    :param u64 unpacked_lun:
        unpacked LUN to reference for struct se_lun

    :param u32 data_length:
        fabric expected data transfer length

    :param int task_attr:
        SAM task attribute

    :param int data_dir:
        DMA data direction

    :param int flags:
        flags for command submission from target_sc_flags_tables

    :param struct scatterlist \*sgl:
        struct scatterlist memory for unidirectional mapping

    :param u32 sgl_count:
        scatterlist count for unidirectional mapping

    :param struct scatterlist \*sgl_bidi:
        struct scatterlist memory for bidirectional READ mapping

    :param u32 sgl_bidi_count:
        scatterlist count for bidirectional READ mapping

    :param struct scatterlist \*sgl_prot:
        struct scatterlist memory protection information

    :param u32 sgl_prot_count:
        scatterlist count for protection information

.. _`target_submit_cmd_map_sgls.description`:

Description
-----------

Task tags are supported if the caller has set \ ``se_cmd``\ ->tag.

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

    :param struct se_cmd \*se_cmd:
        command descriptor to submit

    :param struct se_session \*se_sess:
        associated se_sess for endpoint

    :param unsigned char \*cdb:
        pointer to SCSI CDB

    :param unsigned char \*sense:
        pointer to SCSI sense buffer

    :param u64 unpacked_lun:
        unpacked LUN to reference for struct se_lun

    :param u32 data_length:
        fabric expected data transfer length

    :param int task_attr:
        SAM task attribute

    :param int data_dir:
        DMA data direction

    :param int flags:
        flags for command submission from target_sc_flags_tables

.. _`target_submit_cmd.description`:

Description
-----------

Task tags are supported if the caller has set \ ``se_cmd``\ ->tag.

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

    :param struct se_cmd \*se_cmd:
        command descriptor to submit

    :param struct se_session \*se_sess:
        associated se_sess for endpoint

    :param unsigned char \*sense:
        pointer to SCSI sense buffer

    :param u64 unpacked_lun:
        unpacked LUN to reference for struct se_lun

    :param void \*fabric_tmr_ptr:
        fabric context for TMR req

    :param unsigned char tm_type:
        Type of TM request

    :param gfp_t gfp:
        gfp type for caller

    :param u64 tag:
        referenced task tag for TMR_ABORT_TASK

    :param int flags:
        submit cmd flags

.. _`target_submit_tmr.description`:

Description
-----------

Callable from all contexts.

.. _`target_get_sess_cmd`:

target_get_sess_cmd
===================

.. c:function:: int target_get_sess_cmd(struct se_cmd *se_cmd, bool ack_kref)

    Add command to active ->sess_cmd_list

    :param struct se_cmd \*se_cmd:
        command descriptor to add

    :param bool ack_kref:
        Signal that fabric will perform an ack \ :c:func:`target_put_sess_cmd`\ 

.. _`target_put_sess_cmd`:

target_put_sess_cmd
===================

.. c:function:: int target_put_sess_cmd(struct se_cmd *se_cmd)

    decrease the command reference count

    :param struct se_cmd \*se_cmd:
        command to drop a reference from

.. _`target_put_sess_cmd.description`:

Description
-----------

Returns 1 if and only if this \ :c:func:`target_put_sess_cmd`\  call caused the
refcount to drop to zero. Returns zero otherwise.

.. _`target_sess_cmd_list_set_waiting`:

target_sess_cmd_list_set_waiting
================================

.. c:function:: void target_sess_cmd_list_set_waiting(struct se_session *se_sess)

    Flag all commands in sess_cmd_list to complete cmd_wait_comp.  Set sess_tearing_down so no more commands are queued.

    :param struct se_session \*se_sess:
        session to flag

.. _`target_wait_for_sess_cmds`:

target_wait_for_sess_cmds
=========================

.. c:function:: void target_wait_for_sess_cmds(struct se_session *se_sess)

    Wait for outstanding descriptors

    :param struct se_session \*se_sess:
        session to wait for active I/O

.. _`transport_wait_for_tasks`:

transport_wait_for_tasks
========================

.. c:function:: bool transport_wait_for_tasks(struct se_cmd *cmd)

    set CMD_T_STOP and wait for t_transport_stop_comp

    :param struct se_cmd \*cmd:
        command to wait on

.. This file was automatic generated / don't edit.

