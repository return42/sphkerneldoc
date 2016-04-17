.. -*- coding: utf-8; mode: rst -*-

========
notify.c
========


.. _`usb_register_notify`:

usb_register_notify
===================

.. c:function:: void usb_register_notify (struct notifier_block *nb)

    register a notifier callback whenever a usb change happens

    :param struct notifier_block \*nb:
        pointer to the notifier block for the callback events.



.. _`usb_register_notify.description`:

Description
-----------

These changes are either USB devices or busses being added or removed.



.. _`usb_unregister_notify`:

usb_unregister_notify
=====================

.. c:function:: void usb_unregister_notify (struct notifier_block *nb)

    unregister a notifier callback

    :param struct notifier_block \*nb:
        pointer to the notifier block for the callback events.



.. _`usb_unregister_notify.description`:

Description
-----------

:c:func:`usb_register_notify` must have been previously called for this function
to work properly.

