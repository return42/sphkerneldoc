.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-sa1100/ssp.c

.. _`ssp_write_word`:

ssp_write_word
==============

.. c:function:: int ssp_write_word(u16 data)

    write a word to the SSP port

    :param u16 data:
        16-bit, MSB justified data to write.

.. _`ssp_write_word.description`:

Description
-----------

Wait for a free entry in the SSP transmit FIFO, and write a data
word to the SSP port.  Wait for the SSP port to start sending
the data.

The caller is expected to perform the necessary locking.

.. _`ssp_write_word.return`:

Return
------

\ ``-ETIMEDOUT``\         timeout occurred
0                  success

.. _`ssp_read_word`:

ssp_read_word
=============

.. c:function:: int ssp_read_word(u16 *data)

    read a word from the SSP port

    :param u16 \*data:
        *undescribed*

.. _`ssp_read_word.description`:

Description
-----------

Wait for a data word in the SSP receive FIFO, and return the
received data.  Data is LSB justified.

.. _`ssp_read_word.note`:

Note
----

Currently, if data is not expected to be received, this
function will wait for ever.

The caller is expected to perform the necessary locking.

.. _`ssp_read_word.return`:

Return
------

\ ``-ETIMEDOUT``\         timeout occurred
16-bit data        success

.. _`ssp_flush`:

ssp_flush
=========

.. c:function:: int ssp_flush( void)

    flush the transmit and receive FIFOs

    :param  void:
        no arguments

.. _`ssp_flush.description`:

Description
-----------

Wait for the SSP to idle, and ensure that the receive FIFO
is empty.

The caller is expected to perform the necessary locking.

.. _`ssp_flush.return`:

Return
------

\ ``-ETIMEDOUT``\         timeout occurred
0                  success

.. _`ssp_enable`:

ssp_enable
==========

.. c:function:: void ssp_enable( void)

    enable the SSP port

    :param  void:
        no arguments

.. _`ssp_enable.description`:

Description
-----------

Turn on the SSP port.

.. _`ssp_disable`:

ssp_disable
===========

.. c:function:: void ssp_disable( void)

    shut down the SSP port

    :param  void:
        no arguments

.. _`ssp_disable.description`:

Description
-----------

Turn off the SSP port, optionally powering it down.

.. _`ssp_save_state`:

ssp_save_state
==============

.. c:function:: void ssp_save_state(struct ssp_state *ssp)

    save the SSP configuration

    :param struct ssp_state \*ssp:
        pointer to structure to save SSP configuration

.. _`ssp_save_state.description`:

Description
-----------

Save the configured SSP state for suspend.

.. _`ssp_restore_state`:

ssp_restore_state
=================

.. c:function:: void ssp_restore_state(struct ssp_state *ssp)

    restore a previously saved SSP configuration

    :param struct ssp_state \*ssp:
        pointer to configuration saved by ssp_save_state

.. _`ssp_restore_state.description`:

Description
-----------

Restore the SSP configuration saved previously by ssp_save_state.

.. _`ssp_init`:

ssp_init
========

.. c:function:: int ssp_init( void)

    setup the SSP port

    :param  void:
        no arguments

.. _`ssp_init.description`:

Description
-----------

initialise and claim resources for the SSP port.

.. _`ssp_init.return`:

Return
------

\ ``-ENODEV``\    if the SSP port is unavailable
\ ``-EBUSY``\     if the resources are already in use
\ ``0``\          on success

.. _`ssp_exit`:

ssp_exit
========

.. c:function:: void ssp_exit( void)

    undo the effects of ssp_init

    :param  void:
        no arguments

.. _`ssp_exit.description`:

Description
-----------

release and free resources for the SSP port.

.. This file was automatic generated / don't edit.

