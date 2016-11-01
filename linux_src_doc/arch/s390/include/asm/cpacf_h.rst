.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/cpacf.h

.. _`__cpacf_query`:

__cpacf_query
=============

.. c:function:: void __cpacf_query(unsigned int opcode, cpacf_mask_t *mask)

    check if a specific CPACF function is available

    :param unsigned int opcode:
        the opcode of the crypto instruction

    :param cpacf_mask_t \*mask:
        *undescribed*

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

    :param unsigned long func:
        the function code passed to KM; see CPACF_KM_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param u8 \*dest:
        address of destination memory area

    :param const u8 \*src:
        address of source memory area

    :param long src_len:
        length of src operand in bytes

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

    :param unsigned long func:
        the function code passed to KM; see CPACF_KMC_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param u8 \*dest:
        address of destination memory area

    :param const u8 \*src:
        address of source memory area

    :param long src_len:
        length of src operand in bytes

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

    :param unsigned long func:
        the function code passed to KM; see CPACF_KIMD_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param const u8 \*src:
        address of source memory area

    :param long src_len:
        length of src operand in bytes

.. _`cpacf_klmd`:

cpacf_klmd
==========

.. c:function:: void cpacf_klmd(unsigned long func, void *param, const u8 *src, long src_len)

    executes the KLMD (COMPUTE LAST MESSAGE DIGEST) instruction

    :param unsigned long func:
        the function code passed to KM; see CPACF_KLMD_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param const u8 \*src:
        address of source memory area

    :param long src_len:
        length of src operand in bytes

.. _`cpacf_kmac`:

cpacf_kmac
==========

.. c:function:: int cpacf_kmac(unsigned long func, void *param, const u8 *src, long src_len)

    executes the KMAC (COMPUTE MESSAGE AUTHENTICATION CODE) instruction

    :param unsigned long func:
        the function code passed to KM; see CPACF_KMAC_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param const u8 \*src:
        address of source memory area

    :param long src_len:
        length of src operand in bytes

.. _`cpacf_kmac.description`:

Description
-----------

Returns 0 for the query func, number of processed bytes for digest funcs

.. _`cpacf_kmctr`:

cpacf_kmctr
===========

.. c:function:: int cpacf_kmctr(unsigned long func, void *param, u8 *dest, const u8 *src, long src_len, u8 *counter)

    executes the KMCTR (CIPHER MESSAGE WITH COUNTER) instruction

    :param unsigned long func:
        the function code passed to KMCTR; see CPACF_KMCTR_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param u8 \*dest:
        address of destination memory area

    :param const u8 \*src:
        address of source memory area

    :param long src_len:
        length of src operand in bytes

    :param u8 \*counter:
        address of counter value

.. _`cpacf_kmctr.description`:

Description
-----------

Returns 0 for the query func, number of processed bytes for
encryption/decryption funcs

.. _`cpacf_ppno`:

cpacf_ppno
==========

.. c:function:: void cpacf_ppno(unsigned long func, void *param, u8 *dest, long dest_len, const u8 *seed, long seed_len)

    executes the PPNO (PERFORM PSEUDORANDOM NUMBER OPERATION) instruction

    :param unsigned long func:
        the function code passed to PPNO; see CPACF_PPNO_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

    :param u8 \*dest:
        address of destination memory area

    :param long dest_len:
        size of destination memory area in bytes

    :param const u8 \*seed:
        address of seed data

    :param long seed_len:
        size of seed data in bytes

.. _`cpacf_pcc`:

cpacf_pcc
=========

.. c:function:: void cpacf_pcc(unsigned long func, void *param)

    executes the PCC (PERFORM CRYPTOGRAPHIC COMPUTATION) instruction

    :param unsigned long func:
        the function code passed to PCC; see CPACF_KM_xxx defines

    :param void \*param:
        address of parameter block; see POP for details on each func

.. This file was automatic generated / don't edit.

