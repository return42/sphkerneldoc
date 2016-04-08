
.. _API-rio-inb-pwrite-handler:

======================
rio_inb_pwrite_handler
======================

*man rio_inb_pwrite_handler(9)*

*4.6.0-rc1*

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

Processes an inbound port-write message. Returns 0 if the request has been satisfied.
