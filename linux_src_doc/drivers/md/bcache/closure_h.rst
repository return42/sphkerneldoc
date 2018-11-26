.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/closure.h

.. _`closure_sync`:

closure_sync
============

.. c:function:: void closure_sync(struct closure *cl)

    sleep until a closure a closure has nothing left to wait on

    :param cl:
        *undescribed*
    :type cl: struct closure \*

.. _`closure_sync.description`:

Description
-----------

Sleeps until the refcount hits 1 - the thread that's running the closure owns
the last refcount.

.. _`closure_get`:

closure_get
===========

.. c:function:: void closure_get(struct closure *cl)

    increment a closure's refcount

    :param cl:
        *undescribed*
    :type cl: struct closure \*

.. _`closure_init`:

closure_init
============

.. c:function:: void closure_init(struct closure *cl, struct closure *parent)

    Initialize a closure, setting the refcount to 1

    :param cl:
        closure to initialize
    :type cl: struct closure \*

    :param parent:
        parent of the new closure. cl will take a refcount on it for its
        lifetime; may be NULL.
    :type parent: struct closure \*

.. _`closure_wake_up`:

closure_wake_up
===============

.. c:function:: void closure_wake_up(struct closure_waitlist *list)

    wake up all closures on a wait list, with memory barrier

    :param list:
        *undescribed*
    :type list: struct closure_waitlist \*

.. _`continue_at`:

continue_at
===========

.. c:function::  continue_at( _cl,  _fn,  _wq)

    jump to another function with barrier

    :param _cl:
        *undescribed*
    :type _cl: 

    :param _fn:
        *undescribed*
    :type _fn: 

    :param _wq:
        *undescribed*
    :type _wq: 

.. _`continue_at.description`:

Description
-----------

After \ ``cl``\  is no longer waiting on anything (i.e. all outstanding refs have
been dropped with \ :c:func:`closure_put`\ ), it will resume execution at \ ``fn``\  running out
of \ ``wq``\  (or, if \ ``wq``\  is NULL, \ ``fn``\  will be called by \ :c:func:`closure_put`\  directly).

This is because after calling \ :c:func:`continue_at`\  you no longer have a ref on \ ``cl``\ ,
and whatever \ ``cl``\  owns may be freed out from under you - a running closure fn
has a ref on its own closure which \ :c:func:`continue_at`\  drops.

Note you are expected to immediately return after using this macro.

.. _`closure_return`:

closure_return
==============

.. c:function::  closure_return( _cl)

    finish execution of a closure

    :param _cl:
        *undescribed*
    :type _cl: 

.. _`closure_return.description`:

Description
-----------

This is used to indicate that \ ``cl``\  is finished: when all outstanding refs on
\ ``cl``\  have been dropped \ ``cl``\ 's ref on its parent closure (as passed to
\ :c:func:`closure_init`\ ) will be dropped, if one was specified - thus this can be
thought of as returning to the parent closure.

.. _`continue_at_nobarrier`:

continue_at_nobarrier
=====================

.. c:function::  continue_at_nobarrier( _cl,  _fn,  _wq)

    jump to another function without barrier

    :param _cl:
        *undescribed*
    :type _cl: 

    :param _fn:
        *undescribed*
    :type _fn: 

    :param _wq:
        *undescribed*
    :type _wq: 

.. _`continue_at_nobarrier.description`:

Description
-----------

Causes \ ``fn``\  to be executed out of \ ``cl``\ , in \ ``wq``\  context (or called directly if
\ ``wq``\  is NULL).

The ref the caller of \ :c:func:`continue_at_nobarrier`\  had on \ ``cl``\  is now owned by \ ``fn``\ ,
thus it's not safe to touch anything protected by \ ``cl``\  after a
\ :c:func:`continue_at_nobarrier`\ .

.. _`closure_return_with_destructor`:

closure_return_with_destructor
==============================

.. c:function::  closure_return_with_destructor( _cl,  _destructor)

    finish execution of a closure, with destructor

    :param _cl:
        *undescribed*
    :type _cl: 

    :param _destructor:
        *undescribed*
    :type _destructor: 

.. _`closure_return_with_destructor.description`:

Description
-----------

Works like \ :c:func:`closure_return`\ , except \ ``destructor``\  will be called when all
outstanding refs on \ ``cl``\  have been dropped; \ ``destructor``\  may be used to safely
free the memory occupied by \ ``cl``\ , and it is called with the ref on the parent
closure still held - so \ ``destructor``\  could safely return an item to a
freelist protected by \ ``cl``\ 's parent.

.. _`closure_call`:

closure_call
============

.. c:function:: void closure_call(struct closure *cl, closure_fn fn, struct workqueue_struct *wq, struct closure *parent)

    execute \ ``fn``\  out of a new, uninitialized closure

    :param cl:
        *undescribed*
    :type cl: struct closure \*

    :param fn:
        *undescribed*
    :type fn: closure_fn

    :param wq:
        *undescribed*
    :type wq: struct workqueue_struct \*

    :param parent:
        *undescribed*
    :type parent: struct closure \*

.. _`closure_call.description`:

Description
-----------

Typically used when running out of one closure, and we want to run \ ``fn``\ 
asynchronously out of a new closure - \ ``parent``\  will then wait for \ ``cl``\  to
finish.

.. This file was automatic generated / don't edit.

