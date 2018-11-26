.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/time.h

.. _`utc2ntfs`:

utc2ntfs
========

.. c:function:: sle64 utc2ntfs(const struct timespec64 ts)

    convert Linux UTC time to NTFS time

    :param ts:
        Linux UTC time to convert to NTFS time
    :type ts: const struct timespec64

.. _`utc2ntfs.description`:

Description
-----------

Convert the Linux UTC time \ ``ts``\  to its corresponding NTFS time and return
that in little endian format.

Linux stores time in a struct timespec64 consisting of a time64_t tv_sec
and a long tv_nsec where tv_sec is the number of 1-second intervals since
1st January 1970, 00:00:00 UTC and tv_nsec is the number of 1-nano-second
intervals since the value of tv_sec.

NTFS uses Microsoft's standard time format which is stored in a s64 and is
measured as the number of 100-nano-second intervals since 1st January 1601,
00:00:00 UTC.

.. _`get_current_ntfs_time`:

get_current_ntfs_time
=====================

.. c:function:: sle64 get_current_ntfs_time( void)

    get the current time in little endian NTFS format

    :param void:
        no arguments
    :type void: 

.. _`get_current_ntfs_time.description`:

Description
-----------

Get the current time from the Linux kernel, convert it to its corresponding
NTFS time and return that in little endian format.

.. _`ntfs2utc`:

ntfs2utc
========

.. c:function:: struct timespec64 ntfs2utc(const sle64 time)

    convert NTFS time to Linux time

    :param time:
        NTFS time (little endian) to convert to Linux UTC
    :type time: const sle64

.. _`ntfs2utc.description`:

Description
-----------

Convert the little endian NTFS time \ ``time``\  to its corresponding Linux UTC
time and return that in cpu format.

Linux stores time in a struct timespec64 consisting of a time64_t tv_sec
and a long tv_nsec where tv_sec is the number of 1-second intervals since
1st January 1970, 00:00:00 UTC and tv_nsec is the number of 1-nano-second
intervals since the value of tv_sec.

NTFS uses Microsoft's standard time format which is stored in a s64 and is
measured as the number of 100 nano-second intervals since 1st January 1601,
00:00:00 UTC.

.. This file was automatic generated / don't edit.

