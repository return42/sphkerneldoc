.. -*- coding: utf-8; mode: rst -*-

===========
fb_notify.c
===========


.. _`fb_register_client`:

fb_register_client
==================

.. c:function:: int fb_register_client (struct notifier_block *nb)

    register a client notifier

    :param struct notifier_block \*nb:
        notifier block to callback on events



.. _`fb_unregister_client`:

fb_unregister_client
====================

.. c:function:: int fb_unregister_client (struct notifier_block *nb)

    unregister a client notifier

    :param struct notifier_block \*nb:
        notifier block to callback on events



.. _`fb_notifier_call_chain`:

fb_notifier_call_chain
======================

.. c:function:: int fb_notifier_call_chain (unsigned long val, void *v)

    notify clients of fb_events

    :param unsigned long val:

        *undescribed*

    :param void \*v:

        *undescribed*

