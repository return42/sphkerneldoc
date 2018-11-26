.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/closure.c

.. _`closure_wait`:

closure_wait
============

.. c:function:: bool closure_wait(struct closure_waitlist *waitlist, struct closure *cl)

    add a closure to a waitlist

    :param waitlist:
        will own a ref on \ ``cl``\ , which will be released when
        \ :c:func:`closure_wake_up`\  is called on \ ``waitlist``\ .
    :type waitlist: struct closure_waitlist \*

    :param cl:
        closure pointer.
    :type cl: struct closure \*

.. This file was automatic generated / don't edit.

