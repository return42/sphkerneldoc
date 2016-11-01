.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/fdtget.c

.. _`show_data`:

show_data
=========

.. c:function:: int show_data(struct display_info *disp, const char *data, int len)

    :param struct display_info \*disp:
        *undescribed*

    :param const char \*data:
        *undescribed*

    :param int len:
        *undescribed*

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

    :param const void \*blob:
        *undescribed*

    :param int node:
        *undescribed*

.. _`list_properties.description`:

Description
-----------

@param blob          FDT blob
\ ``param``\  node          Node to display
\ ``return``\  0 if ok, or FDT_ERR... if not.

.. _`list_subnodes`:

list_subnodes
=============

.. c:function:: int list_subnodes(const void *blob, int node)

    :param const void \*blob:
        *undescribed*

    :param int node:
        *undescribed*

.. _`list_subnodes.description`:

Description
-----------

@param blob          FDT blob
\ ``param``\  node          Node to display
\ ``return``\  0 if ok, or FDT_ERR... if not.

.. _`show_data_for_item`:

show_data_for_item
==================

.. c:function:: int show_data_for_item(const void *blob, struct display_info *disp, int node, const char *property)

    display option provided.

    :param const void \*blob:
        *undescribed*

    :param struct display_info \*disp:
        *undescribed*

    :param int node:
        *undescribed*

    :param const char \*property:
        *undescribed*

.. _`show_data_for_item.description`:

Description
-----------

@param blob          FDT blob
\ ``param``\  disp          Display information / options
\ ``param``\  node          Node to display
\ ``param``\  property      Name of property to display, or NULL if none
\ ``return``\  0 if ok, -ve on error

.. _`do_fdtget`:

do_fdtget
=========

.. c:function:: int do_fdtget(struct display_info *disp, const char *filename, char **arg, int arg_count, int args_per_step)

    :param struct display_info \*disp:
        *undescribed*

    :param const char \*filename:
        *undescribed*

    :param char \*\*arg:
        *undescribed*

    :param int arg_count:
        *undescribed*

    :param int args_per_step:
        *undescribed*

.. _`do_fdtget.description`:

Description
-----------

@param disp          Display information / options
\ ``param``\  filename      Filename of blob file
\ ``param``\  arg           List of arguments to process
\ ``param``\  arg_count     Number of arguments
\ ``param``\  return 0 if ok, -ve on error

.. This file was automatic generated / don't edit.

