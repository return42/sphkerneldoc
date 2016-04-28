.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-edid-to-eld:

===============
drm_edid_to_eld
===============

*man drm_edid_to_eld(9)*

*4.6.0-rc5*

build ELD from EDID


Synopsis
========

.. c:function:: void drm_edid_to_eld( struct drm_connector * connector, struct edid * edid )

Arguments
=========

``connector``
    connector corresponding to the HDMI/DP sink

``edid``
    EDID to parse


Description
===========

Fill the ELD (EDID-Like Data) buffer for passing to the audio driver.
The Conn_Type, HDCP and Port_ID ELD fields are left for the graphics
driver to fill in.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
