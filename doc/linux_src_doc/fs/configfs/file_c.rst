.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/configfs/file.c

.. _`fill_read_buffer`:

fill_read_buffer
================

.. c:function:: int fill_read_buffer(struct dentry *dentry, struct configfs_buffer *buffer)

    allocate and fill buffer from item.

    :param struct dentry \*dentry:
        dentry pointer.

    :param struct configfs_buffer \*buffer:
        data buffer for file.

.. _`fill_read_buffer.description`:

Description
-----------

Allocate \ ``buffer``\ ->page, if it hasn't been already, then call the
config_item's \ :c:func:`show`\  method to fill the buffer with this attribute's
data.
This is called only once, on the file's first read.

.. _`configfs_read_file`:

configfs_read_file
==================

.. c:function:: ssize_t configfs_read_file(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    read an attribute.

    :param struct file \*file:
        file pointer.

    :param char __user \*buf:
        buffer to fill.

    :param size_t count:
        number of bytes to read.

    :param loff_t \*ppos:
        starting offset in file.

.. _`configfs_read_file.description`:

Description
-----------

Userspace wants to read an attribute file. The attribute descriptor
is in the file's ->d_fsdata. The target item is in the directory's
->d_fsdata.

We call \ :c:func:`fill_read_buffer`\  to allocate and fill the buffer from the
item's \ :c:func:`show`\  method exactly once (if the read is happening from
the beginning of the file). That should fill the entire buffer with
all the data the item has to offer for that attribute.
We then call \ :c:func:`flush_read_buffer`\  to copy the buffer to userspace
in the increments specified.

.. _`configfs_read_bin_file`:

configfs_read_bin_file
======================

.. c:function:: ssize_t configfs_read_bin_file(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    read a binary attribute.

    :param struct file \*file:
        file pointer.

    :param char __user \*buf:
        buffer to fill.

    :param size_t count:
        number of bytes to read.

    :param loff_t \*ppos:
        starting offset in file.

.. _`configfs_read_bin_file.description`:

Description
-----------

Userspace wants to read a binary attribute file. The attribute
descriptor is in the file's ->d_fsdata. The target item is in the
directory's ->d_fsdata.

We check whether we need to refill the buffer. If so we will
call the attributes' attr->\ :c:func:`read`\  twice. The first time we
will pass a NULL as a buffer pointer, which the attributes' method
will use to return the size of the buffer required. If no error
occurs we will allocate the buffer using vmalloc and call
attr->\ :c:func:`read`\  again passing that buffer as an argument.
Then we just copy to user-space using simple_read_from_buffer.

.. _`fill_write_buffer`:

fill_write_buffer
=================

.. c:function:: int fill_write_buffer(struct configfs_buffer *buffer, const char __user *buf, size_t count)

    copy buffer from userspace.

    :param struct configfs_buffer \*buffer:
        data buffer for file.

    :param const char __user \*buf:
        data from user.

    :param size_t count:
        number of bytes in \ ``userbuf``\ .

.. _`fill_write_buffer.description`:

Description
-----------

Allocate \ ``buffer``\ ->page if it hasn't been already, then
copy the user-supplied buffer into it.

.. _`flush_write_buffer`:

flush_write_buffer
==================

.. c:function:: int flush_write_buffer(struct dentry *dentry, struct configfs_buffer *buffer, size_t count)

    push buffer to config_item.

    :param struct dentry \*dentry:
        dentry to the attribute

    :param struct configfs_buffer \*buffer:
        data buffer for file.

    :param size_t count:
        number of bytes

.. _`flush_write_buffer.description`:

Description
-----------

Get the correct pointers for the config_item and the attribute we're
dealing with, then call the \ :c:func:`store`\  method for the attribute,
passing the buffer that we acquired in \ :c:func:`fill_write_buffer`\ .

.. _`configfs_write_file`:

configfs_write_file
===================

.. c:function:: ssize_t configfs_write_file(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    write an attribute.

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data to write

    :param size_t count:
        number of bytes

    :param loff_t \*ppos:
        starting offset

.. _`configfs_write_file.description`:

Description
-----------

Similar to \ :c:func:`configfs_read_file`\ , though working in the opposite direction.
We allocate and fill the data from the user in \ :c:func:`fill_write_buffer`\ ,
then push it to the config_item in \ :c:func:`flush_write_buffer`\ .
There is no easy way for us to know if userspace is only doing a partial
write, so we don't support them. We expect the entire buffer to come
on the first write.

.. _`configfs_write_file.hint`:

Hint
----

if you're writing a value, first read the file, modify only the
the value you're changing, then write entire buffer back.

.. _`configfs_write_bin_file`:

configfs_write_bin_file
=======================

.. c:function:: ssize_t configfs_write_bin_file(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    write a binary attribute.

    :param struct file \*file:
        file pointer

    :param const char __user \*buf:
        data to write

    :param size_t count:
        number of bytes

    :param loff_t \*ppos:
        starting offset

.. _`configfs_write_bin_file.description`:

Description
-----------

Writing to a binary attribute file is similar to a normal read.
We buffer the consecutive writes (binary attribute files do not
support lseek) in a continuously growing buffer, but we don't
commit until the close of the file.

.. _`configfs_create_file`:

configfs_create_file
====================

.. c:function:: int configfs_create_file(struct config_item *item, const struct configfs_attribute *attr)

    create an attribute file for an item.

    :param struct config_item \*item:
        item we're creating for.

    :param const struct configfs_attribute \*attr:
        atrribute descriptor.

.. _`configfs_create_bin_file`:

configfs_create_bin_file
========================

.. c:function:: int configfs_create_bin_file(struct config_item *item, const struct configfs_bin_attribute *bin_attr)

    create a binary attribute file for an item.

    :param struct config_item \*item:
        item we're creating for.

    :param const struct configfs_bin_attribute \*bin_attr:
        *undescribed*

.. This file was automatic generated / don't edit.

