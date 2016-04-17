.. -*- coding: utf-8; mode: rst -*-

==============
notification.c
==============


.. _`fsnotify_get_cookie`:

fsnotify_get_cookie
===================

.. c:function:: u32 fsnotify_get_cookie ( void)

    return a unique cookie for use in synchronizing events. Called from fsnotify_move, which is inlined into filesystem modules.

    :param void:
        no arguments

