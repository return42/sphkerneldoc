.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/android/binder.h

.. _`binder_object_header`:

struct binder_object_header
===========================

.. c:type:: struct binder_object_header

    header shared by all binder metadata objects.

.. _`binder_object_header.definition`:

Definition
----------

.. code-block:: c

    struct binder_object_header {
        __u32 type;
    }

.. _`binder_object_header.members`:

Members
-------

type
    type of the object

.. _`binder_fd_object`:

struct binder_fd_object
=======================

.. c:type:: struct binder_fd_object

    describes a filedescriptor to be fixed up.

.. _`binder_fd_object.definition`:

Definition
----------

.. code-block:: c

    struct binder_fd_object {
        struct binder_object_header hdr;
        __u32 pad_flags;
        union {
            binder_uintptr_t pad_binder;
            __u32 fd;
        } ;
        binder_uintptr_t cookie;
    }

.. _`binder_fd_object.members`:

Members
-------

hdr
    common header structure

pad_flags
    padding to remain compatible with old userspace code

{unnamed_union}
    anonymous

pad_binder
    padding to remain compatible with old userspace code

fd
    file descriptor

cookie
    opaque data, used by user-space

.. This file was automatic generated / don't edit.

