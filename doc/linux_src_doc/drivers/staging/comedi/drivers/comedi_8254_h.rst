.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/comedi_8254.h

.. _`comedi_8254`:

struct comedi_8254
==================

.. c:type:: struct comedi_8254

    private data used by this module

.. _`comedi_8254.definition`:

Definition
----------

.. code-block:: c

    struct comedi_8254 {
        unsigned long iobase;
        void __iomem *mmio;
        unsigned int iosize;
        unsigned int regshift;
        unsigned int osc_base;
        unsigned int divisor;
        unsigned int divisor1;
        unsigned int divisor2;
        unsigned int next_div;
        unsigned int next_div1;
        unsigned int next_div2;
        unsigned int clock_src[3];
        unsigned int gate_src[3];
        bool busy[3];
        int (*insn_config)(struct comedi_device *, struct comedi_subdevice *s,struct comedi_insn *, unsigned int *data);
    }

.. _`comedi_8254.members`:

Members
-------

iobase
    PIO base address of the registers (in/out)

mmio
    MMIO base address of the registers (read/write)

iosize
    I/O size used to access the registers (b/w/l)

regshift
    register gap shift

osc_base
    cascaded oscillator speed in ns

divisor
    divisor for single counter

divisor1
    divisor loaded into first cascaded counter

divisor2
    divisor loaded into second cascaded counter
    #next_div:           next divisor for single counter

next_div
    *undescribed*

next_div1
    next divisor to use for first cascaded counter

next_div2
    next divisor to use for second cascaded counter
    \ ``clock_src``\ ;          current clock source for each counter (driver specific)
    \ ``gate_src``\ ;           current gate source  for each counter (driver specific)

busy
    flags used to indicate that a counter is "busy"

insn_config
    driver specific (\*insn_config) callback

.. This file was automatic generated / don't edit.

