.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-close-group:

==================
devres_close_group
==================

*man devres_close_group(9)*

*4.6.0-rc5*

Close a devres group


Synopsis
========

.. c:function:: void devres_close_group( struct device * dev, void * id )

Arguments
=========

``dev``
    Device to close devres group for

``id``
    ID of target group, can be NULL


Description
===========

Close the group identified by ``id``. If ``id`` is NULL, the latest open
group is selected.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
