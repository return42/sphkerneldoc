.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pxa2xx_ssp.h

.. _`pxa_ssp_write_reg`:

pxa_ssp_write_reg
=================

.. c:function:: void pxa_ssp_write_reg(struct ssp_device *dev, u32 reg, u32 val)

    Write to a SSP register

    :param dev:
        SSP device to access
    :type dev: struct ssp_device \*

    :param reg:
        Register to write to
    :type reg: u32

    :param val:
        Value to be written.
    :type val: u32

.. _`pxa_ssp_read_reg`:

pxa_ssp_read_reg
================

.. c:function:: u32 pxa_ssp_read_reg(struct ssp_device *dev, u32 reg)

    Read from a SSP register

    :param dev:
        SSP device to access
    :type dev: struct ssp_device \*

    :param reg:
        Register to read from
    :type reg: u32

.. This file was automatic generated / don't edit.

