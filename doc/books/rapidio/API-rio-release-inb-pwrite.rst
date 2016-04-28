.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-release-inb-pwrite:

======================
rio_release_inb_pwrite
======================

*man rio_release_inb_pwrite(9)*

*4.6.0-rc5*

release inbound port-write message service associated with specific
RapidIO device


Synopsis
========

.. c:function:: int rio_release_inb_pwrite( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device which registered for inbound port-write callback


Description
===========

Removes callback from the rio_dev structure. Returns 0 if the request
has been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
