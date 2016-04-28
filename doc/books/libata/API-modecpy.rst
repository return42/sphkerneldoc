.. -*- coding: utf-8; mode: rst -*-

.. _API-modecpy:

=======
modecpy
=======

*man modecpy(9)*

*4.6.0-rc5*

Prepare response for MODE SENSE


Synopsis
========

.. c:function:: void modecpy( u8 * dest, const u8 * src, int n, bool changeable )

Arguments
=========

``dest``
    output buffer

``src``
    data being copied

``n``
    length of mode page

``changeable``
    whether changeable parameters are requested


Description
===========

Generate a generic MODE SENSE page for either current or changeable
parameters.


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
