.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/be2iscsi/be_main.h

.. _`be_adapter_link_up`:

BE_ADAPTER_LINK_UP
==================

.. c:function::  BE_ADAPTER_LINK_UP()

.. _`hwi_get_async_pdu_ctx`:

HWI_GET_ASYNC_PDU_CTX
=====================

.. c:function::  HWI_GET_ASYNC_PDU_CTX( phwi,  ulp_num)

    So have atleast 8 of them by default

    :param  phwi:
        *undescribed*

    :param  ulp_num:
        *undescribed*

.. _`membar_ctrl_int_ctrl_hostintr_mask`:

MEMBAR_CTRL_INT_CTRL_HOSTINTR_MASK
==================================

.. c:function::  MEMBAR_CTRL_INT_CTRL_HOSTINTR_MASK()

    Disable" may still globally block interrupts in addition to individual interrupt masks; a mechanism for the device driver to block all interrupts atomically without having to arbitrate for the PCI Interrupt Disable bit with the OS.

.. _`db_txulp0_offset`:

DB_TXULP0_OFFSET
================

.. c:function::  DB_TXULP0_OFFSET()

    in BladeEngine.

.. _`beiscsi_conn`:

struct beiscsi_conn
===================

.. c:type:: struct beiscsi_conn

    iscsi connection structure

.. _`beiscsi_conn.definition`:

Definition
----------

.. code-block:: c

    struct beiscsi_conn {
        struct iscsi_conn *conn;
        struct beiscsi_hba *phba;
        u32 exp_statsn;
        u32 doorbell_offset;
        u32 beiscsi_conn_cid;
        struct beiscsi_endpoint *ep;
        unsigned short login_in_progress;
        struct wrb_handle *plogin_wrb_handle;
        struct sgl_handle *plogin_sgl_handle;
        struct beiscsi_session *beiscsi_sess;
        struct iscsi_task *task;
    }

.. _`beiscsi_conn.members`:

Members
-------

conn
    *undescribed*

phba
    *undescribed*

exp_statsn
    *undescribed*

doorbell_offset
    *undescribed*

beiscsi_conn_cid
    *undescribed*

ep
    *undescribed*

login_in_progress
    *undescribed*

plogin_wrb_handle
    *undescribed*

plogin_sgl_handle
    *undescribed*

beiscsi_sess
    *undescribed*

task
    *undescribed*

.. _`be_tgt_ctx_updt_cmd`:

BE_TGT_CTX_UPDT_CMD
===================

.. c:function::  BE_TGT_CTX_UPDT_CMD()

.. _`be_tgt_ctx_updt_cmd.as-a-byte`:

as a byte
---------

used to calculate offset/shift/mask of each field

.. This file was automatic generated / don't edit.

