.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/async.c

.. _`async_schedule`:

async_schedule
==============

.. c:function:: async_cookie_t async_schedule(async_func_t func, void *data)

    schedule a function for asynchronous execution

    :param async_func_t func:
        function to execute asynchronously

    :param void \*data:
        data pointer to pass to the function

.. _`async_schedule.description`:

Description
-----------

Returns an async_cookie_t that may be used for checkpointing later.

.. _`async_schedule.note`:

Note
----

This function may be called from atomic or non-atomic contexts.

.. _`async_schedule_domain`:

async_schedule_domain
=====================

.. c:function:: async_cookie_t async_schedule_domain(async_func_t func, void *data, struct async_domain *domain)

    schedule a function for asynchronous execution within a certain domain

    :param async_func_t func:
        function to execute asynchronously

    :param void \*data:
        data pointer to pass to the function

    :param struct async_domain \*domain:
        the domain

.. _`async_schedule_domain.description`:

Description
-----------

Returns an async_cookie_t that may be used for checkpointing later.
\ ``domain``\  may be used in the async_synchronize\_\*\_domain() functions to
wait within a certain synchronization domain rather than globally.  A
synchronization domain is specified via \ ``domain``\ .  Note: This function
may be called from atomic or non-atomic contexts.

.. _`async_synchronize_full`:

async_synchronize_full
======================

.. c:function:: void async_synchronize_full( void)

    synchronize all asynchronous function calls

    :param  void:
        no arguments

.. _`async_synchronize_full.description`:

Description
-----------

This function waits until all asynchronous function calls have been done.

.. _`async_unregister_domain`:

async_unregister_domain
=======================

.. c:function:: void async_unregister_domain(struct async_domain *domain)

    ensure no more anonymous waiters on this domain

    :param struct async_domain \*domain:
        idle domain to flush out of any async_synchronize_full instances

.. _`async_unregister_domain.description`:

Description
-----------

async_synchronize_{cookie\|full}_domain() are not flushed since callers
of these routines should know the lifetime of \ ``domain``\ 

Prefer \ :c:func:`ASYNC_DOMAIN_EXCLUSIVE`\  declarations over flushing

.. _`async_synchronize_full_domain`:

async_synchronize_full_domain
=============================

.. c:function:: void async_synchronize_full_domain(struct async_domain *domain)

    synchronize all asynchronous function within a certain domain

    :param struct async_domain \*domain:
        the domain to synchronize

.. _`async_synchronize_full_domain.description`:

Description
-----------

This function waits until all asynchronous function calls for the
synchronization domain specified by \ ``domain``\  have been done.

.. _`async_synchronize_cookie_domain`:

async_synchronize_cookie_domain
===============================

.. c:function:: void async_synchronize_cookie_domain(async_cookie_t cookie, struct async_domain *domain)

    synchronize asynchronous function calls within a certain domain with cookie checkpointing

    :param async_cookie_t cookie:
        async_cookie_t to use as checkpoint

    :param struct async_domain \*domain:
        the domain to synchronize (%NULL for all registered domains)

.. _`async_synchronize_cookie_domain.description`:

Description
-----------

This function waits until all asynchronous function calls for the
synchronization domain specified by \ ``domain``\  submitted prior to \ ``cookie``\ 
have been done.

.. _`async_synchronize_cookie`:

async_synchronize_cookie
========================

.. c:function:: void async_synchronize_cookie(async_cookie_t cookie)

    synchronize asynchronous function calls with cookie checkpointing

    :param async_cookie_t cookie:
        async_cookie_t to use as checkpoint

.. _`async_synchronize_cookie.description`:

Description
-----------

This function waits until all asynchronous function calls prior to \ ``cookie``\ 
have been done.

.. _`current_is_async`:

current_is_async
================

.. c:function:: bool current_is_async( void)

    is \ ``current``\  an async worker task?

    :param  void:
        no arguments

.. _`current_is_async.description`:

Description
-----------

Returns \ ``true``\  if \ ``current``\  is an async worker task.

.. This file was automatic generated / don't edit.

