.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_transport.c

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
        *undescribed*

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

.. _`transport_put_cmd`:

transport_put_cmd
=================

.. c:function:: int transport_put_cmd(struct se_cmd *cmd)

    release a reference to a command

    :param struct se_cmd \*cmd:
        command to release

.. _`transport_put_cmd.description`:

Description
-----------

This routine releases our reference to the command and frees it if possible.

.. _`transport_wait_for_tasks`:

transport_wait_for_tasks
========================

.. c:function:: bool transport_wait_for_tasks(struct se_cmd *cmd)

    wait for completion to occur

    :param struct se_cmd \*cmd:
        command to wait

.. _`transport_wait_for_tasks.description`:

Description
-----------

Called from frontend fabric context to wait for storage engine
to pause and/or release frontend generated struct se_cmd.

.. This file was automatic generated / don't edit.

