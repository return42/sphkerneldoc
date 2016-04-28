.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-remove-group:

===================
devres_remove_group
===================

*man devres_remove_group(9)*

*4.6.0-rc5*

Remove a devres group


Synopsis
========

.. c:function:: void devres_remove_group( struct device * dev, void * id )

Arguments
=========

``dev``
    Device to remove group for

``id``
    ID of target group, can be NULL


Description
===========

Remove the group identified by ``id``. If ``id`` is NULL, the latest
open group is selected. Note that removing a group doesn't affect any
other resources.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
