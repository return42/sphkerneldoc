
.. _API-uart-handle-dcd-change:

======================
uart_handle_dcd_change
======================

*man uart_handle_dcd_change(9)*

*4.6.0-rc1*

handle a change of carrier detect state


Synopsis
========

.. c:function:: void uart_handle_dcd_change( struct uart_port * uport, unsigned int status )

Arguments
=========

``uport``
    uart_port structure for the open port

``status``
    new carrier detect status, nonzero if active


Description
===========

Caller must hold uport->lock
