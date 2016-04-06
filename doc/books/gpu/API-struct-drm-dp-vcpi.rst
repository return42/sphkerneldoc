
.. _API-struct-drm-dp-vcpi:

==================
struct drm_dp_vcpi
==================

*man struct drm_dp_vcpi(9)*

*4.6.0-rc1*

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
