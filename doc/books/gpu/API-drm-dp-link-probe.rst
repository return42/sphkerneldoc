
.. _API-drm-dp-link-probe:

=================
drm_dp_link_probe
=================

*man drm_dp_link_probe(9)*

*4.6.0-rc1*

probe a DisplayPort link for capabilities


Synopsis
========

.. c:function:: int drm_dp_link_probe( struct drm_dp_aux * aux, struct drm_dp_link * link )

Arguments
=========

``aux``
    DisplayPort AUX channel

``link``
    pointer to structure in which to return link capabilities


Description
===========

The structure filled in by this function can usually be passed directly into ``drm_dp_link_power_up`` and ``drm_dp_link_configure`` to power up and configure the link based on the
link's capabilities.

Returns 0 on success or a negative error code on failure.
