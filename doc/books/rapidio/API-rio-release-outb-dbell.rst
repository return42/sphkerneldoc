
.. _API-rio-release-outb-dbell:

======================
rio_release_outb_dbell
======================

*man rio_release_outb_dbell(9)*

*4.6.0-rc1*

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

Releases ownership of a doorbell message range. Returns 0 if the request has been satisfied.
