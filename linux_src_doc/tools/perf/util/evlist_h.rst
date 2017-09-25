.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/evlist.h

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

.. _`__evlist__for_each_entry`:

__evlist__for_each_entry
========================

.. c:function::  __evlist__for_each_entry( list,  evsel)

    iterate thru all the evsels

    :param  list:
        list_head instance to iterate

    :param  evsel:
        struct evsel iterator

.. _`evlist__for_each_entry`:

evlist__for_each_entry
======================

.. c:function::  evlist__for_each_entry( evlist,  evsel)

    iterate thru all the evsels

    :param  evlist:
        evlist instance to iterate

    :param  evsel:
        struct evsel iterator

.. _`__evlist__for_each_entry_continue`:

__evlist__for_each_entry_continue
=================================

.. c:function::  __evlist__for_each_entry_continue( list,  evsel)

    continue iteration thru all the evsels

    :param  list:
        list_head instance to iterate

    :param  evsel:
        struct evsel iterator

.. _`evlist__for_each_entry_continue`:

evlist__for_each_entry_continue
===============================

.. c:function::  evlist__for_each_entry_continue( evlist,  evsel)

    continue iteration thru all the evsels

    :param  evlist:
        evlist instance to iterate

    :param  evsel:
        struct evsel iterator

.. _`__evlist__for_each_entry_reverse`:

__evlist__for_each_entry_reverse
================================

.. c:function::  __evlist__for_each_entry_reverse( list,  evsel)

    iterate thru all the evsels in reverse order

    :param  list:
        list_head instance to iterate

    :param  evsel:
        struct evsel iterator

.. _`evlist__for_each_entry_reverse`:

evlist__for_each_entry_reverse
==============================

.. c:function::  evlist__for_each_entry_reverse( evlist,  evsel)

    iterate thru all the evsels in reverse order

    :param  evlist:
        evlist instance to iterate

    :param  evsel:
        struct evsel iterator

.. _`__evlist__for_each_entry_safe`:

__evlist__for_each_entry_safe
=============================

.. c:function::  __evlist__for_each_entry_safe( list,  tmp,  evsel)

    safely iterate thru all the evsels

    :param  list:
        list_head instance to iterate

    :param  tmp:
        struct evsel temp iterator

    :param  evsel:
        struct evsel iterator

.. _`evlist__for_each_entry_safe`:

evlist__for_each_entry_safe
===========================

.. c:function::  evlist__for_each_entry_safe( evlist,  tmp,  evsel)

    safely iterate thru all the evsels

    :param  evlist:
        evlist instance to iterate

    :param  tmp:
        struct evsel temp iterator

    :param  evsel:
        struct evsel iterator

.. This file was automatic generated / don't edit.

