
.. _API-drm-mode-probed-add:

===================
drm_mode_probed_add
===================

*man drm_mode_probed_add(9)*

*4.6.0-rc1*

add a mode to a connector's probed_mode list


Synopsis
========

.. c:function:: void drm_mode_probed_add( struct drm_connector * connector, struct drm_display_mode * mode )

Arguments
=========

``connector``
    connector the new mode

``mode``
    mode data


Description
===========

Add ``mode`` to ``connector``'s probed_mode list for later use. This list should then in a second step get filtered and all the modes actually supported by the hardware moved to
the ``connector``'s modes list.
