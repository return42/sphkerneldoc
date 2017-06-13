.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/sync_file.h

.. _`sync_merge_data`:

struct sync_merge_data
======================

.. c:type:: struct sync_merge_data

    data passed to merge ioctl

.. _`sync_merge_data.definition`:

Definition
----------

.. code-block:: c

    struct sync_merge_data {
        char name;
        __s32 fd2;
        __s32 fence;
        __u32 flags;
        __u32 pad;
    }

.. _`sync_merge_data.members`:

Members
-------

name
    name of new fence

fd2
    file descriptor of second fence

fence
    returns the fd of the new fence to userspace

flags
    merge_data flags

pad
    padding for 64-bit alignment, should always be zero

.. _`sync_fence_info`:

struct sync_fence_info
======================

.. c:type:: struct sync_fence_info

    detailed fence information

.. _`sync_fence_info.definition`:

Definition
----------

.. code-block:: c

    struct sync_fence_info {
        char obj_name;
        char driver_name;
        __s32 status;
        __u32 flags;
        __u64 timestamp_ns;
    }

.. _`sync_fence_info.members`:

Members
-------

obj_name
    name of parent sync_timeline

driver_name
    name of driver implementing the parent

status
    status of the fence 0:active 1:signaled <0:error

flags
    fence_info flags

timestamp_ns
    timestamp of status change in nanoseconds

.. _`sync_file_info`:

struct sync_file_info
=====================

.. c:type:: struct sync_file_info

    data returned from fence info ioctl

.. _`sync_file_info.definition`:

Definition
----------

.. code-block:: c

    struct sync_file_info {
        char name;
        __s32 status;
        __u32 flags;
        __u32 num_fences;
        __u32 pad;
        __u64 sync_fence_info;
    }

.. _`sync_file_info.members`:

Members
-------

name
    name of fence

status
    status of fence. 1: signaled 0:active <0:error

flags
    sync_file_info flags
    \ ``num_fences``\   number of fences in the sync_file

num_fences
    *undescribed*

pad
    padding for 64-bit alignment, should always be zero

sync_fence_info
    pointer to array of structs sync_fence_info with all
    fences in the sync_file

.. _`sync_ioc_merge`:

SYNC_IOC_MERGE
==============

.. c:function::  SYNC_IOC_MERGE()

    old API to get weird errors when trying to handling sync_files. The API change happened during the de-stage of the Sync Framework when there was no upstream users available.

.. This file was automatic generated / don't edit.

