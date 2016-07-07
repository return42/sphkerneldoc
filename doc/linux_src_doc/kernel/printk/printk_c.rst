.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/printk/printk.c

.. _`printk`:

printk
======

.. c:function:: __visible int printk(const char *fmt,  ...)

    print a kernel message

    :param const char \*fmt:
        format string

    :param ... :
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

    :param char \*name:
        device name

    :param int idx:
        device index

    :param char \*options:
        options for this console

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

    :param  void:
        no arguments

.. _`suspend_console.description`:

Description
-----------

This disables \ :c:func:`printk`\  while we go into suspend states

.. _`console_cpu_notify`:

console_cpu_notify
==================

.. c:function:: int console_cpu_notify(struct notifier_block *self, unsigned long action, void *hcpu)

    print deferred console messages after CPU hotplug

    :param struct notifier_block \*self:
        notifier struct

    :param unsigned long action:
        CPU hotplug event

    :param void \*hcpu:
        unused

.. _`console_cpu_notify.description`:

Description
-----------

If \ :c:func:`printk`\  is called from a CPU that is not online yet, the messages
will be spooled but will not show up on the console.  This function is
called when a new CPU comes online (or fails to come up), and ensures
that any such output gets printed.

.. _`console_lock`:

console_lock
============

.. c:function:: void console_lock( void)

    lock the console system for exclusive use.

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

.. _`console_flush_on_panic.description`:

Description
-----------

Immediately output all pending messages no matter what.

.. _`printk_timed_ratelimit`:

printk_timed_ratelimit
======================

.. c:function:: bool printk_timed_ratelimit(unsigned long *caller_jiffies, unsigned int interval_msecs)

    caller-controlled printk ratelimiting

    :param unsigned long \*caller_jiffies:
        pointer to caller's state

    :param unsigned int interval_msecs:
        minimum interval between prints

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

    :param struct kmsg_dumper \*dumper:
        pointer to the kmsg_dumper structure

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

    :param struct kmsg_dumper \*dumper:
        pointer to the kmsg_dumper structure

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

    :param enum kmsg_dump_reason reason:
        the reason (oops, panic etc) for dumping

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

    :param struct kmsg_dumper \*dumper:
        registered kmsg dumper

    :param bool syslog:
        include the "<4>" prefixes

    :param char \*line:
        buffer to copy the line to

    :param size_t size:
        maximum size of the buffer

    :param size_t \*len:
        length of line placed into buffer

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

    :param struct kmsg_dumper \*dumper:
        registered kmsg dumper

    :param bool syslog:
        include the "<4>" prefixes

    :param char \*line:
        buffer to copy the line to

    :param size_t size:
        maximum size of the buffer

    :param size_t \*len:
        length of line placed into buffer

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

    :param struct kmsg_dumper \*dumper:
        registered kmsg dumper

    :param bool syslog:
        include the "<4>" prefixes

    :param char \*buf:
        buffer to copy the line to

    :param size_t size:
        maximum size of the buffer

    :param size_t \*len:
        length of line placed into buffer

.. _`kmsg_dump_get_buffer.description`:

Description
-----------

Start at the end of the kmsg buffer and fill the provided buffer
with as many of the the \*youngest\* kmsg records that fit into it.
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

    :param struct kmsg_dumper \*dumper:
        registered kmsg dumper

.. _`kmsg_dump_rewind_nolock.description`:

Description
-----------

Reset the dumper's iterator so that \ :c:func:`kmsg_dump_get_line`\  and
\ :c:func:`kmsg_dump_get_buffer`\  can be called again and used multiple
times within the same dumper.\ :c:func:`dump`\  callback.

The function is similar to \ :c:func:`kmsg_dump_rewind`\ , but grabs no locks.

.. _`kmsg_dump_rewind`:

kmsg_dump_rewind
================

.. c:function:: void kmsg_dump_rewind(struct kmsg_dumper *dumper)

    reset the interator

    :param struct kmsg_dumper \*dumper:
        registered kmsg dumper

.. _`kmsg_dump_rewind.description`:

Description
-----------

Reset the dumper's iterator so that \ :c:func:`kmsg_dump_get_line`\  and
\ :c:func:`kmsg_dump_get_buffer`\  can be called again and used multiple
times within the same dumper.\ :c:func:`dump`\  callback.

.. _`dump_stack_set_arch_desc`:

dump_stack_set_arch_desc
========================

.. c:function:: void dump_stack_set_arch_desc(const char *fmt,  ...)

    set arch-specific str to show with task dumps

    :param const char \*fmt:
        printf-style format string

    :param ... :
        arguments for the format string

.. _`dump_stack_set_arch_desc.description`:

Description
-----------

The configured string will be printed right after utsname during task
dumps.  Usually used to add arch-specific system identifiers.  If an
arch wants to make use of such an ID string, it should initialize this
as soon as possible during boot.

.. _`dump_stack_print_info`:

dump_stack_print_info
=====================

.. c:function:: void dump_stack_print_info(const char *log_lvl)

    print generic debug info for \ :c:func:`dump_stack`\ 

    :param const char \*log_lvl:
        log level

.. _`dump_stack_print_info.description`:

Description
-----------

Arch-specific \ :c:func:`dump_stack`\  implementations can use this function to
print out the same debug information as the generic \ :c:func:`dump_stack`\ .

.. _`show_regs_print_info`:

show_regs_print_info
====================

.. c:function:: void show_regs_print_info(const char *log_lvl)

    print generic debug info for \ :c:func:`show_regs`\ 

    :param const char \*log_lvl:
        log level

.. _`show_regs_print_info.description`:

Description
-----------

\ :c:func:`show_regs`\  implementations can use this function to print out generic
debug information.

.. This file was automatic generated / don't edit.

