
.. _API-intel-fbc-enable:

================
intel_fbc_enable
================

*man intel_fbc_enable(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: void intel_fbc_enable( struct intel_crtc * crtc )

Arguments
=========

``crtc``
    the CRTC


Description
===========

This function checks if the given CRTC was chosen for FBC, then enables it if possible. Notice that it doesn't activate FBC. It is valid to call intel_fbc_enable multiple times
for the same pipe without an intel_fbc_disable in the middle, as long as it is deactivated.
