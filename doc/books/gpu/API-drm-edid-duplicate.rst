.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-edid-duplicate:

==================
drm_edid_duplicate
==================

*man drm_edid_duplicate(9)*

*4.6.0-rc5*

duplicate an EDID and the extensions


Synopsis
========

.. c:function:: struct edid * drm_edid_duplicate( const struct edid * edid )

Arguments
=========

``edid``
    EDID to duplicate


Return
======

Pointer to duplicated EDID or NULL on allocation failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
