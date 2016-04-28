.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-hotplug-event:

===========================
drm_fb_helper_hotplug_event
===========================

*man drm_fb_helper_hotplug_event(9)*

*4.6.0-rc5*

respond to a hotplug notification by probing all the outputs attached to
the fb


Synopsis
========

.. c:function:: int drm_fb_helper_hotplug_event( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    the drm_fb_helper


Description
===========

Scan the connectors attached to the fb_helper and try to put together a
setup after *notification of a change in output configuration.

Called at runtime, takes the mode config locks to be able to
check/change the modeset configuration. Must be run from process context
(which usually means either the output polling work or a work item
launched from the driver's hotplug interrupt).

Note that drivers may call this even before calling
drm_fb_helper_initial_config but only aftert drm_fb_helper_init.
This allows for a race-free fbcon setup and will make sure that the
fbdev emulation will not miss any hotplug events.


RETURNS
=======

0 on success and a non-zero error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
