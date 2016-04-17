.. -*- coding: utf-8; mode: rst -*-

===========
dm-uevent.c
===========


.. _`dm_send_uevents`:

dm_send_uevents
===============

.. c:function:: void dm_send_uevents (struct list_head *events, struct kobject *kobj)

    send uevents for given list

    :param struct list_head \*events:
        list of events to send

    :param struct kobject \*kobj:
        kobject generating event



.. _`dm_path_uevent`:

dm_path_uevent
==============

.. c:function:: void dm_path_uevent (enum dm_uevent_type event_type, struct dm_target *ti, const char *path, unsigned nr_valid_paths)

    called to create a new path event and queue it

    :param enum dm_uevent_type event_type:
        path event type enum

    :param struct dm_target \*ti:
        pointer to a dm_target

    :param const char \*path:
        string containing pathname

    :param unsigned nr_valid_paths:
        number of valid paths remaining

