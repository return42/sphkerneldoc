.. -*- coding: utf-8; mode: rst -*-

.. _basics:

***********************
Basic hardware handling
***********************

TBD

This chapter shall contain information on getting a hw struct allocated
and registered with mac80211.

Since it is required to allocate rates/modes before registering a hw
struct, this chapter shall also contain information on setting up the
rate/mode structs.

Additionally, some discussion about the callbacks and the general
programming model should be in here, including the definition of
ieee80211_ops which will be referred to a lot.

Finally, a discussion of hardware capabilities should be done with
references to other parts of the book.


.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_hw

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_hw_flags

.. kernel-doc:: include/net/mac80211.h
    :functions: SET_IEEE80211_DEV

.. kernel-doc:: include/net/mac80211.h
    :functions: SET_IEEE80211_PERM_ADDR

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_ops

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_alloc_hw

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_register_hw

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_unregister_hw

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_free_hw



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
