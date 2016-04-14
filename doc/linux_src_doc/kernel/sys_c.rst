.. -*- coding: utf-8; mode: rst -*-

=====
sys.c
=====

.. _`sys_getpid`:

sys_getpid
==========

.. c:function:: long sys_getpid ( void)

    return the thread group id of the current process

    :param void:
        no arguments


.. _`sys_getpid.description`:

Description
-----------


Note, despite the name, this returns the tgid not the pid.  The tgid and
the pid are identical unless CLONE_THREAD was specified on :c:func:`clone` in
which case the tgid is the same in all threads of the same group.

This is SMP safe as current->tgid does not change.


.. _`do_sysinfo`:

do_sysinfo
==========

.. c:function:: int do_sysinfo (struct sysinfo *info)

    fill in sysinfo struct

    :param struct sysinfo \*info:
        pointer to buffer to fill

