.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-open-group:

=================
devres_open_group
=================

*man devres_open_group(9)*

*4.6.0-rc5*

Open a new devres group


Synopsis
========

.. c:function:: void * devres_open_group( struct device * dev, void * id, gfp_t gfp )

Arguments
=========

``dev``
    Device to open devres group for

``id``
    Separator ID

``gfp``
    Allocation flags


Description
===========

Open a new devres group for ``dev`` with ``id``. For ``id``, using a
pointer to an object which won't be used for another group is
recommended. If ``id`` is NULL, address-wise unique ID is created.


RETURNS
=======

ID of the new group, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
