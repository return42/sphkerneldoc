.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-init-em:

===========
rio_init_em
===========

*man rio_init_em(9)*

*4.6.0-rc5*

Initializes RIO Error Management (for switches)


Synopsis
========

.. c:function:: void rio_init_em( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

For each enumerated switch, call device-specific error management
initialization routine (if supplied by the switch driver).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
