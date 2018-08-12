.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/closure.c

.. _`closure_wait`:

closure_wait
============

.. c:function:: bool closure_wait(struct closure_waitlist *waitlist, struct closure *cl)

    add a closure to a waitlist

    :param struct closure_waitlist \*waitlist:
        will own a ref on \ ``cl``\ , which will be released when
        \ :c:func:`closure_wake_up`\  is called on \ ``waitlist``\ .

    :param struct closure \*cl:
        closure pointer.

.. This file was automatic generated / don't edit.

