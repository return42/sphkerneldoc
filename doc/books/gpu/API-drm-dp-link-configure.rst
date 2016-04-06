
.. _API-drm-dp-link-configure:

=====================
drm_dp_link_configure
=====================

*man drm_dp_link_configure(9)*

*4.6.0-rc1*

configure a DisplayPort link


Synopsis
========

.. c:function:: int drm_dp_link_configure( struct drm_dp_aux * aux, struct drm_dp_link * link )

Arguments
=========

``aux``
    DisplayPort AUX channel

``link``
    pointer to a structure containing the link configuration


Description
===========

Returns 0 on success or a negative error code on failure.
