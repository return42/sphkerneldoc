.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/gaccess.h

.. _`kvm_s390_real_to_abs`:

kvm_s390_real_to_abs
====================

.. c:function:: unsigned long kvm_s390_real_to_abs(struct kvm_vcpu *vcpu, unsigned long gra)

    convert guest real address to guest absolute address \ ``vcpu``\  - guest virtual cpu \ ``gra``\  - guest real address

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param unsigned long gra:
        *undescribed*

.. _`kvm_s390_real_to_abs.description`:

Description
-----------

Returns the guest absolute address that corresponds to the passed guest real
address \ ``gra``\  of a virtual guest cpu by applying its prefix.

.. _`kvm_s390_logical_to_effective`:

kvm_s390_logical_to_effective
=============================

.. c:function:: unsigned long kvm_s390_logical_to_effective(struct kvm_vcpu *vcpu, unsigned long ga)

    convert guest logical to effective address

    :param struct kvm_vcpu \*vcpu:
        guest virtual cpu

    :param unsigned long ga:
        guest logical address

.. _`kvm_s390_logical_to_effective.description`:

Description
-----------

Convert a guest vcpu logical address to a guest vcpu effective address by
applying the rules of the vcpu's addressing mode defined by PSW bits 31
and 32 (extendended/basic addressing mode).

Depending on the vcpu's addressing mode the upper 40 bits (24 bit addressing
mode), 33 bits (31 bit addressing mode) or no bits (64 bit addressing mode)
of \ ``ga``\  will be zeroed and the remaining bits will be returned.

.. _`put_guest_lc`:

put_guest_lc
============

.. c:function::  put_guest_lc( vcpu,  x,  gra)

    write a simple variable to a guest vcpu's lowcore

    :param  vcpu:
        virtual cpu

    :param  x:
        value to copy to guest

    :param  gra:
        vcpu's destination guest real address

.. _`put_guest_lc.description`:

Description
-----------

Copies a simple value from kernel space to a guest vcpu's lowcore.
The size of the variable may be 1, 2, 4 or 8 bytes. The destination
must be located in the vcpu's lowcore. Otherwise the result is undefined.

Returns zero on success or -EFAULT on error.

.. _`put_guest_lc.note`:

Note
----

an error indicates that either the kernel is out of memory or
the guest memory mapping is broken. In any case the best solution
would be to terminate the guest.
It is wrong to inject a guest exception.

.. _`write_guest_lc`:

write_guest_lc
==============

.. c:function:: int write_guest_lc(struct kvm_vcpu *vcpu, unsigned long gra, void *data, unsigned long len)

    copy data from kernel space to guest vcpu's lowcore

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gra:
        vcpu's source guest real address

    :param void \*data:
        source address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`write_guest_lc.description`:

Description
-----------

Copy data from kernel space to guest vcpu's lowcore. The entire range must
be located within the vcpu's lowcore, otherwise the result is undefined.

Returns zero on success or -EFAULT on error.

.. _`write_guest_lc.note`:

Note
----

an error indicates that either the kernel is out of memory or
the guest memory mapping is broken. In any case the best solution
would be to terminate the guest.
It is wrong to inject a guest exception.

.. _`read_guest_lc`:

read_guest_lc
=============

.. c:function:: int read_guest_lc(struct kvm_vcpu *vcpu, unsigned long gra, void *data, unsigned long len)

    copy data from guest vcpu's lowcore to kernel space

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gra:
        vcpu's source guest real address

    :param void \*data:
        destination address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`read_guest_lc.description`:

Description
-----------

Copy data from guest vcpu's lowcore to kernel space. The entire range must
be located within the vcpu's lowcore, otherwise the result is undefined.

Returns zero on success or -EFAULT on error.

.. _`read_guest_lc.note`:

Note
----

an error indicates that either the kernel is out of memory or
the guest memory mapping is broken. In any case the best solution
would be to terminate the guest.
It is wrong to inject a guest exception.

.. _`write_guest`:

write_guest
===========

.. c:function:: int write_guest(struct kvm_vcpu *vcpu, unsigned long ga, ar_t ar, void *data, unsigned long len)

    copy data from kernel space to guest space

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long ga:
        guest address

    :param ar_t ar:
        access register

    :param void \*data:
        source address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`write_guest.description`:

Description
-----------

Copy \ ``len``\  bytes from \ ``data``\  (kernel space) to \ ``ga``\  (guest address).

.. _`write_guest.in-order-to-copy-data-to-guest-space-the-psw-of-the-vcpu-is-inspected`:

In order to copy data to guest space the PSW of the vcpu is inspected
---------------------------------------------------------------------

If DAT is off data will be copied to guest real or absolute memory.
If DAT is on data will be copied to the address space as specified by

.. _`write_guest.the-address-space-bits-of-the-psw`:

the address space bits of the PSW
---------------------------------

Primary, secondary, home space or access register mode.
The addressing mode of the PSW is also inspected, so that address wrap
around is taken into account for 24-, 31- and 64-bit addressing mode,
if the to be copied data crosses page boundaries in guest address space.
In addition also low address and DAT protection are inspected before
copying any data (key protection is currently not implemented).

This function modifies the 'struct kvm_s390_pgm_info pgm' member of \ ``vcpu``\ .
In case of an access exception (e.g. protection exception) pgm will contain
all data necessary so that a subsequent call to '\ :c:func:`kvm_s390_inject_prog_vcpu`\ '
will inject a correct exception into the guest.
If no access exception happened, the contents of pgm are undefined when
this function returns.

.. _`write_guest.return`:

Return
------

- zero on success
- a negative value if e.g. the guest mapping is broken or in
case of out-of-memory. In this case the contents of pgm are
undefined. Also parts of \ ``data``\  may have been copied to guest
space.
- a positive value if an access exception happened. In this case
the returned value is the program interruption code and the
contents of pgm may be used to inject an exception into the
guest. No data has been copied to guest space.

.. _`write_guest.note`:

Note
----

in case an access exception is recognized no data has been copied to
guest space (this is also true, if the to be copied data would cross
one or more page boundaries in guest space).
Therefore this function may be used for nullifying and suppressing
instruction emulation.
It may also be used for terminating instructions, if it is undefined
if data has been changed in guest space in case of an exception.

.. _`read_guest`:

read_guest
==========

.. c:function:: int read_guest(struct kvm_vcpu *vcpu, unsigned long ga, ar_t ar, void *data, unsigned long len)

    copy data from guest space to kernel space

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long ga:
        guest address

    :param ar_t ar:
        access register

    :param void \*data:
        destination address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`read_guest.description`:

Description
-----------

Copy \ ``len``\  bytes from \ ``ga``\  (guest address) to \ ``data``\  (kernel space).

The behaviour of read_guest is identical to write_guest, except that
data will be copied from guest space to kernel space.

.. _`read_guest_instr`:

read_guest_instr
================

.. c:function:: int read_guest_instr(struct kvm_vcpu *vcpu, void *data, unsigned long len)

    copy instruction data from guest space to kernel space

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param void \*data:
        destination address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`read_guest_instr.description`:

Description
-----------

Copy \ ``len``\  bytes from the current psw address (guest space) to \ ``data``\  (kernel
space).

The behaviour of read_guest_instr is identical to read_guest, except that
instruction data will be read from primary space when in home-space or
address-space mode.

.. _`write_guest_abs`:

write_guest_abs
===============

.. c:function:: int write_guest_abs(struct kvm_vcpu *vcpu, unsigned long gpa, void *data, unsigned long len)

    copy data from kernel space to guest space absolute

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gpa:
        guest physical (absolute) address

    :param void \*data:
        source address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`write_guest_abs.description`:

Description
-----------

Copy \ ``len``\  bytes from \ ``data``\  (kernel space) to \ ``gpa``\  (guest absolute address).
It is up to the caller to ensure that the entire guest memory range is
valid memory before calling this function.
Guest low address and key protection are not checked.

Returns zero on success or -EFAULT on error.

If an error occurs data may have been copied partially to guest memory.

.. _`read_guest_abs`:

read_guest_abs
==============

.. c:function:: int read_guest_abs(struct kvm_vcpu *vcpu, unsigned long gpa, void *data, unsigned long len)

    copy data from guest space absolute to kernel space

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gpa:
        guest physical (absolute) address

    :param void \*data:
        destination address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`read_guest_abs.description`:

Description
-----------

Copy \ ``len``\  bytes from \ ``gpa``\  (guest absolute address) to \ ``data``\  (kernel space).
It is up to the caller to ensure that the entire guest memory range is
valid memory before calling this function.
Guest key protection is not checked.

Returns zero on success or -EFAULT on error.

If an error occurs data may have been copied partially to kernel space.

.. _`write_guest_real`:

write_guest_real
================

.. c:function:: int write_guest_real(struct kvm_vcpu *vcpu, unsigned long gra, void *data, unsigned long len)

    copy data from kernel space to guest space real

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gra:
        guest real address

    :param void \*data:
        source address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`write_guest_real.description`:

Description
-----------

Copy \ ``len``\  bytes from \ ``data``\  (kernel space) to \ ``gra``\  (guest real address).
It is up to the caller to ensure that the entire guest memory range is
valid memory before calling this function.
Guest low address and key protection are not checked.

Returns zero on success or -EFAULT on error.

If an error occurs data may have been copied partially to guest memory.

.. _`read_guest_real`:

read_guest_real
===============

.. c:function:: int read_guest_real(struct kvm_vcpu *vcpu, unsigned long gra, void *data, unsigned long len)

    copy data from guest space real to kernel space

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gra:
        guest real address

    :param void \*data:
        destination address in kernel space

    :param unsigned long len:
        number of bytes to copy

.. _`read_guest_real.description`:

Description
-----------

Copy \ ``len``\  bytes from \ ``gra``\  (guest real address) to \ ``data``\  (kernel space).
It is up to the caller to ensure that the entire guest memory range is
valid memory before calling this function.
Guest key protection is not checked.

Returns zero on success or -EFAULT on error.

If an error occurs data may have been copied partially to kernel space.

.. This file was automatic generated / don't edit.

