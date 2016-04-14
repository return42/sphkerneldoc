.. -*- coding: utf-8; mode: rst -*-

=========
seccomp.h
=========

.. _`seccomp_data`:

struct seccomp_data
===================

.. c:type:: struct seccomp_data

    the format the BPF program executes over.



Definition
----------

.. code-block:: c

  struct seccomp_data {
    int nr;
    __u32 arch;
    __u64 instruction_pointer;
    __u64 args[6];
  };



Members
-------

:``nr``:
    the system call number

:``arch``:
    indicates system call convention as an AUDIT_ARCH_\* value
    as defined in <linux/audit.h>.

:``instruction_pointer``:
    at the time of the system call.

:``args[6]``:
    up to 6 system call arguments always stored as 64-bit values
    regardless of the architecture.


