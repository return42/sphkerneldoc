.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/comedi_8254.c

.. _`comedi_8254_status`:

comedi_8254_status
==================

.. c:function:: unsigned int comedi_8254_status(struct comedi_8254 *i8254, unsigned int counter)

    return the status of a counter

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter:
        the counter number
    :type counter: unsigned int

.. _`comedi_8254_read`:

comedi_8254_read
================

.. c:function:: unsigned int comedi_8254_read(struct comedi_8254 *i8254, unsigned int counter)

    read the current counter value

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter:
        the counter number
    :type counter: unsigned int

.. _`comedi_8254_write`:

comedi_8254_write
=================

.. c:function:: void comedi_8254_write(struct comedi_8254 *i8254, unsigned int counter, unsigned int val)

    load a 16-bit initial counter value

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter:
        the counter number
    :type counter: unsigned int

    :param val:
        the initial value
    :type val: unsigned int

.. _`comedi_8254_set_mode`:

comedi_8254_set_mode
====================

.. c:function:: int comedi_8254_set_mode(struct comedi_8254 *i8254, unsigned int counter, unsigned int mode)

    set the mode of a counter

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter:
        the counter number
    :type counter: unsigned int

    :param mode:
        the I8254_MODEx and I8254_BCD\|I8254_BINARY
    :type mode: unsigned int

.. _`comedi_8254_load`:

comedi_8254_load
================

.. c:function:: int comedi_8254_load(struct comedi_8254 *i8254, unsigned int counter, unsigned int val, unsigned int mode)

    program the mode and initial count of a counter

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter:
        the counter number
    :type counter: unsigned int

    :param val:
        the initial value
    :type val: unsigned int

    :param mode:
        the I8254_MODEx and I8254_BCD\|I8254_BINARY
    :type mode: unsigned int

.. _`comedi_8254_pacer_enable`:

comedi_8254_pacer_enable
========================

.. c:function:: void comedi_8254_pacer_enable(struct comedi_8254 *i8254, unsigned int counter1, unsigned int counter2, bool enable)

    set the mode and load the cascaded counters

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter1:
        the counter number for the first divisor
    :type counter1: unsigned int

    :param counter2:
        the counter number for the second divisor
    :type counter2: unsigned int

    :param enable:
        flag to enable (load) the counters
    :type enable: bool

.. _`comedi_8254_update_divisors`:

comedi_8254_update_divisors
===========================

.. c:function:: void comedi_8254_update_divisors(struct comedi_8254 *i8254)

    update the divisors for the cascaded counters

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

.. _`comedi_8254_cascade_ns_to_timer`:

comedi_8254_cascade_ns_to_timer
===============================

.. c:function:: void comedi_8254_cascade_ns_to_timer(struct comedi_8254 *i8254, unsigned int *nanosec, unsigned int flags)

    calculate the cascaded divisor values

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param nanosec:
        the desired ns time
    :type nanosec: unsigned int \*

    :param flags:
        comedi_cmd flags
    :type flags: unsigned int

.. _`comedi_8254_ns_to_timer`:

comedi_8254_ns_to_timer
=======================

.. c:function:: void comedi_8254_ns_to_timer(struct comedi_8254 *i8254, unsigned int *nanosec, unsigned int flags)

    calculate the divisor value for nanosec timing

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param nanosec:
        the desired ns time
    :type nanosec: unsigned int \*

    :param flags:
        comedi_cmd flags
    :type flags: unsigned int

.. _`comedi_8254_set_busy`:

comedi_8254_set_busy
====================

.. c:function:: void comedi_8254_set_busy(struct comedi_8254 *i8254, unsigned int counter, bool busy)

    set/clear the "busy" flag for a given counter

    :param i8254:
        comedi_8254 struct for the timer
    :type i8254: struct comedi_8254 \*

    :param counter:
        the counter number
    :type counter: unsigned int

    :param busy:
        set/clear flag
    :type busy: bool

.. _`comedi_8254_subdevice_init`:

comedi_8254_subdevice_init
==========================

.. c:function:: void comedi_8254_subdevice_init(struct comedi_subdevice *s, struct comedi_8254 *i8254)

    initialize a comedi_subdevice for the 8254 timer

    :param s:
        comedi_subdevice struct
    :type s: struct comedi_subdevice \*

    :param i8254:
        *undescribed*
    :type i8254: struct comedi_8254 \*

.. _`comedi_8254_init`:

comedi_8254_init
================

.. c:function:: struct comedi_8254 *comedi_8254_init(unsigned long iobase, unsigned int osc_base, unsigned int iosize, unsigned int regshift)

    allocate and initialize the 8254 device for pio access

    :param iobase:
        *undescribed*
    :type iobase: unsigned long

    :param osc_base:
        base time of the counter in ns
        OPTIONAL - only used by \ :c:func:`comedi_8254_cascade_ns_to_timer`\ 
    :type osc_base: unsigned int

    :param iosize:
        I/O register size
    :type iosize: unsigned int

    :param regshift:
        register gap shift
    :type regshift: unsigned int

.. _`comedi_8254_mm_init`:

comedi_8254_mm_init
===================

.. c:function:: struct comedi_8254 *comedi_8254_mm_init(void __iomem *mmio, unsigned int osc_base, unsigned int iosize, unsigned int regshift)

    allocate and initialize the 8254 device for mmio access

    :param mmio:
        memory mapped I/O base address
    :type mmio: void __iomem \*

    :param osc_base:
        base time of the counter in ns
        OPTIONAL - only used by \ :c:func:`comedi_8254_cascade_ns_to_timer`\ 
    :type osc_base: unsigned int

    :param iosize:
        I/O register size
    :type iosize: unsigned int

    :param regshift:
        register gap shift
    :type regshift: unsigned int

.. This file was automatic generated / don't edit.

