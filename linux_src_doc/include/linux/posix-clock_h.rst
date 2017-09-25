.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/posix-clock.h

.. _`posix_clock_operations`:

struct posix_clock_operations
=============================

.. c:type:: struct posix_clock_operations

    functional interface to the clock

.. _`posix_clock_operations.definition`:

Definition
----------

.. code-block:: c

    struct posix_clock_operations {
        struct module *owner;
        int (*clock_adjtime)(struct posix_clock *pc, struct timex *tx);
        int (*clock_gettime)(struct posix_clock *pc, struct timespec64 *ts);
        int (*clock_getres) (struct posix_clock *pc, struct timespec64 *ts);
        int (*clock_settime)(struct posix_clock *pc, const struct timespec64 *ts);
        long (*ioctl) (struct posix_clock *pc, unsigned int cmd, unsigned long arg);
        int (*open) (struct posix_clock *pc, fmode_t f_mode);
        uint (*poll) (struct posix_clock *pc, struct file *file, poll_table *wait);
        int (*release) (struct posix_clock *pc);
        ssize_t (*read) (struct posix_clock *pc, uint flags, char __user *buf, size_t cnt);
    }

.. _`posix_clock_operations.members`:

Members
-------

owner
    The clock driver should set to THIS_MODULE

clock_adjtime
    Adjust the clock

clock_gettime
    Read the current time

clock_getres
    Get the clock resolution

clock_settime
    Set the current time value

ioctl
    Optional character device ioctl method

open
    Optional character device open method

poll
    Optional character device poll method

release
    Optional character device release method

read
    Optional character device read method

.. _`posix_clock_operations.description`:

Description
-----------

Every posix clock is represented by a character device. Drivers may
optionally offer extended capabilities by implementing the
character device methods. The character device file operations are
first handled by the clock device layer, then passed on to the
driver by calling these functions.

.. _`posix_clock`:

struct posix_clock
==================

.. c:type:: struct posix_clock

    represents a dynamic posix clock

.. _`posix_clock.definition`:

Definition
----------

.. code-block:: c

    struct posix_clock {
        struct posix_clock_operations ops;
        struct cdev cdev;
        struct kref kref;
        struct rw_semaphore rwsem;
        bool zombie;
        void (*release)(struct posix_clock *clk);
    }

.. _`posix_clock.members`:

Members
-------

ops
    Functional interface to the clock

cdev
    Character device instance for this clock

kref
    Reference count.

rwsem
    Protects the 'zombie' field from concurrent access.

zombie
    If 'zombie' is true, then the hardware has disappeared.

release
    A function to free the structure when the reference count reaches
    zero. May be NULL if structure is statically allocated.

.. _`posix_clock.description`:

Description
-----------

Drivers should embed their struct posix_clock within a private
structure, obtaining a reference to it during callbacks using
\ :c:func:`container_of`\ .

.. _`posix_clock_register`:

posix_clock_register
====================

.. c:function:: int posix_clock_register(struct posix_clock *clk, dev_t devid)

    register a new clock

    :param struct posix_clock \*clk:
        Pointer to the clock. Caller must provide 'ops' and 'release'

    :param dev_t devid:
        Allocated device id

.. _`posix_clock_register.description`:

Description
-----------

A clock driver calls this function to register itself with the
clock device subsystem. If 'clk' points to dynamically allocated
memory, then the caller must provide a 'release' function to free
that memory.

Returns zero on success, non-zero otherwise.

.. _`posix_clock_unregister`:

posix_clock_unregister
======================

.. c:function:: void posix_clock_unregister(struct posix_clock *clk)

    unregister a clock

    :param struct posix_clock \*clk:
        Clock instance previously registered via \ :c:func:`posix_clock_register`\ 

.. _`posix_clock_unregister.description`:

Description
-----------

A clock driver calls this function to remove itself from the clock
device subsystem. The posix_clock itself will remain (in an
inactive state) until its reference count drops to zero, at which
point it will be deallocated with its 'release' method.

.. This file was automatic generated / don't edit.

