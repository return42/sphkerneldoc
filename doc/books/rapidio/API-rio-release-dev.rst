
.. _API-rio-release-dev:

===============
rio_release_dev
===============

*man rio_release_dev(9)*

*4.6.0-rc1*

Frees a RIO device struct


Synopsis
========

.. c:function:: void rio_release_dev( struct device * dev )

Arguments
=========

``dev``
    LDM device associated with a RIO device struct


Description
===========

Gets the RIO device struct associated a RIO device struct. The RIO device struct is freed.
