.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-edid-is-valid:

=================
drm_edid_is_valid
=================

*man drm_edid_is_valid(9)*

*4.6.0-rc5*

sanity check EDID data


Synopsis
========

.. c:function:: bool drm_edid_is_valid( struct edid * edid )

Arguments
=========

``edid``
    EDID data


Description
===========

Sanity-check an entire EDID record (including extensions)


Return
======

True if the EDID data is valid, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
