
.. _API-struct-pwm-chip:

===============
struct pwm_chip
===============

*man struct pwm_chip(9)*

*4.6.0-rc1*

abstract a PWM controller


Synopsis
========

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


Members
=======

dev
    device providing the PWMs

list
    list node for internal use

ops
    callbacks for this PWM controller

base
    number of first PWM controlled by this chip

npwm
    number of PWMs controlled by this chip

pwms
    array of PWM devices allocated by the framework

of_xlate
    request a PWM device given a device tree PWM specifier

of_pwm_n_cells
    number of cells expected in the device tree PWM specifier

can_sleep
    must be true if the .\ ``config``, .\ ``enable`` or .\ ``disable`` operations may sleep
