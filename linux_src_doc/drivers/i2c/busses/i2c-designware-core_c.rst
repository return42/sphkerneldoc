.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-designware-core.c

.. _`i2c_dw_init`:

i2c_dw_init
===========

.. c:function:: int i2c_dw_init(struct dw_i2c_dev *dev)

    initialize the designware i2c master hardware

    :param struct dw_i2c_dev \*dev:
        device private data

.. _`i2c_dw_init.description`:

Description
-----------

This functions configures and enables the I2C master.
This function is called during I2C init function, and in case of timeout at
run time.

.. This file was automatic generated / don't edit.

