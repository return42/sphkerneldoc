.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/queue.h

.. _`mmc_drv_op`:

enum mmc_drv_op
===============

.. c:type:: enum mmc_drv_op

    enumerates the operations in the mmc_queue_req

.. _`mmc_drv_op.definition`:

Definition
----------

.. code-block:: c

    enum mmc_drv_op {
        MMC_DRV_OP_IOCTL,
        MMC_DRV_OP_IOCTL_RPMB,
        MMC_DRV_OP_BOOT_WP,
        MMC_DRV_OP_GET_CARD_STATUS,
        MMC_DRV_OP_GET_EXT_CSD
    };

.. _`mmc_drv_op.constants`:

Constants
---------

MMC_DRV_OP_IOCTL
    ioctl operation

MMC_DRV_OP_IOCTL_RPMB
    RPMB-oriented ioctl operation

MMC_DRV_OP_BOOT_WP
    write protect boot partitions

MMC_DRV_OP_GET_CARD_STATUS
    get card status

MMC_DRV_OP_GET_EXT_CSD
    get the EXT CSD from an eMMC card

.. This file was automatic generated / don't edit.

