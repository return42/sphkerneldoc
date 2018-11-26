.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/debugfs/file.c

.. _`debugfs_file_get`:

debugfs_file_get
================

.. c:function:: int debugfs_file_get(struct dentry *dentry)

    mark the beginning of file data access

    :param dentry:
        the dentry object whose data is being accessed.
    :type dentry: struct dentry \*

.. _`debugfs_file_get.description`:

Description
-----------

Up to a matching call to \ :c:func:`debugfs_file_put`\ , any successive call
into the file removing functions \ :c:func:`debugfs_remove`\  and
\ :c:func:`debugfs_remove_recursive`\  will block. Since associated private
file data may only get freed after a successful return of any of
the removal functions, you may safely access it after a successful
call to \ :c:func:`debugfs_file_get`\  without worrying about lifetime issues.

If -%EIO is returned, the file has already been removed and thus,
it is not safe to access any of its data. If, on the other hand,
it is allowed to access the file data, zero is returned.

.. _`debugfs_file_put`:

debugfs_file_put
================

.. c:function:: void debugfs_file_put(struct dentry *dentry)

    mark the end of file data access

    :param dentry:
        the dentry object formerly passed to
        \ :c:func:`debugfs_file_get`\ .
    :type dentry: struct dentry \*

.. _`debugfs_file_put.description`:

Description
-----------

Allow any ongoing concurrent call into \ :c:func:`debugfs_remove`\  or
\ :c:func:`debugfs_remove_recursive`\  blocked by a former call to
\ :c:func:`debugfs_file_get`\  to proceed and return to its caller.

.. _`debugfs_create_u8`:

debugfs_create_u8
=================

.. c:function:: struct dentry *debugfs_create_u8(const char *name, umode_t mode, struct dentry *parent, u8 *value)

    create a debugfs file that is used to read and write an unsigned 8-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u8 \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u16`:

debugfs_create_u16
==================

.. c:function:: struct dentry *debugfs_create_u16(const char *name, umode_t mode, struct dentry *parent, u16 *value)

    create a debugfs file that is used to read and write an unsigned 16-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u16 \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u32`:

debugfs_create_u32
==================

.. c:function:: struct dentry *debugfs_create_u32(const char *name, umode_t mode, struct dentry *parent, u32 *value)

    create a debugfs file that is used to read and write an unsigned 32-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u32 \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u64`:

debugfs_create_u64
==================

.. c:function:: struct dentry *debugfs_create_u64(const char *name, umode_t mode, struct dentry *parent, u64 *value)

    create a debugfs file that is used to read and write an unsigned 64-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u64 \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_ulong`:

debugfs_create_ulong
====================

.. c:function:: struct dentry *debugfs_create_ulong(const char *name, umode_t mode, struct dentry *parent, unsigned long *value)

    create a debugfs file that is used to read and write an unsigned long value.

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: unsigned long \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_x8`:

debugfs_create_x8
=================

.. c:function:: struct dentry *debugfs_create_x8(const char *name, umode_t mode, struct dentry *parent, u8 *value)

    create a debugfs file that is used to read and write an unsigned 8-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u8 \*

.. _`debugfs_create_x16`:

debugfs_create_x16
==================

.. c:function:: struct dentry *debugfs_create_x16(const char *name, umode_t mode, struct dentry *parent, u16 *value)

    create a debugfs file that is used to read and write an unsigned 16-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u16 \*

.. _`debugfs_create_x32`:

debugfs_create_x32
==================

.. c:function:: struct dentry *debugfs_create_x32(const char *name, umode_t mode, struct dentry *parent, u32 *value)

    create a debugfs file that is used to read and write an unsigned 32-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u32 \*

.. _`debugfs_create_x64`:

debugfs_create_x64
==================

.. c:function:: struct dentry *debugfs_create_x64(const char *name, umode_t mode, struct dentry *parent, u64 *value)

    create a debugfs file that is used to read and write an unsigned 64-bit value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: u64 \*

.. _`debugfs_create_size_t`:

debugfs_create_size_t
=====================

.. c:function:: struct dentry *debugfs_create_size_t(const char *name, umode_t mode, struct dentry *parent, size_t *value)

    create a debugfs file that is used to read and write an size_t value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: size_t \*

.. _`debugfs_create_atomic_t`:

debugfs_create_atomic_t
=======================

.. c:function:: struct dentry *debugfs_create_atomic_t(const char *name, umode_t mode, struct dentry *parent, atomic_t *value)

    create a debugfs file that is used to read and write an atomic_t value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: atomic_t \*

.. _`debugfs_create_bool`:

debugfs_create_bool
===================

.. c:function:: struct dentry *debugfs_create_bool(const char *name, umode_t mode, struct dentry *parent, bool *value)

    create a debugfs file that is used to read and write a boolean value

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param value:
        a pointer to the variable that the file should read to and write
        from.
    :type value: bool \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_blob`:

debugfs_create_blob
===================

.. c:function:: struct dentry *debugfs_create_blob(const char *name, umode_t mode, struct dentry *parent, struct debugfs_blob_wrapper *blob)

    create a debugfs file that is used to read a binary blob

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param blob:
        a pointer to a struct debugfs_blob_wrapper which contains a pointer
        to the blob data and the size of the data.
    :type blob: struct debugfs_blob_wrapper \*

.. _`debugfs_create_blob.description`:

Description
-----------

This function creates a file in debugfs with the given name that exports
\ ``blob->data``\  as a binary blob. If the \ ``mode``\  variable is so set it can be
read from. Writing is not supported.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_u32_array`:

debugfs_create_u32_array
========================

.. c:function:: struct dentry *debugfs_create_u32_array(const char *name, umode_t mode, struct dentry *parent, u32 *array, u32 elements)

    create a debugfs file that is used to read u32 array.

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have.
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param array:
        u32 array that provides data.
    :type array: u32 \*

    :param elements:
        total number of elements in the array.
    :type elements: u32

.. _`debugfs_create_u32_array.description`:

Description
-----------

This function creates a file in debugfs with the given name that exports
\ ``array``\  as data. If the \ ``mode``\  variable is so set it can be read from.
Writing is not supported. Seek within the file is also not supported.
Once array is created its size can not be changed.

The function returns a pointer to dentry on success. If debugfs is not
enabled in the kernel, the value -%ENODEV will be returned.

.. _`debugfs_print_regs32`:

debugfs_print_regs32
====================

.. c:function:: void debugfs_print_regs32(struct seq_file *s, const struct debugfs_reg32 *regs, int nregs, void __iomem *base, char *prefix)

    use seq_print to describe a set of registers

    :param s:
        the seq_file structure being used to generate output
    :type s: struct seq_file \*

    :param regs:
        an array if struct debugfs_reg32 structures
    :type regs: const struct debugfs_reg32 \*

    :param nregs:
        the length of the above array
    :type nregs: int

    :param base:
        the base address to be used in reading the registers
    :type base: void __iomem \*

    :param prefix:
        a string to be prefixed to every output line
    :type prefix: char \*

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

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param regset:
        a pointer to a struct debugfs_regset32, which contains a pointer
        to an array of register definitions, the array size and the base
        address where the register bank is to be found.
    :type regset: struct debugfs_regset32 \*

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

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.  It is not wise to check for this value, but rather, check for
\ ``NULL``\  or !%NULL instead as to eliminate the need for #ifdef in the calling
code.

.. _`debugfs_create_devm_seqfile`:

debugfs_create_devm_seqfile
===========================

.. c:function:: struct dentry *debugfs_create_devm_seqfile(struct device *dev, const char *name, struct dentry *parent, int (*read_fn)(struct seq_file *s, void *data))

    create a debugfs file that is bound to device.

    :param dev:
        device related to this debugfs file.
    :type dev: struct device \*

    :param name:
        name of the debugfs file.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param int (\*read_fn)(struct seq_file \*s, void \*data):
        function pointer called to print the seq_file content.

.. This file was automatic generated / don't edit.

