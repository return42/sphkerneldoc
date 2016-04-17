.. -*- coding: utf-8; mode: rst -*-

==========
oprofile.h
==========


.. _`oprofile_arch_init`:

oprofile_arch_init
==================

.. c:function:: int oprofile_arch_init (struct oprofile_operations *ops)

    time initialisation. \*ops must be set to a filled-in operations structure. This is called even in timer interrupt mode so an arch can set a backtrace callback.

    :param struct oprofile_operations \*ops:

        *undescribed*



.. _`oprofile_arch_init.description`:

Description
-----------


If an error occurs, the fields should be left untouched.



.. _`oprofile_arch_exit`:

oprofile_arch_exit
==================

.. c:function:: void oprofile_arch_exit ( void)

    time exit/cleanup for the arch.

    :param void:
        no arguments



.. _`oprofile_add_sample`:

oprofile_add_sample
===================

.. c:function:: void oprofile_add_sample (struct pt_regs *const regs, unsigned long event)

    :param struct pt_regs \*const regs:

        *undescribed*

    :param unsigned long event:

        *undescribed*



.. _`oprofile_add_ext_sample`:

oprofile_add_ext_sample
=======================

.. c:function:: void oprofile_add_ext_sample (unsigned long pc, struct pt_regs *const regs, unsigned long event, int is_kernel)

     we cannot determine if we're in kernel mode from the regs.

    :param unsigned long pc:

        *undescribed*

    :param struct pt_regs \*const regs:

        *undescribed*

    :param unsigned long event:

        *undescribed*

    :param int is_kernel:

        *undescribed*



.. _`oprofile_add_ext_sample.description`:

Description
-----------


This function does perform a backtrace.



.. _`oprofile_add_ext_hw_sample`:

oprofile_add_ext_hw_sample
==========================

.. c:function:: void oprofile_add_ext_hw_sample (unsigned long pc, struct pt_regs *const regs, unsigned long event, int is_kernel, struct task_struct *task)

    :param unsigned long pc:

        *undescribed*

    :param struct pt_regs \*const regs:

        *undescribed*

    :param unsigned long event:

        *undescribed*

    :param int is_kernel:

        *undescribed*

    :param struct task_struct \*task:

        *undescribed*



.. _`oprofilefs_create_file`:

oprofilefs_create_file
======================

.. c:function:: int oprofilefs_create_file (struct dentry *root, char const *name, const struct file_operations *fops)

    :param struct dentry \*root:

        *undescribed*

    :param char const \*name:

        *undescribed*

    :param const struct file_operations \*fops:

        *undescribed*



.. _`oprofilefs_create_file.description`:

Description
-----------

the specified file operations.



.. _`oprofilefs_str_to_user`:

oprofilefs_str_to_user
======================

.. c:function:: ssize_t oprofilefs_str_to_user (char const *str, char __user *buf, size_t count, loff_t *offset)

    :param char const \*str:

        *undescribed*

    :param char __user \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*offset:

        *undescribed*



.. _`oprofilefs_str_to_user.description`:

Description
-----------

appropriately. Returns bytes written or -EFAULT.



.. _`oprofilefs_ulong_to_user`:

oprofilefs_ulong_to_user
========================

.. c:function:: ssize_t oprofilefs_ulong_to_user (unsigned long val, char __user *buf, size_t count, loff_t *offset)

    :param unsigned long val:

        *undescribed*

    :param char __user \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*offset:

        *undescribed*



.. _`oprofilefs_ulong_to_user.description`:

Description
-----------

updating \*offset appropriately. Returns bytes written or -EFAULT.



.. _`oprofilefs_ulong_from_user`:

oprofilefs_ulong_from_user
==========================

.. c:function:: int oprofilefs_ulong_from_user (unsigned long *val, char const __user *buf, size_t count)

    :param unsigned long \*val:

        *undescribed*

    :param char const __user \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*



.. _`oprofilefs_ulong_from_user.description`:

Description
-----------

Returns 0 on success, < 0 on error.



.. _`oprofile_put_buff`:

oprofile_put_buff
=================

.. c:function:: void oprofile_put_buff (unsigned long *buf, unsigned int start, unsigned int stop, unsigned int max)

    :param unsigned long \*buf:

        *undescribed*

    :param unsigned int start:

        *undescribed*

    :param unsigned int stop:

        *undescribed*

    :param unsigned int max:

        *undescribed*

