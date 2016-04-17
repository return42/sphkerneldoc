.. -*- coding: utf-8; mode: rst -*-

===============
jitterentropy.c
===============


.. _`jent_loop_shuffle`:

jent_loop_shuffle
=================

.. c:function:: __u64 jent_loop_shuffle (struct rand_data *ec, unsigned int bits, unsigned int min)

    :param struct rand_data \*ec:

        *undescribed*

    :param unsigned int bits:

        *undescribed*

    :param unsigned int min:

        *undescribed*



.. _`jent_loop_shuffle.description`:

Description
-----------

an entropy collection.



.. _`jent_loop_shuffle.input`:

Input
-----

``ec`` entropy collector struct -- may be NULL
``bits`` is the number of low bits of the timer to consider
``min`` is the number of bits we shift the timer value to the right at
the end to make sure we have a guaranteed minimum value

``return`` Newly calculated loop counter



.. _`jent_fold_time`:

jent_fold_time
==============

.. c:function:: __u64 jent_fold_time (struct rand_data *ec, __u64 time, __u64 *folded, __u64 loop_cnt)

    - this is the noise source based on the CPU execution time jitter

    :param struct rand_data \*ec:

        *undescribed*

    :param __u64 time:

        *undescribed*

    :param __u64 \*folded:

        *undescribed*

    :param __u64 loop_cnt:

        *undescribed*



.. _`jent_fold_time.description`:

Description
-----------


This function folds the time into one bit units by iterating



.. _`jent_fold_time.through-the-data_size_bits-bit-time-value-as-follows`:

through the DATA_SIZE_BITS bit time value as follows
----------------------------------------------------

assume our time value
is 0xabcd
1st loop, 1st shift generates 0xd000
1st loop, 2nd shift generates 0x000d
2nd loop, 1st shift generates 0xcd00
2nd loop, 2nd shift generates 0x000c
3rd loop, 1st shift generates 0xbcd0
3rd loop, 2nd shift generates 0x000b
4th loop, 1st shift generates 0xabcd
4th loop, 2nd shift generates 0x000a
Now, the values at the end of the 2nd shifts are XORed together.

The code is deliberately inefficient and shall stay that way. This function
is the root cause why the code shall be compiled without optimization. This
function not only acts as folding operation, but this function's execution
is used to measure the CPU execution time jitter. Any change to the loop in
this function implies that careful retesting must be done.



.. _`jent_fold_time.input`:

Input
-----

``ec`` entropy collector struct -- may be NULL
``time`` time stamp to be folded
``loop_cnt`` if a value not equal to 0 is set, use the given value as number of
loops to perform the folding



.. _`jent_fold_time.output`:

Output
------

``folded`` result of folding operation

``return`` Number of loops the folding operation is performed



.. _`jent_memaccess`:

jent_memaccess
==============

.. c:function:: unsigned int jent_memaccess (struct rand_data *ec, __u64 loop_cnt)

    - this is a noise source based on variations in memory access times

    :param struct rand_data \*ec:

        *undescribed*

    :param __u64 loop_cnt:

        *undescribed*



.. _`jent_memaccess.description`:

Description
-----------


This function performs memory accesses which will add to the timing
variations due to an unknown amount of CPU wait states that need to be
added when accessing memory. The memory size should be larger than the L1
caches as outlined in the documentation and the associated testing.

The L1 cache has a very high bandwidth, albeit its access rate is  usually
slower than accessing CPU registers. Therefore, L1 accesses only add minimal
variations as the CPU has hardly to wait. Starting with L2, significant
variations are added because L2 typically does not belong to the CPU any more
and therefore a wider range of CPU wait states is necessary for accesses.
L3 and real memory accesses have even a wider range of wait states. However,
to reliably access either L3 or memory, the ec->mem memory must be quite
large which is usually not desirable.



.. _`jent_memaccess.input`:

Input
-----

``ec`` Reference to the entropy collector with the memory access data -- if
the reference to the memory block to be accessed is NULL, this noise
source is disabled

``loop_cnt`` if a value not equal to 0 is set, use the given value as number of
loops to perform the folding

``return`` Number of memory access operations



.. _`jent_stuck`:

jent_stuck
==========

.. c:function:: void jent_stuck (struct rand_data *ec, __u64 current_delta)

    :param struct rand_data \*ec:

        *undescribed*

    :param __u64 current_delta:

        *undescribed*



.. _`jent_stuck.description`:

Description
-----------

1st derivation of the jitter measurement (time delta)
2nd derivation of the jitter measurement (delta of time deltas)
3rd derivation of the jitter measurement (delta of delta of time deltas)

All values must always be non-zero.



.. _`jent_stuck.input`:

Input
-----

``ec`` Reference to entropy collector
``current_delta`` Jitter time delta

``return``

        0 jitter measurement not stuck (good bit)
        1 jitter measurement stuck (reject bit)



.. _`jent_measure_jitter`:

jent_measure_jitter
===================

.. c:function:: __u64 jent_measure_jitter (struct rand_data *ec)

    :param struct rand_data \*ec:

        *undescribed*



.. _`jent_measure_jitter.description`:

Description
-----------

use the CPU jitter in the time deltas. The jitter is folded into one
bit. You can call this function the "random bit generator" as it
produces one random bit per invocation.



.. _`jent_measure_jitter.warning`:

WARNING
-------

ensure that ->prev_time is primed before using the output
of this function! This can be done by calling this function
and not using its result.



.. _`jent_measure_jitter.input`:

Input
-----

``entropy_collector`` Reference to entropy collector

``return`` One random bit



.. _`jent_unbiased_bit`:

jent_unbiased_bit
=================

.. c:function:: __u64 jent_unbiased_bit (struct rand_data *entropy_collector)

    :param struct rand_data \*entropy_collector:

        *undescribed*



.. _`jent_unbiased_bit.description`:

Description
-----------

documentation of that RNG, the bits from jent_measure_jitter are considered
independent which implies that the Von Neuman unbias operation is applicable.
A proof of the Von-Neumann unbias operation to remove skews is given in the
document "A proposal for: Functionality classes for random number
generators", version 2.0 by Werner Schindler, section 5.4.1.



.. _`jent_unbiased_bit.input`:

Input
-----

``entropy_collector`` Reference to entropy collector

``return`` One random bit



.. _`jent_stir_pool`:

jent_stir_pool
==============

.. c:function:: void jent_stir_pool (struct rand_data *entropy_collector)

    :param struct rand_data \*entropy_collector:

        *undescribed*



.. _`jent_stir_pool.description`:

Description
-----------

into the pool.

The function generates a mixer value that depends on the bits set and the
location of the set bits in the random number generated by the entropy
source. Therefore, based on the generated random number, this mixer value
can have 2**64 different values. That mixer value is initialized with the
first two SHA-1 constants. After obtaining the mixer value, it is XORed into
the random number.

The mixer value is not assumed to contain any entropy. But due to the XOR
operation, it can also not destroy any entropy present in the entropy pool.



.. _`jent_stir_pool.input`:

Input
-----

``entropy_collector`` Reference to entropy collector



.. _`jent_gen_entropy`:

jent_gen_entropy
================

.. c:function:: void jent_gen_entropy (struct rand_data *ec)

    :param struct rand_data \*ec:

        *undescribed*



.. _`jent_gen_entropy.description`:

Description
-----------

Function fills rand_data->data



.. _`jent_gen_entropy.input`:

Input
-----

``ec`` Reference to entropy collector



.. _`jent_fips_test`:

jent_fips_test
==============

.. c:function:: void jent_fips_test (struct rand_data *ec)

    2 -- the function automatically primes the test if needed.

    :param struct rand_data \*ec:

        *undescribed*



.. _`jent_fips_test.return`:

Return
------

0 if FIPS test passed
< 0 if FIPS test failed



.. _`jent_read_entropy`:

jent_read_entropy
=================

.. c:function:: int jent_read_entropy (struct rand_data *ec, unsigned char *data, unsigned int len)

    :param struct rand_data \*ec:

        *undescribed*

    :param unsigned char \*data:

        *undescribed*

    :param unsigned int len:

        *undescribed*



.. _`jent_read_entropy.description`:

Description
-----------


This function invokes the entropy gathering logic as often to generate
as many bytes as requested by the caller. The entropy gathering logic
creates 64 bit per invocation.

This function truncates the last 64 bit entropy value output to the exact
size specified by the caller.



.. _`jent_read_entropy.input`:

Input
-----

``ec`` Reference to entropy collector
``data`` pointer to buffer for storing random data -- buffer must already
exist

``len`` size of the buffer, specifying also the requested number of random
in bytes

``return`` 0 when request is fulfilled or an error



.. _`jent_read_entropy.the-following-error-codes-can-occur`:

The following error codes can occur
-----------------------------------

-1        entropy_collector is NULL

