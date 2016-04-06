
.. _API-drm-helper-move-panel-connectors-to-head:

========================================
drm_helper_move_panel_connectors_to_head
========================================

*man drm_helper_move_panel_connectors_to_head(9)*

*4.6.0-rc1*

move panels to the front in the connector list


Synopsis
========

.. c:function:: void drm_helper_move_panel_connectors_to_head( struct drm_device * dev )

Arguments
=========

``dev``
    drm device to operate on


Description
===========

Some userspace presumes that the first connected connector is the main display, where it's supposed to display e.g. the login screen. For laptops, this should be the main panel.
Use this function to sort all (eDP/LVDS) panels to the front of the connector list, instead of painstakingly trying to initialize them in the right order.
