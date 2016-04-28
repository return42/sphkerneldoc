.. -*- coding: utf-8; mode: rst -*-

.. _API-pnp-disable-dev:

===============
pnp_disable_dev
===============

*man pnp_disable_dev(9)*

*4.6.0-rc5*

disables device


Synopsis
========

.. c:function:: int pnp_disable_dev( struct pnp_dev * dev )

Arguments
=========

``dev``
    pointer to the desired device


Description
===========

inform the correct pnp protocol so that resources can be used by other
devices


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
