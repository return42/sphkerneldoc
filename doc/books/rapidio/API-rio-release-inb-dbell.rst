.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-release-inb-dbell:

=====================
rio_release_inb_dbell
=====================

*man rio_release_inb_dbell(9)*

*4.6.0-rc5*

release inbound doorbell message service


Synopsis
========

.. c:function:: int rio_release_inb_dbell( struct rio_mport * mport, u16 start, u16 end )

Arguments
=========

``mport``
    RIO master port from which to release the doorbell resource

``start``
    Doorbell info range start

``end``
    Doorbell info range end


Description
===========

Releases ownership of an inbound doorbell resource and removes callback
from the doorbell event list. Returns 0 if the request has been
satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
