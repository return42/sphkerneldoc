.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/compat.h

.. _`ns_to_old_timeval32`:

ns_to_old_timeval32
===================

.. c:function:: struct old_timeval32 ns_to_old_timeval32(s64 nsec)

    Compat version of ns_to_timeval

    :param nsec:
        the nanoseconds value to be converted
    :type nsec: s64

.. _`ns_to_old_timeval32.description`:

Description
-----------

Returns the old_timeval32 representation of the nsec parameter.

.. This file was automatic generated / don't edit.

