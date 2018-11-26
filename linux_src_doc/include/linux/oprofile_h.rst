.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/oprofile.h

.. _`oprofile_arch_init`:

oprofile_arch_init
==================

.. c:function:: int oprofile_arch_init(struct oprofile_operations *ops)

    time initialisation. \*ops must be set to a filled-in operations structure. This is called even in timer interrupt mode so an arch can set a backtrace callback.

    :param ops:
        *undescribed*
    :type ops: struct oprofile_operations \*

.. _`oprofile_arch_init.description`:

Description
-----------

If an error occurs, the fields should be left untouched.

.. _`oprofile_arch_exit`:

oprofile_arch_exit
==================

.. c:function:: void oprofile_arch_exit( void)

    time exit/cleanup for the arch.

    :param void:
        no arguments
    :type void: 

.. _`oprofile_add_sample`:

oprofile_add_sample
===================

.. c:function:: void oprofile_add_sample(struct pt_regs * const regs, unsigned long event)

    :param regs:
        *undescribed*
    :type regs: struct pt_regs \* const

    :param event:
        *undescribed*
    :type event: unsigned long

.. _`oprofile_add_ext_sample`:

oprofile_add_ext_sample
=======================

.. c:function:: void oprofile_add_ext_sample(unsigned long pc, struct pt_regs * const regs, unsigned long event, int is_kernel)

    we cannot determine if we're in kernel mode from the regs.

    :param pc:
        *undescribed*
    :type pc: unsigned long

    :param regs:
        *undescribed*
    :type regs: struct pt_regs \* const

    :param event:
        *undescribed*
    :type event: unsigned long

    :param is_kernel:
        *undescribed*
    :type is_kernel: int

.. _`oprofile_add_ext_sample.description`:

Description
-----------

This function does perform a backtrace.

.. _`oprofile_add_ext_hw_sample`:

oprofile_add_ext_hw_sample
==========================

.. c:function:: void oprofile_add_ext_hw_sample(unsigned long pc, struct pt_regs * const regs, unsigned long event, int is_kernel, struct task_struct *task)

    :param pc:
        *undescribed*
    :type pc: unsigned long

    :param regs:
        *undescribed*
    :type regs: struct pt_regs \* const

    :param event:
        *undescribed*
    :type event: unsigned long

    :param is_kernel:
        *undescribed*
    :type is_kernel: int

    :param task:
        *undescribed*
    :type task: struct task_struct \*

.. _`oprofilefs_create_file`:

oprofilefs_create_file
======================

.. c:function:: int oprofilefs_create_file(struct dentry *root, char const *name, const struct file_operations *fops)

    the specified file operations.

    :param root:
        *undescribed*
    :type root: struct dentry \*

    :param name:
        *undescribed*
    :type name: char const \*

    :param fops:
        *undescribed*
    :type fops: const struct file_operations \*

.. _`oprofilefs_str_to_user`:

oprofilefs_str_to_user
======================

.. c:function:: ssize_t oprofilefs_str_to_user(char const *str, char __user *buf, size_t count, loff_t *offset)

    appropriately. Returns bytes written or -EFAULT.

    :param str:
        *undescribed*
    :type str: char const \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param offset:
        *undescribed*
    :type offset: loff_t \*

.. _`oprofilefs_ulong_to_user`:

oprofilefs_ulong_to_user
========================

.. c:function:: ssize_t oprofilefs_ulong_to_user(unsigned long val, char __user *buf, size_t count, loff_t *offset)

    updating \*offset appropriately. Returns bytes written or -EFAULT.

    :param val:
        *undescribed*
    :type val: unsigned long

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param offset:
        *undescribed*
    :type offset: loff_t \*

.. _`oprofilefs_ulong_from_user`:

oprofilefs_ulong_from_user
==========================

.. c:function:: int oprofilefs_ulong_from_user(unsigned long *val, char const __user *buf, size_t count)

    Returns 0 on success, < 0 on error.

    :param val:
        *undescribed*
    :type val: unsigned long \*

    :param buf:
        *undescribed*
    :type buf: char const __user \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`oprofile_put_buff`:

oprofile_put_buff
=================

.. c:function:: void oprofile_put_buff(unsigned long *buf, unsigned int start, unsigned int stop, unsigned int max)

    :param buf:
        *undescribed*
    :type buf: unsigned long \*

    :param start:
        *undescribed*
    :type start: unsigned int

    :param stop:
        *undescribed*
    :type stop: unsigned int

    :param max:
        *undescribed*
    :type max: unsigned int

.. This file was automatic generated / don't edit.

