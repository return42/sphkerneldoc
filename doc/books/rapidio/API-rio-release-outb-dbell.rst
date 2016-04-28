.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-release-outb-dbell:

======================
rio_release_outb_dbell
======================

*man rio_release_outb_dbell(9)*

*4.6.0-rc5*

release outbound doorbell message range


Synopsis
========

.. c:function:: int rio_release_outb_dbell( struct rio_dev * rdev, struct resource * res )

Arguments
=========

``rdev``
    RIO device from which to release the doorbell resource

``res``
    Doorbell resource to be freed


Description
===========

Releases ownership of a doorbell message range. Returns 0 if the request
has been satisfied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
