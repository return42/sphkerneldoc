.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qedf/qedf_main.c

.. _`qedf_xmit`:

qedf_xmit
=========

.. c:function:: int qedf_xmit(struct fc_lport *lport, struct fc_frame *fp)

    qedf FCoE frame transmit function

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`qedf_rport_event_handler`:

qedf_rport_event_handler
========================

.. c:function:: void qedf_rport_event_handler(struct fc_lport *lport, struct fc_rport_priv *rdata, enum fc_rport_event event)

    initiated target login. qedf can proceed with initiating the session establishment.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_rport_priv \*rdata:
        *undescribed*

    :param enum fc_rport_event event:
        *undescribed*

.. _`qedf_fcoe_reset`:

qedf_fcoe_reset
===============

.. c:function:: int qedf_fcoe_reset(struct Scsi_Host *shost)

    Resets the fcoe

    :param struct Scsi_Host \*shost:
        shost the reset is from

.. _`qedf_fcoe_reset.return`:

Return
------

always 0

.. This file was automatic generated / don't edit.

