.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-handle-dcd-change:

======================
uart_handle_dcd_change
======================

*man uart_handle_dcd_change(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
