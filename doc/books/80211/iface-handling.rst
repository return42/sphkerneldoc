.. -*- coding: utf-8; mode: rst -*-

.. _iface-handling:

******************
Virtual interfaces
******************

TBD

This chapter should describe virtual interface basics that are relevant
to the driver (VLANs, MGMT etc are not.) It should explain the use of
the add_iface/remove_iface callbacks as well as the interface
configuration callbacks.

Things related to AP mode should be discussed there.

Things related to supporting multiple interfaces should be in the
appropriate chapter, a BIG FAT note should be here about this though and
the recommendation to allow only a single interface in STA mode at
first!


.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_vif



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
