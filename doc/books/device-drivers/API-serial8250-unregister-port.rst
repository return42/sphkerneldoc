
.. _API-serial8250-unregister-port:

==========================
serial8250_unregister_port
==========================

*man serial8250_unregister_port(9)*

*4.6.0-rc1*

remove a 16x50 serial port at runtime


Synopsis
========

.. c:function:: void serial8250_unregister_port( int line )

Arguments
=========

``line``
    serial line number


Description
===========

Remove one serial port. This may not be called from interrupt context. We hand the port back to the our control.
