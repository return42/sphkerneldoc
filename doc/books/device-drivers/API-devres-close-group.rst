
.. _API-devres-close-group:

==================
devres_close_group
==================

*man devres_close_group(9)*

*4.6.0-rc1*

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

Close the group identified by ``id``. If ``id`` is NULL, the latest open group is selected.
