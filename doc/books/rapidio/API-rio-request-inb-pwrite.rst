.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-request-inb-pwrite:

======================
rio_request_inb_pwrite
======================

*man rio_request_inb_pwrite(9)*

*4.6.0-rc5*

request inbound port-write message service for specific RapidIO device


Synopsis
========

.. c:function:: int rio_request_inb_pwrite( struct rio_dev * rdev, int (*pwcback) struct rio_dev *rdev, union rio_pw_msg *msg, int step )

Arguments
=========

``rdev``
    RIO device to which register inbound port-write callback routine

``pwcback``
    Callback routine to execute when port-write is received


Description
===========

Binds a port-write callback function to the RapidIO device. Returns 0 if
the request has been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
