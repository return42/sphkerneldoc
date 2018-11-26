.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/fdtget.c

.. _`show_data`:

show_data
=========

.. c:function:: int show_data(struct display_info *disp, const char *data, int len)

    :param disp:
        *undescribed*
    :type disp: struct display_info \*

    :param data:
        *undescribed*
    :type data: const char \*

    :param len:
        *undescribed*
    :type len: int

.. _`show_data.description`:

Description
-----------

If a specific data type is provided in disp, then this is used. Otherwise
we try to guess the data type / size from the contents.

\ ``param``\  disp          Display information / options
\ ``param``\  data          Data to display
\ ``param``\  len           Maximum length of buffer
\ ``return``\  0 if ok, -1 if data does not match format

.. _`list_properties`:

list_properties
===============

.. c:function:: int list_properties(const void *blob, int node)

    :param blob:
        *undescribed*
    :type blob: const void \*

    :param node:
        *undescribed*
    :type node: int

.. _`list_properties.description`:

Description
-----------

\ ``param``\  blob          FDT blob
\ ``param``\  node          Node to display
\ ``return``\  0 if ok, or FDT_ERR... if not.

.. _`list_subnodes`:

list_subnodes
=============

.. c:function:: int list_subnodes(const void *blob, int node)

    :param blob:
        *undescribed*
    :type blob: const void \*

    :param node:
        *undescribed*
    :type node: int

.. _`list_subnodes.description`:

Description
-----------

\ ``param``\  blob          FDT blob
\ ``param``\  node          Node to display
\ ``return``\  0 if ok, or FDT_ERR... if not.

.. _`show_data_for_item`:

show_data_for_item
==================

.. c:function:: int show_data_for_item(const void *blob, struct display_info *disp, int node, const char *property)

    display option provided.

    :param blob:
        *undescribed*
    :type blob: const void \*

    :param disp:
        *undescribed*
    :type disp: struct display_info \*

    :param node:
        *undescribed*
    :type node: int

    :param property:
        *undescribed*
    :type property: const char \*

.. _`show_data_for_item.description`:

Description
-----------

\ ``param``\  blob          FDT blob
\ ``param``\  disp          Display information / options
\ ``param``\  node          Node to display
\ ``param``\  property      Name of property to display, or NULL if none
\ ``return``\  0 if ok, -ve on error

.. _`do_fdtget`:

do_fdtget
=========

.. c:function:: int do_fdtget(struct display_info *disp, const char *filename, char **arg, int arg_count, int args_per_step)

    :param disp:
        *undescribed*
    :type disp: struct display_info \*

    :param filename:
        *undescribed*
    :type filename: const char \*

    :param arg:
        *undescribed*
    :type arg: char \*\*

    :param arg_count:
        *undescribed*
    :type arg_count: int

    :param args_per_step:
        *undescribed*
    :type args_per_step: int

.. _`do_fdtget.description`:

Description
-----------

\ ``param``\  disp          Display information / options
\ ``param``\  filename      Filename of blob file
\ ``param``\  arg           List of arguments to process
\ ``param``\  arg_count     Number of arguments
\ ``param``\  return 0 if ok, -ve on error

.. This file was automatic generated / don't edit.

