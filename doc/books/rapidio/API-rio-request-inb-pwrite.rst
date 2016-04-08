
.. _API-rio-request-inb-pwrite:

======================
rio_request_inb_pwrite
======================

*man rio_request_inb_pwrite(9)*

*4.6.0-rc1*

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

Binds a port-write callback function to the RapidIO device. Returns 0 if the request has been satisfied.
