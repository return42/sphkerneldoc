
.. _API-sil-set-mode:

============
sil_set_mode
============

*man sil_set_mode(9)*

*4.6.0-rc1*

wrap set_mode functions


Synopsis
========

.. c:function:: int sil_set_mode( struct ata_link * link, struct ata_device ** r_failed )

Arguments
=========

``link``
    link to set up

``r_failed``
    returned device when we fail


Description
===========

Wrap the libata method for device setup as after the setup we need to inspect the results and do some configuration work
