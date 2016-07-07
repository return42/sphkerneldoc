.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ipack/devices/ipoctal.h

.. _`ipoctal_stats`:

struct ipoctal_stats
====================

.. c:type:: struct ipoctal_stats

    - Stats since last reset

.. _`ipoctal_stats.definition`:

Definition
----------

.. code-block:: c

    struct ipoctal_stats {
        unsigned long tx;
        unsigned long rx;
        unsigned long overrun_err;
        unsigned long parity_err;
        unsigned long framing_err;
        unsigned long rcv_break;
    }

.. _`ipoctal_stats.members`:

Members
-------

tx
    Number of transmitted bytes

rx
    Number of received bytes

overrun_err
    *undescribed*

parity_err
    Number of parity errors

framing_err
    Number of framing errors

rcv_break
    Number of break received

.. This file was automatic generated / don't edit.

