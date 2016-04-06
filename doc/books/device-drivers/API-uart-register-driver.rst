
.. _API-uart-register-driver:

====================
uart_register_driver
====================

*man uart_register_driver(9)*

*4.6.0-rc1*

register a driver with the uart core layer


Synopsis
========

.. c:function:: int uart_register_driver( struct uart_driver * drv )

Arguments
=========

``drv``
    low level driver structure


Description
===========

Register a uart driver with the core driver. We in turn register with the tty layer, and initialise the core driver per-port state.

We have a proc file in /proc/tty/driver which is named after the normal driver.

drv->port should be NULL, and the per-port structures should be registered using uart_add_one_port after this call has succeeded.
