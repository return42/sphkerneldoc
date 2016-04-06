
.. _API-uart-handle-cts-change:

======================
uart_handle_cts_change
======================

*man uart_handle_cts_change(9)*

*4.6.0-rc1*

handle a change of clear-to-send state


Synopsis
========

.. c:function:: void uart_handle_cts_change( struct uart_port * uport, unsigned int status )

Arguments
=========

``uport``
    uart_port structure for the open port

``status``
    new clear to send status, nonzero if active


Description
===========

Caller must hold uport->lock
