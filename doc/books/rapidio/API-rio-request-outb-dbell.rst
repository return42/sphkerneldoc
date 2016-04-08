
.. _API-rio-request-outb-dbell:

======================
rio_request_outb_dbell
======================

*man rio_request_outb_dbell(9)*

*4.6.0-rc1*

request outbound doorbell message range


Synopsis
========

.. c:function:: struct resource ⋆ rio_request_outb_dbell( struct rio_dev * rdev, u16 start, u16 end )

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

Requests ownership of a doorbell message range. Returns a resource if the request has been satisfied or ``NULL`` on failure.
