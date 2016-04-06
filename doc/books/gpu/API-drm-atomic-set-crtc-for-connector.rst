
.. _API-drm-atomic-set-crtc-for-connector:

=================================
drm_atomic_set_crtc_for_connector
=================================

*man drm_atomic_set_crtc_for_connector(9)*

*4.6.0-rc1*

set crtc for connector


Synopsis
========

.. c:function:: int drm_atomic_set_crtc_for_connector( struct drm_connector_state * conn_state, struct drm_crtc * crtc )

Arguments
=========

``conn_state``
    atomic state object for the connector

``crtc``
    crtc to use for the connector


Description
===========

Changing the assigned crtc for a connector requires us to grab the lock and state for the new crtc, as needed. This function takes care of all these details besides updating the
pointer in the state object itself.


Returns
=======

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is EDEADLK then the w/w mutex code has detected a deadlock and the entire atomic sequence must be restarted. All
other errors are fatal.
