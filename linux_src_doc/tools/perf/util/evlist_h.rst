.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/evlist.h

.. _`__evlist__for_each_entry`:

\__evlist__for_each_entry
=========================

.. c:function::  __evlist__for_each_entry( list,  evsel)

    iterate thru all the evsels

    :param list:
        list_head instance to iterate
    :type list: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`evlist__for_each_entry`:

evlist__for_each_entry
======================

.. c:function::  evlist__for_each_entry( evlist,  evsel)

    iterate thru all the evsels

    :param evlist:
        evlist instance to iterate
    :type evlist: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`__evlist__for_each_entry_continue`:

\__evlist__for_each_entry_continue
==================================

.. c:function::  __evlist__for_each_entry_continue( list,  evsel)

    continue iteration thru all the evsels

    :param list:
        list_head instance to iterate
    :type list: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`evlist__for_each_entry_continue`:

evlist__for_each_entry_continue
===============================

.. c:function::  evlist__for_each_entry_continue( evlist,  evsel)

    continue iteration thru all the evsels

    :param evlist:
        evlist instance to iterate
    :type evlist: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`__evlist__for_each_entry_reverse`:

\__evlist__for_each_entry_reverse
=================================

.. c:function::  __evlist__for_each_entry_reverse( list,  evsel)

    iterate thru all the evsels in reverse order

    :param list:
        list_head instance to iterate
    :type list: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`evlist__for_each_entry_reverse`:

evlist__for_each_entry_reverse
==============================

.. c:function::  evlist__for_each_entry_reverse( evlist,  evsel)

    iterate thru all the evsels in reverse order

    :param evlist:
        evlist instance to iterate
    :type evlist: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`__evlist__for_each_entry_safe`:

\__evlist__for_each_entry_safe
==============================

.. c:function::  __evlist__for_each_entry_safe( list,  tmp,  evsel)

    safely iterate thru all the evsels

    :param list:
        list_head instance to iterate
    :type list: 

    :param tmp:
        struct evsel temp iterator
    :type tmp: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. _`evlist__for_each_entry_safe`:

evlist__for_each_entry_safe
===========================

.. c:function::  evlist__for_each_entry_safe( evlist,  tmp,  evsel)

    safely iterate thru all the evsels

    :param evlist:
        evlist instance to iterate
    :type evlist: 

    :param tmp:
        struct evsel temp iterator
    :type tmp: 

    :param evsel:
        struct evsel iterator
    :type evsel: 

.. This file was automatic generated / don't edit.

