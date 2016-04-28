.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-do-upload:

=============
mpt_do_upload
=============

*man mpt_do_upload(9)*

*4.6.0-rc5*

Construct and Send FWUpload request to MPT adapter port.


Synopsis
========

.. c:function:: int mpt_do_upload( MPT_ADAPTER * ioc, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

Returns 0 for success, >0 for handshake failure <0 for fw upload
failure.


Remark
======

If bound IOC and a successful FWUpload was performed on the bound IOC,
the second image is discarded and memory is free'd. Both channels must
upload to prevent IOC from running in degraded mode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
