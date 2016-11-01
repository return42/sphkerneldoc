.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/config.h

.. _`perf_config_sections__for_each_entry`:

perf_config_sections__for_each_entry
====================================

.. c:function::  perf_config_sections__for_each_entry( list,  section)

    iterate thru all the sections

    :param  list:
        list_head instance to iterate

    :param  section:
        struct perf_config_section iterator

.. _`perf_config_items__for_each_entry`:

perf_config_items__for_each_entry
=================================

.. c:function::  perf_config_items__for_each_entry( list,  item)

    iterate thru all the items

    :param  list:
        list_head instance to iterate

    :param  item:
        struct perf_config_item iterator

.. _`perf_config_set__for_each_entry`:

perf_config_set__for_each_entry
===============================

.. c:function::  perf_config_set__for_each_entry( set,  section,  item)

    iterate thru all the config section-item pairs

    :param  set:
        evlist instance to iterate

    :param  section:
        struct perf_config_section iterator

    :param  item:
        struct perf_config_item iterator

.. This file was automatic generated / don't edit.

