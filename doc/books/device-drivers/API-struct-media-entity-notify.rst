
.. _API-struct-media-entity-notify:

==========================
struct media_entity_notify
==========================

*man struct media_entity_notify(9)*

*4.6.0-rc1*

Media Entity Notify


Synopsis
========

.. code-block:: c

    struct media_entity_notify {
      struct list_head list;
      void * notify_data;
      void (* notify) (struct media_entity *entity, void *notify_data);
    };


Members
=======

list
    List head

notify_data
    Input data to invoke the callback

notify
    Callback function pointer


Description
===========

Drivers may register a callback to take action when new entities get registered with the media device.
