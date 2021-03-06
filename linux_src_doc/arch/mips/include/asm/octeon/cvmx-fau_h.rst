.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-fau.h

.. _`cvmx_fau_tagwait64_t`:

typedef cvmx_fau_tagwait64_t
============================

.. c:type:: typedef cvmx_fau_tagwait64_t

    bit will be set. Otherwise the value of the register before the update will be returned.

.. _`cvmx_fau_tagwait32_t`:

typedef cvmx_fau_tagwait32_t
============================

.. c:type:: typedef cvmx_fau_tagwait32_t

    bit will be set. Otherwise the value of the register before the update will be returned.

.. _`cvmx_fau_tagwait16_t`:

typedef cvmx_fau_tagwait16_t
============================

.. c:type:: typedef cvmx_fau_tagwait16_t

    bit will be set. Otherwise the value of the register before the update will be returned.

.. _`cvmx_fau_tagwait8_t`:

typedef cvmx_fau_tagwait8_t
===========================

.. c:type:: typedef cvmx_fau_tagwait8_t

    bit will be set. Otherwise the value of the register before the update will be returned.

.. _`cvmx_fau_async_tagwait_result_t`:

typedef cvmx_fau_async_tagwait_result_t
=======================================

.. c:type:: typedef cvmx_fau_async_tagwait_result_t

    the error bit will be set. Otherwise the value of the register before the update will be returned.

.. _`__cvmx_fau_store_address`:

\__cvmx_fau_store_address
=========================

.. c:function:: uint64_t __cvmx_fau_store_address(uint64_t noadd, uint64_t reg)

    :param noadd:
        0 = Store value is atomically added to the current value
        1 = Store value is atomically written over the current value
    :type noadd: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
        - Step by 4 for 32 bit access.
        - Step by 8 for 64 bit access.
        Returns Address to store for atomic update
    :type reg: uint64_t

.. _`__cvmx_fau_atomic_address`:

\__cvmx_fau_atomic_address
==========================

.. c:function:: uint64_t __cvmx_fau_atomic_address(uint64_t tagwait, uint64_t reg, int64_t value)

    :param tagwait:
        Should the atomic add wait for the current tag switch
        operation to complete.
        - 0 = Don't wait
        - 1 = Wait for tag switch to complete
    :type tagwait: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
        - Step by 4 for 32 bit access.
        - Step by 8 for 64 bit access.
    :type reg: uint64_t

    :param value:
        Signed value to add.
        Note: When performing 32 and 64 bit access, only the low
        22 bits are available.
        Returns Address to read from for atomic update
    :type value: int64_t

.. _`cvmx_fau_fetch_and_add64`:

cvmx_fau_fetch_and_add64
========================

.. c:function:: int64_t cvmx_fau_fetch_and_add64(cvmx_fau_reg_64_t reg, int64_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 8 for 64 bit access.
    :type reg: cvmx_fau_reg_64_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns Value of the register before the update
    :type value: int64_t

.. _`cvmx_fau_fetch_and_add32`:

cvmx_fau_fetch_and_add32
========================

.. c:function:: int32_t cvmx_fau_fetch_and_add32(cvmx_fau_reg_32_t reg, int32_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 4 for 32 bit access.
    :type reg: cvmx_fau_reg_32_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns Value of the register before the update
    :type value: int32_t

.. _`cvmx_fau_fetch_and_add16`:

cvmx_fau_fetch_and_add16
========================

.. c:function:: int16_t cvmx_fau_fetch_and_add16(cvmx_fau_reg_16_t reg, int16_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
    :type reg: cvmx_fau_reg_16_t

    :param value:
        Signed value to add.
        Returns Value of the register before the update
    :type value: int16_t

.. _`cvmx_fau_fetch_and_add8`:

cvmx_fau_fetch_and_add8
=======================

.. c:function:: int8_t cvmx_fau_fetch_and_add8(cvmx_fau_reg_8_t reg, int8_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
    :type reg: cvmx_fau_reg_8_t

    :param value:
        Signed value to add.
        Returns Value of the register before the update
    :type value: int8_t

.. _`cvmx_fau_tagwait_fetch_and_add64`:

cvmx_fau_tagwait_fetch_and_add64
================================

.. c:function:: cvmx_fau_tagwait64_t cvmx_fau_tagwait_fetch_and_add64(cvmx_fau_reg_64_t reg, int64_t value)

    completes

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 8 for 64 bit access.
    :type reg: cvmx_fau_reg_64_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns If a timeout occurs, the error bit will be set. Otherwise
        the value of the register before the update will be
        returned
    :type value: int64_t

.. _`cvmx_fau_tagwait_fetch_and_add32`:

cvmx_fau_tagwait_fetch_and_add32
================================

.. c:function:: cvmx_fau_tagwait32_t cvmx_fau_tagwait_fetch_and_add32(cvmx_fau_reg_32_t reg, int32_t value)

    completes

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 4 for 32 bit access.
    :type reg: cvmx_fau_reg_32_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns If a timeout occurs, the error bit will be set. Otherwise
        the value of the register before the update will be
        returned
    :type value: int32_t

.. _`cvmx_fau_tagwait_fetch_and_add16`:

cvmx_fau_tagwait_fetch_and_add16
================================

.. c:function:: cvmx_fau_tagwait16_t cvmx_fau_tagwait_fetch_and_add16(cvmx_fau_reg_16_t reg, int16_t value)

    completes

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
    :type reg: cvmx_fau_reg_16_t

    :param value:
        Signed value to add.
        Returns If a timeout occurs, the error bit will be set. Otherwise
        the value of the register before the update will be
        returned
    :type value: int16_t

.. _`cvmx_fau_tagwait_fetch_and_add8`:

cvmx_fau_tagwait_fetch_and_add8
===============================

.. c:function:: cvmx_fau_tagwait8_t cvmx_fau_tagwait_fetch_and_add8(cvmx_fau_reg_8_t reg, int8_t value)

    completes

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
    :type reg: cvmx_fau_reg_8_t

    :param value:
        Signed value to add.
        Returns If a timeout occurs, the error bit will be set. Otherwise
        the value of the register before the update will be
        returned
    :type value: int8_t

.. _`__cvmx_fau_iobdma_data`:

\__cvmx_fau_iobdma_data
=======================

.. c:function:: uint64_t __cvmx_fau_iobdma_data(uint64_t scraddr, int64_t value, uint64_t tagwait, cvmx_fau_op_size_t size, uint64_t reg)

    :param scraddr:
        Scratch pad byte address to write to.  Must be 8 byte aligned
    :type scraddr: uint64_t

    :param value:
        Signed value to add.
        Note: When performing 32 and 64 bit access, only the low
        22 bits are available.
    :type value: int64_t

    :param tagwait:
        Should the atomic add wait for the current tag switch
        operation to complete.
        - 0 = Don't wait
        - 1 = Wait for tag switch to complete
    :type tagwait: uint64_t

    :param size:
        The size of the operation:
        - CVMX_FAU_OP_SIZE_8  (0) = 8 bits
        - CVMX_FAU_OP_SIZE_16 (1) = 16 bits
        - CVMX_FAU_OP_SIZE_32 (2) = 32 bits
        - CVMX_FAU_OP_SIZE_64 (3) = 64 bits
    :type size: cvmx_fau_op_size_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
        - Step by 4 for 32 bit access.
        - Step by 8 for 64 bit access.
        Returns Data to write using cvmx_send_single
    :type reg: uint64_t

.. _`cvmx_fau_async_fetch_and_add64`:

cvmx_fau_async_fetch_and_add64
==============================

.. c:function:: void cvmx_fau_async_fetch_and_add64(uint64_t scraddr, cvmx_fau_reg_64_t reg, int64_t value)

    placed in the scratch memory at byte address scraddr.

    :param scraddr:
        Scratch memory byte address to put response in.
        Must be 8 byte aligned.
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 8 for 64 bit access.
    :type reg: cvmx_fau_reg_64_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns Placed in the scratch pad register
    :type value: int64_t

.. _`cvmx_fau_async_fetch_and_add32`:

cvmx_fau_async_fetch_and_add32
==============================

.. c:function:: void cvmx_fau_async_fetch_and_add32(uint64_t scraddr, cvmx_fau_reg_32_t reg, int32_t value)

    placed in the scratch memory at byte address scraddr.

    :param scraddr:
        Scratch memory byte address to put response in.
        Must be 8 byte aligned.
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 4 for 32 bit access.
    :type reg: cvmx_fau_reg_32_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns Placed in the scratch pad register
    :type value: int32_t

.. _`cvmx_fau_async_fetch_and_add16`:

cvmx_fau_async_fetch_and_add16
==============================

.. c:function:: void cvmx_fau_async_fetch_and_add16(uint64_t scraddr, cvmx_fau_reg_16_t reg, int16_t value)

    placed in the scratch memory at byte address scraddr.

    :param scraddr:
        Scratch memory byte address to put response in.
        Must be 8 byte aligned.
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
    :type reg: cvmx_fau_reg_16_t

    :param value:
        Signed value to add.
        Returns Placed in the scratch pad register
    :type value: int16_t

.. _`cvmx_fau_async_fetch_and_add8`:

cvmx_fau_async_fetch_and_add8
=============================

.. c:function:: void cvmx_fau_async_fetch_and_add8(uint64_t scraddr, cvmx_fau_reg_8_t reg, int8_t value)

    placed in the scratch memory at byte address scraddr.

    :param scraddr:
        Scratch memory byte address to put response in.
        Must be 8 byte aligned.
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
    :type reg: cvmx_fau_reg_8_t

    :param value:
        Signed value to add.
        Returns Placed in the scratch pad register
    :type value: int8_t

.. _`cvmx_fau_async_tagwait_fetch_and_add64`:

cvmx_fau_async_tagwait_fetch_and_add64
======================================

.. c:function:: void cvmx_fau_async_tagwait_fetch_and_add64(uint64_t scraddr, cvmx_fau_reg_64_t reg, int64_t value)

    switch completes.

    :param scraddr:
        Scratch memory byte address to put response in.  Must be
        8 byte aligned.  If a timeout occurs, the error bit (63)
        will be set. Otherwise the value of the register before
        the update will be returned
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 8 for 64 bit access.
    :type reg: cvmx_fau_reg_64_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns Placed in the scratch pad register
    :type value: int64_t

.. _`cvmx_fau_async_tagwait_fetch_and_add32`:

cvmx_fau_async_tagwait_fetch_and_add32
======================================

.. c:function:: void cvmx_fau_async_tagwait_fetch_and_add32(uint64_t scraddr, cvmx_fau_reg_32_t reg, int32_t value)

    switch completes.

    :param scraddr:
        Scratch memory byte address to put response in.  Must be
        8 byte aligned.  If a timeout occurs, the error bit (63)
        will be set. Otherwise the value of the register before
        the update will be returned
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 4 for 32 bit access.
    :type reg: cvmx_fau_reg_32_t

    :param value:
        Signed value to add.
        Note: Only the low 22 bits are available.
        Returns Placed in the scratch pad register
    :type value: int32_t

.. _`cvmx_fau_async_tagwait_fetch_and_add16`:

cvmx_fau_async_tagwait_fetch_and_add16
======================================

.. c:function:: void cvmx_fau_async_tagwait_fetch_and_add16(uint64_t scraddr, cvmx_fau_reg_16_t reg, int16_t value)

    switch completes.

    :param scraddr:
        Scratch memory byte address to put response in.  Must be
        8 byte aligned.  If a timeout occurs, the error bit (63)
        will be set. Otherwise the value of the register before
        the update will be returned
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
    :type reg: cvmx_fau_reg_16_t

    :param value:
        Signed value to add.
    :type value: int16_t

.. _`cvmx_fau_async_tagwait_fetch_and_add16.description`:

Description
-----------

Returns Placed in the scratch pad register

.. _`cvmx_fau_async_tagwait_fetch_and_add8`:

cvmx_fau_async_tagwait_fetch_and_add8
=====================================

.. c:function:: void cvmx_fau_async_tagwait_fetch_and_add8(uint64_t scraddr, cvmx_fau_reg_8_t reg, int8_t value)

    switch completes.

    :param scraddr:
        Scratch memory byte address to put response in.  Must be
        8 byte aligned.  If a timeout occurs, the error bit (63)
        will be set. Otherwise the value of the register before
        the update will be returned
    :type scraddr: uint64_t

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
    :type reg: cvmx_fau_reg_8_t

    :param value:
        Signed value to add.
    :type value: int8_t

.. _`cvmx_fau_async_tagwait_fetch_and_add8.description`:

Description
-----------

Returns Placed in the scratch pad register

.. _`cvmx_fau_atomic_add64`:

cvmx_fau_atomic_add64
=====================

.. c:function:: void cvmx_fau_atomic_add64(cvmx_fau_reg_64_t reg, int64_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 8 for 64 bit access.
    :type reg: cvmx_fau_reg_64_t

    :param value:
        Signed value to add.
    :type value: int64_t

.. _`cvmx_fau_atomic_add32`:

cvmx_fau_atomic_add32
=====================

.. c:function:: void cvmx_fau_atomic_add32(cvmx_fau_reg_32_t reg, int32_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 4 for 32 bit access.
    :type reg: cvmx_fau_reg_32_t

    :param value:
        Signed value to add.
    :type value: int32_t

.. _`cvmx_fau_atomic_add16`:

cvmx_fau_atomic_add16
=====================

.. c:function:: void cvmx_fau_atomic_add16(cvmx_fau_reg_16_t reg, int16_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
    :type reg: cvmx_fau_reg_16_t

    :param value:
        Signed value to add.
    :type value: int16_t

.. _`cvmx_fau_atomic_add8`:

cvmx_fau_atomic_add8
====================

.. c:function:: void cvmx_fau_atomic_add8(cvmx_fau_reg_8_t reg, int8_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
    :type reg: cvmx_fau_reg_8_t

    :param value:
        Signed value to add.
    :type value: int8_t

.. _`cvmx_fau_atomic_write64`:

cvmx_fau_atomic_write64
=======================

.. c:function:: void cvmx_fau_atomic_write64(cvmx_fau_reg_64_t reg, int64_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 8 for 64 bit access.
    :type reg: cvmx_fau_reg_64_t

    :param value:
        Signed value to write.
    :type value: int64_t

.. _`cvmx_fau_atomic_write32`:

cvmx_fau_atomic_write32
=======================

.. c:function:: void cvmx_fau_atomic_write32(cvmx_fau_reg_32_t reg, int32_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 4 for 32 bit access.
    :type reg: cvmx_fau_reg_32_t

    :param value:
        Signed value to write.
    :type value: int32_t

.. _`cvmx_fau_atomic_write16`:

cvmx_fau_atomic_write16
=======================

.. c:function:: void cvmx_fau_atomic_write16(cvmx_fau_reg_16_t reg, int16_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
        - Step by 2 for 16 bit access.
    :type reg: cvmx_fau_reg_16_t

    :param value:
        Signed value to write.
    :type value: int16_t

.. _`cvmx_fau_atomic_write8`:

cvmx_fau_atomic_write8
======================

.. c:function:: void cvmx_fau_atomic_write8(cvmx_fau_reg_8_t reg, int8_t value)

    :param reg:
        FAU atomic register to access. 0 <= reg < 2048.
    :type reg: cvmx_fau_reg_8_t

    :param value:
        Signed value to write.
    :type value: int8_t

.. This file was automatic generated / don't edit.

