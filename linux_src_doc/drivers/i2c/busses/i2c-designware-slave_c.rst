.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-designware-slave.c

.. _`i2c_dw_init_slave`:

i2c_dw_init_slave
=================

.. c:function:: int i2c_dw_init_slave(struct dw_i2c_dev *dev)

    Initialize the designware i2c slave hardware

    :param struct dw_i2c_dev \*dev:
        device private data

.. _`i2c_dw_init_slave.description`:

Description
-----------

This function configures and enables the I2C in slave mode.
This function is called during I2C init function, and in case of timeout at
run time.

.. This file was automatic generated / don't edit.

