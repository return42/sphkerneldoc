.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-disc-mport:

==============
rio_disc_mport
==============

*man rio_disc_mport(9)*

*4.6.0-rc5*

Start discovery through a master port


Synopsis
========

.. c:function:: int rio_disc_mport( struct rio_mport * mport, u32 flags )

Arguments
=========

``mport``
    Master port to send transactions

``flags``
    discovery control flags


Description
===========

Starts the discovery process. If we have an active link, then wait for
the signal that enumeration is complete (if wait is allowed). When
enumeration completion is signaled, start recursive peer discovery.
Returns ``0`` if discovery succeeds or ``-EBUSY`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
