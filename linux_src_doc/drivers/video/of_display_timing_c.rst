.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/of_display_timing.c

.. _`parse_timing_property`:

parse_timing_property
=====================

.. c:function:: int parse_timing_property(const struct device_node *np, const char *name, struct timing_entry *result)

    parse timing_entry from device_node

    :param np:
        device_node with the property
    :type np: const struct device_node \*

    :param name:
        name of the property
    :type name: const char \*

    :param result:
        will be set to the return value
    :type result: struct timing_entry \*

.. _`parse_timing_property.description`:

Description
-----------

Every display_timing can be specified with either just the typical value or
a range consisting of min/typ/max. This function helps handling this

.. _`of_parse_display_timing`:

of_parse_display_timing
=======================

.. c:function:: int of_parse_display_timing(const struct device_node *np, struct display_timing *dt)

    parse display_timing entry from device_node

    :param np:
        device_node with the properties
    :type np: const struct device_node \*

    :param dt:
        *undescribed*
    :type dt: struct display_timing \*

.. _`of_get_display_timing`:

of_get_display_timing
=====================

.. c:function:: int of_get_display_timing(const struct device_node *np, const char *name, struct display_timing *dt)

    parse a display_timing entry

    :param np:
        device_node with the timing subnode
    :type np: const struct device_node \*

    :param name:
        name of the timing node
    :type name: const char \*

    :param dt:
        display_timing struct to fill
    :type dt: struct display_timing \*

.. _`of_get_display_timings`:

of_get_display_timings
======================

.. c:function:: struct display_timings *of_get_display_timings(const struct device_node *np)

    parse all display_timing entries from a device_node

    :param np:
        device_node with the subnodes
    :type np: const struct device_node \*

.. This file was automatic generated / don't edit.

