.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_cmds.h

.. _`mpu_mailbox_db_offset`:

MPU_MAILBOX_DB_OFFSET
=====================

.. c:function::  MPU_MAILBOX_DB_OFFSET()

    The software must write this register twice to post any command. First, it writes the register with hi=1 and the upper bits of the physical address for the MAILBOX structure. Software must poll the ready bit until this is acknowledged. Then, sotware writes the register with hi=0 with the lower bits in the address. It must poll the ready bit until the command is complete. Upon completion, the MAILBOX will contain a valid completion queue entry.

.. _`async_trailer_event_code_shift`:

ASYNC_TRAILER_EVENT_CODE_SHIFT
==============================

.. c:function::  ASYNC_TRAILER_EVENT_CODE_SHIFT()

.. _`be_async_link_up_mask`:

BE_ASYNC_LINK_UP_MASK
=====================

.. c:function::  BE_ASYNC_LINK_UP_MASK()

    ASYNC_EVENT_LINK_UP                  0x1 ASYNC_EVENT_LINK_LOGICAL_DOWN        0x2 ASYNC_EVENT_LINK_LOGICAL_UP          0x3

.. _`opcode_common_cq_create`:

OPCODE_COMMON_CQ_CREATE
=======================

.. c:function::  OPCODE_COMMON_CQ_CREATE()

    These opcodes are unique for each subsystem defined above

.. _`opcode_common_iscsi_cfg_post_sgl_pages`:

OPCODE_COMMON_ISCSI_CFG_POST_SGL_PAGES
======================================

.. c:function::  OPCODE_COMMON_ISCSI_CFG_POST_SGL_PAGES()

    used by CMD_SUBSYSTEM_ISCSI These opcodes are unique for each subsystem defined above

.. _`db_wrb_post_cid_mask`:

DB_WRB_POST_CID_MASK
====================

.. c:function::  DB_WRB_POST_CID_MASK()

    stack to notify the controller of a posted Work Request Block

.. _`sol_cmd_complete`:

SOL_CMD_COMPLETE
================

.. c:function::  SOL_CMD_COMPLETE()

    and taget mode of operation.

.. This file was automatic generated / don't edit.

