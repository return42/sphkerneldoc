.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-edid-header-is-valid:

========================
drm_edid_header_is_valid
========================

*man drm_edid_header_is_valid(9)*

*4.6.0-rc5*

sanity check the header of the base EDID block


Synopsis
========

.. c:function:: int drm_edid_header_is_valid( const u8 * raw_edid )

Arguments
=========

``raw_edid``
    pointer to raw base EDID block


Description
===========

Sanity check the header of the base EDID block.


Return
======

8 if the header is perfect, down to 0 if it's totally wrong.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
