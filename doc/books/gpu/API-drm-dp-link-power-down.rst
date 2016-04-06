
.. _API-drm-dp-link-power-down:

======================
drm_dp_link_power_down
======================

*man drm_dp_link_power_down(9)*

*4.6.0-rc1*

power down a DisplayPort link


Synopsis
========

.. c:function:: int drm_dp_link_power_down( struct drm_dp_aux * aux, struct drm_dp_link * link )

Arguments
=========

``aux``
    DisplayPort AUX channel

``link``
    pointer to a structure containing the link configuration


Description
===========

Returns 0 on success or a negative error code on failure.
