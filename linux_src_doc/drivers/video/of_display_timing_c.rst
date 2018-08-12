.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/of_display_timing.c

.. _`parse_timing_property`:

parse_timing_property
=====================

.. c:function:: int parse_timing_property(const struct device_node *np, const char *name, struct timing_entry *result)

    parse timing_entry from device_node

    :param const struct device_node \*np:
        device_node with the property

    :param const char \*name:
        name of the property

    :param struct timing_entry \*result:
        will be set to the return value

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

    :param const struct device_node \*np:
        device_node with the properties

    :param struct display_timing \*dt:
        *undescribed*

.. _`of_get_display_timing`:

of_get_display_timing
=====================

.. c:function:: int of_get_display_timing(const struct device_node *np, const char *name, struct display_timing *dt)

    parse a display_timing entry

    :param const struct device_node \*np:
        device_node with the timing subnode

    :param const char \*name:
        name of the timing node

    :param struct display_timing \*dt:
        display_timing struct to fill

.. _`of_get_display_timings`:

of_get_display_timings
======================

.. c:function:: struct display_timings *of_get_display_timings(const struct device_node *np)

    parse all display_timing entries from a device_node

    :param const struct device_node \*np:
        device_node with the subnodes

.. This file was automatic generated / don't edit.

