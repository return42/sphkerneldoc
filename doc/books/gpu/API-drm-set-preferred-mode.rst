.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-set-preferred-mode:

======================
drm_set_preferred_mode
======================

*man drm_set_preferred_mode(9)*

*4.6.0-rc5*

Sets the preferred mode of a connector


Synopsis
========

.. c:function:: void drm_set_preferred_mode( struct drm_connector * connector, int hpref, int vpref )

Arguments
=========

``connector``
    connector whose mode list should be processed

``hpref``
    horizontal resolution of preferred mode

``vpref``
    vertical resolution of preferred mode


Description
===========

Marks a mode as preferred if it matches the resolution specified by
``hpref`` and ``vpref``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
