
.. _API-cable-is-40wire:

===============
cable_is_40wire
===============

*man cable_is_40wire(9)*

*4.6.0-rc1*

40/80/SATA decider


Synopsis
========

.. c:function:: int cable_is_40wire( struct ata_port * ap )

Arguments
=========

``ap``
    port to consider


Description
===========

This function encapsulates the policy for speed management in one place. At the moment we don't cache the result but there is a good case for setting ap->cbl to the result when we
are called with unknown cables (and figuring out if it impacts hotplug at all).

Return 1 if the cable appears to be 40 wire.
