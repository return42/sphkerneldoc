.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-select-eld:

==============
drm_select_eld
==============

*man drm_select_eld(9)*

*4.6.0-rc5*

select one ELD from multiple HDMI/DP sinks


Synopsis
========

.. c:function:: struct drm_connector * drm_select_eld( struct drm_encoder * encoder )

Arguments
=========

``encoder``
    the encoder just changed display mode


Description
===========

It's possible for one encoder to be associated with multiple HDMI/DP
sinks. The policy is now hard coded to simply use the first HDMI/DP
sink's ELD.


Return
======

The connector associated with the first HDMI/DP sink that has ELD
attached to it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
