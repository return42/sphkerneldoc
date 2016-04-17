.. -*- coding: utf-8; mode: rst -*-

========
select.c
========


.. _`poll_select_set_timeout`:

poll_select_set_timeout
=======================

.. c:function:: int poll_select_set_timeout (struct timespec *to, long sec, long nsec)

    helper function to setup the timeout value

    :param struct timespec \*to:
        pointer to timespec variable for the final timeout

    :param long sec:
        seconds (from user space)

    :param long nsec:
        nanoseconds (from user space)



.. _`poll_select_set_timeout.description`:

Description
-----------

Note, we do not use a timespec for the user space value here, That
way we can use the function for timeval and compat interfaces as well.

Returns -EINVAL if sec/nsec are not normalized. Otherwise 0.

