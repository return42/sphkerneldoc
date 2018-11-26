.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-designware-master.c

.. _`i2c_dw_init_master`:

i2c_dw_init_master
==================

.. c:function:: int i2c_dw_init_master(struct dw_i2c_dev *dev)

    Initialize the designware I2C master hardware

    :param dev:
        device private data
    :type dev: struct dw_i2c_dev \*

.. _`i2c_dw_init_master.description`:

Description
-----------

This functions configures and enables the I2C master.
This function is called during I2C init function, and in case of timeout at
run time.

.. This file was automatic generated / don't edit.

