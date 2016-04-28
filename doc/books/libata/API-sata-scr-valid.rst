.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-scr-valid:

==============
sata_scr_valid
==============

*man sata_scr_valid(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
