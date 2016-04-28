.. -*- coding: utf-8; mode: rst -*-

.. _API-sil-set-mode:

============
sil_set_mode
============

*man sil_set_mode(9)*

*4.6.0-rc5*

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

Wrap the libata method for device setup as after the setup we need to
inspect the results and do some configuration work


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
