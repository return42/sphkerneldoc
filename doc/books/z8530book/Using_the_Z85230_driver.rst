.. -*- coding: utf-8; mode: rst -*-

.. _Using_the_Z85230_driver:

***********************
Using the Z85230 driver
***********************

The Z85230 driver provides the back end interface to your board. To
configure a Z8530 interface you need to detect the board and to identify
its ports and interrupt resources. It is also your problem to verify the
resources are available.

Having identified the chip you need to fill in a struct z8530_dev,
which describes each chip. This object must exist until you finally
shutdown the board. Firstly zero the active field. This ensures nothing
goes off without you intending it. The irq field should be set to the
interrupt number of the chip. (Each chip has a single interrupt source
rather than each channel). You are responsible for allocating the
interrupt line. The interrupt handler should be set to
``z8530_interrupt``. The device id should be set to the z8530_dev
structure pointer. Whether the interrupt can be shared or not is board
dependent, and up to you to initialise.

The structure holds two channel structures. Initialise chanA.ctrlio and
chanA.dataio with the address of the control and data ports. You can or
this with Z8530_PORT_SLEEP to indicate your interface needs the 5uS
delay for chip settling done in software. The PORT_SLEEP option is
architecture specific. Other flags may become available on future
platforms, eg for MMIO. Initialise the chanA.irqs to &z8530_nop to
start the chip up as disabled and discarding interrupt events. This
ensures that stray interrupts will be mopped up and not hang the bus.
Set chanA.dev to point to the device structure itself. The private and
name field you may use as you wish. The private field is unused by the
Z85230 layer. The name is used for error reporting and it may thus make
sense to make it match the network name.

Repeat the same operation with the B channel if your chip has both
channels wired to something useful. This isn't always the case. If it is
not wired then the I/O values do not matter, but you must initialise
chanB.dev.

If your board has DMA facilities then initialise the txdma and rxdma
fields for the relevant channels. You must also allocate the ISA DMA
channels and do any necessary board level initialisation to configure
them. The low level driver will do the Z8530 and DMA controller
programming but not board specific magic.

Having initialised the device you can then call ``z8530_init``. This
will probe the chip and reset it into a known state. An identification
sequence is then run to identify the chip type. If the checks fail to
pass the function returns a non zero error code. Typically this
indicates that the port given is not valid. After this call the type
field of the z8530_dev structure is initialised to either Z8530, Z85C30
or Z85230 according to the chip found.

Once you have called z8530_init you can also make use of the utility
function ``z8530_describe``. This provides a consistent reporting format
for the Z8530 devices, and allows all the drivers to provide consistent
reporting.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
