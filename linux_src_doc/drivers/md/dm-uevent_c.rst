.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/dm-uevent.c

.. _`dm_send_uevents`:

dm_send_uevents
===============

.. c:function:: void dm_send_uevents(struct list_head *events, struct kobject *kobj)

    send uevents for given list

    :param events:
        list of events to send
    :type events: struct list_head \*

    :param kobj:
        kobject generating event
    :type kobj: struct kobject \*

.. _`dm_path_uevent`:

dm_path_uevent
==============

.. c:function:: void dm_path_uevent(enum dm_uevent_type event_type, struct dm_target *ti, const char *path, unsigned nr_valid_paths)

    called to create a new path event and queue it

    :param event_type:
        path event type enum
    :type event_type: enum dm_uevent_type

    :param ti:
        pointer to a dm_target
    :type ti: struct dm_target \*

    :param path:
        string containing pathname
    :type path: const char \*

    :param nr_valid_paths:
        number of valid paths remaining
    :type nr_valid_paths: unsigned

.. This file was automatic generated / don't edit.

