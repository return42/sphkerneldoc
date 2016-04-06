
.. _API-pnp-disable-dev:

===============
pnp_disable_dev
===============

*man pnp_disable_dev(9)*

*4.6.0-rc1*

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

inform the correct pnp protocol so that resources can be used by other devices
