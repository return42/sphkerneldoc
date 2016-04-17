.. -*- coding: utf-8; mode: rst -*-

=====
mcb.h
=====


.. _`mcb_bus`:

struct mcb_bus
==============

.. c:type:: mcb_bus

    MEN Chameleon Bus


.. _`mcb_bus.definition`:

Definition
----------

.. code-block:: c

  struct mcb_bus {
    struct list_head children;
    struct device dev;
    int bus_nr;
    int (* get_irq) (struct mcb_device *dev);
  };


.. _`mcb_bus.members`:

Members
-------

:``children``:
    the child busses

:``dev``:
    pointer to carrier device

:``bus_nr``:
    mcb bus number

:``get_irq``:
    callback to get IRQ number




.. _`mcb_device`:

struct mcb_device
=================

.. c:type:: mcb_device

    MEN Chameleon Bus device


.. _`mcb_device.definition`:

Definition
----------

.. code-block:: c

  struct mcb_device {
    struct list_head bus_list;
    struct device dev;
    struct mcb_bus * bus;
    struct mcb_bus * subordinate;
    bool is_added;
    struct mcb_driver * driver;
    u16 id;
    int inst;
    int group;
    int var;
    int bar;
    int rev;
    struct resource irq;
  };


.. _`mcb_device.members`:

Members
-------

:``bus_list``:
    internal list handling for bus code

:``dev``:
    device in kernel representation

:``bus``:
    mcb bus the device is plugged to

:``subordinate``:
    subordinate MCBus in case of bridge

:``is_added``:
    flag to check if device is added to bus

:``driver``:
    associated mcb_driver

:``id``:
    mcb device id

:``inst``:
    instance in Chameleon table

:``group``:
    group in Chameleon table

:``var``:
    variant in Chameleon table

:``bar``:
    BAR in Chameleon table

:``rev``:
    revision in Chameleon table

:``irq``:
    IRQ resource




.. _`mcb_driver`:

struct mcb_driver
=================

.. c:type:: mcb_driver

    MEN Chameleon Bus device driver


.. _`mcb_driver.definition`:

Definition
----------

.. code-block:: c

  struct mcb_driver {
    struct device_driver driver;
    const struct mcb_device_id * id_table;
    int (* probe) (struct mcb_device *mdev, const struct mcb_device_id *id);
    void (* remove) (struct mcb_device *mdev);
    void (* shutdown) (struct mcb_device *mdev);
  };


.. _`mcb_driver.members`:

Members
-------

:``driver``:
    device_driver

:``id_table``:
    mcb id table

:``probe``:
    probe callback

:``remove``:
    remove callback

:``shutdown``:
    shutdown callback


