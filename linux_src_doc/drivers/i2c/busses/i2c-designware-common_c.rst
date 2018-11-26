.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-designware-common.c

.. _`i2c_dw_set_reg_access`:

i2c_dw_set_reg_access
=====================

.. c:function:: int i2c_dw_set_reg_access(struct dw_i2c_dev *dev)

    Set register access flags

    :param dev:
        device private data
    :type dev: struct dw_i2c_dev \*

.. _`i2c_dw_set_reg_access.description`:

Description
-----------

Autodetects needed register access mode and sets access flags accordingly.
This must be called before doing any other register access.

.. This file was automatic generated / don't edit.

