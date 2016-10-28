.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-s3c24xx/setup-ts.c

.. _`s3c24xx_ts_cfg_gpio`:

s3c24xx_ts_cfg_gpio
===================

.. c:function:: void s3c24xx_ts_cfg_gpio(struct platform_device *dev)

    configure gpio for s3c2410 systems

    :param struct platform_device \*dev:
        *undescribed*

.. _`s3c24xx_ts_cfg_gpio.description`:

Description
-----------

Configure the GPIO for the S3C2410 system, where we have external FETs
connected to the device (later systems such as the S3C2440 integrate
these into the device).

.. This file was automatic generated / don't edit.

