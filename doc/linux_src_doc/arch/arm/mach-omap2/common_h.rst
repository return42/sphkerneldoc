.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/common.h

.. _`omap_test_timeout`:

omap_test_timeout
=================

.. c:function::  omap_test_timeout( cond,  timeout,  index)

    busy-loop, testing a condition

    :param  cond:
        condition to test until it evaluates to true

    :param  timeout:
        maximum number of microseconds in the timeout

    :param  index:
        loop index (integer)

.. _`omap_test_timeout.description`:

Description
-----------

Loop waiting for \ ``cond``\  to become true or until at least \ ``timeout``\ 
microseconds have passed.  To use, define some integer \ ``index``\  in the
calling code.  After running, if \ ``index``\  == \ ``timeout``\ , then the loop has
timed out.

.. This file was automatic generated / don't edit.

