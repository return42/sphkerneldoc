.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libsas/sas_init.c

.. _`transport_sas_phy_reset`:

transport_sas_phy_reset
=======================

.. c:function:: int transport_sas_phy_reset(struct sas_phy *phy, int hard_reset)

    reset a phy and permit libata to manage the link

    :param struct sas_phy \*phy:
        *undescribed*

    :param int hard_reset:
        *undescribed*

.. _`transport_sas_phy_reset.description`:

Description
-----------

phy reset request via sysfs in host workqueue context so we know we
can block on eh and safely traverse the domain_device topology

.. This file was automatic generated / don't edit.

