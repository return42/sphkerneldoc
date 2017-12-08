.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/mmap.h

.. _`perf_mmap`:

struct perf_mmap
================

.. c:type:: struct perf_mmap

    perf's ring buffer mmap details

.. _`perf_mmap.definition`:

Definition
----------

.. code-block:: c

    struct perf_mmap {
        void *base;
        int mask;
        int fd;
        refcount_t refcnt;
        u64 prev;
        struct auxtrace_mmap auxtrace_mmap;
        char event_copy[PERF_SAMPLE_MAX_SIZE] __aligned(8);
    }

.. _`perf_mmap.members`:

Members
-------

base
    *undescribed*

mask
    *undescribed*

fd
    *undescribed*

refcnt
    *undescribed*

prev
    *undescribed*

auxtrace_mmap
    *undescribed*

event_copy
    *undescribed*

.. _`perf_mmap.description`:

Description
-----------

@refcnt - e.g. code using PERF_EVENT_IOC_SET_OUTPUT to share this

.. This file was automatic generated / don't edit.

