.. -*- coding: utf-8; mode: rst -*-

=============
thread_info.h
=============


.. _`set_restore_sigmask`:

set_restore_sigmask
===================

.. c:function:: void set_restore_sigmask ( void)

    make sure saved_sigmask processing gets done

    :param void:
        no arguments



.. _`set_restore_sigmask.description`:

Description
-----------


This sets TIF_RESTORE_SIGMASK and ensures that the arch signal code
will run before returning to user mode, to process the flag.  For
all callers, TIF_SIGPENDING is already set or it's no harm to set
it.  TIF_RESTORE_SIGMASK need not be in the set of bits that the
arch code will notice on return to user mode, in case those bits
are scarce.  We set TIF_SIGPENDING here to ensure that the arch
signal code always gets run when TIF_RESTORE_SIGMASK is set.

