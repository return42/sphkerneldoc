
.. _API-serial8250-get-port:

===================
serial8250_get_port
===================

*man serial8250_get_port(9)*

*4.6.0-rc1*

retrieve struct uart_8250_port


Synopsis
========

.. c:function:: struct uart_8250_port ⋆ serial8250_get_port( int line )

Arguments
=========

``line``
    serial line number


Description
===========

This function retrieves struct uart_8250_port for the specific line. This struct ⋆must⋆ ⋆not⋆ be used to perform a 8250 or serial core operation which is not accessible
otherwise. Its only purpose is to make the struct accessible to the runtime-pm callbacks for context suspend/restore. The lock assumption made here is none because runtime-pm
suspend/resume callbacks should not be invoked if there is any operation performed on the port.
