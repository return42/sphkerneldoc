.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-io.c

.. _`snd_soc_component_read`:

snd_soc_component_read
======================

.. c:function:: int snd_soc_component_read(struct snd_soc_component *component, unsigned int reg, unsigned int *val)

    Read register value

    :param struct snd_soc_component \*component:
        Component to read from

    :param unsigned int reg:
        Register to read

    :param unsigned int \*val:
        Pointer to where the read value is stored

.. _`snd_soc_component_read.return`:

Return
------

0 on success, a negative error code otherwise.

.. _`snd_soc_component_write`:

snd_soc_component_write
=======================

.. c:function:: int snd_soc_component_write(struct snd_soc_component *component, unsigned int reg, unsigned int val)

    Write register value

    :param struct snd_soc_component \*component:
        Component to write to

    :param unsigned int reg:
        Register to write

    :param unsigned int val:
        Value to write to the register

.. _`snd_soc_component_write.return`:

Return
------

0 on success, a negative error code otherwise.

.. _`snd_soc_component_update_bits`:

snd_soc_component_update_bits
=============================

.. c:function:: int snd_soc_component_update_bits(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int val)

    Perform read/modify/write cycle

    :param struct snd_soc_component \*component:
        Component to update

    :param unsigned int reg:
        Register to update

    :param unsigned int mask:
        Mask that specifies which bits to update

    :param unsigned int val:
        New value for the bits specified by mask

.. _`snd_soc_component_update_bits.return`:

Return
------

1 if the operation was successful and the value of the register
changed, 0 if the operation was successful, but the value did not change.
Returns a negative error code otherwise.

.. _`snd_soc_component_update_bits_async`:

snd_soc_component_update_bits_async
===================================

.. c:function:: int snd_soc_component_update_bits_async(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int val)

    Perform asynchronous read/modify/write cycle

    :param struct snd_soc_component \*component:
        Component to update

    :param unsigned int reg:
        Register to update

    :param unsigned int mask:
        Mask that specifies which bits to update

    :param unsigned int val:
        New value for the bits specified by mask

.. _`snd_soc_component_update_bits_async.description`:

Description
-----------

This function is similar to \ :c:func:`snd_soc_component_update_bits`\ , but the update
operation is scheduled asynchronously. This means it may not be completed
when the function returns. To make sure that all scheduled updates have been
completed \ :c:func:`snd_soc_component_async_complete`\  must be called.

.. _`snd_soc_component_update_bits_async.return`:

Return
------

1 if the operation was successful and the value of the register
changed, 0 if the operation was successful, but the value did not change.
Returns a negative error code otherwise.

.. _`snd_soc_component_async_complete`:

snd_soc_component_async_complete
================================

.. c:function:: void snd_soc_component_async_complete(struct snd_soc_component *component)

    Ensure asynchronous I/O has completed

    :param struct snd_soc_component \*component:
        Component for which to wait

.. _`snd_soc_component_async_complete.description`:

Description
-----------

This function blocks until all asynchronous I/O which has previously been
scheduled using \ :c:func:`snd_soc_component_update_bits_async`\  has completed.

.. _`snd_soc_component_test_bits`:

snd_soc_component_test_bits
===========================

.. c:function:: int snd_soc_component_test_bits(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int value)

    Test register for change

    :param struct snd_soc_component \*component:
        component

    :param unsigned int reg:
        Register to test

    :param unsigned int mask:
        Mask that specifies which bits to test

    :param unsigned int value:
        Value to test against

.. _`snd_soc_component_test_bits.description`:

Description
-----------

Tests a register with a new value and checks if the new value is
different from the old value.

.. _`snd_soc_component_test_bits.return`:

Return
------

1 for change, otherwise 0.

.. This file was automatic generated / don't edit.

