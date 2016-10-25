.. -*- coding: utf-8; mode: rst -*-

.. _rationale:

*********
Rationale
*********

The original implementation of interrupt handling in Linux uses the
__do_IRQ() super-handler, which is able to deal with every type of
interrupt logic.

Originally, Russell King identified different types of handlers to build
a quite universal set for the ARM interrupt handler implementation in
Linux 2.5/2.6. He distinguished between:

-  Level type

-  Edge type

-  Simple type

During the implementation we identified another type:

-  Fast EOI type

In the SMP world of the __do_IRQ() super-handler another type was
identified:

-  Per CPU type

This split implementation of high-level IRQ handlers allows us to
optimize the flow of the interrupt handling for each specific interrupt
type. This reduces complexity in that particular code path and allows
the optimized handling of a given type.

The original general IRQ implementation used hw_interrupt_type
structures and their ->ack(), ->end() [etc.] callbacks to differentiate
the flow control in the super-handler. This leads to a mix of flow logic
and low-level hardware logic, and it also leads to unnecessary code
duplication: for example in i386, there is an ioapic_level_irq and an
ioapic_edge_irq IRQ-type which share many of the low-level details but
have different flow handling.

A more natural abstraction is the clean separation of the 'irq flow' and
the 'chip details'.

Analysing a couple of architecture's IRQ subsystem implementations
reveals that most of them can use a generic set of 'irq flow' methods
and only need to add the chip-level specific code. The separation is
also valuable for (sub)architectures which need specific quirks in the
IRQ flow itself but not in the chip details - and thus provides a more
transparent IRQ subsystem design.

Each interrupt descriptor is assigned its own high-level flow handler,
which is normally one of the generic implementations. (This high-level
flow handler implementation also makes it simple to provide
demultiplexing handlers which can be found in embedded platforms on
various architectures.)

The separation makes the generic interrupt handling layer more flexible
and extensible. For example, an (sub)architecture can use a generic
IRQ-flow implementation for 'level type' interrupts and add a
(sub)architecture specific 'edge type' implementation.

To make the transition to the new model easier and prevent the breakage
of existing implementations, the __do_IRQ() super-handler is still
available. This leads to a kind of duality for the time being. Over time
the new model should be used in more and more architectures, as it
enables smaller and cleaner IRQ subsystems. It's deprecated for three
years now and about to be removed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
