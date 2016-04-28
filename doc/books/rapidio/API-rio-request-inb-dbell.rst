.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-request-inb-dbell:

=====================
rio_request_inb_dbell
=====================

*man rio_request_inb_dbell(9)*

*4.6.0-rc5*

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

Requests ownership of an inbound doorbell resource and binds a callback
function to the resource. Returns 0 if the request has been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
