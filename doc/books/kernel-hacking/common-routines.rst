.. -*- coding: utf-8; mode: rst -*-

.. _common-routines:

***************
Common Routines
***************


.. _routines-printk:

printk() include/linux/kernel.h
===============================

``printk()`` feeds kernel messages to the console, dmesg, and the syslog
daemon. It is useful for debugging and reporting errors, and can be used
inside interrupt context, but use with caution: a machine which has its
console flooded with printk messages is unusable. It uses a format
string mostly compatible with ANSI C printf, and C string concatenation
to give it a first "priority" argument:


.. code-block:: c

    printk(KERN_INFO "i = %un", i);

See ``include/linux/kernel.h``; for other KERN_ values; these are
interpreted by syslog as the level. Special case: for printing an IP
address use


.. code-block:: c

    __be32 ipaddress;
    printk(KERN_INFO "my ip: %pI4n", &ipaddress);

``printk()`` internally uses a 1K buffer and does not catch overruns.
Make sure that will be enough.

    **Note**

    You will know when you are a real kernel hacker when you start
    typoing printf as printk in your user programs :)

    **Note**

    Another sidenote: the original Unix Version 6 sources had a comment
    on top of its printf function: "Printf should not be used for
    chit-chat". You should follow that advice.


.. _routines-copy:

copy_[to/from]_user() / get_user() / put_user() include/asm/uaccess.h
=====================================================================

*[SLEEPS]*

``put_user()`` and ``get_user()`` are used to get and put single values
(such as an int, char, or long) from and to userspace. A pointer into
userspace should never be simply dereferenced: data should be copied
using these routines. Both return ``-EFAULT`` or 0.

``copy_to_user()`` and ``copy_from_user()`` are more general: they copy
an arbitrary amount of data to and from userspace.

    **Caution**

    Unlike ``put_user()`` and ``get_user()``, they return the amount of
    uncopied data (ie. 0 still means success).

[Yes, this moronic interface makes me cringe. The flamewar comes up
every year or so. --RR.]

The functions may sleep implicitly. This should never be called outside
user context (it makes no sense), with interrupts disabled, or a
spinlock held.


.. _routines-kmalloc:

kmalloc()/kfree() include/linux/slab.h
======================================

*[MAY SLEEP: SEE BELOW]*

These routines are used to dynamically request pointer-aligned chunks of
memory, like malloc and free do in userspace, but ``kmalloc()`` takes an
extra flag word. Important values:

``GFP_KERNEL``
    May sleep and swap to free memory. Only allowed in user context, but
    is the most reliable way to allocate memory.

``GFP_ATOMIC``
    Don't sleep. Less reliable than ``GFP_KERNEL``, but may be called
    from interrupt context. You should *really* have a good
    out-of-memory error-handling strategy.

``GFP_DMA``
    Allocate ISA DMA lower than 16MB. If you don't know what that is you
    don't need it. Very unreliable.

If you see a sleeping function called from invalid context warning
message, then maybe you called a sleeping allocation function from
interrupt context without ``GFP_ATOMIC``. You should really fix that.
Run, don't walk.

If you are allocating at least ``PAGE_SIZE`` (``include/asm/page.h``)
bytes, consider using ``__get_free_pages()`` (``include/linux/mm.h``).
It takes an order argument (0 for page sized, 1 for double page, 2 for
four pages etc.) and the same memory priority flag word as above.

If you are allocating more than a page worth of bytes you can use
``vmalloc()``. It'll allocate virtual memory in the kernel map. This
block is not contiguous in physical memory, but the MMU makes it look
like it is for you (so it'll only look contiguous to the CPUs, not to
external device drivers). If you really need large physically contiguous
memory for some weird device, you have a problem: it is poorly supported
in Linux because after some time memory fragmentation in a running
kernel makes it hard. The best way is to allocate the block early in the
boot process via the ``alloc_bootmem()`` routine.

Before inventing your own cache of often-used objects consider using a
slab cache in ``include/linux/slab.h``


.. _routines-current:

current include/asm/current.h
=============================

This global variable (really a macro) contains a pointer to the current
task structure, so is only valid in user context. For example, when a
process makes a system call, this will point to the task structure of
the calling process. It is *not NULL* in interrupt context.


.. _routines-udelay:

mdelay()/udelay() include/asm/delay.h include/linux/delay.h
===========================================================

The ``udelay()`` and ``ndelay()`` functions can be used for small
pauses. Do not use large values with them as you risk overflow - the
helper function ``mdelay()`` is useful here, or consider ``msleep()``.


.. _routines-endian:

cpu_to_be32()/be32_to_cpu()/cpu_to_le32()/le32_to_cpu() include/asm/byteorder.h
===============================================================================

The ``cpu_to_be32()`` family (where the "32" can be replaced by 64 or
16, and the "be" can be replaced by "le") are the general way to do
endian conversions in the kernel: they return the converted value. All
variations supply the reverse as well: ``be32_to_cpu()``, etc.

There are two major variations of these functions: the pointer
variation, such as ``cpu_to_be32p()``, which take a pointer to the given
type, and return the converted value. The other variation is the
"in-situ" family, such as ``cpu_to_be32s()``, which convert value
referred to by the pointer, and return void.


.. _routines-local-irqs:

local_irq_save()/local_irq_restore() include/linux/irqflags.h
=============================================================

These routines disable hard interrupts on the local CPU, and restore
them. They are reentrant; saving the previous state in their one
``unsigned long flags`` argument. If you know that interrupts are
enabled, you can simply use ``local_irq_disable()`` and
``local_irq_enable()``.


.. _routines-softirqs:

local_bh_disable()/local_bh_enable() include/linux/interrupt.h
==============================================================

These routines disable soft interrupts on the local CPU, and restore
them. They are reentrant; if soft interrupts were disabled before, they
will still be disabled after this pair of functions has been called.
They prevent softirqs and tasklets from running on the current CPU.


.. _routines-processorids:

smp_processor_id() include/asm/smp.h
====================================

``get_cpu()`` disables preemption (so you won't suddenly get moved to
another CPU) and returns the current processor number, between 0 and
``NR_CPUS``. Note that the CPU numbers are not necessarily continuous.
You return it again with ``put_cpu()`` when you are done.

If you know you cannot be preempted by another task (ie. you are in
interrupt context, or have preemption disabled) you can use
smp_processor_id().


.. _routines-init:

__init/__exit/__initdata include/linux/init.h
=============================================

After boot, the kernel frees up a special section; functions marked with
``__init`` and data structures marked with ``__initdata`` are dropped
after boot is complete: similarly modules discard this memory after
initialization. ``__exit`` is used to declare a function which is only
required on exit: the function will be dropped if this file is not
compiled as a module. See the header file for use. Note that it makes no
sense for a function marked with ``__init`` to be exported to modules
with ``EXPORT_SYMBOL()`` - this will break.


.. _routines-init-again:

__initcall()/module_init() include/linux/init.h
===============================================

Many parts of the kernel are well served as a module
(dynamically-loadable parts of the kernel). Using the ``module_init()``
and ``module_exit()`` macros it is easy to write code without #ifdefs
which can operate both as a module or built into the kernel.

The ``module_init()`` macro defines which function is to be called at
module insertion time (if the file is compiled as a module), or at boot
time: if the file is not compiled as a module the ``module_init()``
macro becomes equivalent to ``__initcall()``, which through linker magic
ensures that the function is called on boot.

The function can return a negative error number to cause module loading
to fail (unfortunately, this has no effect if the module is compiled
into the kernel). This function is called in user context with
interrupts enabled, so it can sleep.


.. _routines-moduleexit:

module_exit() include/linux/init.h
==================================

This macro defines the function to be called at module removal time (or
never, in the case of the file compiled into the kernel). It will only
be called if the module usage count has reached zero. This function can
also sleep, but cannot fail: everything must be cleaned up by the time
it returns.

Note that this macro is optional: if it is not present, your module will
not be removable (except for 'rmmod -f').


.. _routines-module-use-counters:

try_module_get()/module_put() include/linux/module.h
====================================================

These manipulate the module usage count, to protect against removal (a
module also can't be removed if another module uses one of its exported
symbols: see below). Before calling into module code, you should call
``try_module_get()`` on that module: if it fails, then the module is
being removed and you should act as if it wasn't there. Otherwise, you
can safely enter the module, and call ``module_put()`` when you're
finished.

Most registerable structures have an ``owner`` field, such as in the
``file_operations`` structure. Set this field to the macro
``THIS_MODULE``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
