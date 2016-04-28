.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-dmx-demux-caps:

===================
enum dmx_demux_caps
===================

*man enum dmx_demux_caps(9)*

*4.6.0-rc5*

MPEG-2 TS Demux capabilities bitmap


Synopsis
========

.. code-block:: c

    enum dmx_demux_caps {
      DMX_TS_FILTERING,
      DMX_SECTION_FILTERING,
      DMX_MEMORY_BASED_FILTERING
    };


Constants
=========

DMX_TS_FILTERING
    set if TS filtering is supported;

DMX_SECTION_FILTERING
    set if section filtering is supported;

DMX_MEMORY_BASED_FILTERING
    set if ``write`` available.


Description
===========

Those flags are OR'ed in the ``dmx_demux``.\ ``capabilities`` field


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
