.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/kmod.c

.. _`__request_module`:

__request_module
================

.. c:function:: int __request_module(bool wait, const char *fmt,  ...)

    try to load a kernel module

    :param bool wait:
        wait (or not) for the operation to complete

    :param const char \*fmt:
        printf style format string for the name of the module

    :param ellipsis ellipsis:
        arguments as specified in the format string

.. _`__request_module.description`:

Description
-----------

Load a module using the user mode module loader. The function returns
zero on success or a negative errno code or positive exit code from
"modprobe" on failure. Note that a successful module load does not mean
the module did not then unload and exit on an error of its own. Callers
must check that the service they requested is now available not blindly
invoke it.

If module auto-loading support is disabled then this function
becomes a no-operation.

.. This file was automatic generated / don't edit.

