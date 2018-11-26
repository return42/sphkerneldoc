.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fscache/object.c

.. _`fscache_object_init`:

fscache_object_init
===================

.. c:function:: void fscache_object_init(struct fscache_object *object, struct fscache_cookie *cookie, struct fscache_cache *cache)

    Initialise a cache object description

    :param object:
        Object description
    :type object: struct fscache_object \*

    :param cookie:
        Cookie object will be attached to
    :type cookie: struct fscache_cookie \*

    :param cache:
        Cache in which backing object will be found
    :type cache: struct fscache_cache \*

.. _`fscache_object_init.description`:

Description
-----------

Initialise a cache object description to its basic values.

See Documentation/filesystems/caching/backend-api.txt for a complete
description.

.. _`fscache_object_lookup_negative`:

fscache_object_lookup_negative
==============================

.. c:function:: void fscache_object_lookup_negative(struct fscache_object *object)

    Note negative cookie lookup

    :param object:
        Object pointing to cookie to mark
    :type object: struct fscache_object \*

.. _`fscache_object_lookup_negative.description`:

Description
-----------

Note negative lookup, permitting those waiting to read data from an already
existing backing object to continue as there's no data for them to read.

.. _`fscache_obtained_object`:

fscache_obtained_object
=======================

.. c:function:: void fscache_obtained_object(struct fscache_object *object)

    Note successful object lookup or creation

    :param object:
        Object pointing to cookie to mark
    :type object: struct fscache_object \*

.. _`fscache_obtained_object.description`:

Description
-----------

Note successful lookup and/or creation, permitting those waiting to write
data to a backing object to continue.

Note that after calling this, an object's cookie may be relinquished by the
netfs, and so must be accessed with object lock held.

.. _`fscache_object_destroy`:

fscache_object_destroy
======================

.. c:function:: void fscache_object_destroy(struct fscache_object *object)

    Note that a cache object is about to be destroyed

    :param object:
        The object to be destroyed
    :type object: struct fscache_object \*

.. _`fscache_object_destroy.description`:

Description
-----------

Note the imminent destruction and deallocation of a cache object record.

.. _`fscache_object_sleep_till_congested`:

fscache_object_sleep_till_congested
===================================

.. c:function:: bool fscache_object_sleep_till_congested(signed long *timeoutp)

    Sleep until object wq is congested

    :param timeoutp:
        Scheduler sleep timeout
    :type timeoutp: signed long \*

.. _`fscache_object_sleep_till_congested.description`:

Description
-----------

Allow an object handler to sleep until the object workqueue is congested.

The caller must set up a wake up event before calling this and must have set
the appropriate sleep mode (such as TASK_UNINTERRUPTIBLE) and tested its own
condition before calling this function as no test is made here.

\ ``true``\  is returned if the object wq is congested, \ ``false``\  otherwise.

.. _`fscache_check_aux`:

fscache_check_aux
=================

.. c:function:: enum fscache_checkaux fscache_check_aux(struct fscache_object *object, const void *data, uint16_t datalen, loff_t object_size)

    Ask the netfs whether an object on disk is still valid

    :param object:
        The object to ask about
    :type object: struct fscache_object \*

    :param data:
        The auxiliary data for the object
    :type data: const void \*

    :param datalen:
        The size of the auxiliary data
    :type datalen: uint16_t

    :param object_size:
        *undescribed*
    :type object_size: loff_t

.. _`fscache_check_aux.description`:

Description
-----------

This function consults the netfs about the coherency state of an object.
The caller must be holding a ref on cookie->n_active (held by
\ :c:func:`fscache_look_up_object`\  on behalf of the cache backend during object lookup
and creation).

.. _`fscache_object_retrying_stale`:

fscache_object_retrying_stale
=============================

.. c:function:: void fscache_object_retrying_stale(struct fscache_object *object)

    Note retrying stale object

    :param object:
        The object that will be retried
    :type object: struct fscache_object \*

.. _`fscache_object_retrying_stale.description`:

Description
-----------

Note that an object lookup found an on-disk object that was adjudged to be
stale and has been deleted.  The lookup will be retried.

.. _`fscache_object_mark_killed`:

fscache_object_mark_killed
==========================

.. c:function:: void fscache_object_mark_killed(struct fscache_object *object, enum fscache_why_object_killed why)

    Note that an object was killed

    :param object:
        The object that was culled
    :type object: struct fscache_object \*

    :param why:
        The reason the object was killed.
    :type why: enum fscache_why_object_killed

.. _`fscache_object_mark_killed.description`:

Description
-----------

Note that an object was killed.  Returns true if the object was
already marked killed, false if it wasn't.

.. This file was automatic generated / don't edit.

