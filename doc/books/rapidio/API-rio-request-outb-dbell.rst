.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-request-outb-dbell:

======================
rio_request_outb_dbell
======================

*man rio_request_outb_dbell(9)*

*4.6.0-rc5*

request outbound doorbell message range


Synopsis
========

.. c:function:: struct resource * rio_request_outb_dbell( struct rio_dev * rdev, u16 start, u16 end )

Arguments
=========

``rdev``
    RIO device from which to allocate the doorbell resource

``start``
    Doorbell message range start

``end``
    Doorbell message range end


Description
===========

Requests ownership of a doorbell message range. Returns a resource if
the request has been satisfied or ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
