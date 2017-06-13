.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-s3c24xx.c

.. _`spi_fiq_code`:

struct spi_fiq_code
===================

.. c:type:: struct spi_fiq_code

    FIQ code and header

.. _`spi_fiq_code.definition`:

Definition
----------

.. code-block:: c

    struct spi_fiq_code {
        u32 length;
        u32 ack_offset;
        u8 data;
    }

.. _`spi_fiq_code.members`:

Members
-------

length
    The length of the code fragment, excluding this header.

ack_offset
    The offset from \ ``data``\  to the word to place the IRQ ACK bit at.

data
    The code itself to install as a FIQ handler.

.. _`ack_bit`:

ack_bit
=======

.. c:function:: u32 ack_bit(unsigned int irq)

    turn IRQ into IRQ acknowledgement bit

    :param unsigned int irq:
        The interrupt number

.. _`ack_bit.description`:

Description
-----------

Returns the bit to write to the interrupt acknowledge register.

.. _`s3c24xx_spi_tryfiq`:

s3c24xx_spi_tryfiq
==================

.. c:function:: void s3c24xx_spi_tryfiq(struct s3c24xx_spi *hw)

    attempt to claim and setup FIQ for transfer

    :param struct s3c24xx_spi \*hw:
        The hardware state.

.. _`s3c24xx_spi_tryfiq.description`:

Description
-----------

Claim the FIQ handler (only one can be active at any one time) and
then setup the correct transfer code for this transfer.

This call updates all the necessary state information if successful,
so the caller does not need to do anything more than start the transfer
as normal, since the IRQ will have been re-routed to the FIQ handler.

.. _`s3c24xx_spi_fiqop`:

s3c24xx_spi_fiqop
=================

.. c:function:: int s3c24xx_spi_fiqop(void *pw, int release)

    FIQ core code callback

    :param void \*pw:
        Data registered with the handler

    :param int release:
        Whether this is a release or a return.

.. _`s3c24xx_spi_fiqop.description`:

Description
-----------

Called by the FIQ code when another module wants to use the FIQ, so
return whether we are currently using this or not and then update our
internal state.

.. _`s3c24xx_spi_initfiq`:

s3c24xx_spi_initfiq
===================

.. c:function:: void s3c24xx_spi_initfiq(struct s3c24xx_spi *hw)

    setup the information for the FIQ core

    :param struct s3c24xx_spi \*hw:
        The hardware state.

.. _`s3c24xx_spi_initfiq.description`:

Description
-----------

Setup the fiq_handler block to pass to the FIQ core.

.. _`s3c24xx_spi_usefiq`:

s3c24xx_spi_usefiq
==================

.. c:function:: bool s3c24xx_spi_usefiq(struct s3c24xx_spi *hw)

    return if we should be using FIQ.

    :param struct s3c24xx_spi \*hw:
        The hardware state.

.. _`s3c24xx_spi_usefiq.description`:

Description
-----------

Return true if the platform data specifies whether this channel is
allowed to use the FIQ.

.. _`s3c24xx_spi_usingfiq`:

s3c24xx_spi_usingfiq
====================

.. c:function:: bool s3c24xx_spi_usingfiq(struct s3c24xx_spi *spi)

    return if channel is using FIQ

    :param struct s3c24xx_spi \*spi:
        The hardware state.

.. _`s3c24xx_spi_usingfiq.description`:

Description
-----------

Return whether the channel is currently using the FIQ (separate from
whether the FIQ is claimed).

.. This file was automatic generated / don't edit.

