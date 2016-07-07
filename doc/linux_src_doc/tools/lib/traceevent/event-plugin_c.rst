.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/event-plugin.c

.. _`traceevent_plugin_add_options`:

traceevent_plugin_add_options
=============================

.. c:function:: int traceevent_plugin_add_options(const char *name, struct pevent_plugin_option *options)

    Add a set of options by a plugin

    :param const char \*name:
        The name of the plugin adding the options

    :param struct pevent_plugin_option \*options:
        The set of options being loaded

.. _`traceevent_plugin_add_options.description`:

Description
-----------

Sets the options with the values that have been added by user.

.. _`traceevent_plugin_remove_options`:

traceevent_plugin_remove_options
================================

.. c:function:: void traceevent_plugin_remove_options(struct pevent_plugin_option *options)

    remove plugin options that were registered

    :param struct pevent_plugin_option \*options:
        Options to removed that were registered with traceevent_plugin_add_options

.. _`traceevent_print_plugins`:

traceevent_print_plugins
========================

.. c:function:: void traceevent_print_plugins(struct trace_seq *s, const char *prefix, const char *suffix, const struct plugin_list *list)

    print out the list of plugins loaded

    :param struct trace_seq \*s:
        the trace_seq descripter to write to

    :param const char \*prefix:
        The prefix string to add before listing the option name

    :param const char \*suffix:
        The suffix string ot append after the option name

    :param const struct plugin_list \*list:
        The list of plugins (usually returned by \ :c:func:`traceevent_load_plugins`\ 

.. _`traceevent_print_plugins.description`:

Description
-----------

Writes to the trace_seq \ ``s``\  the list of plugins (files) that is
returned by \ :c:func:`traceevent_load_plugins`\ . Use \ ``prefix``\  and \ ``suffix``\  for formating:
\ ``prefix``\  = "  ", \ ``suffix``\  = "\n".

.. This file was automatic generated / don't edit.

