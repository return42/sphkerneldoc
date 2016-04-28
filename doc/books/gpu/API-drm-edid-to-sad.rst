.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-edid-to-sad:

===============
drm_edid_to_sad
===============

*man drm_edid_to_sad(9)*

*4.6.0-rc5*

extracts SADs from EDID


Synopsis
========

.. c:function:: int drm_edid_to_sad( struct edid * edid, struct cea_sad ** sads )

Arguments
=========

``edid``
    EDID to parse

``sads``
    pointer that will be set to the extracted SADs


Description
===========

Looks for CEA EDID block and extracts SADs (Short Audio Descriptors)
from it.


Note
====

The returned pointer needs to be freed using ``kfree``.


Return
======

The number of found SADs or negative number on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
