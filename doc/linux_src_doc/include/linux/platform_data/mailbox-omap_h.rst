.. -*- coding: utf-8; mode: rst -*-

==============
mailbox-omap.h
==============


.. _`omap_mbox_dev_info`:

struct omap_mbox_dev_info
=========================

.. c:type:: omap_mbox_dev_info

    OMAP mailbox device attribute info


.. _`omap_mbox_dev_info.definition`:

Definition
----------

.. code-block:: c

  struct omap_mbox_dev_info {
    const char * name;
    u32 tx_id;
    u32 rx_id;
    u32 irq_id;
    u32 usr_id;
  };


.. _`omap_mbox_dev_info.members`:

Members
-------

:``name``:
    name of the mailbox device

:``tx_id``:
    mailbox queue id used for transmitting messages

:``rx_id``:
    mailbox queue id on which messages are received

:``irq_id``:
    irq identifier number to use from the hwmod data

:``usr_id``:
    mailbox user id for identifying the interrupt into
    the MPU interrupt controller.




.. _`omap_mbox_pdata`:

struct omap_mbox_pdata
======================

.. c:type:: omap_mbox_pdata

    OMAP mailbox platform data


.. _`omap_mbox_pdata.definition`:

Definition
----------

.. code-block:: c

  struct omap_mbox_pdata {
    u32 intr_type;
    u32 num_users;
    u32 num_fifos;
    u32 info_cnt;
    struct omap_mbox_dev_info * info;
  };


.. _`omap_mbox_pdata.members`:

Members
-------

:``intr_type``:
    type of interrupt configuration registers used

:``num_users``:
    number of users (processor devices) that the mailbox
    h/w block can interrupt

:``num_fifos``:
    number of h/w fifos within the mailbox h/w block

:``info_cnt``:
    number of mailbox devices for the platform

:``info``:
    array of mailbox device attributes


