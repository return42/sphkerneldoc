.. -*- coding: utf-8; mode: rst -*-

====================
userspace-consumer.h
====================


.. _`regulator_userspace_consumer_data`:

struct regulator_userspace_consumer_data
========================================

.. c:type:: regulator_userspace_consumer_data

    line consumer initialisation data.


.. _`regulator_userspace_consumer_data.definition`:

Definition
----------

.. code-block:: c

  struct regulator_userspace_consumer_data {
    const char * name;
    int num_supplies;
    struct regulator_bulk_data * supplies;
    bool init_on;
  };


.. _`regulator_userspace_consumer_data.members`:

Members
-------

:``name``:
    Name for the consumer line

:``num_supplies``:
    Number of supplies feeding the line

:``supplies``:
    Supplies configuration.

:``init_on``:
    Set if the regulators supplying the line should be
    enabled during initialisation


