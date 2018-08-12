.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_nx.c

.. _`qla82xx_pci_config`:

qla82xx_pci_config
==================

.. c:function:: int qla82xx_pci_config(scsi_qla_host_t *vha)

    Setup ISP82xx PCI configuration registers.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla82xx_pci_config.description`:

Description
-----------

Returns 0 on success.

.. _`qla82xx_reset_chip`:

qla82xx_reset_chip
==================

.. c:function:: void qla82xx_reset_chip(scsi_qla_host_t *vha)

    Setup ISP82xx PCI configuration registers.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla82xx_reset_chip.description`:

Description
-----------

Returns 0 on success.

.. _`qla82xx_intr_handler`:

qla82xx_intr_handler
====================

.. c:function:: irqreturn_t qla82xx_intr_handler(int irq, void *dev_id)

    Process interrupts for the ISP23xx and ISP63xx.

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        SCSI driver HA context

.. _`qla82xx_intr_handler.description`:

Description
-----------

Called by system whenever the host adapter generates an interrupt.

Returns handled flag.

.. This file was automatic generated / don't edit.

