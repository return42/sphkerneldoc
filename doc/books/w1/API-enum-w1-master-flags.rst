.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-w1-master-flags:

====================
enum w1_master_flags
====================

*man enum w1_master_flags(9)*

*4.6.0-rc5*

bitfields used in w1_master.flags


Synopsis
========

.. code-block:: c

    enum w1_master_flags {
      W1_ABORT_SEARCH,
      W1_WARN_MAX_COUNT
    };


Constants
=========

W1_ABORT_SEARCH
    abort searching early on shutdown

W1_WARN_MAX_COUNT
    limit warning when the maximum count is reached


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
