.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_dev.c

.. _`asd_init_sata_pm_port_ddb`:

asd_init_sata_pm_port_ddb
=========================

.. c:function:: int asd_init_sata_pm_port_ddb(struct domain_device *dev)

    - SATA Port Multiplier Port

    :param dev:
        *undescribed*
    :type dev: struct domain_device \*

.. _`asd_init_sata_pm_port_ddb.dev`:

dev
---

pointer to domain device

For SATA Port Multiplier Ports we need to allocate one SATA Port
Multiplier Port DDB and depending on whether the target on it
supports SATA II NCQ, one SATA Tag DDB.

.. _`asd_init_sata_pm_ddb`:

asd_init_sata_pm_ddb
====================

.. c:function:: int asd_init_sata_pm_ddb(struct domain_device *dev)

    - SATA Port Multiplier

    :param dev:
        *undescribed*
    :type dev: struct domain_device \*

.. _`asd_init_sata_pm_ddb.dev`:

dev
---

pointer to domain device

For STP and direct-attached SATA Port Multipliers we need
one target port DDB entry and one SATA PM table DDB entry.

.. This file was automatic generated / don't edit.

