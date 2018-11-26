.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/event-plugin.c

.. _`tep_plugin_list_options`:

tep_plugin_list_options
=======================

.. c:function:: char **tep_plugin_list_options( void)

    get list of plugin options

    :param void:
        no arguments
    :type void: 

.. _`tep_plugin_list_options.description`:

Description
-----------

Returns an array of char strings that list the currently registered
plugin options in the format of <plugin>:<option>. This list can be
used by toggling the option.

Returns NULL if there's no options registered. On error it returns
INVALID_PLUGIN_LIST_OPTION

Must be freed with \ :c:func:`tep_plugin_free_options_list`\ .

.. _`tep_plugin_add_options`:

tep_plugin_add_options
======================

.. c:function:: int tep_plugin_add_options(const char *name, struct tep_plugin_option *options)

    Add a set of options by a plugin

    :param name:
        The name of the plugin adding the options
    :type name: const char \*

    :param options:
        The set of options being loaded
    :type options: struct tep_plugin_option \*

.. _`tep_plugin_add_options.description`:

Description
-----------

Sets the options with the values that have been added by user.

.. _`tep_plugin_remove_options`:

tep_plugin_remove_options
=========================

.. c:function:: void tep_plugin_remove_options(struct tep_plugin_option *options)

    remove plugin options that were registered

    :param options:
        Options to removed that were registered with tep_plugin_add_options
    :type options: struct tep_plugin_option \*

.. _`tep_print_plugins`:

tep_print_plugins
=================

.. c:function:: void tep_print_plugins(struct trace_seq *s, const char *prefix, const char *suffix, const struct tep_plugin_list *list)

    print out the list of plugins loaded

    :param s:
        the trace_seq descripter to write to
    :type s: struct trace_seq \*

    :param prefix:
        The prefix string to add before listing the option name
    :type prefix: const char \*

    :param suffix:
        The suffix string ot append after the option name
    :type suffix: const char \*

    :param list:
        The list of plugins (usually returned by \ :c:func:`tep_load_plugins`\ 
    :type list: const struct tep_plugin_list \*

.. _`tep_print_plugins.description`:

Description
-----------

Writes to the trace_seq \ ``s``\  the list of plugins (files) that is
returned by \ :c:func:`tep_load_plugins`\ . Use \ ``prefix``\  and \ ``suffix``\  for formating:
\ ``prefix``\  = "  ", \ ``suffix``\  = "\n".

.. This file was automatic generated / don't edit.

