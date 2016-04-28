.. -*- coding: utf-8; mode: rst -*-

.. _sta-info:

=====================
Station info handling
=====================


Programming information
=======================


.. toctree::
    :maxdepth: 1

    API-struct-sta-info
    API-enum-ieee80211-sta-info-flags


STA information lifetime rules
==============================

STA info structures (``struct sta_info``) are managed in a hash table
for faster lookup and a list for iteration. They are managed using RCU,
i.e. access to the list and hash table is protected by RCU.

Upon allocating a STA info structure with ``sta_info_alloc``, the caller
owns that structure. It must then insert it into the hash table using
either ``sta_info_insert`` or ``sta_info_insert_rcu``; only in the
latter case (which acquires an rcu read section but must not be called
from within one) will the pointer still be valid after the call. Note
that the caller may not do much with the STA info before inserting it,
in particular, it may not start any mesh peer link management or add
encryption keys.

When the insertion fails (``sta_info_insert``) returns non-zero), the
structure will have been freed by ``sta_info_insert``!

Station entries are added by mac80211 when you establish a link with a
peer. This means different things for the different type of interfaces
we support. For a regular station this mean we add the AP sta when we
receive an association response from the AP. For IBSS this occurs when
get to know about a peer on the same IBSS. For WDS we add the sta for
the peer immediately upon device open. When using AP mode we add
stations for each respective station upon request from userspace through
nl80211.

In order to remove a STA info structure, various sta_info_destroy_*()
calls are available.

There is no concept of ownership on a STA entry, each structure is owned
by the global hash table/list until it is removed. All users of the
structure need to be RCU protected so that the structure won't be freed
before they are done using it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
