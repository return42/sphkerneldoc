.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/timeconv.c

.. _`time64_to_tm`:

time64_to_tm
============

.. c:function:: void time64_to_tm(time64_t totalsecs, int offset, struct tm *result)

    converts the calendar time to local broken-down time

    :param time64_t totalsecs:
        00:00 on January 1, 1970,
        Coordinated Universal Time (UTC).
        \ ``offset``\       offset seconds adding to totalsecs.
        \ ``result``\       pointer to struct tm variable to receive broken-down time

    :param int offset:
        *undescribed*

    :param struct tm \*result:
        *undescribed*

.. This file was automatic generated / don't edit.

