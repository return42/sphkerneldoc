.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-release-dev:

===============
rio_release_dev
===============

*man rio_release_dev(9)*

*4.6.0-rc5*

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

Gets the RIO device struct associated a RIO device struct. The RIO
device struct is freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
