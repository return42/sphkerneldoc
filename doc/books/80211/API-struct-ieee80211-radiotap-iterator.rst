.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-radiotap-iterator:

==================================
struct ieee80211_radiotap_iterator
==================================

*man struct ieee80211_radiotap_iterator(9)*

*4.6.0-rc5*

tracks walk thru present radiotap args


Synopsis
========

.. code-block:: c

    struct ieee80211_radiotap_iterator {
      struct ieee80211_radiotap_header * _rtheader;
      const struct ieee80211_radiotap_vendor_namespaces * _vns;
      const struct ieee80211_radiotap_namespace * current_namespace;
      unsigned char * _arg;
      unsigned char * _next_ns_data;
      __le32 * _next_bitmap;
      unsigned char * this_arg;
      int this_arg_index;
      int this_arg_size;
      int is_radiotap_ns;
      int _max_length;
      int _arg_index;
      uint32_t _bitmap_shifter;
      int _reset_on_ext;
    };


Members
=======

_rtheader
    pointer to the radiotap header we are walking through

_vns
    vendor namespace definitions

current_namespace
    pointer to the current namespace definition (or internally ``NULL``
    if the current namespace is unknown)

_arg
    next argument pointer

_next_ns_data
    beginning of the next namespace's data

_next_bitmap
    internal pointer to next present u32

this_arg
    pointer to current radiotap arg; it is valid after each call to
    ``ieee80211_radiotap_iterator_next`` but also after
    ``ieee80211_radiotap_iterator_init`` where it will point to the
    beginning of the actual data portion

this_arg_index
    index of current arg, valid after each successful call to
    ``ieee80211_radiotap_iterator_next``

this_arg_size
    length of the current arg, for convenience

is_radiotap_ns
    indicates whether the current namespace is the default radiotap
    namespace or not

_max_length
    length of radiotap header in cpu byte ordering

_arg_index
    next argument index

_bitmap_shifter
    internal shifter for curr u32 bitmap, b0 set == arg present

_reset_on_ext
    internal; reset the arg index to 0 when going to the next bitmap
    word


Description
===========

Describes the radiotap parser state. Fields prefixed with an underscore
must not be used by users of the parser, only by the parser internally.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
