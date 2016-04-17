.. -*- coding: utf-8; mode: rst -*-

=========
devinfo.h
=========


.. _`dev_pin_info`:

struct dev_pin_info
===================

.. c:type:: dev_pin_info

    pin state container for devices


.. _`dev_pin_info.definition`:

Definition
----------

.. code-block:: c

  struct dev_pin_info {
    struct pinctrl * p;
    struct pinctrl_state * default_state;
    struct pinctrl_state * init_state;
    #ifdef CONFIG_PM
    struct pinctrl_state * sleep_state;
    struct pinctrl_state * idle_state;
    #endif
  };


.. _`dev_pin_info.members`:

Members
-------

:``p``:
    pinctrl handle for the containing device

:``default_state``:
    the default state for the handle, if found

:``init_state``:
    the state at probe time, if found

:``sleep_state``:
    the state at suspend time, if found

:``idle_state``:
    the state at idle (runtime suspend) time, if found


