
.. _API-thaw-super:

==========
thaw_super
==========

*man thaw_super(9)*

*4.6.0-rc1*

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

Unlocks the filesystem and marks it writeable again after ``freeze_super``.
