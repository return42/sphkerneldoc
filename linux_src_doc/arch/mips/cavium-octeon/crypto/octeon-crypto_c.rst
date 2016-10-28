.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/crypto/octeon-crypto.c

.. _`octeon_crypto_enable`:

octeon_crypto_enable
====================

.. c:function:: unsigned long octeon_crypto_enable(struct octeon_cop2_state *state)

    crypto operations in calls to octeon_crypto_enable/disable in order to make sure the state of COP2 isn't corrupted if userspace is also performing hardware crypto operations. Allocate the state parameter on the stack. Returns with preemption disabled.

    :param struct octeon_cop2_state \*state:
        Pointer to state structure to store current COP2 state in.

.. _`octeon_crypto_enable.return`:

Return
------

Flags to be passed to \ :c:func:`octeon_crypto_disable`\ 

.. _`octeon_crypto_disable`:

octeon_crypto_disable
=====================

.. c:function:: void octeon_crypto_disable(struct octeon_cop2_state *state, unsigned long crypto_flags)

    called after an \ :c:func:`octeon_crypto_enable`\  before any context switch or return to userspace.

    :param struct octeon_cop2_state \*state:
        Pointer to COP2 state to restore

    :param unsigned long crypto_flags:
        *undescribed*

.. This file was automatic generated / don't edit.

