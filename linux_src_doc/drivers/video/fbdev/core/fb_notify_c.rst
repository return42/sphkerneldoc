.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fb_notify.c

.. _`fb_register_client`:

fb_register_client
==================

.. c:function:: int fb_register_client(struct notifier_block *nb)

    register a client notifier

    :param nb:
        notifier block to callback on events
    :type nb: struct notifier_block \*

.. _`fb_unregister_client`:

fb_unregister_client
====================

.. c:function:: int fb_unregister_client(struct notifier_block *nb)

    unregister a client notifier

    :param nb:
        notifier block to callback on events
    :type nb: struct notifier_block \*

.. _`fb_notifier_call_chain`:

fb_notifier_call_chain
======================

.. c:function:: int fb_notifier_call_chain(unsigned long val, void *v)

    notify clients of fb_events

    :param val:
        *undescribed*
    :type val: unsigned long

    :param v:
        *undescribed*
    :type v: void \*

.. This file was automatic generated / don't edit.

