.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/nand_hynix.c

.. _`hynix_read_retry`:

struct hynix_read_retry
=======================

.. c:type:: struct hynix_read_retry

    read-retry data

.. _`hynix_read_retry.definition`:

Definition
----------

.. code-block:: c

    struct hynix_read_retry {
        int nregs;
        const u8 *regs;
        u8 values[0];
    }

.. _`hynix_read_retry.members`:

Members
-------

nregs
    number of register to set when applying a new read-retry mode

regs
    register offsets (NAND chip dependent)

values
    array of values to set in registers. The array size is equal to
    (nregs \* nmodes)

.. _`hynix_nand`:

struct hynix_nand
=================

.. c:type:: struct hynix_nand

    private Hynix NAND struct

.. _`hynix_nand.definition`:

Definition
----------

.. code-block:: c

    struct hynix_nand {
        const struct hynix_read_retry *read_retry;
    }

.. _`hynix_nand.members`:

Members
-------

read_retry
    read-retry information

.. _`hynix_read_retry_otp`:

struct hynix_read_retry_otp
===========================

.. c:type:: struct hynix_read_retry_otp

    structure describing how the read-retry OTP area

.. _`hynix_read_retry_otp.definition`:

Definition
----------

.. code-block:: c

    struct hynix_read_retry_otp {
        int nregs;
        const u8 *regs;
        const u8 *values;
        int page;
        int size;
    }

.. _`hynix_read_retry_otp.members`:

Members
-------

nregs
    number of hynix private registers to set before reading the reading
    the OTP area

regs
    registers that should be configured

values
    values that should be set in regs

page
    the address to pass to the READ_PAGE command. Depends on the NAND
    chip

size
    size of the read-retry OTP section

.. _`hynix_get_majority`:

hynix_get_majority
==================

.. c:function:: int hynix_get_majority(const u8 *in, int repeat, u8 *out)

    get the value that is occurring the most in a given set of values

    :param const u8 \*in:
        the array of values to test

    :param int repeat:
        the size of the in array

    :param u8 \*out:
        pointer used to store the output value

.. _`hynix_get_majority.description`:

Description
-----------

This function implements the 'majority check' logic that is supposed to
overcome the unreliability of MLC NANDs when reading the OTP area storing
the read-retry parameters.

It's based on a pretty simple assumption: if we repeat the same value
several times and then take the one that is occurring the most, we should
find the correct value.
Let's hope this dummy algorithm prevents us from losing the read-retry
parameters.

.. This file was automatic generated / don't edit.

