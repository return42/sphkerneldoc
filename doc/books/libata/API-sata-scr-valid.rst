
.. _API-sata-scr-valid:

==============
sata_scr_valid
==============

*man sata_scr_valid(9)*

*4.6.0-rc1*

test whether SCRs are accessible


Synopsis
========

.. c:function:: int sata_scr_valid( struct ata_link * link )

Arguments
=========

``link``
    ATA link to test SCR accessibility for


Description
===========

Test whether SCRs are accessible for ``link``.


LOCKING
=======

None.


RETURNS
=======

1 if SCRs are accessible, 0 otherwise.
