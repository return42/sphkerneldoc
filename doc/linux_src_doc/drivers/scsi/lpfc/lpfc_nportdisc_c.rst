.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_nportdisc.c

.. _`lpfc_mbx_cmpl_resume_rpi`:

lpfc_mbx_cmpl_resume_rpi
========================

.. c:function:: void lpfc_mbx_cmpl_resume_rpi(struct lpfc_hba *phba, LPFC_MBOXQ_t *mboxq)

    Resume RPI completion routine

    :param struct lpfc_hba \*phba:
        pointer to lpfc hba data structure.

    :param LPFC_MBOXQ_t \*mboxq:
        pointer to mailbox object

.. _`lpfc_mbx_cmpl_resume_rpi.description`:

Description
-----------

This routine is invoked to issue a completion to a rcv'ed
ADISC or PDISC after the paused RPI has been resumed.

.. _`lpfc_release_rpi`:

lpfc_release_rpi
================

.. c:function:: void lpfc_release_rpi(struct lpfc_hba *phba, struct lpfc_vport *vport, uint16_t rpi)

    Release a RPI by issuing unreg_login mailbox cmd.

    :param struct lpfc_hba \*phba:
        Pointer to lpfc_hba structure.

    :param struct lpfc_vport \*vport:
        Pointer to lpfc_vport structure.

    :param uint16_t rpi:
        rpi to be release.

.. _`lpfc_release_rpi.description`:

Description
-----------

This function will send a unreg_login mailbox command to the firmware
to release a rpi.

.. This file was automatic generated / don't edit.

