
.. _API-of-drm-find-bridge:

==================
of_drm_find_bridge
==================

*man of_drm_find_bridge(9)*

*4.6.0-rc1*

find the bridge corresponding to the device node in the global bridge list


Synopsis
========

.. c:function:: struct drm_bridge ⋆ of_drm_find_bridge( struct device_node * np )

Arguments
=========

``np``
    device node


RETURNS
=======

drm_bridge control struct on success, NULL on failure
