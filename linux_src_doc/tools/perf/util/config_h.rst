.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/config.h

.. _`perf_config_sections__for_each_entry`:

perf_config_sections__for_each_entry
====================================

.. c:function::  perf_config_sections__for_each_entry( list,  section)

    iterate thru all the sections

    :param list:
        list_head instance to iterate
    :type list: 

    :param section:
        struct perf_config_section iterator
    :type section: 

.. _`perf_config_items__for_each_entry`:

perf_config_items__for_each_entry
=================================

.. c:function::  perf_config_items__for_each_entry( list,  item)

    iterate thru all the items

    :param list:
        list_head instance to iterate
    :type list: 

    :param item:
        struct perf_config_item iterator
    :type item: 

.. _`perf_config_set__for_each_entry`:

perf_config_set__for_each_entry
===============================

.. c:function::  perf_config_set__for_each_entry( set,  section,  item)

    iterate thru all the config section-item pairs

    :param set:
        evlist instance to iterate
    :type set: 

    :param section:
        struct perf_config_section iterator
    :type section: 

    :param item:
        struct perf_config_item iterator
    :type item: 

.. This file was automatic generated / don't edit.

