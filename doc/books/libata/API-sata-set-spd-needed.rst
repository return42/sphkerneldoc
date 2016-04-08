
.. _API-sata-set-spd-needed:

===================
sata_set_spd_needed
===================

*man sata_set_spd_needed(9)*

*4.6.0-rc1*

is SATA spd configuration needed


Synopsis
========

.. c:function:: int sata_set_spd_needed( struct ata_link * link )

Arguments
=========

``link``
    Link in question


Description
===========

Test whether the spd limit in SControl matches ``link``->sata_spd_limit. This function is used to determine whether hardreset is necessary to apply SATA spd configuration.


LOCKING
=======

Inherited from caller.


RETURNS
=======

1 if SATA spd configuration is needed, 0 otherwise.
