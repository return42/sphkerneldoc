.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/cpacf.h

.. _`__cpacf_query`:

\__cpacf_query
==============

.. c:function:: void __cpacf_query(unsigned int opcode, cpacf_mask_t *mask)

    check if a specific CPACF function is available

    :param opcode:
        the opcode of the crypto instruction
    :type opcode: unsigned int

    :param mask:
        *undescribed*
    :type mask: cpacf_mask_t \*

.. _`__cpacf_query.description`:

Description
-----------

Executes the query function for the given crypto instruction \ ``opcode``\ 
and checks if \ ``func``\  is available

Returns 1 if \ ``func``\  is available for \ ``opcode``\ , 0 otherwise

.. _`cpacf_km`:

cpacf_km
========

.. c:function:: int cpacf_km(unsigned long func, void *param, u8 *dest, const u8 *src, long src_len)

    executes the KM (CIPHER MESSAGE) instruction

    :param func:
        the function code passed to KM; see CPACF_KM_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param dest:
        address of destination memory area
    :type dest: u8 \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: long

.. _`cpacf_km.description`:

Description
-----------

Returns 0 for the query func, number of processed bytes for
encryption/decryption funcs

.. _`cpacf_kmc`:

cpacf_kmc
=========

.. c:function:: int cpacf_kmc(unsigned long func, void *param, u8 *dest, const u8 *src, long src_len)

    executes the KMC (CIPHER MESSAGE WITH CHAINING) instruction

    :param func:
        the function code passed to KM; see CPACF_KMC_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param dest:
        address of destination memory area
    :type dest: u8 \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: long

.. _`cpacf_kmc.description`:

Description
-----------

Returns 0 for the query func, number of processed bytes for
encryption/decryption funcs

.. _`cpacf_kimd`:

cpacf_kimd
==========

.. c:function:: void cpacf_kimd(unsigned long func, void *param, const u8 *src, long src_len)

    executes the KIMD (COMPUTE INTERMEDIATE MESSAGE DIGEST) instruction

    :param func:
        the function code passed to KM; see CPACF_KIMD_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: long

.. _`cpacf_klmd`:

cpacf_klmd
==========

.. c:function:: void cpacf_klmd(unsigned long func, void *param, const u8 *src, long src_len)

    executes the KLMD (COMPUTE LAST MESSAGE DIGEST) instruction

    :param func:
        the function code passed to KM; see CPACF_KLMD_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: long

.. _`cpacf_kmac`:

cpacf_kmac
==========

.. c:function:: int cpacf_kmac(unsigned long func, void *param, const u8 *src, long src_len)

    executes the KMAC (COMPUTE MESSAGE AUTHENTICATION CODE) instruction

    :param func:
        the function code passed to KM; see CPACF_KMAC_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: long

.. _`cpacf_kmac.description`:

Description
-----------

Returns 0 for the query func, number of processed bytes for digest funcs

.. _`cpacf_kmctr`:

cpacf_kmctr
===========

.. c:function:: int cpacf_kmctr(unsigned long func, void *param, u8 *dest, const u8 *src, long src_len, u8 *counter)

    executes the KMCTR (CIPHER MESSAGE WITH COUNTER) instruction

    :param func:
        the function code passed to KMCTR; see CPACF_KMCTR_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param dest:
        address of destination memory area
    :type dest: u8 \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: long

    :param counter:
        address of counter value
    :type counter: u8 \*

.. _`cpacf_kmctr.description`:

Description
-----------

Returns 0 for the query func, number of processed bytes for
encryption/decryption funcs

.. _`cpacf_prno`:

cpacf_prno
==========

.. c:function:: void cpacf_prno(unsigned long func, void *param, u8 *dest, unsigned long dest_len, const u8 *seed, unsigned long seed_len)

    executes the PRNO (PERFORM RANDOM NUMBER OPERATION) instruction

    :param func:
        the function code passed to PRNO; see CPACF_PRNO_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param dest:
        address of destination memory area
    :type dest: u8 \*

    :param dest_len:
        size of destination memory area in bytes
    :type dest_len: unsigned long

    :param seed:
        address of seed data
    :type seed: const u8 \*

    :param seed_len:
        size of seed data in bytes
    :type seed_len: unsigned long

.. _`cpacf_trng`:

cpacf_trng
==========

.. c:function:: void cpacf_trng(u8 *ucbuf, unsigned long ucbuf_len, u8 *cbuf, unsigned long cbuf_len)

    executes the TRNG subfunction of the PRNO instruction

    :param ucbuf:
        buffer for unconditioned data
    :type ucbuf: u8 \*

    :param ucbuf_len:
        amount of unconditioned data to fetch in bytes
    :type ucbuf_len: unsigned long

    :param cbuf:
        buffer for conditioned data
    :type cbuf: u8 \*

    :param cbuf_len:
        amount of conditioned data to fetch in bytes
    :type cbuf_len: unsigned long

.. _`cpacf_pcc`:

cpacf_pcc
=========

.. c:function:: void cpacf_pcc(unsigned long func, void *param)

    executes the PCC (PERFORM CRYPTOGRAPHIC COMPUTATION) instruction

    :param func:
        the function code passed to PCC; see CPACF_KM_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

.. _`cpacf_pckmo`:

cpacf_pckmo
===========

.. c:function:: void cpacf_pckmo(long func, void *param)

    executes the PCKMO (PERFORM CRYPTOGRAPHIC KEY MANAGEMENT) instruction

    :param func:
        the function code passed to PCKMO; see CPACF_PCKMO_xxx defines
    :type func: long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

.. _`cpacf_pckmo.description`:

Description
-----------

Returns 0.

.. _`cpacf_kma`:

cpacf_kma
=========

.. c:function:: void cpacf_kma(unsigned long func, void *param, u8 *dest, const u8 *src, unsigned long src_len, const u8 *aad, unsigned long aad_len)

    executes the KMA (CIPHER MESSAGE WITH AUTHENTICATION) instruction

    :param func:
        the function code passed to KMA; see CPACF_KMA_xxx defines
    :type func: unsigned long

    :param param:
        address of parameter block; see POP for details on each func
    :type param: void \*

    :param dest:
        address of destination memory area
    :type dest: u8 \*

    :param src:
        address of source memory area
    :type src: const u8 \*

    :param src_len:
        length of src operand in bytes
    :type src_len: unsigned long

    :param aad:
        address of additional authenticated data memory area
    :type aad: const u8 \*

    :param aad_len:
        length of aad operand in bytes
    :type aad_len: unsigned long

.. This file was automatic generated / don't edit.

