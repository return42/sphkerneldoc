.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/msr.c

.. _`msr_read`:

msr_read
========

.. c:function:: int msr_read(u32 msr, struct msr *m)

    :param u32 msr:
        MSR to read

    :param struct msr \*m:
        value to read into

.. _`msr_read.description`:

Description
-----------

It returns read data only on success, otherwise it doesn't change the output
argument \ ``m``\ .

.. _`msr_write`:

msr_write
=========

.. c:function:: int msr_write(u32 msr, struct msr *m)

    :param u32 msr:
        MSR to write

    :param struct msr \*m:
        value to write

.. _`msr_set_bit`:

msr_set_bit
===========

.. c:function:: int msr_set_bit(u32 msr, u8 bit)

    :param u32 msr:
        *undescribed*

    :param u8 bit:
        *undescribed*

.. _`msr_set_bit.retval`:

Retval
------

< 0: An error was encountered.
= 0: Bit was already set.
> 0: Hardware accepted the MSR write.

.. _`msr_clear_bit`:

msr_clear_bit
=============

.. c:function:: int msr_clear_bit(u32 msr, u8 bit)

    :param u32 msr:
        *undescribed*

    :param u8 bit:
        *undescribed*

.. _`msr_clear_bit.retval`:

Retval
------

< 0: An error was encountered.
= 0: Bit was already cleared.
> 0: Hardware accepted the MSR write.

.. This file was automatic generated / don't edit.

