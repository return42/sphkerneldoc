.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_target.c

.. _`qlt_lport_register`:

qlt_lport_register
==================

.. c:function:: int qlt_lport_register(void *target_lport_ptr, u64 phys_wwpn, u64 npiv_wwpn, u64 npiv_wwnn, int (*callback)(struct scsi_qla_host *, void *, u64, u64))

    register lport with external module

    :param void \*target_lport_ptr:
        pointer for tcm_qla2xxx specific lport data

    :param u64 phys_wwpn:
        *undescribed*

    :param u64 npiv_wwpn:
        *undescribed*

    :param u64 npiv_wwnn:
        *undescribed*

    :param int (\*callback)(struct scsi_qla_host \*, void \*, u64, u64):
        lport initialization callback for tcm_qla2xxx code

.. _`qlt_lport_deregister`:

qlt_lport_deregister
====================

.. c:function:: void qlt_lport_deregister(struct scsi_qla_host *vha)

    Degister lport

    :param struct scsi_qla_host \*vha:
        Registered scsi_qla_host pointer

.. This file was automatic generated / don't edit.

