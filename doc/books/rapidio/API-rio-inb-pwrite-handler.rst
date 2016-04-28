.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-inb-pwrite-handler:

======================
rio_inb_pwrite_handler
======================

*man rio_inb_pwrite_handler(9)*

*4.6.0-rc5*

inbound port-write message handler


Synopsis
========

.. c:function:: int rio_inb_pwrite_handler( struct rio_mport * mport, union rio_pw_msg * pw_msg )

Arguments
=========

``mport``
    mport device associated with port-write

``pw_msg``
    pointer to inbound port-write message


Description
===========

Processes an inbound port-write message. Returns 0 if the request has
been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
