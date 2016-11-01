.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/fdtput.c

.. _`report_error`:

report_error
============

.. c:function:: void report_error(const char *name, int namelen, int err)

    :param const char \*name:
        *undescribed*

    :param int namelen:
        *undescribed*

    :param int err:
        *undescribed*

.. _`report_error.description`:

Description
-----------

@param name          Node name to report error on
\ ``param``\  namelen       Length of node name, or -1 to use entire string
\ ``param``\  err           Error number to report (-FDT_ERR_...)

.. _`encode_value`:

encode_value
============

.. c:function:: int encode_value(struct display_info *disp, char **arg, int arg_count, char **valuep, int *value_len)

    :param struct display_info \*disp:
        *undescribed*

    :param char \*\*arg:
        *undescribed*

    :param int arg_count:
        *undescribed*

    :param char \*\*valuep:
        *undescribed*

    :param int \*value_len:
        *undescribed*

.. _`encode_value.description`:

Description
-----------

@param disp          Display information / options
\ ``param``\  arg           List of arguments from command line
\ ``param``\  arg_count     Number of arguments (may be 0)
\ ``param``\  valuep        Returns buffer containing value
\ ``param``\  \*value_len    Returns length of value encoded

.. _`create_paths`:

create_paths
============

.. c:function:: int create_paths(void *blob, const char *in_path)

    :param void \*blob:
        *undescribed*

    :param const char \*in_path:
        *undescribed*

.. _`create_paths.description`:

Description
-----------

Any components of the path that do not exist are created. Errors are
reported.

\ ``param``\  blob          FDT blob to write into
\ ``param``\  in_path       Path to process
\ ``return``\  0 if ok, -1 on error

.. _`create_node`:

create_node
===========

.. c:function:: int create_node(void *blob, const char *node_name)

    :param void \*blob:
        *undescribed*

    :param const char \*node_name:
        *undescribed*

.. _`create_node.description`:

Description
-----------

This will overwrite the node_name string. Any error is reported.

.. _`create_node.todo`:

TODO
----

Perhaps create \ :c:func:`fdt_path_offset_namelen`\  so we don't need to do this.

\ ``param``\  blob          FDT blob to write into
\ ``param``\  node_name     Name of node to create
\ ``return``\  new node offset if found, or -1 on failure

.. This file was automatic generated / don't edit.

