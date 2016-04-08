
.. _API-sata-link-scr-lpm:

=================
sata_link_scr_lpm
=================

*man sata_link_scr_lpm(9)*

*4.6.0-rc1*

manipulate SControl IPM and SPM fields


Synopsis
========

.. c:function:: int sata_link_scr_lpm( struct ata_link * link, enum ata_lpm_policy policy, bool spm_wakeup )

Arguments
=========

``link``
    ATA link to manipulate SControl for

``policy``
    LPM policy to configure

``spm_wakeup``
    initiate LPM transition to active state


Description
===========

Manipulate the IPM field of the SControl register of ``link`` according to ``policy``. If ``policy`` is ATA_LPM_MAX_POWER and ``spm_wakeup`` is ``true``, the SPM field is
manipulated to wake up the link. This function also clears PHYRDY_CHG before returning.


LOCKING
=======

EH context.


RETURNS
=======

0 on success, -errno otherwise.
