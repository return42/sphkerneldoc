.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pxa2xx_ssp.h

.. _`pxa_ssp_write_reg`:

pxa_ssp_write_reg
=================

.. c:function:: void pxa_ssp_write_reg(struct ssp_device *dev, u32 reg, u32 val)

    Write to a SSP register

    :param struct ssp_device \*dev:
        SSP device to access

    :param u32 reg:
        Register to write to

    :param u32 val:
        Value to be written.

.. _`pxa_ssp_read_reg`:

pxa_ssp_read_reg
================

.. c:function:: u32 pxa_ssp_read_reg(struct ssp_device *dev, u32 reg)

    Read from a SSP register

    :param struct ssp_device \*dev:
        SSP device to access

    :param u32 reg:
        Register to read from

.. This file was automatic generated / don't edit.

