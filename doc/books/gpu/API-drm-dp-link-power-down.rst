.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dp-link-power-down:

======================
drm_dp_link_power_down
======================

*man drm_dp_link_power_down(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
