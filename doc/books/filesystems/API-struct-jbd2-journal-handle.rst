.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-jbd2-journal-handle:

==========================
struct jbd2_journal_handle
==========================

*man struct jbd2_journal_handle(9)*

*4.6.0-rc5*

The handle_s type is the concrete type associated with handle_t.


Synopsis
========

.. code-block:: c

    struct jbd2_journal_handle {
      union {unnamed_union};
      int h_buffer_credits;
      int h_ref;
      int h_err;
      unsigned int h_sync:1;
      unsigned int h_jdata:1;
      unsigned int h_aborted:1;
    #ifdef CONFIG_DEBUG_LOCK_ALLOC
    #endif
    };


Members
=======

{unnamed_union}
    anonymous

h_buffer_credits
    Number of remaining buffers we are allowed to dirty.

h_ref
    Reference count on this handle

h_err
    Field for caller's use to track errors through large fs operations

h_sync
    flag for sync-on-close

h_jdata
    flag to force data journaling

h_aborted
    flag indicating fatal error on handle


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
