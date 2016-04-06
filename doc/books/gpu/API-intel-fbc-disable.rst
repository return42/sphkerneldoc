
.. _API-intel-fbc-disable:

=================
intel_fbc_disable
=================

*man intel_fbc_disable(9)*

*4.6.0-rc1*

disable FBC if it's associated with crtc


Synopsis
========

.. c:function:: void intel_fbc_disable( struct intel_crtc * crtc )

Arguments
=========

``crtc``
    the CRTC


Description
===========

This function disables FBC if it's associated with the provided CRTC.
