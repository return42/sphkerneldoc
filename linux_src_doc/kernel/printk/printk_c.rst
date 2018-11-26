.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/printk/printk.c

.. _`console_lock_spinning_enable`:

console_lock_spinning_enable
============================

.. c:function:: void console_lock_spinning_enable( void)

    mark beginning of code where another thread might safely busy wait

    :param void:
        no arguments
    :type void: 

.. _`console_lock_spinning_enable.description`:

Description
-----------

This basically converts console_lock into a spinlock. This marks
the section where the console_lock owner can not sleep, because
there may be a waiter spinning (like a spinlock). Also it must be
ready to hand over the lock at the end of the section.

.. _`console_lock_spinning_disable_and_check`:

console_lock_spinning_disable_and_check
=======================================

.. c:function:: int console_lock_spinning_disable_and_check( void)

    mark end of code where another thread was able to busy wait and check if there is a waiter

    :param void:
        no arguments
    :type void: 

.. _`console_lock_spinning_disable_and_check.description`:

Description
-----------

This is called at the end of the section where spinning is allowed.
It has two functions. First, it is a signal that it is no longer
safe to start busy waiting for the lock. Second, it checks if
there is a busy waiter and passes the lock rights to her.

Important: Callers lose the lock if there was a busy waiter.
     They must not touch items synchronized by console_lock
     in this case.

.. _`console_lock_spinning_disable_and_check.return`:

Return
------

1 if the lock rights were passed, 0 otherwise.

.. _`console_trylock_spinning`:

console_trylock_spinning
========================

.. c:function:: int console_trylock_spinning( void)

    try to get console_lock by busy waiting

    :param void:
        no arguments
    :type void: 

.. _`console_trylock_spinning.description`:

Description
-----------

This allows to busy wait for the console_lock when the current
owner is running in specially marked sections. It means that
the current owner is running and cannot reschedule until it
is ready to lose the lock.

.. _`console_trylock_spinning.return`:

Return
------

1 if we got the lock, 0 othrewise

.. _`printk`:

printk
======

.. c:function:: __visible int printk(const char *fmt,  ...)

    print a kernel message

    :param fmt:
        format string
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`printk.description`:

Description
-----------

This is \ :c:func:`printk`\ . It can be called from any context. We want it to work.

We try to grab the console_lock. If we succeed, it's easy - we log the
output and call the console drivers.  If we fail to get the semaphore, we
place the output into the log buffer and return. The current holder of
the console_sem will notice the new output in \ :c:func:`console_unlock`\ ; and will
send it to the consoles before releasing the lock.

One effect of this deferred printing is that code which calls \ :c:func:`printk`\  and
then changes console_loglevel may break. This is because console_loglevel
is inspected when the actual printing occurs.

.. _`printk.see-also`:

See also
--------

printf(3)

See the \ :c:func:`vsnprintf`\  documentation for format string extensions over C99.

.. _`add_preferred_console`:

add_preferred_console
=====================

.. c:function:: int add_preferred_console(char *name, int idx, char *options)

    add a device to the list of preferred consoles.

    :param name:
        device name
    :type name: char \*

    :param idx:
        device index
    :type idx: int

    :param options:
        options for this console
    :type options: char \*

.. _`add_preferred_console.description`:

Description
-----------

The last preferred console added will be used for kernel messages
and stdin/out/err for init.  Normally this is used by console_setup
above to handle user-supplied console arguments; however it can also
be used by arch-specific code either to override the user or more
commonly to provide a default console (ie from PROM variables) when
the user has not supplied one.

.. _`suspend_console`:

suspend_console
===============

.. c:function:: void suspend_console( void)

    suspend the console subsystem

    :param void:
        no arguments
    :type void: 

.. _`suspend_console.description`:

Description
-----------

This disables \ :c:func:`printk`\  while we go into suspend states

.. _`console_cpu_notify`:

console_cpu_notify
==================

.. c:function:: int console_cpu_notify(unsigned int cpu)

    print deferred console messages after CPU hotplug

    :param cpu:
        unused
    :type cpu: unsigned int

.. _`console_cpu_notify.description`:

Description
-----------

If \ :c:func:`printk`\  is called from a CPU that is not online yet, the messages
will be printed on the console only if there are CON_ANYTIME consoles.
This function is called when a new CPU comes online (or fails to come
up) or goes offline.

.. _`console_lock`:

console_lock
============

.. c:function:: void console_lock( void)

    lock the console system for exclusive use.

    :param void:
        no arguments
    :type void: 

.. _`console_lock.description`:

Description
-----------

Acquires a lock which guarantees that the caller has
exclusive access to the console system and the console_drivers list.

Can sleep, returns nothing.

.. _`console_trylock`:

console_trylock
===============

.. c:function:: int console_trylock( void)

    try to lock the console system for exclusive use.

    :param void:
        no arguments
    :type void: 

.. _`console_trylock.description`:

Description
-----------

Try to acquire a lock which guarantees that the caller has exclusive
access to the console system and the console_drivers list.

returns 1 on success, and 0 on failure to acquire the lock.

.. _`console_unlock`:

console_unlock
==============

.. c:function:: void console_unlock( void)

    unlock the console system

    :param void:
        no arguments
    :type void: 

.. _`console_unlock.description`:

Description
-----------

Releases the console_lock which the caller holds on the console system
and the console driver list.

While the console_lock was held, console output may have been buffered
by \ :c:func:`printk`\ .  If this is the case, \ :c:func:`console_unlock`\ ; emits
the output prior to releasing the lock.

If there is output waiting, we wake /dev/kmsg and \ :c:func:`syslog`\  users.

\ :c:func:`console_unlock`\ ; may be called from any context.

.. _`console_conditional_schedule`:

console_conditional_schedule
============================

.. c:function:: void __sched console_conditional_schedule( void)

    yield the CPU if required

    :param void:
        no arguments
    :type void: 

.. _`console_conditional_schedule.description`:

Description
-----------

If the console code is currently allowed to sleep, and
if this CPU should yield the CPU to another task, do
so here.

Must be called within \ :c:func:`console_lock`\ ;.

.. _`console_flush_on_panic`:

console_flush_on_panic
======================

.. c:function:: void console_flush_on_panic( void)

    flush console content on panic

    :param void:
        no arguments
    :type void: 

.. _`console_flush_on_panic.description`:

Description
-----------

Immediately output all pending messages no matter what.

.. _`printk_timed_ratelimit`:

printk_timed_ratelimit
======================

.. c:function:: bool printk_timed_ratelimit(unsigned long *caller_jiffies, unsigned int interval_msecs)

    caller-controlled printk ratelimiting

    :param caller_jiffies:
        pointer to caller's state
    :type caller_jiffies: unsigned long \*

    :param interval_msecs:
        minimum interval between prints
    :type interval_msecs: unsigned int

.. _`printk_timed_ratelimit.description`:

Description
-----------

\ :c:func:`printk_timed_ratelimit`\  returns true if more than \ ``interval_msecs``\ 
milliseconds have elapsed since the last time \ :c:func:`printk_timed_ratelimit`\ 
returned true.

.. _`kmsg_dump_register`:

kmsg_dump_register
==================

.. c:function:: int kmsg_dump_register(struct kmsg_dumper *dumper)

    register a kernel log dumper.

    :param dumper:
        pointer to the kmsg_dumper structure
    :type dumper: struct kmsg_dumper \*

.. _`kmsg_dump_register.description`:

Description
-----------

Adds a kernel log dumper to the system. The dump callback in the
structure will be called when the kernel oopses or panics and must be
set. Returns zero on success and \ ``-EINVAL``\  or \ ``-EBUSY``\  otherwise.

.. _`kmsg_dump_unregister`:

kmsg_dump_unregister
====================

.. c:function:: int kmsg_dump_unregister(struct kmsg_dumper *dumper)

    unregister a kmsg dumper.

    :param dumper:
        pointer to the kmsg_dumper structure
    :type dumper: struct kmsg_dumper \*

.. _`kmsg_dump_unregister.description`:

Description
-----------

Removes a dump device from the system. Returns zero on success and
\ ``-EINVAL``\  otherwise.

.. _`kmsg_dump`:

kmsg_dump
=========

.. c:function:: void kmsg_dump(enum kmsg_dump_reason reason)

    dump kernel log to kernel message dumpers.

    :param reason:
        the reason (oops, panic etc) for dumping
    :type reason: enum kmsg_dump_reason

.. _`kmsg_dump.description`:

Description
-----------

Call each of the registered dumper's \ :c:func:`dump`\  callback, which can
retrieve the kmsg records with \ :c:func:`kmsg_dump_get_line`\  or
\ :c:func:`kmsg_dump_get_buffer`\ .

.. _`kmsg_dump_get_line_nolock`:

kmsg_dump_get_line_nolock
=========================

.. c:function:: bool kmsg_dump_get_line_nolock(struct kmsg_dumper *dumper, bool syslog, char *line, size_t size, size_t *len)

    retrieve one kmsg log line (unlocked version)

    :param dumper:
        registered kmsg dumper
    :type dumper: struct kmsg_dumper \*

    :param syslog:
        include the "<4>" prefixes
    :type syslog: bool

    :param line:
        buffer to copy the line to
    :type line: char \*

    :param size:
        maximum size of the buffer
    :type size: size_t

    :param len:
        length of line placed into buffer
    :type len: size_t \*

.. _`kmsg_dump_get_line_nolock.description`:

Description
-----------

Start at the beginning of the kmsg buffer, with the oldest kmsg
record, and copy one record into the provided buffer.

Consecutive calls will return the next available record moving
towards the end of the buffer with the youngest messages.

A return value of FALSE indicates that there are no more records to
read.

The function is similar to \ :c:func:`kmsg_dump_get_line`\ , but grabs no locks.

.. _`kmsg_dump_get_line`:

kmsg_dump_get_line
==================

.. c:function:: bool kmsg_dump_get_line(struct kmsg_dumper *dumper, bool syslog, char *line, size_t size, size_t *len)

    retrieve one kmsg log line

    :param dumper:
        registered kmsg dumper
    :type dumper: struct kmsg_dumper \*

    :param syslog:
        include the "<4>" prefixes
    :type syslog: bool

    :param line:
        buffer to copy the line to
    :type line: char \*

    :param size:
        maximum size of the buffer
    :type size: size_t

    :param len:
        length of line placed into buffer
    :type len: size_t \*

.. _`kmsg_dump_get_line.description`:

Description
-----------

Start at the beginning of the kmsg buffer, with the oldest kmsg
record, and copy one record into the provided buffer.

Consecutive calls will return the next available record moving
towards the end of the buffer with the youngest messages.

A return value of FALSE indicates that there are no more records to
read.

.. _`kmsg_dump_get_buffer`:

kmsg_dump_get_buffer
====================

.. c:function:: bool kmsg_dump_get_buffer(struct kmsg_dumper *dumper, bool syslog, char *buf, size_t size, size_t *len)

    copy kmsg log lines

    :param dumper:
        registered kmsg dumper
    :type dumper: struct kmsg_dumper \*

    :param syslog:
        include the "<4>" prefixes
    :type syslog: bool

    :param buf:
        buffer to copy the line to
    :type buf: char \*

    :param size:
        maximum size of the buffer
    :type size: size_t

    :param len:
        length of line placed into buffer
    :type len: size_t \*

.. _`kmsg_dump_get_buffer.description`:

Description
-----------

Start at the end of the kmsg buffer and fill the provided buffer
with as many of the the *youngest* kmsg records that fit into it.
If the buffer is large enough, all available kmsg records will be
copied with a single call.

Consecutive calls will fill the buffer with the next block of
available older records, not including the earlier retrieved ones.

A return value of FALSE indicates that there are no more records to
read.

.. _`kmsg_dump_rewind_nolock`:

kmsg_dump_rewind_nolock
=======================

.. c:function:: void kmsg_dump_rewind_nolock(struct kmsg_dumper *dumper)

    reset the interator (unlocked version)

    :param dumper:
        registered kmsg dumper
    :type dumper: struct kmsg_dumper \*

.. _`kmsg_dump_rewind_nolock.description`:

Description
-----------

Reset the dumper's iterator so that \ :c:func:`kmsg_dump_get_line`\  and
\ :c:func:`kmsg_dump_get_buffer`\  can be called again and used multiple
times within the same dumper.dump() callback.

The function is similar to \ :c:func:`kmsg_dump_rewind`\ , but grabs no locks.

.. _`kmsg_dump_rewind`:

kmsg_dump_rewind
================

.. c:function:: void kmsg_dump_rewind(struct kmsg_dumper *dumper)

    reset the interator

    :param dumper:
        registered kmsg dumper
    :type dumper: struct kmsg_dumper \*

.. _`kmsg_dump_rewind.description`:

Description
-----------

Reset the dumper's iterator so that \ :c:func:`kmsg_dump_get_line`\  and
\ :c:func:`kmsg_dump_get_buffer`\  can be called again and used multiple
times within the same dumper.dump() callback.

.. This file was automatic generated / don't edit.

