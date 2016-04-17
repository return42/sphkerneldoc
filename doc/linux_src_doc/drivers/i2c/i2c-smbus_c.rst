.. -*- coding: utf-8; mode: rst -*-

===========
i2c-smbus.c
===========


.. _`i2c_setup_smbus_alert`:

i2c_setup_smbus_alert
=====================

.. c:function:: struct i2c_client *i2c_setup_smbus_alert (struct i2c_adapter *adapter, struct i2c_smbus_alert_setup *setup)

    Setup SMBus alert support

    :param struct i2c_adapter \*adapter:
        the target adapter

    :param struct i2c_smbus_alert_setup \*setup:
        setup data for the SMBus alert handler



.. _`i2c_setup_smbus_alert.context`:

Context
-------

can sleep



.. _`i2c_setup_smbus_alert.description`:

Description
-----------

Setup handling of the SMBus alert protocol on a given I2C bus segment.

Handling can be done either through our IRQ handler, or by the
adapter (from its handler, periodic polling, or whatever).

NOTE that if we manage the IRQ, we \*MUST\* know if it's level or
edge triggered in order to hand it to the workqueue correctly.
If triggering the alert seems to wedge the system, you probably
should have said it's level triggered.

This returns the ara client, which should be saved for later use with
:c:func:`i2c_handle_smbus_alert` and ultimately :c:func:`i2c_unregister_device`; or NULL
to indicate an error.



.. _`i2c_handle_smbus_alert`:

i2c_handle_smbus_alert
======================

.. c:function:: int i2c_handle_smbus_alert (struct i2c_client *ara)

    Handle an SMBus alert

    :param struct i2c_client \*ara:
        the ARA client on the relevant adapter



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
:c:func:`i2c_setup_smbus_alert`.

