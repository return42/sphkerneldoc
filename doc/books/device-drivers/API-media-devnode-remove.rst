
.. _API-media-devnode-remove:

====================
media_devnode_remove
====================

*man media_devnode_remove(9)*

*4.6.0-rc1*

removes a device node interface


Synopsis
========

.. c:function:: void media_devnode_remove( struct media_intf_devnode * devnode )

Arguments
=========

``devnode``
    pointer to ``media_intf_devnode`` to be freed.


Description
===========

When a device node interface is removed, all links to it are automatically removed.
