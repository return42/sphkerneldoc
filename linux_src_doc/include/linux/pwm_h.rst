.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pwm.h

.. _`pwm_polarity`:

enum pwm_polarity
=================

.. c:type:: enum pwm_polarity

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

PWM_POLARITY_NORMAL
    a high signal for the duration of the duty-
    cycle, followed by a low signal for the remainder of the pulse
    period

PWM_POLARITY_INVERSED
    a low signal for the duration of the duty-
    cycle, followed by a high signal for the remainder of the pulse
    period

.. _`pwm_args`:

struct pwm_args
===============

.. c:type:: struct pwm_args

    board-dependent PWM arguments

.. _`pwm_args.definition`:

Definition
----------

.. code-block:: c

    struct pwm_args {
        unsigned int period;
        enum pwm_polarity polarity;
    }

.. _`pwm_args.members`:

Members
-------

period
    reference period

polarity
    reference polarity

.. _`pwm_args.description`:

Description
-----------

This structure describes board-dependent arguments attached to a PWM
device. These arguments are usually retrieved from the PWM lookup table or
device tree.

Do not confuse this with the PWM state: PWM arguments represent the initial
configuration that users want to use on this PWM device rather than the
current PWM hardware state.

.. _`pwm_device`:

struct pwm_device
=================

.. c:type:: struct pwm_device

    PWM channel object

.. _`pwm_device.definition`:

Definition
----------

.. code-block:: c

    struct pwm_device {
        const char *label;
        unsigned long flags;
        unsigned int hwpwm;
        unsigned int pwm;
        struct pwm_chip *chip;
        void *chip_data;
        struct pwm_args args;
        struct pwm_state state;
    }

.. _`pwm_device.members`:

Members
-------

label
    name of the PWM device

flags
    flags associated with the PWM device

hwpwm
    per-chip relative index of the PWM device

pwm
    global index of the PWM device

chip
    PWM chip providing this PWM device

chip_data
    chip-private data associated with the PWM device

args
    PWM arguments

state
    curent PWM channel state

.. _`pwm_get_state`:

pwm_get_state
=============

.. c:function:: void pwm_get_state(const struct pwm_device *pwm, struct pwm_state *state)

    retrieve the current PWM state

    :param const struct pwm_device \*pwm:
        PWM device

    :param struct pwm_state \*state:
        state to fill with the current PWM state

.. _`pwm_init_state`:

pwm_init_state
==============

.. c:function:: void pwm_init_state(const struct pwm_device *pwm, struct pwm_state *state)

    prepare a new state to be applied with \ :c:func:`pwm_apply_state`\ 

    :param const struct pwm_device \*pwm:
        PWM device

    :param struct pwm_state \*state:
        state to fill with the prepared PWM state

.. _`pwm_init_state.description`:

Description
-----------

This functions prepares a state that can later be tweaked and applied
to the PWM device with \ :c:func:`pwm_apply_state`\ . This is a convenient function
that first retrieves the current PWM state and the replaces the period
and polarity fields with the reference values defined in pwm->args.
Once the function returns, you can adjust the ->enabled and ->duty_cycle
fields according to your needs before calling \ :c:func:`pwm_apply_state`\ .

->duty_cycle is initially set to zero to avoid cases where the current
->duty_cycle value exceed the pwm_args->period one, which would trigger
an error if the user calls \ :c:func:`pwm_apply_state`\  without adjusting ->duty_cycle
first.

.. _`pwm_get_relative_duty_cycle`:

pwm_get_relative_duty_cycle
===========================

.. c:function:: unsigned int pwm_get_relative_duty_cycle(const struct pwm_state *state, unsigned int scale)

    Get a relative duty cycle value

    :param const struct pwm_state \*state:
        PWM state to extract the duty cycle from

    :param unsigned int scale:
        target scale of the relative duty cycle

.. _`pwm_get_relative_duty_cycle.description`:

Description
-----------

This functions converts the absolute duty cycle stored in \ ``state``\  (expressed
in nanosecond) into a value relative to the period.

For example if you want to get the duty_cycle expressed in percent, call:

pwm_get_state(pwm, \ :c:type:`struct state <state>`\ );
duty = pwm_get_relative_duty_cycle(&state, 100);

.. _`pwm_set_relative_duty_cycle`:

pwm_set_relative_duty_cycle
===========================

.. c:function:: int pwm_set_relative_duty_cycle(struct pwm_state *state, unsigned int duty_cycle, unsigned int scale)

    Set a relative duty cycle value

    :param struct pwm_state \*state:
        PWM state to fill

    :param unsigned int duty_cycle:
        relative duty cycle value

    :param unsigned int scale:
        scale in which \ ``duty_cycle``\  is expressed

.. _`pwm_set_relative_duty_cycle.description`:

Description
-----------

This functions converts a relative into an absolute duty cycle (expressed
in nanoseconds), and puts the result in state->duty_cycle.

For example if you want to configure a 50% duty cycle, call:

pwm_init_state(pwm, \ :c:type:`struct state <state>`\ );
pwm_set_relative_duty_cycle(&state, 50, 100);
pwm_apply_state(pwm, \ :c:type:`struct state <state>`\ );

This functions returns -EINVAL if \ ``duty_cycle``\  and/or \ ``scale``\  are
inconsistent (@scale == 0 or \ ``duty_cycle``\  > \ ``scale``\ ).

.. _`pwm_ops`:

struct pwm_ops
==============

.. c:type:: struct pwm_ops

    PWM controller operations

.. _`pwm_ops.definition`:

Definition
----------

.. code-block:: c

    struct pwm_ops {
        int (*request)(struct pwm_chip *chip, struct pwm_device *pwm);
        void (*free)(struct pwm_chip *chip, struct pwm_device *pwm);
        int (*config)(struct pwm_chip *chip, struct pwm_device *pwm,int duty_ns, int period_ns);
        int (*set_polarity)(struct pwm_chip *chip, struct pwm_device *pwm,enum pwm_polarity polarity);
        int (*capture)(struct pwm_chip *chip, struct pwm_device *pwm,struct pwm_capture *result, unsigned long timeout);
        int (*enable)(struct pwm_chip *chip, struct pwm_device *pwm);
        void (*disable)(struct pwm_chip *chip, struct pwm_device *pwm);
        int (*apply)(struct pwm_chip *chip, struct pwm_device *pwm,struct pwm_state *state);
        void (*get_state)(struct pwm_chip *chip, struct pwm_device *pwm,struct pwm_state *state);
    #ifdef CONFIG_DEBUG_FS
        void (*dbg_show)(struct pwm_chip *chip, struct seq_file *s);
    #endif
        struct module *owner;
    }

.. _`pwm_ops.members`:

Members
-------

request
    optional hook for requesting a PWM

free
    optional hook for freeing a PWM

config
    configure duty cycles and period length for this PWM

set_polarity
    configure the polarity of this PWM

capture
    capture and report PWM signal

enable
    enable PWM output toggling

disable
    disable PWM output toggling

apply
    atomically apply a new PWM config. The state argument
    should be adjusted with the real hardware config (if the
    approximate the period or duty_cycle value, state should
    reflect it)

get_state
    get the current PWM state. This function is only
    called once per PWM device when the PWM chip is
    registered.

dbg_show
    optional routine to show contents in debugfs

owner
    helps prevent removal of modules exporting active PWMs

.. _`pwm_chip`:

struct pwm_chip
===============

.. c:type:: struct pwm_chip

    abstract a PWM controller

.. _`pwm_chip.definition`:

Definition
----------

.. code-block:: c

    struct pwm_chip {
        struct device *dev;
        struct list_head list;
        const struct pwm_ops *ops;
        int base;
        unsigned int npwm;
        struct pwm_device *pwms;
        struct pwm_device * (*of_xlate)(struct pwm_chip *pc,const struct of_phandle_args *args);
        unsigned int of_pwm_n_cells;
    }

.. _`pwm_chip.members`:

Members
-------

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

.. _`pwm_capture`:

struct pwm_capture
==================

.. c:type:: struct pwm_capture

    PWM capture data

.. _`pwm_capture.definition`:

Definition
----------

.. code-block:: c

    struct pwm_capture {
        unsigned int period;
        unsigned int duty_cycle;
    }

.. _`pwm_capture.members`:

Members
-------

period
    period of the PWM signal (in nanoseconds)

duty_cycle
    duty cycle of the PWM signal (in nanoseconds)

.. _`pwm_config`:

pwm_config
==========

.. c:function:: int pwm_config(struct pwm_device *pwm, int duty_ns, int period_ns)

    change a PWM device configuration

    :param struct pwm_device \*pwm:
        PWM device

    :param int duty_ns:
        "on" time (in nanoseconds)

    :param int period_ns:
        duration (in nanoseconds) of one cycle

.. _`pwm_config.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwm_set_polarity`:

pwm_set_polarity
================

.. c:function:: int pwm_set_polarity(struct pwm_device *pwm, enum pwm_polarity polarity)

    configure the polarity of a PWM signal

    :param struct pwm_device \*pwm:
        PWM device

    :param enum pwm_polarity polarity:
        new polarity of the PWM signal

.. _`pwm_set_polarity.description`:

Description
-----------

Note that the polarity cannot be configured while the PWM device is
enabled.

.. _`pwm_set_polarity.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwm_enable`:

pwm_enable
==========

.. c:function:: int pwm_enable(struct pwm_device *pwm)

    start a PWM output toggling

    :param struct pwm_device \*pwm:
        PWM device

.. _`pwm_enable.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwm_disable`:

pwm_disable
===========

.. c:function:: void pwm_disable(struct pwm_device *pwm)

    stop a PWM output toggling

    :param struct pwm_device \*pwm:
        PWM device

.. This file was automatic generated / don't edit.

