.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-release-group:

====================
devres_release_group
====================

*man devres_release_group(9)*

*4.6.0-rc5*

Release resources in a devres group


Synopsis
========

.. c:function:: int devres_release_group( struct device * dev, void * id )

Arguments
=========

``dev``
    Device to release group for

``id``
    ID of target group, can be NULL


Description
===========

Release all resources in the group identified by ``id``. If ``id`` is
NULL, the latest open group is selected. The selected group and groups
properly nested inside the selected group are removed.


RETURNS
=======

The number of released non-group resources.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
