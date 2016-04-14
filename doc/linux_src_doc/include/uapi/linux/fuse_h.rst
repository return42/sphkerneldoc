.. -*- coding: utf-8; mode: rst -*-

======
fuse.h
======

.. _`fattr_mode`:

FATTR_MODE
==========

.. c:function:: FATTR_MODE ()


.. _`fopen_direct_io`:

FOPEN_DIRECT_IO
===============

.. c:function:: FOPEN_DIRECT_IO ()


.. _`fopen_direct_io.description`:

Description
-----------


FOPEN_DIRECT_IO: bypass page cache for this open file
FOPEN_KEEP_CACHE: don't invalidate the data cache on open
FOPEN_NONSEEKABLE: the file is not seekable


.. _`fuse_async_read`:

FUSE_ASYNC_READ
===============

.. c:function:: FUSE_ASYNC_READ ()


.. _`fuse_async_read.description`:

Description
-----------


FUSE_ASYNC_READ: asynchronous read requests
FUSE_POSIX_LOCKS: remote locking for POSIX file locks
FUSE_FILE_OPS: kernel sends file handle for fstat, etc... (not yet supported)
FUSE_ATOMIC_O_TRUNC: handles the O_TRUNC open flag in the filesystem
FUSE_EXPORT_SUPPORT: filesystem handles lookups of "." and ".."
FUSE_BIG_WRITES: filesystem can handle write size larger than 4kB
FUSE_DONT_MASK: don't apply umask to file mode on create operations
FUSE_SPLICE_WRITE: kernel supports splice write on the device
FUSE_SPLICE_MOVE: kernel supports splice move on the device
FUSE_SPLICE_READ: kernel supports splice read on the device
FUSE_FLOCK_LOCKS: remote locking for BSD style file locks
FUSE_HAS_IOCTL_DIR: kernel supports ioctl on directories
FUSE_AUTO_INVAL_DATA: automatically invalidate cached pages
FUSE_DO_READDIRPLUS: do READDIRPLUS (READDIR+LOOKUP in one)
FUSE_READDIRPLUS_AUTO: adaptive readdirplus
FUSE_ASYNC_DIO: asynchronous direct I/O submission
FUSE_WRITEBACK_CACHE: use writeback cache for buffered writes
FUSE_NO_OPEN_SUPPORT: kernel supports zero-message opens


.. _`cuse_unrestricted_ioctl`:

CUSE_UNRESTRICTED_IOCTL
=======================

.. c:function:: CUSE_UNRESTRICTED_IOCTL ()


.. _`cuse_unrestricted_ioctl.description`:

Description
-----------


CUSE_UNRESTRICTED_IOCTL:  use unrestricted ioctl


.. _`fuse_release_flush`:

FUSE_RELEASE_FLUSH
==================

.. c:function:: FUSE_RELEASE_FLUSH ()


.. _`fuse_getattr_fh`:

FUSE_GETATTR_FH
===============

.. c:function:: FUSE_GETATTR_FH ()


.. _`fuse_lk_flock`:

FUSE_LK_FLOCK
=============

.. c:function:: FUSE_LK_FLOCK ()


.. _`fuse_write_cache`:

FUSE_WRITE_CACHE
================

.. c:function:: FUSE_WRITE_CACHE ()


.. _`fuse_write_cache.description`:

Description
-----------


FUSE_WRITE_CACHE: delayed write from page cache, file handle is guessed
FUSE_WRITE_LOCKOWNER: lock_owner field is valid


.. _`fuse_read_lockowner`:

FUSE_READ_LOCKOWNER
===================

.. c:function:: FUSE_READ_LOCKOWNER ()


.. _`fuse_ioctl_compat`:

FUSE_IOCTL_COMPAT
=================

.. c:function:: FUSE_IOCTL_COMPAT ()


.. _`fuse_ioctl_compat.description`:

Description
-----------


FUSE_IOCTL_COMPAT: 32bit compat ioctl on 64bit machine
FUSE_IOCTL_UNRESTRICTED: not restricted to well-formed ioctls, retry allowed
FUSE_IOCTL_RETRY: retry with new iovecs
FUSE_IOCTL_32BIT: 32bit ioctl
FUSE_IOCTL_DIR: is a directory

FUSE_IOCTL_MAX_IOV: maximum of in_iovecs + out_iovecs


.. _`fuse_poll_schedule_notify`:

FUSE_POLL_SCHEDULE_NOTIFY
=========================

.. c:function:: FUSE_POLL_SCHEDULE_NOTIFY ()


.. _`fuse_poll_schedule_notify.description`:

Description
-----------


FUSE_POLL_SCHEDULE_NOTIFY: request poll notify

