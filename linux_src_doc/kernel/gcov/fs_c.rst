.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/gcov/fs.c

.. _`gcov_node`:

struct gcov_node
================

.. c:type:: struct gcov_node

    represents a debugfs entry

.. _`gcov_node.definition`:

Definition
----------

.. code-block:: c

    struct gcov_node {
        struct list_head list;
        struct list_head children;
        struct list_head all;
        struct gcov_node *parent;
        struct gcov_info **loaded_info;
        struct gcov_info *unloaded_info;
        struct dentry *dentry;
        struct dentry **links;
        int num_loaded;
        char name;
    }

.. _`gcov_node.members`:

Members
-------

list
    list head for child node list

children
    child nodes

all
    list head for list of all nodes

parent
    parent node

loaded_info
    array of pointers to profiling data sets for loaded object
    files.

unloaded_info
    accumulated copy of profiling data sets for unloaded
    object files. Used only when gcov_persist=1.

dentry
    main debugfs entry, either a directory or data file

links
    associated symbolic links

num_loaded
    number of profiling data sets for loaded object files.

name
    data file basename

.. _`gcov_node.description`:

Description
-----------

struct gcov_node represents an entity within the gcov/ subdirectory
of debugfs. There are directory and data file nodes. The latter represent
the actual synthesized data file plus any associated symbolic links which
are needed by the gcov tool to work correctly.

.. This file was automatic generated / don't edit.

