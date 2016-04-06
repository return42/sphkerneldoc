
.. _API-uart-update-timeout:

===================
uart_update_timeout
===================

*man uart_update_timeout(9)*

*4.6.0-rc1*

update per-port FIFO timeout.


Synopsis
========

.. c:function:: void uart_update_timeout( struct uart_port * port, unsigned int cflag, unsigned int baud )

Arguments
=========

``port``
    uart_port structure describing the port

``cflag``
    termios cflag value

``baud``
    speed of the port


Description
===========

Set the port FIFO timeout value. The ``cflag`` value should reflect the actual hardware settings.
