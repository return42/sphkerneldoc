
.. _API-rio-request-inb-dbell:

=====================
rio_request_inb_dbell
=====================

*man rio_request_inb_dbell(9)*

*4.6.0-rc1*

request inbound doorbell message service


Synopsis
========

.. c:function:: int rio_request_inb_dbell( struct rio_mport * mport, void * dev_id, u16 start, u16 end, void (*dinb) struct rio_mport * mport, void *dev_id, u16 src, u16 dst, u16 info )

Arguments
=========

``mport``
    RIO master port from which to allocate the doorbell resource

``dev_id``
    Device specific pointer to pass on event

``start``
    Doorbell info range start

``end``
    Doorbell info range end

``dinb``
    Callback to execute when doorbell is received


Description
===========

Requests ownership of an inbound doorbell resource and binds a callback function to the resource. Returns 0 if the request has been satisfied.
