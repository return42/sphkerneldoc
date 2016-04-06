
.. _API-pnp-release-card-device:

=======================
pnp_release_card_device
=======================

*man pnp_release_card_device(9)*

*4.6.0-rc1*

call this when the driver no longer needs the device


Synopsis
========

.. c:function:: void pnp_release_card_device( struct pnp_dev * dev )

Arguments
=========

``dev``
    pointer to the PnP device structure
