.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-compat-ioctl32.c

.. _`assign_in_user`:

assign_in_user
==============

.. c:function::  assign_in_user( to,  from)

    Copy from one \__user var to another one

    :param to:
        \__user var where data will be stored
    :type to: 

    :param from:
        \__user var where data will be retrieved.
    :type from: 

.. _`assign_in_user.description`:

Description
-----------

As this code very often needs to allocate userspace memory, it is easier
to have a macro that will do both \ :c:func:`get_user`\  and \ :c:func:`put_user`\  at once.

This function complements the macros defined at asm-generic/uaccess.h.
It uses the same argument order as \ :c:func:`copy_in_user`\ 

.. _`get_user_cast`:

get_user_cast
=============

.. c:function::  get_user_cast( __x,  __ptr)

    Stores at a kernelspace local var the contents from a pointer with userspace data that is not tagged with \__user.

    :param __x:
        var where data will be stored
    :type __x: 

    :param __ptr:
        var where data will be retrieved.
    :type __ptr: 

.. _`get_user_cast.description`:

Description
-----------

Sometimes we need to declare a pointer without \__user because it
comes from a pointer struct field that will be retrieved from userspace
by the 64-bit native ioctl handler. This function ensures that the
\ ``__ptr``\  will be cast to \__user before calling \ :c:func:`get_user`\  in order to
avoid warnings with static code analyzers like smatch.

.. _`put_user_force`:

put_user_force
==============

.. c:function::  put_user_force( __x,  __ptr)

    Stores the contents of a kernelspace local var into a userspace pointer, removing any \__user cast.

    :param __x:
        var where data will be stored
    :type __x: 

    :param __ptr:
        var where data will be retrieved.
    :type __ptr: 

.. _`put_user_force.description`:

Description
-----------

Sometimes we need to remove the \__user attribute from some data,
by passing the \__force macro. This function ensures that the
\ ``__ptr``\  will be cast with \__force before calling \ :c:func:`put_user`\ , in order to
avoid warnings with static code analyzers like smatch.

.. _`assign_in_user_cast`:

assign_in_user_cast
===================

.. c:function::  assign_in_user_cast( to,  from)

    Copy from one \__user var to another one

    :param to:
        \__user var where data will be stored
    :type to: 

    :param from:
        var where data will be retrieved that needs to be cast to \__user.
    :type from: 

.. _`assign_in_user_cast.description`:

Description
-----------

As this code very often needs to allocate userspace memory, it is easier
to have a macro that will do both \ :c:func:`get_user_cast`\  and \ :c:func:`put_user`\  at once.

This function should be used instead of \ :c:func:`assign_in_user`\  when the \ ``from``\ 
variable was not declared as \__user. See \ :c:func:`get_user_cast`\  for more details.

This function complements the macros defined at asm-generic/uaccess.h.
It uses the same argument order as \ :c:func:`copy_in_user`\ 

.. _`native_ioctl`:

native_ioctl
============

.. c:function:: long native_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Ancillary function that calls the native 64 bits ioctl handler.

    :param file:
        pointer to \ :c:type:`struct file <file>`\  with the file handler
    :type file: struct file \*

    :param cmd:
        ioctl to be called
    :type cmd: unsigned int

    :param arg:
        arguments passed from/to the ioctl handler
    :type arg: unsigned long

.. _`native_ioctl.description`:

Description
-----------

This function calls the native ioctl handler at v4l2-dev, e. g. \ :c:func:`v4l2_ioctl`\ 

.. _`v4l2_create_buffers32`:

struct v4l2_create_buffers32
============================

.. c:type:: struct v4l2_create_buffers32

    VIDIOC_CREATE_BUFS32 argument

.. _`v4l2_create_buffers32.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_create_buffers32 {
        __u32 index;
        __u32 count;
        __u32 memory;
        struct v4l2_format32 format;
        __u32 capabilities;
        __u32 reserved[7];
    }

.. _`v4l2_create_buffers32.members`:

Members
-------

index
    on return, index of the first created buffer

count
    entry: number of requested buffers,
    return: number of created buffers

memory
    buffer memory type

format
    frame format, for which buffers are requested

capabilities
    capabilities of this buffer type.

reserved
    future extensions

.. _`alloc_userspace`:

alloc_userspace
===============

.. c:function:: int alloc_userspace(unsigned int size, u32 aux_space, void __user **new_p64)

    Allocates a 64-bits userspace pointer compatible for calling the native 64-bits version of an ioctl.

    :param size:
        size of the structure itself to be allocated.
    :type size: unsigned int

    :param aux_space:
        extra size needed to store "extra" data, e.g. space for
        other \__user data that is pointed to fields inside the
        structure.
    :type aux_space: u32

    :param new_p64:
        pointer to a pointer to be filled with the allocated struct.
    :type new_p64: void __user \*\*

.. _`alloc_userspace.return`:

Return
------


if it can't allocate memory, either -ENOMEM or -EFAULT will be returned.
Zero otherwise.

.. _`do_video_ioctl`:

do_video_ioctl
==============

.. c:function:: long do_video_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Ancillary function with handles a compat32 ioctl call

    :param file:
        pointer to \ :c:type:`struct file <file>`\  with the file handler
    :type file: struct file \*

    :param cmd:
        ioctl to be called
    :type cmd: unsigned int

    :param arg:
        arguments passed from/to the ioctl handler
    :type arg: unsigned long

.. _`do_video_ioctl.description`:

Description
-----------

This function is called when a 32 bits application calls a V4L2 ioctl
and the Kernel is compiled with 64 bits.

This function is called by \ :c:func:`v4l2_compat_ioctl32`\  when the function is
not private to some specific driver.

It converts a 32-bits struct into a 64 bits one, calls the native 64-bits
ioctl handler and fills back the 32-bits struct with the results of the
native call.

.. _`v4l2_compat_ioctl32`:

v4l2_compat_ioctl32
===================

.. c:function:: long v4l2_compat_ioctl32(struct file *file, unsigned int cmd, unsigned long arg)

    Handles a compat32 ioctl call

    :param file:
        pointer to \ :c:type:`struct file <file>`\  with the file handler
    :type file: struct file \*

    :param cmd:
        ioctl to be called
    :type cmd: unsigned int

    :param arg:
        arguments passed from/to the ioctl handler
    :type arg: unsigned long

.. _`v4l2_compat_ioctl32.description`:

Description
-----------

This function is meant to be used as .compat_ioctl fops at v4l2-dev.c
in order to deal with 32-bit calls on a 64-bits Kernel.

This function calls \ :c:func:`do_video_ioctl`\  for non-private V4L2 ioctls.
If the function is a private one it calls vdev->fops->compat_ioctl32
instead.

.. This file was automatic generated / don't edit.

