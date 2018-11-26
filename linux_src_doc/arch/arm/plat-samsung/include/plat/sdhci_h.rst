.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/sdhci.h

.. _`s3c_sdhci0_set_platdata`:

s3c_sdhci0_set_platdata
=======================

.. c:function:: void s3c_sdhci0_set_platdata(struct s3c_sdhci_platdata *pd)

    Set platform data for S3C SDHCI device.

    :param pd:
        Platform data to register to device.
    :type pd: struct s3c_sdhci_platdata \*

.. _`s3c_sdhci0_set_platdata.description`:

Description
-----------

Register the given platform data for use withe S3C SDHCI device.
The call will copy the platform data, so the board definitions can
make the structure itself \__initdata.

.. This file was automatic generated / don't edit.

