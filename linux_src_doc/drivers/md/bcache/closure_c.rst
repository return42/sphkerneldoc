.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/closure.c

.. _`closure_put`:

closure_put
===========

.. c:function:: void closure_put(struct closure *cl)

    decrement a closure's refcount

    :param struct closure \*cl:
        *undescribed*

.. _`__closure_wake_up`:

__closure_wake_up
=================

.. c:function:: void __closure_wake_up(struct closure_waitlist *wait_list)

    wake up all closures on a wait list, without memory barrier

    :param struct closure_waitlist \*wait_list:
        *undescribed*

.. _`closure_wait`:

closure_wait
============

.. c:function:: bool closure_wait(struct closure_waitlist *waitlist, struct closure *cl)

    add a closure to a waitlist

    :param struct closure_waitlist \*waitlist:
        *undescribed*

    :param struct closure \*cl:
        *undescribed*

.. _`closure_wait.description`:

Description
-----------

@waitlist will own a ref on \ ``cl``\ , which will be released when
\ :c:func:`closure_wake_up`\  is called on \ ``waitlist``\ .

.. _`closure_sync`:

closure_sync
============

.. c:function:: void closure_sync(struct closure *cl)

    sleep until a closure has nothing left to wait on

    :param struct closure \*cl:
        *undescribed*

.. _`closure_sync.description`:

Description
-----------

Sleeps until the refcount hits 1 - the thread that's running the closure owns
the last refcount.

.. This file was automatic generated / don't edit.

