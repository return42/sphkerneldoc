.. -*- coding: utf-8; mode: rst -*-

==========
chipidea.h
==========


.. _`ci_hdrc_cable`:

struct ci_hdrc_cable
====================

.. c:type:: ci_hdrc_cable

    structure for external connector cable state tracking


.. _`ci_hdrc_cable.definition`:

Definition
----------

.. code-block:: c

  struct ci_hdrc_cable {
    bool state;
    bool changed;
    struct extcon_dev * edev;
    struct ci_hdrc * ci;
    struct notifier_block nb;
  };


.. _`ci_hdrc_cable.members`:

Members
-------

:``state``:
    current state of the line

:``changed``:
    set to true when extcon event happen

:``edev``:
    device which generate events

:``ci``:
    driver state of the chipidea device

:``nb``:
    hold event notification callback


