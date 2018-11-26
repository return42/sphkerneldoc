.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/echo/oslec.h

.. _`oslec_create`:

oslec_create
============

.. c:function:: struct oslec_state *oslec_create(int len, int adaption_mode)

    Create a voice echo canceller context.

    :param len:
        The length of the canceller, in samples.
    :type len: int

    :param adaption_mode:
        *undescribed*
    :type adaption_mode: int

.. _`oslec_free`:

oslec_free
==========

.. c:function:: void oslec_free(struct oslec_state *ec)

    Free a voice echo canceller context.

    :param ec:
        The echo canceller context.
    :type ec: struct oslec_state \*

.. _`oslec_flush`:

oslec_flush
===========

.. c:function:: void oslec_flush(struct oslec_state *ec)

    Flush (reinitialise) a voice echo canceller context.

    :param ec:
        The echo canceller context.
    :type ec: struct oslec_state \*

.. _`oslec_adaption_mode`:

oslec_adaption_mode
===================

.. c:function:: void oslec_adaption_mode(struct oslec_state *ec, int adaption_mode)

    set the adaption mode of a voice echo canceller context. \ ``ec``\  The echo canceller context.

    :param ec:
        *undescribed*
    :type ec: struct oslec_state \*

    :param adaption_mode:
        The mode.
    :type adaption_mode: int

.. _`oslec_update`:

oslec_update
============

.. c:function:: int16_t oslec_update(struct oslec_state *ec, int16_t tx, int16_t rx)

    Process a sample through a voice echo canceller.

    :param ec:
        The echo canceller context.
    :type ec: struct oslec_state \*

    :param tx:
        The transmitted audio sample.
    :type tx: int16_t

    :param rx:
        The received audio sample.
    :type rx: int16_t

.. _`oslec_update.description`:

Description
-----------

The return value is the clean (echo cancelled) received sample.

.. _`oslec_hpf_tx`:

oslec_hpf_tx
============

.. c:function:: int16_t oslec_hpf_tx(struct oslec_state *ec, int16_t tx)

    Process to high pass filter the tx signal.

    :param ec:
        The echo canceller context.
    :type ec: struct oslec_state \*

    :param tx:
        The transmitted auio sample.
    :type tx: int16_t

.. _`oslec_hpf_tx.description`:

Description
-----------

The return value is the HP filtered transmit sample, send this to your D/A.

.. This file was automatic generated / don't edit.

