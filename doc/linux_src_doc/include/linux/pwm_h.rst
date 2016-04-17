.. -*- coding: utf-8; mode: rst -*-

=====
pwm.h
=====


.. _`pwm_polarity`:

enum pwm_polarity
=================

.. c:type:: pwm_polarity

    polarity of a PWM signal


.. _`pwm_polarity.definition`:

Definition
----------

.. code-block:: c

    enum pwm_polarity {
      PWM_POLARITY_NORMAL,
      PWM_POLARITY_INVERSED
    };


.. _`pwm_polarity.constants`:

Constants
---------

:``PWM_POLARITY_NORMAL``:
    a high signal for the duration of the duty-
    cycle, followed by a low signal for the remainder of the pulse
    period

:``PWM_POLARITY_INVERSED``:
    a low signal for the duration of the duty-
    cycle, followed by a high signal for the remainder of the pulse
    period


.. _`pwm_device`:

struct pwm_device
=================

.. c:type:: pwm_device

    PWM channel object


.. _`pwm_device.definition`:

Definition
----------

.. code-block:: c

  struct pwm_device {
    const char * label;
    unsigned long flags;
    unsigned int hwpwm;
    unsigned int pwm;
    struct pwm_chip * chip;
    void * chip_data;
    struct mutex lock;
    unsigned int period;
    unsigned int duty_cycle;
    enum pwm_polarity polarity;
  };


.. _`pwm_device.members`:

Members
-------

:``label``:
    name of the PWM device

:``flags``:
    flags associated with the PWM device

:``hwpwm``:
    per-chip relative index of the PWM device

:``pwm``:
    global index of the PWM device

:``chip``:
    PWM chip providing this PWM device

:``chip_data``:
    chip-private data associated with the PWM device

:``lock``:
    used to serialize accesses to the PWM device where necessary

:``period``:
    period of the PWM signal (in nanoseconds)

:``duty_cycle``:
    duty cycle of the PWM signal (in nanoseconds)

:``polarity``:
    polarity of the PWM signal




.. _`pwm_ops`:

struct pwm_ops
==============

.. c:type:: pwm_ops

    PWM controller operations


.. _`pwm_ops.definition`:

Definition
----------

.. code-block:: c

  struct pwm_ops {
    int (* request) (struct pwm_chip *chip, struct pwm_device *pwm);
    void (* free) (struct pwm_chip *chip, struct pwm_device *pwm);
    int (* config) (struct pwm_chip *chip, struct pwm_device *pwm,int duty_ns, int period_ns);
    int (* set_polarity) (struct pwm_chip *chip, struct pwm_device *pwm,enum pwm_polarity polarity);
    int (* enable) (struct pwm_chip *chip, struct pwm_device *pwm);
    void (* disable) (struct pwm_chip *chip, struct pwm_device *pwm);
    #ifdef CONFIG_DEBUG_FS
    void (* dbg_show) (struct pwm_chip *chip, struct seq_file *s);
    #endif
    struct module * owner;
  };


.. _`pwm_ops.members`:

Members
-------

:``request``:
    optional hook for requesting a PWM

:``free``:
    optional hook for freeing a PWM

:``config``:
    configure duty cycles and period length for this PWM

:``set_polarity``:
    configure the polarity of this PWM

:``enable``:
    enable PWM output toggling

:``disable``:
    disable PWM output toggling

:``dbg_show``:
    optional routine to show contents in debugfs

:``owner``:
    helps prevent removal of modules exporting active PWMs




.. _`pwm_chip`:

struct pwm_chip
===============

.. c:type:: pwm_chip

    abstract a PWM controller


.. _`pwm_chip.definition`:

Definition
----------

.. code-block:: c

  struct pwm_chip {
    struct device * dev;
    struct list_head list;
    const struct pwm_ops * ops;
    int base;
    unsigned int npwm;
    struct pwm_device * pwms;
    struct pwm_device * (* of_xlate) (struct pwm_chip *pc,const struct of_phandle_args *args);
    unsigned int of_pwm_n_cells;
    bool can_sleep;
  };


.. _`pwm_chip.members`:

Members
-------

:``dev``:
    device providing the PWMs

:``list``:
    list node for internal use

:``ops``:
    callbacks for this PWM controller

:``base``:
    number of first PWM controlled by this chip

:``npwm``:
    number of PWMs controlled by this chip

:``pwms``:
    array of PWM devices allocated by the framework

:``of_xlate``:
    request a PWM device given a device tree PWM specifier

:``of_pwm_n_cells``:
    number of cells expected in the device tree PWM specifier

:``can_sleep``:
    must be true if the .:c:func:`config`, .:c:func:`enable` or .:c:func:`disable`
    operations may sleep


