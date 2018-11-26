.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/atp870u.c

.. _`atp870u_queuecommand_lck`:

atp870u_queuecommand_lck
========================

.. c:function:: int atp870u_queuecommand_lck(struct scsi_cmnd *req_p, void (*done)(struct scsi_cmnd *))

    Queue SCSI command

    :param req_p:
        request block
    :type req_p: struct scsi_cmnd \*

    :param void (\*done)(struct scsi_cmnd \*):
        completion function

.. _`atp870u_queuecommand_lck.description`:

Description
-----------

Queue a command to the ATP queue. Called with the host lock held.

.. _`send_s870`:

send_s870
=========

.. c:function:: void send_s870(struct atp_unit *dev, unsigned char c)

    send a command to the controller

    :param dev:
        *undescribed*
    :type dev: struct atp_unit \*

    :param c:
        *undescribed*
    :type c: unsigned char

.. _`send_s870.description`:

Description
-----------

On entry there is work queued to be done. We move some of that work to the
controller itself.

Caller holds the host lock.

.. This file was automatic generated / don't edit.

