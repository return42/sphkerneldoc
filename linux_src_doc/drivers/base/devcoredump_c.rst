.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/devcoredump.c

.. _`dev_coredumpv`:

dev_coredumpv
=============

.. c:function:: void dev_coredumpv(struct device *dev, void *data, size_t datalen, gfp_t gfp)

    create device coredump with vmalloc data

    :param dev:
        the struct device for the crashed device
    :type dev: struct device \*

    :param data:
        vmalloc data containing the device coredump
    :type data: void \*

    :param datalen:
        length of the data
    :type datalen: size_t

    :param gfp:
        allocation flags
    :type gfp: gfp_t

.. _`dev_coredumpv.description`:

Description
-----------

This function takes ownership of the vmalloc'ed data and will free
it when it is no longer used. See \ :c:func:`dev_coredumpm`\  for more information.

.. _`devcd_free_sgtable`:

devcd_free_sgtable
==================

.. c:function:: void devcd_free_sgtable(void *data)

    free all the memory of the given scatterlist table (i.e. both pages and scatterlist instances)

    :param data:
        *undescribed*
    :type data: void \*

.. _`devcd_free_sgtable.note`:

NOTE
----

if two tables allocated with devcd_alloc_sgtable and then chained
using the sg_chain function then that function should be called only once
on the chained table

.. _`devcd_read_from_sgtable`:

devcd_read_from_sgtable
=======================

.. c:function:: ssize_t devcd_read_from_sgtable(char *buffer, loff_t offset, size_t buf_len, void *data, size_t data_len)

    copy data from sg_table to a given buffer and return the number of bytes read

    :param buffer:
        the buffer to copy the data to it
    :type buffer: char \*

    :param offset:
        start copy from \ ``offset``\ @ bytes from the head of the data
        in the given scatterlist
    :type offset: loff_t

    :param buf_len:
        the length of the buffer
    :type buf_len: size_t

    :param data:
        the scatterlist table to copy from
    :type data: void \*

    :param data_len:
        the length of the data in the sg_table
    :type data_len: size_t

.. _`dev_coredumpm`:

dev_coredumpm
=============

.. c:function:: void dev_coredumpm(struct device *dev, struct module *owner, void *data, size_t datalen, gfp_t gfp, ssize_t (*read)(char *buffer, loff_t offset, size_t count, void *data, size_t datalen), void (*free)(void *data))

    create device coredump with read/free methods

    :param dev:
        the struct device for the crashed device
    :type dev: struct device \*

    :param owner:
        the module that contains the read/free functions, use \ ``THIS_MODULE``\ 
    :type owner: struct module \*

    :param data:
        data cookie for the \ ``read``\ /@free functions
    :type data: void \*

    :param datalen:
        length of the data
    :type datalen: size_t

    :param gfp:
        allocation flags
    :type gfp: gfp_t

    :param ssize_t (\*read)(char \*buffer, loff_t offset, size_t count, void \*data, size_t datalen):
        function to read from the given buffer

    :param void (\*free)(void \*data):
        function to free the given buffer

.. _`dev_coredumpm.description`:

Description
-----------

Creates a new device coredump for the given device. If a previous one hasn't
been read yet, the new coredump is discarded. The data lifetime is determined
by the device coredump framework and when it is no longer needed the \ ``free``\ 
function will be called to free the data.

.. _`dev_coredumpsg`:

dev_coredumpsg
==============

.. c:function:: void dev_coredumpsg(struct device *dev, struct scatterlist *table, size_t datalen, gfp_t gfp)

    create device coredump that uses scatterlist as data parameter

    :param dev:
        the struct device for the crashed device
    :type dev: struct device \*

    :param table:
        the dump data
    :type table: struct scatterlist \*

    :param datalen:
        length of the data
    :type datalen: size_t

    :param gfp:
        allocation flags
    :type gfp: gfp_t

.. _`dev_coredumpsg.description`:

Description
-----------

Creates a new device coredump for the given device. If a previous one hasn't
been read yet, the new coredump is discarded. The data lifetime is determined
by the device coredump framework and when it is no longer needed
it will free the data.

.. This file was automatic generated / don't edit.

