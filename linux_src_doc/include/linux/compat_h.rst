.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/compat.h

.. _`ns_to_compat_timeval`:

ns_to_compat_timeval
====================

.. c:function:: struct compat_timeval ns_to_compat_timeval(s64 nsec)

    Compat version of ns_to_timeval

    :param s64 nsec:
        the nanoseconds value to be converted

.. _`ns_to_compat_timeval.description`:

Description
-----------

Returns the compat_timeval representation of the nsec parameter.

.. This file was automatic generated / don't edit.

