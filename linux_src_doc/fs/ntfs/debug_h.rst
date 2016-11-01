.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/debug.h

.. _`ntfs_debug`:

ntfs_debug
==========

.. c:function::  ntfs_debug( f,  a...)

    write a debug level message to syslog

    :param  f:
        a printf format string containing the message

    :param  a...:
        variable arguments

.. _`ntfs_debug.description`:

Description
-----------

ntfs_debug() writes a DEBUG level message to the syslog but only if the
driver was compiled with -DDEBUG. Otherwise, the call turns into a NOP.

.. This file was automatic generated / don't edit.

