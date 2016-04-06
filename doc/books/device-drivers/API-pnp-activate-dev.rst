
.. _API-pnp-activate-dev:

================
pnp_activate_dev
================

*man pnp_activate_dev(9)*

*4.6.0-rc1*

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
