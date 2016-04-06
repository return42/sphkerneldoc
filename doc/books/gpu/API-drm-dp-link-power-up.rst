
.. _API-drm-dp-link-power-up:

====================
drm_dp_link_power_up
====================

*man drm_dp_link_power_up(9)*

*4.6.0-rc1*

power up a DisplayPort link


Synopsis
========

.. c:function:: int drm_dp_link_power_up( struct drm_dp_aux * aux, struct drm_dp_link * link )

Arguments
=========

``aux``
    DisplayPort AUX channel

``link``
    pointer to a structure containing the link configuration


Description
===========

Returns 0 on success or a negative error code on failure.
