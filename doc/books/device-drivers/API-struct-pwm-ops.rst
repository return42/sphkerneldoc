.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-pwm-ops:

==============
struct pwm_ops
==============

*man struct pwm_ops(9)*

*4.6.0-rc5*

PWM controller operations


Synopsis
========

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


Members
=======

request
    optional hook for requesting a PWM

free
    optional hook for freeing a PWM

config
    configure duty cycles and period length for this PWM

set_polarity
    configure the polarity of this PWM

enable
    enable PWM output toggling

disable
    disable PWM output toggling

dbg_show
    optional routine to show contents in debugfs

owner
    helps prevent removal of modules exporting active PWMs


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
