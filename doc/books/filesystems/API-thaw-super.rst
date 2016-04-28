.. -*- coding: utf-8; mode: rst -*-

.. _API-thaw-super:

==========
thaw_super
==========

*man thaw_super(9)*

*4.6.0-rc5*

- unlock filesystem


Synopsis
========

.. c:function:: int thaw_super( struct super_block * sb )

Arguments
=========

``sb``
    the super to thaw


Description
===========

Unlocks the filesystem and marks it writeable again after
``freeze_super``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
