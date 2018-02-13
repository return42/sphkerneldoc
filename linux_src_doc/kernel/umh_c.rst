.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/umh.c

.. _`__usermodehelper_set_disable_depth`:

\__usermodehelper_set_disable_depth
===================================

.. c:function:: void __usermodehelper_set_disable_depth(enum umh_disable_depth depth)

    Modify usermodehelper_disabled.

    :param enum umh_disable_depth depth:
        New value to assign to usermodehelper_disabled.

.. _`__usermodehelper_set_disable_depth.description`:

Description
-----------

Change the value of usermodehelper_disabled (under umhelper_sem locked for
writing) and wakeup tasks waiting for it to change.

.. _`__usermodehelper_disable`:

\__usermodehelper_disable
=========================

.. c:function:: int __usermodehelper_disable(enum umh_disable_depth depth)

    Prevent new helpers from being started.

    :param enum umh_disable_depth depth:
        New value to assign to usermodehelper_disabled.

.. _`__usermodehelper_disable.description`:

Description
-----------

Set usermodehelper_disabled to \ ``depth``\  and wait for running helpers to exit.

.. _`call_usermodehelper_setup`:

call_usermodehelper_setup
=========================

.. c:function:: struct subprocess_info *call_usermodehelper_setup(const char *path, char **argv, char **envp, gfp_t gfp_mask, int (*init)(struct subprocess_info *info, struct cred *new), void (*cleanup)(struct subprocess_info *info), void *data)

    prepare to call a usermode helper

    :param const char \*path:
        path to usermode executable

    :param char \*\*argv:
        arg vector for process

    :param char \*\*envp:
        environment for process

    :param gfp_t gfp_mask:
        gfp mask for memory allocation

    :param int (\*init)(struct subprocess_info \*info, struct cred \*new):
        an init function

    :param void (\*cleanup)(struct subprocess_info \*info):
        a cleanup function

    :param void \*data:
        arbitrary context sensitive data

.. _`call_usermodehelper_setup.description`:

Description
-----------

Returns either \ ``NULL``\  on allocation failure, or a subprocess_info
structure.  This should be passed to call_usermodehelper_exec to
exec the process and free the structure.

The init function is used to customize the helper process prior to
exec.  A non-zero return code causes the process to error out, exit,
and return the failure to the calling process

The cleanup function is just before ethe subprocess_info is about to
be freed.  This can be used for freeing the argv and envp.  The
Function must be runnable in either a process context or the
context in which call_usermodehelper_exec is called.

.. _`call_usermodehelper_exec`:

call_usermodehelper_exec
========================

.. c:function:: int call_usermodehelper_exec(struct subprocess_info *sub_info, int wait)

    start a usermode application

    :param struct subprocess_info \*sub_info:
        information about the subprocessa

    :param int wait:
        wait for the application to finish and return status.
        when UMH_NO_WAIT don't wait at all, but you get no useful error back
        when the program couldn't be exec'ed. This makes it safe to call
        from interrupt context.

.. _`call_usermodehelper_exec.description`:

Description
-----------

Runs a user-space application.  The application is started
asynchronously if wait is not set, and runs as a child of system workqueues.
(ie. it runs with full root capabilities and optimized affinity).

.. _`call_usermodehelper`:

call_usermodehelper
===================

.. c:function:: int call_usermodehelper(const char *path, char **argv, char **envp, int wait)

    prepare and start a usermode application

    :param const char \*path:
        path to usermode executable

    :param char \*\*argv:
        arg vector for process

    :param char \*\*envp:
        environment for process

    :param int wait:
        wait for the application to finish and return status.
        when UMH_NO_WAIT don't wait at all, but you get no useful error back
        when the program couldn't be exec'ed. This makes it safe to call
        from interrupt context.

.. _`call_usermodehelper.description`:

Description
-----------

This function is the equivalent to use \ :c:func:`call_usermodehelper_setup`\  and
\ :c:func:`call_usermodehelper_exec`\ .

.. This file was automatic generated / don't edit.

