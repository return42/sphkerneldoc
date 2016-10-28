.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/closure.h

.. _`closure_get`:

closure_get
===========

.. c:function:: void closure_get(struct closure *cl)

    increment a closure's refcount

    :param struct closure \*cl:
        *undescribed*

.. _`closure_init`:

closure_init
============

.. c:function:: void closure_init(struct closure *cl, struct closure *parent)

    Initialize a closure, setting the refcount to 1

    :param struct closure \*cl:
        closure to initialize

    :param struct closure \*parent:
        parent of the new closure. cl will take a refcount on it for its
        lifetime; may be NULL.

.. _`closure_wake_up`:

closure_wake_up
===============

.. c:function:: void closure_wake_up(struct closure_waitlist *list)

    wake up all closures on a wait list.

    :param struct closure_waitlist \*list:
        *undescribed*

.. _`continue_at`:

continue_at
===========

.. c:function::  continue_at( _cl,  _fn,  _wq)

    jump to another function with barrier

    :param  _cl:
        *undescribed*

    :param  _fn:
        *undescribed*

    :param  _wq:
        *undescribed*

.. _`continue_at.description`:

Description
-----------

After \ ``cl``\  is no longer waiting on anything (i.e. all outstanding refs have
been dropped with \ :c:func:`closure_put`\ ), it will resume execution at \ ``fn``\  running out
of \ ``wq``\  (or, if \ ``wq``\  is NULL, \ ``fn``\  will be called by \ :c:func:`closure_put`\  directly).

.. _`continue_at.note`:

NOTE
----

This macro expands to a return in the calling function!

This is because after calling \ :c:func:`continue_at`\  you no longer have a ref on \ ``cl``\ ,
and whatever \ ``cl``\  owns may be freed out from under you - a running closure fn
has a ref on its own closure which \ :c:func:`continue_at`\  drops.

.. _`closure_return`:

closure_return
==============

.. c:function::  closure_return( _cl)

    finish execution of a closure

    :param  _cl:
        *undescribed*

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

    :param  _cl:
        *undescribed*

    :param  _fn:
        *undescribed*

    :param  _wq:
        *undescribed*

.. _`continue_at_nobarrier.description`:

Description
-----------

Causes \ ``fn``\  to be executed out of \ ``cl``\ , in \ ``wq``\  context (or called directly if
\ ``wq``\  is NULL).

.. _`continue_at_nobarrier.note`:

NOTE
----

like \ :c:func:`continue_at`\ , this macro expands to a return in the caller!

The ref the caller of \ :c:func:`continue_at_nobarrier`\  had on \ ``cl``\  is now owned by \ ``fn``\ ,
thus it's not safe to touch anything protected by \ ``cl``\  after a
\ :c:func:`continue_at_nobarrier`\ .

.. _`closure_return_with_destructor`:

closure_return_with_destructor
==============================

.. c:function::  closure_return_with_destructor( _cl,  _destructor)

    finish execution of a closure, with destructor

    :param  _cl:
        *undescribed*

    :param  _destructor:
        *undescribed*

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

    :param struct closure \*cl:
        *undescribed*

    :param closure_fn fn:
        *undescribed*

    :param struct workqueue_struct \*wq:
        *undescribed*

    :param struct closure \*parent:
        *undescribed*

.. _`closure_call.description`:

Description
-----------

Typically used when running out of one closure, and we want to run \ ``fn``\ 
asynchronously out of a new closure - \ ``parent``\  will then wait for \ ``cl``\  to
finish.

.. This file was automatic generated / don't edit.

