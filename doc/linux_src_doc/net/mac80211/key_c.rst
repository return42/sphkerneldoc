.. -*- coding: utf-8; mode: rst -*-

=====
key.c
=====

.. _`key-handling-basics`:

Key handling basics
===================

Key handling in mac80211 is done based on per-interface (sub_if_data)
keys and per-station keys. Since each station belongs to an interface,
each station key also belongs to that interface.

Hardware acceleration is done on a best-effort basis for algorithms
that are implemented in software,  for each key the hardware is asked
to enable that key for offloading but if it cannot do that the key is
simply kept for software encryption (unless it is for an algorithm
that isn't implemented in software).
There is currently no way of knowing whether a key is handled in SW
or HW except by looking into debugfs.

All key management is internally protected by a mutex. Within all
other parts of mac80211, key references are, just as STA structure
references, protected by RCU. Note, however, that some things are
unprotected, namely the key->sta dereferences within the hardware
acceleration functions. This means that :c:func:`sta_info_destroy` must
remove the key which waits for an RCU grace period.

