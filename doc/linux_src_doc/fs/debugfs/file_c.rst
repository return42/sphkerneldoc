.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/debugfs/file.c

.. _`debugfs_use_file_start`:

debugfs_use_file_start
======================

.. c:function:: int debugfs_use_file_start(const struct dentry *dentry, int *srcu_idx)

    mark the beginning of file data access

    :param const struct dentry \*dentry:
        the dentry object whose data is being accessed.

    :param int \*srcu_idx:
        a pointer to some memory to store a SRCU index in.

.. _`debugfs_use_file_start.description`:

Description
-----------

Up to a matching call to \ :c:func:`debugfs_use_file_finish`\ , any
successive call into the file removing functions \ :c:func:`debugfs_remove`\ 
and \ :c:func:`debugfs_remove_recursive`\  will block. Since associated private
file data may only get freed after a successful return of any of
the removal functions, you may safely access it after a successful
call to \ :c:func:`debugfs_use_file_start`\  without worrying about
lifetime issues.

If -\ ``EIO``\  is returned, the file has already been removed and thus,
it is not safe to access any of its data. If, on the other hand,
it is allowed to access the file data, zero is returned.

Regardless of the return code, any call to
\ :c:func:`debugfs_use_file_start`\  must be followed by a matching call
to \ :c:func:`debugfs_use_file_finish`\ .

.. _`debugfs_use_file_finish`:

debugfs_use_file_finish
=======================

.. c:function:: void debugfs_use_file_finish(int srcu_idx)

    mark the end of file data access

    :param int srcu_idx:
        the SRCU index "created" by a former call to
        \ :c:func:`debugfs_use_file_start`\ .

.. _`debugfs_use_file_finish.description`:

Description
-----------

Allow any ongoing concurrent call into \ :c:func:`debugfs_remove`\  or
\ :c:func:`debugfs_remove_recursive`\  blocked by a former call to
\ :c:func:`debugfs_use_file_start`\  to proceed and return to its caller.

.. _`debugfs_create_u8`:

debugfs_create_u8
=================

.. c:function:: struct dentry *debugfs_create_u8(const char *name, umode_t mode, struct dentry *parent, u8 *value)

    create a debugfs file that is used to read and write an unsigned 8-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u8 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_u8.description`:

Description
-----------

This function creates a file in debugfs with the given name that
contains the value of the variable \ ``value``\ .  If the \ ``mode``\  variable is so
set, it can be read from, and written to.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u16`:

debugfs_create_u16
==================

.. c:function:: struct dentry *debugfs_create_u16(const char *name, umode_t mode, struct dentry *parent, u16 *value)

    create a debugfs file that is used to read and write an unsigned 16-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u16 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_u16.description`:

Description
-----------

This function creates a file in debugfs with the given name that
contains the value of the variable \ ``value``\ .  If the \ ``mode``\  variable is so
set, it can be read from, and written to.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u32`:

debugfs_create_u32
==================

.. c:function:: struct dentry *debugfs_create_u32(const char *name, umode_t mode, struct dentry *parent, u32 *value)

    create a debugfs file that is used to read and write an unsigned 32-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u32 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_u32.description`:

Description
-----------

This function creates a file in debugfs with the given name that
contains the value of the variable \ ``value``\ .  If the \ ``mode``\  variable is so
set, it can be read from, and written to.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u64`:

debugfs_create_u64
==================

.. c:function:: struct dentry *debugfs_create_u64(const char *name, umode_t mode, struct dentry *parent, u64 *value)

    create a debugfs file that is used to read and write an unsigned 64-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u64 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_u64.description`:

Description
-----------

This function creates a file in debugfs with the given name that
contains the value of the variable \ ``value``\ .  If the \ ``mode``\  variable is so
set, it can be read from, and written to.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_ulong`:

debugfs_create_ulong
====================

.. c:function:: struct dentry *debugfs_create_ulong(const char *name, umode_t mode, struct dentry *parent, unsigned long *value)

    create a debugfs file that is used to read and write an unsigned long value.

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param unsigned long \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_ulong.description`:

Description
-----------

This function creates a file in debugfs with the given name that
contains the value of the variable \ ``value``\ .  If the \ ``mode``\  variable is so
set, it can be read from, and written to.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_x8`:

debugfs_create_x8
=================

.. c:function:: struct dentry *debugfs_create_x8(const char *name, umode_t mode, struct dentry *parent, u8 *value)

    create a debugfs file that is used to read and write an unsigned 8-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u8 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_x16`:

debugfs_create_x16
==================

.. c:function:: struct dentry *debugfs_create_x16(const char *name, umode_t mode, struct dentry *parent, u16 *value)

    create a debugfs file that is used to read and write an unsigned 16-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u16 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_x32`:

debugfs_create_x32
==================

.. c:function:: struct dentry *debugfs_create_x32(const char *name, umode_t mode, struct dentry *parent, u32 *value)

    create a debugfs file that is used to read and write an unsigned 32-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u32 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_x64`:

debugfs_create_x64
==================

.. c:function:: struct dentry *debugfs_create_x64(const char *name, umode_t mode, struct dentry *parent, u64 *value)

    create a debugfs file that is used to read and write an unsigned 64-bit value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u64 \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_size_t`:

debugfs_create_size_t
=====================

.. c:function:: struct dentry *debugfs_create_size_t(const char *name, umode_t mode, struct dentry *parent, size_t *value)

    create a debugfs file that is used to read and write an size_t value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param size_t \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_atomic_t`:

debugfs_create_atomic_t
=======================

.. c:function:: struct dentry *debugfs_create_atomic_t(const char *name, umode_t mode, struct dentry *parent, atomic_t *value)

    create a debugfs file that is used to read and write an atomic_t value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param atomic_t \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_bool`:

debugfs_create_bool
===================

.. c:function:: struct dentry *debugfs_create_bool(const char *name, umode_t mode, struct dentry *parent, bool *value)

    create a debugfs file that is used to read and write a boolean value

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param bool \*value:
        a pointer to the variable that the file should read to and write
        from.

.. _`debugfs_create_bool.description`:

Description
-----------

This function creates a file in debugfs with the given name that
contains the value of the variable \ ``value``\ .  If the \ ``mode``\  variable is so
set, it can be read from, and written to.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_blob`:

debugfs_create_blob
===================

.. c:function:: struct dentry *debugfs_create_blob(const char *name, umode_t mode, struct dentry *parent, struct debugfs_blob_wrapper *blob)

    create a debugfs file that is used to read a binary blob

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param struct debugfs_blob_wrapper \*blob:
        a pointer to a struct debugfs_blob_wrapper which contains a pointer
        to the blob data and the size of the data.

.. _`debugfs_create_blob.description`:

Description
-----------

This function creates a file in debugfs with the given name that exports
\ ``blob``\ ->data as a binary blob. If the \ ``mode``\  variable is so set it can be
read from. Writing is not supported.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u32_array`:

debugfs_create_u32_array
========================

.. c:function:: struct dentry *debugfs_create_u32_array(const char *name, umode_t mode, struct dentry *parent, u32 *array, u32 elements)

    create a debugfs file that is used to read u32 array.

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have.

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param u32 \*array:
        u32 array that provides data.

    :param u32 elements:
        total number of elements in the array.

.. _`debugfs_create_u32_array.description`:

Description
-----------

This function creates a file in debugfs with the given name that exports
\ ``array``\  as data. If the \ ``mode``\  variable is so set it can be read from.
Writing is not supported. Seek within the file is also not supported.
Once array is created its size can not be changed.

The function returns a pointer to dentry on success. If debugfs is not
enabled in the kernel, the value -\ ``ENODEV``\  will be returned.

.. _`debugfs_print_regs32`:

debugfs_print_regs32
====================

.. c:function:: void debugfs_print_regs32(struct seq_file *s, const struct debugfs_reg32 *regs, int nregs, void __iomem *base, char *prefix)

    use seq_print to describe a set of registers

    :param struct seq_file \*s:
        the seq_file structure being used to generate output

    :param const struct debugfs_reg32 \*regs:
        an array if struct debugfs_reg32 structures

    :param int nregs:
        the length of the above array

    :param void __iomem \*base:
        the base address to be used in reading the registers

    :param char \*prefix:
        a string to be prefixed to every output line

.. _`debugfs_print_regs32.description`:

Description
-----------

This function outputs a text block describing the current values of
some 32-bit hardware registers. It is meant to be used within debugfs
files based on seq_file that need to show registers, intermixed with other
information. The prefix argument may be used to specify a leading string,
because some peripherals have several blocks of identical registers,
for example configuration of dma channels

.. _`debugfs_create_regset32`:

debugfs_create_regset32
=======================

.. c:function:: struct dentry *debugfs_create_regset32(const char *name, umode_t mode, struct dentry *parent, struct debugfs_regset32 *regset)

    create a debugfs file that returns register values

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param struct debugfs_regset32 \*regset:
        a pointer to a struct debugfs_regset32, which contains a pointer
        to an array of register definitions, the array size and the base
        address where the register bank is to be found.

.. _`debugfs_create_regset32.description`:

Description
-----------

This function creates a file in debugfs with the given name that reports
the names and values of a set of 32-bit registers. If the \ ``mode``\  variable
is so set it can be read from. Writing is not supported.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -\ ``ENODEV``\  will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !\ ``NULL``\  instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_devm_seqfile`:

debugfs_create_devm_seqfile
===========================

.. c:function:: struct dentry *debugfs_create_devm_seqfile(struct device *dev, const char *name, struct dentry *parent, int (*read_fn)(struct seq_file *s, void *data))

    create a debugfs file that is bound to device.

    :param struct device \*dev:
        device related to this debugfs file.

    :param const char \*name:
        name of the debugfs file.

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.

    :param int (\*read_fn)(struct seq_file \*s, void \*data):
        function pointer called to print the seq_file content.

.. This file was automatic generated / don't edit.

