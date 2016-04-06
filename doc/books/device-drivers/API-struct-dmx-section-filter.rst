
.. _API-struct-dmx-section-filter:

=========================
struct dmx_section_filter
=========================

*man struct dmx_section_filter(9)*

*4.6.0-rc1*

Structure that describes a section filter


Synopsis
========

.. code-block:: c

    struct dmx_section_filter {
      u8 filter_value[DMX_MAX_FILTER_SIZE];
      u8 filter_mask[DMX_MAX_FILTER_SIZE];
      u8 filter_mode[DMX_MAX_FILTER_SIZE];
      struct dmx_section_feed * parent;
      void * priv;
    };


Members
=======

filter_value[DMX_MAX_FILTER_SIZE]
    Contains up to 16 bytes (128 bits) of the TS section header that will be matched by the section filter

filter_mask[DMX_MAX_FILTER_SIZE]
    Contains a 16 bytes (128 bits) filter mask with the bits specified by ``filter_value`` that will be used on the filter match logic.

filter_mode[DMX_MAX_FILTER_SIZE]
    Contains a 16 bytes (128 bits) filter mode.

parent
    Pointer to struct dmx_section_feed.

priv
    Pointer to private data of the API client.


Description
===========

The ``filter_mask`` controls which bits of ``filter_value`` are compared with the section headers/payload. On a binary value of 1 in filter_mask, the corresponding bits are
compared. The filter only accepts sections that are equal to filter_value in all the tested bit positions.
