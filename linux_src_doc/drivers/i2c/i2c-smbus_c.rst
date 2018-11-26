.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/i2c-smbus.c

.. _`i2c_handle_smbus_alert`:

i2c_handle_smbus_alert
======================

.. c:function:: int i2c_handle_smbus_alert(struct i2c_client *ara)

    Handle an SMBus alert

    :param ara:
        the ARA client on the relevant adapter
    :type ara: struct i2c_client \*

.. _`i2c_handle_smbus_alert.context`:

Context
-------

can't sleep

.. _`i2c_handle_smbus_alert.description`:

Description
-----------

Helper function to be called from an I2C bus driver's interrupt
handler. It will schedule the alert work, in turn calling the
corresponding I2C device driver's alert function.

It is assumed that ara is a valid i2c client previously returned by
\ :c:func:`i2c_setup_smbus_alert`\ .

.. This file was automatic generated / don't edit.

