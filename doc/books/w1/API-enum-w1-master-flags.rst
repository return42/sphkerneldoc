
.. _API-enum-w1-master-flags:

====================
enum w1_master_flags
====================

*man enum w1_master_flags(9)*

*4.6.0-rc1*

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
