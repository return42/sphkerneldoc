.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iopoll.h

.. _`readx_poll_timeout`:

readx_poll_timeout
==================

.. c:function::  readx_poll_timeout( op,  addr,  val,  cond,  sleep_us,  timeout_us)

    Periodically poll an address until a condition is met or a timeout occurs

    :param op:
        accessor function (takes \ ``addr``\  as its only argument)
    :type op: 

    :param addr:
        Address to poll
    :type addr: 

    :param val:
        Variable to read the value into
    :type val: 

    :param cond:
        Break condition (usually involving \ ``val``\ )
    :type cond: 

    :param sleep_us:
        Maximum time to sleep between reads in us (0
        tight-loops).  Should be less than ~20ms since usleep_range
        is used (see Documentation/timers/timers-howto.txt).
    :type sleep_us: 

    :param timeout_us:
        Timeout in us, 0 means never timeout
    :type timeout_us: 

.. _`readx_poll_timeout.description`:

Description
-----------

Returns 0 on success and -ETIMEDOUT upon a timeout. In either
case, the last read value at \ ``addr``\  is stored in \ ``val``\ . Must not
be called from atomic context if sleep_us or timeout_us are used.

When available, you'll probably want to use one of the specialized
macros defined below rather than this macro directly.

.. _`readx_poll_timeout_atomic`:

readx_poll_timeout_atomic
=========================

.. c:function::  readx_poll_timeout_atomic( op,  addr,  val,  cond,  delay_us,  timeout_us)

    Periodically poll an address until a condition is met or a timeout occurs

    :param op:
        accessor function (takes \ ``addr``\  as its only argument)
    :type op: 

    :param addr:
        Address to poll
    :type addr: 

    :param val:
        Variable to read the value into
    :type val: 

    :param cond:
        Break condition (usually involving \ ``val``\ )
    :type cond: 

    :param delay_us:
        Time to udelay between reads in us (0 tight-loops).  Should
        be less than ~10us since udelay is used (see
        Documentation/timers/timers-howto.txt).
    :type delay_us: 

    :param timeout_us:
        Timeout in us, 0 means never timeout
    :type timeout_us: 

.. _`readx_poll_timeout_atomic.description`:

Description
-----------

Returns 0 on success and -ETIMEDOUT upon a timeout. In either
case, the last read value at \ ``addr``\  is stored in \ ``val``\ .

When available, you'll probably want to use one of the specialized
macros defined below rather than this macro directly.

.. This file was automatic generated / don't edit.

