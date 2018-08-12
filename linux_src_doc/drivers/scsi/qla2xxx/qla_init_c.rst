.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_init.c

.. _`qla2100_pci_config`:

qla2100_pci_config
==================

.. c:function:: int qla2100_pci_config(scsi_qla_host_t *vha)

    Setup ISP21xx PCI configuration registers.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2100_pci_config.description`:

Description
-----------

Returns 0 on success.

.. _`qla2300_pci_config`:

qla2300_pci_config
==================

.. c:function:: int qla2300_pci_config(scsi_qla_host_t *vha)

    Setup ISP23xx PCI configuration registers.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2300_pci_config.description`:

Description
-----------

Returns 0 on success.

.. _`qla24xx_pci_config`:

qla24xx_pci_config
==================

.. c:function:: int qla24xx_pci_config(scsi_qla_host_t *vha)

    Setup ISP24xx PCI configuration registers.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla24xx_pci_config.description`:

Description
-----------

Returns 0 on success.

.. _`qla25xx_pci_config`:

qla25xx_pci_config
==================

.. c:function:: int qla25xx_pci_config(scsi_qla_host_t *vha)

    Setup ISP25xx PCI configuration registers.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla25xx_pci_config.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_isp_firmware`:

qla2x00_isp_firmware
====================

.. c:function:: int qla2x00_isp_firmware(scsi_qla_host_t *vha)

    Choose firmware image.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_isp_firmware.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_reset_chip`:

qla2x00_reset_chip
==================

.. c:function:: void qla2x00_reset_chip(scsi_qla_host_t *vha)

    Reset ISP chip.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_reset_chip.description`:

Description
-----------

Returns 0 on success.

.. _`qla81xx_reset_mpi`:

qla81xx_reset_mpi
=================

.. c:function:: int qla81xx_reset_mpi(scsi_qla_host_t *vha)

    Reset's MPI FW via Write MPI Register MBC.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla81xx_reset_mpi.description`:

Description
-----------

Returns 0 on success.

.. _`qla24xx_reset_risc`:

qla24xx_reset_risc
==================

.. c:function:: int qla24xx_reset_risc(scsi_qla_host_t *vha)

    Perform full reset of ISP24xx RISC.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla24xx_reset_risc.description`:

Description
-----------

Returns 0 on success.

.. _`qla24xx_reset_chip`:

qla24xx_reset_chip
==================

.. c:function:: void qla24xx_reset_chip(scsi_qla_host_t *vha)

    Reset ISP24xx chip.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla24xx_reset_chip.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_chip_diag`:

qla2x00_chip_diag
=================

.. c:function:: int qla2x00_chip_diag(scsi_qla_host_t *vha)

    Test chip for proper operation.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_chip_diag.description`:

Description
-----------

Returns 0 on success.

.. _`qla24xx_chip_diag`:

qla24xx_chip_diag
=================

.. c:function:: int qla24xx_chip_diag(scsi_qla_host_t *vha)

    Test ISP24xx for proper operation.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla24xx_chip_diag.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_setup_chip`:

qla2x00_setup_chip
==================

.. c:function:: int qla2x00_setup_chip(scsi_qla_host_t *vha)

    Load and start RISC firmware.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_setup_chip.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_init_response_q_entries`:

qla2x00_init_response_q_entries
===============================

.. c:function:: void qla2x00_init_response_q_entries(struct rsp_que *rsp)

    Initializes response queue entries.

    :param struct rsp_que \*rsp:
        response queue

.. _`qla2x00_init_response_q_entries.description`:

Description
-----------

Beginning of request ring has initialization control block already built
by nvram config routine.

Returns 0 on success.

.. _`qla2x00_update_fw_options`:

qla2x00_update_fw_options
=========================

.. c:function:: void qla2x00_update_fw_options(scsi_qla_host_t *vha)

    Read and process firmware options.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_update_fw_options.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_init_rings`:

qla2x00_init_rings
==================

.. c:function:: int qla2x00_init_rings(scsi_qla_host_t *vha)

    Initializes firmware.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_init_rings.description`:

Description
-----------

Beginning of request ring has initialization control block already built
by nvram config routine.

Returns 0 on success.

.. _`qla2x00_fw_ready`:

qla2x00_fw_ready
================

.. c:function:: int qla2x00_fw_ready(scsi_qla_host_t *vha)

    Waits for firmware ready.

    :param scsi_qla_host_t \*vha:
        HA context

.. _`qla2x00_fw_ready.description`:

Description
-----------

Returns 0 on success.

.. _`qla2x00_alloc_fcport`:

qla2x00_alloc_fcport
====================

.. c:function:: fc_port_t *qla2x00_alloc_fcport(scsi_qla_host_t *vha, gfp_t flags)

    Allocate a generic fcport.

    :param scsi_qla_host_t \*vha:
        HA context

    :param gfp_t flags:
        allocation flags

.. _`qla2x00_alloc_fcport.description`:

Description
-----------

Returns a pointer to the allocated fcport, or NULL, if none available.

.. This file was automatic generated / don't edit.

