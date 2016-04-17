.. -*- coding: utf-8; mode: rst -*-

===========
knav_qmss.h
===========


.. _`knav_queue_ctrl_cmd`:

enum knav_queue_ctrl_cmd
========================

.. c:type:: knav_queue_ctrl_cmd

    queue operations.


.. _`knav_queue_ctrl_cmd.definition`:

Definition
----------

.. code-block:: c

    enum knav_queue_ctrl_cmd {
      KNAV_QUEUE_GET_ID,
      KNAV_QUEUE_FLUSH,
      KNAV_QUEUE_SET_NOTIFIER,
      KNAV_QUEUE_ENABLE_NOTIFY,
      KNAV_QUEUE_DISABLE_NOTIFY,
      KNAV_QUEUE_GET_COUNT
    };


.. _`knav_queue_ctrl_cmd.constants`:

Constants
---------

:``KNAV_QUEUE_GET_ID``:
    Get the ID number for an open queue

:``KNAV_QUEUE_FLUSH``:
    forcibly empty a queue if possible

:``KNAV_QUEUE_SET_NOTIFIER``:
    Set a notifier callback to a queue handle.

:``KNAV_QUEUE_ENABLE_NOTIFY``:
    Enable notifier callback for a queue handle.

:``KNAV_QUEUE_DISABLE_NOTIFY``:
    Disable notifier callback for a queue handle.

:``KNAV_QUEUE_GET_COUNT``:
    Get number of queues.


.. _`knav_queue_notify_config`:

struct knav_queue_notify_config
===============================

.. c:type:: knav_queue_notify_config

    


.. _`knav_queue_notify_config.definition`:

Definition
----------

.. code-block:: c

  struct knav_queue_notify_config {
    knav_queue_notify_fn fn;
    void * fn_arg;
  };


.. _`knav_queue_notify_config.members`:

Members
-------

:``fn``:
    Notifier function

:``fn_arg``:
    Notifier function arguments


