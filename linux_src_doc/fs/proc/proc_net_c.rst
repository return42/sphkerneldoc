.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/proc/proc_net.c

.. _`proc_create_net_data_write`:

proc_create_net_data_write
==========================

.. c:function:: struct proc_dir_entry *proc_create_net_data_write(const char *name, umode_t mode, struct proc_dir_entry *parent, const struct seq_operations *ops, proc_write_t write, unsigned int state_size, void *data)

    Create a writable net_ns-specific proc file

    :param name:
        The name of the file.
    :type name: const char \*

    :param mode:
        The file's access mode.
    :type mode: umode_t

    :param parent:
        The parent directory in which to create.
    :type parent: struct proc_dir_entry \*

    :param ops:
        The seq_file ops with which to read the file.
    :type ops: const struct seq_operations \*

    :param write:
        The write method which which to 'modify' the file.
    :type write: proc_write_t

    :param state_size:
        *undescribed*
    :type state_size: unsigned int

    :param data:
        Data for retrieval by \ :c:func:`PDE_DATA`\ .
    :type data: void \*

.. _`proc_create_net_data_write.description`:

Description
-----------

Create a network namespaced proc file in the \ ``parent``\  directory with the
specified \ ``name``\  and \ ``mode``\  that allows reading of a file that displays a
series of elements and also provides for the file accepting writes that have
some arbitrary effect.

The functions in the \ ``ops``\  table are used to iterate over items to be
presented and extract the readable content using the seq_file interface.

The \ ``write``\  function is called with the data copied into a kernel space
scratch buffer and has a NUL appended for convenience.  The buffer may be
modified by the \ ``write``\  function.  \ ``write``\  should return 0 on success.

The \ ``data``\  value is accessible from the \ ``show``\  and \ ``write``\  functions by calling
\ :c:func:`PDE_DATA`\  on the file inode.  The network namespace must be accessed by
calling \ :c:func:`seq_file_net`\  on the seq_file struct.

.. _`proc_create_net_single_write`:

proc_create_net_single_write
============================

.. c:function:: struct proc_dir_entry *proc_create_net_single_write(const char *name, umode_t mode, struct proc_dir_entry *parent, int (*show)(struct seq_file *, void *), proc_write_t write, void *data)

    Create a writable net_ns-specific proc file

    :param name:
        The name of the file.
    :type name: const char \*

    :param mode:
        The file's access mode.
    :type mode: umode_t

    :param parent:
        The parent directory in which to create.
    :type parent: struct proc_dir_entry \*

    :param int (\*show)(struct seq_file \*, void \*):
        The seqfile show method with which to read the file.

    :param write:
        The write method which which to 'modify' the file.
    :type write: proc_write_t

    :param data:
        Data for retrieval by \ :c:func:`PDE_DATA`\ .
    :type data: void \*

.. _`proc_create_net_single_write.description`:

Description
-----------

Create a network-namespaced proc file in the \ ``parent``\  directory with the
specified \ ``name``\  and \ ``mode``\  that allows reading of a file that displays a
single element rather than a series and also provides for the file accepting
writes that have some arbitrary effect.

The \ ``show``\  function is called to extract the readable content via the
seq_file interface.

The \ ``write``\  function is called with the data copied into a kernel space
scratch buffer and has a NUL appended for convenience.  The buffer may be
modified by the \ ``write``\  function.  \ ``write``\  should return 0 on success.

The \ ``data``\  value is accessible from the \ ``show``\  and \ ``write``\  functions by calling
\ :c:func:`PDE_DATA`\  on the file inode.  The network namespace must be accessed by
calling \ :c:func:`seq_file_single_net`\  on the seq_file struct.

.. This file was automatic generated / don't edit.

