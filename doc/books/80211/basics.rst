.. -*- coding: utf-8; mode: rst -*-

.. _basics:

=======================
Basic hardware handling
=======================

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


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-hw
    API-enum-ieee80211-hw-flags
    API-SET-IEEE80211-DEV
    API-SET-IEEE80211-PERM-ADDR
    API-struct-ieee80211-ops
    API-ieee80211-alloc-hw
    API-ieee80211-register-hw
    API-ieee80211-unregister-hw
    API-ieee80211-free-hw




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
