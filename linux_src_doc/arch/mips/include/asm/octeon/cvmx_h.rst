.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx.h

.. _`cvmx_build_io_address`:

cvmx_build_io_address
=====================

.. c:function:: uint64_t cvmx_build_io_address(uint64_t major_did, uint64_t sub_did)

    :param uint64_t major_did:
        5 bit major did

    :param uint64_t sub_did:
        3 bit sub did
        Returns I/O base address

.. _`cvmx_build_bits`:

cvmx_build_bits
===============

.. c:function:: uint64_t cvmx_build_bits(uint64_t high_bit, uint64_t low_bit, uint64_t value)

    the supplied bit rage.

    :param uint64_t high_bit:
        Highest bit value can occupy (inclusive) 0-63

    :param uint64_t low_bit:
        Lowest bit value can occupy inclusive 0-high_bit

    :param uint64_t value:
        Value to use
        Returns Value masked and shifted

.. _`cvmx_build_bits.example`:

Example
-------

.. code-block:: c

    cvmx_build_bits(39,24,value)
    <pre>
    6       5       4       3       3       2       1
    3       5       7       9       1       3       5       7      0
    +-------+-------+-------+-------+-------+-------+-------+------+
    000000000000000000000000___________value000000000000000000000000
    </pre>


.. _`cvmx_ptr_to_phys`:

cvmx_ptr_to_phys
================

.. c:function:: uint64_t cvmx_ptr_to_phys(void *ptr)

    memory address (uint64_t). Octeon hardware widgets don't understand logical addresses.

    :param void \*ptr:
        C style memory pointer
        Returns Hardware physical address

.. _`cvmx_phys_to_ptr`:

cvmx_phys_to_ptr
================

.. c:function:: void *cvmx_phys_to_ptr(uint64_t physical_address)

    memory pointer (void \*).

    :param uint64_t physical_address:
        Hardware physical address to memory
        Returns Pointer to memory

.. _`cvmx_pop`:

cvmx_pop
========

.. c:function:: uint32_t cvmx_pop(uint32_t val)

    Simple wrapper for POP instruction.

    :param uint32_t val:
        32 bit value to count set bits in

.. _`cvmx_pop.description`:

Description
-----------

Returns Number of bits set

.. _`cvmx_dpop`:

cvmx_dpop
=========

.. c:function:: int cvmx_dpop(uint64_t val)

    Simple wrapper for DPOP instruction.

    :param uint64_t val:
        64 bit value to count set bits in

.. _`cvmx_dpop.description`:

Description
-----------

Returns Number of bits set

.. _`cvmx_get_cycle`:

cvmx_get_cycle
==============

.. c:function:: uint64_t cvmx_get_cycle( void)

    :param  void:
        no arguments

.. _`cvmx_get_cycle.description`:

Description
-----------

Returns current cycle counter

.. _`cvmx_get_cycle_global`:

cvmx_get_cycle_global
=====================

.. c:function:: uint64_t cvmx_get_cycle_global( void)

    chip reset.  The counter is 64 bit. This register does not exist on CN38XX pass 1 silicion

    :param  void:
        no arguments

.. _`cvmx_get_cycle_global.description`:

Description
-----------

Returns Global chip cycle count since chip reset.

.. _`cvmx_wait_for_field64`:

CVMX_WAIT_FOR_FIELD64
=====================

.. c:function::  CVMX_WAIT_FOR_FIELD64( address,  type,  field,  op,  value,  timeout_usec)

    is common in code to need to wait for a specific field in a CSR to match a specific value. Conceptually this macro expands to:

    :param  address:
        *undescribed*

    :param  type:
        *undescribed*

    :param  field:
        *undescribed*

    :param  op:
        *undescribed*

    :param  value:
        *undescribed*

    :param  timeout_usec:
        *undescribed*

.. _`cvmx_wait_for_field64.description`:

Description
-----------

1) read csr at "address" with a csr typedef of "type"
2) Check if ("type".s."field" "op" "value")
3) If #2 isn't true loop to #1 unless too much time has passed.

.. This file was automatic generated / don't edit.

