.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/proc/proc_sysctl.c

.. _`get_subdir`:

get_subdir
==========

.. c:function:: struct ctl_dir *get_subdir(struct ctl_dir *dir, const char *name, int namelen)

    find or create a subdir with the specified name.

    :param dir:
        Directory to create the subdirectory in
    :type dir: struct ctl_dir \*

    :param name:
        The name of the subdirectory to find or create
    :type name: const char \*

    :param namelen:
        The length of name
    :type namelen: int

.. _`get_subdir.description`:

Description
-----------

Takes a directory with an elevated reference count so we know that
if we drop the lock the directory will not go away.  Upon success
the reference is moved from \ ``dir``\  to the returned subdirectory.
Upon error an error code is returned and the reference on \ ``dir``\  is
simply dropped.

.. _`__register_sysctl_table`:

\__register_sysctl_table
========================

.. c:function:: struct ctl_table_header *__register_sysctl_table(struct ctl_table_set *set, const char *path, struct ctl_table *table)

    register a leaf sysctl table

    :param set:
        Sysctl tree to register on
    :type set: struct ctl_table_set \*

    :param path:
        The path to the directory the sysctl table is in.
    :type path: const char \*

    :param table:
        the top-level table structure
    :type table: struct ctl_table \*

.. _`__register_sysctl_table.description`:

Description
-----------

Register a sysctl table hierarchy. \ ``table``\  should be a filled in ctl_table
array. A completely 0 filled entry terminates the table.

The members of the \ :c:type:`struct ctl_table <ctl_table>`\  structure are used as follows:

procname - the name of the sysctl file under /proc/sys. Set to \ ``NULL``\  to not
enter a sysctl file

data - a pointer to data for use by proc_handler

maxlen - the maximum size in bytes of the data

mode - the file permissions for the /proc/sys file

child - must be \ ``NULL``\ .

proc_handler - the text handler routine (described below)

extra1, extra2 - extra pointers usable by the proc handler routines

Leaf nodes in the sysctl tree will be represented by a single file
under /proc; non-leaf nodes will be represented by directories.

There must be a proc_handler routine for any terminal nodes.
Several default handlers are available to cover common cases -

\ :c:func:`proc_dostring`\ , \ :c:func:`proc_dointvec`\ , \ :c:func:`proc_dointvec_jiffies`\ ,
\ :c:func:`proc_dointvec_userhz_jiffies`\ , \ :c:func:`proc_dointvec_minmax`\ ,
\ :c:func:`proc_doulongvec_ms_jiffies_minmax`\ , \ :c:func:`proc_doulongvec_minmax`\ 

It is the handler's job to read the input buffer from user memory
and process it. The handler should return 0 on success.

This routine returns \ ``NULL``\  on a failure to register, and a pointer
to the table header on success.

.. _`register_sysctl`:

register_sysctl
===============

.. c:function:: struct ctl_table_header *register_sysctl(const char *path, struct ctl_table *table)

    register a sysctl table

    :param path:
        The path to the directory the sysctl table is in.
    :type path: const char \*

    :param table:
        the table structure
    :type table: struct ctl_table \*

.. _`register_sysctl.description`:

Description
-----------

Register a sysctl table. \ ``table``\  should be a filled in ctl_table
array. A completely 0 filled entry terminates the table.

See \__register_sysctl_table for more details.

.. _`__register_sysctl_paths`:

\__register_sysctl_paths
========================

.. c:function:: struct ctl_table_header *__register_sysctl_paths(struct ctl_table_set *set, const struct ctl_path *path, struct ctl_table *table)

    register a sysctl table hierarchy

    :param set:
        Sysctl tree to register on
    :type set: struct ctl_table_set \*

    :param path:
        The path to the directory the sysctl table is in.
    :type path: const struct ctl_path \*

    :param table:
        the top-level table structure
    :type table: struct ctl_table \*

.. _`__register_sysctl_paths.description`:

Description
-----------

Register a sysctl table hierarchy. \ ``table``\  should be a filled in ctl_table
array. A completely 0 filled entry terminates the table.

See \__register_sysctl_table for more details.

.. _`register_sysctl_paths`:

register_sysctl_paths
=====================

.. c:function:: struct ctl_table_header *register_sysctl_paths(const struct ctl_path *path, struct ctl_table *table)

    register a sysctl table hierarchy

    :param path:
        The path to the directory the sysctl table is in.
    :type path: const struct ctl_path \*

    :param table:
        the top-level table structure
    :type table: struct ctl_table \*

.. _`register_sysctl_paths.description`:

Description
-----------

Register a sysctl table hierarchy. \ ``table``\  should be a filled in ctl_table
array. A completely 0 filled entry terminates the table.

See \__register_sysctl_paths for more details.

.. _`register_sysctl_table`:

register_sysctl_table
=====================

.. c:function:: struct ctl_table_header *register_sysctl_table(struct ctl_table *table)

    register a sysctl table hierarchy

    :param table:
        the top-level table structure
    :type table: struct ctl_table \*

.. _`register_sysctl_table.description`:

Description
-----------

Register a sysctl table hierarchy. \ ``table``\  should be a filled in ctl_table
array. A completely 0 filled entry terminates the table.

See register_sysctl_paths for more details.

.. _`unregister_sysctl_table`:

unregister_sysctl_table
=======================

.. c:function:: void unregister_sysctl_table(struct ctl_table_header *header)

    unregister a sysctl table hierarchy

    :param header:
        the header returned from register_sysctl_table
    :type header: struct ctl_table_header \*

.. _`unregister_sysctl_table.description`:

Description
-----------

Unregisters the sysctl table and all children. proc entries may not
actually be removed until they are no longer used by anyone.

.. This file was automatic generated / don't edit.

