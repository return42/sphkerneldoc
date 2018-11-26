.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_target.c

.. _`qlt_lport_register`:

qlt_lport_register
==================

.. c:function:: int qlt_lport_register(void *target_lport_ptr, u64 phys_wwpn, u64 npiv_wwpn, u64 npiv_wwnn, int (*callback)(struct scsi_qla_host *, void *, u64, u64))

    register lport with external module

    :param target_lport_ptr:
        pointer for tcm_qla2xxx specific lport data
    :type target_lport_ptr: void \*

    :param phys_wwpn:
        physical port WWPN
    :type phys_wwpn: u64

    :param npiv_wwpn:
        NPIV WWPN
    :type npiv_wwpn: u64

    :param npiv_wwnn:
        NPIV WWNN
    :type npiv_wwnn: u64

    :param int (\*callback)(struct scsi_qla_host \*, void \*, u64, u64):
        lport initialization callback for tcm_qla2xxx code

.. _`qlt_lport_deregister`:

qlt_lport_deregister
====================

.. c:function:: void qlt_lport_deregister(struct scsi_qla_host *vha)

    Degister lport

    :param vha:
        Registered scsi_qla_host pointer
    :type vha: struct scsi_qla_host \*

.. This file was automatic generated / don't edit.

