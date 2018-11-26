.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/msa.h

.. _`read_msa_wr`:

read_msa_wr
===========

.. c:function:: void read_msa_wr(unsigned idx, union fpureg *to, enum msa_2b_fmt fmt)

    Read a single MSA vector register

    :param idx:
        The index of the vector register to read
    :type idx: unsigned

    :param to:
        The FPU register union to store the registers value in
    :type to: union fpureg \*

    :param fmt:
        The format of the data in the vector register
    :type fmt: enum msa_2b_fmt

.. _`read_msa_wr.description`:

Description
-----------

Read the value of MSA vector register idx into the FPU register
union to, using the format fmt.

.. _`write_msa_wr`:

write_msa_wr
============

.. c:function:: void write_msa_wr(unsigned idx, union fpureg *from, enum msa_2b_fmt fmt)

    Write a single MSA vector register

    :param idx:
        The index of the vector register to write
    :type idx: unsigned

    :param from:
        The FPU register union to take the registers value from
    :type from: union fpureg \*

    :param fmt:
        The format of the data in the vector register
    :type fmt: enum msa_2b_fmt

.. _`write_msa_wr.description`:

Description
-----------

Write the value from the FPU register union from into MSA vector
register idx, using the format fmt.

.. This file was automatic generated / don't edit.

