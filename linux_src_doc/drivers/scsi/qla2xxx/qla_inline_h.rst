.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_inline.h

.. _`qla24xx_calc_iocbs`:

qla24xx_calc_iocbs
==================

.. c:function:: uint16_t qla24xx_calc_iocbs(scsi_qla_host_t *vha, uint16_t dsds)

    Determine number of Command Type 3 and Continuation Type 1 IOCBs to allocate.

    :param scsi_qla_host_t \*vha:
        HA context

    :param uint16_t dsds:
        number of data segment decriptors needed

.. _`qla24xx_calc_iocbs.description`:

Description
-----------

Returns the number of IOCB entries needed to store \ ``dsds``\ .

.. This file was automatic generated / don't edit.

