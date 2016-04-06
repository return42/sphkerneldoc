
.. _API-uart-get-baud-rate:

==================
uart_get_baud_rate
==================

*man uart_get_baud_rate(9)*

*4.6.0-rc1*

return baud rate for a particular port


Synopsis
========

.. c:function:: unsigned int uart_get_baud_rate( struct uart_port * port, struct ktermios * termios, struct ktermios * old, unsigned int min, unsigned int max )

Arguments
=========

``port``
    uart_port structure describing the port in question.

``termios``
    desired termios settings.

``old``
    old termios (or NULL)

``min``
    minimum acceptable baud rate

``max``
    maximum acceptable baud rate


Description
===========

Decode the termios structure into a numeric baud rate, taking account of the magic 38400 baud rate (with spd_⋆ flags), and mapping the ``B0`` rate to 9600 baud.

If the new baud rate is invalid, try the old termios setting. If it's still invalid, we try 9600 baud.

Update the ``termios`` structure to reflect the baud rate we're actually going to be using. Don't do this for the case where B0 is requested (“hang up”).
