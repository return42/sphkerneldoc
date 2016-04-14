.. -*- coding: utf-8; mode: rst -*-

============
membarrier.h
============

.. _`membarrier_cmd`:

enum membarrier_cmd
===================

.. c:type:: enum membarrier_cmd

    membarrier system call command



Constants
---------

:``MEMBARRIER_CMD_QUERY``:
    Query the set of supported commands. It returns
    a bitmask of valid commands.

:``MEMBARRIER_CMD_SHARED``:
    Execute a memory barrier on all running threads.::

                             Upon return from system call, the caller thread
                             is ensured that all running threads have passed
                             through a state where all memory accesses to
                             user-space addresses match program order between
                             entry to and return from the system call
                             (non-running threads are de facto in such a
                             state). This covers threads from all processes
                             running on the system. This command returns 0.


Description
-----------

Command to be passed to the membarrier system call. The commands need to
be a single bit each, except for MEMBARRIER_CMD_QUERY which is assigned to
the value 0.

