.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/syscalls.c

.. _`do_spu_run`:

do_spu_run
==========

.. c:function:: long do_spu_run(struct file *filp, __u32 __user *unpc, __u32 __user *ustatus)

    run code loaded into an SPU

    :param struct file \*filp:
        *undescribed*

    :param __u32 __user \*unpc:
        next program counter for the SPU

    :param __u32 __user \*ustatus:
        status of the SPU

.. _`do_spu_run.description`:

Description
-----------

This system call transfers the control of execution of a
user space thread to an SPU. It will return when the
SPU has finished executing or when it hits an error
condition and it will be interrupted if a signal needs
to be delivered to a handler in user space.

The next program counter is set to the passed value
before the SPU starts fetching code and the user space
pointer gets updated with the new value when returning
from kernel space.

The status value returned from spu_run reflects the
value of the spu_status register after the SPU has stopped.

.. This file was automatic generated / don't edit.

