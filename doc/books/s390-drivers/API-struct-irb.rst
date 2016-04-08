
.. _API-struct-irb:

==========
struct irb
==========

*man struct irb(9)*

*4.6.0-rc1*

interruption response block


Synopsis
========

.. code-block:: c

    struct irb {
      union scsw scsw;
      union esw;
      __u8 ecw[32];
    };


Members
=======

scsw
    subchannel status word

esw
    extended status word

ecw[32]
    extended control word


Description
===========

The irb that is handed to the device driver when an interrupt occurs. For solicited interrupts, the common I/O layer already performs checks whether a field is valid; a field not
being valid is always passed as ``0``. If a unit check occurred, ``ecw`` may contain sense data; this is retrieved by the common I/O layer itself if the device doesn't support
concurrent sense (so that the device driver never needs to perform basic sene itself). For unsolicited interrupts, the irb is passed as-is (expect for sense data, if applicable).
