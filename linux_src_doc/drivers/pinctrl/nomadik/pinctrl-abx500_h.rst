.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/nomadik/pinctrl-abx500.h

.. _`abx500_function`:

struct abx500_function
======================

.. c:type:: struct abx500_function

    ABx500 pinctrl mux function

.. _`abx500_function.definition`:

Definition
----------

.. code-block:: c

    struct abx500_function {
        const char *name;
        const char * const *groups;
        unsigned ngroups;
    }

.. _`abx500_function.members`:

Members
-------

name
    The name of the function, exported to pinctrl core.

groups
    An array of pin groups that may select this function.

ngroups
    The number of entries in \ ``groups``\ .

.. _`abx500_pingroup`:

struct abx500_pingroup
======================

.. c:type:: struct abx500_pingroup

    describes a ABx500 pin group

.. _`abx500_pingroup.definition`:

Definition
----------

.. code-block:: c

    struct abx500_pingroup {
        const char *name;
        const unsigned int *pins;
        const unsigned npins;
        int altsetting;
    }

.. _`abx500_pingroup.members`:

Members
-------

name
    the name of this specific pin group

pins
    an array of discrete physical pins used in this group, taken
    from the driver-local pin enumeration space

npins
    *undescribed*

altsetting
    the altsetting to apply to all pins in this group to
    configure them to be used by a function

.. _`alternate_functions`:

struct alternate_functions
==========================

.. c:type:: struct alternate_functions


.. _`alternate_functions.definition`:

Definition
----------

.. code-block:: c

    struct alternate_functions {
        unsigned pin_number;
        s8 gpiosel_bit;
        s8 alt_bit1;
        s8 alt_bit2;
        u8 alta_val;
        u8 altb_val;
        u8 altc_val;
    }

.. _`alternate_functions.members`:

Members
-------

pin_number
    The pin number

gpiosel_bit
    Control bit in GPIOSEL register,

alt_bit1
    First AlternateFunction bit used to select the
    alternate function

alt_bit2
    Second AlternateFunction bit used to select the
    alternate function

alta_val
    value to write in alternatfunc to select altA function

altb_val
    value to write in alternatfunc to select altB function

altc_val
    value to write in alternatfunc to select altC function

.. _`alternate_functions.description`:

Description
-----------

these 3 following fields are necessary due to none
coherency on how to select the altA, altB and altC
function between the ABx500 SOC family when using
alternatfunc register.

.. _`abx500_gpio_irq_cluster`:

struct abx500_gpio_irq_cluster
==============================

.. c:type:: struct abx500_gpio_irq_cluster

    indicates GPIOs which are interrupt capable

.. _`abx500_gpio_irq_cluster.definition`:

Definition
----------

.. code-block:: c

    struct abx500_gpio_irq_cluster {
        int start;
        int end;
        int to_irq;
    }

.. _`abx500_gpio_irq_cluster.members`:

Members
-------

start
    The pin number of the first pin interrupt capable

end
    The pin number of the last pin interrupt capable

to_irq
    The ABx500 GPIO's associated IRQs are clustered
    together throughout the interrupt numbers at irregular
    intervals. To solve this quandary, we will place the
    read-in values into the cluster information table

.. _`abx500_pinrange`:

struct abx500_pinrange
======================

.. c:type:: struct abx500_pinrange

    map pin numbers to GPIO offsets

.. _`abx500_pinrange.definition`:

Definition
----------

.. code-block:: c

    struct abx500_pinrange {
        unsigned int offset;
        unsigned int npins;
        int altfunc;
    }

.. _`abx500_pinrange.members`:

Members
-------

offset
    offset into the GPIO local numberspace, incidentally
    identical to the offset into the local pin numberspace

npins
    number of pins to map from both offsets

altfunc
    altfunc setting to be used to enable GPIO on a pin in
    this range (may vary)

.. _`abx500_pinctrl_soc_data`:

struct abx500_pinctrl_soc_data
==============================

.. c:type:: struct abx500_pinctrl_soc_data

    ABx500 pin controller per-SoC configuration

.. _`abx500_pinctrl_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct abx500_pinctrl_soc_data {
        const struct abx500_pinrange *gpio_ranges;
        unsigned gpio_num_ranges;
        const struct pinctrl_pin_desc *pins;
        unsigned npins;
        const struct abx500_function *functions;
        unsigned nfunctions;
        const struct abx500_pingroup *groups;
        unsigned ngroups;
        struct alternate_functions *alternate_functions;
        struct abx500_gpio_irq_cluster *gpio_irq_cluster;
        unsigned ngpio_irq_cluster;
        int irq_gpio_rising_offset;
        int irq_gpio_falling_offset;
        int irq_gpio_factor;
    }

.. _`abx500_pinctrl_soc_data.members`:

Members
-------

gpio_ranges
    An array of GPIO ranges for this SoC

gpio_num_ranges
    The number of GPIO ranges for this SoC

pins
    An array describing all pins the pin controller affects.
    All pins which are also GPIOs must be listed first within the
    array, and be numbered identically to the GPIO controller's
    numbering.

npins
    The number of entries in \ ``pins``\ .

functions
    The functions supported on this SoC.

nfunctions
    *undescribed*

groups
    An array describing all pin groups the pin SoC supports.

ngroups
    The number of entries in \ ``groups``\ .

alternate_functions
    array describing pins which supports alternate and
    how to set it.

gpio_irq_cluster
    An array of GPIO interrupt capable for this SoC

ngpio_irq_cluster
    The number of GPIO inetrrupt capable for this SoC

irq_gpio_rising_offset
    Interrupt offset used as base to compute specific
    setting strategy of the rising interrupt line

irq_gpio_falling_offset
    Interrupt offset used as base to compute specific
    setting strategy of the falling interrupt line

irq_gpio_factor
    Factor used to compute specific setting strategy of
    the interrupt line

.. This file was automatic generated / don't edit.

