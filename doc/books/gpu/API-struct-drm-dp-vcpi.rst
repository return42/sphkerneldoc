.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-dp-vcpi:

==================
struct drm_dp_vcpi
==================

*man struct drm_dp_vcpi(9)*

*4.6.0-rc5*

Virtual Channel Payload Identifier


Synopsis
========

.. code-block:: c

    struct drm_dp_vcpi {
      int vcpi;
      int pbn;
      int aligned_pbn;
      int num_slots;
    };


Members
=======

vcpi
    Virtual channel ID.

pbn
    Payload Bandwidth Number for this channel

aligned_pbn
    PBN aligned with slot size

num_slots
    number of slots for this PBN


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
