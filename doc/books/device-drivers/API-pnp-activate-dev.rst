.. -*- coding: utf-8; mode: rst -*-

.. _API-pnp-activate-dev:

================
pnp_activate_dev
================

*man pnp_activate_dev(9)*

*4.6.0-rc5*

activates a PnP device for use


Synopsis
========

.. c:function:: int pnp_activate_dev( struct pnp_dev * dev )

Arguments
=========

``dev``
    pointer to the desired device


Description
===========

does not validate or set resources so be careful.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
