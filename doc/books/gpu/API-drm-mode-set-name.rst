.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-set-name:

=================
drm_mode_set_name
=================

*man drm_mode_set_name(9)*

*4.6.0-rc5*

set the name on a mode


Synopsis
========

.. c:function:: void drm_mode_set_name( struct drm_display_mode * mode )

Arguments
=========

``mode``
    name will be set in this mode


Description
===========

Set the name of ``mode`` to a standard format which is
<hdisplay>x<vdisplay> with an optional 'i' suffix for interlaced modes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
