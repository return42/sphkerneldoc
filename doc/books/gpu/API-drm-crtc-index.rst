.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-index:

==============
drm_crtc_index
==============

*man drm_crtc_index(9)*

*4.6.0-rc5*

find the index of a registered CRTC


Synopsis
========

.. c:function:: unsigned int drm_crtc_index( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    CRTC to find index for


Description
===========

Given a registered CRTC, return the index of that CRTC within a DRM
device's list of CRTCs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
