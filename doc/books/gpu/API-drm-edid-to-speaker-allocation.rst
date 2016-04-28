.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-edid-to-speaker-allocation:

==============================
drm_edid_to_speaker_allocation
==============================

*man drm_edid_to_speaker_allocation(9)*

*4.6.0-rc5*

extracts Speaker Allocation Data Blocks from EDID


Synopsis
========

.. c:function:: int drm_edid_to_speaker_allocation( struct edid * edid, u8 ** sadb )

Arguments
=========

``edid``
    EDID to parse

``sadb``
    pointer to the speaker block


Description
===========

Looks for CEA EDID block and extracts the Speaker Allocation Data Block
from it.


Note
====

The returned pointer needs to be freed using ``kfree``.


Return
======

The number of found Speaker Allocation Blocks or negative number on
error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
