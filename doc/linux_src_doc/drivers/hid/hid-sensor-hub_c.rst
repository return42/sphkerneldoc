.. -*- coding: utf-8; mode: rst -*-

================
hid-sensor-hub.c
================


.. _`sensor_hub_data`:

struct sensor_hub_data
======================

.. c:type:: sensor_hub_data

    Hold a instance data for a HID hub device


.. _`sensor_hub_data.definition`:

Definition
----------

.. code-block:: c

  struct sensor_hub_data {
    struct mutex mutex;
    spinlock_t lock;
    struct list_head dyn_callback_list;
    spinlock_t dyn_callback_lock;
    struct mfd_cell * hid_sensor_hub_client_devs;
    int hid_sensor_client_cnt;
    int ref_cnt;
  };


.. _`sensor_hub_data.members`:

Members
-------

:``mutex``:
    Mutex to serialize synchronous request.

:``lock``:
    Spin lock to protect pending request structure.

:``dyn_callback_list``:
    Holds callback function

:``dyn_callback_lock``:
    spin lock to protect callback list

:``hid_sensor_hub_client_devs``:
    Stores all MFD cells for a hub instance.

:``hid_sensor_client_cnt``:
    Number of MFD cells, (no of sensors attached).

:``ref_cnt``:
    Number of MFD clients have opened this device




.. _`hid_sensor_hub_callbacks_list`:

struct hid_sensor_hub_callbacks_list
====================================

.. c:type:: hid_sensor_hub_callbacks_list

    Stores callback list


.. _`hid_sensor_hub_callbacks_list.definition`:

Definition
----------

.. code-block:: c

  struct hid_sensor_hub_callbacks_list {
    struct list_head list;
    u32 usage_id;
    struct hid_sensor_hub_callbacks * usage_callback;
    void * priv;
  };


.. _`hid_sensor_hub_callbacks_list.members`:

Members
-------

:``list``:
    list head.

:``usage_id``:
    usage id for a physical device.

:``usage_callback``:
    Stores registered callback functions.

:``priv``:
    Private data for a physical device.


