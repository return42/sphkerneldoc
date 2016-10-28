.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2fc/bnx2fc_tgt.c

.. _`bnx2fc_rport_event_handler`:

bnx2fc_rport_event_handler
==========================

.. c:function:: void bnx2fc_rport_event_handler(struct fc_lport *lport, struct fc_rport_priv *rdata, enum fc_rport_event event)

    initiated target login. bnx2fc can proceed with initiating the session establishment.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_rport_priv \*rdata:
        *undescribed*

    :param enum fc_rport_event event:
        *undescribed*

.. _`bnx2fc_tgt_lookup`:

bnx2fc_tgt_lookup
=================

.. c:function:: struct bnx2fc_rport *bnx2fc_tgt_lookup(struct fcoe_port *port, u32 port_id)

    Lookup a bnx2fc_rport by port_id

    :param struct fcoe_port \*port:
        fcoe_port struct to lookup the target port on

    :param u32 port_id:
        The remote port ID to look up

.. _`bnx2fc_alloc_conn_id`:

bnx2fc_alloc_conn_id
====================

.. c:function:: u32 bnx2fc_alloc_conn_id(struct bnx2fc_hba *hba, struct bnx2fc_rport *tgt)

    allocates FCOE Connection id

    :param struct bnx2fc_hba \*hba:
        pointer to adapter structure

    :param struct bnx2fc_rport \*tgt:
        pointer to bnx2fc_rport structure

.. _`bnx2fc_alloc_session_resc`:

bnx2fc_alloc_session_resc
=========================

.. c:function:: int bnx2fc_alloc_session_resc(struct bnx2fc_hba *hba, struct bnx2fc_rport *tgt)

    Allocate qp resources for the session

    :param struct bnx2fc_hba \*hba:
        *undescribed*

    :param struct bnx2fc_rport \*tgt:
        *undescribed*

.. _`bnx2fc_free_session_resc`:

bnx2fc_free_session_resc
========================

.. c:function:: void bnx2fc_free_session_resc(struct bnx2fc_hba *hba, struct bnx2fc_rport *tgt)

    free qp resources for the session

    :param struct bnx2fc_hba \*hba:
        adapter structure pointer

    :param struct bnx2fc_rport \*tgt:
        bnx2fc_rport structure pointer

.. _`bnx2fc_free_session_resc.description`:

Description
-----------

Free QP resources - SQ/RQ/CQ/XFERQ memory and PBL

.. This file was automatic generated / don't edit.

