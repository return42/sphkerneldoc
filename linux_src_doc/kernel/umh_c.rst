.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/umh.c

.. _`__usermodehelper_set_disable_depth`:

\__usermodehelper_set_disable_depth
===================================

.. c:function:: void __usermodehelper_set_disable_depth(enum umh_disable_depth depth)

    Modify usermodehelper_disabled.

    :param depth:
        New value to assign to usermodehelper_disabled.
    :type depth: enum umh_disable_depth

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

    :param depth:
        New value to assign to usermodehelper_disabled.
    :type depth: enum umh_disable_depth

.. _`__usermodehelper_disable.description`:

Description
-----------

Set usermodehelper_disabled to \ ``depth``\  and wait for running helpers to exit.

.. _`call_usermodehelper_setup`:

call_usermodehelper_setup
=========================

.. c:function:: struct subprocess_info *call_usermodehelper_setup(const char *path, char **argv, char **envp, gfp_t gfp_mask, int (*init)(struct subprocess_info *info, struct cred *new), void (*cleanup)(struct subprocess_info *info), void *data)

    prepare to call a usermode helper

    :param path:
        path to usermode executable
    :type path: const char \*

    :param argv:
        arg vector for process
    :type argv: char \*\*

    :param envp:
        environment for process
    :type envp: char \*\*

    :param gfp_mask:
        gfp mask for memory allocation
    :type gfp_mask: gfp_t

    :param int (\*init)(struct subprocess_info \*info, struct cred \*new):
        an init function

    :param void (\*cleanup)(struct subprocess_info \*info):
        a cleanup function

    :param data:
        arbitrary context sensitive data
    :type data: void \*

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

.. _`fork_usermode_blob`:

fork_usermode_blob
==================

.. c:function:: int fork_usermode_blob(void *data, size_t len, struct umh_info *info)

    fork a blob of bytes as a usermode process

    :param data:
        a blob of bytes that can be do_execv-ed as a file
    :type data: void \*

    :param len:
        length of the blob
    :type len: size_t

    :param info:
        information about usermode process (shouldn't be NULL)
    :type info: struct umh_info \*

.. _`fork_usermode_blob.description`:

Description
-----------

If info->cmdline is set it will be used as command line for the
user process, else "usermodehelper" is used.

Returns either negative error or zero which indicates success
in executing a blob of bytes as a usermode process. In such
case 'struct umh_info \*info' is populated with two pipes
and a pid of the process. The caller is responsible for health
check of the user process, killing it via pid, and closing the
pipes when user process is no longer needed.

.. _`call_usermodehelper_exec`:

call_usermodehelper_exec
========================

.. c:function:: int call_usermodehelper_exec(struct subprocess_info *sub_info, int wait)

    start a usermode application

    :param sub_info:
        information about the subprocessa
    :type sub_info: struct subprocess_info \*

    :param wait:
        wait for the application to finish and return status.
        when UMH_NO_WAIT don't wait at all, but you get no useful error back
        when the program couldn't be exec'ed. This makes it safe to call
        from interrupt context.
    :type wait: int

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

    :param path:
        path to usermode executable
    :type path: const char \*

    :param argv:
        arg vector for process
    :type argv: char \*\*

    :param envp:
        environment for process
    :type envp: char \*\*

    :param wait:
        wait for the application to finish and return status.
        when UMH_NO_WAIT don't wait at all, but you get no useful error back
        when the program couldn't be exec'ed. This makes it safe to call
        from interrupt context.
    :type wait: int

.. _`call_usermodehelper.description`:

Description
-----------

This function is the equivalent to use \ :c:func:`call_usermodehelper_setup`\  and
\ :c:func:`call_usermodehelper_exec`\ .

.. This file was automatic generated / don't edit.

